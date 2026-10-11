# B3 run b3-opus-5-5-high-r1-20261011T155547Z-9f32a55

Model `claude-opus-5-5` at high effort, repeat 1; prompt `93fa052fe394`, interpreter v1, gates v1. Cost $0.1758.

| Directive | Field accuracy | Ambiguities flagged | Units | Units with extraction errors | Protected extraction errors |
|---|---|---|---|---|---|
| 2025-18469 | 19/20 | 1/1 | 18 | 10 | 9 |
| 2026-16954 | 21/21 | 1/1 | 5 | 0 | 0 |

## Field errors

- 2025-18469 `required_actions[(g)].combination`: expected `"whichever_occurs_later"`, drafted `"unclear"`
- 2025-18469: additional ambiguity on (i)(2) (for the proofreader)

## Units

| Unit | Expected | Drafted | Reference | Extraction errors | Also fail with reference |
|---|---|---|---|---|---|
| seed-001 | applies/action_required | applies/needs_review | applies/action_required | 8, 10, 12 | – |
| seed-002 | applies/no_action_triggered | applies/no_action_triggered | applies/no_action_triggered | – | – |
| seed-003 | applies/needs_review | applies/needs_review | applies/needs_review | – | – |
| seed-004 | outside_supported_scope/None | outside_supported_scope/None | outside_supported_scope/None | – | – |
| seed-005 | applies/action_required | applies/needs_review | applies/needs_review | 10 | 8, 12 |
| seed-006 | applies/action_required | applies/needs_review | applies/action_required | 8, 12 | – |
| seed-007 | applies/action_required | applies/needs_review | applies/action_required | 8, 12 | – |
| seed-008 | applies/action_required | applies/needs_review | applies/action_required | 8 | – |
| seed-009 | applies/needs_review | applies/needs_review | applies/needs_review | – | – |
| seed-010 | outside_supported_scope/None | outside_supported_scope/None | outside_supported_scope/None | – | – |
| seed-018 | applies/no_action_triggered | applies/no_action_triggered | applies/no_action_triggered | – | – |
| seed-019 | applies/action_required | applies/needs_review | applies/action_required | 8, 12 | – |
| seed-023/2025-18469 | applies/action_required | applies/needs_review | applies/action_required | 8, 12 | – |
| seed-024 | applies/no_action_triggered | applies/no_action_triggered | applies/no_action_triggered | – | – |
| seed-026 | applies/action_required | applies/needs_review | applies/action_required | 8, 12 | – |
| seed-027 | applies/action_required | applies/needs_review | applies/action_required | 8 | – |
| seed-028 | applies/action_required | applies/needs_review | applies/action_required | 8, 12 | – |
| seed-029 | applies/needs_review | applies/needs_review | applies/needs_review | – | – |
| seed-011 | applies/action_required_on_event | applies/action_required_on_event | applies/action_required_on_event | – | – |
| seed-012 | does_not_apply/None | does_not_apply/None | does_not_apply/None | – | – |
| seed-013 | applies/action_required_on_event | applies/action_required_on_event | applies/action_required_on_event | – | 10 |
| seed-014 | applies/needs_review | applies/needs_review | applies/needs_review | – | 10 |
| seed-023/2026-16954 | applies/action_required_on_event | applies/action_required_on_event | applies/action_required_on_event | – | – |

Gates: 1 No false clear; 2 No scope leak; 3 No false confidence; 4 Every missing fact named; 5 No forbidden claim; 6 No fabricated citation; 7 Authority respected; 8 Exact arithmetic; 9 Exact part identity; 10 Required evidence cited; 11 Timing stated correctly; 12 No needless escalation; 13 No false alarm; 14 Candidate recall

- The evaluated claim stays AD 2025-19-13. AD 2026-17-03 results are reported separately; its labels and reference record are Claude drafts awaiting owner confirmation, and they do not widen the claim.
- The reference records were written by the same author as the seed labels (Claude), so field accuracy measures agreement with one reading, as S1 does. The interpreter applies no adjudication: where the readings of AD 2025-19-13 (g) diverge (seed-005), it routes to review even with the reference record, so that unit fails gates 8 and 12 for every system here and is not counted against a draft.
