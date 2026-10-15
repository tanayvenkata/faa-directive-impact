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

Observation without a disagreement: cov-063 (ESN V15000) falls inside AD
2012-09-09's range but outside the range of AD 2015-10-04, which replaced it.
Both reviewers give the same outcomes; the narrowing of the range between the
two directives is noted for anyone reading the thread, not acted on.

## Group A (AD 2024-11-03, 2022-02-09, 2021-11-51, 2021-14-19, 2020-07-51, 2016-18-10, 2017-14-07)

34 cases (cov-001 to cov-031 and seed-020 to seed-022), 37 outcomes. 7 field
disagreements in 4 outcomes. Every label is kept.

| Case | Field | Label | Reviewer | Verdict |
|---|---|---|---|---|
| cov-005 | action status, missing facts | no_action_triggered (published, not yet effective) | needs_review, hub lists named | **Label kept.** An AD not in force requires no action (same rule as cov-077); the hub lists matter once it takes effect |
| cov-018 | missing facts | none; reason states the record is contradicted | names `ad_records[AD 2020-07-51]` as contradicted | **Label kept.** Both give action_required: the listed disk is installed, so the record cannot clear it. The contradiction is already in the reason |
| cov-024 | applicability, action status, missing facts | unknown / needs_review, bulletin 72-0661 Rev 2 named | applies / no_action_triggered on the operator's inspection record | **Label kept.** The reviewer's argument (listed or not, the record leaves nothing open) is sound only if the recorded inspection used the listed-hub procedure and found no defect; neither can be checked without the bulletin, and a failed inspection triggers removal under (e)(4). Naming the bulletin keeps a person in the loop |
| seed-020 | missing facts | none | names the 72-0713 tables and Figure 1 | **Label kept.** Same outcome; the case's reason already explains why those items do not change it on its as-of date |

The reviewer judged seed-020 to seed-022 against the 2026-10-15 generation's
text, because the seed generation's raw files are not under the retrieval
storage root. The documents are the same Federal Register publications.

## Disputed Labels After the Reference Runs (GATES.md "Disputed Labels")

Raised by the reference-record author after `coverage-reference-v2.1`.
Adjudicated by Claude as the owner's stand-in. No gate text changed.

| Case | Dispute | Verdict |
|---|---|---|
| cov-004 | Should be needs_review: if the replacement hubs are listed, removal is open | **Label kept.** Under the pre-registered Operator Records rule, an unknown listing is not a contradicting fact; the complied record for a passed deadline gives no_action_triggered with the note. Case writer and blind reviewer agree. The screen's review is a safe gate-12 escalation |
| seed-023/2025-17066 | Relies on a free-text program-revision event, not an `ad_records` entry | **Label kept.** The revision is a stated fact of the asset (an event), already scored this way by S1, B2, and B3. The screen not reading free text is a safe gate-12 escalation |
| cov-017, cov-026 | Missing facts written in record-path syntax with extra words, so the scorer could never match them | **Corrected, format only, in their own commit.** cov-026 now uses the project's path convention (`...cycles_since_new_readings[2016-10-07]`); cov-017's installation history has no record path, so it is now a described fact judged on meaning. The reference screens name neither fact, so gate 4 fails for both before and after the correction; no earlier result changes |
| cov-006/2022-02574 | Requires citing 2024-12594 (i), which is outside the thread the frozen manifest records | **Label kept; failure reported.** AD 2024-11-03 (i) does say its (g)(1) satisfies AD 2022-02-09, but the generation records no relationship between them ((b) calls it "related"), so the screen cannot cite it without fabricating under gate 6. A relationship-derivation gap, reported, not patched after the results |
