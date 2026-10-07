# B2 Summary

Prompt version `e0a54c1578a5`. Mechanical gates only; gates 5 and 11 are on each run's hand-review sheet. S1 (hand-written rules) passes every mechanical gate on the 18 AD 2025-19-13 units.

| Model | Effort | Repeats | Cost | Cost per engine check | Mean latency |
|---|---|---|---|---|---|
| `claude-haiku-5-5` | medium | 1 | $0.04 | $0.00121 | 303.7 s (batch) |
| `claude-sonnet-5-5` | medium | 1 | $0.4836 | $0.01465 | 454.7 s (batch) |

## `claude-haiku-5-5`

Failures per unit, as runs failing out of 1. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 1) | Answers seen |
|---|---|---|---|
| seed-005 | 2025-18469 | 8* (1/1) | applies/action_required |
| seed-008 | 2025-18469 | 8* (1/1) | applies/action_required_on_event |
| seed-011 | 2026-16954 | 10 (1/1) | applies/action_required_on_event |
| seed-012 | 2026-16954 | 10 (1/1) | does_not_apply/None |
| seed-013 | 2026-16954 | 1* (1/1), 10 (1/1) | applies/no_action_triggered |
| seed-014 | 2026-16954 | 3* (1/1), 10 (1/1) | applies/no_action_triggered |
| seed-015 | 2025-20088 | 10 (1/1) | applies/no_action_triggered |
| seed-016 | 2025-17066 | 6* (1/1), 10 (1/1) | applies/action_required |
| seed-017 | 2025-17066 | 10 (1/1) | applies/action_required |
| seed-018 | 2025-18469 | 10 (1/1) | applies/no_action_triggered |
| seed-020/2021-11960 | 2021-11960 | 10 (1/1) | unknown/needs_review |
| seed-020/2022-02574 | 2022-02574 | 10 (1/1) | unknown/needs_review |
| seed-021 | 2022-02574 | 10 (1/1) | unknown/needs_review |
| seed-022/2021-14268 | 2021-14268 | 3* (1/1), 4* (1/1), 10 (1/1) | applies/action_required |
| seed-022/2021-11960 | 2021-11960 | 10 (1/1) | unknown/needs_review |
| seed-023/2026-16954 | 2026-16954 | 10 (1/1) | applies/action_required_on_event |
| seed-023/2025-17066 | 2025-17066 | 10 (1/1) | applies/no_action_triggered |
| seed-027 | 2025-18469 | 4* (1/1) | applies/action_required |
| seed-029 | 2025-18469 | 9* (1/1), 10 (1/1) | applies/needs_review |

Units whose answer changed between repeats: none.

## `claude-sonnet-5-5`

Failures per unit, as runs failing out of 1. Protected gates are marked *.

| Unit | Directive | Failed gates (runs out of 1) | Answers seen |
|---|---|---|---|
| seed-005 | 2025-18469 | 8* (1/1) | applies/action_required |
| seed-006 | 2025-18469 | 8* (1/1) | applies/action_required_on_event |
| seed-007 | 2025-18469 | 8* (1/1) | applies/action_required_on_event |
| seed-008 | 2025-18469 | 8* (1/1) | applies/action_required_on_event |
| seed-011 | 2026-16954 | 10 (1/1) | applies/action_required_on_event |
| seed-012 | 2026-16954 | 10 (1/1) | does_not_apply/None |
| seed-013 | 2026-16954 | 1* (1/1), 10 (1/1) | applies/no_action_triggered |
| seed-014 | 2026-16954 | 3* (1/1), 10 (1/1) | applies/action_required_on_event |
| seed-015 | 2025-20088 | 10 (1/1) | applies/no_action_triggered |
| seed-016 | 2025-17066 | 10 (1/1) | applies/action_required |
| seed-017 | 2025-17066 | 10 (1/1) | applies/action_required |
| seed-018 | 2025-18469 | 13 (1/1) | applies/action_required_on_event |
| seed-020/2021-11960 | 2021-11960 | 10 (1/1) | unknown/needs_review |
| seed-020/2022-02574 | 2022-02574 | 10 (1/1) | unknown/needs_review |
| seed-021 | 2022-02574 | 10 (1/1) | unknown/needs_review |
| seed-022/2021-14268 | 2021-14268 | 3* (1/1), 4* (1/1), 10 (1/1) | applies/action_required |
| seed-022/2021-11960 | 2021-11960 | 10 (1/1) | unknown/needs_review |
| seed-023/2025-18469 | 2025-18469 | 8* (1/1) | applies/action_required_on_event |
| seed-023/2026-16954 | 2026-16954 | 10 (1/1) | applies/action_required_on_event |
| seed-023/2025-17066 | 2025-17066 | 10 (1/1) | applies/no_action_triggered |
| seed-026 | 2025-18469 | 8* (1/1) | applies/action_required_on_event |
| seed-027 | 2025-18469 | 8* (1/1) | applies/action_required_on_event |
| seed-028 | 2025-18469 | 8* (1/1) | applies/action_required_on_event |
| seed-029 | 2025-18469 | 9* (1/1), 10 (1/1) | applies/needs_review |

Units whose answer changed between repeats: none.

Gate names: 1 No false clear; 2 No scope leak; 3 No false confidence; 4 Every missing fact named; 6 No fabricated citation; 7 Authority respected; 8 Exact arithmetic; 9 Exact part identity; 10 Required evidence cited; 12 No needless escalation; 13 No false alarm.
