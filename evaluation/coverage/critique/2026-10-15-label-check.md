# Independent Label Check: Adjudication

Pre-registered in [`../PREREGISTRATION.md`](../PREREGISTRATION.md), "Cases".
A separate Claude Opus subagent derived each outcome from a blind packet
(`label_check.blind_case`: facts and candidates, no expected outcome,
rationale, reason, notes, or forbidden claims) and the directive text. Its
outcomes were compared field by field (`label_check.compare`: applicability,
action status, and whether missing facts are named). Claude, standing in for
the owner, adjudicated each disagreement against the cited text. Both
reviewers are the same model family; their errors can be correlated.

## Group B (AD 2019-18-01, 2019-16-01, 2015-10-04, 2013-07-10, 2025-17-16, 2026-17-03)

39 cases (cov-050 to cov-080 and the seed cases for these directives), 41
outcomes. 8 field disagreements in 6 outcomes.

| Case | Field | Label | Reviewer | Verdict |
|---|---|---|---|---|
| cov-055 | applicability, action status, missing facts | does_not_apply | unknown / needs_review, interpretation named | **Label changed to the reviewer's reading.** Paragraph (c) lists engine serials only, so read literally the AD does not apply. But the engine carries a disk paragraph (g) names for removal, and a screen must not clear that. Now `expert_required`, needs_review with the interpretation question named |
| cov-067 | missing facts | names the A0615 compliance groups | none | **Label kept.** The installed silver-plated nuts settle the action, but the drum inspection timing still depends on the unavailable groups; naming them is correct and informative |
| cov-073 | action status | no_action_triggered | action_required_on_event | **Label kept.** The tube is 4,000 cycles below the paragraph (f) threshold, so nothing is triggered now; paragraph (g)'s check at each installation is recorded as a continuing obligation. Labeled `engineer_interpreted` |
| cov-077 | action status | no_action_triggered | action_required, deadline 2026-01-08 | **Label kept.** On the as-of date the AD is published but not effective; an AD not in force requires no action (schema, `authority_state`; same as seed-015 and cov-005). The deadline is stated in the timing |
| seed-013 | action status | action_required_on_event | action_required | **Label kept.** The visit was inducted on 2026-09-14, before the 2026-09-24 effective date; paragraph (g) applies at "the next engine shop visit after the effective date", and paragraph (h)(3) defines a shop visit by its induction. The reviewer's reading is recorded as the stricter alternative |
| seed-014 | missing facts | readings recorded | interpretation named as a missing fact | **Label kept.** The case already records the two readings and scores safe behavior only (`expert_required`); naming the question twice adds nothing |
