# S1 Run s1-20261006T223638Z-6a301b1

| Field | Value |
|---|---|
| System | S1 rules baseline (hpt_hub_rules) |
| Gate version | 1 |
| Git commit | `6a301b111ae3e2642531c64cd703ce9ac73087fa` |
| Uncommitted changes at run time | False |
| Source generation | `gen-20260926T215105Z-7fe9da08` |
| Source XML SHA-256 | `5bb727351abd85f5ab9b1f4917223766b9f1096073b5ae38f2b627839b3d1ca5` |
| Normalized record SHA-256 | `cb51aa827f2a613c0f15f1baca76ce37bf86870680a925bc025a8a6756883a13` |
| Units scored | 18 |

## Read This First

The S1 rules port the logic of `evaluation/hpt_hub_reference.py`, the reference derivation written alongside the seed labels by the same author, and add citations and wording. A test asserts the two agree on every S1 unit. Agreement with the labels therefore shows that the rules reproduce one reading of AD 2025-19-13 consistently. It does not show that the reading is correct. Practitioner review (issue #9) is the independent check.

Eighteen units cannot support a statistical claim. With zero failures in 18 units, the rough 95% upper bound on the true failure rate is about 17% (3/18); for the ten gate 1 units it is about 30%. Results are exact counts on this disclosed suite, not rates. Protected gates are tripwires, not statistical demonstrations.

Gates 5 and 11 are checked by hand on `hand-review.md`. Until that review is recorded in `verdict.md`, the go / constrain / switch decision is not made.

## Gates

| # | Gate | Verdict | Covered S1 units | Failed |
|---|---|---|---|---|
| 1 | No false clear | pass | 10 | — |
| 2 | No scope leak | pass | 2 | — |
| 3 | No false confidence | pass | 3 | — |
| 4 | Every missing fact named | pass | 5 | — |
| 5 | No forbidden claim | pending_hand_review | 18 | — |
| 6 | No fabricated citation | pass | 18 | — |
| 7 | Authority respected | pass | 1 | — |
| 8 | Exact arithmetic | pass | 10 | — |
| 9 | Exact part identity | pass | 3 | — |
| 10 | Required evidence cited | pass | 18 | — |
| 11 | Timing stated correctly | pending_hand_review | 18 | — |
| 12 | No needless escalation | pass | 13 | — |
| 13 | No false alarm | pass | 3 | — |
| 14 | Candidate recall | not_exercised | — | — |

Gate 10 is scored here on its citation part only: each required (document, paragraph) pair must be cited, and every clear must cite its clearing paragraph. Locators are listed on the hand-review sheet.

## Units

| Unit | Slice | Severity | Failed gates |
|---|---|---|---|
| seed-001 | exact_match | critical | — |
| seed-002 | unaffected_part | critical | — |
| seed-003 | missing_state | critical | — |
| seed-004 | out_of_family | high | — |
| seed-005 | shop_visit_trigger | critical | — |
| seed-006 | cycle_limit | critical | — |
| seed-007 | exact_match | critical | — |
| seed-008 | missing_state | critical | — |
| seed-009 | missing_state | critical | — |
| seed-010 | out_of_family | high | — |
| seed-018 | effective_date | high | — |
| seed-019 | cycle_limit | critical | — |
| seed-023/2025-18469 | multiple_directives | critical | — |
| seed-024 | unaffected_part | critical | — |
| seed-026 | changed_product | critical | — |
| seed-027 | operator_assertion | critical | — |
| seed-028 | operator_assertion | critical | — |
| seed-029 | part_identity | critical | — |

## Failure Taxonomy (mechanical gates)

No mechanical gate failed on any S1 unit. This is expected: the rules port the reference derivation that already agrees with every label (see Read This First).

## Not Yet Evaluated

S1 covers only AD 2025-19-13. These units are neither passes nor failures: seed-011, seed-012, seed-013, seed-014, seed-015, seed-016, seed-017, seed-020/2021-11960, seed-020/2022-02574, seed-021, seed-022/2021-14268, seed-022/2021-11960, seed-023/2026-16954, seed-023/2025-17066, seed-025.

## Known Gaps (from GATES.md)

A pass says nothing about these risks.

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
