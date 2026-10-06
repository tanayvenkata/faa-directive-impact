# Evaluation Gates

- **Version:** 1
- **Status:** frozen on 2026-10-06, before any S1 run (issue #13). The
  frozen text is the commit that sets this line; the git log records it.
- **Applies to:** the feasibility seed in `seed/cases/` (seed-001 to
  seed-029).

These gates say what counts as good enough before any system output exists.
After the first scored run they do not change. A change means a new version
with a stated reason, and every result names the gate version it was scored
under.

## Scoring Unit

The unit is one **expected outcome**: one `expected` entry in one case. The
seed has 33 units across 29 cases, because seed-020, seed-022, and seed-023
expect outcomes for more than one directive.

A unit is judged on its atomic fields `applicability` and `action_status`, not
on the derived review queue. The queue merges `action_required` and
`action_required_on_event`, and the cases keep them apart.

A system that does not yet cover a directive scores that directive's units
`not_yet_evaluated`. They do not count as failures or passes. S1 covers only
AD 2025-19-13 (`2025-18469`), which is **18 units**: seed-001 to seed-010,
seed-018, seed-019, seed-024, seed-026 to seed-029, and the `2025-18469`
outcome of seed-023.

## What the Sample Can Show

Eighteen units cannot support a statistical claim. With zero failures in 18
independent units, the rough 95% upper bound on the true failure rate is 3/18,
about 17%. Gate 1 covers ten S1 units, which gives about 30%. Results are
reported as exact counts on this disclosed suite, never as rates or
significance. The protected gates are tripwires, not statistical
demonstrations, and reports say so.

The seed is also the only labeled set, and the same person wrote the labels,
these gates, and the reference derivation. A pass shows that the rules
reproduce the labels, not that they generalize. Recall measured against labels
that are not independent of the system is not meaningful on its own (Cormack &
Grossman, SIGIR 2024), which is why practitioner review (issue #9) matters
more than any threshold here. Later comparisons run on the same frozen units,
and each run is reported with the full history of earlier runs.

## Protected Gates

Any single failure blocks. These are the errors the product cannot make.

| # | Gate | Fails when | Reads |
|---|---|---|---|
| 1 | No false clear | Expected `applies` with `action_required` or `action_required_on_event`, and the system says `does_not_apply`, `no_action_triggered`, or `outside_supported_scope` | `applicability`, `action_status` |
| 2 | No scope leak | Expected `outside_supported_scope`, and the system outputs anything else. The only passing output is `outside_supported_scope` with no action status; `unknown` or `needs_review` also fails | `applicability`, `action_status` |
| 3 | No false confidence | Expected `needs_review` or applicability `unknown`, and the system gives a settled answer either way | `applicability`, `action_status` |
| 4 | Every missing fact named | Any item in `required_missing_facts` is absent from the output. This includes cases where the established action and the missing fact must both appear (seed-008, seed-017, seed-027) | `required_missing_facts` |
| 5 | No forbidden claim | The output states, or its fields imply, any entry in the case's `forbidden_claims` or in the standing list below | `forbidden_claims` |
| 6 | No fabricated citation | A cited document, paragraph, or locator does not exist in the case's source generation | cited evidence |
| 7 | Authority respected | The system treats a directive as in force when it is not (`proposed`, `published_not_yet_effective`, or replaced), or as not in force when it is | `authority_state` |
| 8 | Exact arithmetic | Any `computed` value differs from the expected value. Cycle counts have zero tolerance | `computed` |
| 9 | Exact part identity | The system matches a part to a listed row on anything but the exact P/N and S/N pair; or settles either way a listed S/N recorded in its own position under a different or differently written P/N (seed-029); or flags a part whose S/N only resembles a listed one (seed-002) | `installed_components` |

**What gate 1 also catches.** Under 14 CFR 39.15 and AC 39-7D paragraph 9c,
an AD applies to a product even after it has been repaired, modified, or
altered in the affected area. The following never clear an engine on their
own:

- a repair or modification (seed-026);
- the operator's recorded AD status (seed-028);
- a claimed AMOC without verified FAA approval (seed-027, 14 CFR 39.19);
- earlier work claimed as "already done" when it is not the required action.

Each of these is a fact for a person to verify. It is never a reason to clear.

**What gate 8 also requires.** Counting follows the FAA's conventions from
the AD Manual (FAA-IR-M-8040.1C, chapter 8):

- "within X" includes X;
- "before exceeding X" and "before accumulating X" exclude it;
- "calendar months" run to the end of the month;
- "whichever occurs later" and "whichever occurs first" are not swapped;
- a part's own cycles since new are never replaced by engine cycles. The
  two differ once a part has moved between engines.

**Gate 5 is checked by hand.** Forbidden claims are prose, and the output is
structured. For each unit, the reviewer reads the output against every
forbidden claim and records `absent` or `present` with a one-line reason in
the run report. A field value that entails a claim counts as stating it. For
example, `does_not_apply` states "AD 2025-19-13 does not apply to this engine."
Gate 5 also covers false alarms on near-miss parts: seed-002 forbids flagging
P/N 2A5001 on its part number alone.

**Standing forbidden claims, for every unit.** The output never says or
implies any of these:

- that an engine or part is compliant or noncompliant;
- that it is safe or airworthy;
- that it is approved for return to service.

It is also never worded as the operator's AD status record. FAA guidance
keeps that record, and the record of accomplishment, with the operator and
the certificated person (14 CFR 91.417, 43.9; AC 39-9). Being within an AD's
limit is not safety: NTSB recommendation A-06-60 covers an HPT disk that
ruptured while still inside its AD window.

**Gate 6 is checked mechanically** against the section index of the source
generation. Hand review covers any locator the index cannot resolve, such as a
table row.

Cases with `expert_required` provenance that are not yet adjudicated (seed-014)
score safe behavior only: `needs_review`, with the competing readings named.

## Aggregate Gates

Exact counts with a budget. Exceeding a budget fails the gate, but it does not
block on its own (see Verdicts).

| # | Gate | Counts | Budget (S1) |
|---|---|---|---|
| 10 | Required evidence cited | `required_evidence` entries whose document and paragraph are not cited for the unit. Extra valid citations are allowed. Every `does_not_apply` or `no_action_triggered` answer must also cite the paragraph that clears it, not merely report that nothing matched (EASA AMC M.A.305(c)) | 0 on `critical` units, and 0 uncited clears; at most 1 on `high` units |
| 11 | Timing stated correctly | Units whose stated timing, compared by hand, contradicts `action_timing` (wrong trigger, limit, or date) | 0 |
| 12 | No needless escalation | Determinate units sent to `needs_review`. A determinate unit has no `required_missing_facts`, an expected answer other than `needs_review` or `unknown`, and is not unadjudicated `expert_required`. Escalating where the AD itself says what to do about an unknown fact also counts | at most 1 of 13 *(declared policy)* |
| 13 | No false alarm | Units expected `does_not_apply` or `no_action_triggered` where the system says `action_required` or `action_required_on_event` | at most 1 *(declared policy)* |

**Why gate 12 exists.** It stops a trivial system from passing: one that sends
every engine to `needs_review` passes gates 1–4 and fails here. Escalation is
not free either. After the 2008 AD audits, literal readings grounded aircraft
over trivial deviations (FAA AD Compliance Review Team, 2009).

**Why gate 13 is aggregate.** A false alarm costs review time, not safety. A
false alarm that a case explicitly forbids is caught by gate 5 instead.

**Where the two budgets come from.** The budgets of 1 are declared policy, not
measurements. No published source gives an accepted error rate for this kind
of screen, and no vendor publishes accuracy for its applicability decisions.
Setting thresholds in advance as policy follows the IDx-DR pivotal trial,
whose endpoints were fixed before enrollment. The opposite risk is also on
record: at about 99% sensitivity, an autonomous chest X-ray screen could clear
only a minority of normal studies itself (Plesner et al., Radiology 2023; figures from a secondary report, see the research record). If the
budget conflicts with zero false clears, that shows up in gate 12, and only
version 2 may move it.

## Retrieval Gate (Defined, Not Exercised by S1)

| # | Gate | Estimand |
|---|---|---|
| 14 | Candidate recall | For each case, the share of its `directive_candidates` that the system surfaces for the engine. Protected: a missed candidate whose expected outcome is `action_required*` or `needs_review` is a false clear by omission |

S1 receives its directive directly and does no retrieval, so gate 14 is
reported `not_exercised`. Measuring precision needs the frozen distractor set
from ROADMAP step 6, which does not exist yet. That gate will come in a later
version, not as an improvised one.

## Coverage

The test `tests/evaluation/test_gates.py` derives these lists from the case
files. It fails if they drift.

| Gate | All units | S1 units |
|---|---|---|
| 1 | Covers: seed-001, seed-005, seed-006, seed-007, seed-008, seed-011, seed-013, seed-016, seed-017, seed-019, seed-023/2025-18469, seed-023/2026-16954, seed-026, seed-027, seed-028 | 10 |
| 2 | Covers: seed-004, seed-010, seed-025 | 2 |
| 3 | Covers: seed-003, seed-009, seed-014, seed-020/2021-11960, seed-020/2022-02574, seed-021, seed-022/2021-14268, seed-022/2021-11960, seed-029 | 3 |
| 4 | Covers: seed-003, seed-008, seed-009, seed-017, seed-020/2021-11960, seed-021, seed-022/2021-14268, seed-022/2021-11960, seed-027, seed-029 | 5 |
| 7 | Covers: seed-015, seed-018, seed-020/2022-02574 | 1 |
| 8 | Covers: seed-001, seed-005, seed-006, seed-007, seed-008, seed-019, seed-023/2025-18469, seed-026, seed-027, seed-028 | 10 |
| 9 | Covers: seed-002, seed-012, seed-024, seed-029 | 3 |
| 12 | Covers: seed-001, seed-002, seed-004, seed-005, seed-006, seed-007, seed-010, seed-011, seed-012, seed-013, seed-015, seed-016, seed-018, seed-019, seed-023/2025-18469, seed-023/2026-16954, seed-023/2025-17066, seed-024, seed-025, seed-026, seed-028 | 13 |
| 13 | Covers: seed-002, seed-012, seed-015, seed-018, seed-023/2025-17066, seed-024 | 3 |

Gates 5, 6, 10, and 11 apply to every unit. Gate 14 applies to every case.

### By Seed Slice

Issue #13 asks that each gate map to the E1 slices.

| Slice | Cases | Protected gates | Aggregate gates |
|---|---|---|---|
| `exact_match` | 001, 007, 011, 016 | 1, 8 | 12 |
| `unaffected_part` | 002, 012, 024 | 9 | 12, 13 |
| `part_identity` | 029 | 3, 4, 9 | — |
| `missing_state` | 003, 008, 009, 017 | 1, 3, 4, 8 | — |
| `out_of_family` | 004, 010, 025 | 2 | 12 |
| `shop_visit_trigger` | 005, 013 | 1, 8 | 12 |
| `cycle_limit` | 006, 019 | 1, 8 | 12 |
| `changed_product` | 026 | 1, 8 | 12 |
| `operator_assertion` | 027, 028 | 1, 4, 8 | 12 |
| `superseded_or_corrected` | 014 | 3 | — |
| `effective_date` | 015, 018, 020 | 3, 4, 7 | 12, 13 |
| `missing_incorporated_material` | 021, 022 | 3, 4 | — |
| `multiple_directives` | 023 | 1, 8 | 12, 13 |

Gates 5, 6, 10, and 11 also apply to every slice.

### Known Gaps

These risks have a gate but no case that exercises them. A pass says nothing
about them, and the report must list them.

- **Thin slices.** Gate 7 has one S1 unit (seed-018). The `changed_product`
  and `part_identity` slices have one case each, and
  `superseded_or_corrected` has one, outside S1.
- **Several ADs on one engine.** No case tests multi-directive behavior
  itself. Seed-023 is scored as three independent units, and the gate that
  would check it (14) is `not_exercised`.
- **Authority, reverse direction.** No case has a final rule with a request
  for comments, which is in force from its effective date. No case has an
  emergency AD binding on actual notice. No case has a replaced AD queried
  after its replacement took effect.
- **Counting boundaries.** No case sits exactly on an inclusive/exclusive
  limit, a calendar-month deadline, or a part that moved between engines
  with a different cycle count.
- **The AD settles an unknown itself.** For example, CFM56 AD 2018-09-10 says
  what to do when a blade's cycles are unknown. No V2500 AD in the frozen
  generation has such a clause.
- **Recurring and terminating actions.** The outcome vocabulary has no
  next-due slot, and no case needs one yet.
- **Proposal-era work.** For AD 2025-19-13 the proposal's required actions
  and table match the final rule, so work done against the proposal cannot
  diverge.

## Disputed Labels

Most cases are still `draft`. If a unit fails, the label is
not edited to match the output. The owner checks it against the cited source
text, and the check is recorded in `seed/critique/` with a verdict.

- Until that check is recorded, the unit scores `unresolved`, never `pass`.
- If the label was wrong, the case is corrected in its own commit, and every
  earlier run is re-scored and reported under both labels.
- The gate text does not change.

## Verdicts

Each gate gets `pass`, `fail`, `unresolved`, or `not_exercised`. They roll up
into the go / constrain / switch decision required by S1:

- **go** — every protected gate passes, every aggregate is within budget, and
  nothing is `unresolved`.
- **constrain** — every protected gate passes, but an aggregate gate fails on
  an identifiable slice. The claim is narrowed: that slice is routed to
  `needs_review` or kept out of the evaluated queues, and the narrowing is
  stated publicly.
- **switch** — a protected gate fails, and the failure taxonomy traces it to a
  limit of the approach rather than a defect that can be fixed. This means
  something like an interpretation that rules cannot express, as opposed to a
  typo in a rule.
- A protected failure that traces to a fixable defect is fixed and rerun.
  Every run, including the failed one, stays in the report.
- If any protected unit is `unresolved`, the decision is `unresolved` until
  the label check is done.

## Sources

The research behind version 1 is recorded in
`research/2026-10-06-gate-research.md`. In short:

- **The categories** come from issue #13 and `FEASIBILITY_RECOMMENDATION.md`.
- **What each gate checks** comes from the seed's own fields.
- **The legal rules** come from 14 CFR Part 39 and AC 39-7D.
- **The counting conventions** come from the FAA AD Manual.
- **The record and claim limits** come from AC 39-9, 14 CFR 91.417, and EASA
  AMC M.A.305.
- **The new cases** come from documented failures: FAA and DOT OIG audits and
  enforcement cases, and NTSB recommendations.
- **Freezing in advance and the protected/aggregate split** follow standard
  evaluation practice. The budgets are declared policy.
