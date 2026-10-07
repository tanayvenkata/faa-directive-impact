# B2 Run b2-haiku-5-5-max-r2-20261007T234622Z-85bb2ec

| Field | Value |
|---|---|
| System | B2 full-context model |
| Model | `claude-haiku-5-5`, effort `max` |
| Repeat | 2 (batch) |
| Prompt version | `e0a54c1578a5` |
| Gate version | 1 |
| Git commit | `85bb2ecfd3bdc5562ecc097379ca9813377dd41c` (dirty: True) |
| Source generation | `gen-20260926T215105Z-7fe9da08` |
| Units | 33; no answer: 30 |
| Cost | $0.1299 total, $0.00394 per unit |
| Tokens | input 10,092, cache write 0, cache read 478,806, output 507,846 |
| Mean latency | 212.69 s |

## Method

The prompt contains: the outcome vocabulary and record conventions from evaluation/seed/README.md (including that operator AD records and AMOC claims are claims to check, not evidence), the list of supported engine models, the missing-fact path format, the answer format, and each document's type, publication date, and Federal Register effective date alongside its text. Documents are rendered from the XML with image placeholders, and each unit gets its directive plus the related documents published by its question date. The prompt never contains a case's title, slice, label, rationale, forbidden claims, notes, or any adjudication.

A unit with no usable answer (a refusal, a non-JSON response, or JSON that does not match the answer schema) fails every gate it is covered by, because no safe output was produced. Only transport errors are retried, by the SDK; answers are never retried for content.

Seed-005's expected timing follows informal FAA correspondence (faa-informal-2026-10-05) that is not in the directive text, and its expected `computed.readings` includes an `FAA` reading. A system reading only the text is expected to miss it on gate 8. That is a limit of the text, not a model error, and it was written here before the run.

Gates 5 and 11, missing facts described in words, and locators the index cannot resolve are on the hand-review sheet and pending here.

## Gates on the 18 AD 2025-19-13 units (paired with S1)

| # | Gate | Verdict | Covered | Failed |
|---|---|---|---|---|
| 1 | No false clear | unresolved | 10 | seed-001, seed-005, seed-006, seed-007, seed-008, seed-019, seed-023/2025-18469, seed-026, seed-027, seed-028 |
| 2 | No scope leak | pass | 2 | — |
| 3 | No false confidence | unresolved | 3 | seed-003, seed-009, seed-029 |
| 4 | Every missing fact named | unresolved | 5 | seed-003, seed-008, seed-009, seed-027, seed-029 |
| 5 | No forbidden claim | pending_hand_review | 18 | — |
| 6 | No fabricated citation | unresolved | 18 | seed-001, seed-002, seed-003, seed-005, seed-006, seed-007, seed-008, seed-009, seed-018, seed-019, seed-023/2025-18469, seed-024, seed-026, seed-027, seed-028, seed-029 |
| 7 | Authority respected | unresolved | 1 | seed-001, seed-002, seed-003, seed-005, seed-006, seed-007, seed-008, seed-009, seed-018, seed-019, seed-023/2025-18469, seed-024, seed-026, seed-027, seed-028, seed-029 |
| 8 | Exact arithmetic | unresolved | 10 | seed-001, seed-005, seed-006, seed-007, seed-008, seed-019, seed-023/2025-18469, seed-026, seed-027, seed-028 |
| 9 | Exact part identity | unresolved | 3 | seed-002, seed-024, seed-029 |
| 10 | Required evidence cited | unresolved | 18 | seed-001, seed-002, seed-003, seed-005, seed-006, seed-007, seed-008, seed-009, seed-018, seed-019, seed-023/2025-18469, seed-024, seed-026, seed-027, seed-028, seed-029 |
| 11 | Timing stated correctly | pending_hand_review | 18 | — |
| 12 | No needless escalation | unresolved | 13 | seed-001, seed-002, seed-005, seed-006, seed-007, seed-018, seed-019, seed-023/2025-18469, seed-024, seed-026, seed-028 |
| 13 | No false alarm | unresolved | 3 | seed-002, seed-018, seed-024 |
| 14 | Candidate recall | not_exercised | — | — |

## Gates on all 33 units

| # | Gate | Verdict | Covered | Failed |
|---|---|---|---|---|
| 1 | No false clear | unresolved | 15 | seed-001, seed-005, seed-006, seed-007, seed-008, seed-011, seed-013, seed-016, seed-017, seed-019, seed-023/2025-18469, seed-023/2026-16954, seed-026, seed-027, seed-028 |
| 2 | No scope leak | pass | 3 | — |
| 3 | No false confidence | unresolved | 9 | seed-003, seed-009, seed-014, seed-020/2021-11960, seed-020/2022-02574, seed-021, seed-022/2021-14268, seed-022/2021-11960, seed-029 |
| 4 | Every missing fact named | unresolved | 10 | seed-003, seed-008, seed-009, seed-017, seed-020/2021-11960, seed-021, seed-022/2021-14268, seed-022/2021-11960, seed-027, seed-029 |
| 5 | No forbidden claim | pending_hand_review | 33 | — |
| 6 | No fabricated citation | unresolved | 33 | seed-001, seed-002, seed-003, seed-005, seed-006, seed-007, seed-008, seed-009, seed-011, seed-012, seed-013, seed-014, seed-015, seed-016, seed-017, seed-018, seed-019, seed-020/2021-11960, seed-020/2022-02574, seed-021, seed-022/2021-14268, seed-022/2021-11960, seed-023/2025-18469, seed-023/2026-16954, seed-023/2025-17066, seed-024, seed-026, seed-027, seed-028, seed-029 |
| 7 | Authority respected | unresolved | 3 | seed-001, seed-002, seed-003, seed-005, seed-006, seed-007, seed-008, seed-009, seed-011, seed-012, seed-013, seed-014, seed-015, seed-016, seed-017, seed-018, seed-019, seed-020/2021-11960, seed-020/2022-02574, seed-021, seed-022/2021-14268, seed-022/2021-11960, seed-023/2025-18469, seed-023/2026-16954, seed-023/2025-17066, seed-024, seed-026, seed-027, seed-028, seed-029 |
| 8 | Exact arithmetic | unresolved | 10 | seed-001, seed-005, seed-006, seed-007, seed-008, seed-019, seed-023/2025-18469, seed-026, seed-027, seed-028 |
| 9 | Exact part identity | unresolved | 4 | seed-002, seed-012, seed-024, seed-029 |
| 10 | Required evidence cited | unresolved | 33 | seed-001, seed-002, seed-003, seed-005, seed-006, seed-007, seed-008, seed-009, seed-011, seed-012, seed-013, seed-014, seed-015, seed-016, seed-017, seed-018, seed-019, seed-020/2021-11960, seed-020/2022-02574, seed-021, seed-022/2021-11960, seed-022/2021-14268, seed-023/2025-17066, seed-023/2025-18469, seed-023/2026-16954, seed-024, seed-026, seed-027, seed-028, seed-029 |
| 11 | Timing stated correctly | pending_hand_review | 33 | — |
| 12 | No needless escalation | unresolved | 21 | seed-001, seed-002, seed-005, seed-006, seed-007, seed-011, seed-012, seed-013, seed-015, seed-016, seed-018, seed-019, seed-023/2025-18469, seed-023/2026-16954, seed-023/2025-17066, seed-024, seed-026, seed-028 |
| 13 | No false alarm | unresolved | 6 | seed-002, seed-012, seed-015, seed-018, seed-023/2025-17066, seed-024 |
| 14 | Candidate recall | not_exercised | — | — |

## Units

| Unit | Directive | Slice | Severity | Failed gates |
|---|---|---|---|---|
| seed-001 | 2025-18469 | exact_match | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-002 | 2025-18469 | unaffected_part | critical | 6, 7, 9, 10, 12, 13 (no answer) |
| seed-003 | 2025-18469 | missing_state | critical | 3, 4, 6, 7, 10 (no answer) |
| seed-004 | 2025-18469 | out_of_family | high | — |
| seed-005 | 2025-18469 | shop_visit_trigger | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-006 | 2025-18469 | cycle_limit | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-007 | 2025-18469 | exact_match | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-008 | 2025-18469 | missing_state | critical | 1, 4, 6, 7, 8, 10 (no answer) |
| seed-009 | 2025-18469 | missing_state | critical | 3, 4, 6, 7, 10 (no answer) |
| seed-010 | 2025-18469 | out_of_family | high | — |
| seed-011 | 2026-16954 | exact_match | critical | 1, 6, 7, 10, 12 (no answer) |
| seed-012 | 2026-16954 | unaffected_part | high | 6, 7, 9, 10, 12, 13 (no answer) |
| seed-013 | 2026-16954 | shop_visit_trigger | high | 1, 6, 7, 10, 12 (no answer) |
| seed-014 | 2026-16954 | superseded_or_corrected | high | 3, 6, 7, 10 (no answer) |
| seed-015 | 2025-20088 | effective_date | high | 6, 7, 10, 12, 13 (no answer) |
| seed-016 | 2025-17066 | exact_match | high | 1, 6, 7, 10, 12 (no answer) |
| seed-017 | 2025-17066 | missing_state | high | 1, 4, 6, 7, 10 (no answer) |
| seed-018 | 2025-18469 | effective_date | high | 6, 7, 10, 12, 13 (no answer) |
| seed-019 | 2025-18469 | cycle_limit | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-020/2021-11960 | 2021-11960 | effective_date | high | 3, 4, 6, 7, 10 (no answer) |
| seed-020/2022-02574 | 2022-02574 | effective_date | high | 3, 6, 7, 10 (no answer) |
| seed-021 | 2022-02574 | missing_incorporated_material | critical | 3, 4, 6, 7, 10 (no answer) |
| seed-022/2021-14268 | 2021-14268 | missing_incorporated_material | critical | 3, 4, 6, 7, 10 (no answer) |
| seed-022/2021-11960 | 2021-11960 | missing_incorporated_material | critical | 3, 4, 6, 7, 10 (no answer) |
| seed-023/2025-18469 | 2025-18469 | multiple_directives | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-023/2026-16954 | 2026-16954 | multiple_directives | critical | 1, 6, 7, 10, 12 (no answer) |
| seed-023/2025-17066 | 2025-17066 | multiple_directives | critical | 6, 7, 10, 12, 13 (no answer) |
| seed-024 | 2025-18469 | unaffected_part | critical | 6, 7, 9, 10, 12, 13 (no answer) |
| seed-025 | 2025-17066 | out_of_family | high | — |
| seed-026 | 2025-18469 | changed_product | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-027 | 2025-18469 | operator_assertion | critical | 1, 4, 6, 7, 8, 10 (no answer) |
| seed-028 | 2025-18469 | operator_assertion | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-029 | 2025-18469 | part_identity | critical | 3, 4, 6, 7, 9, 10 (no answer) |

## Failures (mechanical gates)

| Unit | Gate | Detail |
|---|---|---|
| seed-001 | 1 (protected) | no_answer |
| seed-001 | 6 (protected) | no_answer |
| seed-001 | 7 (protected) | expected in_force, system said no_answer |
| seed-001 | 8 (protected) | no_answer |
| seed-001 | 10 | no_answer |
| seed-001 | 12 | no_answer |
| seed-002 | 6 (protected) | no_answer |
| seed-002 | 7 (protected) | expected in_force, system said no_answer |
| seed-002 | 9 (protected) | no_answer |
| seed-002 | 10 | no_answer |
| seed-002 | 12 | no_answer |
| seed-002 | 13 | no_answer |
| seed-003 | 3 (protected) | no_answer |
| seed-003 | 4 (protected) | no_answer |
| seed-003 | 6 (protected) | no_answer |
| seed-003 | 7 (protected) | expected in_force, system said no_answer |
| seed-003 | 10 | no_answer |
| seed-005 | 1 (protected) | no_answer |
| seed-005 | 6 (protected) | no_answer |
| seed-005 | 7 (protected) | expected in_force, system said no_answer |
| seed-005 | 8 (protected) | no_answer |
| seed-005 | 10 | no_answer |
| seed-005 | 12 | no_answer |
| seed-006 | 1 (protected) | no_answer |
| seed-006 | 6 (protected) | no_answer |
| seed-006 | 7 (protected) | expected in_force, system said no_answer |
| seed-006 | 8 (protected) | no_answer |
| seed-006 | 10 | no_answer |
| seed-006 | 12 | no_answer |
| seed-007 | 1 (protected) | no_answer |
| seed-007 | 6 (protected) | no_answer |
| seed-007 | 7 (protected) | expected in_force, system said no_answer |
| seed-007 | 8 (protected) | no_answer |
| seed-007 | 10 | no_answer |
| seed-007 | 12 | no_answer |
| seed-008 | 1 (protected) | no_answer |
| seed-008 | 4 (protected) | no_answer |
| seed-008 | 6 (protected) | no_answer |
| seed-008 | 7 (protected) | expected in_force, system said no_answer |
| seed-008 | 8 (protected) | no_answer |
| seed-008 | 10 | no_answer |
| seed-009 | 3 (protected) | no_answer |
| seed-009 | 4 (protected) | no_answer |
| seed-009 | 6 (protected) | no_answer |
| seed-009 | 7 (protected) | expected in_force, system said no_answer |
| seed-009 | 10 | no_answer |
| seed-011 | 1 (protected) | no_answer |
| seed-011 | 6 (protected) | no_answer |
| seed-011 | 7 (protected) | expected in_force, system said no_answer |
| seed-011 | 10 | no_answer |
| seed-011 | 12 | no_answer |
| seed-012 | 6 (protected) | no_answer |
| seed-012 | 7 (protected) | expected in_force, system said no_answer |
| seed-012 | 9 (protected) | no_answer |
| seed-012 | 10 | no_answer |
| seed-012 | 12 | no_answer |
| seed-012 | 13 | no_answer |
| seed-013 | 1 (protected) | no_answer |
| seed-013 | 6 (protected) | no_answer |
| seed-013 | 7 (protected) | expected in_force, system said no_answer |
| seed-013 | 10 | no_answer |
| seed-013 | 12 | no_answer |
| seed-014 | 3 (protected) | no_answer |
| seed-014 | 6 (protected) | no_answer |
| seed-014 | 7 (protected) | expected in_force, system said no_answer |
| seed-014 | 10 | no_answer |
| seed-015 | 6 (protected) | no_answer |
| seed-015 | 7 (protected) | no_answer |
| seed-015 | 10 | no_answer |
| seed-015 | 12 | no_answer |
| seed-015 | 13 | no_answer |
| seed-016 | 1 (protected) | no_answer |
| seed-016 | 6 (protected) | no_answer |
| seed-016 | 7 (protected) | expected in_force, system said no_answer |
| seed-016 | 10 | no_answer |
| seed-016 | 12 | no_answer |
| seed-017 | 1 (protected) | no_answer |
| seed-017 | 4 (protected) | no_answer |
| seed-017 | 6 (protected) | no_answer |
| seed-017 | 7 (protected) | expected in_force, system said no_answer |
| seed-017 | 10 | no_answer |
| seed-018 | 6 (protected) | no_answer |
| seed-018 | 7 (protected) | no_answer |
| seed-018 | 10 | no_answer |
| seed-018 | 12 | no_answer |
| seed-018 | 13 | no_answer |
| seed-019 | 1 (protected) | no_answer |
| seed-019 | 6 (protected) | no_answer |
| seed-019 | 7 (protected) | expected in_force, system said no_answer |
| seed-019 | 8 (protected) | no_answer |
| seed-019 | 10 | no_answer |
| seed-019 | 12 | no_answer |
| seed-020/2021-11960 | 3 (protected) | no_answer |
| seed-020/2021-11960 | 4 (protected) | no_answer |
| seed-020/2021-11960 | 6 (protected) | no_answer |
| seed-020/2021-11960 | 7 (protected) | expected in_force, system said no_answer |
| seed-020/2021-11960 | 10 | no_answer |
| seed-020/2022-02574 | 3 (protected) | no_answer |
| seed-020/2022-02574 | 6 (protected) | no_answer |
| seed-020/2022-02574 | 7 (protected) | no_answer |
| seed-020/2022-02574 | 10 | no_answer |
| seed-021 | 3 (protected) | no_answer |
| seed-021 | 4 (protected) | no_answer |
| seed-021 | 6 (protected) | no_answer |
| seed-021 | 7 (protected) | expected in_force, system said no_answer |
| seed-021 | 10 | no_answer |
| seed-022/2021-14268 | 3 (protected) | no_answer |
| seed-022/2021-14268 | 4 (protected) | no_answer |
| seed-022/2021-14268 | 6 (protected) | no_answer |
| seed-022/2021-14268 | 7 (protected) | expected in_force, system said no_answer |
| seed-022/2021-14268 | 10 | no_answer |
| seed-022/2021-11960 | 3 (protected) | no_answer |
| seed-022/2021-11960 | 4 (protected) | no_answer |
| seed-022/2021-11960 | 6 (protected) | no_answer |
| seed-022/2021-11960 | 7 (protected) | expected in_force, system said no_answer |
| seed-022/2021-11960 | 10 | no_answer |
| seed-023/2025-18469 | 1 (protected) | no_answer |
| seed-023/2025-18469 | 6 (protected) | no_answer |
| seed-023/2025-18469 | 7 (protected) | expected in_force, system said no_answer |
| seed-023/2025-18469 | 8 (protected) | no_answer |
| seed-023/2025-18469 | 10 | no_answer |
| seed-023/2025-18469 | 12 | no_answer |
| seed-023/2026-16954 | 1 (protected) | no_answer |
| seed-023/2026-16954 | 6 (protected) | no_answer |
| seed-023/2026-16954 | 7 (protected) | expected in_force, system said no_answer |
| seed-023/2026-16954 | 10 | no_answer |
| seed-023/2026-16954 | 12 | no_answer |
| seed-023/2025-17066 | 6 (protected) | no_answer |
| seed-023/2025-17066 | 7 (protected) | expected in_force, system said no_answer |
| seed-023/2025-17066 | 10 | no_answer |
| seed-023/2025-17066 | 12 | no_answer |
| seed-023/2025-17066 | 13 | no_answer |
| seed-024 | 6 (protected) | no_answer |
| seed-024 | 7 (protected) | expected in_force, system said no_answer |
| seed-024 | 9 (protected) | no_answer |
| seed-024 | 10 | no_answer |
| seed-024 | 12 | no_answer |
| seed-024 | 13 | no_answer |
| seed-026 | 1 (protected) | no_answer |
| seed-026 | 6 (protected) | no_answer |
| seed-026 | 7 (protected) | expected in_force, system said no_answer |
| seed-026 | 8 (protected) | no_answer |
| seed-026 | 10 | no_answer |
| seed-026 | 12 | no_answer |
| seed-027 | 1 (protected) | no_answer |
| seed-027 | 4 (protected) | no_answer |
| seed-027 | 6 (protected) | no_answer |
| seed-027 | 7 (protected) | expected in_force, system said no_answer |
| seed-027 | 8 (protected) | no_answer |
| seed-027 | 10 | no_answer |
| seed-028 | 1 (protected) | no_answer |
| seed-028 | 6 (protected) | no_answer |
| seed-028 | 7 (protected) | expected in_force, system said no_answer |
| seed-028 | 8 (protected) | no_answer |
| seed-028 | 10 | no_answer |
| seed-028 | 12 | no_answer |
| seed-029 | 3 (protected) | no_answer |
| seed-029 | 4 (protected) | no_answer |
| seed-029 | 6 (protected) | no_answer |
| seed-029 | 7 (protected) | expected in_force, system said no_answer |
| seed-029 | 9 (protected) | no_answer |
| seed-029 | 10 | no_answer |

## Known Gaps (from GATES.md)

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
