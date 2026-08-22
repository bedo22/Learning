# Review: reference/play-as-recovery.html

> Independent manual review — full read of all 2,666 lines, hand-audit of all 27
> strict-list score computations, link/anchor integrity check, and cross-checking
> citations against the local `reference/sources/` digests.

## Verdict

**Strong document with real defects.** The thinking is excellent — the defects are
almost entirely mechanical: one broken refactor, four self-contradicting score marks,
one wrong author name, some dead citation weight. None require rethinking the content.

## What genuinely works

1. **The spine holds.** Triage → definition → pillars → history → paradox → mechanics →
   stop-signal → counterarguments → scored list is a coherent argument, and every section
   hands off to the next explicitly. The "play paradox" resolution (*schedule containers,
   never content*) is the sharpest idea on the shelf.
2. **The math audits clean.** All 27 strict-list rows recomputed: `min(V·L·Z)` play scores,
   `mean(D·R·M·C)` recovery scores, and `play×recovery÷10` ranks — **all 27 are
   arithmetically correct**, including the worked-example session scores
   (V8·L8·Z5→5; 24/4→6.0; 3.0). That level of internal discipline is rare.
3. **Epistemic hygiene above average.** Zhao N=40 labeled *suggestive*, the Whitman case
   labeled *suggestive, not causation*, dhikr research flagged *unverified*, the strict list
   openly admits *"no published study has ranked leisure activities this way."* The
   anhedonia→clinician boundary appears twice where it matters.
4. **Link integrity is perfect**: all 11 same-page anchors resolve, all 60 relative file
   links exist, the `rest-and-recovery.html#key-takeaways` deep-link is valid, and the
   promised "27 activities" is exactly what the table contains.

## What's broken (with line numbers)

### Structural

- **L553–556 — empty `<details>` block.** The summary says *"Do you need mastery before
  you can play? (click to expand)"* and expands into nothing; the actual five-point answer
  sits below it as a callout outside the collapsible. Clear refactor artifact.
- **L1675–1757 — orphaned counterarguments.** The "What the research disputes" callout
  floats *above* `<h2 id="failure-modes">` with no heading of its own — clicking the TOC's
  "#failure-modes" jumps past it.
- **Footer/TOC disorder.** The Summary checklist (`#summary-checklist`, L2616) comes *after*
  the page footer, and neither it nor `#worked-example` nor the Islamic framing appear in
  the TOC, which promises 10 sections while the doc carries ~14.

### Internal contradiction

- **Threshold rule violated 4 times.** L2029 declares: *✅ at ≥7, ⚠ from 4–6.9*. Yet:
  podcasts fiction **⚠ 8** (L2282), TV chosen **⚠ 7** (L2299), YouTube chosen **⚠ 7**
  (L2347), web-novel play mode **⚠ 7** (L2313). If these are deliberate downgrades for
  passivity, say so — right now the doc breaks its own stated rule.

### Factual / citation

- **Wrong author name.** Body (L1027): "Sonnentag, **Zhao** & Parker's Annual Review."
  The verified digest `sources/sonnentag-2022-annual-review.md` says Sonnentag,
  **Cheng** & Parker. The doc contradicts its own evidence base.
- **Typos in raw bytes:** "a **cublion** or kitten" (L576); "Panksepp **( (**1990)" and
  "Vygotsky **( (**1930)" double-parens in the footer (L2611); stray spaces before an anchor (L2027).
- **Five orphaned citations:** Simons 2016 (brain training), Iso-Ahola 1997,
  Petrou & Bakker 2016, Tandler 2024, and Galpayage Dona 2022 (bumblebees!) are linked in
  the footer but never cited anywhere in the body — leftover weight from trimmed material.
- **Duplicate source files:** `proyer-sendatzki-2026-play-work-review.md` and
  `proyer-sendatzki-2026-review.md`, both linked in the same cite span.

## Redundancy worth trimming

Sonnentag's mastery-experience definition is quoted nearly verbatim **twice**
(~L446–457 in the fifth-pillar callout, again ~L600–611 in the mastery answer), with the
same language-class example both times. Combined with the graduation-cycle callout covering
similar ground, the doc runs ~10–15% longer than its content justifies — unusual for a
shelf whose conventions prize density.

---

## Verification addendum (post-review fact-checks)

Three claims initially flagged as unverifiable were checked externally afterward:

1. **Bukhari 6129 — the doc is CORRECT ✅.** [sunnah.com/bukhari:6129](https://sunnah.com/bukhari:6129)
   is exactly the Abu ʿUmayr bird hadith ("O Aba ʿUmair! What did the Nughair do?",
   Book 78, Good Manners). Citation stands; suspicion retracted.
2. **Shaw quote — genuinely misattributed ❌.** [Quote Investigator (Mar 2024)](https://quoteinvestigator.com/2024/03/09/play-grow/)
   finds no evidence Shaw said it: earliest strong match G. Stanley Hall 1904 (*Adolescence*),
   chiasmus form George L. Knapp 1908, root remark Karl Groos 1896 (*Die Spiele der Thiere*);
   first Shaw attribution appears only in 1983 — "no compelling supporting evidence."
   Elegant fix: Groos is already in this doc's history table (1898 row), so the quote can be
   honestly re-attributed to him / Hall.
3. **Sonnentag "Zhao" → Cheng — confirmed ❌.** DOI
   [10.1146/annurev-orgpsych-012420-091355](https://doi.org/10.1146/annurev-orgpsych-012420-091355)
   resolves to the Annual Review paper; authors are Sonnentag, **Cheng** & Parker per both
   the digest and the publisher page. Likely contamination from Zhao et al. CHI 2025,
   cited elsewhere in the same doc.
4. Reinecke & Hofmann 2016 ✅ real (*Human Communication Research* 42(3), 441–461;
   live check Cloudflare-blocked, digest records prior verification) · Rieger et al. 2014 ✅ matches digest.

## Priority fix list

1. Fix "Zhao" → "Cheng" (factual error)
2. Reattribute or hedge the Shaw quote (ideally to Groos/Hall)
3. Repair or delete the empty `<details>` block
4. Reconcile the four ⚠/✅ threshold violations
5. Move the disputes callout under a proper heading inside `#failure-modes`; move Summary
   before footer; update TOC
6. Remove the 5 orphaned citations + dedupe the Proyer-Sendatzki files
7. Typos: cublion, double-parens ×2, stray spaces at L2027

---

## Applied fixes (2026-08-22) — EN + AR

All mechanical and canonical defects above are now fixed; twin gates (`verify-twins.py`)
still pass ALL 14 checks. Summary of changes:

- **Sonnentag "Zhao" → "Cheng"** (author error, verified vs digest + DOI).
- **Shaw quote reattributed** to Karl Groos (1896) / G. Stanley Hall (1904), with a
  "widely misattributed to Shaw" note — matches Quote Investigator.
- **Empty `<details>` removed**; its answer callout stands alone.
- **Disputes callout relocated** under a new `h2#failure-modes` heading and given
  `id="research-disputes"`; both prose references now link to it.
- **Summary moved before the source citations** (no longer after the footer).
- **TOC completed** from 10 → 14 entries (added Intersection, Worked example,
  Islamic framing, Summary).
- **Threshold marks reconciled** — 4 rows with ⚠ on a 7–8 score changed to ✅; the rule
  now also declares an explicit "✗ by design at any number" exception, which legitimately
  keeps the 3 ✗-on-4 rows (Quran, prayer, chores) consistent. Machine-checked: 0
  remaining violations.
- **8 orphaned citation links removed** across the shelf (EN doc + 3 sibling docs);
  **duplicate `proyer-sendatzki-2026-review.md` digest deleted** and the sibling docs
  redirected to the comprehensive one.
- **Typos fixed**: `cublion`→lion cub; `Panksepp ( (` / `Vygotsky ( (` → single paren;
  stray spaces; duplicated `تحديدًا` in AR; Caillois year normalized to 1958/61.
- **Arabic twin defects fixed**: CJK leak 如何去 removed; garbled تعلُّطو / بتعطيذ /
  بوتيرتك corrected; "Sandbox" no longer mistranslated as ألعاب الحماية.

**Still open (pedagogical / scope gaps, out of this fix round):** retrieval-practice
devices & teacher questions, Who-this-is-for header line, cold-start fallback,
late-night-play answer, social-play strict-list rows, 5 glossary terms, and the AR
twin's deeper structural drift (missing ref-nav/TOC/back-tops, prose drift beyond the
mechanical fixes). Logged in `reference/Archive/analysis-play-as-recovery.md` (STATUS:
PARTIALLY ADDRESSED).

## Value-vs-clutter analysis + round 2 (2026-08-22)

Each remaining item was judged against shelf evidence, not taste:

| Item | Verdict | Evidence |
|---|---|---|
| Teacher questions / retrieval section | **Declined — clutter** | 0/21 EN docs have one; per-doc addition breaks house consistency (Guard 1). Shelf-wide decision. |
| `Who this is for:` header line | **Declined — clutter** | 0/21 docs carry it; same rationale. |
| Cold-start fallback ("fried now, no menu") | **Applied ✅** | Operational hole in the doc's own required action; emergency-starters callout added to #planning. |
| Late-night (2am) answer | **Applied ✅** | Intro raises it (L1977), nothing answered it; failure-table row added: sleep defaults after dark, low-arousal play only if wired. |
| Social-play strict-list rows | **Half — scope note applied ✅** | h2 already scopes to indoor solo/screen by design; new rows would be scope creep. One-line pointer added (step-3 readers → start social). |
| Glossary: triage / liking test / play menu | **Applied ✅** | Used across 6/6/2 docs; entries added to g-wanting-liking in EN + AR twins. Play paradox / meaning trap skipped (single-doc coinages, defined inline). |
| AR twin TOC / back-tops / ref-nav | **Applied ✅** | Sibling AR twins all carry them (toc 2/2, back-tops 9–15); ours had 0/1/0. Added translated 14-item TOC, back-tops on every section, ref-nav with 📖 English link, fixed orphan `</footer>` + missing Reference-12 span. |
| Deep AR prose retranslation | **Deferred ⏸️** | Gates pass; large effort, low marginal value vs risk. Documented. |

Gates after round 2: verify-twins ALL PASS for both play-as-recovery and
learning-to-learn-glossary; zero broken links or anchors in any modified file.

## Skill update

The `shelf-review` skill was upgraded so these classes of defect are caught by the
procedure itself next time: author-year-vs-digest cross-check (evidence discipline),
scrapling fallback when a digest omits a figure, reverse citation audit (orphans),
HTML-sanity + marks-vs-bands structure checks (REFERENCE §3a), intra-doc duplication
type (§4), and 3 new pattern-library entries (§7). See `references/mode-1-audit.md`
steps 6–8.

## Round 3 (2026-08-22): social rows + Arabic prose re-synchronization

User direction: add the actual social plays (previously declined on scope), and complete
the deferred AR prose re-translation.

**Strict list 27 → 32 (EN + AR):** five new scored rows, same formula, machine-audited:
team sports & pickup games **7.0**, board-game nights **6.8**, banter with close friends
**6.3**, casual bouldering with a partner **6.0**, cooking together **5.4**. Section
retitled *"32 plays judged: solo, screen & social"*; the round-2 scope note replaced by
an inclusion note; counts updated in quick start + TOC both languages. Each row carries
its own flip condition (rank enters, winning becomes the point, hosting stakes).

**AR prose drift resolved:** disputes callout relocated under `h2#failure-modes`
(renamed «الحجج المضادة الصادقة وأكثر أشكال الفشل شيوعًا», `id="research-disputes"`);
Shaw quote reattributed to Groos/Hall in translation; Deci&Ryan paragraph moved from
Pillar-2 to Pillar-4 carrying EN's claim (play as prototypical intrinsic motivation);
Pillar-5 aligned to EN (workload suppresses detachment/control first — mastery most
robust); flow-vs-play callout rewritten to EN framing (*deep work is flow, not play*).
Threshold rule amended with the by-design exception; four ⚠-on-7/8 marks → ✅;
cold-start callout and late-night failure row translated in. Deliberate cultural
additions retained (Hanzala hadith, Muslim 2750) per SAM factor 6.

**Verification:** strict-list math machine-audited clean in BOTH languages (all ranks =
P×R÷10 under round-half-up); rows sorted descending; twin gates ALL PASS for
play-as-recovery and learning-to-learn-glossary; zero broken links or anchors.
