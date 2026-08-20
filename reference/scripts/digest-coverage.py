#!/usr/bin/env python3
"""Digest-coverage report: which citations have source digests and which don't.

Scans every shelf doc's <span class="cite"> blocks and reports:
  - per doc: cite blocks total / with 📄 digest links / without
  - digests in sources/ never linked from any doc (orphans)
Exit 0 = every cite block carries at least one digest link.

Usage: python3 scripts/digest-coverage.py [--json]
"""
import re, sys, json, glob, os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = sorted(glob.glob(os.path.join(ROOT, "*.html")))
AR_DOCS = sorted(glob.glob(os.path.join(ROOT, "ar", "*.html")))

def scan(path):
    t = open(path, encoding="utf-8").read()
    spans = re.findall(r'<span class="cite"[^>]*>(.*?)</span>', t, re.S)
    rows = []
    for s in spans:
        txt = re.sub(r"<[^>]+>", "", s)
        links = re.findall(r'href="(?:\.\./)?sources/([^"#]+\.md)"', s)
        # split into cited segments on the separator
        segs = [x.strip() for x in re.split(r"&nbsp;·&nbsp;|·", txt) if x.strip()]
        rows.append({"segments": len(segs), "digest_links": links,
                     "covered": bool(links)})
    return rows

def main():
    as_json = "--json" in sys.argv
    report, fail = {}, False
    all_linked = set()
    for path in DOCS + AR_DOCS:
        rel = os.path.relpath(path, ROOT)
        rows = scan(path)
        no_cov = [r for r in rows if not r["covered"]]
        for r in rows:
            all_linked.update(r["digest_links"])
        report[rel] = {"cite_blocks": len(rows),
                       "with_digests": len(rows) - len(no_cov),
                       "without": len(no_cov)}
        if no_cov:
            fail = True
            report[rel]["uncovered_segments"] = [
                r["segments"] for r in no_cov][:5]
    used = {os.path.basename(x) for x in all_linked}
    have = {os.path.basename(p) for p in glob.glob(os.path.join(ROOT, "sources", "*.md"))
            if not os.path.basename(p).startswith(("_", "SOURCE", "TEMPLATE"))}
    orphans = sorted(have - used)
    report["_summary"] = {
        "docs_scanned": len(DOCS) + len(AR_DOCS),
        "digest_files": len(have),
        "digest_files_linked": len(used & have),
        "orphan_digests": orphans,
    }
    if as_json:
        print(json.dumps(report, indent=2, ensure_ascii=False))
    else:
        print(f"{'doc':52} {'cites':>6} {'linked':>7} {'missing':>8}")
        for k, v in report.items():
            if k.startswith("_"):
                continue
            mark = "" if v["without"] == 0 else "  <-- UNCOVERED"
            print(f"{k[:52]:52} {v['cite_blocks']:>6} {v['with_digests']:>7} {v['without']:>8}{mark}")
        s = report["_summary"]
        print(f"\ndigest files: {s['digest_files']} | linked somewhere: {s['digest_files_linked']}")
        print("orphan digests (never linked):", ", ".join(s["orphan_digests"]) or "none")
        print("EXIT:", "FAIL" if fail else "OK")
    sys.exit(1 if fail else 0)

if __name__ == "__main__":
    main()
