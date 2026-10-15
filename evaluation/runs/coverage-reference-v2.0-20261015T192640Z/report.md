# Coverage run: reference-v2.0

- Records: `evaluation/coverage/reference`; interpreter v2
- Source generation: `gen-20261015T175844Z-57440372`
- Gates 5 and 11 are judged by hand and are pending here.

| Directive | Units | Serial guard | Mechanical gates | Failed units |
|---|---|---|---|---|
| 2013-08448 | 5 | ok | fail | cov-072 (10): expected unknown/needs_review, got unknown/needs_review; cov-073 (8, 13): expected applies/no_action_triggered, got applies/action_required_on_event |
| 2015-12068 | 7 | ok | fail | cov-063 (10): expected does_not_apply/None, got does_not_apply/None; cov-064 (10): expected outside_supported_scope/None, got outside_supported_scope/None; cov-065 (10): expected applies/no_action_triggered, got applies/no_action_triggered; cov-067 (1, 10): expected applies/action_required, got applies/no_action_triggered; cov-068 (4, 9, 10): expected applies/action_required, got applies/action_required |
| 2016-21061 | 5 | ok | fail | cov-022 (10): expected unknown/needs_review, got unknown/needs_review; cov-024 (10): expected unknown/needs_review, got unknown/needs_review; cov-026 (4, 10): expected unknown/needs_review, got unknown/needs_review |
| 2017-14706 | 4 | ok | fail | cov-027 (10): expected unknown/needs_review, got unknown/needs_review; cov-028 (10): expected unknown/needs_review, got unknown/needs_review; cov-030 (10): expected unknown/needs_review, got unknown/needs_review |
| 2019-17403 | 6 | ok | fail | cov-059 (8, 10): expected applies/action_required, got applies/action_required; cov-060 (8, 12): expected applies/action_required, got applies/needs_review; cov-061 (10, 12): expected applies/action_required, got applies/needs_review |
| 2019-19412 | 6 | ok | fail | cov-050 (8): expected applies/action_required, got applies/action_required; cov-051 (10): expected does_not_apply/None, got does_not_apply/None; cov-055 (3, 9, 10): expected unknown/needs_review, got does_not_apply/None |
| 2020-07627 | 4 | ok | pass | cov-018 (12): expected applies/action_required, got applies/needs_review |
| 2021-11960 | 2 | ok | pass | — |
| 2021-14268 | 7 | ok | fail | cov-011 (10, 12): expected applies/no_action_triggered, got applies/needs_review; cov-012 (4): expected applies/needs_review, got applies/needs_review |
| 2021-15486 | 4 | ok | fail | cov-014 (10): expected unknown/needs_review, got unknown/needs_review; cov-015 (10): expected unknown/needs_review, got unknown/needs_review; cov-017 (4, 10): expected unknown/needs_review, got unknown/needs_review |
| 2022-02574 | 5 | ok | fail | cov-006/2022-02574 (10): expected unknown/needs_review, got unknown/needs_review; cov-008 (10): expected unknown/needs_review, got unknown/needs_review; seed-020/2022-02574 (10): expected unknown/needs_review, got unknown/needs_review |
| 2024-12594 | 6 | ok | fail | cov-001 (10): expected applies/needs_review, got applies/needs_review; cov-002 (10): expected applies/needs_review, got applies/needs_review; cov-003 (8, 10, 12): expected applies/action_required, got applies/needs_review; cov-004 (10, 12): expected applies/no_action_triggered, got applies/needs_review; cov-006/2024-12594 (8, 12): expected applies/action_required, got applies/needs_review |
| 2025-17066 | 8 | ok | fail | cov-076 (1): expected applies/action_required, got applies/no_action_triggered; cov-077 (10): expected applies/no_action_triggered, got applies/no_action_triggered; seed-023/2025-17066 (12): expected applies/no_action_triggered, got applies/needs_review |
| 2026-16954 | 8 | ok | fail | cov-079 (10, 12): expected applies/action_required, got applies/needs_review; seed-013 (10): expected applies/action_required_on_event, got applies/action_required_on_event; seed-014 (10): expected applies/needs_review, got applies/needs_review |
