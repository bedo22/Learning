# Reference Shelf — Doc-by-Doc Analysis
_Date: 2026-08-19 · Reviewer scope: all 22 HTML docs · Post-recovery state (play/rest/wanting restored & committed)_

This file records a one-by-one review of every doc on the shelf: what it does well,
what questions/sections are missing, content gaps, design notes, and the highest-value
improvements. Shelf-wide findings come first because they repeat across docs.

---

## 0. Shelf-wide findings (fix once, benefits every doc)

| # | Finding | Scope | Priority |
|---|---------|-------|----------|
| S1 | **8 content docs have no Arabic twin**: blooms, evidence-base, metacognition, motivation, note-taking, orders-of-learning, reverse-goal-setting, skill-acquisition (index is meta, EN-only is fine) | AR coverage | HIGH |
| S2 | **rest-and-recovery has ZERO digest links** despite ~20 of its papers having digests (raichle, immordino-yang, wilson, fox, dewar, weng, diekelmann-born, geurts-sonnentag, brodt…). The link-sources.py runs never linked this doc | evidence plumbing | HIGH |
| S3 | **The "standard quartet" (Worked example · Failure modes · Principles · Summary) exists in only 4 docs**: focus-and-attention, planning-and-execution, play-as-recovery, wanting-vs-liking. These four are also the most mature docs — the quartet is what made them good | structure | HIGH |
| S4 | **Digest-link coverage is wildly uneven**: play 68, memory 35, wanting 34, focus 24 vs planning 2, self-management 2, ai-and-learning 2, skill-acquisition 3, note-taking 4, reverse-goal-setting 4. Docs whose backbone papers HAVE digests aren't linked to them | evidence plumbing | HIGH |
| S5 | **Inline lang-switch missing on 6 docs** (blooms, metacognition, motivation, orders, reverse-goal-setting, skill-acquisition) — mostly the same docs missing AR twins, so fixing S1 fixes this | nav consistency | MED |
| S6 | **Thin docs**: learning-system (844 words), orders-of-learning (799), blooms (869), self-management (934), note-taking (949) carry core curriculum weight at half the depth of their siblings | depth | MED |
| S7 | **Glossary is flat** — 4,489 words with zero H2 structure. No letter groups, no topic groups, no TOC | navigation | MED |
| S8 | **ai-and-learning under-links its own backbone**: the two RCTs (Bastani, Kestin) are the doc's central evidence and their digests exist, yet only 2 digest links appear in the doc | evidence plumbing | MED |
| S9 | **Back-to-top / prev-next nav is inconsistent** across docs (present on some, absent on siblings) | nav consistency | LOW |
| S10 | **evidence-base claims "156 source digests"** — this number is hand-maintained and will drift; consider generating it from `ls sources/*.md \| wc -l` at build time or noting the count is as-of-a-date | maintenance | LOW |

---

## 1. play-as-recovery — the flagship
**Profile:** 14 H2 · 32 H3 · ~15,300 words · 68 digest links · AR twin ✓

**Strengths:** The deepest doc on the shelf and the model for the quartet structure.
Full history table with 12+ landmark papers, honest counterarguments box, strict list
with scored verdicts, Islamic framing section unique to this shelf, rest-palette callout,
graded-properties clarification, mastery–play disambiguation, stop-signal mechanics,
meaning trap. Survived restructuring well; TOC present.

**Missing questions / sections:**
- No "how to measure progress" section — the doc says play builds recovery assets and mastery compounds, but never defines how a reader tracks that over weeks (a 4-week self-experiment template would fit the shelf's diagnostic style).
- The strict list covers indoor solo & screen plays — there is no companion outdoor/social list, even though the rest-palette names body/heart channels. A short "outdoor & social plays, judged" table would close the loop.
- Digital-play section is strong on motive but never addresses *dose* (how much screen-play is compatible with recovery before wanting-feeds creep back).

**Content gaps:** The bumblebee/animal-play evidence is cited in history but the "play across species → play as baseline equipment" argument is never spelled out for the adult reader.

**Design:** Longest doc on the shelf (~15k words). Consider whether the strict list (27 rows + scoring legend + worked example) deserves its own page — it is a tool, not narrative — with the main doc linking to it. Otherwise the restructure (triage up, history down) reads well.

---

## 2. rest-and-recovery
**Profile:** 11 H2 · 20 H3 · ~6,400 words · **0 digest links** · AR twin ✓

**Strengths:** Rich h3 layer (Justin Sung case study, detachment-vs-flow, mastery compounding,
recovery menu by time-available, student-specific section, sleep timing around exams).
The guard callout and marker-not-mechanism clarifications hardened the two riskiest readings.
Sleep section now carries an honest citing-note (Lutz unverifiable → Brodt 2023 verified).

**Missing questions / sections:**
- **No Failure-modes section** (the quartet gap). "Why recovery fails when you need it most" partially covers it, but a named failure-modes table (recovery paradox, fake rest, rumination masquerading as rest, oversleeping) would match sibling docs.
- No Principles list (the shared constants that sibling docs echo).
- Micro-recovery exists as an h3 but has no concrete protocol card (the 90-minute cycle: what to do at each break).

**Content gaps:** The rest-palette lives in the PLAY doc, not here — a reader landing on Rest & Recovery never learns the palette framing. Either add a compact version here or a prominent cross-link, since "palette of needs" is arguably rest vocabulary.

**Design / plumbing:** **S2 — zero digest links is the single worst plumbing gap on the shelf.** Every major claim here (DMN, wakeful rest meta, sleep consolidation, four recovery experiences) has a verified digest sitting unused in `sources/`. Run link-sources or add manually.

---

## 3. wanting-vs-liking
**Profile:** 16 H2 · 3 H3 · ~5,100 words · 34 digest links · AR twin ✓

**Strengths:** Complete quartet, full history arc with the taste-reactivity callout answering
"how did they know dopamine isn't pleasure," 2×2 matrix, urge-triage protocol (deny/triage/
redirect), denial-backfire mechanisms with the ego-depletion caveat done honestly, clinical
tails, education-exploitation section (new), build-liking section (new).

**Missing questions / sections:**
- The 2×2 names four cells but the doc never gives a *worked diagnosis walk-through of another person* (parent/child/friend) — readers will first apply this to someone else; a short other-person example would meet them where they start.
- "How to build liking" arrived late (added recently); it could forward-reference the play doc's menu instead of standing alone — check for duplication with play's "start playing" section.

**Content gaps:** Nothing major. The strongest doc after play.

**Design:** Fine. Dense but navigable.

---

## 4. focus-and-attention
**Profile:** 11 H2 · 2 H3 · ~2,400 words · 24 digest links · AR twin ✓

**Strengths:** Model citizen: complete quartet, distraction taxonomy, attention residue,
phone effect, honest training-evidence answer, worked example under attack.

**Missing questions / sections:**
- No coverage of *environment design beyond the phone* (noise, interruptions by people, tab hygiene) — the taxonomy names attackers but the countermeasures lean phone-centric.
- Flow is mentioned via neighbors but focus doc never says when flow is the WRONG target (it imports the detachment-vs-flow insight only implicitly).

**Content gaps:** Minor. Third-most-complete doc.

---

## 5. planning-and-execution
**Profile:** 9 H2 · 3 H3 · ~2,200 words · **only 2 digest links** · AR twin ✓

**Strengths:** Complete quartet. Intention–action gap, planning fallacy, decomposition,
trigger-attached plans, plan–do–review loop, concrete exam-block worked example.

**Missing questions / sections:**
- Nothing structural. Content-wise: no treatment of *replanning triggers* (when is changing the plan discipline vs self-deception?) — the review loop touches it but a named rule would help.

**Content gaps / plumbing:** **S4 — Gollwitzer implementation-intentions, planning fallacy, and goal-setting papers have digests that aren't linked here.** The doc's whole spine is implementation intentions; its digest exists unlinked.

---

## 6. study-advice
**Profile:** 6 H2 · 19 H3 · ~2,300 words · 12 digest links · AR twin ✓

**Strengths:** The hub doc — 16 lessons, effectiveness ranking, 2/7/30 spacing rhythm,
exam-day tactics, AI-era section. The "techniques → systems" reframe is the right message.

**Missing questions / sections:**
- No failure-modes section despite being the most habit-prone domain (cramming relapse, highlight addiction, rereading comfort).
- Lesson-to-doc cross-links are implicit. Each lesson should end with "deep dive: X doc" — currently only some do.

**Content gaps:** Overlap management: spacing details duplicate learning-system; memorization duplicates memory-techniques; AI duplicates ai-and-learning. This is acceptable for a hub, but each overlap should be an explicit pointer, not parallel prose that can drift apart.

---

## 7. memory-techniques
**Profile:** 2 H2 · 14 H3 · ~2,400 words · 35 digest links · AR twin ✓

**Strengths:** Best digest backing after play. Working-memory weight-limit honesty,
six strategies each with 2021–2026 evidence nuance, handwriting/offload coverage,
sleep link.

**Missing questions / sections:**
- Quartet gap: no worked example, failure modes, principles, summary. For a techniques doc, a "which technique for which material" decision table is the missing crown — the strategies are listed but selection guidance is thin.
- Memory palace / link method live in study-advice h3s, not here — odd home for technique detail.

**Design:** h3-heavy (14) under only 2 h2 — the outline is top-heavy; grouping strategies under sub-headings would help scanning.

---

## 8. metacognition-and-calibration
**Profile:** 8 H2 · 1 H3 · ~1,280 words · 21 digest links · **AR twin ✗**

**Strengths:** Monitoring/control split, fluency illusion, retrieval-as-instrument,
region of proximal learning, self-explanation, learning log as calibration device.
Well-sourced (21 digests).

**Missing questions / sections:**
- Quartet gap (no worked example / failure modes / summary as named sections).
- No treatment of *calibrating confidence before exams* (predicting your grade — the classic exercise) even though "predict the exam" exists in blooms doc; these two should reference each other.

**Plumbing:** High-value doc missing its AR twin (S1). Arabic learners lose the single best antidote to the fluency illusion.

---

## 9. motivation-and-self-determination
**Profile:** 6 H2 · 6 H3 · ~1,540 words · 10 digest links · **AR twin ✗**

**Strengths:** Type-over-amount framing, SDT three needs, Locke & Latham, learning vs
performance goals, harmonious vs obsessive passion, self-concordance, action-first law.

**Missing questions / sections:**
- Quartet gap.
- No bridge to procrastination (emotional-regulation view lives as an h3 in self-management) — motivation is where procrastination belongs; pull it in or cross-link explicitly.
- Wanting-vs-liking intersection exists but the *amotivation* cell (depleted quadrant) isn't connected to the clinical flags.

---

## 10. productivity-systems
**Profile:** 6 H2 · 4 H3 · ~1,400 words · 6 digest links · AR twin ✓

**Strengths:** The 4+1 parts structure is memorable; cue-based architecture over willpower;
weekly ritual; toxic-productivity trap; recovery as the "sneaky part" — correct and rare.

**Missing questions / sections:**
- Quartet gap: no worked example (a real person's week built through the 4 parts would be the doc's most valuable addition), no failure modes (system decay, over-optimizing, tool-hopping).
- Tool neutrality is claimed but never demonstrated (no example stack).

---

## 11. ai-and-learning
**Profile:** 6 H2 · 2 H3 · ~1,060 words · **only 2 digest links** · AR twin ✓

**Strengths:** The two-RCT bracket structure (Bastani harm / Kestin gain) is the clearest
AI-learning framing anywhere; operating rules; calibration warning tied to metacognition.

**Missing questions / sections:**
- Quartet gap: no worked example (a study session with AI done right vs wrong side-by-side is begging to exist), no failure modes (fluency trap variants: explain-seeking, summary-trust, answer-laundering).
- Missing: AI for *feedback* vs AI for *answers* distinction — the doc implies it but never names feedback-seeking as the safe channel explicitly enough.

**Plumbing:** S8 — Bastani and Kestin digests exist; link them. This doc's authority rests entirely on those two studies.

---

## 12. learning-myths
**Profile:** 4 H2 · 5 H3 · ~1,240 words · 12 digest links · AR twin ✓

**Strengths:** Eight myths settled with sources; the time/talent myth opening is the right
emotional entry; growth mindset handled with appropriate nuance.

**Missing questions / sections:**
- Candidate myths absent: "I work better under pressure" (deadline crunch), "highlighting = studying," "I'll remember this because it's important to me" (importance ≠ encoding), "sleep is lost study time."
- No "how to debunk politely" guidance — readers meet these myths in friends/teachers; one paragraph on pushing back without condescension fits the shelf's voice.

---

## 13. note-taking
**Profile:** 5 H2 · 1 H3 · ~950 words · 4 digest links · **AR twin ✗**

**Strengths:** Encoding-vs-transcription frame, ICAP framework, methods-when-they-earn-place,
notes→retrieval pipeline, AI-era section.

**Missing questions / sections:**
- Thin overall (S6). Missing: review cadence (when do notes get re-read?), the difference between lecture notes and reading notes, and a worked example of one real note transformed through the pipeline.
- Handwriting-vs-typing evidence lives in memory-techniques — cross-link rather than partial-duplicate.

---

## 14. learning-system
**Profile:** 2 H2 · 3 H3 · ~840 words · 22 digest links · AR twin ✓

**Strengths:** Correctly identifies encoding as the prize; forgetting curve; method × frequency;
opportunistic retrieval for professionals; curiosity amplifier.

**Missing questions / sections:**
- **Thinnest core doc on the shelf (S6)** — this is the foundation everything else cites, yet it's 844 words. Deserves: interleaving (currently homeless — mentioned nowhere as its own mechanism), desirable-difficulty placement (lives in orders-of-learning), a schema/prior-knowledge section (encoding depends on what you already know — completely absent shelf-wide!), and the quartet.
- The absence of prior-knowledge/advance-organizer content is the biggest single content gap on the shelf.

---

## 15. orders-of-learning
**Profile:** 2 H2 · 2 H3 · ~800 words · 8 digest links · **AR twin ✗**

**Strengths:** Higher-order beats lower-order with the honest "feels worse, works" framing;
habit-breaking section is a genuinely useful angle.

**Missing questions / sections:**
- Thin (S6). Should align explicitly with Bloom's levels (they're siblings teaching the same hierarchy from different angles — neither links the other!). Add question stems per order ("generate, critique, transfer" examples).
- No worked example of converting a lower-order study session into a higher-order one.

---

## 16. blooms-six-levels-of-thinking
**Profile:** 4 H2 · 0 H3 · ~870 words · 6 digest links · **AR twin ✗**

**Strengths:** Start-at-level-5 advice is contrarian and correct; effort-is-the-mechanism;
predict-the-exam tip.

**Missing questions / sections:**
- Thin (S6). Missing: verb lists / question stems per level (the practical toolkit), common misuses (treating levels as rigid stages, "knowledge = worthless"), assessment alignment (what exam verbs demand which level).
- Zero h3s — flattest doc on the shelf; needs internal structure.
- Cross-link to orders-of-learning is the obvious merge-or-link decision (see #15).

---

## 17. skill-acquisition
**Profile:** 4 H2 · 4 H3 · ~1,530 words · 3 digest links · **AR twin ✗**

**Strengths:** RAIL framework is a good scaffold; theory:practice ratio rule of thumb;
feedback-type discussion; latent learning; deliberate-practice demystified.

**Missing questions / sections:**
- Quartet gap. Missing: plateau handling (the most common mid-skill crisis), transfer-near-vs-far, and practice-scheduling (spacing applies to motor/cognitive skills too — link learning-system).
- Only 3 digest links despite deliberate-practice literature being well covered in sources.

---

## 18. reverse-goal-setting
**Profile:** 7 H2 · 6 H3 · ~1,550 words · 4 digest links · **AR twin ✗ (profile correction)**

**Strengths:** Future-self/meta-goal framing distinguishes it from generic goal advice;
force-field analysis; bottleneck principle; conservative timelines.

**Missing questions / sections:**
- Quartet gap. Missing: review cadence for goals (when do you revisit?), what to do when the future-self vision changes (identity drift is normal), and the motivation-doc bridge (self-concordance is motivation vocabulary).
- **Note:** earlier scans flagged this doc as having an AR twin; it does not. Add to the S1 list.

---

## 19. self-management
**Profile:** 3 H2 · 2 H3 · ~930 words · 2 digest links · AR twin ✓

**Strengths:** Honest hub doc — points outward to time/task/focus specialists; procrastination-
is-emotional h3 is the right seed.

**Missing questions / sections:**
- Thin (S6) and the shallowest linker (2 digests). As the entry-point doc it should have the shelf's best "where do I go for X" routing table — currently the intersection prose does this weakly.
- Procrastination deserves promotion from h3 to full section (emotional-regulation view + temporal discounting + the 5-minute start bridge).

---

## 20. evidence-base (Reference 20)
**Profile:** 7 H2 · 13 H3 · ~1,900 words · 23 digest links · **AR twin ✗**

**Strengths:** Trust tiers, verification pipeline, digest anatomy, access guide, key-papers-by-topic.
The right meta-doc at the right time (post-digest-backfill).

**Missing questions / sections:**
- No AR twin (meta-doc, lower priority than content docs — but the trust-tier table is exactly what an Arabic-first reader needs to trust the shelf).
- The digest count (156) is hand-written (S10). The "key papers by topic" lists will rot as batches land — consider marking it "as of 2026-08."
- Template strings (`{DOI}` examples) caused verify-links noise — now filtered in the script, but the doc could use real example DOIs instead, killing the special-case entirely.

---

## 21. index
**Profile:** 3 H2 · ~840 words · meta doc

**Strengths:** Shelf map with lessons→references table; conventions section; all 22 docs
referenced including Reference 20.

**Missing questions / sections:**
- No "start here" path recommendation (first-time visitors need: read learning-system → study-advice → pick your problem doc). The lesson map implies it but never says it.
- Digest-count/status banner would help returning readers know the shelf's evidence posture at a glance.

---

## 22. learning-to-learn-glossary
**Profile:** 0 H2 · ~4,500 words · AR twin ✓

**Strengths:** Definitions are written in the shelf's voice with cross-links into docs —
genuinely useful, not dictionary filler.

**Missing questions / sections:**
- **Flat structure (S7):** 4,500 words with no H2 groups. Add alphabetical anchor groups or topic clusters (motivation terms / memory terms / recovery terms) + a mini-TOC. Currently the only navigation is browser find.
- Missing entries spotted while reviewing docs: *interleaving*, *desirable difficulty*, *prior knowledge / schema*, *ICAP*, *region of proximal learning* (used in metacognition doc), *implementation intention* (present?), *extinction* (defined in wanting doc, glossary?).

---

## Prioritized improvement plan (if working shelf-wide)

1. **P1 — Plumbing sweep (half a day):** link digests into rest-and-recovery (0→~20),
   planning-and-execution, ai-and-learning (Bastani/Kestin), skill-acquisition,
   self-management, note-taking. Fixes S2/S4/S8 mechanically.
2. **P2 — Quartet rollout:** add Worked example / Failure modes / Principles / Summary to
   the 6 mature-but-incomplete docs (rest, study-advice, memory-techniques, metacognition,
   motivation, productivity-systems, ai-and-learning, skill-acquisition, reverse-goal-setting).
   Use focus-and-attention as the template.
3. **P3 — AR twins for 8 content docs** (metacognition, motivation, note-taking,
   orders-of-learning, blooms, skill-acquisition, reverse-goal-setting, evidence-base),
   using the established twin workflow + verify-twins gate.
4. **P4 — Content gaps that change the shelf's correctness:** prior-knowledge/schema section
   (learning-system), interleaving ownership, Bloom↔orders-of-learning alignment,
   procrastination promotion in self-management, glossary regrouping + missing entries.
5. **P5 — Design polish:** inline lang-switch consistency, prev-next on all docs,
   glossary TOC, "start here" path on index.

---
*Generated as part of the 2026-08-19 recovery + audit session. All findings above were
verified against the live files (structure extraction + link/digest counts), not from memory.*
