# Lesson Plan — Learn to Learn

The knowledge base is complete: 11 topic reference docs + an 80-term glossary, all sourced from Dr. Justin Sung's 8 transcripts. This document plans the **next phase**: turning that knowledge into skills through interactive lessons.

> See the [teaching philosophy](./MISSION.md) for the principles behind this plan.

---

## Organizing logic

Two principles govern the sequence:

1. **Lead with the reframe, then rest & plan, then the pillars.** Sung says master the three pillars in order — enablers → retrieval → encoding. But for a motivated adult learner (a freelancer — not a struggling student), starting with time management feels dry and disconnected from "learning." So we open with a short **Phase 0 (Reframe)** — three low-difficulty, high-impact knowledge lessons that create buy-in. *Then* we bring **Phase 1 (Rest & Plan)** forward — not in Sung's original order, but because the user's immediate need (struggling with rest) puts it in their zone of proximal development. *Then* the pillars follow in Sung's recommended order.

2. **Every lesson models what it teaches.** The retrieval-practice lessons *use* retrieval practice to teach retrieval practice. The mind-mapping lesson *is* a nonlinear map. This meta-quality reinforces storage strength without extra effort.

The three learning pillars (Sung's framework):
- **Enablers** — time, tasks, focus → [`self-management`](./reference/self-management.html), extended by rest/recovery, productivity, reverse goal setting
- **Retrieval** → [`learning-system`](./reference/learning-system.html)
- **Encoding** → [`orders-of-learning`](./reference/orders-of-learning.html) + [`memory-techniques`](./reference/memory-techniques.html), extended by mind mapping & skill acquisition

---

## Phase map — 18 lessons across 6 phases

| # | Lesson (one tangible win) | Phase | Skill focus | Primary reference | Widget |
|---|---|---|---|---|---|
| 01 | Studying isn't learning | 0 Reframe | Audit your methods: sort "activity" from "outcome" | study-advice, learning-system | quiz |
| 02 | Your memory is a leaky bucket | 0 Reframe | Sketch the forgetting curve; explain why cramming fails | learning-system | predict |
| 03 | Climb Bloom's from the top | 0 Reframe | Name the 6 levels; explain why "evaluate first" works | blooms-six-levels | quiz |
| 04 | Real rest vs fake rest | 1 Rest & Plan | Tell real recovery from fake rest; audit your breaks | rest-and-recovery | quiz |
| 05 | The recovery break | 1 Rest & Plan | Pick the right break (2/10/30 min) for between sessions | rest-and-recovery, memory-techniques | quiz |
| 06 | Leave work at work | 1 Rest & Plan | Script an end-of-day transition that needs no willpower | rest-and-recovery, productivity-systems | quiz |
| 07 | Plan rest, not just work | 1 Rest & Plan | Plan a day/week with rest anchors built in | productivity-systems, self-management | checklist |
| 08 | Find your lost 10 hours | 2 Enablers | Track one day's time; spot the leaks | self-management (time) | checklist |
| 09 | Important ≠ urgent | 2 Enablers | Sort real tasks into the Eisenhower quadrants | self-management (tasks) | quiz |
| 10 | Procrastination is an emotion | 2 Enablers | Name the feeling; deploy one if-then script | self-management (focus), productivity-systems | quiz |
| 11 | Recognition is the imposter | 3 Retrieval | Tell recognition from recall; stop fooling yourself | learning-system, study-advice | quiz |
| 12 | The 2-minute brain dump | 3 Retrieval | Do a free-recall dump; find your gaps | study-advice, learning-system | free-recall |
| 13 | Match the method to the mission | 3 Retrieval | Pick the right retrieval strategy for a real goal | learning-system, study-advice | quiz |
| 14 | Your 15-second window | 4 Encoding | Explain working-memory limits; why schemas lighten load | memory-techniques | quiz |
| 15 | Think on paper | 4 Encoding | Offload thinking onto paper in one real session | memory-techniques, study-advice | guided exercise |
| 16 | Build the web, not the dots | 4 Encoding | Make an analogy + Feynman-explain a concept | orders-of-learning, study-advice | predict + make |
| 17 | Maps, not lists | 4 Encoding | Spot mind-map levels 0 vs 2; know higher-order is the key | skill-acquisition, orders-of-learning, blooms | quiz |
| 18 | Learn a skill with RAIL | 5 Integrate | Diagnose your RAIL stage for a real skill; pick the action | skill-acquisition | quiz |

### Phase summaries

- **Phase 0 — Reframe (3 lessons)** — Low-difficulty knowledge that shifts the mental model. The "why" before the "how." Creates buy-in.
- **Phase 1 — Rest & Plan (4 lessons)** — Brought forward from the user's immediate need. Real recovery vs fake rest, the recovery break between focus sessions, the end-of-day transition, and planning rest into the week.
- **Phase 2 — Enablers (3 lessons)** — Time, tasks, focus. Sung's foundational pillar. Skills-based, with self-audits.
- **Phase 3 — Retrieval (3 lessons)** — The first pillar that pays off immediately. Desirable difficulty: practice retrieval.
- **Phase 4 — Encoding (4 lessons)** — The big prize: flattening the forgetting curve from the start. Highest-leverage but slowest skill.
- **Phase 5 — Integrate (1 lesson)** — Apply the full system to learning a new skill (RAIL).

---

## Design constraints (baked into every lesson)

- **One skill, one win.** Each lesson teaches a single skill (knowledge is only what that skill requires). The win is a concrete thing you can *do* after — not just "understand."
- **Short & within working memory.** A lesson reads in ~5 min; practice takes ~2-5 more. No lesson covers a whole reference doc.
- **Interactive feedback loop.** Every lesson uses `assets/lesson.js` widgets — the **quiz** (multiple-choice with `data-answer` + `data-explain` reveal) and the **predict** (text-input match). New interaction types become new components in `assets/` (never inline code that duplicates).
- **Equal-length quiz answers.** Every quiz option is the same word/character count so formatting gives no clue.
- **Domain interleaving for transfer.** Examples alternate between **front-end/freelancing** (the user's work), **exams/certifications**, and **general life** — so skills transfer broadly and build storage strength.
- **Spacing.** One lesson per session, with real time between — so each builds on consolidated memory, not fresh fluency.
- **Retrieval as the meta-mechanism.** Later lessons revisit earlier concepts in new contexts (L08 revisits L07; L12 revisits L03; L13 revisits L03+L12) — interleaving that strengthens storage.
- **Each lesson links out** to reference doc(s) + adjacent lessons. Each recommends a **primary source** (the specific YouTube video). Each closes with a `section.teacher` reminder to ask follow-up questions.

---

## Lesson anatomy (reusing `assets/lesson.css`)

Every lesson file (`./lessons/0001-<dash-case-name>.html`):

```
header.lesson-head  → kicker, h1, meta (source)
[h2/h3 content]     → knowledge: only what the skill needs
[interactive]       → quiz / predict / guided widget (the skill practice)
section.recap       → one-sentence retrieval of the core idea
section.win         → the tangible thing you can now do (border-left: green)
section.next        → links to next lesson(s) + reference doc(s)
section.teacher     → "Ask me anything that's unclear" (border-left: ochre)
cite                → primary source link
```

---

## New components to create in `assets/`

Most lessons reuse `lesson.js` (quiz + predict) as-is. Two new reusable widgets:

- **`assets/checklist.js`** (or CSS-only `<details>` checklist) — for L07 (plan rest), L08 (time audit).
- **`assets/free-recall.js`** — textarea + "reveal checklist to self-score" for L12.

---

## Build order

Build **one lesson at a time** — respects spacing and lets each be tuned to the user's zone of proximal development.

1. `LESSON-FORMAT.md` — define the lesson skeleton contract. ✓
2. Phase 0 (Reframe): L01–03.
3. Phase 1 (Rest & Plan): L04–07 — brought forward from the user's immediate need.
4. Continue through remaining phases.

### Status

- [x] LESSON-FORMAT.md
- [x] 01 — Studying isn't learning
- [x] 02 — Your memory is a leaky bucket
- [x] 03 — Climb Bloom's from the top
- [x] 04 — Real rest vs fake rest
- [x] 05 — The recovery break
- [x] 06 — Leave work at work
- [x] 07 — Plan rest, not just work
- [x] 07b — Build a play menu (added from `play-as-recovery.html`; sits between 07 and 08)
- [x] 08 — Find your lost 10 hours
- [x] 09 — Important ≠ urgent
- [x] 10 — Procrastination is an emotion
- [x] 11 — Recognition is the imposter
- [x] 12 — The 2-minute brain dump
- [x] 13 — Match the method to the mission
- [x] 14 — Your 15-second window
- [x] 15 — Think on paper
- [x] 16 — Build the web, not the dots
- [x] 17 — Maps, not lists
- [x] 18 — Learn a skill with RAIL
