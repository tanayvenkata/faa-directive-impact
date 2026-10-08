# B2 Run b2-haiku-5-5-max-r3-20261008T003625Z-6d080d8

| Field | Value |
|---|---|
| System | B2 full-context model |
| Model | `claude-haiku-5-5`, effort `max` |
| Repeat | 3 (batch) |
| Prompt version | `e0a54c1578a5` |
| Gate version | 1 |
| Git commit | `6d080d8dc237a7287eab9d6b78d9e80637fb4ec1` (dirty: True) |
| Source generation | `gen-20260926T215105Z-7fe9da08` |
| Units | 33; no answer: 10 |
| Cost | $0.4356 total, $0.0132 per unit |
| Tokens | input 10,092, cache write 194,299, cache read 284,507, output 1,686,168 |
| Mean latency | 911.2 s |

## Method

The prompt contains: the outcome vocabulary and record conventions from evaluation/seed/README.md (including that operator AD records and AMOC claims are claims to check, not evidence), the list of supported engine models, the missing-fact path format, the answer format, and each document's type, publication date, and Federal Register effective date alongside its text. Documents are rendered from the XML with image placeholders, and each unit gets its directive plus the related documents published by its question date. The prompt never contains a case's title, slice, label, rationale, forbidden claims, notes, or any adjudication.

A unit with no usable answer (a refusal, a non-JSON response, or JSON that does not match the answer schema) fails every gate it is covered by, because no safe output was produced. Only transport errors are retried, by the SDK; answers are never retried for content.

Seed-005's expected timing follows informal FAA correspondence (faa-informal-2026-10-05) that is not in the directive text, and its expected `computed.readings` includes an `FAA` reading. A system reading only the text is expected to miss it on gate 8. That is a limit of the text, not a model error, and it was written here before the run.

Gates 5 and 11, missing facts described in words, and locators the index cannot resolve are on the hand-review sheet and pending here.

## Gates on the 18 AD 2025-19-13 units (paired with S1)

| # | Gate | Verdict | Covered | Failed |
|---|---|---|---|---|
| 1 | No false clear | unresolved | 10 | seed-007, seed-023/2025-18469, seed-026, seed-027 |
| 2 | No scope leak | pass | 2 | — |
| 3 | No false confidence | unresolved | 3 | seed-029 |
| 4 | Every missing fact named | unresolved | 5 | seed-027, seed-029 |
| 5 | No forbidden claim | pending_hand_review | 18 | — |
| 6 | No fabricated citation | unresolved | 18 | seed-007, seed-023/2025-18469, seed-026, seed-027, seed-029 |
| 7 | Authority respected | unresolved | 1 | seed-007, seed-023/2025-18469, seed-026, seed-027, seed-029 |
| 8 | Exact arithmetic | unresolved | 10 | seed-005, seed-007, seed-023/2025-18469, seed-026, seed-027 |
| 9 | Exact part identity | unresolved | 3 | seed-029 |
| 10 | Required evidence cited | unresolved | 18 | seed-007, seed-023/2025-18469, seed-026, seed-027, seed-029 |
| 11 | Timing stated correctly | pending_hand_review | 18 | — |
| 12 | No needless escalation | unresolved | 13 | seed-007, seed-023/2025-18469, seed-026 |
| 13 | No false alarm | pass | 3 | — |
| 14 | Candidate recall | not_exercised | — | — |

## Gates on all 33 units

| # | Gate | Verdict | Covered | Failed |
|---|---|---|---|---|
| 1 | No false clear | unresolved | 15 | seed-007, seed-013, seed-023/2025-18469, seed-026, seed-027 |
| 2 | No scope leak | pass | 3 | — |
| 3 | No false confidence | unresolved | 9 | seed-014, seed-020/2021-11960, seed-022/2021-14268, seed-022/2021-11960, seed-029 |
| 4 | Every missing fact named | unresolved | 10 | seed-020/2021-11960, seed-022/2021-11960, seed-027, seed-029 |
| 5 | No forbidden claim | pending_hand_review | 33 | — |
| 6 | No fabricated citation | unresolved | 33 | seed-007, seed-013, seed-014, seed-016, seed-020/2021-11960, seed-020/2022-02574, seed-022/2021-11960, seed-023/2025-18469, seed-023/2025-17066, seed-026, seed-027, seed-029 |
| 7 | Authority respected | unresolved | 3 | seed-007, seed-013, seed-014, seed-020/2021-11960, seed-022/2021-11960, seed-023/2025-18469, seed-023/2025-17066, seed-026, seed-027, seed-029 |
| 8 | Exact arithmetic | unresolved | 10 | seed-005, seed-007, seed-023/2025-18469, seed-026, seed-027 |
| 9 | Exact part identity | unresolved | 4 | seed-029 |
| 10 | Required evidence cited | unresolved | 33 | seed-007, seed-011, seed-012, seed-013, seed-014, seed-015, seed-017, seed-020/2021-11960, seed-021, seed-022/2021-11960, seed-022/2021-14268, seed-023/2025-17066, seed-023/2025-18469, seed-023/2026-16954, seed-026, seed-027, seed-029 |
| 11 | Timing stated correctly | pending_hand_review | 33 | — |
| 12 | No needless escalation | unresolved | 21 | seed-007, seed-013, seed-023/2025-18469, seed-023/2025-17066, seed-026 |
| 13 | No false alarm | pass | 6 | seed-023/2025-17066 (1 of 1 allowed) |
| 14 | Candidate recall | not_exercised | — | — |

## Units

| Unit | Directive | Slice | Severity | Failed gates |
|---|---|---|---|---|
| seed-001 | 2025-18469 | exact_match | critical | — |
| seed-002 | 2025-18469 | unaffected_part | critical | — |
| seed-003 | 2025-18469 | missing_state | critical | — |
| seed-004 | 2025-18469 | out_of_family | high | — |
| seed-005 | 2025-18469 | shop_visit_trigger | critical | 8 |
| seed-006 | 2025-18469 | cycle_limit | critical | — |
| seed-007 | 2025-18469 | exact_match | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-008 | 2025-18469 | missing_state | critical | — |
| seed-009 | 2025-18469 | missing_state | critical | — |
| seed-010 | 2025-18469 | out_of_family | high | — |
| seed-011 | 2026-16954 | exact_match | critical | 10 |
| seed-012 | 2026-16954 | unaffected_part | high | 10 |
| seed-013 | 2026-16954 | shop_visit_trigger | high | 1, 6, 7, 10, 12 (no answer) |
| seed-014 | 2026-16954 | superseded_or_corrected | high | 3, 6, 7, 10 (no answer) |
| seed-015 | 2025-20088 | effective_date | high | 10 |
| seed-016 | 2025-17066 | exact_match | high | 6 |
| seed-017 | 2025-17066 | missing_state | high | 10 |
| seed-018 | 2025-18469 | effective_date | high | — |
| seed-019 | 2025-18469 | cycle_limit | critical | — |
| seed-020/2021-11960 | 2021-11960 | effective_date | high | 3, 4, 6, 7, 10 (no answer) |
| seed-020/2022-02574 | 2022-02574 | effective_date | high | 6 |
| seed-021 | 2022-02574 | missing_incorporated_material | critical | 10 |
| seed-022/2021-14268 | 2021-14268 | missing_incorporated_material | critical | 3, 10 |
| seed-022/2021-11960 | 2021-11960 | missing_incorporated_material | critical | 3, 4, 6, 7, 10 (no answer) |
| seed-023/2025-18469 | 2025-18469 | multiple_directives | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-023/2026-16954 | 2026-16954 | multiple_directives | critical | 10 |
| seed-023/2025-17066 | 2025-17066 | multiple_directives | critical | 6, 7, 10, 12, 13 (no answer) |
| seed-024 | 2025-18469 | unaffected_part | critical | — |
| seed-025 | 2025-17066 | out_of_family | high | — |
| seed-026 | 2025-18469 | changed_product | critical | 1, 6, 7, 8, 10, 12 (no answer) |
| seed-027 | 2025-18469 | operator_assertion | critical | 1, 4, 6, 7, 8, 10 (no answer) |
| seed-028 | 2025-18469 | operator_assertion | critical | — |
| seed-029 | 2025-18469 | part_identity | critical | 3, 4, 6, 7, 9, 10 (no answer) |

## Failures (mechanical gates)

| Unit | Gate | Detail |
|---|---|---|
| seed-005 | 8 (protected) | expected/got: {'latest_engine_flight_cycles': (20900, 18100), 'readings': ({'A': 18100, 'B': 18040, 'FAA': 20900}, {'Shop-visit-anchored reading (later read as first)': 18040})} |
| seed-007 | 1 (protected) | no_answer |
| seed-007 | 6 (protected) | no_answer |
| seed-007 | 7 (protected) | expected in_force, system said no_answer |
| seed-007 | 8 (protected) | no_answer |
| seed-007 | 10 | no_answer |
| seed-007 | 12 | no_answer |
| seed-011 | 10 | uncited: ['2026-18423 (c)', '2026-18423 (h)(2)', '2026-18423 (h)(3)'] |
| seed-012 | 10 | uncited: ['2026-18423 (c)', '2026-18423 (h)(1)(i)'] |
| seed-013 | 1 (protected) | no_answer |
| seed-013 | 6 (protected) | no_answer |
| seed-013 | 7 (protected) | expected in_force, system said no_answer |
| seed-013 | 10 | no_answer |
| seed-013 | 12 | no_answer |
| seed-014 | 3 (protected) | no_answer |
| seed-014 | 6 (protected) | no_answer |
| seed-014 | 7 (protected) | expected in_force, system said no_answer |
| seed-014 | 10 | no_answer |
| seed-015 | 10 | uncited: ['2025-20088 (a)'] |
| seed-016 | 6 (protected) | fabricated: ['2025-17066 Table 1 to paragraph (g)'] |
| seed-017 | 10 | uncited: ['2025-17066 (g)(1)(i)'] |
| seed-020/2021-11960 | 3 (protected) | no_answer |
| seed-020/2021-11960 | 4 (protected) | no_answer |
| seed-020/2021-11960 | 6 (protected) | no_answer |
| seed-020/2021-11960 | 7 (protected) | expected in_force, system said no_answer |
| seed-020/2021-11960 | 10 | no_answer |
| seed-020/2022-02574 | 6 (protected) | fabricated: ['2022-02574 Note 1 to paragraph (g)(1)'] |
| seed-021 | 10 | uncited: ['2022-02574 (c)(1)', '2022-02574 (c)(2)'] |
| seed-022/2021-14268 | 3 (protected) | system said applies/action_required |
| seed-022/2021-14268 | 10 | uncited: ['2021-14268 (k)'] |
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
| seed-023/2026-16954 | 10 | uncited: ['2026-18423 (c)'] |
| seed-023/2025-17066 | 6 (protected) | no_answer |
| seed-023/2025-17066 | 7 (protected) | expected in_force, system said no_answer |
| seed-023/2025-17066 | 10 | no_answer |
| seed-023/2025-17066 | 12 | no_answer |
| seed-023/2025-17066 | 13 | no_answer |
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
