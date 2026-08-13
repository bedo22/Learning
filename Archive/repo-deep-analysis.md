# Deep Analysis — the Learn to Learn repository (v2, deepened)

Date: 2026-08-13 (v2 — refreshed after the roadmap was implemented) · Scope: whole repo (reference shelf, lessons, learning-records, Archive, Trascriptions, assets) · Focus: **gaps, improvements, and contradictions** — especially content.

> **How this version differs from v1:** v1 was written when the shelf had 13 docs and its "gaps" section was a roadmap. That roadmap has since been implemented (4 new docs, sleep section, exam strategy, extra myths, CONVENTIONS, index). This v2 audits the *new* state of 17 docs + 24 lessons, and — new — runs a systematic **contradiction audit** (definitions, numbers, cross-refs, verdicts). The headline finding: the shelf has real internal contradictions, the biggest being a **two-scheme numbering system** where 7 of 17 docs disagree with the index about their own number.

---

## 1. What this repo is (current state)

A personal "learning to learn" knowledge system built from 8 Dr. Justin Sung (iCanStudy) transcripts. Core deliverable: a **17-doc reference shelf** (`reference/`) with a shared vocabulary (**100-term glossary**), plus a practice layer (**24 lesson pages**), a learning log (**2 records**), raw transcripts (`Trascriptions/`), analysis artifacts (`Archive/`), and assets. **Three docs have Arabic twins** (`reference/ar/`): rest-and-recovery, play-as-recovery, wanting-vs-liking. House rules live both in `reference/CONVENTIONS.md` (committed) and in agent skills.

**Shelf inventory — size + kicker vs index number:**
| Doc | KB | h2 | h2 ids | Kicker # | Index # | Disagree? |
|---|---|---|---|---|---|---|
| blooms-six-levels-of-thinking | 7.3 | **0** | 0 | 01 | 11 | **YES** |
| learning-myths | 9.2 | 4 | 1 | 02 | 02 | |
| learning-system | 7.2 | 2 | 0 | 03 | 01 | **YES** |
| orders-of-learning | 5.8 | 2 | 0 | 04 | 03 | **YES** |
| self-management | 7.1 | 3 | 0 | 05 | 05 | |
| memory-techniques | 17.7 | 2 | 0 | 06 | 04 | **YES** |
| study-advice | 16.7 | 6 | 0 | 07 | 07 | |
| rest-and-recovery | 37.8 | 9 | 1 | 08 | 08 | |
| productivity-systems | 10.9 | 6 | 0 | 09 | 06 | **YES** |
| reverse-goal-setting | 11.8 | 7 | 0 | 10 | 09 | **YES** |
| skill-acquisition | 11.3 | 4 | 0 | 11 | 10 | **YES** |
| play-as-recovery | **124** | 16 | 16 | 12 | 12 | |
| motivation-and-self-determination | 12.1 | 6 | 0 | 13 | 13 | |
| metacognition-and-calibration | 9.5 | 8 | 0 | 14 | 14 | |
| ai-and-learning | 8.4 | 6 | 0 | 15 | 15 | |
| note-taking | 7.7 | 5 | 0 | 16 | 16 | |
| wanting-vs-liking | 37.9 | 16 | 16 | 17 | 17 | |
| learning-to-learn-glossary | 35.6 | 0 | 0 | — | — | |
| index.html | 8.2 | — | — | — | — | |

---

## 2. Contradictions found (new in v2 — the headline)

### C1. Two numbering schemes: 7 docs disagree with the index about their own number ⚠️ HIGH
The docs' own kickers follow **creation order** (`blooms=01`, `myths=02`, `system=03`, `orders=04`, `self-management=05`, `memory=06`, `study-advice=07`, `rest=08`, `productivity=09`, `reverse-goal=10`, `skill=11`). The **index.html reordered the shelf pedagogically** (`learning-system=01`, `myths=02`, `orders=03`, `memory=04`, `self-management=05`, `productivity=06`, `study-advice=07`, `rest=08`, `reverse-goal=09`, `skill=10`, `blooms=11`). Seven docs therefore carry a kicker number that contradicts the index listing (blooms, learning-system, orders, memory, productivity, reverse-goal, skill). CONVENTIONS.md says numbers are "assigned in creation order" — so **the kickers are the authority and the index is wrong**, but nobody can tell which without reading CONVENTIONS. A reader citing "Reference 06" gets memory-techniques from the doc but productivity-systems from the index.

**Fix:** renumber the index to match the kickers (creation order), or renumber the kickers to match the index and update the 7 footer/kicker pairs. Pick one source of truth and state it in CONVENTIONS.

### C2. wanting-vs-liking cites "Rest & Recovery (Reference 9)" — it is Reference 08 ⚠️ HIGH
Both the EN doc and its AR twin (المرجع ٩) say Rest & Recovery is Reference 9. It is **08** in its own kicker, its footer, and the index. Reference 9 is productivity-systems (kicker scheme) or reverse-goal-setting (index scheme) — either way, wrong. (The other four numbers in that same citation — 12, 13, 14, 15 — are correct.)

**Fix:** change `Reference 9` → `Reference 08` in `wanting-vs-liking.html` and `المرجع ٩` → `المرجع ٨` in the AR twin.

### C3. The wanting doc promises glossary terms that don't exist ⚠️ MEDIUM
`wanting-vs-liking.html` §Ecosystem says "glossary terms live in the Glossary" and lists **Sensitization, Cold reproduction, Extinction, Urge surfing** as vocabulary. The glossary has **none of these four**. The doc also introduced extinction and urge-surfing as core concepts in §sec-urge — they're defined inline, but the ecosystem section's "these live in the glossary" claim is false.

**Fix:** add the four terms to the glossary (Sensitization, Cold reproduction, Extinction, Urge surfing), each pointing at wanting-vs-liking as the "See" target.

### C4. CONVENTIONS.md is stale in three places ⚠️ MEDIUM
- "Numbers are assigned in creation order (01–16 today)" — there are **17** docs.
- "Only docs with twins: rest-and-recovery, play-as-recovery" — **wanting-vs-liking has a twin too** (and the AR rule for it is already in force).
- The template shows `<!DOCTYPE html>` uppercase with non-self-closing `<meta charset="utf-8">`, but the two newest docs use `<!doctype html>` + self-closing metas.

**Fix:** update the count, the twin list, and either pick one doctype style or state that both are acceptable.

### C5. Heading numerals violate the shelf's own no-ordinals rule ⚠️ MEDIUM
CONVENTIONS: "Headings carry meaning, not ordinals. Do not number sections ('First principle', '1 ·', 'Part 2')." Yet numerals persist in 8 docs: memory-techniques (`1 ·`–`6 ·`), study-advice (`1 ·`–`16 ·`), self-management (`1 ·`–`3 ·`), productivity (`Part 1`–`4`), reverse-goal (`Step 1`–`5`), play (`Pillar 1`–`4`), learning-myths (`Myth 1`–`8`), wanting (`2×2`, content — fine). Some are defensible as content (Myth/Step/Pillar are names), but `1 · Increase complexity`, `1 · Time management`, `Part 1`, and `1 · Studying ≠ learning` are pure ordinals. The rule was added after these docs were written; the shelf contradicts its own convention.

**Fix:** either strip the ordinals (keep Myth/Step/Pillar as content) or amend CONVENTIONS to allow ordinals that are content ("Myth 1" yes, "1 ·" no). Pick one.

### C6. blooms-six-levels has **zero h2 sections** ⚠️ MEDIUM
Every other doc is built on `h2` sections; blooms has only `h1` + 2 `h3`s. It is the only doc that breaks the house template structurally, which also means it can't participate in section-anchor linking and reads as a fragment rather than a shelf doc.

**Fix:** restructure into the standard h2-spine (e.g. "The six levels", "The effort is the mechanism", "A study tip: predict the exam's questions", plus the AI-answer rubric if present).

### C7. Citation style is still split two ways ⚠️ LOW
rest-and-recovery uses `div.references`; all other 16 docs use `span.cite`. CONVENTIONS explicitly permits this ("Use the div.references block only for heavier source lists (rest-and-recovery)"), so it is *sanctioned* — but v1's recommendation to unify was not executed, and a reader can't tell from the page whether the styles render differently (they don't — both are footnote blocks). Low priority; either unify or leave with the CONVENTIONS note.

### C8. Doctype split: 18 uppercase vs 4 lowercase ⚠️ LOW
`<!DOCTYPE html>` (non-self-closing metas) in 18 files; `<!doctype html>` + self-closing metas in the two newest docs (wanting EN/AR) and the play twins. Harmless to render; the CONVENTIONS template shows the old style while new docs use the new one. Fold into C4's template decision.

### What is NOT a contradiction (checked and cleared)
- **"Fourth recovery mode" vs "missing fifth mode"** (play doc intro vs intersection table) — reconciled: play maps to the *control* dimension (the 4th of Sonnentag's four), and the table explicitly says it *feels* like a missing fifth because it also brings mastery/novelty. Consistent.
- **Music in the strict list** ("✅ by definition, ⚠ as rest") vs the "what play is NOT" table ("relaxation lowers activity; play raises engagement") — reconciled: the strict-list row explicitly notes its *function* sits on the rest channel even though it passes the definition. Consistent (this was v1's flagged tension, now resolved).
- **"Genuine rest IS recovery"** (rest doc) vs recovery-as-restoration definitions elsewhere — rest-and-recovery itself argues rest is recovery *provided it doesn't tip into rumination*, and the triage doc treats them as one palette. Consistent.
- **study-advice "AI and learning" section vs the dedicated ai-and-learning doc** — study-advice is explicitly a condensed pointer ("Full treatment … in AI & Learning (Ref 15)"). Intentional layering, not duplication.

---

## 3. What's strong (unchanged, plus the new additions)

1. **Retrieval/encoding spine is coherent and evidence-backed** — Karpicke & Blunt (2011), Dunlosky (2013), Rowland (2014), Adesope (2017), Agarwal (2021) anchor "test yourself" across study-advice, learning-system, orders, memory.
2. **Recovery family is the deepest** — rest, play, and now wanting-vs-liking form a genuinely sophisticated, cross-linked treatment (effort-recovery, four experiences, triage, stop-signal, urge handling) with honest counterargument sections. The triage is now *defined* (named method, three moves) and the urge-triage is wired back to it.
3. **The 2021–2026 evidence pass closed the big citation holes** — study-advice, myths, skill, system, productivity, orders, rest, reverse-goal, blooms all carry primary sources now.
4. **AI-era content is owned twice at the right granularity** — a condensed section in study-advice + a full reference doc (Ref 15) with the paired Bastani/Kestin RCTs and the Gerlich offloading warning.
5. **The denial-backfire section (new)** — ironic process (Wegner; Wang et al. meta-analysis), forbidden-fruit/reactance (Brehm), AVE (Marlatt & Gordon), rigid-vs-flexible restraint (Westenhoefer), plus extinction as the only cue-removal mechanism — a rare, honest treatment of "don't just ban it."
6. **Cross-linking is unusually good** — the wanting doc is linked from 9 files; the lesson→reference map in index.html covers all 24 lessons.

---

## 4. Content audit — doc by doc (v2)

### 01/11 · blooms-six-levels-of-thinking — *still the weakest shape*
- **Gaps:** zero h2 structure (C6); content is a fragment, not a shelf doc. It *does* now carry the desirable-difficulties point and 13 AI/rubric mentions (v1's gap fixed), but the structure prevents it from being section-linkable.
- **Improve:** rebuild on the standard h2 spine; keep the AI-answer evaluation note; consider whether it should absorb or defer to orders-of-learning (they overlap on "higher vs lower order").

### 02 · learning-myths
- **Fixed since v1:** myths 6–8 added (multitasking, 10% brain, left/right brain) with Sana/neuromyth citations.
- **Gaps:** the "Over 95% of people hold at least one" line now spans 8 myths — fine, but it reads like it was written for 3; consider "almost everyone holds at least one."
- **Improve:** add a one-line "why these myths persist" (fluency illusion cross-link — metacognition doc) so the page connects myth → mechanism.

### 03 · learning-system
- **Gaps:** consolidation (sleep, wakeful rest) is still only cross-linked, not owned; interleaving still absent from the encoding tactics.
- **Improve:** one callout: "the third leg: consolidation" → link to rest-and-recovery §sleep; add Rohrer 2015 interleaving as an encoding tactic with the desirable-difficulties tie.

### 04 · orders-of-learning — *smallest doc*
- **Gaps:** still doesn't carry the desirable-difficulties citation (Bjork) for "why higher order feels worse but works," despite v1 flagging it.
- **Improve:** add the Rohrer 2015 / Rowland 2014 metacognitive-illusion sentence; decide its boundary with blooms (overlap noted above).

### 05 · self-management
- **Gaps:** attention-residue (Leroy 2009) still absent; the shutdown-ritual cross-link (rest doc) is only one-way (rest links it; self-management doesn't link back); distraction stats live in the cite block, not the body.
- **Improve:** add a 2-line attention-residue callout with a link to rest-and-recovery's shutdown ritual; move one distraction stat into §3 body.

### 06 · memory-techniques — *evidence-dense, one blind spot*
- **Gaps:** **still no sleep-consolidation section/link** — v1 flagged this; grep shows only 1 mention of rest/sleep in the whole doc. "The memory doc" still can't answer "how do I make it stick overnight."
- **Improve:** add a 3-line "sleep is the second half of memory" callout (Diekelmann & Born 2010; Lutz 2026) linking rest-and-recovery §sleep. Highest-value small fix in the shelf.

### 07 · study-advice
- **Fixed since v1:** test-day/exam-strategy section added (now has h2 "Test day — the exam strategy"); AI section added with pointer to Ref 15.
- **Gaps:** no spacing *schedule template* in the doc itself (2/7/30 rhythm lives only in the forgetting-curve doc and play's rest menu); numbered h3s `1 ·`–`16 ·` violate C5.
- **Improve:** add the concrete 2/7/30 example; strip the ordinals.

### 08 · rest-and-recovery — *rich, now with sleep*
- **Fixed since v1:** sleep section added ("Sleep — the consolidation engine", with Diekelmann & Born 2010 + Lutz 2026 + naps + all-nighter warning), `#shutdown` anchor wired, wakeful-rest callout present.
- **Gaps:** burnout warning signs named in the caution but not developed; the doc is 37.8 KB and growing; still the only doc using `div.references`.
- **Improve:** add a 3-line burnout checklist; consider a "recovery needs" page if it grows further (the palette callout is already nearly that).

### 09 · productivity-systems
- **Gaps:** weekly-review evidence still not cited (v1 flagged); time-blocking research absent; the "energy ≠ willpower" tie to self-management/rest is implied, not stated.
- **Improve:** 2 citations (weekly review / time blocking); one sentence tying energy to the recovery docs. Low priority.

### 10 · reverse-goal-setting — *fixed, now one of the better-grounded*
- **Fixed since v1:** now carries a full "what the goal-setting science says" section (Locke & Latham, WOOP/Oettingen, self-concordance/Sheldon & Elliot) — v1's top content priority, done.
- **Gaps:** none major. `Step 1`–`5` headings are content-ordinals (acceptable under C5's proposed rule).

### 11 · skill-acquisition
- **Gaps:** feedback science (Hattie & Timperley) still not cited despite v1 flagging; transfer-of-training line still absent; theory-practice balance could cite the spacing/difficulty family.
- **Improve:** add the feedback callout (direction of feedback) + one transfer sentence (varied practice / interleaving). Small, high-value.

### 12 · play-as-recovery — *content-complete but oversized (124 KB EN / 162 KB AR)*
- **Fixed since v1:** ordinals stripped from h2s; strict list rebuilt with a transparent scoring system (V·L·Z / D·R·M·C grounded in REQ, behavioral activation, DRAMMA); worked example; triage now *defined*; urge-triage extension wired.
- **Gaps:** v1's "split into core + appendices" recommendation **was not executed** — it's still the biggest doc by 3.3× (next is rest at 37.8 KB). The strict list (27 rows × 5 cols) and the Islamic-fiqh section are the bulk; both are appendix-grade for most readers.
- **Improve:** split or at least add a table of contents + "what to read when" quick-start. Keep the strict list (it's the doc's most-used tool) but consider moving the fiqh detail + full reference list to an appendix.

### 13 · motivation-and-self-determination — *new, good*
- **Gaps:** none major. Could cite Vallerand's passion types (harmonious vs obsessive) explicitly — the play strict list references "harmonious passion" without the citation living anywhere.
- **Improve:** add Vallerand 2003 to the cite block.

### 14 · metacognition-and-calibration — *new, good*
- **Gaps:** none major. Could use one "this is the same illusion as wanting-without-liking" cross-link to wanting-vs-liking (it links the other direction already).
- **Improve:** trivial cross-link polish.

### 15 · ai-and-learning — *new, tight*
- **Gaps:** 6 h2s, no h2 ids (C-adjacent); no AR twin.
- **Improve:** add section ids; it's the right size — don't grow it.

### 16 · note-taking — *new, tight*
- **Gaps:** Mueller & Oppenheimer's mixed replications handled honestly (good); no h2 ids; no AR twin; **no dedicated lesson** (0017 touches it but doesn't teach note-taking).
- **Improve:** add section ids; consider a 0019 "take notes that produce tests" lesson.

### 17 · wanting-vs-liking — *new, best cross-linked*
- **Gaps:** C2 (wrong rest reference), C3 (promises 4 glossary terms that don't exist); h2s have ids and lang-switch (model citizen); the AR twin passes the full battery.
- **Improve:** fix C2+C3; add Vallerand passion cross-link to motivation doc.

### Glossary — 100 terms, but the doc promises more than it has
- **Missing terms** that docs *claim* live here: **Sensitization, Cold reproduction, Extinction, Urge surfing** (wanting doc §Ecosystem). Also verify "cognitive offloading" and "AI fluency illusion" have entries (v1 flagged these).
- **Improve:** term-audit: grep every `<strong>` that reads as a term across the 5 newest docs and add ~6 entries. Consider a glossary twin (the translate skill's terminology gate currently has no AR glossary to gate against).

---

## 5. Missing topics — what the shelf still doesn't own

1. **Sleep & Learning as a first-class topic** — sleep is now a *section* of rest-and-recovery (good), but memory-techniques (its natural second home) still doesn't link it, and no lesson teaches "sleep as study strategy." Either link memory → rest §sleep (cheap) or promote to a doc (probably overkill).
2. **Attention & distraction** — partially in self-management; attention-residue (Leroy) still missing; a dedicated distraction doc is probably *not* worth it (self-management + productivity cover it) — resolve by adding the residue callout.
3. **Feedback science** — Hattie & Timperley belongs in skill-acquisition (RAIL's Awareness stage) and is still missing.
4. **Passion types (Vallerand)** — the play strict list already *uses* "harmonious passion" as a verdict condition; the theory behind it (harmonious vs obsessive) is not owned anywhere.
5. **Learning-record culture** — only 2 records in learning-records/ despite study-advice lesson 16 arguing the learning log is among the highest-leverage habits. The shelf *preaches* the log and doesn't *practice* it.
6. **AR twins for 14 of 17 docs** — including the glossary, which the translate skill treats as the terminology gate. Highest-value next twins: glossary, then study-advice / memory-techniques / learning-system (the fundamentals v1 named).

---

## 6. Evidence & citation audit (v2)

| Tier | Docs | Notes |
|---|---|---|
| Strong | memory, play, rest, wanting, motivation, metacognition, ai, note-taking, reverse-goal | primary sources + honest hedging |
| Good | study-advice, myths, system, productivity, skill, self-management | a few gaps each (listed in §4) |
| Weak | **blooms, orders** | not citation-poor, but structurally thin / smallest |

**Format inconsistencies (v2):**
- `span.cite` everywhere except rest-and-recovery (`div.references`) — sanctioned by CONVENTIONS (C7).
- Bare Wikipedia links mixed into cite blocks in 11 docs vs pure `span.cite` in 6 — cosmetic.
- The wanting doc's cite block contains the C2 wrong-reference error — the only *factual* citation error found.

---

## 7. Structural & format inconsistencies (v2)

1. **Two numbering schemes** (C1) — the index reorders 7 docs against their own kickers. **Fix first.**
2. **Doctype/template split** (C4/C8) — 18 uppercase vs 4 lowercase; CONVENTIONS template is the old style.
3. **Heading numerals** (C5) — 8 docs carry ordinals against the no-ordinals rule.
4. **Anchor ids** — only play (16) and wanting (16) have full h2 ids; rest has 1 (`#key-takeaways`... plus `#shutdown`); the other 14 docs have **zero** h2 ids. Cross-doc section links are impossible for most of the shelf (only play/wanting can be section-linked).
5. **Kicker numbering** is internally consistent with footers (good) — the conflict is only kicker-vs-index.

---

## 8. Lessons & learning-records

- **lessons/** (24 pages): the play family (0007–0007g) and the strict-list lesson (0007g) are excellent; the lesson→reference map in index.html covers all 24. **Gap:** the 5 newest docs (motivation, metacognition, ai, note-taking, wanting) have **no dedicated lessons** — the practice layer stops at 0018 + the 0007 family.
- **learning-records/**: 2 entries only. The shelf's own highest-leverage habit (the log) is the most neglected artifact. Make "add a learning record" part of every session's close.

---

## 9. Process & tooling gaps

1. **CONVENTIONS.md exists but is stale** (C4) and silent on the two-scheme numbering problem. It should also state *which* numbering is authoritative.
2. **AR-sync scripts are still not vendored** — `verify-twins.py`, `twin-pipeline.py`, `splice-sections.py` live in `~/.agents/skills/translate-to-arabic/`; the repo has no copy. The last AR sync (wanting twin) used them from the skill dir; a fresh environment can't run the battery.
3. **The translate skill's `maps/` + `PROGRESS.md` infrastructure doesn't exist in this repo** — twin status isn't tracked anywhere in-repo.
4. **Three files carry pre-existing uncommitted edits** (`Archive/Play as recovery Review.txt`, `Archive/Rest and Recovery Review.txt`, `Trascriptions/Productivity is Hard Until You Build Systems Like This.txt`) — commit or revert so `git status` is clean.

---

## 10. Prioritized roadmap (v2)

**P0 — contradictions first (correctness, cheap)**
1. **Fix C1:** make numbering single-scheme (renumber the index to match kickers, or vice versa) + state authority in CONVENTIONS.
2. **Fix C2:** `Reference 9` → `08` in wanting-vs-liking EN + AR (المرجع ٨).
3. **Fix C3:** add Sensitization, Cold reproduction, Extinction, Urge surfing to the glossary.
4. **Fix C4:** update CONVENTIONS (17 docs, 3 twins, doctype decision).

**P1 — content, high value**
5. **memory-techniques:** add the "sleep is the second half of memory" callout (3 lines + link).
6. **blooms:** rebuild on the h2 spine (fix C6) so it's section-linkable.
7. **skill-acquisition:** Hattie & Timperley feedback callout + transfer sentence.
8. **self-management:** attention-residue callout (Leroy) + link back to rest's shutdown ritual.
9. **orders-of-learning:** the desirable-difficulties "feels worse but works" citation.
10. **motivation doc:** add Vallerand passion types (the play strict list already depends on the concept).

**P2 — content, medium value**
11. **play-as-recovery:** split core vs appendix (fiqh detail + full reference list) or add a "what to read when" quick-start — it's 3.3× the next-biggest doc.
12. **study-advice:** add the 2/7/30 spacing template; strip `1 ·`–`16 ·` ordinals.
13. **Note-taking lesson (0019)** — the newest doc has no lesson.
14. **learning-myths:** one "why these myths persist" line (fluency-illusion cross-link).

**P3 — Arabic**
15. Glossary twin (the terminology gate) → then study-advice, memory-techniques, learning-system.
16. Vendor the AR-sync scripts + a `maps/`/`PROGRESS.md`-style twin-status ledger into the repo.

**P4 — process**
17. Renumber index (see P0-1) — keep index.html's lesson map authoritative.
18. Add a learning record each session (currently 2 of …).
19. Clean up the three pre-existing modified files.
20. Add h2 section ids to the 5 newest docs (motivation, metacognition, ai, note-taking — wanting already has them) so the shelf can section-link.

---

## 11. One-line summary (v2)

The shelf's *content* is now strong and current (17 docs, evidence-backed, well cross-linked, honest about its science) — the work that remains is **consistency and correctness**: fix the two numbering schemes that contradict each other (C1), the wrong cross-reference (C2), the glossary promises (C3), and the stale conventions (C4), then close the small evidence gaps (sleep↔memory, feedback, attention-residue) and keep the practice layer (lessons, learning records, AR twins) marching behind the reference layer.
