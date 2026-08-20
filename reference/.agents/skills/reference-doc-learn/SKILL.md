---
name: reference-doc-learn
description: >-
  Build a new entry for the Learn to Learn reference shelf — EN HTML doc
  plus AR RTL twin. Extends the general reference-doc skill with this
  shelf's specific conventions. Load reference-doc first for the base
  contract.
---

# Reference Doc — Learn to Learn

Extends `reference-doc` (load it first). This skill defines the
shelf-specific patterns: section ordering, navigation, source digests,
learning conventions, and verification for the Learn to Learn shelf.

## Shelf state

| Metric | Value |
|---|---|
| EN docs | 21 (reference/*.html, excluding index) |
| AR twins | 13 (reference/ar/*.html) |
| Source digests | 145 (reference/sources/*.md) |
| Glossary | learning-to-learn-glossary.html + AR twin |
| Index | index.html (English-only) |
| Evidence base | evidence-base.html (Reference 20) |
| CSS | assets/lesson.css (Tufte-ish: serif, ochre, paper) |
| Scripts | scripts/verify-links.py, scripts/link-sources.py |
| Nav convention | Kicker+lang-switch / TOC / back-to-top / ref-nav |

## Section ordering (guide, not law)

There is no fixed spine. Each doc chooses its own order based on its
narrative. The guide:

**Opening** — Hook (why this doc exists) → Quick Start callout → TOC
**Definition** — What it is (and what it's not)
**Theory** — How it works (pillars, mechanisms, models)
**Practice** — When to use it, how to do it, when to stop
**Reference** — Strict lists, worked examples, failure modes
**Closing** — Summary checklist → Sources → Nav

Anchors: the first H2 should define the topic; the last H2 should be
the summary. Everything between is yours to design.

## Navigation convention

Every doc has four navigation layers:

### 1. Kicker (top, linked breadcrumb)
```html
<p class="kicker">
  <a href="../index.html">Reference N · Learning to Learn</a>
  <span class="lang-switch-inline">
    <a href="./ar/{topic}.html">العربية</a>
  </span>
</p>
```
AR twin uses `../../index.html` and links back to EN with `📖 English`.

### 2. Section map (TOC, after quick-start)
```html
<nav class="toc" aria-label="Section map">
  <p><strong>In this document</strong></p>
  <ol>
    <li><a href="#sec-{kebab}">{Section name}</a></li>
    ...
  </ol>
</nav>
```
2-column layout (CSS handles responsive collapse). List 7-10 main sections.

### 3. Back-to-top anchors (before every H2 after the first)
```html
<p class="back-top"><a href="#">↑ Top</a></p>
```

### 4. Ref-nav (bottom, cross-references)
```html
<nav class="ref-nav">
  <strong>Close</strong> · <a href="{sibling}.html">{Name}</a> · ...
  <strong>Also</strong> · <a href="{distant}.html">{Name}</a> · ...
  <a href="{prev}.html">← {Prev}</a> · <a href="{next}.html">{Next} →</a>
  · <a href="learning-to-learn-glossary.html">Glossary</a>
  · <a href="evidence-base.html">Evidence Base</a>
</nav>
```
- **Close**: 1-2 hop neighbors (same layer)
- **Also**: related but distant docs
- **Prev/Next**: reading order (your choice)
- All source-heavy docs link to Evidence Base

Generate navs with `scripts/upgrade-nav.py` (update ORDER, NAMES,
NEIGHBORS, SOURCE_HEAVY in the script, then run it).

## Section patterns

### Callouts
```html
<div class="callout">
  <h3>{Title}</h3>
  <p>{Content}</p>
</div>
```
Use for: core ideas, clarifications, counter-arguments, definitions,
deep dives. Max 2-3 per section. Stack rarely — merge instead.

### Collapsible deep dives
```html
<details>
  <summary>{Question} (click to expand)</summary>
  {content — callout, table, or prose}
</details>
```
Use for: material that's important but not core narrative (e.g., "Do
you need mastery before you can play?"). Max 1-2 per doc.

### Flow boxes
```html
<div class="flow">
  <strong>How it fits:</strong> {connection to shelf neighbors}
</div>
```
Use at the end of worked examples to show how the doc fits the shelf.

### Tables
```html
<table>
  <thead><tr><th>{Col}</th>...</tr></thead>
  <tbody><tr><td>{Cell}</td>...</tr></tbody>
</table>
```
Use for: comparisons, timelines, scored lists, triage matrices.
CSS: alternating row colors, ochre headers.

### Score colors (strict lists)
```html
<td><strong class="score-good">7.0</strong></td>  <!-- green, ≥7 -->
<td><strong class="score-mid">4.5</strong></td>    <!-- ochre, 4–6.9 -->
<td><strong class="score-bad">1.3</strong></td>    <!-- red, <4 -->
```

## Learning conventions

### Summary section
The summary is a **retrieval scaffold**, not a restatement:
1. Checklist items (the quick-lookup)
2. Recite-before-check instruction (cover, recite, verify)
3. Spacing note (re-recite tomorrow, week, month)
4. Transfer prompt ("teach this to someone in one minute")

### Teacher questions (if present)
1. Open-ended retrieval (never recognition with visible answers)
2. Interleaved across sections (not doc order)
3. At least one self-explanation ("explain why")
4. Feedback built in (attempt → verify against section)
5. Two-tier: recall for beginners, teach/transfer for coaches

## Source digest system

Every cited paper has a digest in `reference/sources/<short-key>.md`
following `sources/_TEMPLATE.md`. Fields: Identity, DOI, Key findings,
Key quotes with locations, What the doc(s) claim, Caveats, Verification.

**Before researching:** grep `sources/` for the paper. If a digest
exists, update its "What the doc claims" list — never re-research.

**DOI verification:** Crossref API (`api.crossref.org/works/{doi}`).
200 = registered. Every DOI in docs and digests must verify.

**Linking:** Run `scripts/link-sources.py` after adding/updating
digests. It inserts `📄` links from docs to their digests.

**Verification:** Run `scripts/verify-links.py` before shipping.
Cache-first (`.link-cache.json`), rate-limited, scans docs + digests.

**Access guide:** `reference/sources/SOURCE-ACCESS.md` — how to
access each source type, fallback chain, trust tiers.

## Arabic adaptation

- `<html lang="ar" dir="rtl">`; asset paths: `../../assets/`
- Headings: mirror EN text 1:1, reuse EN `id` anchors verbatim
- Technical terms: keep English form where natural, Arabic beside it
- Cultural fit: examples, metaphors, norms fit Arabic readers — not
  literal Western renderings (SAM factor 6)
- Kicker: `مرجع N · تعلّم كيف تتعلّم` linked to `../../index.html`
- Lang-switch: `📖 English` pointing to `../{topic}.html`
- Ref-nav: `ذوي الصلة` (Close) / `أيضًا` (Also) tiers

## Pattern library (recurring gaps)

Append when audits surface new themes. Record confidence + counter-examples.

- **Fluency illusion warnings** — docs should flag when rereading feels
  productive but isn't (metacognition doc owns this)
- **Retrieval depth** — questions test application, not just recall
- **Cross-reference density** — docs link to neighbors (play↔recovery,
  motivation↔wanting)
- **Source digest coverage** — every cited paper has a digest
- **Worked examples** — abstract concepts get concrete examples
- **Stop conditions** — docs tell readers when to stop (rereading,
  playing, planning)
- **AR cultural adaptation** — metaphors and examples fit Arabic readers

## Verification scripts

| Script | What it does | When to run |
|---|---|---|
| `scripts/verify-links.py` | Verifies all DOIs (Crossref) + URLs + anchor links in docs + digests | Before every commit |
| `scripts/link-sources.py` | Inserts 📄 links from docs to their source digests | After adding/updating digests |
| `scripts/upgrade-nav.py` | Regenerates all nav blocks (update ORDER/NAMES/NEIGHBORS first) | After adding a new doc |

Cache: `scripts/.link-cache.json` — committed, avoids re-verification.
