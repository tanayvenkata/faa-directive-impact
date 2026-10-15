# Which Directives Became Evaluated

Applies `PREREGISTRATION.md`, "What Evaluated Means Here", to the reviewed
records ([`report.md`](report.md)). Every judgment here is Claude's, as the
owner's stand-in; no person has checked it. Labels are
`label_review: claude_stand_in`, `independent_check: claude_subagent`.

The three conditions:

1. At least three coverage cases, including one action due or waiting on an
   event, one where nothing is triggered, and one where a named fact is
   missing, unless the directive cannot produce that outcome (stated per
   directive).
2. The independent label check is complete and every disagreement
   adjudicated (`evaluation/coverage/critique/`).
3. The reviewed record passes every protected gate and stays within every
   aggregate budget, including the hand-judged gates 5 and 11
   ([`hand-review.json`](hand-review.json)).

No per-directive exception to condition 1 was stated before scoring, and
none is added now.

## Result: one directive

| Directive | AD | State | Why |
|---|---|---|---|
| 2020-07627 | AD 2020-07-51 | **evaluated** | 4 cases cover action due (cov-018), missing fact (cov-019), and nothing triggered (cov-020, cov-021); label check group A; every mechanical gate passes (one needless escalation, cov-018, within the budget of 1); gates 5 and 11 pass on all 4 units |
| 2025-18469 | AD 2025-19-13 | evaluated (unchanged) | Keeps S1 and its existing evaluation; its reviewed draft is not used by the fleet |
| 2017-14706 | AD 2017-14-07 | not_yet_evaluated | Mechanical gates pass, but condition 1 fails: no unit is action due (all four are `needs_review` or `does_not_apply`) and no exception was stated |
| 2021-15486 | AD 2021-14-19 | not_yet_evaluated | Mechanical gates pass, but condition 1 fails for the same reason |
| 2021-11960 | AD 2021-11-15 | not_yet_evaluated | Mechanical gates pass, but condition 1 fails: no coverage case; its two units are seed units. Superseded by AD 2022-02-09 |
| 2013-08448 | AD 2013-07-10 | not_yet_evaluated | Gates 8, 12 |
| 2015-12068 | AD 2015-10-04 | not_yet_evaluated | Gates 4, 10, 12 |
| 2016-21061 | AD 2016-18-10 | not_yet_evaluated | Gate 4 (cov-026) |
| 2019-17403 | AD 2019-16-01 | not_yet_evaluated | Gates 4, 8, 12 |
| 2019-19412 | AD 2019-18-01 | not_yet_evaluated | Gate 8 (cov-050) |
| 2021-14268 | AD 2021-11-51 | not_yet_evaluated | Gates 4, 10, 12 |
| 2022-02574 | AD 2022-02-09 | not_yet_evaluated | Gate 10 (cov-006) |
| 2024-12594 | AD 2024-11-03 | not_yet_evaluated | Gates 8, 12 |
| 2025-17066 | AD 2025-17-16 | not_yet_evaluated | Gates 4, 12 |
| 2026-16954 | AD 2026-17-03 | not_yet_evaluated | Gates 4, 10, 12 |
| 2012-12329 | AD 2012-09-09 | not_yet_evaluated | No scored unit; superseded by AD 2015-10-04 |

No reviewed record produced a false clear (gate 1). Every failure above
sends an engine to a person or misses a number; none clears an engine that
needs action.
