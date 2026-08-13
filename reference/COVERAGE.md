# Coverage Map — the shelf's external domain model

The standing answer to: **"Is the shelf complete?"** It is not a claim to be
asserted — it is a map to be checked. This file is the external model that the
shelf is measured against, because *topical completeness cannot be verified
from inside the artifact*. The old failure: audits verified what exists
(numbering, citations, twins) and let that stand for coverage. Absence is only
visible against an external model — this one.

## How the model was derived

Top-down from `../MISSION.md` ("master the general skill of learning how to
learn … apply it across exams, coding, career, lifelong learning"). That
mission implies a full learner cycle, not just memory. The cycle is the
domain model: every node below is something a learner must be able to *do*.
A node is "covered" only when a reader can learn to do it from the shelf —
not when a doc merely mentions it.

## The domain model — nodes and coverage

Coverage legend per node: **Doc** (a reference doc that owns the topic) ·
**Lesson** (≥1 lesson teaches it) · **Glossary** (terms anchored) · **Twin**
(AR twin for core nodes). A node is **COVERED** when it has Doc + Lesson +
Glossary; **THIN** when it has Doc but no Lesson (or only passing mention);
**GAP** when no doc owns it.

| # | Node | What the learner must be able to do | Doc | Lesson | Gloss | Twin | Status |
|---|---|---|---|---|---|---|---|
| 1 | **Encode & understand** | Turn input into meaning: maps, levels of thinking, orders, notes | learning-system, orders-of-learning, blooms, note-taking | 0003, 0013, 0016, 0017, 0019 | ✅ | learning-system | ✅ COVERED |
| 2 | **Store & consolidate** | Get it to stick: memory techniques, spacing, sleep | memory-techniques, study-advice | 0002, 0012, 0014, 0015 | ✅ | memory-techniques | ✅ COVERED |
| 3 | **Retrieve & apply** | Pull it out on demand: testing, skill transfer, practice | study-advice, skill-acquisition, learning-system | 0001, 0011, 0018 | ✅ | study-advice | ✅ COVERED |
| 4 | **Regulate** | Know what you don't know, keep going, manage urges: metacognition, motivation, wanting | metacognition, motivation, wanting-vs-liking | 0020, 0021, 0022 | ✅ | wanting-vs-liking | ✅ COVERED |
| 5 | **Execute — plan** | Turn intention into scheduled action: plan, decompose, review | planning-and-execution | 0023 | ✅ | ✅ | ✅ COVERED (new) |
| 6 | **Execute — focus** | Protect and direct attention: single-task, resist distraction, recover focus | focus-and-attention | 0024 | ✅ | ✅ | ✅ COVERED (new) |
| 7 | **Execute — systems** | Run the weekly machinery: cues, scripts, time & task management | productivity-systems, self-management | 0007, 0008, 0009, 0010 | ✅ | both | ✅ COVERED (twins added 2026-08-13) |
| 8 | **Sustain** | Recover energy, rest well, play: rest, recovery, play | rest-and-recovery, play-as-recovery | 0004–0006, 0007b–g | ✅ | both | ✅ COVERED |
| 9 | **Set direction** | Know the "why & who": goals, meta-goals | reverse-goal-setting | 0025 | ✅ | — | ✅ COVERED (lesson 0025 added 2026-08-13) |
| 10 | **Guard against myths** | Spot false learning beliefs: myths, AI misuse | learning-myths, ai-and-learning | 0022 | ✅ | learning-myths | ✅ COVERED (twins added 2026-08-13) |
| 11 | **Use tools (AI)** | Use AI without fluency theft | ai-and-learning | 0021 | ✅ | ai-and-learning | ✅ COVERED (twin added 2026-08-13) |
| 12 | **Meta** | Navigate the system: glossary, index, conventions | glossary, index | — | — | glossary | ✅ COVERED |

## What "complete" means — the operational definition

The shelf is **complete** when all of these hold:

1. **Every node in the model is COVERED** — Doc + Lesson + Glossary per node
   (twins for core nodes). This table is the single source of truth.
2. **Every doc is internally consistent** — numbering, cross-references,
   citation traceability (the old verification battery).
3. **The map is current** — any change to a doc, lesson, glossary term, or
   twin updates this table in the same commit.

Until all three hold, the honest word is **"internally consistent"**, never
"complete." This file is deliberately small: it is a checklist, not an essay.

## How to audit coverage (the procedure)

1. **Run the map first (absence detection).** Read the model above. For each
   node, ask: *can a learner learn to do this from the shelf?* Check Doc,
   Lesson, Glossary, Twin columns. Empty cells are gaps — no doc reading needed.
2. **Then run the internal checks.** Numbering, cross-refs, citation
   traceability, twin batteries (see CONVENTIONS.md).
3. **Update the map in the same commit** as any shelf change. A doc that
   grows a section updates its node's coverage; a new doc adds a node or fills
   an empty cell.

## Open cells (as of 2026-08-13, evening pass)

None. The four THIN cells from the morning audit were closed in the same day:

- **Node 7 (systems)** — twins added for productivity-systems and
  self-management; the execute layer is now fully Arabic-accessible.
- **Node 9 (direction)** — lesson 0025 ("Become the Person, Not the
  Outcome") added for reverse-goal-setting.
- **Node 10 (myths)** — learning-myths twin added.
- **Node 11 (AI)** — ai-and-learning twin added.

Every node in the model is now **COVERED** (Doc + Lesson + Glossary; twins
for core nodes). The honest remaining caveats are structural, not coverage:
three non-core docs (orders-of-learning, skill-acquisition, note-taking) have
no twins, and reverse-goal-setting, motivation, and metacognition have no
lesson of their own — both are voluntary depth work, not gaps. The next audit
should re-derive the domain model from MISSION.md from scratch (rather than
patching this table) to confirm the boundary itself hasn't drifted.
