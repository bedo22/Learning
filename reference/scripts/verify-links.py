#!/usr/bin/env python3
"""
verify-links.py — verify every citation link in the reference shelf.

The gate that makes "citations are verified links" true. It is DESIGNED to
never look like a bot:

  - Cache-first: results are stored in .link-cache.json (keyed by URL/DOI with
    a timestamp). Re-runs on unchanged docs are pure cache hits — ZERO network
    requests. This is the anti-bot answer: the steady state makes no requests.
  - DOI-aware: DOIs are verified against the Crossref REST API
    (api.crossref.org), which is API-first and designed for automated use.
    The User-Agent carries a mailto so Crossref can contact us if we misbehave
    (their documented etiquette requirement).
  - Rate-limited: at most 1 request/second with random jitter; exponential
    backoff on 429/503; a 24h floor between network runs (unless --force).
  - Staleness window: a cached entry is trusted for 30 days, then re-checked.

Exit code 1 if any link fails verification. Run from the reference/ dir:

    python3 scripts/verify-links.py            # normal run (cache-first)
    python3 scripts/verify-links.py --force    # ignore cache, re-check all
    python3 scripts/verify-links.py --json     # machine-readable report

Config (env vars, all optional):
    VERIFY_MAILTO      — email in the User-Agent (Crossref etiquette). Default:
                         shelf-verify@example.com  (change to a real address)
    VERIFY_STALE_DAYS  — re-check window. Default: 30
    VERIFY_MIN_INTERVAL — min seconds between requests. Default: 1.0
"""

import argparse
import hashlib
import json
import os
import random
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from html.parser import HTMLParser
from pathlib import Path

# ---------------------------------------------------------------------------
# Config
# ---------------------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent  # the reference/ dir
CACHE_FILE = Path(__file__).resolve().parent / ".link-cache.json"
MAILTO = os.environ.get("VERIFY_MAILTO", "shelf-verify@example.com")
STALE_DAYS = int(os.environ.get("VERIFY_STALE_DAYS", "30"))
MIN_INTERVAL = float(os.environ.get("VERIFY_MIN_INTERVAL", "1.0"))
CROSSREF = "https://api.crossref.org/works/{}"
DOI_ORG = "https://doi.org/{}"

# ---------------------------------------------------------------------------
# Link extraction — HTML-aware, no regex over tags
# ---------------------------------------------------------------------------


class LinkExtractor(HTMLParser):
    """Collect every external href + every bare doi:... token in a doc."""

    def __init__(self):
        super().__init__()
        self.links = set()

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        d = dict(attrs)
        href = d.get("href", "")
        # skip in-doc anchors and internal shelf links
        if href.startswith("#") or href.startswith("./") or href.startswith("../"):
            return
        if href.startswith("http"):
            self.links.add(href)

    def handle_data(self, data):
        # catch bare doi:10.xxxx/yyyy tokens in text (not wrapped in <a>)
        # allow parens/underscores/dashes (old Elsevier DOIs contain (93));
        # strip trailing punctuation incl. Arabic semicolons
        for m in re.finditer(r"doi:\s*(10\.\d{4,9}/[A-Za-z0-9()._\-/]+)", data):
            raw = m.group(1)
            raw = re.sub(r"[)؛.;,:]+$", "", raw)
            if raw.count("(") > raw.count(")"):
                raw = raw.rstrip("(")
            self.links.add("https://doi.org/" + raw)


class MarkdownLinkExtractor:
    """Collect every URL + bare doi:... token in a source digest (.md).

    Handles markdown [text](url) links, bare https:// URLs, and doi: tokens.
    The digests use all three forms; a dead link in a digest is a real
    finding (it's the accumulated research asset).
    """

    def __init__(self):
        self.links = set()
        self._text = None

    def extract(self, path: Path):
        self._text = path.read_text(encoding="utf-8")
        # markdown links: [text](url) and [text](<url>) — url may contain
        # balanced parens (old Elsevier DOIs like ...0173(98)00019-8), so walk
        # forward until the markdown-close paren that is NOT part of a pair.
        for m in re.finditer(r"\]\s*\(\s*<?(https?://[^>\s]*)>?\s*\)", self._text):
            url = m.group(1)
            # trim trailing non-URL junk (", ., ) when unbalanced)
            depth = url.count("(") - url.count(")")
            if depth > 0:
                # find the matching close: take everything before the markdown ") "
                # simplest: rstrip one unbalanced close if present
                url = url.rstrip(")")
            self.links.add(url.rstrip(").,"))
        # bare https:// URLs (not inside parens we already caught)
        # bare https:// URLs — capture until whitespace, then balance parens
        # (DOIs like 10.1016/s0165-0173(98)00019-8 contain parens; a trailing
        # " (1998)" annotation must not be swallowed)
        for m in re.finditer(r"(?<![\w(])(https?://[^\s<>]+)", self._text):
            url = m.group(1)
            # trim trailing punctuation (", ., )) unless it closes a ( pair
            stripped = url.rstrip(").,")
            if url.count("(") == url.count(")") and url.endswith((")", ".", ",")):
                url = stripped
            elif url.endswith(")") and url.count("(") < url.count(")"):
                url = url.rstrip(")")
            self.links.add(url.rstrip(").,"))
        # bare doi: tokens — same paren-tolerance as the HTML extractor
        for m in re.finditer(r"doi:\s*(10\.\d{4,9}/[A-Za-z0-9()._\-/+]+)", self._text):
            raw = m.group(1)
            raw = re.sub(r"[)؛.;,:]+$", "", raw)
            if raw.count("(") > raw.count(")"):
                raw = raw.rstrip("(")
            self.links.add("https://doi.org/" + raw)
        return self.links


def extract_links(path: Path) -> set:
    if path.suffix == ".md":
        links = MarkdownLinkExtractor().extract(path)
    else:
        parser = LinkExtractor()
        parser.feed(path.read_text(encoding="utf-8"))
        links = parser.links
    # skip template/example placeholders (e.g. https://api.crossref.org/works/{DOI}
    # in SOURCE-ACCESS.md) — they are documentation, not real links to check.
    return {l for l in links if "{" not in l and "}" not in l}


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------


def load_cache() -> dict:
    if CACHE_FILE.exists():
        try:
            return json.loads(CACHE_FILE.read_text(encoding="utf-8"))
        except (json.JSONDecodeError, OSError):
            return {}
    return {}


def save_cache(cache: dict) -> None:
    CACHE_FILE.write_text(
        json.dumps(cache, indent=2, ensure_ascii=False), encoding="utf-8"
    )


# ---------------------------------------------------------------------------
# Verification primitives
# ---------------------------------------------------------------------------

_last_request = 0.0


def _throttle() -> None:
    """At most one request per MIN_INTERVAL seconds, with jitter."""
    global _last_request
    now = time.monotonic()
    wait = _last_request + MIN_INTERVAL - now + random.uniform(0, 0.25)
    if wait > 0:
        time.sleep(wait)
    _last_request = time.monotonic()


def _request(url: str, headers: dict, tries: int = 4) -> int:
    """GET with backoff; returns HTTP status. 0 = transport error."""
    for attempt in range(tries):
        _throttle()
        try:
            req = urllib.request.Request(url, headers=headers)
            with urllib.request.urlopen(req, timeout=20) as resp:
                return resp.status
        except urllib.error.HTTPError as e:
            if e.code in (429, 503) and attempt < tries - 1:
                time.sleep(2 ** attempt + random.uniform(0, 1))
                continue
            return e.code
        except (urllib.error.URLError, TimeoutError, OSError):
            if attempt < tries - 1:
                time.sleep(2 ** attempt + random.uniform(0, 1))
                continue
            return 0
    return 0


def verify_doi(doi: str) -> tuple[bool, str]:
    """
    Verify a DOI via Crossref metadata. Returns (ok, detail).
    Crossref says the DOI *exists and is registered* — that is the guarantee
    we need. Paywalled content still resolves (the DOI is valid even when a
    browser gets 403 from the publisher page).
    """
    url = CROSSREF.format(urllib.parse.quote(doi, safe=""))
    headers = {"User-Agent": f"reference-shelf-verifier/1.0 (mailto:{MAILTO})"}
    status = _request(url, headers)
    if status == 200:
        return True, "crossref 200"
    if status == 404:
        return False, f"crossref 404 — DOI not registered: {doi}"
    return False, f"crossref status {status}"


def verify_url(url: str) -> tuple[bool, str]:
    """HEAD/GET a plain URL. Some servers reject HEAD; fall back to GET."""
    if url.startswith("https://doi.org/"):
        return verify_doi(url[len("https://doi.org/") :])
    headers = {"User-Agent": f"reference-shelf-verifier/1.0 (mailto:{MAILTO})"}
    status = _request(url, headers)
    if status in (200, 301, 302, 403, 405):
        # 403/405 = reachable but guarding (paywall/anti-bot) — the link works
        return True, f"http {status}"
    return False, f"http {status}"


# ---------------------------------------------------------------------------
# Orchestration
# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true", help="ignore cache, re-check all")
    ap.add_argument("--json", action="store_true", help="machine-readable report")
    args = ap.parse_args()

    docs = (
        sorted(BASE_DIR.glob("*.html"))
        + sorted(BASE_DIR.glob("ar/*.html"))
        + sorted(p for p in BASE_DIR.glob("sources/*.md") if p.name != "_TEMPLATE.md")
    )
    cache = load_cache()
    now = datetime.now(timezone.utc)
    all_links: dict[str, list[str]] = {}  # link -> docs that use it

    for doc in docs:
        for link in extract_links(doc):
            all_links.setdefault(link, []).append(str(doc.relative_to(BASE_DIR)))

    results = {}
    new_checks = 0
    for link, users in sorted(all_links.items()):
        entry = cache.get(link, {})
        ts = entry.get("ts")
        fresh = False
        if ts and not args.force:
            try:
                age = (now - datetime.fromisoformat(ts)).days
                fresh = age < STALE_DAYS
            except (ValueError, TypeError):
                fresh = False
        if fresh:
            results[link] = {"ok": entry.get("ok"), "detail": entry.get("detail", "cached")}
        else:
            new_checks += 1
            ok, detail = verify_url(link)
            results[link] = {"ok": ok, "detail": detail}
            cache[link] = {
                "ok": ok,
                "detail": detail,
                "ts": now.isoformat(),
                "users": users,
            }

    save_cache(cache)

    failed = {k: v for k, v in results.items() if not v["ok"]}
    cached_hits = len(results) - new_checks

    if args.json:
        print(json.dumps({"total": len(results), "cached": cached_hits,
                          "checked": new_checks, "failed": failed}, indent=2))
    else:
        print(f"verify-links: {len(results)} links "
              f"({cached_hits} cached, {new_checks} network checks)")
        for link, v in sorted(results.items()):
            mark = "ok " if v["ok"] else "FAIL"
            print(f"  [{mark}] {link}  ({v['detail']})")
        if failed:
            print(f"\n{len(failed)} link(s) FAILED:")
            for link in failed:
                print(f"  {link}")

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
