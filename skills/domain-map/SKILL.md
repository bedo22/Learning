---
name: domain-map
description: >-
  Build an external domain model of a territory — derived top-down from
  purpose, never from what you already know — then map what the user knows
  onto it; the empty cells are the unknown unknowns they couldn't ask about.
  Use when the user wants to explore a topic, find gaps in their knowledge or
  materials, discover what exists in a domain, build a knowledge
  map/tree/roadmap, or says things like "I don't know what I don't know",
  "what am I missing in X?", or "I can't ask about a thing I don't know
  exists" — for any domain (programming, sports, life, focus, studies, work).
argument-hint: "Topic or territory to map (optional: what you want to be able to do)"
---

# Domain Map

You cannot search for what you don't know exists. The fix is an **external
domain model**: a decomposition of the territory derived top-down from the
purpose, independent of what the user already knows. Map their knowledge onto
it — **the empty cells are the unknown unknowns**, named and ranked.

## Core principle

Topical completeness cannot be verified from inside the artifact. Auditing
what exists (notes, docs, projects, memory) can only find errors *inside*
what exists — it can never see what's *absent*. Absence is only visible
against a model derived from outside: from purpose, first principles, and the
domain's canonical structure.

## Inputs

- **Required:** the territory (a topic, skill, or life area).
- **Required:** the purpose — what the user must be able to *do*, in what
  contexts. Elicit it if absent (Step 1).
- **Optional:** the user's existing materials (notes, docs, code, projects).
  Read these ONLY after the model exists.

## The five steps

**Step 1 — Purpose first** *(done: a one-line "must be able to do X in
contexts Y" the user confirmed)*. Extract what the user must be able to *do*,
not what they want to learn *about* ("pass the AWS cert and build real
backends" ≠ "cloud stuff"). If no purpose is given, run a tight intake (max 5
questions, one batch, accept "not sure"): what do you want to be able to do?
in what contexts / for whom? how will you know you've succeeded? what's out of
scope? what have you tried? Do this before reading any of their materials.

**Step 2 — Derive the model top-down** *(done: 5–15 ability-phrased nodes,
each tracing to the purpose, boundary stated)*. Each node is a "must be able
to do" statement, never a topic name ("protect and direct attention", not
"focus"). **Allowed sources:** the purpose (necessary conditions), the
domain's canonical structure (curriculum, textbook TOC, body-of-knowledge
taxonomies), web search for the standard decomposition. **Forbidden source:**
the user's own notes/docs/projects — using them reintroduces the inside-out
failure. **Boundary discipline:** name what is out of scope vs merely
adjacent; quarantine adjacent nodes in an "Adjacent (not modeled)" note so
the 5–15 stay honest and don't sprawl.

**Step 3 — Map what the user has** *(done: every node has a status with
evidence)*. Read their artifacts *for* the nodes, after the model exists.
Mark each node:

| Status | Meaning | Test |
|---|---|---|
| **covered** | Can actually do it | "Show me / do it now" — passes cold |
| **thin** | Heard of it; passing mention | Can name it, can't demonstrate it |
| **gap** | Nothing there | Can't name it, can't do it |

"Covered" means *can do*, not *knows of*; cold demonstration beats
self-report ("I know about it" = thin).

**Step 4 — The named gap list (the deliverable)** *(done: every gap named with
what / why / seed, ranked by leverage)*. Each gap: (a) what the node is, (b)
why it matters given the purpose, (c) a first seed — search query,
book/chapter, course, or person. **This is the list the user couldn't ask
for.** Rank by leverage: the #1 gap is upstream of the rest (bottleneck test).

**Step 5 — Verify against the territory** *(done: every gap confirmed by ≥1
external authority, evidence labeled; check-map.py exits 0)*. Search the node
+ canonical terms ("X fundamentals", "X body of knowledge", "X curriculum");
prefer the domain's canonical sources. Hypothesize-then-probe nodes that
might hide sub-unknowns ("I believe X because Y" → test it). **Misnamed vs
wrong:** no authority matches → rename (synonyms) or re-derive that branch.
**Label evidence quality:** canonical / corroborated / single-source (flag
candidates). Never present an unverified gap as fact.

## The deliverable

Write `DOMAIN-MAP.md` (skeleton: `scripts/map-template.py`) at the
territory's artifact store root, or the cwd. Contents: **Purpose** (one line)
· **Node table** (node | must-be-able-to | status | evidence) · **Adjacent
(not modeled)** · **Named gap list** (ranked, each with seed) · **Re-
derivation date** (the map expires). Validate with `scripts/check-map.py
DOMAIN-MAP.md` before handing over.

## After the map

Offer the natural next skills (all installed): `learn` (build a real mental
model of a gap), `teach` (turn a gap into a learning path), `research`
(delegate source-gathering).

## Guards (each encodes a real failure mode)

- **Derive before you look.** Reading the user's materials first reproduces
  their blind spots. Purpose → model → map.
- **Nodes are abilities, not topics.** If a node can't be phrased as an
  ability, it's not a node.
- **Covered = can do.** Heard of ≠ covered. Passing mention = thin.
- **Verify every gap.** Unverified gaps destroy the map's authority; cite
  real sources, label invented data as such.
- **Name the boundary.** Adjacent sprawl hides the real 5–15. Quarantine it.
- **Re-derive, don't patch.** The map expires; re-derive from purpose from
  scratch — patching can't see boundary drift.

## Workflows

- **Full explore (unknown territory):** all five steps in order.
- **Gap check (known territory, new purpose):** re-derive from the new
  purpose, remap, diff the gap lists — the delta is the answer.
- **Boundary re-derivation (map >1 month old):** re-run steps 1–2 from
  scratch (do NOT open the old map first), then diff — changed nodes are
  boundary drift.

## Don't use when

- Territory already mapped; user needs task-level clarity →
  `explore-unknowns`.
- User has a named gap to enter → skip the map; use `learn` directly.

See [REFERENCE.md](REFERENCE.md) for the deep method and worked examples in
[EXAMPLES.md](EXAMPLES.md).
