# 0003 — Deep-Analysis Roadmap Applied

## Date
2026-08-13

## Topic
Applying the repo deep-analysis roadmap — contradiction fixes, content upgrades, Arabic twin expansion

## Context
The deep analysis (`Archive/repo-deep-analysis.md`) surfaced contradictions, gaps, and structural debt across the shelf. This session applied its roadmap P0–P4.

## Key insight / decision
**Contradictions outrank new content.** The two highest-severity findings were consistency bugs, not missing material: the index numbered docs pedagogically while docs self-numbered by creation order (7 docs disagreed), and a wrong cross-reference ("Reference 9" for rest-and-recovery, actually 08) had been introduced into the new wanting-vs-liking doc. Both were cheap to fix and both would mislead every future reader. Lesson: after adding a doc, re-verify the cross-reference *numbers* it carries — not just its links.

**AR twins were the highest-leverage content addition.** The shelf went from 3 twins to 7 in one session (glossary, study-advice, memory-techniques, learning-system). Each twin requires: identical h2 ids in both files (the battery *fails* on id-less h2s — both files must carry the same ids), a `lang-switch` line in **both** directions (EN docs that never had a twin lack the AR link), and house terminology harvested from existing twins (الرغبة/الاستمتاع for wanting/liking), not invented per-doc. The twin battery (`verify-twins.py`) is now vendored in-repo (`reference/scripts/`) with a `twin-status.md` ledger so syncs don't depend on the skill being installed.

## Evidence
- Deep analysis C1: index renumbered to match doc kickers (creation order).
- C2: "Reference 9" → 08 in wanting-vs-liking EN + AR.
- C3: 4 glossary terms the wanting doc promised but lacked (Sensitization, Cold reproduction, Extinction, Urge surfing) — added.
- P1 content: memory sleep callout (diekelmann & Born), blooms rebuilt on h2 spine (was the only doc with zero h2s), skill-acquisition feedback/transfer citations, self-management attention-residue (Leroy), orders desirable-difficulties, motivation Vallerand.
- P2: play quick-start block, study-advice 2/7/30 template + 16 ordinals stripped (9 glossary refs updated), lesson 0019 (note-taking), myths persistence line.
- P4: h2 ids added to the 4 newest docs (wanting-vs-liking already had them).

## Revises
0001-reference-structure-decision (implicitly — the shelf grew from 13 to 17 docs + 7 twins)

## Next
- 10 docs still lack twins (blooms, myths, orders, metacognition, note-taking, productivity, self-management, motivation, reverse-goal, skill-acquisition, ai) — the ledger in `reference/twin-status.md` tracks them.
- The 3 pre-existing modified files (Archive/* Review.txt, Trascriptions/*.txt) remain uncommitted — decide whether to commit or discard.
- Deep analysis flagged: memory doc sleep link (now added), Hattie & Timperley feedback science (skill-acquisition now cites it), attention-residue (now in self-management), play doc still oversized (3.3× — split decision still open).
