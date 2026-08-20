# Glossary design analysis — `learning-to-learn-glossary.html`

Measured state (August 2026): **108 entries**, one flat `<dl>`, ~36 words/entry,
~4,500 words total, ordered by source-doc sequence (Ref 01 → 20). Arabic twin
exists and passes twin gates.

## Findings (ranked by reader impact)

### F1 · It is a wall with no doors — no grouping, no anchors
Zero `<h2>` group headers and **zero `id` attributes on any `<dt>`**. A reader
landing mid-page cannot tell which doc's vocabulary they're in, and no other
doc can deep-link to a term (`glossary.html#term` resolves nowhere). The shelf's
docs all link the glossary generically; none link a specific term because they
can't.

### F2 · Cross-linking is asymmetric
Entries for the early docs (Bloom's levels, learning-system core, orders,
self-management) carry **0 links** to their defining documents; later entries
(wanting-vs-liking onward) carry 1–3. Roughly 30 of 108 entries are orphaned —
the glossary doesn't lead back to the shelf.

### F3 · Recent shelf concepts are missing
Terms introduced by later work absent from the glossary:
- **Interleaving** (Rohrer et al. 2015 — now a learning-system section)
- **Prior knowledge / schema activation** (Bransford & Johnson 1972 — now a
  learning-system section; `Schema (network)` exists but predates this framing)
- **Encoding specificity** (Tulving & Thomson 1973 — cited in learning-system)
- **Testing effect** (Roediger & Karpicke 2006 — the shelf's most-cited finding)

### F4 · Type labels are data, but invisible as structure
Every `<dt>` ends with a type word (principle / term / technique / tool /
framework / pitfall / myth / clinical flag…). This is good metadata rendered as
undifferentiated text — nothing scannable distinguishes a *pitfall* from a
*principle* at a glance.

### F5 · One entry is a spec, not a term
`Recognition / cued recall / free recall (spec)` is three terms in one row;
it should be three short entries or one named entry ("Retrieval formats").

## Proposed improvements (P4-G plan)

| # | Change | Cost |
|---|--------|------|
| G1 | Add one `<h2>` group header per source doc/theme (≈20 groups) + `id` on every `<dt>` | mechanical, scriptable |
| G2 | Add "→ defined in Ref NN" link to every orphaned entry (~30) | small |
| G3 | Add the four missing entries above (+AR twins) | small, sourced |
| G4 | Render type suffixes as styled badges (CSS class per type) | CSS only |
| G5 | Optional: tiny client-side filter box (no dependencies) | small JS |

G1+G2 unblock deep-linking from all 22 docs; G3 closes the coverage gap with
already-verified digests; G4–G5 are polish.

## Non-issues
- Doc-order arrangement is *defensible* (mirrors the shelf's own sequence) —
  keep it; group headers make it legible rather than re-sorting alphabetically.
- Entry length is healthy (avg 36w); only `Wanting vs liking` (82w) runs long
  because it is genuinely two concepts.
