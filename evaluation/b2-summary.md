# B2 Summary

Prompt version `e0a54c1578a5`. Mechanical gates only; gates 5 and 11 are on each run's hand-review sheet. S1 (hand-written rules) passes every mechanical gate on the 18 AD 2025-19-13 units.

| Model | Effort | Repeats | Cost | Cost per engine check | Mean latency |
|---|---|---|---|---|---|
| `claude-haiku-5-5` | high | 3 | $0.1448 | $0.00146 | 212.6 s (batch) |
| `claude-haiku-5-5` | low | 3 | $0.0712 | $0.00072 | 212.6 s (batch) |
| `claude-haiku-5-5` | max | 3 | $0.3921 | $0.00396 | 252.9 s (batch) |
| `claude-haiku-5-5` | max | 3 | $1.328 | $0.01341 | 678.0 s (batch) |
| `claude-haiku-5-5` | medium | 3 | $0.0992 | $0.001 | 242.9 s (batch) |
| `claude-sonnet-5-5` | high | 3 | $1.6954 | $0.01713 | 404.8 s (batch) |
| `claude-sonnet-5-5` | low | 3 | $1.2916 | $0.01305 | 465.0 s (batch) |
| `claude-sonnet-5-5` | medium | 3 | $1.3027 | $0.01316 | 455.2 s (batch) |

## `claude-haiku-5-5` at high effort, output cap 16,000

Failures per unit, as runs failing out of 3. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 3) | Answers seen |
|---|---|---|---|
| seed-001 | 2025-18469 | 10 (1/3) | applies/action_required |
| seed-005 | 2025-18469 | 8* (3/3) | applies/action_required |
| seed-006 | 2025-18469 | 8* (1/3) | applies/action_required |
| seed-007 | 2025-18469 | 8* (1/3) | applies/action_required |
| seed-011 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-012 | 2026-16954 | 10 (3/3) | does_not_apply/None |
| seed-013 | 2026-16954 | 1* (3/3), 10 (3/3) | applies/no_action_triggered |
| seed-014 | 2026-16954 | 3* (3/3), 10 (3/3) | applies/action_required_on_event; applies/no_action_triggered |
| seed-015 | 2025-20088 | 10 (3/3) | applies/no_action_triggered |
| seed-016 | 2025-17066 | 6* (2/3), 10 (3/3) | applies/action_required |
| seed-017 | 2025-17066 | 10 (3/3) | applies/action_required |
| seed-018 | 2025-18469 | 10 (3/3), 12 (1/3) | applies/needs_review; applies/no_action_triggered |
| seed-020/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-020/2022-02574 | 2022-02574 | 10 (2/3) | unknown/needs_review |
| seed-021 | 2022-02574 | 10 (2/3) | unknown/needs_review |
| seed-022/2021-14268 | 2021-14268 | 3* (3/3), 10 (3/3) | applies/action_required |
| seed-022/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-023/2025-18469 | 2025-18469 | 6* (1/3) | applies/action_required |
| seed-023/2026-16954 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-023/2025-17066 | 2025-17066 | 6* (3/3), 10 (3/3), 13 (1/3) | applies/action_required_on_event; applies/no_action_triggered |
| seed-024 | 2025-18469 | 9* (1/3), 12 (1/3) | applies/needs_review; applies/no_action_triggered |
| seed-027 | 2025-18469 | 10 (2/3) | applies/action_required |
| seed-029 | 2025-18469 | 3* (2/3), 9* (3/3) | applies/action_required; unknown/needs_review |

Units whose answer changed between repeats: seed-014, seed-018, seed-023/2025-17066, seed-024, seed-026, seed-029.

## `claude-haiku-5-5` at low effort, output cap 16,000

Failures per unit, as runs failing out of 3. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 3) | Answers seen |
|---|---|---|---|
| seed-001 | 2025-18469 | 10 (2/3) | applies/action_required |
| seed-005 | 2025-18469 | 8* (3/3) | applies/action_required; applies/action_required_on_event |
| seed-006 | 2025-18469 | 8* (1/3) | applies/action_required |
| seed-011 | 2026-16954 | 6* (1/3), 10 (3/3) | applies/action_required_on_event |
| seed-012 | 2026-16954 | 9* (1/3), 10 (3/3), 12 (1/3) | does_not_apply/None; unknown/needs_review |
| seed-013 | 2026-16954 | 1* (2/3), 10 (3/3), 12 (1/3) | applies/needs_review; applies/no_action_triggered |
| seed-014 | 2026-16954 | 3* (3/3), 10 (3/3) | applies/action_required_on_event; applies/no_action_triggered |
| seed-015 | 2025-20088 | 10 (3/3), 12 (1/3) | applies/no_action_triggered; unknown/needs_review |
| seed-016 | 2025-17066 | 6* (1/3), 10 (3/3) | applies/action_required |
| seed-017 | 2025-17066 | 6* (1/3), 10 (3/3) | unknown/needs_review |
| seed-018 | 2025-18469 | 10 (3/3) | applies/no_action_triggered |
| seed-020/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-020/2022-02574 | 2022-02574 | 10 (3/3) | unknown/needs_review |
| seed-021 | 2022-02574 | 10 (3/3) | unknown/needs_review |
| seed-022/2021-14268 | 2021-14268 | 3* (3/3), 10 (3/3) | applies/action_required |
| seed-022/2021-11960 | 2021-11960 | 10 (2/3) | unknown/needs_review |
| seed-023/2026-16954 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-023/2025-17066 | 2025-17066 | 6* (2/3), 10 (3/3), 13 (1/3) | applies/action_required_on_event; applies/no_action_triggered |
| seed-027 | 2025-18469 | 4* (1/3) | applies/action_required |
| seed-029 | 2025-18469 | 3* (2/3), 9* (3/3), 10 (2/3) | applies/action_required; applies/needs_review |

Units whose answer changed between repeats: seed-005, seed-008, seed-012, seed-013, seed-014, seed-015, seed-023/2025-17066, seed-023/2025-18469, seed-028, seed-029.

## `claude-haiku-5-5` at max effort, output cap 16,000

Failures per unit, as runs failing out of 3. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 3) | Answers seen |
|---|---|---|---|
| seed-001 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-002 | 2025-18469 | 6* (3/3), 7* (3/3), 9* (3/3), 10 (3/3), 12 (3/3), 13 (3/3) | no_answer |
| seed-003 | 2025-18469 | 3* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-005 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-006 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-007 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-008 | 2025-18469 | 1* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3) | no_answer |
| seed-009 | 2025-18469 | 3* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-010 | 2025-18469 | 2* (1/3), 6* (1/3), 7* (1/3), 10 (1/3), 12 (1/3) | no_answer; outside_supported_scope/None |
| seed-011 | 2026-16954 | 1* (3/3), 6* (3/3), 7* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-012 | 2026-16954 | 6* (3/3), 7* (3/3), 9* (3/3), 10 (3/3), 12 (3/3), 13 (3/3) | no_answer |
| seed-013 | 2026-16954 | 1* (3/3), 6* (3/3), 7* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-014 | 2026-16954 | 3* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-015 | 2025-20088 | 6* (3/3), 7* (3/3), 10 (3/3), 12 (3/3), 13 (3/3) | no_answer |
| seed-016 | 2025-17066 | 1* (3/3), 6* (3/3), 7* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-017 | 2025-17066 | 1* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-018 | 2025-18469 | 6* (3/3), 7* (3/3), 10 (3/3), 12 (3/3), 13 (3/3) | no_answer |
| seed-019 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-020/2021-11960 | 2021-11960 | 3* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-020/2022-02574 | 2022-02574 | 3* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-021 | 2022-02574 | 3* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-022/2021-14268 | 2021-14268 | 3* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-022/2021-11960 | 2021-11960 | 3* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-023/2025-18469 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-023/2026-16954 | 2026-16954 | 1* (3/3), 6* (3/3), 7* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-023/2025-17066 | 2025-17066 | 6* (3/3), 7* (3/3), 10 (3/3), 12 (3/3), 13 (3/3) | no_answer |
| seed-024 | 2025-18469 | 6* (3/3), 7* (3/3), 9* (3/3), 10 (3/3), 12 (3/3), 13 (3/3) | no_answer |
| seed-026 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-027 | 2025-18469 | 1* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3) | no_answer |
| seed-028 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-029 | 2025-18469 | 3* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 9* (3/3), 10 (3/3) | no_answer |

Units whose answer changed between repeats: seed-010.

## `claude-haiku-5-5` at max effort, output cap 64,000

Failures per unit, as runs failing out of 3. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 3) | Answers seen |
|---|---|---|---|
| seed-001 | 2025-18469 | 1* (1/3), 6* (1/3), 7* (1/3), 8* (1/3), 10 (1/3), 12 (1/3) | applies/action_required; no_answer |
| seed-005 | 2025-18469 | 8* (3/3) | applies/action_required |
| seed-006 | 2025-18469 | 1* (2/3), 6* (2/3), 7* (2/3), 8* (2/3), 10 (2/3), 12 (2/3) | applies/action_required; no_answer |
| seed-007 | 2025-18469 | 1* (1/3), 6* (1/3), 7* (1/3), 8* (1/3), 10 (1/3), 12 (1/3) | applies/action_required; no_answer |
| seed-011 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-012 | 2026-16954 | 10 (3/3) | does_not_apply/None |
| seed-013 | 2026-16954 | 1* (1/3), 6* (1/3), 7* (1/3), 10 (3/3), 12 (1/3) | applies/action_required_on_event; no_answer |
| seed-014 | 2026-16954 | 3* (3/3), 6* (3/3), 7* (3/3), 10 (3/3) | no_answer |
| seed-015 | 2025-20088 | 10 (1/3) | applies/no_action_triggered |
| seed-016 | 2025-17066 | 6* (1/3), 10 (2/3) | applies/action_required |
| seed-017 | 2025-17066 | 10 (2/3) | applies/action_required |
| seed-018 | 2025-18469 | 13 (1/3) | applies/action_required_on_event; applies/no_action_triggered |
| seed-020/2021-11960 | 2021-11960 | 3* (2/3), 4* (2/3), 6* (2/3), 7* (2/3), 10 (3/3) | no_answer; unknown/needs_review |
| seed-020/2022-02574 | 2022-02574 | 3* (1/3), 6* (3/3), 7* (1/3), 10 (1/3) | no_answer; unknown/needs_review |
| seed-021 | 2022-02574 | 6* (2/3), 10 (3/3) | unknown/needs_review |
| seed-022/2021-14268 | 2021-14268 | 3* (3/3), 4* (1/3), 6* (1/3), 7* (1/3), 10 (3/3) | applies/action_required; no_answer |
| seed-022/2021-11960 | 2021-11960 | 3* (1/3), 4* (1/3), 6* (2/3), 7* (1/3), 10 (2/3) | no_answer; unknown/needs_review |
| seed-023/2025-18469 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-023/2026-16954 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-023/2025-17066 | 2025-17066 | 6* (3/3), 7* (3/3), 10 (3/3), 12 (3/3), 13 (3/3) | no_answer |
| seed-026 | 2025-18469 | 1* (3/3), 6* (3/3), 7* (3/3), 8* (3/3), 10 (3/3), 12 (3/3) | no_answer |
| seed-027 | 2025-18469 | 1* (2/3), 4* (2/3), 6* (2/3), 7* (2/3), 8* (2/3), 10 (3/3) | applies/action_required; no_answer |
| seed-028 | 2025-18469 | 1* (1/3), 6* (1/3), 7* (1/3), 8* (1/3), 10 (1/3), 12 (1/3) | applies/action_required; no_answer |
| seed-029 | 2025-18469 | 3* (3/3), 4* (3/3), 6* (3/3), 7* (3/3), 9* (3/3), 10 (3/3) | no_answer |

Units whose answer changed between repeats: seed-001, seed-006, seed-007, seed-013, seed-018, seed-020/2021-11960, seed-020/2022-02574, seed-022/2021-11960, seed-022/2021-14268, seed-027, seed-028.

## `claude-haiku-5-5` at medium effort, output cap 16,000

Failures per unit, as runs failing out of 3. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 3) | Answers seen |
|---|---|---|---|
| seed-005 | 2025-18469 | 8* (3/3) | applies/action_required |
| seed-008 | 2025-18469 | 8* (1/3) | applies/action_required; applies/action_required_on_event |
| seed-011 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-012 | 2026-16954 | 10 (3/3) | does_not_apply/None |
| seed-013 | 2026-16954 | 1* (2/3), 10 (3/3), 12 (1/3) | applies/needs_review; applies/no_action_triggered |
| seed-014 | 2026-16954 | 3* (3/3), 10 (3/3) | applies/no_action_triggered |
| seed-015 | 2025-20088 | 10 (3/3) | applies/no_action_triggered |
| seed-016 | 2025-17066 | 6* (1/3), 10 (3/3) | applies/action_required |
| seed-017 | 2025-17066 | 10 (3/3) | applies/action_required |
| seed-018 | 2025-18469 | 10 (3/3) | applies/no_action_triggered |
| seed-020/2021-11960 | 2021-11960 | 10 (3/3) | applies/needs_review; unknown/needs_review |
| seed-020/2022-02574 | 2022-02574 | 10 (2/3) | unknown/needs_review |
| seed-021 | 2022-02574 | 10 (3/3) | unknown/needs_review |
| seed-022/2021-14268 | 2021-14268 | 3* (3/3), 10 (3/3) | applies/action_required |
| seed-022/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-023/2026-16954 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-023/2025-17066 | 2025-17066 | 6* (2/3), 10 (3/3) | applies/no_action_triggered |
| seed-027 | 2025-18469 | 4* (2/3) | applies/action_required |
| seed-028 | 2025-18469 | 8* (1/3) | applies/action_required; applies/action_required_on_event |
| seed-029 | 2025-18469 | 3* (2/3), 9* (3/3), 10 (2/3) | applies/action_required; applies/needs_review |

Units whose answer changed between repeats: seed-001, seed-007, seed-008, seed-013, seed-020/2021-11960, seed-028, seed-029.

## `claude-sonnet-5-5` at high effort, output cap 16,000

Failures per unit, as runs failing out of 3. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 3) | Answers seen |
|---|---|---|---|
| seed-005 | 2025-18469 | 8* (3/3) | applies/action_required |
| seed-011 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-012 | 2026-16954 | 10 (3/3) | does_not_apply/None |
| seed-013 | 2026-16954 | 6* (2/3), 10 (3/3) | applies/action_required_on_event |
| seed-014 | 2026-16954 | 3* (3/3), 6* (1/3), 10 (3/3) | applies/action_required_on_event |
| seed-015 | 2025-20088 | 10 (3/3) | applies/no_action_triggered |
| seed-016 | 2025-17066 | 10 (3/3) | applies/action_required |
| seed-017 | 2025-17066 | 10 (3/3) | applies/action_required |
| seed-018 | 2025-18469 | 13 (3/3) | applies/action_required_on_event |
| seed-020/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-020/2022-02574 | 2022-02574 | 10 (3/3) | unknown/needs_review |
| seed-021 | 2022-02574 | 10 (2/3) | unknown/needs_review |
| seed-022/2021-14268 | 2021-14268 | 3* (3/3), 10 (3/3) | applies/action_required |
| seed-022/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-023/2026-16954 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-023/2025-17066 | 2025-17066 | 10 (3/3) | applies/no_action_triggered |
| seed-029 | 2025-18469 | 9* (3/3), 10 (2/3) | applies/needs_review |

Units whose answer changed between repeats: seed-001, seed-008, seed-028.

## `claude-sonnet-5-5` at low effort, output cap 16,000

Failures per unit, as runs failing out of 3. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 3) | Answers seen |
|---|---|---|---|
| seed-001 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-005 | 2025-18469 | 8* (3/3) | applies/action_required |
| seed-006 | 2025-18469 | 8* (2/3) | applies/action_required_on_event |
| seed-007 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-008 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-011 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-012 | 2026-16954 | 10 (3/3) | does_not_apply/None |
| seed-013 | 2026-16954 | 1* (3/3), 10 (3/3) | applies/no_action_triggered |
| seed-014 | 2026-16954 | 3* (3/3), 10 (3/3) | applies/action_required_on_event |
| seed-015 | 2025-20088 | 10 (3/3) | applies/no_action_triggered |
| seed-016 | 2025-17066 | 10 (3/3) | applies/action_required |
| seed-017 | 2025-17066 | 10 (3/3) | applies/action_required |
| seed-018 | 2025-18469 | 13 (3/3) | applies/action_required_on_event |
| seed-019 | 2025-18469 | 8* (1/3) | applies/action_required_on_event |
| seed-020/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-020/2022-02574 | 2022-02574 | 10 (3/3) | unknown/needs_review |
| seed-021 | 2022-02574 | 10 (3/3) | unknown/needs_review |
| seed-022/2021-14268 | 2021-14268 | 3* (3/3), 10 (3/3) | applies/action_required |
| seed-022/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-023/2025-18469 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-023/2026-16954 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-023/2025-17066 | 2025-17066 | 10 (3/3) | applies/no_action_triggered |
| seed-026 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-027 | 2025-18469 | 8* (2/3) | applies/action_required_on_event |
| seed-028 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-029 | 2025-18469 | 9* (3/3), 10 (3/3) | applies/needs_review |

Units whose answer changed between repeats: seed-003.

## `claude-sonnet-5-5` at medium effort, output cap 16,000

Failures per unit, as runs failing out of 3. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 3) | Answers seen |
|---|---|---|---|
| seed-005 | 2025-18469 | 8* (3/3) | applies/action_required |
| seed-006 | 2025-18469 | 8* (2/3) | applies/action_required_on_event |
| seed-007 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-008 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-011 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-012 | 2026-16954 | 10 (3/3) | does_not_apply/None |
| seed-013 | 2026-16954 | 1* (3/3), 10 (3/3) | applies/no_action_triggered |
| seed-014 | 2026-16954 | 3* (3/3), 6* (1/3), 10 (3/3) | applies/action_required_on_event |
| seed-015 | 2025-20088 | 10 (3/3) | applies/no_action_triggered |
| seed-016 | 2025-17066 | 10 (3/3) | applies/action_required |
| seed-017 | 2025-17066 | 10 (3/3) | applies/action_required |
| seed-018 | 2025-18469 | 13 (3/3) | applies/action_required_on_event |
| seed-019 | 2025-18469 | 8* (2/3) | applies/action_required_on_event |
| seed-020/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-020/2022-02574 | 2022-02574 | 10 (3/3) | unknown/needs_review |
| seed-021 | 2022-02574 | 10 (3/3) | unknown/needs_review |
| seed-022/2021-14268 | 2021-14268 | 3* (3/3), 10 (3/3) | applies/action_required |
| seed-022/2021-11960 | 2021-11960 | 10 (3/3) | unknown/needs_review |
| seed-023/2025-18469 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-023/2026-16954 | 2026-16954 | 10 (3/3) | applies/action_required_on_event |
| seed-023/2025-17066 | 2025-17066 | 10 (3/3) | applies/no_action_triggered |
| seed-026 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-027 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-028 | 2025-18469 | 8* (3/3) | applies/action_required_on_event |
| seed-029 | 2025-18469 | 9* (3/3), 10 (3/3) | applies/needs_review |

Units whose answer changed between repeats: seed-001.

Gate names: 1 No false clear; 2 No scope leak; 3 No false confidence; 4 Every missing fact named; 6 No fabricated citation; 7 Authority respected; 8 Exact arithmetic; 9 Exact part identity; 10 Required evidence cited; 12 No needless escalation; 13 No false alarm.
