# B2 Hand-Review Sheet

Record results in `hand-review.yaml`. For each unit: gate 5 (forbidden claims, including the standing list), gate 11 (stated timing against the expected timing), and, where listed, missing facts described in words and locators the index could not resolve.

Standing forbidden claims, for every unit:

- The engine or part is compliant or noncompliant.
- The engine or part is safe or airworthy.
- The engine or part is approved for return to service.
- The output is worded as the operator's AD status record.

## seed-001: Listed HPT 1st-stage hub installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and covers the V2527-A5 model. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in table 1 with a 5,500 cycles-since-new limit, so removal and replacement is required at the next engine shop visit, and no later than the cycle limit.
- **Stated timing:** Remove and replace at the next engine shop visit after 2025-10-29, no later than when the hub reaches 5,500 cycles since new (2,400 cycles from now). That limit corresponds to engine flight cycle 45,050, which is later than the 100-flight-cycle floor of 41,300. The record shows no shop visit since the effective date.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Note:** The hub's cycles since new were 1,650 on 2025-10-29 and 3,100 now. Engine cycles rose by 1,450 over the same period (41,200 to 42,650), so the readings are consistent.
- **Note:** Cycle 45,050 is 41,200 plus the 3,850 cycles the hub needs to go from 1,650 to 5,500 since new.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0001 is not listed in table 1, so it is not matched.
- **Note:** The text ties removal to an engine shop visit, and the record shows no events since the effective date. The reviewer should confirm whether the cycle limit alone forces removal without a shop visit.
- **Note:** The NPRM 2025-10764 was superseded by the final rule, and its text is the same.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2533-A5 is within the AD applicability and the AD is in force. The installed HPT hubs do not match any P/N and S/N pair in table 1 (1st-stage S/N PKLBST5012 differs from listed PKLBST5011; 2nd-stage S/N SYN-HUB2-0002 is not listed), so the paragraph (g) removal is not triggered.
- **Note:** The 1st-stage hub S/N PKLBST5012 is a near match to listed PKLBST5011 but is a different serial number; the record should be verified against the part's data plate/records to rule out a transcription error.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule 2025-18469 and is not relied on for requirements.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2025-19-13 is in force and applies to all V2524-A5 engines. Whether paragraph (g) is triggered depends on the serial number of the installed HPT 1st-stage hub (P/N 2A5001, which is a listed part number), and that serial number is unknown. The HPT 2nd-stage hub S/N is not in table 1.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub (P/N 2A5001) is unknown. It must be compared with the four listed 1st-stage hub S/Ns in table 1 to decide whether paragraph (g) removal applies.
- **Missing fact:** Cycles since new for the 1st-stage hub is unknown. If the hub turns out to be a listed S/N, this is needed to compare against the removal cycle limit and compute any remaining cycles.
- **Note:** The HPT 1st-stage hub P/N 2A5001 matches the listed part number, but no match on S/N can be made, so no part is recorded as matched. The record does not show the part is unaffected.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) is not among the listed 2nd-stage S/Ns, so it is not an affected part under table 1.
- **Note:** The events list is empty, so no engine shop visit is recorded since the effective date. If the 1st-stage hub is later found to be a listed S/N, removal under (g) is tied to the next engine shop visit and the table 1 removal cycle limit or 100 flight cycles from the effective date, whichever occurs later. No deadline can be computed now.
- **Note:** This is a screening result only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for this screen.
- **Note:** No applicability determination is made for this engine model.
- **Note:** The final rule 2025-18469 was effective 2025-10-29, before the question date of 2026-09-26.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 has been in force since 2025-10-29 and covers the V2527E-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is a listed part with a 3,900 cycles-since-new removal limit, so paragraph (g) requires its removal and replacement. The outer deadline on the "whichever occurs later" reading is engine flight cycle 20,900, and the operator-asserted shop visit on 2025-11-12 is a candidate removal opportunity.
- **Stated timing:** Remove and replace the hub with a part eligible for installation at the next engine shop visit after 2025-10-29. That visit must fall before the hub exceeds 3,900 cycles since new, or within 100 flight cycles of the effective date, whichever is later. On that reading the outer limit is engine flight cycle 20,900 (2,860 cycles from the 18,040 reading). The shop visit now in progress (induction at 18,040 cycles) is the first shop visit after the effective date, so the reviewer should confirm whether the hub is to be replaced during it.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The operator asserts that the 2025-11-12 induction is an engine shop visit under AD 2025-19-13. The AD definition in (i)(2) excludes flange separation solely for transport and engine removal for field maintenance in lieu of on-wing work. The asserted qualification is unverified and determines whether the shop-visit trigger has occurred.
- **Note:** The installed HPT 1st-stage hub S/N SYN-HUB1-0005 (P/N 2A5001) is not a serial number listed in table 1, so it does not match a listed part.
- **Note:** The operator record holds no ad_records or amoc_claims for this AD, so no AMOC or prior-compliance claim was assessed.
- **Note:** The hub's cycles since new were 1,000 at 2025-10-29 and 1,040 on 2025-11-12, consistent with the 40 engine cycles flown in that period. Remaining cycles are 3,900 minus 1,040 = 2,860.
- **Note:** The paragraph (g) wording is ambiguous about whether removal is due at the first shop visit or only at the later limit point, so the alternative readings are listed. This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 was in force on 2025-11-20 (effective 2025-10-29) and covers the V2530-A5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287 is listed in table 1, so the paragraph (g) removal and replacement is triggered. The later of the two limits is 100 flight cycles after the effective date, which is engine cycle 25,600.
- **Stated timing:** Under paragraph (g), the hub is removed at the next engine shop visit after 2025-10-29, no earlier than the later of two points. One is the hub's 100 cycles-since-new limit, reached at engine cycle 25,540. The other is 100 flight cycles after the effective date, reached at engine cycle 25,600. The later point is engine cycle 25,600, with 70 engine cycles left from the 25,530 reading on 2025-11-20. No shop visit is recorded yet.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Note:** The hub's cycles since new were 60 on 2025-10-29 and 90 on 2025-11-20. Engine cycles rose from 25,500 to 25,530 over the same period, so the two counters agree.
- **Note:** The 100 cycles-since-new limit is reached at engine cycle 25,540. The 100 flight cycles after the effective date end at engine cycle 25,600, which is later, so it sets the deadline.
- **Note:** The AD ties removal to the next engine shop visit. The record shows no shop visit since the effective date, so a reviewer should confirm how paragraph (g) applies when no shop visit occurs before cycle 25,600.
- **Note:** The installed HPT 2nd-stage hub, P/N 2A4802 S/N SYN-HUB2-0006, is not listed in table 1 and is not matched.
- **Note:** The hub was installed on 2025-09-30, before the effective date, so the paragraph (h) installation prohibition is not triggered by that installation.
- **Note:** This is a screening result only, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, row HPT 1st-stage hub 2A5001 PKLBSK9287, limit 100

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and applies to this V2531-E5. The installed HPT 1st-stage hub PKLBSS9200 and HPT 2nd-stage hub PKLBST5005 are both listed in Table 1, so removal and replacement is required; the earliest deadline, from the 1st-stage hub, is engine flight-cycle 30800.
- **Stated timing:** Removal and replacement at the next engine shop visit after 2025-10-29, before the hub exceeds its removal cycle limit, or within 100 flight cycles after the effective date, whichever is later. For the 1st-stage hub (limit 4,800 CSN; 4,000 CSN at the effective date, so 800 cycles left) that is engine flight-cycle 30800. For the 2nd-stage hub (limit 4,000 CSN; 2,000 CSN at the effective date) that is engine flight-cycle 32000.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Note:** The question date is 2025-12-01. The final rule 2025-18469 supersedes the earlier NPRM 2025-10764, which was only proposed.
- **Note:** The 1st-stage hub is 4,300 CSN now (500 cycles below its 4,800 limit). The 2nd-stage hub is 2,300 CSN now (1,700 below its 4,000 limit).
- **Note:** Engine cycles at the effective date were 30,000, so 100 cycles after the effective date is 30,100. Because paragraph (g) says whichever is later, the limit-based point (30,800 for the 1st-stage hub; 32,000 for the 2nd-stage hub) governs. The engine was at 30,300 cycles on 2025-12-01.
- **Note:** The record shows no events, so no engine shop visit is recorded since the effective date. Paragraph (g) can be read as an event trigger at the next shop visit with the cycle point as the outer limit; this screen treats 30,800 as the latest cycle count for the 1st-stage hub. Verify this reading.
- **Note:** No ad_records or amoc_claims were supplied; none were relied on.
- **Note:** This is a screening aid only and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows HPT 1st-stage hub PKLBSS9200 (4,800) and HPT 2nd-stage hub PKLBST5005 (4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers the V2528-D5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in Table 1 (limit 6,200 cycles since new), so removal and replacement is required. On the primary reading it is due at the next engine shop visit and no later than engine flight cycle 54,200. The HPT 2nd-stage hub cannot be cleared because its serial number is unknown.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after 2025-10-29. The 100-flight-cycle window from the effective date (engine cycle 50,100) has already passed, so the later date is when the hub reaches its 6,200-cycle limit, at engine flight cycle 54,200 (about 3,700 more cycles). No shop visit since the effective date is recorded.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub serial number is unknown, so a match to the Table 1 2A4802 serials (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100) cannot be ruled in or out.
- **Missing fact:** The 2nd-stage hub cycles since new are unknown. They are needed to compute the removal limit if the serial number turns out to be listed.
- **Missing fact:** No shop visits are recorded. The next engine shop visit is the triggering event, and the record should be checked for any visit since 2025-10-29 that meets the AD's definition.
- **Note:** Cycle arithmetic: the hub was at 2,000 cycles since new at engine cycle 50,000 (2025-10-29) and 2,500 at engine cycle 50,500. The 6,200 limit is reached at engine cycle 54,200.
- **Note:** Reading used: the cycle limit sets the outer date because of 'whichever occurs later'. A shop visit before 54,200 triggers removal at that visit. The text could also be read as requiring removal only at the next shop visit whenever it occurs.
- **Note:** The record lists no ad_records or amoc_claims for this AD, so none were assessed.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a V2522-A5, which is within the AD 2025-19-13 applicability, and the AD is in force on the question date. The record lists no installed components, so it cannot be determined whether an affected HPT 1st- or 2nd-stage hub is installed, and a missing record is not evidence that the parts are absent.
- **Missing fact:** No record of the installed HPT 1st-stage hub (P/N and S/N). Needed to check against table 1 to paragraph (g) and to apply the installation prohibition.
- **Missing fact:** No record of the installed HPT 2nd-stage hub (P/N and S/N). Needed to check against table 1 to paragraph (g) and to apply the installation prohibition.
- **Missing fact:** No event history (engine shop visits after October 29, 2025) is recorded. Needed to determine whether the next-shop-visit trigger has occurred. Cycles since new for any matching hub are also needed.
- **Note:** The engine is within applicability by model alone, so the installation prohibition binds regardless of the installed hubs.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule 2025-18469 and is not relied on.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model V2500-A1 is not one of the supported IAE V2500 models, so no applicability determination is made for AD 2025-19-13.
- **Note:** The engine record's model V2500-A1 is outside the supported model list, so no applicability or action determination is made.
- **Note:** The installed hub P/N and S/N appear in the AD's table 1, but because the model is out of scope, no part matching or action determination is made.
- **Note:** The AD was in force on the question date (effective 2025-10-29).

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has a 3rd stage HPC rotor blade set with P/N 6A8353, which is within the AD's applicability. The AD has been in force since 2026-09-24 and the record shows no engine shop visit, so replacement is triggered only at the next engine shop visit where a 3rd stage HPC rotor blade is exposed.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum), replace the full set of 3rd stage HPC rotor blades with parts eligible for installation. No calendar or cycle deadline applies otherwise.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** The question names 2026-16954. Its paragraph (g) omitted the word 'blade' and was corrected by 2026-18423. The correction does not change the effective date or the triggering event, so there is no difference in outcome.
- **Note:** The engine record lists no events, so no engine shop visit after the September 24, 2026 effective date is recorded. If the engine is inducted for maintenance and any 3rd stage HPC rotor blade is removed from the stage 3 to 8 drum, the replacement requirement is triggered.
- **Note:** The blade set is tracked only at set level, with no serial numbers. The AD lists part numbers only, so the match is by P/N 6A8353.
- **Note:** No ad_records or amoc_claims were supplied, and none were relied on.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The engine is a supported model (V2533-A5), but the record shows 3rd stage HPC rotor blades with P/N 6C8368, which is not an affected P/N (6A8353 or 6A8688) under paragraph (c). The AD is in force on the question date (effective 2026-09-24), so on the supplied record the engine falls outside its applicability.
- **Note:** The record gives the blade set as P/N 6C8368 with serial 'not tracked at set level'; the screen relies on that P/N. If any individual blade in the set is actually P/N 6A8353 or 6A8688 (for example a mixed set), applicability would need to be re-evaluated.
- **Note:** The record shows no events, so no shop visit or blade exposure is recorded after the effective date.
- **Note:** The correction 2026-18423 fixes a typographical error in paragraph (g) only.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC rotor blades P/N 6A8688 installed, so AD 2026-17-03 applies and is in force from 2026-09-24. The current shop visit was inducted 2026-09-14, before the effective date, so it does not trigger paragraph (g). Replacement is required only at a later engine shop visit, inducted after the effective date, where a 3rd stage HPC rotor blade is exposed.
- **Stated timing:** No deadline now. Due at the next engine shop visit (induction for maintenance) after 2026-09-24 in which a 3rd stage HPC rotor blade is exposed, that is removed from the HPC stage 3-8 drum.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record shows P/N 6A8688 installed as of the 2026-09-30 snapshot. It does not say whether the full blade set will be replaced with eligible parts before the engine leaves the current visit. Any such replacement would change the part status. A record entry showing replacement with an eligible P/N would settle this.
- **Note:** This is a screening aid and not a compliance determination.
- **Note:** The original 2026-16954 paragraph (g) omitted the word 'blade'. Correction 2026-18423 supplies it, and the analysis follows the corrected text.
- **Note:** The blade exposure on 2026-09-30 falls after the effective date, but the visit was inducted 2026-09-14, before it. Under (h)(3) and the FAA's stated intent, the shop visit is dated by induction, so this visit is not treated as the triggering visit.
- **Note:** The NPRM 2025-20088 keyed the requirement to the exposure event alone. The final rule replaced that with the shop visit construct, so the NPRM wording is not applied.
- **Note:** The shop visit induction qualification ('yes') is the operator's assertion. It matches the (h)(3) definition of induction for maintenance.
- **Note:** The record contains no AMOC or AD status entries for this AD, and none were relied on.
- **Note:** No flight-cycle or component-cycle limit applies, because the trigger is an event.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and was in force on 2026-10-05. Under paragraph (g) as corrected, the 2026-10-01 shop visit did not trigger replacement because no 3rd-stage blade was removed from the drum, so replacement is due at the next engine shop visit that exposes a blade.
- **Stated timing:** At the next engine shop visit after 2026-09-24 in which a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3-8 drum). There is no fixed deadline otherwise.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** The record does not show whether any 3rd-stage blade was removed from the stage 3-8 drum at any time during the 2026-10-01 to 2026-10-04 shop visit. The only exposure entry says none was removed. A removal at any point in the visit would trigger replacement under paragraph (g).
- **Missing fact:** Blade serials are not tracked at set level. Confirming the installed blades are P/N 6A8353 and have not been replaced or reworked to an eligible P/N (6A8353-001, 6C8368, 6C8403 or later) relies on the part number alone.
- **Note:** This is a screening aid only and not a compliance determination.
- **Note:** The correction 2026-18423 (published 2026-09-10, effective 2026-09-24) fixes the omitted word 'blade' in paragraph (g). The uncorrected text said 'where the 3rd stage HPC rotor is exposed', which could be read as triggered by the rotor being exposed for inspection on 2026-10-02. The corrected text and the definition in (h)(2) tie the trigger to blade removal, so this screen treats the shop visit as not triggering replacement.
- **Note:** If the uncorrected wording were applied, the 2026-10-01 visit would have triggered replacement, and the blades appear still to be P/N 6A8353 after the visit. No flight-cycle data was supplied, so no cycle deadline could be computed and no alternative readings are listed.
- **Note:** The operator record shows no ad_records or amoc_claims for this AD. The record asserts the visit qualifies as an engine shop visit under the AD, which is consistent with the (h)(3) definition.
- **Note:** The NPRM 2026-20088 is superseded by the final rule and is not relied on for requirements.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** Engine model V2527E-A5 is supported and has 3rd stage HPC rotor blades P/N 6A8353 installed, so it is within the proposed applicability. The document is only an NPRM on the question date, so it is not in force and cannot require action.
- **Stated timing:** If adopted as proposed, replacement of the full blade set would be due at the next 3rd stage HPC rotor blade exposure (any blade removed from the HPC stage 3 to 8 drum) after the final rule's effective date. No deadline in cycles is stated.
- **Note:** Authority state is proposed: no action is currently required. The final rule could change the text, applicability, or requirements.
- **Note:** The engine record has no events, so no blade exposure is recorded; nothing in the record shows an exposure that would trigger paragraph (g) once the rule is final and effective.
- **Note:** The blade set serial number is not tracked at set level; applicability rests on the part number match only. Whether installed blades are already modified to P/N 6A8353-001 is not shown, since the record lists P/N 6A8353 without a dash suffix.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527-A5 is within the applicability of AD 2025-17-16, which has been in force since 2025-10-10. The record says neither the TLM ALS paragraph B.1 nor the approved maintenance program yet incorporates table 1, so the paragraph (g)(1) and (g)(2) revisions are required by the due date below.
- **Stated timing:** Within 90 days after the effective date of 2025-10-10, so by 2026-01-08. This applies to the paragraph (g)(1) TLM ALS revision and, because the operator reports air carrier operations, to the paragraph (g)(2) revision of the approved maintenance or inspection program.
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Note:** The proposal 2024-26092 was superseded by the final rule. Its table referenced a nonexistent task number (72-45-11-200-009), which the final rule corrected to 72-45-31-200-009, so this screen relies on 2025-17066.
- **Note:** The deadline is calendar-based (90 days after 2025-10-10 is 2026-01-08), not a flight-cycle limit, so no flight-cycle deadline or component cycles remaining can be given.
- **Note:** The installed_components list is empty. Applicability depends only on engine model, and the required action is a manual and program revision, so no component record is needed to trigger it. The new inspections are done at piece-part exposure of P/N 2A5001 and 2A4802, so no part is matched here.
- **Note:** The record lists no AMOC claims for this AD.
- **Note:** This is a screening aid only and not a compliance determination.
- **Unresolved locator:** 2025-17066 (a) Effective date 2025-10-10

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is a listed model, and AD 2025-17-16 was in force on 2025-11-15 (effective 2025-10-10). Paragraph (g)(1) requires an ICA/TLM revision by the 90-day date for all affected engines. Paragraph (g)(2), the maintenance or inspection program revision, applies only to air carrier operations, and the record does not say whether this is one.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, which is by January 8, 2026. This applies to the (g)(1) revision, and to the (g)(2) revision if this is an air carrier operation. The deadline is calendar-based, not a flight-cycle count.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** The record shows 'unknown' for whether the engine is used in air carrier operations. This decides whether paragraph (g)(2) (revising the existing approved maintenance or inspection program) also applies.
- **Note:** Applicability is by engine model only, so the empty installed_components list does not affect applicability. The listed HPT hub part numbers appear only in the Table 1 manual-revision content, and no part matching was possible or needed.
- **Note:** The record has no ad_records or amoc_claims entry for this AD, so whether the revision has already been done is not shown.
- **Note:** The earlier NPRM 2024-26092 is superseded by the final rule. It also had an incorrect task reference, 72-45-11-200-009, which the final rule corrected to 72-45-31-200-009.
- **Note:** This is a screening result only and is not a compliance determination.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is a listed model, and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 matches Table 1 (removal limit 6,000 cycles since new). The AD is published but not effective until 2025-10-29, so nothing is required on the question date; removal and replacement is tied to the next engine shop visit after the effective date.
- **Stated timing:** Not yet in force on 2025-10-15 (effective 2025-10-29). After that date, remove and replace at the next engine shop visit after the effective date, before exceeding the 6,000-cycle removal limit or within 100 flight cycles after the effective date, whichever occurs later. No fixed deadline applies unless a shop visit occurs.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** No engine shop visit events are recorded. Whether and when a qualifying engine shop visit occurs after 2025-10-29 determines when removal is triggered; the engine flight-cycle counter on the effective date is also not supplied, so a 100-cycle deadline cannot be computed.
- **Missing fact:** The engine flight-cycle counter at the effective date is not in the record, so the 100-flight-cycle-after-effective-date point cannot be computed.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0018 (P/N 2A5001) is not listed in Table 1, so it is not matched.
- **Note:** Cycles remaining is 6,000 minus 990 cycles since new = 5,010 for the 2nd-stage hub.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule and was not relied on.
- **Note:** Because the limit is far from reached, the 100-flight-cycles-after-effective-date term is the later point once it is known; the shop-visit trigger still governs.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers the V2531-E5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is listed in table 1 with a 4,800-cycle limit. It was already at 4,950 cycles since new on the effective date, so the 100-flight-cycle alternative is the later point, ending at engine flight cycle 60,100.
- **Stated timing:** Remove and replace the HPT 1st-stage hub within 100 flight cycles after the 2025-10-29 effective date, which is by engine flight cycle 60,100. That leaves about 60 engine cycles from the 60,040 reading on 2025-11-05.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Note:** The paragraph (g) wording ties the action to the next engine shop visit, but also says 'or within 100 flight cycles from the effective date, whichever occurs later'. This screen reads the 100-cycle point (engine cycle 60,100) as the outer deadline. A reviewer should confirm that reading against the AD text and any FAA interpretation.
- **Note:** Cycles since new for the 1st-stage hub were 4,950 at 60,000 engine cycles and 4,990 at 60,040, consistent with the engine counter. The limit of 4,800 is exceeded by 190 cycles.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0019 (P/N 2A4802) is not in table 1, so it is not matched as an affected part. It is an eligible part under (i)(1).
- **Note:** The record shows no shop visit events and no AD records or AMOC claims. None are relied on.
- **Note:** This is a screening aid only and does not determine compliance, airworthiness, or return to service.

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2533-A5 is a supported model with HPT disks of the listed part numbers (2A5001 and 2A4802) installed. Applicability cannot be decided because the Appendix A serial-number tables in the service bulletins were not supplied, so the disk serial numbers cannot be checked against them.
- **Stated timing:** If either disk serial number is listed, paragraphs (g)(1) and (g)(2) require an ultrasonic inspection at the next engine shop visit after July 13, 2021, or before that disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first. The record shows no events, and the flight-cycle count at the effective date is not given, so no deadline can be computed.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not supplied, so it is unknown whether HPT 1st-stage disk P/N 2A5001 S/N SYN-DISK1-0020 is listed. Applicability under (c)(1) depends on it.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not supplied, so it is unknown whether HPT 2nd-stage disk P/N 2A4802 S/N SYN-DISK2-0020 is listed. Applicability under (c)(2) depends on it.
- **Missing fact:** The engine flight-cycle counter at the AD effective date (2021-07-13) is not in the record. It is needed to compute the 3,200-cycle limit under (g)(1) and (g)(2) and the cycles remaining.
- **Missing fact:** The current engine flight-cycle counter is not in the record. It is needed to measure cycles accumulated since the effective date.
- **Missing fact:** The events list is empty. It is not confirmed whether any engine shop visit (as defined in (h)(1)) has occurred since July 13, 2021, which would have triggered the inspection earlier. An empty list is not evidence that none occurred.
- **Missing fact:** No operator AD record or USI accomplishment record for AD 2021-11-15 is supplied, so it is not known whether the inspection was already done ("unless already done", (f)).
- **Note:** On 2022-03-01, AD 2021-11-15 (document 2021-11960) is in force. The superseding AD 2022-02-09 (document 2022-02574) was published 2022-02-08 but is not effective until 2022-03-15, after which AD 2021-11-15 is removed.
- **Note:** The superseding AD replaces the shop-visit/3,200-FC compliance times with Figure 1 times or 10 FCs after March 15, 2022, whichever is later. Figure 1 was not included in the text supplied, so those deadlines could not be evaluated.
- **Note:** Part numbers 2A5001 and 2A4802 match the part numbers the directive lists, but a match requires a listed serial number, which is unconfirmed. No parts are reported as matched.
- **Note:** The V2533-A5 is a high-thrust model, so (g)(1) and (g)(2) are the applicable paragraphs. The (g)(5) and (g)(6) paragraphs for the V2531-E5 are not relevant.
- **Note:** This is a screening aid only and is not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The engine is a supported V2533-A5 with disks of the listed part numbers (P/N 2A5001 and 2A4802). Whether it is within AD 2022-02-09 depends on whether the disk serial numbers appear in the NMSB Appendix A tables, which were not supplied. On 2022-03-01 this AD is published but not effective until 2022-03-15, so it cannot yet require action.
- **Missing fact:** Contents of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1, to check whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed. Applicability turns on this.
- **Missing fact:** Contents of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, to check whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed. Applicability turns on this.
- **Missing fact:** Figure 1 to paragraph (g)(1), the compliance-time table for V2533-A5, was an image not included in the text. Without it the inspection threshold cannot be computed if the engine is affected.
- **Missing fact:** Accumulated flight cycles on the HPT 1st-stage disk. Needed to apply the Figure 1 threshold if the disk is listed.
- **Missing fact:** Accumulated flight cycles on the HPT 2nd-stage disk. Needed to apply the Figure 1 threshold if the disk is listed.
- **Note:** Applicability cannot be decided: the NMSB Appendix A serial-number lists were not supplied. No part is treated as matched, and the absence of data is not evidence that the engine is unaffected.
- **Note:** If the disks are listed, the V2533-A5 deadline would come from Figure 1 (image not provided) or 10 FCs after 2022-03-15, whichever is later.
- **Note:** The record has no flight-cycle counters or events, and no ad_records or amoc_claims entries.
- **Note:** The predecessor AD 2021-11-15 remains in force until 2022-03-15 and is not the directive under question. This screen is not a compliance determination.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2530-A5 is a supported model and AD 2022-02-09 is in force, and both installed disk part numbers (2A5001 and 2A4802) are ones the AD lists. Applicability turns on whether the disk serial numbers appear in Appendix A Tables 1 and 2 of the incorporated service bulletins, which were not supplied. The Figure 1 compliance table, an image, was also not supplied, so no deadline can be computed.
- **Stated timing:** If either disk serial number is listed, paragraphs (g)(1)/(g)(2) require a USI within the Figure 1 compliance time or within 10 flight cycles after March 15, 2022, whichever is later. Figure 1 was not provided, so the deadline cannot be stated.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (listed HPT 1st-stage disk P/N 2A5001 serial numbers) was not supplied. Without it, it cannot be determined whether SYN-DISK1-0021 is listed, which decides applicability.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (listed HPT 2nd-stage disk P/N 2A4802 serial numbers) was not supplied. Without it, it cannot be determined whether SYN-DISK2-0021 is listed, which decides applicability.
- **Missing fact:** Figure 1 to paragraph (g)(1) (the compliance-time table) is an image that was not included. It is needed to compute the USI deadline if either disk is listed.
- **Missing fact:** The record gives no flight-cycle counters or accumulated cycles for the HPT 1st-stage disk or the engine. These are needed to apply the Figure 1 threshold and compute a cycle deadline.
- **Missing fact:** The record gives no flight-cycle counters or accumulated cycles for the HPT 2nd-stage disk. These are needed to apply the Figure 1 threshold and compute a cycle deadline.
- **Missing fact:** The record has no entry showing whether the USI was already done under this AD or under predecessor AD 2021-11-15, so prior accomplishment cannot be assessed.
- **Note:** Both installed part numbers match the P/Ns the AD lists, but the serial numbers were not matched to any listed serial number, so no parts are recorded as matched.
- **Note:** The engine record has no ad_records, amoc_claims or events, so nothing was credited as prior accomplishment.
- **Note:** Because the V2530-A5 is a high-thrust model, the paragraph (g)(1)/(g)(2) Figure 1 time applies to it directly. Figure 1 is an image not included in the text.
- **Note:** This is a screening result only and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2021-11960 (b) Affected ADs / superseding history

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine has an HPT 1st-stage disk, P/N 2A5001, S/N PKLBSH1829, which is listed in paragraph (c)(1), so the AD applies. A USI of that disk is required within 10 flight cycles after the July 19, 2021 effective date, which is by engine cycle 33010.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021. The engine was at 33000 cycles on that date, so the USI is due by 33010 engine flight cycles. At 33004 on 2021-07-20, 6 cycles remain.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** Tables 1 and 2 to paragraphs (g)(1) and (g)(2) are images not included in the supplied text. Confirm that the 1st-stage disk S/N PKLBSH1829 appears in Table 1, since paragraph (g)(1) is tied to that table.
- **Missing fact:** No record shows whether the USI under 2021-11-51 (or the emergency AD issued May 21, 2021) was already done. Paragraph (f) says 'unless already done', so a prior USI would affect the due date.
- **Note:** The deadline is computed from the engine cycle reading of 33000 recorded on the effective date, 2021-07-19, plus 10 cycles.
- **Note:** The 2nd-stage disk S/N SYN-DISK2-0022 is not listed in paragraph (c)(2), so it is not matched. Applicability rests on the 1st-stage disk alone.
- **Note:** The record has no ad_records or amoc_claims entries and no events, so nothing was asserted about prior accomplishment or AMOCs.
- **Note:** This is a screening aid only and not a compliance determination.
- **Expected missing fact (judge on meaning):** operator date of actual notice of Emergency AD 2021-11-51
- **Expected missing fact (judge on meaning):** table 1 to paragraph (g)(1) content (image-only; transcription decided in E3)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 accomplishment instructions (unavailable incorporated material)
- **Unresolved locator:** 2021-14268 (g)(1) Table 1 to paragraph (g)(1) (image not supplied)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-022/2021-11960: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2533-A5 is a listed model and the AD was in force on 2021-07-20. Both installed disks have the listed part numbers (2A5001 and 2A4802), but the Appendix A serial-number tables of the incorporated service bulletin were not supplied, so applicability cannot be confirmed. If a disk serial is listed, (g)(1) or (g)(2) would require a USI at the next engine shop visit or within 3,200 disk flight cycles after 2021-07-13, whichever occurs first.
- **Stated timing:** If a serial number is listed: at the next engine shop visit after 2021-07-13, or before the disk has accumulated 3,200 flight cycles since 2021-07-13, whichever occurs first. No deadline can be computed from the record, and no shop visit is recorded.
- **Missing fact:** Contents of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1, to check whether HPT 1st-stage disk P/N 2A5001 S/N PKLBSH1829 is listed. Without it, applicability cannot be decided.
- **Missing fact:** Contents of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, to check whether HPT 2nd-stage disk P/N 2A4802 S/N SYN-DISK2-0022 is listed.
- **Missing fact:** Engine flight-cycle reading on the effective date (2021-07-13). The record only has readings for 2021-07-19 and 2021-07-20, so the 3,200-cycle limit cannot be converted to an engine cycle count.
- **Missing fact:** Disk cycle accounting is not in the record. The 3,200-cycle limit counts the disk's own cycles since the effective date, which may differ from the engine's cycles.
- **Note:** The part numbers match the AD, but serial-number listing is unverified. A missing or unknown listing is not evidence that the disk is unaffected.
- **Note:** Disk S/N SYN-DISK2-0022 is a synthetic identifier and cannot be checked against the real tables.
- **Note:** The record shows no events, so no engine shop visit since 2021-07-13 is recorded. Whether one occurred is not confirmed beyond the empty events list.
- **Note:** This is a screening aid only and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers the V2527M-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 with a 6,000 cycles-since-new removal limit. Removal and replacement is required at the next engine shop visit, before the hub exceeds that limit. At 3,500 cycles since new, the hub has 2,500 cycles remaining.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before the hub exceeds 6,000 cycles since new. The 100-flight-cycle floor from the effective date (engine cycle 20,100) has already passed, so the later date is the 6,000-cycle limit, reached at about engine flight cycle 25,000.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The record shows no engine shop visit after 2025-10-29 and no per-AD shop-visit qualification. Whether a shop visit has occurred, or is planned, determines whether the hub must be removed before the limit is reached.
- **Missing fact:** There is no dated cycles-since-new reading for the hub at the question date. The 3,500 figure is undated but agrees with 1,000 at 2025-10-29 plus 2,500 engine cycles flown since.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0023 is not listed in table 1, so it is not matched. The 3rd stage HPC rotor blade set is not a part this AD lists.
- **Note:** The record's maintenance program revision cites AD 2025-17-16, a different AD. It does not address AD 2025-19-13, and the record has no ad_records or amoc_claims entry for this AD.
- **Note:** Paragraph (g) can be read as requiring removal only at a shop visit, with the limit and 100-cycle floor setting the latest date. The record does not show whether removal is also required at the limit if no shop visit occurs by then. The 25,000 figure is the engine cycle count at which the hub reaches 6,000 cycles since new.
- **Note:** The NPRM 2025-10764 was adopted as proposed. This screen relies on the final rule.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 was in force on 2026-10-06 (effective 2026-09-24). The V2527M-A5 engine has a 3rd stage HPC rotor blade set P/N 6A8688, so it is within applicability. Replacement of the full blade set is required at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed. The record shows no such visit, so no deadline is running now.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum). There is no calendar or cycle deadline otherwise.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Note:** The record lists no engine shop visit or blade exposure event on or after 2026-09-24, so no replacement is triggered by the supplied facts. If the engine was inducted before 2026-09-24, the AD does not require action for that visit.
- **Note:** The record events list only a maintenance program revision (AD 2025-17-16 table 1). It is unrelated to this AD and does not show any action under AD 2026-17-03.
- **Note:** The HPT 1st-stage and 2nd-stage hub records belong to a different directive and do not bear on this AD.
- **Note:** The blade set has no serial number tracked at set level. The AD lists part numbers only, so the match is on P/N 6A8688.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527M-A5 is a listed model, and AD 2025-17-16 has been in force since 2025-10-10. The operator's record shows the TLM ALS and maintenance program revisions were made on 2025-12-01, inside the 90-day window that ended 2026-01-08, so no further required action is triggered on this record. Continuing obligations still bind.
- **Stated timing:** The paragraph (g)(1) and (g)(2) revisions were due within 90 days after the 2025-10-10 effective date, that is by 2026-01-08. The record shows them made on 2025-12-01. No other deadline is stated.
- **Note:** The record's revision event (2025-12-01) is the operator's own assertion. It says the V2500-A5 TLM ALS was revised to incorporate table 1. The record does not show that paragraph B.1 of the Maintenance Scheduling section was revised or that the TLM was the one listed in (g)(1)(i). Confirm the revision content and TLM identity against the actual documents.
- **Note:** The AD does not state a cycle limit for the hubs, so no component cycles remaining are computed. Both hubs show 3,500 cycles since new, and the 2nd-stage hub's readings are consistent with the engine counter (1,000 at 20,000 engine cycles; 3,500 at 22,500).
- **Note:** The 3rd stage HPC rotor blade set (6A8688) is not listed in this AD and was not matched.
- **Note:** This is a screening aid, not a compliance determination. The inspection tasks themselves are triggered at piece-part exposure under other regulations, not by this AD's required action. The superseded NPRM 2024-26092 was not relied on.
- **Unresolved locator:** 2025-17066 (a) Effective date 2025-10-10
- **Unresolved locator:** 2025-17066 preamble Comment responses

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is within the AD's model applicability, and the AD was in force on the question date. Neither installed hub matches a P/N and S/N pair in table 1 to paragraph (g), so the removal requirement is not triggered. The installation prohibition still binds.
- **Note:** The 2nd-stage hub S/N PKLBST5011 matches a table 1 serial number, but that entry is for P/N 2A5001 (HPT 1st-stage hub). The installed part is P/N 2A4802, and P/N 2A4802 pairs with different serial numbers in the table. Because the AD keys on the P/N and S/N pair, there is no match. A reviewer may want to confirm the part number and serial number against the part's data plate or records, since a transcription error would change this result.
- **Note:** If the record is accurate, the required action is not triggered now. The record shows no events or shop visits, and no AMOC claims or AD records were supplied.
- **Note:** This is a screening result only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model in the record, CFM56-5B4/3, is not one of the supported IAE V2500 models, so no applicability determination is made for AD 2025-17-16.
- **Note:** This screen supports only the listed IAE V2500 engine models; the record's engine model is CFM56-5B4/3.
- **Note:** No applicability determination is made. This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (in force since 2025-10-29) covers the V2530-A5. Installed HPT 1st-stage hub 2A5001 S/N PKLBST7489 is listed in table 1 with a 6,200 cycles-since-new removal limit, so removal and replacement is required. On the later-of reading, the latest engine flight-cycle counter is 23,200.
- **Stated timing:** Remove and replace hub PKLBST7489 at the next engine shop visit after 2025-10-29, no later than the later of 100 flight cycles after the effective date (engine counter 20,100) and the hub reaching 6,200 cycles since new (engine counter 23,200). The later of the two is 23,200.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** The record lists no engine shop visit after 2025-10-29. The repair (2024-06-10) and inspection (2024-06-12) of the hub predate the effective date and do not qualify. Confirm that no qualifying shop visit has occurred since the effective date, because removal is tied to the next shop visit.
- **Note:** Cycle arithmetic: the hub had 3,000 cycles since new at the effective date, when the engine counter was 20,000. It reaches 6,200 at engine counter 20,000 + 3,200 = 23,200. At the current 3,600 cycles since new, 2,600 cycles remain. The record's 600-cycle engine increase matches the hub's 600-cycle increase.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0026 (P/N 2A4802) is not listed in table 1, so it is not matched.
- **Note:** The 2024 blend repair and repeat ultrasonic inspection do not change the hub's P/N or S/N listing, so the table 1 match stands.
- **Note:** The NPRM 2025-10764 was adopted as the final rule 2025-18469 without substantive change; the final rule was relied on.
- **Note:** This is a screening result only and does not state any compliance or airworthiness status.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this hub because it was repaired.
- The re-inspection satisfies AD 2025-19-13.
- No removal is required.
- The engine is compliant with AD 2025-19-13.
- The 2024 repair or inspection was the engine shop visit that triggered removal under paragraph (g).
- The repair resets or extends the 6,200 CSN removal limit.

## seed-027: Listed hub near its limit, with an unverified AMOC claimed to extend it

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers the V2527-A5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is listed in Table 1 with a 4,800 CSN removal limit, and it is at 4,750 CSN. Removal and replacement is therefore required at the next engine shop visit, no later than the point where the hub would exceed 4,800 CSN (engine flight cycle 15,300), which is 50 cycles away.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29, before the hub exceeds 4,800 CSN. Reading 'whichever occurs later' literally, the later of the 4,800 CSN limit (engine FC 15,300) and 100 FC after the effective date (engine FC 15,100) governs, so the deadline is engine FC 15,300, 50 cycles from the 2026-01-20 reading.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The planning note that an AMOC extends the hub limit to 5,300 CSN has no FAA approval reference or letter. An unverified AMOC claim is not credited, so the 4,800 CSN limit is used. An approval letter would be needed to rely on any extension.
- **Missing fact:** No engine shop visit is recorded. The timing of the next shop visit relative to engine FC 15,300 is unknown, and whether any future visit meets the paragraph (i)(2) engine shop visit definition must be confirmed.
- **Note:** Hub CSN was 4,500 at 2025-10-29 (engine FC 15,000) and is 4,750 at 2026-01-20 (engine FC 15,250); the 250-cycle hub increase matches the engine increase. It reaches 4,800 CSN at engine FC 15,300.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0027 (P/N 2A4802) is not listed in Table 1, so it is not matched.
- **Note:** The NPRM 2025-10764 is superseded by the final rule; the final rule text was used.
- **Note:** This is a screening result only and not a compliance determination.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers all V2524-A5 engines. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 is listed in table 1, so removal and replacement is triggered at the next engine shop visit. The record shows no shop visit since the effective date.
- **Stated timing:** At the next engine shop visit after 2025-10-29, no later than the later of (a) the 4,000 cycles-since-new removal limit or (b) 100 flight cycles after the effective date. On the record's figures, the cycles-since-new limit is the later bound and falls at engine flight cycle 11,000.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Note:** The operator's AD record marks AD 2025-19-13 as not applicable because no affected hubs are installed. That claim conflicts with the installed 2nd-stage hub PKLBST5005, which is listed in table 1, and the AD applies to all engines of this model regardless of installed parts. This is a claim to be checked, not evidence.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0028 is not listed in table 1 and is not matched.
- **Note:** Cycle arithmetic: the 2nd-stage hub had 1000 cycles since new at 2025-10-29 (engine cycle 8000) and has 1400 now (engine cycle 8400), leaving 2600 cycles before 4,000. The 4,000-cycle limit is therefore reached at engine cycle 11,000, and 2600 cycles remain.
- **Note:** The record lists no events, so no shop visit has occurred since the effective date and none has triggered the removal. Any future shop visit must be checked against the paragraph (i)(2) definition.
- **Note:** The NPRM 2025-10-764 (published 2025-06-13) is the proposed version. The final rule 2025-18469 governs, and its text is the same.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 row: HPT 2nd-stage hub 2A4802 PKLBST5005, 4,000

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is within the applicability of AD 2025-19-13, which has been in force since 2025-10-29. The 1st-stage hub S/N PKLBSK9287 matches a listed serial number but is recorded as P/N 2A5001-01 rather than the listed 2A5001, so whether it is an affected part needs review. The 2nd-stage hub S/N is not listed.
- **Stated timing:** If the 1st-stage hub is confirmed as the listed part: at the next engine shop visit after 2025-10-29, no earlier than the later of the 100-cycle removal limit or 100 flight cycles after the effective date. The hub's 2,400 cycles since new already exceed the 100-cycle limit, so the 100-flight-cycle-from-effective-date term would govern. No shop visit is recorded, and the engine flight-cycle count at the effective date is not in the record.
- **Missing fact:** Installed P/N is 2A5001-01 but the table lists P/N 2A5001 for S/N PKLBSK9287. Paragraph (g) is triggered by a P/N and S/N match, so it must be confirmed whether the -01 dash number is the listed part. If it is, the hub is 2,300 cycles past its 100-cycle limit.
- **Missing fact:** The engine flight-cycle counter on 2025-10-29 (the effective date) is not in the record. Without it, the 100-flight-cycles-after-effective-date term cannot be converted to a counter value.
- **Missing fact:** Whether the 'whichever occurs later' wording sets the due point at the next shop visit or independently at 100 flight cycles after the effective date is not clear from the text. Whether an engine shop visit has occurred since 2025-10-29 is also not confirmed, since the events list is empty.
- **Note:** This is a screening aid and not a compliance determination.
- **Note:** The -2300 component_cycles_remaining figure (100 minus 2,400 cycles since new) is conditional on the 2A5001-01 hub being treated as the listed 2A5001 part.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0029) is not matched to any listed S/N.
- **Note:** The events list is empty, so no engine shop visit is recorded that would trigger the replacement.
- **Note:** The record has no AD status or AMOC claims for this AD.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 2nd-stage hub rows

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
