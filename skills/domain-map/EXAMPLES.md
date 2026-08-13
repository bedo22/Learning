# Domain Map — Worked Examples

Four examples: (a) the method's own birthplace — this repo's COVERAGE.md —
showing a real GAP found and filled; (b) a technical territory (programming);
(c) a soft territory (focus); (d) a mixed technical + business territory
(freelance front-end development — a full end-to-end run). The structure is
identical in all four.

---

## Example A — the origin: the "Learn to Learn" shelf (real, from this repo)

**Purpose:** master the general skill of learning how to learn, applied across
exams, coding, career, and lifelong learning. *What must the learner be able
to do?*

**Model derived top-down** (12 nodes, each a "must be able to do"):

| Node | Must be able to | Status |
|---|---|---|
| Encode & understand | Turn input into meaning (maps, levels, notes) | covered |
| Store & consolidate | Make it stick (memory, spacing, sleep) | covered |
| Retrieve & apply | Pull it out on demand (testing, transfer) | covered |
| Regulate | Know what you don't know; manage urges | covered |
| Execute — plan | Turn intention into scheduled action | **GAP → new doc** |
| Execute — focus | Protect and direct attention | **GAP → new doc** |
| Execute — systems | Run the weekly machinery (cues, scripts) | covered |
| Sustain | Recover energy; rest; play | covered |
| Set direction | Know the why & who (goals, meta-goals) | covered |
| Guard against myths | Spot false learning beliefs | covered |
| Use tools (AI) | Use AI without fluency theft | covered |
| Meta | Navigate the system (glossary, index) | covered |

**The result:** every earlier audit — all inside-out consistency checks — had
declared the shelf effectively complete. The purpose-first derivation exposed
**two GAPs in seconds**: *plan* and *focus*. The user felt them ("I can't
focus, I don't plan") but could not name them — they were unknown unknowns.
Each became a full reference doc + lesson + Arabic twin.

**Key move to copy:** the model came from *purpose* ("what must a learner be
able to do?"), not from scanning the existing docs. Scanning could only see
what existed; the purpose could see what didn't.

---

## Example B — a technical territory: "become employable as a backend developer"

**Purpose:** build and ship real backend services that employers trust enough
to hire for — not "learn backend stuff."

**Model derived top-down** (10 nodes, ability-phrased):

| Node | Must be able to | Status (example) |
|---|---|---|
| Model data | Design schemas and relationships for real requirements | covered |
| Build APIs | Design, implement, and version HTTP APIs | covered |
| Persist state | Use databases correctly (queries, indexes, transactions) | covered |
| Secure the system | AuthN/AuthZ, input validation, secrets, OWASP top-10 | thin |
| Deploy & operate | Ship, monitor, debug in production | **GAP** |
| Test reliably | Write tests that catch regressions, not just pass | covered |
| Handle scale | Caching, queues, load, observability | **GAP** |
| Integrate | Third-party services, auth providers, payments | thin |
| Read others' code | Navigate and extend an unfamiliar codebase | thin |
| Communicate | Explain designs, review PRs, write docs | **GAP** |

**The named gap list (the deliverable the user couldn't ask for):**

1. **Deploy & operate** — the user can build but never ships; every skill
   before it is unproven without it. *Seed:* "deployment pipeline tutorial
   (CI/CD + container + host)".
2. **Handle scale** — caching and queues are invisible until traffic grows;
   employers ask about them in every senior interview. *Seed:* "caching
   strategies and message queues — when to use each".
3. **Communicate** — hiring is a communication act; the user has no evidence
   of design-explain ability. *Seed:* "how to write a design doc / explain a
   system architecture".

**What's notable:** the user's own project list was full of APIs and schemas —
they felt *good* about this territory. The purpose-derived model still found
three gaps they'd never have listed, because the gaps live in the *unbuilt*
parts of the purpose (shipping, growing, being hired), not in the topic's
inventory.

---

## Example C — a soft territory: "focus" (the user's own domain)

**Purpose:** sit down, do the planned deep work for its full window, and walk
away with the output — repeatedly, across a career.

**Model derived top-down** (8 nodes):

| Node | Must be able to | Status (example) |
|---|---|---|
| Protect attention | Remove/disable what attacks focus (phone, noise, feeds) | covered |
| Resist internal pull | Handle mind-wandering and the urge to switch | covered |
| Recover focus | Rest and restore depleted attention | covered |
| Match effort to state | Schedule hard tasks at cognitive peaks | thin |
| Bounce back from breaks | Return cleanly without attention residue | thin |
| Train attention capacity | Get better at returning to task over months | **GAP** |
| Diagnose the failure | Tell boredom from fatigue from overwhelm — fix accordingly | covered |
| Sustain the system | Keep the environment and schedule working for years | **GAP** |

**The named gap list:**

1. **Train attention capacity** — the user fixes the environment but has no
   *practice* for the return-to-focus muscle; environment alone caps out.
   *Seed:* "attention training research — what actually transfers".
2. **Sustain the system** — one-off setups decay; no review loop keeps the
   environment honest. *Seed:* "weekly review routine / habit maintenance".

**What's notable:** the user had strong coverage of the *defensive* nodes
(protect, resist, recover) but zero on the *developmental* ones (train,
sustain). A topic-name audit of "focus" would have produced a list of
distraction-fighting tips — the ability-phrased model found the missing
*long-horizon* abilities instead.

---

---

## Example D — a mixed territory: "become employable as a freelance front-end developer"

**Purpose:** build and ship production-quality front-end work for paying
clients — get hired, deliver, get paid, sustainably. (Not "learn front-end".)

**Model derived top-down** (12 nodes, ability-phrased): the technical chain
(mark up & style → make it interactive → use the toolchain → ensure quality →
ship & deliver) and the business chain (read a brief → estimate & price →
contract & protect → manage the project → get clients → invoice & get paid),
plus keep-skills-current. Taxes, accounting, design aesthetics, and networking
were quarantined as adjacent-but-not-modeled.

| Node (ability) | Status |
|---|---|
| Mark up & style: build semantic, responsive, accessible HTML/CSS | thin |
| Make it interactive: maintainable JS — DOM, state, async | thin |
| Use the toolchain: framework (React), Git, build tools | **GAP** |
| Ensure quality: tests, a11y, performance, cross-browser | **GAP** |
| Ship & deliver: deploy, QA, hand off | **GAP** |
| Read a brief: requirements → scope | **GAP** |
| Estimate & price: quote time/money covering cost and risk | **GAP** |
| Contract & protect: scope, revisions, payment terms | **GAP** |
| Manage the project: milestones, revisions, comms cadence | **GAP** |
| Get clients: portfolio, proposals, acquisition | **GAP** |
| Invoice & get paid: invoicing, chasing, cash flow | **GAP** |
| Keep skills current: learn new tooling without burning out | thin |

**The named gap list (ranked by leverage):**

1. **Read a brief** — everything downstream (estimate, contract, delivery)
   depends on scoping correctly. *Seed:* "how to scope client projects,
   requirements gathering".
2. **Estimate & price** — underpricing is the top freelancer failure; wrong
   estimates destroy trust and margins. *Seed:* "freelance web development
   pricing: hourly vs project".
3. **Contract & protect** — unprotected scope creep turns profit into loss.
   *Seed:* "freelance web developer contract, scope of work, revision
   clauses".
4. **Get clients** — no pipeline, no income; every other skill is moot
   without it. *Seed:* "freelance web developer client acquisition".
5. **Use the toolchain** — most paid work assumes a framework + Git; without
   it rates and employability cap. *Seed:* "React portfolio projects, build
   tools, git workflow".
6. **Manage the project** — delivery chaos erodes the trust repeat work
   depends on. *Seed:* "freelance client communication, milestones".
7. **Ensure quality** — the bar that separates professional from hobby work.
   *Seed:* "web accessibility, performance, testing audit checklist".
8. **Ship & deliver** — a built site never deployed or handed off has no
   value. *Seed:* "freelance web developer deployment, handoff checklist".
9. **Invoice & get paid** — cash-flow failure ends the business even with
   great work. *Seed:* "freelance invoicing, payment terms, chasing late
   payments".

**What's notable:** the technical inventory was largely *present* (marked thin
from the user's challenge work) while the entire business chain was empty. A
topic-name audit of "front-end development" would have produced another list
of CSS tricks and framework tips — the ability-phrased model found that the
purpose's real bottleneck is the business chain, not more markup. Eight of the
nine gaps were business-side, and none of them could have been asked about
("what am I missing in freelancing?" returns advice, not this list). All nine
gaps were verified against the territory via freelancer skill taxonomies
(2026) before the map was handed over.

## The pattern across all four

1. **Purpose as a verb** ("be able to do X in contexts Y") — not a noun.
2. **Nodes as abilities** — testable, demonstrable, traceable to the purpose.
3. **The gaps are the unbuilt parts of the purpose**, not the unloved parts
   of the topic. That's why the user can't name them: they're invisible in
   the topic's inventory and visible only in the purpose's requirements.
