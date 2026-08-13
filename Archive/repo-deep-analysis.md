# Deep Analysis — the Learn to Learn repository (v3, deepened again)

Date: 2026-08-13 (v3 — after roadmap P0–P4 + the 2026 research pass) · Scope: whole repo (17-doc reference shelf, 25 lessons, learning-records, Archive, Trascriptions, assets) · Focus: **gaps, improvements, and contradictions** — deeper than v2.

> **How v3 differs from v2:** v2's roadmap (numbering, glossary promises, blooms spine, h2 ids, AR twins, vendored scripts, learning record) is fully implemented. This v3 re-audits the *post-roadmap* state and adds a **research-strategy pass**: a claim-anchored survey of foundational papers (`Archive/research-strategy-2026.md` + `Archive/learning-science-research-2026.md`) that found 8 missing landmarks and — the big one — **a scientific contradiction in wanting-vs-liking** (ego-depletion stated as fact; the preregistered replication says otherwise), now fixed. v3's remaining findings are smaller and more structural.

---

## 1. Current state (post-roadmap, post-research)

**Shelf inventory — size, structure, and consistency (recomputed):**
| Doc | KB | h2 | h2 ids | num-heads | Twin |
|---|---|---|---|---|---|
| blooms-six-levels-of-thinking | 7 | 4 | **4/4** | 0 | — |
| learning-myths | 9 | 4 | **1/4** | 0 | — |
| learning-system | 7 | 2 | 2/2 | 0 | ✅ |
| orders-of-learning | 6 | 2 | **0/2** | 0 | — |
| self-management | 7 | 3 | **0/3** | 0 | — |
| memory-techniques | 18 | 2 | 2/2 | 0 | ✅ |
| study-advice | 17 | 6 | 6/6 | 0 | ✅ |
| rest-and-recovery | 36 | 9 | 9/9 | 0 | ✅ |
| productivity-systems | 10 | 6 | **0/6** | 0 | — |
| reverse-goal-setting | 11 | 7 | **0/7** | 0 | — |
| skill-acquisition | 12 | 4 | **0/4** | 0 | — |
| play-as-recovery | 120 | 16 | 16/16 | 0 | ✅ |
| motivation-and-self-determination | 12 | 6 | 6/6 | 0 | — |
| metacognition-and-calibration | 9 | 8 | 8/8 | 0 | — |
| ai-and-learning | 8 | 6 | 6/6 | 0 | — |
| note-taking | 8 | 5 | 5/5 | 0 | — |
| wanting-vs-liking | 37 | 16 | 16/16 | 0 | ✅ |
| learning-to-learn-glossary | 35 | 0 | — | 0 | ✅ |

**Fixed since v2 (verified, not assumed):**
- ✅ C1 numbering: index now matches the docs' kickers (creation order) — zero "Reference N" mismatches anywhere (audited every `Reference/Ref/مرجع N` claim in all 18 docs: all self-consistent now).
- ✅ C2: wanting-vs-liking's "Rest & Recovery (Reference 9)" → 08 in EN + AR (المرجع ٨).
- ✅ C3: Sensitization, Cold reproduction, Extinction, Urge surfing now in the glossary (104 terms).
- ✅ C4/C8: CONVENTIONS current (17 docs, 7 twins, vendored-scripts section, doctype note).
- ✅ C5: all heading ordinals stripped (num-heads = 0 in every doc).
- ✅ C6: blooms rebuilt on the h2 spine (4 h2s, ids).
- ✅ P1 content: memory sleep callout, skill feedback + transfer, self-management attention-residue, orders desirable-difficulties, motivation Vallerand.
- ✅ P2: play quick-start, study-advice 2/7/30 + ordinals stripped (9 glossary refs updated), lesson 0019, myths persistence line.
- ✅ P3: 7 AR twins (glossary, study-advice, memory-techniques, learning-system added), scripts vendored (`reference/scripts/`), `twin-status.md` ledger.
- ✅ P4: h2 ids on the 5 newest docs; learning record 0003; the 3 pre-existing modified files were pure whitespace noise and restored.
- ✅ Research pass: 8 landmark citations added; ego-depletion overclaim corrected in wanting (both twins).

---

## 2. Contradictions found (v3)

### C1. ~~Two numbering schemes~~ **RESOLVED** — verified zero mismatches. Closed.
### C2. ~~Wrong reference 9~~ **RESOLVED** — 08 everywhere. Closed.
### C3. ~~Glossary promises~~ **RESOLVED** — 4 terms added. Closed.

### C4. h2 ids still missing in 6 docs ⚠️ MEDIUM (structural)
The shelf's own section-link convention (established in v2's P4 and enforced by the twin battery) is "every h2 carries a unique id." Still missing: **learning-myths (3/4), orders-of-learning (0/2), productivity-systems (0/6), reverse-goal-setting (0/7), self-management (0/3), skill-acquisition (0/4)** — 23 h2s without ids. These docs can't be section-linked from lessons or other docs; the rest of the shelf can.

**Fix:** add ids to those 23 h2s (same pattern as the 5 newest docs). Pure mechanical work, no content change.

### C5. Lesson→reference map leaves 5 docs unreferenced ⚠️ MEDIUM
The index's "Lessons → references" table covers all 25 lessons but references only **13 of 18 docs**. Five docs are never named by any lesson: **ai-and-learning, learning-myths, reverse-goal-setting, wanting-vs-liking, learning-to-learn-glossary**. (Glossary as a reference tool is fine to omit; the other four are substantive docs with no lesson even touching them.)

**Fix:** at minimum, add the four substantive docs' lessons; or add a "rest on" line in an existing lesson where the doc is implied (e.g. lesson 0003 for learning-myths, 0018 for wanting-vs-liking? no — better: new lessons, see roadmap).

### C6. The ego-depletion overclaim — now fixed, but note the pattern ⚠️ LOW (resolved)
The research pass found wanting-vs-liking stating "suppression produces ego depletion" as established fact; the preregistered multilab replication (Hagger et al., 2016, N = 2,141) found d ≈ 0.04. Fixed in both twins (mechanism now stated as rebound + reactance + rigid-rule bingeing, with Hagger cited as the caveat). **Pattern worth institutionalizing:** when a doc cites a mechanism (not a finding), check whether the *mechanism's* evidence has a replication record. The deep-analysis methodology now does this; a one-line note in CONVENTIONS would make it a standing rule.

### C7. Play doc still 3.3× the next-biggest ⚠️ LOW (unchanged from v2)
Still not split. The strict list (27 rows) is the doc's most-used tool and should stay; the Islamic-fiqh section + full reference list are appendix-grade. Quick-start was added (v2's minimum), so the doc is now *navigable* — the split remains a size/reading-load question, not a correctness one. Downgraded to LOW.

### What is NOT a contradiction (checked and cleared in v3)
- **Cross-doc term usage** (zero-stakes, wanting-feed, liking test, stop signal, triage, 2/7/30): each term is used consistently where it appears; no doc redefines a shared term. The liking test is the most cross-referenced instrument (5 docs) and never drifts.
- **"Reference N" claims** (audited every claim in every doc): all self-consistent post-fix.
- **Ego-depletion wording** after the fix: consistent with Hagger (the doc now *cites the null result as the caveat*).
- **7 twins**: all pass the battery; ratios in band (0.81–0.89).

---

## 3. What's strong now (v3)

1. **The evidence spine is now complete in both directions**: recent evidence (2010–2026, previous survey) *and* the foundations (Craik & Lockhart 1972, Baddeley & Hitch 1974, Tulving & Thomson 1973, Roediger & Karpicke 2006, Flavell 1979, Steel 2007, Zimmerman 2002, Wisniewski 2020). A reader can now trace "increase complexity" → levels of processing, "match your cues" → encoding specificity, "monitoring and control" → Flavell, "keep a log" → Zimmerman. This was the biggest content gap in the whole shelf and it's closed.
2. **The recovery family (rest + play + wanting) is the deepest, most honest treatment in the shelf** — triage defined, stop-signal, urge-triage, denial-backfire with the replication caveat. It now also handles scientific *disagreement* well (the Hagger correction is a model of "here's what the replication says, here's what still stands").
3. **AR twins are now a real layer**: 7 twins, all battery-green, terminology gated by the AR glossary, scripts vendored so a fresh environment can run the gates.
4. **Cross-linking is shelf-wide**: every doc links neighbors; the wanting doc is linked from 9 files; lesson→reference map covers all lessons.

---

## 4. Content audit — doc by doc (v3, deltas only)

### blooms — now structurally sound
- ✅ h2 spine rebuilt, 4 ids. Content still thin (7 KB, fewest words of any doc) but the *shape* is right. The "should blooms absorb or defer to orders-of-learning" boundary question from v2 is still open — they overlap on higher-vs-lower order. Recommend: leave both; add one cross-link sentence each way.
- **Gap:** no lesson references it beyond 0003 (which does reference it — good).

### learning-myths — good content, 3 h2s still lack ids (C4)
- "Why these myths persist" line added (v2 roadmap). Content is complete for 8 myths. Ids are the only remaining issue.

### learning-system — solid, now fully anchored
- Tulving added to retrieval-method section. The doc is small (7 KB) but complete for its role as the system core.

### orders-of-learning — smallest doc, no ids (C4)
- Desirable-difficulties citation added (v2 roadmap). 2 h2s, no ids. The blooms-boundary question (above) is the only open content item.

### self-management — solid, no ids (C4)
- Attention-residue + Steel added. 3 h2s, no ids.

### memory-techniques — evidence-dense, now founded
- ✅ Baddeley & Hitch + Craik & Lockhart added (the research pass's #1–2). Sleep callout present. Nothing else open.

### study-advice — now the best-anchored applied doc
- ✅ 2/7/30 template, ordinals stripped, Roediger & Karpicke origin + Zimmerman log citation added. Complete.

### rest-and-recovery — rich, complete
- Sleep section, wakeful-rest callout, shutdown anchor — all in place. The v2 "burnout checklist" idea (3 lines) is still optional, not a gap.

### productivity-systems — content complete, no ids (C4)
- Weekly-review evidence still not explicitly cited (v2 flagged; the doc leans on the system's own logic + attention evidence). Low priority.

### reverse-goal-setting — grounded, no ids (C4)
- Goal-science section present. Nothing open beyond ids.

### skill-acquisition — good, now feedback-current
- ✅ Hattie & Timperley + Wisniewski 2020. RAIL intact. 4 h2s, no ids (C4).

### play-as-recovery — content-complete, oversized (C7)
- Strict list, scoring system, triage, stop-signal, quick-start — all in. Size (120 KB) is the only open item.

### motivation / metacognition / ai / note-taking / wanting — newest five, all with ids
- ✅ All five have full h2 ids (v2 P4). wanting has the research-pass correction. None has a dedicated lesson (C5) — ai, wanting, and metacognition are the ones that *need* lessons most (they're the deepest new theory).

### Glossary — 104 terms, AR twin exists
- ✅ Terms promised by wanting (4) now present. No open gaps.

---

## 5. Missing topics — what the shelf still doesn't own

1. **Lessons for the newest theory docs (C5)** — ai-and-learning, wanting-vs-liking, metacognition-and-calibration, motivation-and-self-determination, and learning-myths have **no dedicated lessons**, and the lesson map references only 13 of 18 docs. The practice layer has stopped marching behind the reference layer: lessons 0001–0019 map to the older docs, and the four newest substantive docs have zero lessons. **This is the #1 practice-layer gap.**
2. **Sleep as a lesson** — sleep is a section of rest-and-recovery and a callout in memory-techniques, but no lesson teaches "sleep is the second half of memory." Candidates: fold into an existing rest lesson or add one small lesson.
3. **The learning-record culture** — 3 records now (was 2). The shelf's own study-advice lesson argues the log is highest-leverage; the practice is still thin. Institutionalize "one record per session."
4. **Play doc split** (C7) — appendix-grade content still inside the main doc.

---

## 6. Evidence & citation audit (v3)

| Tier | Docs | Notes |
|---|---|---|
| Strong | memory, play, rest, wanting, motivation, metacognition, ai, note-taking, reverse-goal, study-advice, skill | primary sources + landmarks + honest hedging (Hagger caveat is the model) |
| Good | myths, system, productivity, self-management, orders | complete for their claims; a few no-ids structural items |
| Structural | blooms | now has the h2 spine; smallest content |

**Remaining format inconsistencies:** none of substance. The div.references (rest) vs span.cite (everyone else) split is sanctioned in CONVENTIONS. Doctype split resolved in CONVENTIONS text.

---

## 7. Structural & format inconsistencies (v3)

1. **C4 — 23 h2s without ids across 6 docs.** The only remaining structural inconsistency.
2. **C5 — 5 docs unreferenced by the lesson map.** The practice layer's coverage gap.
3. **C7 — play doc size.** Downgraded to LOW (navigable now).

---

## 8. Lessons & learning-records (v3)

- **lessons/**: 25 pages, all mapped in the index. The 0007 family (play) + 0019 (notes) are the newest. **Gap:** no lessons for ai, wanting, metacognition, motivation, myths.
- **learning-records/**: 3 entries. Still thin relative to the shelf's own advice. Make "one record per session" a standing rule.

---

## 9. Process & tooling (v3)

1. **Vendored + ledgered**: `reference/scripts/` (verify-twins, twin-pipeline, splice-sections, density-audit) + `twin-status.md`. A fresh environment can now run the full battery. ✅ (v2's #2–3 closed.)
2. **The replication-check convention is not yet in CONVENTIONS** — the Hagger finding came from the deep-analysis methodology, not a standing rule. Add one line: "when citing a *mechanism*, check its replication record." (C6)

---

## 10. Prioritized roadmap (v3)

**P0 — structural consistency (mechanical, no content risk)**
1. **C4:** add h2 ids to the 23 missing across learning-myths, orders, productivity, reverse-goal, self-management, skill-acquisition.
2. **CONVENTIONS:** add the replication-check rule (one line) + note the lesson-map coverage expectation.

**P1 — practice layer (the #1 gap: lessons for new theory)**
3. **Lesson 0020 — wanting-vs-liking** (the 2×2, the urge as triage, deny-the-action-not-the-urge). The most-requested topic in the user's own sessions.
4. **Lesson 0021 — AI & learning** (Bastani vs Kestin: answer-machine vs tutor; generation rule).
5. **Lesson 0022 — myths** (the fluency-illusion mechanism behind all 8 myths — ties myths to metacognition).
6. Optionally **lesson 0023 — metacognition** (predict-then-test loop) and **0024 — motivation** (action-first). Only if P1's first three land cleanly.
7. Update the index lesson map for the new lessons; update the "next" chain in 0019.

**P2 — content polish (small)**
8. blooms ↔ orders boundary sentence (one link each way).
9. productivity: one weekly-review citation (optional).

**P3 — learning-record culture**
10. Add a learning record for this session (research + deep-analysis v3).

**P4 — deferred / explicit non-goals**
11. Play doc split (C7) — stays open; quick-start makes it navigable.
12. More AR twins — 10 docs still lack them; do **motivation** and **metacognition** next if Arabic coverage is a priority (they're the most-read new theory docs), tracked in `twin-status.md`.

---

## 11. One-line summary (v3)

The shelf is now **content-complete and consistent**: numbering unified, cross-references verified, glossary promises kept, 7 twins green, and — from the research pass — every core claim traces to its originating paper while the one overclaim (ego-depletion) was caught and corrected. What remains is **structural polish** (23 missing h2 ids) and **the practice layer's coverage gap** (no lessons for the newest theory docs — wanting-vs-liking, AI, myths are the natural next three).
