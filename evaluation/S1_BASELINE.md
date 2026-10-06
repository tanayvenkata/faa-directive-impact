# S1 Rules Baseline: AD 2025-19-13

- **Issue:** #16 (ROADMAP Delivery Sequence step 3)
- **Run:** [`runs/s1-20261006T223638Z-6a301b1/`](runs/s1-20261006T223638Z-6a301b1/)
  at commit `6a301b1`, gate version 1, source generation
  `gen-20260926T215105Z-7fe9da08`
- **Decision:** **go**, provisional until the project owner confirms the
  hand review (gates 5 and 11)

## What Was Built

S1 screens synthetic engines against one directive with plain rules: no
language model, no retrieval.

1. **Normalized record** (`src/faa_directive_impact/directives/`). The frozen
   Federal Register XML is checked against its receipt's SHA-256, then read
   into a JSON record. The record holds every regulatory paragraph id from (a)
   to (l), including `(i)(2)(ii)`, the eight table 1 rows, the effective
   date, the ten listed models, and the 100-flight-cycle window. It is
   derived data, and rebuilding it from the same bytes gives the same file.
2. **Rules** (`src/faa_directive_impact/impact/hpt_hub_rules.py`). For each
   engine the rules return applicability, action status, authority state,
   computed cycle values, missing facts, continuing obligations, stated
   timing, and a citation for every answer, clears included.
3. **Page** (`queues.html` in the run directory). A static page that opens
   directly in a browser, with three queues and each engine's cited
   paragraphs and missing facts. It says it is a screening aid, not a
   compliance determination.
4. **Scorer** (`src/faa_directive_impact/evaluation/s1_scoring.py`). The
   frozen gates applied to the 18 S1 units. Tests feed it deliberately wrong
   outputs to show that each gate catches its failure: a false clear, a scope
   leak, a settled answer without the fact, a dropped missing fact, a
   made-up paragraph or table row, the wrong authority state, an off-by-one
   cycle count, a match on the part number alone, an uncited clear, and a
   needless escalation.

## Results

| Gates | Result on 18 units |
|---|---|
| Protected 1–4, 6–9 (code) | all pass |
| Protected 5 (hand) | pass, first pass by Claude, **unconfirmed** |
| Aggregate 10 (citations), 12, 13 (code) | 0 failures; budgets were 0, ≤1, ≤1 |
| Aggregate 11 (hand) | pass, first pass by Claude, **unconfirmed** |
| 14 (candidate recall) | not exercised: S1 is handed its directive |
| Other directives' 15 units | not yet evaluated |

These are exact counts on a disclosed suite, not rates. With zero failures in
18 units, the true failure rate could still be as high as about 17%.

## Why a Clean Score Means Less Than It Looks

The rules port the logic of `evaluation/hpt_hub_reference.py`, which was
written alongside the labels by the same author. A test keeps the two in
agreement. A clean score therefore shows that the rules reproduce **one
reading** of AD 2025-19-13 consistently, with correct citations, arithmetic,
and wording. It does not show that the reading is right. A misreading shared
by the labels, the oracle, and the rules would pass every gate. Practitioner
review (issue #9) is the independent check.

What the run does show:

- the plumbing works end to end, from frozen bytes to a page with citations;
- every answer, including every clear, cites a paragraph that exists;
- the scorer is not vacuous, because it fails each kind of wrong output fed to it.

## Failure Taxonomy

**Observed failures: none.** No mechanical gate failed, and the first-pass
hand review found no forbidden claim and no contradicted timing.

**Where the rules are thin.** These cause no failure today, but each is where
the next failure is most likely:

| # | Category | Detail | Kind |
|---|---|---|---|
| T1 | Shared interpretation | The labels, oracle, and rules come from one reading of paragraph (g). | Limit of the evidence, not of rules |
| T2 | Informal adjudication encoded | A shop visit inside the first 100 FC follows informal FAA correspondence (`faa-informal-2026-10-05`). The FAA's view of a visit after 100 FC is pending; the rules follow the text there, where both readings agree. | Rule input that may change |
| T3 | Counter projection | Deadlines in engine-counter terms assume the hub stays in this engine and gains cycles one-for-one with it from the effective date. The labels share this assumption. | Modeling assumption |
| T4 | Hand-written extraction | The normalizer's patterns fit this AD: a four-column table and "within N flight cycles from the effective date". A new AD needs new code. | Limit of the approach: scale, not correctness |
| T5 | Wording judgment | The seed-018 timing paraphrases (g)'s shop-visit trigger, while its label calls a later visit's effect pending. Seed-006 omits a caveat that does not change its deadline. Both were recorded as consistent and are flagged for the owner. | Hand-review note |
| T6 | Known gaps | GATES.md "Known Gaps": thin slices, counting boundaries, authority reverse direction, recurring actions. A pass says nothing about them. | Not exercised |

## Decision

Under the GATES.md Verdicts section:

- **go:** every protected gate passes, every aggregate is within budget, and
  nothing is unresolved.
- **not constrain:** no aggregate gate failed on any slice.
- **not switch:** no protected gate failed.

The decision is provisional only because gates 5 and 11 were first-pass
reviewed by Claude, which also wrote the output being reviewed. It becomes
final when the project owner checks `hand-review.yaml`, sets
`reviewer_confirmed: true`, and reruns `make s1-conclude`. If the owner
records a failure, the unit is `unresolved` until its label is checked
(GATES.md, "Disputed Labels"), and this decision is revisited.

**What go means:** plain rules express everything AD 2025-19-13 needs on this
suite. They remain the baseline that later approaches are scored against on
the same 18 units. The limit that matters is T4: each new directive needs
hand-written rules. ROADMAP step 5 (model-proposed, human-verified rule
extraction) exists to remove that limit, and it must match this baseline.

## Reproducing

```bash
make s1                                  # new run under evaluation/runs/
make s1-conclude RUN=evaluation/runs/<run-id>
```

Runs are never overwritten. Every run is kept, including failed ones.
