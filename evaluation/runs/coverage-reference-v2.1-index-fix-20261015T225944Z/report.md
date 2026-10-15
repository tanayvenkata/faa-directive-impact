# Coverage run: reference-v2.1-index-fix

- Records: `evaluation/coverage/reference`; interpreter v3
- Source generation: `gen-20261015T175844Z-57440372`
- Gates 5 and 11 are judged by hand and are pending here.

| Directive | Units | Serial guard | Mechanical gates | Failed units |
|---|---|---|---|---|
| 2013-08448 | 5 | ok | pass | — |
| 2015-12068 | 7 | ok | pass | — |
| 2016-21061 | 5 | ok | fail | cov-026 (4): expected unknown/needs_review, got unknown/needs_review |
| 2017-14706 | 4 | ok | pass | — |
| 2019-17403 | 6 | ok | fail | cov-059 (8): expected applies/action_required, got applies/action_required; cov-060 (8, 12): expected applies/action_required, got applies/needs_review; cov-061 (12): expected applies/action_required, got applies/needs_review |
| 2019-19412 | 6 | ok | fail | cov-050 (8): expected applies/action_required, got applies/action_required |
| 2020-07627 | 4 | ok | pass | — |
| 2021-11960 | 2 | ok | pass | — |
| 2021-14268 | 7 | ok | pass | cov-011 (12): expected applies/no_action_triggered, got applies/needs_review |
| 2021-15486 | 4 | ok | pass | — |
| 2022-02574 | 5 | ok | fail | cov-006/2022-02574 (10): expected unknown/needs_review, got unknown/needs_review |
| 2024-12594 | 6 | ok | fail | cov-003 (8, 12): expected applies/action_required, got applies/needs_review; cov-004 (12): expected applies/no_action_triggered, got applies/needs_review; cov-006/2024-12594 (8, 12): expected applies/action_required, got applies/needs_review |
| 2025-17066 | 8 | ok | fail | cov-075 (12): expected applies/no_action_triggered, got applies/needs_review; cov-076 (12): expected applies/action_required, got applies/needs_review; seed-023/2025-17066 (12): expected applies/no_action_triggered, got applies/needs_review |
| 2026-16954 | 8 | ok | pass | cov-079 (12): expected applies/action_required, got applies/needs_review |
