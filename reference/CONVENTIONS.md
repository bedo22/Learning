# Reference Shelf Conventions

House rules for the `reference/` shelf ("Learn to Learn"). The shelf is a set of
self-contained, evidence-grounded HTML docs that cross-link into one system.
Following these keeps the shelf consistent, verifiable, and syncable.

## File naming & numbering

- Files are `dash-case.html` matching their title (e.g. `play-as-recovery.html`).
- Docs carry a **Reference NN** number in the `<p class="kicker">` and the
  `<footer>`, plus a title in the `<title>` and `<h1>`.
- Numbers are assigned in creation order (01–19 today). The glossary is the one
  unnumbered doc (`Reference · Learning to Learn`).
- A new doc gets the next free number and must be added to:
  1. the `<nav class="ref-nav">` of every closely-related doc,
  2. the glossary's nav (the glossary links everything),
  3. `index.html` (the lessons-to-references map),
  4. any body copy that should point to it.

## HTML template

Every doc follows this skeleton (see `study-advice.html` for the canonical example):

```html
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Doc Name — Learn to Learn</title>
<link rel="stylesheet" href="../assets/lesson.css">
</head>
<body>
<main>
```

Both doctype styles occur in the shelf today (`<!DOCTYPE html>` in older docs,
`<!doctype html>` + self-closing metas in the newest); pick either for new docs
— both render identically — but don't convert existing files for cosmetics.
```

<header class="lesson-head">
  <p class="kicker">Reference NN · Learning to Learn</p>
  <h1>Title</h1>
  <p class="meta">Short descriptor</p>
</header>

[content: h2 sections, h3 sub-sections, tables, callouts]

<span class="cite">Source lines, one per evidence cluster</span>

<nav class="ref-nav">
<strong>Related</strong> &nbsp;·&nbsp; <a href="...">Doc</a> (optional note) &nbsp;·&nbsp; ...
</nav>

<footer class="lesson-foot">
<span>Learning to Learn · Reference NN</span>
<span>Got a question? Ask your teacher.</span>
</footer>

</main>
</body>
</html>
```

## Content rules

- **Headings carry meaning, not ordinals.** Do not use bare section ordinals
  ("1 ·", "Part 2") as headings — use descriptive titles. Numbers are allowed
  when they are the content: lesson numbers, years, counts, and named items
  ("Myth 1", "Step 1", "Pillar 1"). Prefer the named form ("Step 1 · Define the
  goal") over the bare ordinal ("1 · Define the goal").
- **Cite at the bottom, `span.cite` lines**, separated by `&nbsp;·&nbsp;`.
  One line per evidence cluster (e.g. one for the primary source, one for the
  research base, one for Wikipedia/background links). Use the `div.references`
  block only for heavier source lists (rest-and-recovery).
- **Evidence is load-bearing.** Claims cite primary sources; correlational
  studies are labeled "correlational"; single small studies are labeled as such.
  Do not overclaim beyond what the cited source supports.
- **Cross-link deliberately.** Every doc links to its direct neighbors in the
  nav and to the glossary; body copy links to the specific doc a claim lives in.
  Anchors (`id="..."`) are added to sections that other docs reference
  (e.g. `#key-takeaways`, `#shutdown`, `#learning-style`) — add the id when you
  link to a section.
- **House vocabulary** lives in `learning-to-learn-glossary.html`. New terms
  introduced by a doc must be added there (with the doc as the "See" target).
- **Reuse citations.** Before citing something new, check whether the shelf
  already cites it — the reference list is shared, not per-doc.
- **When citing a *mechanism*, check its replication record.** A finding can be
  well-supported while the mechanism behind it is contested (e.g. ego-depletion
  as a resource: the preregistered multilab replication found d ≈ 0.04 — the
  wanting doc cites it as the caveat). State contested mechanisms honestly
  rather than as established fact.

## Source digests & verified citations

- **Every evidence cluster cites a source digest.** Digests live in
  `reference/sources/<short-key>.md`, one per paper the shelf actually cites.
  Follow `sources/_TEMPLATE.md` exactly — every field is load-bearing for the
  verification pipeline.
- **A digest is the accumulated research asset.** Before researching a claim
  again, grep `sources/` for the paper — the digest holds the DOI, the verified
  link, the key quotes with locations, and what each doc claims from it.
  Research is done once, then reused (this is what makes each future question
  faster instead of re-scraping the web).
- **Every citation carries a verifiable identifier.** DOIs are preferred
  (they are permanent and machine-checkable). Books without a DOI use a
  verified stable URL (publisher page, institute page, or open archive). Write
  DOIs as real links in the docs: `<a href="https://doi.org/...">`.
- **Run `python3 scripts/verify-links.py` before shipping.** It is the gate
  that makes "verified citations" true: cache-first (steady state makes zero
  network requests), Crossref-verified DOIs, rate-limited to ≤1 req/s with
  jitter + backoff. It reports any dead link, then the fix belongs in the doc
  AND its source digest. **It scans the docs AND the digests** — a dead
  DOI/URL in `sources/*.md` fails the run just like one in a doc.
- **Digests are English-only** — sources are language-neutral; the AR twin
  mirrors the same citation text (DOI link included) but does not get its own
  digest copy.
- **Reuse, don't re-digest.** When a doc cites a paper that already has a
  digest, update the digest's "what the doc claims" list — never create a
  second digest for the same paper.
- **Accessing papers:** `sources/SOURCE-ACCESS.md` has the fallback chain
  (DOI → Crossref → Semantic Scholar → open-access repos → Internet Archive)
  and per-source-type access methods. Agents researching new claims should
  consult it before attempting raw web searches.

## The Arabic twins

- Thirteen twins exist (`reference/ar/`): `rest-and-recovery`, `play-as-recovery`,
  `wanting-vs-liking`, `learning-to-learn-glossary`, `study-advice`,
  `memory-techniques`, `learning-system`, `planning-and-execution`,
  `focus-and-attention`, `learning-myths`, `ai-and-learning`,
  `productivity-systems`, `self-management`. The EN doc is authoritative; the AR twin mirrors it
  1:1. Live status in `twin-status.md`.
- New twins use the translate-to-arabic skill's gate battery, vendored in-repo
  as `scripts/verify-twins.py`: heading parity, identical h2 ids, AR/EN char
  ratio in the 0.75–0.97 band, lang-switch lines both ways.
- **SYNC, don't append:** when the EN doc changes, the twin must be brought
  fully current (missing sections added, renamed sections renamed, tables
  rebuilt) — not just patched.
- **House voice:** translate into the twin's established terminology (check the
  twin itself for existing terms — e.g. الاستمتاع/الرغبة for liking/wanting)
  rather than inventing new ones.
- **Gates to verify after a sync** (`scripts/verify-twins.py`, run from the
  `reference/` dir): HTML tag balance in both files; heading parity (same
  h2/h3 counts); AR/EN character ratio in the 0.75–0.97 band; no stray
  characters (e.g. `§`) in the AR file; all AR links resolve (including
  `#anchor` targets inside other AR twins). `scripts/density-audit.py`
  flags per-section prose-abbreviation candidates.

## Coverage

- **`COVERAGE.md` is the shelf's external domain model** — the node-by-node map
  of what the learner must be able to do, and which doc/lesson/glossary/twin
  covers each node. It is the definition of "complete": a node is covered when
  it has a doc + lesson + glossary terms (twin for core nodes); the shelf is
  complete when every node is covered AND the internal checks below pass.
- **Update `COVERAGE.md` in the same commit as any shelf change** (new doc,
  new lesson, new glossary term, new twin). An empty cell in the map is a gap
  by definition — this is how the planning and focus GAPs were caught.
- **Language discipline:** use "internally consistent" for a shelf whose
  internal checks pass; reserve "complete" for a shelf whose coverage map is
  green. Verification of what exists cannot see absence.

## Verification

After editing any doc, run the structural checker (HTML tag balance via
`html.parser`) and re-check heading parity + ratio for any touched AR twin.
Links can be verified by grepping the href set against the file list.

## Process

- Analysis notes and research reviews live in `Archive/` (they are working
  documents, not the shelf).
- `Archive/repo-deep-analysis.md` is the standing audit; roadmap items
  eventually land here as conventions.
