# Reference Shelf Conventions

House rules for the `reference/` shelf ("Learn to Learn"). The shelf is a set of
self-contained, evidence-grounded HTML docs that cross-link into one system.
Following these keeps the shelf consistent, verifiable, and syncable.

## File naming & numbering

- Files are `dash-case.html` matching their title (e.g. `play-as-recovery.html`).
- Docs carry a **Reference NN** number in the `<p class="kicker">` and the
  `<footer>`, plus a title in the `<title>` and `<h1>`.
- Numbers are assigned in creation order (01–16 today). The glossary is the one
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

- **Headings carry meaning, not ordinals.** Do not number sections
  ("First principle", "1 ·", "Part 2") in headings. Use descriptive titles.
  Numbers are allowed when they are the content (lesson numbers, years, counts).
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

## The Arabic twins

- Only docs with twins: `rest-and-recovery.html`, `play-as-recovery.html`
  (`reference/ar/`). The EN doc is authoritative; the AR twin mirrors it 1:1.
- **SYNC, don't append:** when the EN doc changes, the twin must be brought
  fully current (missing sections added, renamed sections renamed, tables
  rebuilt) — not just patched.
- **House voice:** translate into the twin's established terminology (check the
  twin itself for existing terms — e.g. الاستمتاع/الرغبة for liking/wanting)
  rather than inventing new ones.
- **Gates to verify after a sync:** HTML tag balance in both files; heading
  parity (same h2/h3 counts); AR/EN character ratio in the 0.75–0.97 band;
  no stray characters (e.g. `§`) in the AR file; all AR links resolve
  (including `#anchor` targets inside other AR twins).

## Verification

After editing any doc, run the structural checker (HTML tag balance via
`html.parser`) and re-check heading parity + ratio for any touched AR twin.
Links can be verified by grepping the href set against the file list.

## Process

- Analysis notes and research reviews live in `Archive/` (they are working
  documents, not the shelf).
- `Archive/repo-deep-analysis.md` is the standing audit; roadmap items
  eventually land here as conventions.
