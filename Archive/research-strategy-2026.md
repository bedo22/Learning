# Research Strategy — Learn to Learn Shelf (2026 pass)

Date: 2026-08-13 · Status: plan (execution in `learning-science-research-2026.md`) · Scope: the 17-doc reference shelf + lessons

## The question: last 15 years, or all landmarks from the beginning?

**Short answer: both, but in two layers with different roles — and the deciding rule is "does a doc's claim already rest on this paper without citing it?", not the publication year.**

### Why not "only the last 15 years"
The shelf already has strong recent coverage (2010–2026: the previous `learning-science-papers-2010-2026.md` survey was applied to the docs; the citation histogram shows 2021–2026 densely populated). A 2010–2026-only strategy would re-verify what's already there and miss the *foundations* the docs' core claims are built on but never name:

- memory-techniques teaches "increase complexity" (= **levels of processing**) and the "weight limit" (= the **working-memory model**) without citing Craik & Lockhart 1972 or Baddeley & Hitch 1974.
- learning-system teaches "match your cues to reality" (= **encoding specificity**) without citing Tulving & Thomson 1973.
- metacognition-and-calibration teaches monitoring/control — the field's founding paper (Flavell 1979) is never cited.
- study-advice/memory teach "test yourself" — the **origin** of the testing effect (Roediger & Karpicke 2006) is never cited (only the 2011 and later meta-analyses are).
- self-management teaches procrastination management with **no procrastination citation at all** (Steel 2007 is the canonical meta-analysis).
- skill-acquisition cites Hattie & Timperley 2007 but not the field's modern update (Wisniewski et al. 2020, ~2,000 effects).
- wanting-vs-liking cites ego-depletion as established fact ("suppression produces ego depletion") — a claim the preregistered multilab replication (Hagger et al. 2016) directly contests. This is a *contradiction risk*, the research equivalent of a bug.

These are not "nice-to-have history" — they are the papers the docs' own arguments are restatements of. A reader of the shelf should be able to trace "increase complexity" to the theory it came from.

### Why not "everything from the beginning"
The shelf is a practical teaching system, not a history of psychology. Papers from before ~1970 that are superseded or not load-bearing for the docs' claims (e.g. Ebbinghaus's raw method, the modal model debates) add noise. Ebbinghaus 1885 and Miller 1956 are already cited where needed. The rule is **claim-anchored**: only add a paper if (a) a doc makes a claim that is best sourced to it, and (b) the doc doesn't already cite it or cites only a derivative.

### The decision
**Two layers, claim-anchored:**

1. **Landmark layer (pre-2010):** the canonical papers that the docs' claims rest on but never cite. Target: the 8 gaps found in the audit (above) + any discovered during execution.
2. **Recent layer (2010–2026):** already largely done. Extend only where the audit found specific missing updates (Wisniewski 2020 feedback meta; Hagger 2016 ego-depletion replication) — and treat any recent paper that *contradicts* a cited claim as a first-class finding (contradiction > addition).

## Topics (mapped to docs)

| Topic | Doc(s) that own the claim | Landmark target | Recent target |
|---|---|---|---|
| Memory: levels of processing | memory-techniques §increase complexity | Craik & Lockhart 1972 | — |
| Memory: working-memory model | memory-techniques §how memory works | Baddeley & Hitch 1974 | — |
| Memory/retrieval: encoding specificity | learning-system §retrieval method | Tulving & Thomson 1973 | — |
| Testing effect (origin) | study-advice, memory-techniques | Roediger & Karpicke 2006 | — |
| Metacognition (origin) | metacognition-and-calibration | Flavell 1979 | — |
| Procrastination | self-management | Steel 2007 | — |
| Feedback | skill-acquisition | (Hattie & Timperley 2007 already cited) | Wisniewski, Zierer & Hattie 2020 |
| Wanting/self-control | wanting-vs-liking §sec-urge | (Baumeister lineage present) | Hagger et al. 2016 (replication — contradiction check) |

## Verification protocol (same as the previous survey)

- Every paper checked against a primary source (journal page, publisher record, DOI, PubMed) during execution — no citing from memory.
- Record the exact venue, year, volume/pages, and DOI.
- Flag "already cited" entries so the reader knows the shelf's current state.
- Flag correlational/null findings explicitly (Hagger 2016 is a *null* result — it doesn't kill the suppression-backfire argument, it refines the *mechanism*: the cost is rebound + reactance, not a depletable resource).

## Exclusion rules

- No pop-psychology, no self-help citations.
- No papers that merely re-state what's already cited without adding evidence or correcting it.
- No single-study results where a meta-analysis exists and is already cited.
- Caveats are mandatory for replications, correlational studies, and null results.

## Output

1. `Archive/learning-science-research-2026.md` — the results (verified entries, gap status before/after).
2. Apply to the docs: add the landmark citations at the exact claims they anchor; fix the ego-depletion overclaim in wanting-vs-liking (both twins).
3. Update the deep analysis with the new state.
