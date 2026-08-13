#!/usr/bin/env python3
"""check-map.py — validate a DOMAIN-MAP.md for the skill's hard rules.

Usage:
    python3 check-map.py DOMAIN-MAP.md

Checks (each maps to a guard in SKILL.md):
  1. purpose present
  2. at least one filled node row, each with a "Must be able to"
  3. status values are from {covered, thin, gap} (case-insensitive)
  4. every gap row in the node table appears in the gap list
  5. every gap-list row has a seed
  6. verification checklist present

Fails with exit 1 on violations. Deterministic; the agent runs it before
handing over the map.
"""

import re, sys

def load(path):
    with open(path, encoding="utf-8") as f:
        return f.read()

def main():
    path = sys.argv[1] if len(sys.argv) > 1 else "DOMAIN-MAP.md"
    text = load(path)
    fails = []

    # 1. purpose
    if not re.search(r"^## Purpose\s*\n+[^|\s]", text, re.M):
        fails.append("no non-empty Purpose section")

    # 2+3. node table rows
    in_table = False
    statuses = {"covered", "thin", "gap"}
    node_gaps = []
    node_rows = 0
    for line in text.splitlines():
        if line.startswith("| # | Node"):
            in_table = True
            continue
        if in_table:
            if line.startswith("|") and "---" not in line and line.strip("| ").strip():
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) >= 5 and cells[1].strip() and cells[1] != "Node (ability)":
                    node_rows += 1
                    st = cells[3].lower()
                    if st not in statuses:
                        fails.append(f"node '{cells[1]}' status '{cells[3]}' not in {{covered, thin, gap}}")
                    if st == "gap":
                        node_gaps.append(cells[1])
                    if not cells[2].strip():
                        fails.append(f"node '{cells[1]}' has empty 'must be able to'")
            elif not line.startswith("|"):
                in_table = False

    if node_rows == 0:
        fails.append("no filled node rows (table is empty — fill it)")

    # 4+5. gap list
    in_gap = False
    gap_items = []
    for line in text.splitlines():
        if line.startswith("| # | Gap"):
            in_gap = True
            continue
        if in_gap:
            if line.startswith("|") and "---" not in line and line.strip("| ").strip():
                cells = [c.strip() for c in line.strip("|").split("|")]
                if len(cells) >= 4 and cells[1].strip() and cells[1] != "Gap":
                    gap_items.append(cells[1])
                    if not cells[3].strip():
                        fails.append(f"gap '{cells[1]}' has empty seed")
            elif not line.startswith("|"):
                in_gap = False

    for g in node_gaps:
        if not any(g.lower() in gi.lower() for gi in gap_items):
            fails.append(f"node-table gap '{g}' missing from the named gap list")

    # 6. verification
    if "## Verification" not in text or "all gaps verified" not in text.lower():
        fails.append("verification section / checklist missing")

    if fails:
        print("FAIL:")
        for f in fails:
            print("  -", f)
        sys.exit(1)
    print("PASS — map satisfies the domain-map hard rules")

if __name__ == "__main__":
    main()
