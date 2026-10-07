# B2 Run b2-haiku-5-5-medium-r1-20261007T230237Z-16a1bf6

| Field | Value |
|---|---|
| System | B2 full-context model |
| Model | `claude-haiku-5-5`, effort `medium` |
| Repeat | 1 (batch) |
| Prompt version | `b73f8e333bee` |
| Gate version | 1 |
| Git commit | `16a1bf688da2d562bcf52903328d3ed4fc9814c5` (dirty: False) |
| Source generation | `gen-20260926T215105Z-7fe9da08` |
| Units | 33; no answer: 0 |
| Cost | $0.0469 total, $0.00142 per unit |
| Tokens | input 10,092, cache write 313,193, cache read 155,977, output 104,102 |
| Mean latency | 121.94 s |

## Method

The prompt contains: the outcome vocabulary and record conventions from evaluation/seed/README.md (including that operator AD records and AMOC claims are claims to check, not evidence), the list of supported engine models, the missing-fact path format, the answer format, and each document's type, publication date, and Federal Register effective date alongside its text. Documents are rendered from the XML with image placeholders, and each unit gets its directive plus the related documents published by its question date. The prompt never contains a case's title, slice, label, rationale, forbidden claims, notes, or any adjudication.

A unit with no usable answer (a refusal, a non-JSON response, or JSON that does not match the answer schema) fails every gate it is covered by, because no safe output was produced. Only transport errors are retried, by the SDK; answers are never retried for content.

Seed-005's expected timing follows informal FAA correspondence (faa-informal-2026-10-05) that is not in the directive text, and its expected `computed.readings` includes an `FAA` reading. A system reading only the text is expected to miss it on gate 8. That is a limit of the text, not a model error, and it was written here before the run.

Gates 5 and 11, missing facts described in words, and locators the index cannot resolve are on the hand-review sheet and pending here.

## Gates on the 18 AD 2025-19-13 units (paired with S1)

| # | Gate | Verdict | Covered | Failed |
|---|---|---|---|---|
| 1 | No false clear | pass | 10 | — |
| 2 | No scope leak | pass | 2 | — |
| 3 | No false confidence | pass | 3 | — |
| 4 | Every missing fact named | unresolved | 5 | seed-003, seed-008, seed-009, seed-027, seed-029 |
| 5 | No forbidden claim | pending_hand_review | 18 | — |
| 6 | No fabricated citation | unresolved | 18 | seed-001, seed-003, seed-004, seed-005, seed-006, seed-007, seed-008, seed-009, seed-010, seed-018, seed-019, seed-023/2025-18469, seed-026, seed-027, seed-028 |
| 7 | Authority respected | pass | 1 | — |
| 8 | Exact arithmetic | unresolved | 10 | seed-005 |
| 9 | Exact part identity | unresolved | 3 | seed-029 |
| 10 | Required evidence cited | unresolved | 18 | seed-001, seed-003, seed-004, seed-005, seed-006, seed-007, seed-008, seed-009, seed-010, seed-018, seed-019, seed-023/2025-18469, seed-026, seed-027, seed-028 |
| 11 | Timing stated correctly | pending_hand_review | 18 | — |
| 12 | No needless escalation | pass | 13 | — |
| 13 | No false alarm | pass | 3 | seed-018 |
| 14 | Candidate recall | not_exercised | — | — |

## Gates on all 33 units

| # | Gate | Verdict | Covered | Failed |
|---|---|---|---|---|
| 1 | No false clear | unresolved | 15 | seed-013 |
| 2 | No scope leak | pass | 3 | — |
| 3 | No false confidence | unresolved | 9 | seed-022/2021-14268 |
| 4 | Every missing fact named | unresolved | 10 | seed-003, seed-008, seed-009, seed-017, seed-022/2021-14268, seed-027, seed-029 |
| 5 | No forbidden claim | pending_hand_review | 33 | — |
| 6 | No fabricated citation | unresolved | 33 | seed-001, seed-003, seed-004, seed-005, seed-006, seed-007, seed-008, seed-009, seed-010, seed-012, seed-013, seed-015, seed-016, seed-017, seed-018, seed-019, seed-020/2021-11960, seed-020/2022-02574, seed-021, seed-022/2021-11960, seed-023/2025-18469, seed-023/2026-16954, seed-025, seed-026, seed-027, seed-028 |
| 7 | Authority respected | pass | 3 | — |
| 8 | Exact arithmetic | unresolved | 10 | seed-005 |
| 9 | Exact part identity | unresolved | 4 | seed-011, seed-013, seed-014, seed-015, seed-020/2021-11960, seed-020/2022-02574, seed-021, seed-023/2026-16954, seed-023/2025-17066, seed-029 |
| 10 | Required evidence cited | unresolved | 33 | seed-001, seed-003, seed-004, seed-005, seed-006, seed-007, seed-008, seed-009, seed-010, seed-011, seed-012, seed-013, seed-014, seed-015, seed-016, seed-017, seed-018, seed-019, seed-020/2021-11960, seed-020/2022-02574, seed-021, seed-022/2021-11960, seed-022/2021-14268, seed-023/2025-17066, seed-023/2025-18469, seed-023/2026-16954, seed-025, seed-026, seed-027, seed-028 |
| 11 | Timing stated correctly | pending_hand_review | 33 | — |
| 12 | No needless escalation | pass | 21 | — |
| 13 | No false alarm | pass | 6 | seed-018 |
| 14 | Candidate recall | not_exercised | — | — |

## Units

| Unit | Directive | Slice | Severity | Failed gates |
|---|---|---|---|---|
| seed-001 | 2025-18469 | exact_match | critical | 6, 10 |
| seed-002 | 2025-18469 | unaffected_part | critical | — |
| seed-003 | 2025-18469 | missing_state | critical | 4, 6, 10 |
| seed-004 | 2025-18469 | out_of_family | high | 6, 10 |
| seed-005 | 2025-18469 | shop_visit_trigger | critical | 6, 8, 10 |
| seed-006 | 2025-18469 | cycle_limit | critical | 6, 10 |
| seed-007 | 2025-18469 | exact_match | critical | 6, 10 |
| seed-008 | 2025-18469 | missing_state | critical | 4, 6, 10 |
| seed-009 | 2025-18469 | missing_state | critical | 4, 6, 10 |
| seed-010 | 2025-18469 | out_of_family | high | 6, 10 |
| seed-011 | 2026-16954 | exact_match | critical | 9, 10 |
| seed-012 | 2026-16954 | unaffected_part | high | 6, 10 |
| seed-013 | 2026-16954 | shop_visit_trigger | high | 1, 6, 9, 10 |
| seed-014 | 2026-16954 | superseded_or_corrected | high | 9, 10 |
| seed-015 | 2025-20088 | effective_date | high | 6, 9, 10 |
| seed-016 | 2025-17066 | exact_match | high | 6, 10 |
| seed-017 | 2025-17066 | missing_state | high | 4, 6, 10 |
| seed-018 | 2025-18469 | effective_date | high | 6, 10, 13 |
| seed-019 | 2025-18469 | cycle_limit | critical | 6, 10 |
| seed-020/2021-11960 | 2021-11960 | effective_date | high | 6, 9, 10 |
| seed-020/2022-02574 | 2022-02574 | effective_date | high | 6, 9, 10 |
| seed-021 | 2022-02574 | missing_incorporated_material | critical | 6, 9, 10 |
| seed-022/2021-14268 | 2021-14268 | missing_incorporated_material | critical | 3, 4, 10 |
| seed-022/2021-11960 | 2021-11960 | missing_incorporated_material | critical | 6, 10 |
| seed-023/2025-18469 | 2025-18469 | multiple_directives | critical | 6, 10 |
| seed-023/2026-16954 | 2026-16954 | multiple_directives | critical | 6, 9, 10 |
| seed-023/2025-17066 | 2025-17066 | multiple_directives | critical | 9, 10 |
| seed-024 | 2025-18469 | unaffected_part | critical | — |
| seed-025 | 2025-17066 | out_of_family | high | 6, 10 |
| seed-026 | 2025-18469 | changed_product | critical | 6, 10 |
| seed-027 | 2025-18469 | operator_assertion | critical | 4, 6, 10 |
| seed-028 | 2025-18469 | operator_assertion | critical | 6, 10 |
| seed-029 | 2025-18469 | part_identity | critical | 4, 9 |

## Failures (mechanical gates)

| Unit | Gate | Detail |
|---|---|---|
| seed-001 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(2) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (a) (document not given)'] |
| seed-001 | 10 | uncited: ['2025-18469 (c)', '2025-18469 (g)', '2025-18469 (i)(2)'] |
| seed-003 | 4 (protected) | not named: ['installed_components[HPT 1st-stage hub].serial_number'] |
| seed-003 | 6 (protected) | fabricated: ['Federal Register document 2025-18469 (c) (document not given)', 'Federal Register document 2025-18469 (g) (document not given)', 'Federal Register document 2025-18469 (h) (document not given)', 'Federal Register document 2025-18469 (i)(2) (document not given)', 'Federal Register document 2025-18469 (a) (document not given)'] |
| seed-003 | 10 | uncited: ['2025-18469 (g)'] |
| seed-004 | 6 (protected) | fabricated: ['Federal Register document 2025-18469 (c) (document not given)'] |
| seed-004 | 10 | uncited: ['2025-18469 (c)'] |
| seed-005 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13, final rule effective 2025-10-29) (a) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(2) (document not given)'] |
| seed-005 | 8 (protected) | expected/got: {'latest_engine_flight_cycles': (20900, 18100), 'readings': ({'A': 18100, 'B': 18040, 'FAA': 20900}, {'Removal required at the 2025-11-12 shop visit itself': 18040})} |
| seed-005 | 10 | uncited: ['2025-18469 (g)', '2025-18469 (i)(2)'] |
| seed-006 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(2) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) DATES (document not given)'] |
| seed-006 | 10 | uncited: ['2025-18469 (c)', '2025-18469 (g)'] |
| seed-007 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(1) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(2) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (a) (document not given)'] |
| seed-007 | 10 | uncited: ['2025-18469 (g)', '2025-18469 (g)'] |
| seed-008 | 4 (protected) | not named: ['installed_components[HPT 2nd-stage hub].serial_number'] |
| seed-008 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (i)(2) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (a) (document not given)'] |
| seed-008 | 10 | uncited: ['2025-18469 (g)', '2025-18469 (g)'] |
| seed-009 | 4 (protected) | not named: ['installed_components[HPT 1st-stage hub]', 'installed_components[HPT 2nd-stage hub]'] |
| seed-009 | 6 (protected) | fabricated: ['Federal Register document 2025-18469 (AD 2025-19-13) (c) (document not given)', 'Federal Register document 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register document 2025-18469 (AD 2025-19-13) (h) (document not given)', 'Federal Register document 2025-18469 (AD 2025-19-13) (i)(1) (document not given)', 'Federal Register document 2025-18469 (AD 2025-19-13) (i)(2) (document not given)', 'Federal Register document 2025-18469 (AD 2025-19-13) (a) (document not given)'] |
| seed-009 | 10 | uncited: ['2025-18469 (c)', '2025-18469 (g)'] |
| seed-010 | 6 (protected) | fabricated: ['Federal Register document 2025-18469 (c) (document not given)', 'Federal Register document 2025-18469 preamble (document not given)'] |
| seed-010 | 10 | uncited: ['2025-18469 (c)'] |
| seed-011 | 9 (protected) | inexact matches ['not tracked at set level']; system said action_required_on_event |
| seed-011 | 10 | uncited: ['2026-18423 (c)', '2026-18423 (h)(2)', '2026-18423 (h)(3)'] |
| seed-012 | 6 (protected) | fabricated: ['Federal Register 2026-16954 (AD 2026-17-03) preamble (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03) (c) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03) (g) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03) (h)(1)(i) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03) (h)(2) (document not given)'] |
| seed-012 | 10 | uncited: ['2026-18423 (c)', '2026-18423 (h)(1)(i)']; clear without its clearing paragraph |
| seed-013 | 1 (protected) | system said no_action_triggered |
| seed-013 | 6 (protected) | fabricated: ['Federal Register 2026-16954 (AD 2026-17-03, final rule) (c) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (a) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (g) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (h)(1) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (h)(2) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (h)(3) (document not given)', 'Federal Register 2026-18423 (correction to AD 2026-17-03) (g) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (i)(1) (document not given)'] |
| seed-013 | 9 (protected) | inexact matches ['not tracked at set level']; system said no_action_triggered |
| seed-013 | 10 | uncited: ['2026-18423 (g)', '2026-18423 (h)(3)', '2026-16954 preamble']; clear without its clearing paragraph |
| seed-014 | 9 (protected) | inexact matches ['not tracked at set level']; system said needs_review |
| seed-014 | 10 | uncited: ['2026-18423 (h)(2)', '2026-18423 preamble'] |
| seed-015 | 6 (protected) | fabricated: ['Federal Register document 2025-20088 (c) (document not given)', 'Federal Register document 2025-20088 (g) (document not given)', 'Federal Register document 2025-20088 (h)(1) (document not given)', 'Federal Register document 2025-20088 (h)(2) (document not given)', 'Federal Register document 2025-20088 preamble (document not given)'] |
| seed-015 | 9 (protected) | inexact matches ['not tracked at set level']; system said no_action_triggered |
| seed-015 | 10 | uncited: ['2025-20088 (a)', '2025-20088 (c)']; clear without its clearing paragraph |
| seed-016 | 6 (protected) | fabricated: ['Federal Register 2025-17066 (a) (document not given)', 'Federal Register 2025-17066 (c) (document not given)', 'Federal Register 2025-17066 (g)(1) (document not given)', 'Federal Register 2025-17066 (g)(2) (document not given)', 'Federal Register 2025-17066 (h) (document not given)', 'Federal Register 2025-17066 (i) (document not given)', 'Federal Register 2025-17066 preamble (document not given)'] |
| seed-016 | 10 | uncited: ['2025-17066 (c)', '2025-17066 (g)(1)(i)', '2025-17066 (g)(2)'] |
| seed-017 | 4 (protected) | not named: ['operator.air_carrier_operation'] |
| seed-017 | 6 (protected) | fabricated: ['Federal Register 2025-17066 (AD 2025-17-16) (a) (document not given)', 'Federal Register 2025-17066 (AD 2025-17-16) (c) (document not given)', 'Federal Register 2025-17066 (AD 2025-17-16) (g)(1) (document not given)', 'Federal Register 2025-17066 (AD 2025-17-16) (g)(2) (document not given)', 'Federal Register 2025-17066 (AD 2025-17-16) (g) (document not given)', 'Federal Register 2025-17066 (AD 2025-17-16) (h) (document not given)'] |
| seed-017 | 10 | uncited: ['2025-17066 (g)(1)(i)', '2025-17066 (g)(2)'] |
| seed-018 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13) (a) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(1) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(2) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) preamble (document not given)'] |
| seed-018 | 10 | uncited: ['2025-18469 (a)', '2025-18469 (g)'] |
| seed-018 | 13 | system said action_required_on_event |
| seed-019 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(2) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (a) (document not given)'] |
| seed-019 | 10 | uncited: ['2025-18469 (g)'] |
| seed-020/2021-11960 | 6 (protected) | fabricated: ['FR Doc 2021-11960 (AD 2021-11-15) (c) (document not given)', 'FR Doc 2021-11960 (AD 2021-11-15) (g)(1) (document not given)', 'FR Doc 2021-11960 (AD 2021-11-15) (g)(2) (document not given)', 'FR Doc 2021-11960 (AD 2021-11-15) (g)(7) (document not given)', 'FR Doc 2021-11960 (AD 2021-11-15) (h)(1) (document not given)', 'FR Doc 2021-11960 (AD 2021-11-15) (h)(2) (document not given)', 'FR Doc 2021-11960 (AD 2021-11-15) (a) (document not given)', 'FR Doc 2022-02574 (AD 2022-02-09) (b) (document not given)', 'FR Doc 2022-02574 (AD 2022-02-09) (c) (document not given)', 'FR Doc 2022-02574 (AD 2022-02-09) preamble (document not given)'] |
| seed-020/2021-11960 | 9 (protected) | inexact matches ['SYN-DISK1-0020', 'SYN-DISK2-0020']; system said needs_review |
| seed-020/2021-11960 | 10 | uncited: ['2021-11960 (c)(1)', '2021-11960 (c)(2)'] |
| seed-020/2022-02574 | 6 (protected) | fabricated: ['Federal Register 2022-02574 (AD 2022-02-09) (a) (document not given)', 'Federal Register 2022-02574 (AD 2022-02-09) (c) (document not given)', 'Federal Register 2022-02574 (AD 2022-02-09) (g)(1) (document not given)', 'Federal Register 2022-02574 (AD 2022-02-09) (g)(2) (document not given)', 'Federal Register 2022-02574 (AD 2022-02-09) (g)(7) (document not given)', 'Federal Register 2022-02574 (AD 2022-02-09) (h)(2) (document not given)', 'Federal Register 2022-02574 (AD 2022-02-09) (b) (document not given)', 'Federal Register 2021-11960 (AD 2021-11-15) (g)(1) (document not given)'] |
| seed-020/2022-02574 | 9 (protected) | inexact matches ['SYN-DISK1-0020', 'SYN-DISK2-0020']; system said needs_review |
| seed-020/2022-02574 | 10 | uncited: ['2022-02574 (a)', '2022-02574 (b)', '2022-02574 (c)'] |
| seed-021 | 6 (protected) | fabricated: ['Federal Register document 2022-02574 preamble (document not given)', 'Federal Register document 2022-02574 (c) (document not given)', 'Federal Register document 2022-02574 (g) (document not given)', 'Federal Register document 2022-02574 (g) (document not given)', 'Federal Register document 2022-02574 (h) (document not given)', 'Federal Register document 2022-02574 (l) (document not given)'] |
| seed-021 | 9 (protected) | inexact matches ['SYN-DISK1-0021', 'SYN-DISK2-0021']; system said needs_review |
| seed-021 | 10 | uncited: ['2022-02574 (c)(1)', '2022-02574 (c)(2)'] |
| seed-022/2021-14268 | 3 (protected) | system said applies/action_required |
| seed-022/2021-14268 | 4 (protected) | not named: ['operator date of actual notice of Emergency AD 2021-11-51'] |
| seed-022/2021-14268 | 10 | uncited: ['2021-14268 (a)', '2021-14268 (c)(1)', '2021-14268 (g)(1)', '2021-14268 (k)'] |
| seed-022/2021-11960 | 6 (protected) | fabricated: ['Federal Register 2021-11960 (AD 2021-11-15) (c) (document not given)', 'Federal Register 2021-11960 (AD 2021-11-15) (g)(1) (document not given)', 'Federal Register 2021-11960 (AD 2021-11-15) (g)(2) (document not given)', 'Federal Register 2021-11960 (AD 2021-11-15) (h)(1) (document not given)', 'Federal Register 2021-11960 (AD 2021-11-15) (h)(2) (document not given)', 'Federal Register 2021-11960 (AD 2021-11-15) preamble (document not given)'] |
| seed-022/2021-11960 | 10 | uncited: ['2021-11960 (c)(1)'] |
| seed-023/2025-18469 | 6 (protected) | fabricated: ['FR Doc. 2025-18469 (AD 2025-19-13) (c) (document not given)', 'FR Doc. 2025-18469 (AD 2025-19-13) (g) (document not given)', 'FR Doc. 2025-18469 (AD 2025-19-13) (h) (document not given)', 'FR Doc. 2025-18469 (AD 2025-19-13) (i)(1) (document not given)', 'FR Doc. 2025-18469 (AD 2025-19-13) (i)(2) (document not given)', 'FR Doc. 2025-18469 (AD 2025-19-13) preamble (document not given)'] |
| seed-023/2025-18469 | 10 | uncited: ['2025-18469 (g)'] |
| seed-023/2026-16954 | 6 (protected) | fabricated: ['Federal Register 2026-16954 (AD 2026-17-03, final rule) (c) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (a) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (g) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (h)(1) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (h)(2) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) (h)(3) (document not given)', 'Federal Register 2026-18423 (correction to AD 2026-17-03) (g) (document not given)', 'Federal Register 2026-16954 (AD 2026-17-03, final rule) preamble (document not given)'] |
| seed-023/2026-16954 | 9 (protected) | inexact matches ['not tracked at set level']; system said action_required_on_event |
| seed-023/2026-16954 | 10 | uncited: ['2026-18423 (c)', '2026-18423 (g)'] |
| seed-023/2025-17066 | 9 (protected) | inexact matches ['PKLBSR2100', 'SYN-HUB1-0023']; system said no_action_triggered |
| seed-023/2025-17066 | 10 | uncited: ['2025-17066 (g)(1)(i)'] |
| seed-025 | 6 (protected) | fabricated: ['Federal Register document 2025-17066 (c) (document not given)'] |
| seed-025 | 10 | uncited: ['2025-17066 (c)'] |
| seed-026 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (i)(1) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13, final rule, effective 2025-10-29) (i)(2) (document not given)'] |
| seed-026 | 10 | uncited: ['2025-18469 (c)', '2025-18469 (g)'] |
| seed-027 | 4 (protected) | not named: ['amoc_claims[AD 2025-19-13]'] |
| seed-027 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(1) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(2) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (j) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) preamble (document not given)'] |
| seed-027 | 10 | uncited: ['2025-18469 (c)', '2025-18469 (g)', '2025-18469 (j)'] |
| seed-028 | 6 (protected) | fabricated: ['Federal Register 2025-18469 (AD 2025-19-13) (c) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (g) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (h) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(1) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) (i)(2) (document not given)', 'Federal Register 2025-18469 (AD 2025-19-13) preamble (document not given)'] |
| seed-028 | 10 | uncited: ['2025-18469 (c)', '2025-18469 (g)'] |
| seed-029 | 4 (protected) | not named: ['installed_components[HPT 1st-stage hub].part_number'] |
| seed-029 | 9 (protected) | inexact matches ['PKLBSK9287']; system said needs_review |

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
