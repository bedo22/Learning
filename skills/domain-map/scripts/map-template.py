#!/usr/bin/env python3
"""map-template.py — generate a blank DOMAIN-MAP.md skeleton.

Usage:
    python3 map-template.py <territory> [--purpose "one-line purpose"] [--out DOMAIN-MAP.md]

Produces the node table + gap list skeleton. The agent fills the rows; the
script only removes the typing of boilerplate. Deterministic, idempotent
(overwrites with a fresh skeleton; re-running after filling would clobber —
pass --out to a new file if you want to keep a filled map).
"""

import argparse, datetime

TEMPLATE = """# DOMAIN-MAP — {territory}

> A map is a snapshot. Re-derive the model from purpose on the next visit —
> never patch. (domain-map skill, REFERENCE.md)

## Purpose

{PURPOSE_LINE}

## Node table

| # | Node (ability) | Must be able to | Status (covered/thin/gap) | Evidence |
|---|---|---|---|---|
| 1 |  |  |  |  |
| 2 |  |  |  |  |

Status legend: **covered** = can do it cold · **thin** = heard of it / passing
mention · **gap** = nothing there. "Covered" means *can do*, not *knows of*.

## The named gap list (the deliverable)

Ranked by leverage on the purpose. Each gap: what it is · why it matters ·
first seed (search query / book / course).

| # | Gap | Why it matters (leverage) | First seed |
|---|---|---|---|
| 1 |  |  |  |
| 2 |  |  |  |

## Verification

Every gap confirmed against ≥1 external authority (web search / curriculum /
textbook / expert). Label evidence: canonical · corroborated · single-source.

- [ ] All gaps verified
- [ ] Nodes are abilities, not topics
- [ ] Model derived from purpose, not from existing materials

---
_Re-derivation date: {date}_
"""

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("territory")
    p.add_argument("--purpose", default="", help="one-line purpose statement")
    p.add_argument("--out", default="DOMAIN-MAP.md")
    a = p.parse_args()
    purpose = a.purpose.strip()
    purpose_line = purpose or "(one line: what must the user be able to DO, and in what contexts?)"
    text = TEMPLATE.format(
        territory=a.territory,
        PURPOSE_LINE=purpose_line,
        date=datetime.date.today().isoformat(),
    )
    with open(a.out, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {a.out}")

if __name__ == "__main__":
    main()
