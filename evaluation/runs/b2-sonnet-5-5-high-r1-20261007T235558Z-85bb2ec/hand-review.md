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
- **Summary:** The V2527-A5 is within the applicability of AD 2025-19-13, which was in force on 2026-09-26. Its HPT 1st-stage hub P/N 2A5001, S/N PKLBST5011 is listed in table 1 with a 5,500 cycles-since-new removal limit, so removal and replacement is required at the next engine shop visit and before the hub exceeds that limit. The 2nd-stage hub S/N is not listed.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after 2025-10-29, before the hub exceeds 5,500 cycles since new. That is the later of the 5,500-cycle limit and 100 flight cycles after the effective date, and the limit is the later one. The hub has 2,400 cycles remaining, which corresponds to engine flight cycle 45,050.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Note:** Cycles since new for the 1st-stage hub are consistent across the record: 1,650 at 2025-10-29 plus 1,450 engine cycles gives 3,100 at 2026-09-26. The 5,500-cycle limit is reached at engine flight cycle 45,050.
- **Note:** 100 flight cycles after the effective date is engine cycle 41,300, which is earlier than the limit date, so the limit is the later of the two.
- **Note:** The record lists no events, so no shop visit after 2025-10-29 is recorded.
- **Note:** The text ties removal to the next shop visit and to the cycle limit. I read the 5,500-cycle limit as the outer bound by which the shop visit and removal must occur. A reviewer should confirm that reading.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0001 matches P/N 2A4802 but its S/N is not listed in table 1, so it is not matched to the AD.
- **Note:** The record has no ad_records or amoc_claims for this AD; none were considered.

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 is a listed model, so AD 2025-19-13 applies and is in force. Neither installed hub's P/N and S/N appears in table 1 (the 1st-stage S/N PKLBST5012 is not the listed PKLBST5011), so paragraph (g) is not triggered; the installation prohibition and other obligations continue.
- **Note:** The 1st-stage hub S/N PKLBST5012 differs by one digit from listed S/N PKLBST5011; the reviewer may want to verify the serial number against the physical part and the records, since a transcription error would change the outcome.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0002 is not in table 1.
- **Note:** The engine record contains no events and no AD or AMOC claims.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 is a listed model, and AD 2025-19-13 has been in force since 2025-10-29, so it applies. Whether paragraph (g) is triggered cannot be decided because the HPT 1st-stage hub serial number is unknown. The 2A5001 part number is listed in Table 1, but only for specific serial numbers. The HPT 2nd-stage hub serial number is not listed.
- **Missing fact:** The HPT 1st-stage hub serial number is unknown. Part number 2A5001 appears in Table 1 for four serial numbers (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489), so it cannot be determined whether this hub is an affected part.
- **Missing fact:** The hub's cycles since new are unknown. If the hub is a listed serial number, they are needed to compare against the removal cycle limit (100 to 6,200 cycles depending on serial number) and to work out the paragraph (g) timing.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) does not match any Table 1 serial number, so paragraph (g) does not reach it on the supplied facts. At 5,100 cycles since new it is also not near any listed limit, but it is not a listed part.
- **Note:** An unknown serial number is not evidence that the 1st-stage hub is unaffected. If the serial number turns out to be listed, paragraph (g) requires removal at the next engine shop visit after the effective date, before exceeding the removal cycle limit or within 100 flight cycles of the effective date, whichever occurs later. Removal is then due at the next engine shop visit, and no later date can be computed from the record. A limit already exceeded would not by itself set a separate deadline.
- **Note:** The engine record lists no events, so no engine shop visit since 2025-10-29 is recorded.
- **Note:** The final rule 2025-18469 adopts the NPRM 2025-10764 as proposed, with only minor editorial changes. The final rule controls here.
- **Note:** The record contains no ad_records or amoc_claims for this AD.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for this directive.
- **Note:** No determination is made on whether the directive applies to this engine.
- **Note:** The engine record has no installed components or events; these were not evaluated because the model is outside the supported scope.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 was in force on 2025-11-12 and covers the V2527E-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed in Table 1, so removal and replacement is required. The reading that gives the later deadline is 100 flight cycles after the effective date, which is engine flight cycle 18100.
- **Stated timing:** Remove the HPT 2nd-stage hub from service and replace it with an eligible part at the next engine shop visit after 2025-10-29, or within 100 flight cycles after the effective date, whichever occurs later. The 100-cycle point is engine flight cycle 18100. The recorded shop visit was inducted at 18040, so the hub is exposed now and the 18100 point is only 60 cycles beyond the latest reading.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0005 (P/N 2A5001) is not listed in Table 1, so it is not matched.
- **Note:** The 2nd-stage hub has 1040 cycles since new against the 3,900 limit, leaving 2860 cycles. The record shows 1000 cycles at 2025-10-29, consistent with 40 cycles flown since then.
- **Note:** The shop visit qualification is asserted by the operator record. The described flange separation for maintenance does not appear to fall within the (i)(2) exclusions, but the record does not rule out transport-only or field-maintenance purposes.
- **Note:** No AMOC claims or AD records were supplied, and none are relied on.
- **Note:** This is a screening result, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The AD is in force (effective 2025-10-29) and covers the V2530-A5. The installed HPT 1st-stage hub P/N 2A5001, S/N PKLBSK9287 is listed in table 1 with a 100 cycles-since-new removal limit. Read as the later of the removal limit and 100 flight cycles after the effective date, removal and replacement is due by engine flight cycle 25600.
- **Stated timing:** By the later of (a) the hub reaching its 100 cycles-since-new limit (engine cycle about 25540) and (b) 100 flight cycles after the 2025-10-29 effective date (engine cycle 25600). The later is 25600, about 70 engine cycles after the 25530 reading on 2025-11-20. The record shows no engine shop visit yet.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Note:** Engine cycles at the effective date were 25500, so 100 FC after it is 25600. The hub had 60 CSN on 2025-10-29 and 90 CSN on 2025-11-20, consistent with the 30 engine cycles flown in that period.
- **Note:** Paragraph (g) is ambiguous about whether removal is required at the deadline if no shop visit has occurred, or only at the next engine shop visit. A reviewer should confirm the reading; this screen treats 25600 as the latest cycle count for removal.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0006 is not listed in table 1, so it is not matched. Its non-listing is taken from the record serial number.
- **Note:** This is a screening aid only, not a compliance determination.
- **Unresolved locator:** 2025-18469 (a) Effective date 2025-10-29

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine is within the applicability of AD 2025-19-13, which was in force on 2025-12-01. It has two installed hubs whose P/N and S/N appear in table 1. The HPT 1st-stage hub PKLBSS9200 has the least margin to its 4,800-cycle removal limit, so its removal and replacement is due by engine flight cycle 30800.
- **Stated timing:** Under (g), the later of the 100-flight-cycle window and the removal cycle limit controls. The 100 flight cycles from the effective date ended at engine cycle 30100 and have passed. The 1st-stage hub reaches its 4,800 cycles-since-new limit at engine cycle 30800, which is 500 cycles after the 30300 reading on 2025-12-01. The 2nd-stage hub does not reach its limit until engine cycle 32000. The record shows no engine shop visit since the effective date, so the replacement is due by the 30800 cycle count.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** The events list is empty, so no engine shop visit since 2025-10-29 is recorded. Whether one has occurred, and whether either hub was already replaced, would change the status. An unknown record is not evidence that no shop visit occurred.
- **Note:** Calculation, 1st-stage hub: 4,000 cycles since new at the effective date, so 800 cycles remained then. The engine was at 30000 cycles at that date, which gives a limit-based deadline of 30800. At 30300 cycles the hub is at 4,300 cycles since new, leaving 500.
- **Note:** Calculation, 2nd-stage hub: 2,000 cycles since new at the effective date, so 2,000 cycles remained. The deadline is engine cycle 32000, and 1,700 cycles remain at 30300.
- **Note:** Paragraph (g) is worded as 'at the next engine shop visit ... before exceeding the limit or within 100 flight cycles ..., whichever occurs later'. I read it as setting the removal deadline at the later of the two cycle bounds. A reviewer should confirm that reading.
- **Note:** No AMOC or AD-record claims were supplied, and none would settle the outcome without verification.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows PKLBSS9200 (4,800) and PKLBST5005 (4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers the V2528-D5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1, so removal and replacement are required at the next engine shop visit after the effective date. No shop visit is recorded since the effective date. The HPT 2nd-stage hub cannot be matched because its serial number is unknown.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after 2025-10-29, no later than the later of reaching its 6,200 cycles-since-new limit or 100 flight cycles after the effective date. The limit is the later date, at about engine flight cycle 54,200. No deadline is computed for the HPT 2nd-stage hub until its serial number is known.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub serial number is unknown. It cannot be checked against the four listed 2A4802 serial numbers in table 1, so it cannot be cleared. A missing record is not evidence that the part is unaffected.
- **Missing fact:** The 2nd-stage hub cycles since new are unknown. If its serial number is listed, they are needed to compute the removal limit and the remaining cycles.
- **Missing fact:** No engine shop visit is recorded. The record should be checked for any shop visit after 2025-10-29 that met the AD's definition, because that would have triggered removal of the 1st-stage hub.
- **Note:** The 1st-stage hub had 2,000 cycles since new at the effective date and has 2,500 now. The limit is 6,200, so 3,700 cycles remain. Engine flight cycles are 50,500 now, so the limit is reached at about 54,200 (50,500 + 3,700).
- **Note:** The 100-flight-cycle point after the effective date is engine flight cycle 50,100. The AD says the later of that point and the limit applies, so the limit controls.
- **Note:** The record's events list is empty, so no shop visit has been recorded since the effective date.
- **Note:** The 3,700 figure is the smallest remaining cycles among the parts that could be computed. The 2nd-stage hub could have a smaller figure if its serial number is listed.
- **Note:** No AMOC or AD record claim was supplied, so none was assessed.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2522-A5 is within the AD's applicability and the AD is in force on the question date. The record lists no installed components, so whether an affected HPT hub is installed cannot be determined and no action can be established or cleared.
- **Missing fact:** No installed-component record for the HPT 1st-stage hub (P/N and S/N). Needed to determine whether it matches a part in table 1 to paragraph (g). An empty record is not evidence the part is absent or unaffected.
- **Missing fact:** No installed-component record for the HPT 2nd-stage hub (P/N and S/N). Needed to determine whether it matches a part in table 1 to paragraph (g).
- **Missing fact:** No engine shop visit history is recorded. Needed to identify the next engine shop visit after October 29, 2025, which sets the paragraph (g) timing if an affected hub is installed.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule 2025-18469, which was adopted as proposed apart from minor editorial changes.
- **Note:** The record has no ad_records or amoc_claims entries for this AD.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made.
- **Note:** The installed part number and serial number appear in table 1 to paragraph (g), but because the engine model is outside the supported scope, no match or applicability determination is made.
- **Note:** The AD (effective 2025-10-29) was in force on the question date of 2026-09-26.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has 3rd stage HPC rotor blades with P/N 6A8353 installed, so AD 2026-17-03 (in force since 2026-09-24) applies. Replacement of the full blade set is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; the record shows no such event so far.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum). No calendar or cycle deadline applies otherwise.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** Paragraph (g) of 2026-16954 as originally published omitted the word 'blade'. The correction 2026-18423 restores it and does not change the effective date or the substantive trigger, so the readings give the same outcome.
- **Note:** The engine record lists no events, so no shop visit or blade exposure after 2026-09-24 is recorded. Re-screen when the engine is next inducted into a shop.
- **Note:** Blade serial numbers are not tracked at set level. The applicability trigger is the installed P/N 6A8353, and the record gives no modified (-001) or replacement P/N for any blade.
- **Note:** The record contains no ad_records or amoc_claims for this AD. Any such claim would need to be checked against the AD text.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The V2533-A5 is a supported model, but the record shows 3rd stage HPC rotor blade set P/N 6C8368, which is not P/N 6A8353 or 6A8688, so the engine is outside the applicability of AD 2026-17-03 on this record. The AD was in force on the question date (effective 2026-09-24).
- **Note:** Result rests on the record's single component entry for the blade set (P/N 6C8368, serial not tracked at set level). If any individual blade of P/N 6A8353 or 6A8688 is mixed into the installed set, applicability would need to be revisited.
- **Note:** The engine record has no events, so no shop visit or blade removal is recorded.
- **Note:** Document 2026-18423 corrected paragraph (g) to read 'the 3rd stage HPC rotor blade is exposed' and left the effective date unchanged; the correction does not affect this screening outcome.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC blade set P/N 6A8688 installed, so AD 2026-17-03 applies and has been in force since 2026-09-24. The current visit was inducted 2026-09-14, before the effective date, so the blade exposure on 2026-09-30 does not by itself trigger paragraph (g). Replacement is required at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed.
- **Stated timing:** No deadline now. Replacement of the full blade set with eligible parts is due at the next engine shop visit inducted after 2026-09-24 in which a 3rd stage HPC rotor blade is exposed, meaning removed from the stage 3-8 drum.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** The induction date of 2026-09-14 and the shop-visit qualification come from the operator's record and are assertions. If induction was actually on or after 2026-09-24, paragraph (g) would be triggered by the 2026-09-30 exposure.
- **Note:** The record does not show whether the blade set was replaced during this visit. It still lists P/N 6A8688, so any later shop visit with blade exposure would trigger replacement.
- **Note:** No flight-cycle counters are in the record, so no cycle-based deadline is computed.
- **Note:** The correction document 2026-18423 restores 'blade' in paragraph (g) and does not change the outcome.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a V2524-A5 with 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force (effective 2026-09-24). The 2026-10-01 shop visit did not expose a blade because none was removed from the stage 3-8 drum, so replacement is required only at the next engine shop visit where a 3rd stage blade is exposed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed (removed from the stage 3 to 8 drum). No deadline applies until that event occurs.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Note:** This is a screening result, not a compliance determination.
- **Note:** The correction document 2026-18423 (published 2026-09-10, effective 2026-09-24) replaces the original paragraph (g) wording. The original text said 'rotor is exposed'. The corrected text says 'rotor blade is exposed', which fits the (h)(2) definition of blade exposure.
- **Note:** The 2026-10-01 to 2026-10-04 shop visit began after the effective date. Per the record, the HPC rotor was exposed for inspection but no 3rd stage blade was removed. This screen therefore treats that visit as not triggering replacement. If a blade was in fact removed from the drum during that visit, the result would change, and replacement would have been due at that visit.
- **Note:** The record does not give an engine flight-cycle counter, and the trigger is an event, so no cycle deadline is computed.
- **Note:** The blade set is tracked by part number only, with no serial number. This does not affect matching because the AD lists part numbers only.
- **Note:** The record does not show that blades were removed during the visit, and the operator's own record is the only source for that fact.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** Document 2025-20088 is only a proposed rule on the question date, so it cannot require action. The engine is a supported model with a 3rd stage HPC rotor blade set P/N 6A8353, which is within the proposed applicability.
- **Note:** The proposal is not final, so no action can be triggered. The final rule could change the requirements, applicability, or compliance times.
- **Note:** If a final rule is adopted as proposed, replacement would be due at the next 3rd stage HPC rotor blade exposure after its effective date. The record lists no events, so no past exposure is recorded.
- **Note:** This is a screening result only, not a compliance determination.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 applies by model to the V2527-A5 engine and has been in force since 2025-10-10. The operator's record shows the paragraph (g) revisions are not yet incorporated, so the TLM ALS revision and, for air carrier operations, the maintenance program revision are required within 90 days after the effective date.
- **Stated timing:** Within 90 days after the effective date of 2025-10-10, that is, by 2026-01-08, for both the paragraph (g)(1) TLM ALS revision and the paragraph (g)(2) air carrier maintenance or inspection program revision.
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Note:** The 90-day deadline is calendar-based, so no engine flight-cycle limit applies. The engine record has no installed components or events, and none are needed because the AD requires only a documentation revision.
- **Note:** The operator's record says maintenance program Revision 47 (2025-06-01) and TLM ALS paragraph B.1 do not yet incorporate table 1. This is an operator statement, not verified evidence.
- **Note:** The operator record says air_carrier_operation is yes, so paragraph (g)(2) applies in addition to (g)(1).
- **Note:** The earlier NPRM 2024-26092 is a proposal. The final rule 2025-17066 governs, and its table 1 references TASK 72-45-31-200-009 for the HPT Stage 2 Hub instead of the NPRM's 72-45-11-200-009.
- **Note:** This is a screening aid only and is not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 was effective 2025-10-10 and applies by model to the V2522-A5. Paragraph (g)(1) calls for a TLM ALS revision within 90 days after the effective date, which falls on 2026-01-08. Whether paragraph (g)(2) also applies depends on the unknown air carrier operation status.
- **Stated timing:** Paragraph (g)(1): within 90 days after October 10, 2025, i.e. by January 8, 2026. Paragraph (g)(2), if the engine is in air carrier operations: the same 90-day period, to revise the existing approved maintenance or inspection program.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the engine is operated in air carrier operations is unknown. This decides whether the paragraph (g)(2) revision of the approved maintenance or inspection program also applies, in addition to the paragraph (g)(1) TLM ALS revision.
- **Note:** The proposed rule 2024-26092 is not the operative text. The final rule 2025-17066 is in force and was relied on. The final rule corrected the HPT Stage 2 Hub task to 72-45-31-200-009 and added paragraph (g)(2) for air carrier operations.
- **Note:** The required action is a revision of the ICA/TLM and, where applicable, the maintenance or inspection program. It is not a part-based or cycle-based action, so it applies regardless of installed component records, and the empty installed_components list does not change the outcome.
- **Note:** The record has no ad_records or amoc_claims for this AD, so no claimed prior revision or AMOC was assessed.
- **Note:** The 90-day date is computed from the effective date, October 10, 2025, to January 8, 2026. This is a screening result, not a compliance determination.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is within the applicability of AD 2025-19-13, and its installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 (limit 6,000 cycles since new). The AD is published but not effective until 2025-10-29 on the question date, so no action is required yet; removal is tied to the next engine shop visit after the effective date.
- **Stated timing:** Not yet in force on 2025-10-15 (effective 2025-10-29). After the effective date, remove and replace at the next engine shop visit, at or after the later of the 6,000 cycles-since-new limit or 100 flight cycles from the effective date. No deadline applies absent a shop visit.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** Current engine flight-cycle count is not in the record, so the 100-flight-cycles-from-effective-date point cannot be converted to an engine cycle counter value.
- **Missing fact:** The hub's cycles since new on the effective date (2025-10-29) are not recorded. The snapshot shows 990 as of 2025-10-15, so the cycles remaining to the 6,000 limit are computed only as of that date.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0018 (P/N 2A5001) does not match any listed serial number, so it is not an affected part under table 1.
- **Note:** No events are recorded, so no engine shop visit has occurred; none is known to be planned. A future shop visit after 2025-10-29 would trigger the removal. The proposed rule 2025-10764 is superseded by the final rule.
- **Note:** Cycles remaining: 6,000 minus 990 = 5,010 as of the 2025-10-15 snapshot.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 was in force on 2025-11-05 (effective 2025-10-29) and covers the V2531-E5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is listed in table 1 with a 4,800-cycle limit and was already past it at the effective date, so the 100-flight-cycle-from-effective-date criterion governs and removal and replacement is due by engine flight cycle 60,100.
- **Stated timing:** The hub was past its 4,800 cycles-since-new limit on the effective date (4,950 on 2025-10-29; 4,990 on 2025-11-05). The later of the two criteria in paragraph (g) is therefore 100 flight cycles after the effective date, which is engine flight cycle 60,100 (60,000 on 2025-10-29 plus 100). That leaves about 60 engine cycles from the 60,040 reading on 2025-11-05. Paragraph (g) also ties the action to an engine shop visit; no shop visit is recorded.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0019 is not listed in table 1, so no action is triggered by it. The listed 2nd-stage hub serial numbers do not match.
- **Note:** Paragraph (g) is worded as 'at the next engine shop visit ... before exceeding the limit or within 100 flight cycles from the effective date, whichever occurs later'. This screen takes 60,100 engine flight cycles as the outer point, because no shop visit is recorded and the limit has already passed. A reviewer should confirm how the FAA reads the interaction between the shop-visit trigger and this cycle point.
- **Note:** The record lists no events, amoc_claims or ad_records for this AD, so no alternative method of compliance or prior action is available to check.
- **Note:** Cycle readings are consistent: 40 engine cycles elapsed and the hub cycles-since-new rose by 40 between 2025-10-29 and 2025-11-05.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 is in force on 2022-03-01, and a V2533-A5 is a model it covers. Applicability turns on whether the installed disk serial numbers appear in Appendix A, Table 1 or 2, of IAE NMSB V2500-ENG-72-0713 Rev 1, and those tables were not supplied.
- **Stated timing:** If either disk serial number is listed, paragraphs (g)(1) and (g)(2) require a USI at the next engine shop visit after July 13, 2021 or before that disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first. The record shows no events, so whether a shop visit has already occurred cannot be confirmed.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided. It is needed to confirm whether HPT 1st-stage disk P/N 2A5001 S/N SYN-DISK1-0020 is listed, which decides applicability under (c)(1) and (g)(1).
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided. It is needed to confirm whether HPT 2nd-stage disk P/N 2A4802 S/N SYN-DISK2-0020 is listed, which decides applicability under (c)(2) and (g)(2).
- **Missing fact:** The record gives no disk flight-cycle counts, either since July 13, 2021 or now. The 3,200-FC limit therefore cannot be computed, and the cycles remaining cannot be computed either.
- **Missing fact:** The events list is empty. An empty list is not evidence that no engine shop visit occurred after July 13, 2021, so whether the shop-visit trigger has been met is unconfirmed.
- **Note:** Both disk part numbers match those named in the AD, but the serial numbers cannot be checked against the NMSB tables from the supplied material. The part-number match alone does not establish applicability.
- **Note:** AD 2022-02-09 (document 2022-02574) supersedes this AD effective 2022-03-15, so on 2022-03-01 the 2021-11-15 requirements are still the ones in force. The superseding AD changes the compliance times and should be screened separately for any date on or after March 15, 2022.
- **Note:** The record contains no AD records or AMOC claims for this directive.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (document 2022-02574) is published but not effective until 2022-03-15, so on 2022-03-01 it cannot yet require action. The engine model and both disk part numbers match the AD, but applicability depends on whether the disk serial numbers appear in the NMSB Appendix A tables, which were not supplied.
- **Stated timing:** If either disk serial number is listed, the USI under (g)(1) and (g)(2) would be due within the Figure 1 compliance time or within 10 flight cycles after 2022-03-15, whichever is later. Nothing is due before the effective date, and the Figure 1 time is not in the supplied text.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not supplied. Without it, S/N SYN-DISK1-0020 (P/N 2A5001) cannot be checked against the listed serial numbers, and applicability under (c)(1) stays unresolved.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not supplied. Without it, S/N SYN-DISK2-0020 (P/N 2A4802) cannot be checked against the listed serial numbers, and applicability under (c)(2) stays unresolved.
- **Missing fact:** The Figure 1 to paragraph (g)(1) compliance-time table is an image not included in the text. The inspection threshold for V2533-A5 engines cannot be computed without it.
- **Missing fact:** The record has no flight-cycle accumulation for the engine or either disk (for example cycles since new or since last inspection). A cycle deadline and remaining cycles cannot be computed without them.
- **Note:** Both installed part numbers match the AD (2A5001 and 2A4802), but the serial numbers were not matched to any listed serial number, so no part is reported as matched.
- **Note:** The V2533-A5 is a high-thrust model, so paragraphs (g)(1) and (g)(2) would be the operative ones if the serial numbers are listed.
- **Note:** The engine record shows no events, no AD records and no AMOC claims.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2530-A5 is a supported model and AD 2022-02-09 is in force. Applicability turns on whether the installed disk serial numbers appear in Appendix A, Tables 1 and 2, of the incorporated service bulletins. That content was not supplied, so applicability and any deadline cannot be determined.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (HPT 1st-stage disk P/N 2A5001 serial numbers) was not provided. It is needed to decide whether S/N SYN-DISK1-0021 is listed.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (HPT 2nd-stage disk P/N 2A4802 serial numbers) was not provided. It is needed to decide whether S/N SYN-DISK2-0021 is listed.
- **Missing fact:** Figure 1 to paragraph (g)(1), the compliance-time table, is an image not included in the text. It is needed to compute the USI deadline if either disk is listed.
- **Missing fact:** The record has no entry showing whether the USI under this AD (or credit under AD 2021-11-15) was done. It also has no disk flight-cycle history, so any deadline could not be computed even if the disks are listed.
- **Note:** Part numbers 2A5001 and 2A4802 match the AD's part numbers, but the serial numbers cannot be checked against the listed serials without the NMSB tables. No part is recorded as matched.
- **Note:** Absence of a serial number from the supplied material is not evidence that the disks are unaffected.
- **Note:** The empty events list does not show that no USI was done or that no shop visit occurred.
- **Note:** Document 2021-11960 (AD 2021-11-15) is superseded by this AD and was not used for the answer.
- **Note:** This is a screening aid only and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine is within the AD's model list and has an HPT 1st-stage disk, P/N 2A5001, S/N PKLBSH1829, which paragraph (c)(1) lists. The AD became effective 2021-07-19, so paragraph (g)(1) calls for an ultrasonic inspection within 10 flight cycles after that date, which is by engine flight cycle 33010.
- **Stated timing:** Within 10 flight cycles after the 2021-07-19 effective date. The engine was at 33000 cycles on 2021-07-19, so the due point is 33010 engine flight cycles. At 33004 on 2021-07-20, 6 cycles remain.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** Table 1 to paragraph (g)(1) is an image that was not supplied. The 1st-stage disk serial is listed in (c)(1), so the engine is within applicability, but the (g)(1) inspection requirement depends on the disk being in Table 1, which could not be checked.
- **Missing fact:** No AD record or inspection history is supplied. It is not shown whether the paragraph (g)(1) ultrasonic inspection was already done, for example under the emergency AD issued 2021-05-21. The record does not show that it was done.
- **Missing fact:** The 2021-07-19 reading of 33000 cycles is taken as the count at the effective date. The record does not say whether it was taken at the start or the end of that day, which matters if cycles were flown on the effective date itself.
- **Note:** This is a screening aid and not a compliance determination.
- **Note:** The installed 2nd-stage disk S/N SYN-DISK2-0022 does not match any serial listed in (c)(2), so (g)(2) is not triggered by it. The 1st-stage disk match alone brings the engine within applicability.
- **Note:** The record has no AD records, AMOC claims or shop-visit events, so nothing in it shows the inspection was already done.
- **Note:** Nothing in the record supports a component cycle limit, so component cycles remaining is not computed.
- **Expected missing fact (judge on meaning):** operator date of actual notice of Emergency AD 2021-11-51
- **Expected missing fact (judge on meaning):** table 1 to paragraph (g)(1) content (image-only; transcription decided in E3)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 accomplishment instructions (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-022/2021-11960: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2533-A5 is a listed model and the AD was in force on 2021-07-20. Both installed disk part numbers (2A5001 and 2A4802) match the AD, but applicability depends on whether the serial numbers appear in the service bulletin Appendix A tables, which were not supplied.
- **Stated timing:** If either disk serial number is listed in the service bulletin Appendix A tables: USI of that disk at the next engine shop visit, or before the disk has accumulated 3,200 flight cycles since 2021-07-13, whichever occurs first. The cycles at which the AD took effect are not in the record, so no deadline can be computed.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not supplied. It is needed to confirm whether HPT 1st-stage disk P/N 2A5001 S/N PKLBSH1829 is listed. If it is, the engine is within applicability.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not supplied. It is needed to confirm whether HPT 2nd-stage disk P/N 2A4802 S/N SYN-DISK2-0022 is listed.
- **Missing fact:** The engine flight-cycle reading on the effective date 2021-07-13 is not recorded. The 3,200-cycle limit counts from that date, so the cycle deadline cannot be fixed without it.
- **Missing fact:** The record does not show whether each disk's own cycle count matches the engine's. The AD limit applies to cycles accumulated by the disk, not the engine.
- **Note:** The AD is in force, but applicability cannot be settled without the NMSB Appendix A serial-number tables, which were not supplied. A missing table is not evidence that the disks are unlisted.
- **Note:** The engine record shows no events, so no shop visit since the effective date is recorded. An empty event list does not prove none occurred, and any future shop visit would trigger the USI if the disks are listed.
- **Note:** The engine cycle count of 33,004 is not the disk's accumulated cycles since 2021-07-13. The engine count on 2021-07-13 is at most 33,000, and the disk cycle count is not given.
- **Note:** The matched_parts entries show part-number matches only. Serial-number matches to the listed tables are unconfirmed, so listed_serial_number is null.
- **Note:** This is a screening aid only and is not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and applies to all V2527M-A5 engines. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 with a 6,000 cycles-since-new removal limit, so removal and replacement is required at the next engine shop visit and before the hub exceeds that limit (engine flight cycle 25,000).
- **Stated timing:** Remove and replace the HPT 2nd-stage hub at the next engine shop visit after 2025-10-29, and before the hub exceeds 6,000 cycles since new. At the 2025-10-29 effective date the hub had 1,000 CSN, so the limit is reached at engine flight cycle 25,000. This is later than the 100-flight-cycle point (engine flight cycle 20,100), so the later one governs. About 2,500 cycles remain from the 2026-10-06 reading of 22,500.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Note:** Cycle arithmetic: the engine went from 20,000 to 22,500 flight cycles between 2025-10-29 and 2026-10-06, which is 2,500 cycles. The hub went from 1,000 to 3,500 CSN over the same period, so the readings are consistent. The 6,000 limit leaves 2,500 cycles, and the limit is reached at engine flight cycle 25,000.
- **Note:** The record lists no engine shop visit events. If an engine shop visit as defined in (i)(2) has occurred since 2025-10-29 or occurs before the limit, the hub must be removed at that visit.
- **Note:** The installed HPT 1st-stage hub S/N SYN-HUB1-0023 is not in table 1 and is therefore a part eligible for installation under (i)(1).
- **Note:** The 3rd stage HPC rotor blade set and the maintenance program Revision 48, which incorporates AD 2025-17-16 table 1, relate to a different AD. They are not an AMOC and do not address AD 2025-19-13.
- **Note:** The record has no ad_records or amoc_claims entry for AD 2025-19-13.
- **Note:** This is a screening aid only and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 1st-stage hub entries

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527M-A5 engine has a 3rd stage HPC rotor blade set with P/N 6A8688, so AD 2026-17-03 applies and has been in force since 2026-09-24. Replacement of the full blade set is required only at the next engine shop visit after that date where a 3rd stage HPC rotor blade is exposed. The record shows no such visit, so no deadline is triggered now.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); there is no calendar or cycle deadline otherwise.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record lists no engine shop visit (induction for maintenance) after the 2026-09-24 effective date. It cannot be confirmed whether any such visit has occurred or exposed a 3rd stage HPC rotor blade. If one did, replacement would be due at that visit.
- **Note:** The question names 2026-16954; correction 2026-18423 (published 2026-09-10) fixes only the omitted word 'blade' in paragraph (g). The corrected text was used and the result is the same.
- **Note:** The NPRM 2025-20088 is superseded by the final rule and is not used for requirements.
- **Note:** The recorded maintenance program revision incorporating AD 2025-17-16 table 1 and the HPT hub records relate to a different directive. They do not affect this AD.
- **Note:** No AMOC is claimed in the record, and the operator's AD status records were not treated as evidence.
- **Note:** The blade set serial number is not tracked at set level. The AD lists the part number only, so this does not affect the match.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 is in force (effective 2025-10-10) and covers the V2527M-A5 engine. The recorded program and V2500-A5 TLM ALS revision of 2025-12-01 falls before the 90-day due date of 2026-01-08, so no required action is triggered now. Continuing obligations still bind.
- **Stated timing:** The paragraph (g)(1) and (g)(2) revisions were due within 90 days after the 2025-10-10 effective date, i.e. by 2026-01-08. The record shows the revision dated 2025-12-01, inside that window. No further deadline is stated.
- **Missing fact:** The content of Revision 48 and of the revised V2500-A5 TLM ALS (paragraph B.1 of the Maintenance Scheduling section) was not supplied. A reviewer would need to confirm that it incorporates both table 1 inspections, TASK 72-45-11-200-006 and TASK 72-45-31-200-009, as the operator's record asserts.
- **Note:** This is a screening result, not a compliance determination. The operator's recorded revision is a claim to be verified against the actual documents.
- **Note:** The AD requires revising the ALS/TLM and the maintenance program. The inspection tasks themselves are done at piece-part exposure under other regulations once incorporated, so no engine-cycle deadline is computed.
- **Note:** The AD sets no cycle limit for the hubs, so component cycles remaining is not computed. The hub cycle values (3500 cycles since new) are consistent with the engine cycle readings.
- **Note:** The 3rd stage HPC rotor blade set (P/N 6A8688) is not listed in the AD and was not matched.
- **Note:** The NPRM 2024-26092 is superseded by the final rule; the final rule's task reference is 72-45-31-200-009 for the HPT 2nd-stage hub.
- **Unresolved locator:** 2025-17066 (a) Effective date 2025-10-10

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is within the applicability of AD 2025-19-13, which was in force on the question date. Neither installed hub matches a P/N and S/N pair in table 1 to paragraph (g), so no removal is triggered by the record, but the paragraph (h) installation prohibition still binds.
- **Note:** The 2nd-stage hub S/N PKLBST5011 matches the serial number of a listed 1st-stage hub (P/N 2A5001, limit 5,500 cycles). Its recorded P/N is 2A4802, and table 1 lists 2A4802 only with other serial numbers. Because both P/N and S/N must match, it is not treated as a listed part.
- **Note:** Because of that serial-number overlap, a reviewer may want to confirm the 2nd-stage hub's P/N and S/N against the physical part and its records. A transcription error would change the result.
- **Note:** This is a screening result from the supplied record only, not a compliance determination.
- **Note:** The record shows no events or shop visits, and no AD or AMOC claims were supplied.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model in the record, CFM56-5B4/3, is not one of the supported IAE V2500 models, so this screen makes no applicability determination for AD 2025-17-16.
- **Note:** No applicability determination is made for this engine model. The directive was in force on the question date of 2026-10-06, since its effective date was 2025-10-10, but that does not bear on this engine.
- **Note:** If the engine model was recorded incorrectly, re-run the screen with the correct model.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers the V2530-A5. Installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1 with a 6,200 cycles-since-new removal limit. At 3,600 cycles since new, 2,600 cycles remain, so removal and replacement is required at the next engine shop visit before that limit, and no later than engine flight cycle 23,200.
- **Stated timing:** Remove and replace hub PKLBST7489 at the next engine shop visit after 2025-10-29, and before it exceeds 6,200 cycles since new. On the record's counts that is no later than engine flight cycle 23,200, which is 2,600 cycles after the 2026-03-01 reading of 20,600. The 100-cycle-from-effective-date prong (engine cycle 20,100) is already passed and does not extend the deadline, because the later of the two applies.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0026 (P/N 2A4802) does not match any S/N in table 1, so it is not an affected part on the record supplied.
- **Note:** The 2024 blend repair and repeat ultrasonic inspection of hub PKLBST7489 do not change its listing in table 1. The AD has no repair or inspection exception and measures the limit in cycles since new. The record's readings are consistent: 3,000 cycles since new at engine cycle 20,000 and 3,600 at 20,600.
- **Note:** The record shows no engine shop visit after 2025-10-29. Removal is due at the next qualifying shop visit as defined in (i)(2), and if none occurs, before the hub exceeds 6,200 cycles since new (engine cycle 23,200).
- **Note:** The text could be read as requiring removal only at a shop visit, with the limit acting only as a cap on when that visit may occur. The 23,200 figure is the outer point under the 'before exceeding the limit' wording.
- **Note:** No AMOC is claimed in the record. The NPRM 2025-10764 is superseded by the final rule and was not relied on.
- **Note:** This is a screening aid only and not a compliance determination.

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
- **Summary:** The V2527-A5 engine is within AD 2025-19-13, which has been in force since 2025-10-29. Its installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is listed in table 1 with a 4,800 cycles-since-new removal limit. On the primary reading, removal and replacement is due by engine flight cycle 15,300, which is 50 component cycles away.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before the hub exceeds 4,800 cycles since new or within 100 flight cycles after the effective date, whichever is later. On the primary reading that is when the hub reaches 4,800 CSN, at engine flight cycle 15,300, about 50 cycles after the 2026-01-20 reading of 15,250.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The operator's planning note claims an AMOC extending the hub limit to 5,300 CSN, but no approval reference or FAA approval letter is on file. An unverified claim cannot change the 4,800 CSN limit in table 1.
- **Missing fact:** No engine shop visit is recorded since 2025-10-29. If one has occurred or is planned, the record should show whether it meets the paragraph (i)(2) definition, because the removal is tied to the next engine shop visit.
- **Note:** The record shows 4,500 CSN at 2025-10-29 (engine cycle 15,000) and 4,750 CSN at 2026-01-20 (engine cycle 15,250), which are consistent with each other. The 4,800 CSN point corresponds to engine cycle 15,300.
- **Note:** Paragraph (g) is worded as an event at the next engine shop visit tied to a cycle limit. Whether the shop visit must occur before the hub exceeds 4,800 CSN, or the removal may occur at any later shop visit, is a reviewer interpretation. The cycle figure above is the latest point on the primary reading.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0027 is not listed in table 1 and was not matched.
- **Note:** The claimed 5,300 CSN AMOC is not supported by any FAA approval on file and was not relied on.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 was in force on 2026-02-10 and covers the V2524-A5. The installed HPT 2nd-stage hub P/N 2A4802, S/N PKLBST5005 is listed in table 1 with a 4,000 cycles-since-new removal limit, so removal and replacement is required. The record's 'no affected hubs installed' N/A entry is contradicted by this match.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29, no earlier than the later of the 4,000 cycles-since-new limit or 100 flight cycles after the effective date. The 4,000-cycle limit is the later point, so the outer limit is engine flight cycle 11,000. The record shows no shop visit since the effective date.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Note:** Hub cycles since new were 1,000 at 2025-10-29 and are 1,400 at 2026-02-10, consistent with the engine's 400 flight cycles over that period. Remaining margin to the 4,000 limit is 2,600 cycles; 4,000 reached corresponds to engine flight cycle 11,000 (8,000 + 3,000).
- **Note:** The wording of (g) can be read two ways. One reading is that removal is triggered at the next engine shop visit after 2025-10-29, with the later-of cycle limit or 100 flight cycles setting the earliest point. The other is that the cycle limit is the outer deadline. Under the first reading, any shop visit that opens the engine would require removal at that visit. The 100-flight-cycle point (engine cycle 8,100) has already passed, so it is not the controlling date.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0028 is not listed in table 1 and was not matched.
- **Note:** The operator's N/A entry (ad_records for AD 2025-19-13, 'no affected hubs installed') conflicts with the installed PKLBST5005 hub and should be rechecked. No AMOC is claimed.
- **Note:** This is a screening result only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is within the applicability of AD 2025-19-13, which is in force on 2026-02-01. The installed HPT 1st-stage hub S/N PKLBSK9287 matches a listed serial number, but its P/N is recorded as 2A5001-01 and the table lists 2A5001, so whether it is an affected part needs review before any action is stated.
- **Stated timing:** If the hub is confirmed as the listed part: its 100-cycle removal limit is already exceeded (2,400 cycles since new), so the later-of test would be set by 100 flight cycles after the 2025-10-29 effective date. Removal would be at the next engine shop visit after the effective date. No shop visit is recorded, and the engine flight-cycle count at the effective date is not supplied, so no counter deadline can be computed.
- **Missing fact:** The record shows P/N 2A5001-01, while table 1 lists P/N 2A5001 for S/N PKLBSK9287. Confirm whether the -01 dash number is the same part as the listed P/N 2A5001 or a different configuration. This decides whether paragraph (g) is triggered.
- **Missing fact:** The engine flight-cycle counter at the AD effective date (2025-10-29) is not supplied. It is needed to compute the 100-flight-cycle point after the effective date and any counter-based deadline.
- **Missing fact:** No events are recorded. Confirm that no engine shop visit (as defined in paragraph (i)(2)) has occurred since 2025-10-29, since an unrecorded visit would bear on the paragraph (g) timing.
- **Note:** The serial number match is exact, but the P/N differs by the -01 suffix. The match is provisional and not confirmed.
- **Note:** The installed HPT 2nd-stage hub S/N SYN-HUB2-0029 is not listed in table 1 and is not matched. The -2300 component cycles figure applies only if the 1st-stage hub is confirmed as the listed part (100 minus 2,400 cycles since new).
- **Note:** The text of paragraph (g) can be read two ways: removal is required at the next shop visit and cannot be deferred past the later of the cycle limit or 100 flight cycles after the effective date, or removal is required only at a shop visit. The record shows no shop visit, so the deadline cannot be fixed without the missing facts.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
