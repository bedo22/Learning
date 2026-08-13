# Twin Status — Arabic Twins Ledger

Status of every EN reference doc and its Arabic twin. The EN doc is authoritative;
the AR twin mirrors it 1:1 (SYNC, don't append). Updated whenever a twin is
created or synced. Run the gate battery on any pair before committing:

```
python3 reference/scripts/verify-twins.py reference/<doc>.html reference/ar/<doc>.html
```

Legend: **✅ synced** (all gates green) · **🟡 stale** (EN changed since last sync) · **— none** (no twin yet)

| Ref | EN doc | AR twin | Status |
|---|---|---|---|
| 01 | `blooms-six-levels-of-thinking.html` | — | — none |
| 02 | `learning-myths.html` | — | — none |
| 03 | `learning-system.html` | `ar/learning-system.html` | ✅ synced |
| 04 | `orders-of-learning.html` | — | — none |
| 05 | `metacognition-and-calibration.html` | — | — none |
| 06 | `memory-techniques.html` | `ar/memory-techniques.html` | ✅ synced |
| 07 | `study-advice.html` | `ar/study-advice.html` | ✅ synced |
| 08 | `rest-and-recovery.html` | `ar/rest-and-recovery.html` | ✅ synced |
| 09 | `note-taking.html` | — | — none |
| 10 | `productivity-systems.html` | — | — none |
| 11 | `self-management.html` | — | — none |
| 12 | `motivation-and-self-determination.html` | — | — none |
| 13 | `reverse-goal-setting.html` | — | — none |
| 14 | `skill-acquisition.html` | — | — none |
| 15 | `ai-and-learning.html` | — | — none |
| 16 | `play-as-recovery.html` | `ar/play-as-recovery.html` | ✅ synced |
| 17 | `wanting-vs-liking.html` | `ar/wanting-vs-liking.html` | ✅ synced |
| 18 | `planning-and-execution.html` | `ar/planning-and-execution.html` | ✅ synced |
| 19 | `focus-and-attention.html` | `ar/focus-and-attention.html` | ✅ synced |
| — | `learning-to-learn-glossary.html` | `ar/learning-to-learn-glossary.html` | ✅ synced |

**To create a new twin:** follow the translate-to-arabic skill (TRANSLATE mode);
mirror the EN h2 ids exactly, add the `lang-switch` line to BOTH files, use the
twin's established terminology (الرغبة/الاستمتاع for wanting/liking, etc.), and
pass every gate of `verify-twins.py` (heading parity, identical h2 ids, AR/EN
char ratio in the 0.75–0.97 band, links resolve both directions).

**To sync a stale twin:** follow the skill's SYNC mode — bring the twin fully
current (missing sections added, renamed sections renamed, tables rebuilt), never
patch-only. Re-run the gate battery after.
