# Domain Map — Reference

The deep method behind the five steps. Read this when a step needs more
machinery than the quick start provides.

## The failure modes this skill encodes

The method is a direct generalization of the `COVERAGE.md` approach built in
the "Learn to Learn" shelf (see EXAMPLES.md), which failed three ways before
it worked. Every guard in SKILL.md maps to one of these:

### Failure 1 — verification of what exists cannot see absence
Every early audit measured the shelf against itself: numbering consistent?
cross-references correct? citations traceable? All consistency checks passed,
and the shelf was still missing two whole topics (planning, focus). They
weren't *wrong* anywhere — they were *missing* everywhere, and no amount of
internal checking can see "missing."

**The fix:** the model is derived top-down from purpose *before* any artifact
is read. Absence detection must not depend on scanning what exists.

### Failure 2 — the measurable metric stood for the real one (Goodhart)
"Every claim traces to its originating paper" was true — and it metastasized
into "the shelf is complete." The measurable thing (citation traceability)
silently replaced the real thing (topical coverage).

**The fix:** "covered" is operationally defined per node (can the learner do
this? does an artifact teach it?) and the map is the single source of truth.
The honest word for a map with empty cells is "gaps exist" — never "complete."

### Failure 3 — the audit loop anchored on the artifact
Every "redo it deeper" dug deeper into the existing docs. The boundary of the
doc set was never questioned. The gap was eventually found from *outside* —
from felt experience ("I can't focus, I don't plan"), not from any audit.

**The fix:** the first step is always purpose-first decomposition, and a
from-scratch re-derivation is a required periodic step. Patching the map can
only see drift inside known nodes; re-derivation sees boundary drift.

## Step 2 in depth — deriving the model

The derivation is the heart of the skill. It must be **top-down and
purpose-anchored**. The discipline:

1. **Start from the purpose as a verb phrase.** "Become able to X in contexts
   Y and Z." This is the root. Every node must trace back to it.
2. **Ask: what must be true for this purpose to be achievable?** Each answer
   is a candidate node, phrased as an ability: "must be able to A, B, C…".
   These are the *necessary conditions* of the purpose, not an inventory of
   the topic.
3. **Collapse to 5–15 nodes.** If you have 40, you're listing topics, not
   deriving conditions. Merge.
4. **Test each node:** (a) is it an ability, not a topic? (b) does the purpose
   genuinely fail without it? (c) can a learner demonstrate it? If a node
   fails any test, rephrase or drop it.
5. **Decompose only real sub-skills.** A node hides sub-skills when a learner
   can be good at the node's name without being able to do its parts. (The
   shelf's "Execute" node decomposed into plan / focus / systems — each a
   distinct ability with distinct science.)

**Allowed sources for the derivation** (in order of trust):
- The purpose itself, decomposed as necessary conditions
- The domain's canonical structure: curriculum, syllabus, textbook table of
  contents, professional body-of-knowledge taxonomies, standards documents
- Web search for "X body of knowledge" / "X curriculum" / "what are the
  fundamentals of X" — to confirm the standard decomposition

**Forbidden source:** the user's own notes, docs, or current projects. Using
them to derive the model reproduces the user's blind spots. They enter at
step 3, as data to be mapped.

**Boundary discipline:** explicitly name what is *out of scope* and what is
merely *adjacent* to the purpose. Quarantine adjacent-but-out nodes in a short
"Adjacent (not modeled)" note so the model stays at 5-15 honest nodes -- sprawl
is how a clean model quietly becomes an inventory of the topic.

## Step 3 in depth — mapping

Map after the model exists. For each node, determine status:

| Status | Definition | Test |
|---|---|---|
| **covered** | The user can actually do it | "Show me / do it now" — passes cold |
| **thin** | Heard of it; passing mention; once did it | Can name it, can't demonstrate it |
| **gap** | Nothing there | Can't name it, can't do it |

Gathering evidence:
- Read the user's artifacts (notes, docs, code, projects) — but only *after*
  the model exists, and read *for* the nodes, not *for* the content.
- Ask the user directly per node: "can you actually do X right now?" — cold
  demonstration beats self-report ("I know about it" = thin).
- Do not accept "I've heard of it" as covered.

## Step 4 in depth — the gap list

Each gap becomes a named item with three parts:

1. **What the node is** — one sentence, ability-phrased, in plain language
   the user can repeat back.
2. **Why it matters given the purpose** — the leverage argument. If you can't
   make this argument, the node may be decorative — re-check it against the
   purpose.
3. **A first seed** — a search query, a canonical book/chapter, a course, or
   a person to ask. The user must be able to act on it in the next five
   minutes.

Rank the list by leverage: which gap, if closed, unlocks the most of the
purpose? The #1 gap is the one whose absence makes the whole purpose
unachievable (the "bottleneck" test: is this gap upstream of the others?).

## Step 5 in depth — verification

Every gap must be confirmed against the territory before it's presented as
fact:

- **Web search** the node's name + canonical terms ("X fundamentals", "X body
  of knowledge", "X curriculum").
- **Check the authority matches the claim:** a node that says "must be able to
  do Y" should appear in the standard structure of the domain, not just in one
  blog post.
- **Misnamed vs wrong:** if the search returns nothing that matches, either
  the node is misnamed (search for synonyms) or the model is wrong (re-derive
  the branch).
- **Label evidence quality:** canonical (in the curriculum/standards),
  corroborated (multiple independent sources), or single-source (treat as
  candidate, flag it).

Correlational or contested evidence gets a caveat, the same discipline as the
shelf's citation rules.

## Re-derivation rule

A map is a snapshot with an expiry. On re-derivation:

1. Re-run steps 1–2 from scratch (purpose → fresh model). Do NOT open the old
   map first.
2. Diff the fresh model against the old one. Changed nodes are boundary
   drift — the most valuable unknown unknowns.
3. Re-map the user's (possibly grown) artifacts against the fresh model.
4. Diff the gap lists. New gaps are either (a) real growth in the territory,
   (b) the user's new knowledge, or (c) your own earlier errors — distinguish
   honestly.

## Verification checklist

- [ ] Purpose obtained before any artifact was read
- [ ] Model derived top-down (ability-phrased nodes, 5–15)
- [ ] Every node traces to the purpose (no decorative nodes)
- [ ] Mapping used cold demonstration, not self-report
- [ ] Every gap verified against ≥1 external authority, evidence labeled
- [ ] Gap list ranked by leverage, each with a seed
- [ ] DOMAIN-MAP.md written with purpose, table, gap list, re-derivation date
