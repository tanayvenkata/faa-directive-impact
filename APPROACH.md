# Approach: The Manual Workflow, the Proposed One, and What We Compare

This note explains what the project builds and why, in plain terms. It also
lists the baselines each stage is measured against. The build order is in
[`ROADMAP.md`](ROADMAP.md); the pass/fail gates are in
[`evaluation/GATES.md`](evaluation/GATES.md).

## The Problem

The FAA publishes airworthiness directives (ADs): legally binding rules saying
which engines or aircraft must be inspected, repaired, or have parts removed,
and by when.

Measured from the Federal Register API on 2026-10-06 (documents from the FAA
whose title begins "Airworthiness Directives"):

| Year | Final ADs | Proposed ADs |
|---|---:|---:|
| 2022 | 424 | 338 |
| 2023 | 348 | 274 |
| 2024 | 280 | 243 |
| 2025 | 317 | 248 |

That is roughly 300–400 final ADs a year, more than one each business day.
Emergency ADs sent directly to operators may not appear in these counts.

Not every AD is checked against every asset. Screening happens in two stages:

1. **Filter by product type (cheap).** Each AD names the aircraft models,
   engine models, propellers, or parts it covers. An operator of A320s with
   V2500 engines drops a Boeing 787 AD immediately. Most ADs fall out here.
2. **Check against each asset's records (expensive).** An AD that names an
   operator's engine model still has to be compared with every such engine:
   which part and serial numbers are installed, their cycles, modification
   status, and shop visits. AD 2025-19-13 names 10 engine models, but only
   engines carrying 8 specific hubs need action.

The hard work, and this project's focus, is stage 2.

The stakes per AD vary widely. AD 2025-19-13, the one S1 covers, estimates
two affected U.S. engines at about $468,500 per hub replacement. Paragraph
(e) states the risk: "an uncontained hub failure, release of high-energy
debris, damage to the engine, damage to the airplane, and loss of the
airplane."

## Why It Matters

The value is not replacing an analyst's salary, which is small next to an
airline's costs. It is in what people cannot practically do today.

- **Knowing what is installed where.** Stage 2 depends on each part's
  history, like a vehicle history report for every life-limited part: which
  engine it is in, where it was before, its own cycles since new, and its
  repairs. A part's cycles are not the engine's cycles once it has moved
  between engines (GATES.md, gate 8). Most of the difficulty is in keeping
  this state correct, not in reading the AD.
- **Re-checking on every change, not only when an AD is published.** Parts
  are swapped at shop visits, engines move between aircraft, and assets
  change hands. Each change should re-run every applicable AD against the new
  configuration. People check mainly when an AD arrives. A rules engine can
  re-check the whole fleet whenever the records change.
- **Speed when it is urgent.** When an emergency AD lands, the question is
  which engines are affected and by when. Hours instead of days matters most
  then.
- **The cost of a miss.** In 2008 the FAA proposed a record $10.2 million
  penalty against Southwest Airlines for operating 46 Boeing 737s on 59,791
  flights without the fuselage inspections AD 2004-18-06 required; six of
  the airplanes were later found to have fatigue cracks. Southwest settled in
  2009 for $7.5 million and agreed to strengthen its maintenance tracking.
  Catching one such miss is worth far more than the analyst time saved.
- **A second check for the analyst.** The system shows its evidence, so an
  analyst can confirm or override each result. Every override is recorded
  and becomes a new test case, so the system improves where it was wrong.
- **Records review at transactions.** When an engine is bought, sold, or
  returned from lease, its AD history is reviewed from the records. That is
  the same screening done in bulk under time pressure.

The pitch is therefore not "automating clerical work." It is **a second check
that never tires, re-runs on every fleet change, and shows its evidence.**

These descriptions of industry practice come from our research and general
knowledge. A practitioner should confirm them once there is a working system
to show (issue #9).

## The Workflow Today (no AI)

Based on vendor documentation and FAA guidance gathered in
[`evaluation/research/`](evaluation/research/2026-10-06-gate-research.md):

```text
New AD published in the Federal Register
   │
   ▼
Engineer notices it (subscription, daily review) and drops it
if it names no product type the operator flies
   │
   ▼
Engineer reads the AD and works out its applicability:
models, part and serial tables, limits, triggers
   │
   ▼
Engineer checks each engine's records by hand or in a spreadsheet
or maintenance-tracking system
   │
   ▼
Engineer records each asset's AD status and plans the work
```

- A person decides applicability for every relevant AD and asset. Airlines
  do this in an engineering or technical-services team and record it in a
  maintenance-tracking system. Smaller operators often pay a tracking
  service to research ADs for them. The software stores and tracks the
  decision; it does not make it.
- The check happens mainly when an AD is published. A later part swap is
  caught only if someone re-checks the ADs against the new configuration.
- Newer vendor AI features draft extractions for an engineer to approve. No
  vendor publishes accuracy for applicability decisions.
- Errors happen. FAA and DOT Inspector General audits record missed and
  misapplied ADs, but no audit gives a base rate of AD-status errors.

## The Proposed Workflow

```text
New AD published                     Fleet record changes
   │                                 (part swap, shop visit, transfer)
   ▼                                          │
Daily sync fetches it, preserves exact bytes ──────────── deterministic (built)
   │
   ▼
AD shown as "new, not yet evaluated" the same day ─────── deterministic (step 6)
   │
   ▼
AI drafts the AD's rules, each value tied to ──────────── AI (step 5)
the paragraph it came from
   │
   ▼
Automatic checks: does every serial number, model, ───── deterministic (step 5)
and limit actually appear in the cited paragraph?
   │
   ▼
Person proofreads the draft against the AD ───────────── human, not expert
   │
   ├── wording is clear ──► rules go live
   │
   └── wording is ambiguous ──► flagged for an expert ─── SME, rare
                                (engines go to "needs review" meanwhile)
   │
   ▼
Rules screen every engine: three queues with ─────────── deterministic (S1, built)
cited paragraphs and named missing facts   ◄──────────────┘ re-run on every change
   │
   ▼
Analyst reviews the queues and verifies ───────────────── human
   │
   ▼
Each override is recorded and becomes a new test case ─── feedback loop
```

The idea behind this flow is that **AI proposes and deterministic checks
decide.**

- **Deciding whether an engine is affected is mechanical once the rules
  exist.** S1 shows this for one AD: plain rules match the answer key on all
  18 cases, cite their paragraphs, and route missing facts to review.
- **Writing the rules is the bottleneck.** For AD 2025-19-13, most of the
  rule content is transcription: 10 models, 8 table rows, a date, and a
  cycle window. One sentence needed interpretation. AI is suited to the
  transcription, and the automatic checks catch values it makes up.
- **Interpretation stays with experts.** The ambiguous sentence in paragraph
  (g) had two grammatical readings. The FAA engineer's answer matched neither.
  An AI that picked one would have been confidently wrong, and only the expert
  answer showed it. The system's job is to flag ambiguity, not resolve it.

| Step | Today | Proposed | Who decides |
|---|---|---|---|
| Notice a new AD | person, by subscription | daily sync | — |
| Turn the AD into rules | engineer, every AD | AI drafts, checks verify, person proofreads | person |
| Resolve ambiguous wording | engineer's judgment | flagged to an expert | expert |
| Check each engine | person, per engine | rules, all engines | rules |
| Re-check after a part moves | only if someone remembers | automatic on every record change | rules |
| Catch a miss | audit, or after the fact | analyst sees an independent second result | analyst |
| Record AD status | operator | **not done by this system** | operator |

The system never states compliance, never writes the operator's AD record, and
never authorizes maintenance.

## Baselines and Metrics

Each stage is scored against a simpler alternative on the same frozen cases.

| # | Baseline | What it measures | Status |
|---|---|---|---|
| B0 | **Manual process** | Miss rate, time to answer an urgent AD across a fleet, and whether a later part swap is caught | No credible public figure (see below). To be measured in a practitioner session. |
| B1 | **Hand-written rules** (S1) | Gates 1–13 on 18 units | **Done:** all gates pass; decision go, provisional ([`evaluation/S1_BASELINE.md`](evaluation/S1_BASELINE.md)) |
| B2 | **LLM given the AD and the engine, no rules** (full context, step 4) | The same gates on the same 18 units | Not run. The obvious "just ask the model" comparison. |
| B3 | **LLM-drafted rules, checked and proofread** (step 5) | Field accuracy against B1's rules, whether it flags ambiguity, and proofreading minutes per AD | Not run |
| B4 | **Retrieval of candidate ADs** (step 7) | Candidate recall (gate 14); precision and ranking metrics once the distractor set exists | Not run |

### External reference points

These help orient the numbers. None of them is a baseline we have reproduced.

- **LLM extraction of AD applicability** (Drop, TU Wien thesis, 2026): 93.8%
  field accuracy on 15 hand-labeled A320 ADs with a schema-guided approach.
  Affected parts was the weakest field, and the author concludes human
  verification is required. That figure is the bar B3 should be read against.
- **Manual time per AD.** Vendor marketing claims "2–4 hours per bulletin"
  for applicability matching and "32 hours" to extract one service bulletin
  ([Ramco](https://www.ramco.com/blog/aviation/agentic-ai-for-aviation-maintenance)).
  Neither cites a study. We treat them as claims, not data. B0 has to be
  measured.
- **Screening trade-off in medicine** (Plesner et al., Radiology 2023): near
  zero misses came at the cost of clearing only 28% of normal cases
  automatically. Expect the same tension between gate 1 (no false clear) and
  gate 12 (no needless escalation).

### What each comparison can claim

- B1 against the labels shows the rules reproduce one reading of the AD. The
  labels and rules share an author, so this does not show correctness.
  Practitioner review (issue #9) is the independent check.
- B2 against B1 shows whether the rules earn their place over plain prompting.
- B3 against B1 is the main AI question: can the rule-writing be automated
  without losing accuracy, and does the model flag ambiguity instead of
  guessing?
- B0 against the proposed flow is the user-value question. Analyst hours
  saved matter less than misses caught, time to answer an urgent AD, and
  re-checks that would otherwise not happen.

## Where Retrieval (RAG) Fits

Retrieval is one component here, not the core of the product.

- **In this episode:** retrieval finds which of thousands of ADs could touch
  an engine (step 7). Its key metric is recall, because a missed AD is a
  silent false clear. The impact decision itself is rules, not generated
  text.
- **Across the series** (the *Production Evidence Systems* plan, kept in the
  owner's planning notes):
  - **Regulation E** is the episode built to compare keyword search, full
    context, simple RAG, and hybrid rule-plus-retrieval head to head.
  - **FAR/DFARS** stresses retrieval completeness across cross-references and
    attachments, with a graph.
- The `rag-field-guide` plugin is a set of practitioner notes used as a
  design reference, not a project.

The series' rule is that complexity has to earn its place. Rules, search,
full context, and RAG are compared on the same cases, and the simplest one
that passes the gates wins.

## What This Means for the Build

- **Asset history is consumed, not built.** S1 screens one snapshot per
  engine. Re-checking on change needs only enough dated records per part
  (installed, removed, cycles at each event) for the synthetic demo fleet to
  show a part moving between engines. The seed already records per-part cycle
  readings. Moving parts between engines is a listed gap in GATES.md.
- **Re-screening is cheap by design.** Rules over normalized records can run
  across the whole fleet on every change. A design that called a model for
  every engine and AD on every change would cost more and could not be
  re-run identically.
- **Overrides feed the cases.** An analyst override is recorded with its
  reason and becomes a regression case, following the series' rule that
  reviewer overrides enter regression while fresh holdout cases stay
  protected.

## Note: Part History Already Exists

Back-to-birth records for life-limited parts are required (14 CFR 91.417),
travel with release certificates (FAA Form 8130-3, EASA Form 1), and are
tracked in airline maintenance systems and reviewed at every engine sale or
lease return. Tracking part history is not a gap this project fills.

What may be a gap, unconfirmed until a practitioner says so:

- the history is split across operators, repair shops, and lessors, and older
  records are often scanned paper;
- joining that history to each AD's requirements is still a person's job.

**Decision (2026-10-06): no part-history work beyond what the demo fleet
needs.** The portfolio piece is the reliable, cited, re-runnable join between
"which part is where" and "what each AD requires." Building a part-history
system would be feature creep. Revisit with a deeper dive only if:

- a practitioner names fragmented or paper records as the main obstacle, or
- the demo fleet (ROADMAP step 8) cannot show a part moving between engines
  without more history modeling than dated installation rows.

## Numbers Still to Collect

- B0: time and errors for a practitioner screening the 18 S1 engines by hand.
- B2: the full-context LLM run on the 18 units.
- B3: LLM rule extraction for a second AD (AD 2026-17-03, already in the
  seed), with proofreading time.
- Hand-coding effort for B1 per AD, recorded so B3's savings can be stated.
- For the demo fleet (step 8): how many results change after a simulated part
  swap, and how fast the fleet is re-screened.
