# Build Plan — "domain-map": a skill for finding unknown unknowns

Date: 2026-08-13 · Status: plan (ready to build) · Owner: repo learning system

## 1. The problem being solved

**The user's exact words:** *"I can ask about a thing I don't know its existence."*
You cannot search for what you don't know exists. This is the unknown-unknowns
problem at the *domain* level: not "which of the things I know about should I
learn next?" but *"what things exist in this territory that I have never heard
of?"* The skill must work for any topic — Programming, Sports, Life, Focus,
and anything else.

**Why this is different from every existing skill (researched 2026-08-13):**

| Existing skill | Level | What it does | Why it doesn't solve this |
|---|---|---|---|
| `dzhng/skills@explore-unknowns` (176 installs) | task | Quadrant walk (known knowns → known unknowns → unknown knowns → unknown unknowns) for **ambiguous requests** | Maps the unknowns of *one task* against a visible codebase; presumes the territory is at least partially visible |
| `ohyeh/agent-scripts@unknowns-discovery` (49) | task | Same four-info model, derived from Anthropic's "Field Guide to Fable"; blindspot pass for implementation tasks | Task-level; presumes an entered codebase |
| `pjt222/agent-almanac@learn` (22) | territory | Survey → hypothesize → probe → integrate → verify → consolidate, for **learning a territory you already entered** | Its "gaps" are "areas that look important but are opaque" — it presumes you can see the boundary |
| `delexw/claude-code-misc@domain-discover` | — | Name matches, content doesn't exist under that name (no SKILL.md found in the repo) | Dead lead |

**The core finding:** all of them are *inside-out* — they map unknowns against a
territory you can already see. The boundary itself (the map before the map) is
unhandled. This skill is the **outside-in** one: it derives the shape of the
territory from first principles, independent of what you know, so the empty
cells in that derived shape are your unknown unknowns.

## 2. The method — the systematic answer (proven in this repo)

The method already exists and works: it is exactly what `reference/COVERAGE.md`
does for the learning shelf. The general principle, restated:

> **Topical completeness cannot be verified from inside the artifact. It
> requires an external domain model** — a decomposition of the territory
> derived top-down from the purpose, independent of what the user already
> knows. Map the user's knowledge onto the model; **the empty cells are the
> unknown unknowns.**

### Why "verify what exists" failed (the repo's own failure, 2026-08-13)

Three stacked failure modes — the skill must encode the *fix* for each:

1. **Verification of what exists cannot see absence.** Every audit measured the
   shelf against itself (numbering, citations, twins) — all consistency checks.
   Planning and focus weren't *wrong* anywhere; they were *missing* everywhere.
   **Fix encoded:** the model is derived top-down from MISSION/purpose *before*
   any artifact is read. Absence detection must not depend on scanning what
   exists.
2. **"Complete" was scoped to citations, then worded as coverage.** A true claim
   ("every claim traces to its paper") metastasized into a false one ("the shelf
   is complete"). Goodhart: the measurable metric stood for the real one.
   **Fix encoded:** the operational definition of "covered" is a node that has
   all artifact types (doc + lesson + glossary + twin); the map is the single
   source of truth; the honest word for a map with empty cells is "gaps exist,"
   never "complete."
3. **The audit loop anchored on the artifact.** Every "redo it deeper" dug
   deeper into the existing docs — never questioned the boundary of the doc set.
   The user found the gap from *outside*, from felt experience ("I can't focus,
   I don't plan"). **Fix encoded:** the skill's first step is purpose-first
   decomposition; a boundary re-derivation from scratch is a required periodic
   step (patching the map can't see boundary drift).

### The domain model — nodes and "covered" definition (from COVERAGE.md)

- A node is a **"what the learner must be able to do"** statement — not a topic
  name. (COVERAGE example: "Protect and direct attention" — not "focus".)
- **COVERED** = doc + lesson + glossary (twin for core nodes).
  **THIN** = doc but no lesson (or passing mention). **GAP** = no doc owns it.
- The distinction matters: THIN = content exists, artifact missing; GAP = no one
  owns the topic. The two GAPs found (planning, focus) became two new docs.

## 3. Skill design

### Name
`domain-map` — builds the external domain model and maps what you know onto it;
the empty cells are the unknown unknowns. (Alt: `map-the-domain`,
`unknown-unknowns`, `coverage-map`. `domain-map` chosen: descriptive, short,
matches `domain-modeling` which already exists in the toolset.)

### The five-step procedure (generalized from COVERAGE.md + the research)

1. **Purpose first.** Ask (or extract): *what is the user trying to become able
   to do in this territory?* Not "what do you want to learn about X" — *"what
   must you be able to do, and in what contexts?"* The purpose is the root of
   the derivation; it must be obtainable **before** looking at the user's
   existing knowledge.
2. **Derive the model top-down.** Decompose the purpose into a small set of
   nodes (5–15), each a "must be able to do" statement. Decompose recursively
   only where a node hides real sub-skills. **Guard:** the derivation must not
   use the user's own notes/docs as the source — that reintroduces the
   inside-out failure. Sources that ARE allowed: the purpose itself, the
   domain's canonical structure (curriculum, textbook TOC, expert taxonomies),
   and web search for the domain's standard decomposition.
3. **Map what the user has.** For each node, check the user's artifacts
   (docs, notes, projects, knowledge): covered / thin / gap. **Guard:** "covered"
   means the user can actually *do* it — not that they've heard of it.
4. **The deliverable: the named gap list.** List every empty cell as a named
   unknown — each with (a) what the node is, (b) why it matters given the
   purpose, (c) a first search query / seed source to enter it. *This is the
   thing the user couldn't ask for.* Rank by leverage on the purpose.
5. **Verify against the territory.** Each named gap must be confirmed against
   at least one external authority (web search, curriculum, textbook, expert).
   A gap that no authority confirms is either misnamed or the model is wrong —
   fix the model. (Same discipline as the twin batteries: claims cite real
   sources; invented nodes destroy the map's authority.)

### The periodic re-derivation rule
A map is a snapshot. The standing rule (from COVERAGE.md's own closing caveat):
**re-derive the model from scratch periodically, never patch it.** Patching can
only see drift inside the known nodes; re-derivation from the purpose can see
boundary drift (new sub-domains, merged nodes, obsolete nodes).

### Deliverable format
A `DOMAIN-MAP.md` (or `COVERAGE.md` per convention) at the root of the
territory's artifact store, containing: the purpose, the node table (node |
must-be-able-to | covered/thin/gap | evidence), the named gap list, and the
re-derivation date. For a chat-only session, the same content as the reply.

## 4. Skill structure (per write-a-skill format)

```
domain-map/
├── SKILL.md           # main instructions — quick start, 5-step workflow, guards (< 100 lines)
├── REFERENCE.md       # deep method: deriving the model (purpose→nodes→sub-nodes),
│                      #   the covered/thin/gap definitions, verification protocol,
│                      #   the three failure modes and their fixes, re-derivation rule
├── EXAMPLES.md        # 3 worked examples: (a) the learning shelf (this repo's own,
│                      #   showing GAPs planning+focus found and filled), (b) a
│                      #   programming topic, (c) a non-technical topic (sports/life)
└── scripts/           # optional: a map-template generator + a gap-list checker
```

- **Description (for the system prompt):** "Build an external domain model of a
  territory — derived top-down from purpose, not from what you already know —
  and map what you know onto it; the empty cells are the unknown unknowns you
  couldn't ask about. Use when the user wants to explore a topic, find gaps in
  their knowledge or materials, discover what exists in a domain, build a
  knowledge map/tree, or says things like 'I don't know what I don't know' /
  'what am I missing in X?'"

## 5. Open decisions (need user input before building)

1. **Name** — `domain-map` (proposed) vs alternatives.
2. **Artifact persistence** — always write a `DOMAIN-MAP.md` file, or chat-only
   when no artifact store exists?
3. **Scripts** — a template generator + gap-list checker are cheap and
   deterministic; include them or keep it instructions-only?
4. **Install location** — user-level (`~/.agents/skills/domain-map`, usable in
   every repo) or project-level (`.agents/skills/`, committed with this repo
   where COVERAGE.md is the living example)?
5. **Worked examples** — the repo's COVERAGE.md as example (a), plus which two
   general topics for (b) and (c)?

## 6. Build checklist

- [ ] SKILL.md — description with triggers, quick start, 5-step workflow, guards
- [ ] REFERENCE.md — full method, three failure modes + fixes, re-derivation rule
- [ ] EXAMPLES.md — 3 worked examples
- [ ] scripts/ (if approved) — template generator + gap checker
- [ ] Install to the chosen location
- [ ] Test against a real session: run it on a fresh topic (e.g. "Focus" or a
      programming topic), verify the gap list names things the user confirms
      they didn't know existed
- [ ] Review with user (write-a-skill step 3)
