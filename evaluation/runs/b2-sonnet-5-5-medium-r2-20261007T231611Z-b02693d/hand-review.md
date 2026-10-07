# B2 Hand-Review Sheet

Record results in `hand-review.yaml`. For each unit: gate 5 (forbidden claims, including the standing list), gate 11 (stated timing against the expected timing), and, where listed, missing facts described in words and locators the index could not resolve.

Standing forbidden claims, for every unit:

- The engine or part is compliant or noncompliant.
- The engine or part is safe or airworthy.
- The engine or part is approved for return to service.
- The output is worded as the operator's AD status record.

## seed-001: Listed HPT 1st-stage hub installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527-A5 is within the applicability of AD 2025-19-13, which has been in force since 2025-10-29. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in table 1 (limit 5,500 cycles since new), and the record shows it at 3,100 cycles. Removal is triggered by the next engine shop visit, and the record shows none yet.
- **Stated timing:** At the next engine shop visit after 2025-10-29, with removal due by the later of the 5,500 cycles-since-new limit or 100 flight cycles after the effective date. The 5,500-cycle limit is the later of the two, at about engine flight cycle 45,050, with 2,400 hub cycles remaining.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0001 is not listed in table 1, so it is not matched. Its P/N 2A4802 is listed, but only with different serial numbers.
- **Note:** Cycle counts are consistent: the hub was at 1,650 on 2025-10-29, and the engine added 1,450 cycles to reach 3,100.
- **Note:** No events are recorded, so no engine shop visit has occurred since the effective date. No AMOC or AD record claims were supplied.
- **Note:** This is a screening aid, not a compliance determination. If an engine shop visit occurs before the limit, removal at that visit is triggered. Whether removal is also required at the limit if no shop visit occurs is a reading a reviewer should confirm.

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2533-A5 is within the AD applicability and the AD is in force. Neither installed hub has a P/N and S/N pair listed in table 1 (the 1st-stage hub S/N PKLBST5012 differs from listed PKLBST5011), so the paragraph (g) removal is not triggered on the record supplied.
- **Note:** The 1st-stage hub S/N PKLBST5012 is one character different from listed S/N PKLBST5011; a reviewer should confirm the serial number against the part's data plate and records to rule out a transcription error.
- **Note:** The AD applies to the engine model regardless of installed hubs, so the installation prohibition remains binding.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a V2524-A5 and is within the applicability of AD 2025-19-13, which has been in force since 2025-10-29. The HPT 1st-stage hub S/N and cycles since new are unknown, so it cannot be determined whether a table 1 part is installed. The 2nd-stage hub S/N is not listed.
- **Missing fact:** The HPT 1st-stage hub P/N 2A5001 matches the listed part number, but its S/N is unknown. Table 1 lists four 2A5001 serial numbers, so it cannot be determined whether this hub is an affected part.
- **Missing fact:** Cycles since new for the 1st-stage hub is unknown. It is needed to compare against the removal cycle limit if the S/N turns out to be listed.
- **Missing fact:** No engine shop visit is recorded. The next shop visit after 2025-10-29 would be the trigger for removal if an affected hub is installed.
- **Note:** The 2nd-stage hub P/N 2A4802 is listed, but S/N SYN-HUB2-0003 is not, so it is not matched. The 1st-stage hub cannot be cleared because of its unknown S/N.
- **Note:** The unknown S/N is not evidence that the part is unaffected.
- **Note:** The required action is tied to a shop visit, and none is recorded.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for this directive.
- **Note:** No applicability determination is made for this engine model.
- **Note:** The final rule was effective 2025-10-29, before the question date.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and covers the V2527E-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed in table 1 (limit 3,900 cycles since new). The record says an engine shop visit began on 2025-11-12, so removal and replacement is triggered, with a deadline of 100 flight cycles after the effective date.
- **Stated timing:** Paragraph (g) reads 'at the next engine shop visit after the effective date before exceeding the removal cycle limit or within 100 flight cycles from the effective date, whichever occurs later'. The hub had about 1000 cycles since new on 2025-10-29, well below the 3,900 limit. The limit-based date is therefore far in the future, and the later date controls: 100 flight cycles after the effective date, at engine cycle 18100. The shop visit on 2025-11-12 (18040 cycles) is within that window. The replacement is due at the latest by engine flight cycle 18100 and must be done as part of the shop visit or the 100-cycle limit, whichever occurs later.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The shop visit qualification is only asserted by the operator record. Confirm the 2025-11-12 induction meets the paragraph (i)(2) definition (separation of major mating flanges, not solely for transport or field maintenance in lieu of on-wing).
- **Missing fact:** The HPT 1st-stage hub serial number SYN-HUB1-0005 is not in table 1, so it does not match a listed hub. No action is triggered for it on the supplied facts.
- **Note:** The 100-cycle deadline is computed from engine cycle 18000 at the effective date. The 2nd-stage hub remaining cycles are 3,900 minus 1,040, which is 2,860.
- **Note:** The operator record contains no ad_records or AMOC claims for this AD.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and the V2530-A5 engine is in its applicability. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287 is listed in table 1 with a 100-cycle limit, so removal is required at the next engine shop visit, and no shop visit is recorded.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 100 cycles-since-new limit or within 100 flight cycles after the effective date, whichever occurs later. On the effective-date-plus-100-cycles reading, that is by engine flight cycle 25600. No shop visit is recorded, so no deadline has been triggered yet.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** The HPT 2nd-stage hub serial number SYN-HUB2-0006 is not in table 1, so it does not match. This is noted for completeness only and creates no obligation.
- **Missing fact:** No engine shop visit is recorded. Whether and when the next shop visit occurs, as defined in paragraph (i)(2), determines when removal of the listed hub is triggered.
- **Note:** The hub cycles-since-new reading is 90 at the question date (engine cycles 25530); its reading at the effective date was 60, which is consistent with 30 cycles flown since then.
- **Note:** The hub was installed 2025-09-30, before the effective date, so the installation prohibition in (h) was not violated by that installation. Do not install this part in any engine after 2025-10-29.
- **Note:** The hub has about 10 cycles left before reaching 100 cycles since new. The 'whichever occurs later' wording means the removal is not due before 25600 engine cycles, but the removal still happens only at a shop visit.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, row PKLBSK9287, limit 100

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a V2531-E5 and carries two hubs listed in table 1 (HPT 1st-stage 2A5001/PKLBSS9200 and HPT 2nd-stage 2A4802/PKLBST5005). The AD is in force, and removal is due at the next engine shop visit, no earlier than the later of the removal cycle limit or 100 flight cycles after the effective date, so no action is triggered until a shop visit occurs.
- **Stated timing:** At the next engine shop visit after 2025-10-29, provided the hub's removal cycle limit has been reached or passed or 100 flight cycles after the effective date have elapsed (whichever is later). No deadline applies if no shop visit occurs. The record shows no events or shop visits.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Note:** The 1st-stage hub has 4,300 cycles since new at the question date against a limit of 4,800, leaving 500 cycles. That is the smallest margin. The 2nd-stage hub has 2,300 cycles since new against 4,000, leaving 1,700 cycles.
- **Note:** The 100 flight cycles from the effective date would end at engine cycle 30,100. That is already passed at 30,300, so the limit 'whichever occurs later' is governed by the cycle limits. The 1st-stage hub reaches 4,800 cycles since new at engine flight cycle 30,800, and the 2nd-stage hub reaches 4,000 at 32,000. Because the engine has not had a shop visit, the required action is only triggered by a future shop visit that occurs at or after those points. A shop visit before a hub reaches its limit is a possible alternative reading of the text, but the text says 'whichever occurs later'.
- **Note:** This is a screening result, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows PKLBSS9200 (4,800) and PKLBST5005 (4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 is within the AD's applicability and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in Table 1 (limit 6,200 cycles since new). Removal is due at the next engine shop visit, and no shop visit is recorded; the 2nd-stage hub identity is unknown, so it cannot be cleared.
- **Stated timing:** At the next engine shop visit after October 29, 2025, at or after the later of reaching the 6,200 cycles-since-new limit or 100 flight cycles after the effective date. The 100-cycle point is engine cycle 50,100, already passed. The hub reaches 6,200 at about engine cycle 54,200, so the shop visit trigger is the later of the two; no deadline applies until a shop visit occurs.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The 2nd-stage hub serial number is unknown. P/N 2A4802 is listed, so it cannot be determined whether the hub matches a Table 1 entry.
- **Missing fact:** The 2nd-stage hub cycles since new are unknown. They are needed to compare against the removal cycle limit if the serial number matches a listed entry.
- **Missing fact:** No shop visit is recorded. A future engine shop visit (per the paragraph (i)(2) definition) will trigger removal of the affected hub if the cycle limit has been reached.
- **Note:** The 1st-stage hub had 2,000 cycles since new on 2025-10-29 and 2,500 on 2026-03-10, leaving 3,700 cycles to the 6,200 limit. Engine cycles went from 50,000 to 50,500 over the same period, consistent with the hub's cycles.
- **Note:** No AMOC is claimed in the record. The record has no AD status entry for this AD.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2522-A5 engine model is within the AD's applicability and the AD is in force on the question date. The record lists no installed components, so it cannot be determined whether an affected HPT 1st- or 2nd-stage hub (Table 1) is installed; an empty list is not evidence that none is installed.
- **Stated timing:** If an affected hub is installed, removal is due at the next engine shop visit after October 29, 2025, before exceeding the table removal cycle limit or within 100 flight cycles after the effective date, whichever occurs later. Timing cannot be computed without the hub records.
- **Missing fact:** No record of the installed HPT 1st-stage hub P/N and S/N, cycles since new. Needed to check against Table 1 (P/N 2A5001) and to compute the removal limit.
- **Missing fact:** No record of the installed HPT 2nd-stage hub P/N and S/N, cycles since new. Needed to check against Table 1 (P/N 2A4802) and to compute the removal limit.
- **Missing fact:** No event history (e.g., engine shop visits since October 29, 2025, or flight cycles since the effective date). Needed to determine whether the shop-visit trigger has occurred and the 100-cycle point.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule 2025-18469 and was not relied on for authority.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made.
- **Note:** The installed HPT 1st-stage hub P/N and S/N appear in the AD table, but no matching or determination is made because the engine model is outside the supported scope.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force as of 2026-10-05. Replacement of the full blade set is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no deadline otherwise.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** The record shows no events, so no shop visit since the effective date is recorded; no action is triggered now.
- **Note:** The question was asked of document 2026-16954, but correction 2026-18423 amended paragraph (g) wording; the intent is a blade exposure, and the outcome is the same.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The engine is a supported model (V2533-A5), but the record shows the 3rd stage HPC rotor blade set at P/N 6C8368, which is not an affected P/N (6A8353 or 6A8688), so the AD's applicability condition is not met on the supplied facts.
- **Note:** Set-level serial numbers are not tracked; the record shows a single P/N for the blade set. If individual blades of P/N 6A8353 or 6A8688 were mixed in the set, applicability would need to be rechecked.
- **Note:** The record has no events, so no shop visit has been recorded since the effective date.
- **Note:** This is a screening result only, not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC blade set P/N 6A8688, which is within the applicability of AD 2026-17-03. The shop visit was inducted 2026-09-14, before the 2026-09-24 effective date, so the paragraph (g) replacement is not triggered by that visit; action arises only at a later qualifying shop visit where a blade is exposed.
- **Stated timing:** No deadline now. Replacement is due at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed (removed from the stage 3-8 drum).
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Confirm the installed blade set part number is still 6A8688 (not already replaced or modified to an eligible part number) as of the current visit; the blade exposure on 2026-09-30 may lead to replacement or change of the set.
- **Note:** The blade removal occurred 2026-09-30, after the effective date, but the visit was inducted 2026-09-14, before it. Under (h)(3) and the preamble, the visit induction date governs, so this visit does not trigger (g) on the supplied facts.
- **Note:** Paragraph (g) is read as tied to induction after the effective date; if the FAA or a reviewer reads the exposure date as controlling, replacement could be triggered by the 2026-09-30 removal. This is flagged for review.
- **Note:** The operator's yes entry on the shop visit qualification is an assertion, not evidence settling the outcome.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force on 2026-10-05. The 2026-10-01 shop visit was inducted after the 2026-09-24 effective date, but no 3rd stage blade was removed from the drum, so the paragraph (g) trigger is not established; action is required at the next qualifying shop visit where the blade is exposed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed (removed from the stage 3-8 drum); no fixed deadline otherwise.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** Whether the HPC rotor exposure on 2026-10-02 involved removal of any 3rd stage blade from the stage 3-8 drum. The record says none was removed, so it is not a blade exposure under (h)(2). Confirm the record is complete, since a removal would trigger replacement at this visit.
- **Note:** The question names document 2026-16954. Its paragraph (g) read 'the 3rd stage HPC rotor is exposed', which the correction 2026-18423 fixed to 'rotor blade'. Under either wording, the record's inspection exposure of the rotor did not remove a blade, and (h)(2) defines blade exposure as removal from the drum. The correction's reading is the stricter and is the one used here.
- **Note:** The 2026-10-01 shop visit began after the effective date, so it is the kind of visit paragraph (g) addresses, but the replacement trigger was not met in the record.
- **Note:** The operator record asserts that the visit qualifies as an engine shop visit; this is a claim, and the (h)(3) definition of induction for maintenance supports it.
- **Note:** No cycle-based deadline exists, so cycle fields are null.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527E-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so it is within the proposed applicability. The document is only an NPRM on the question date, so it cannot require action now.
- **Stated timing:** If adopted as proposed, replacement of the full blade set would be due at the next 3rd stage HPC rotor blade exposure (any blade removed from the HPC stage 3 to 8 drum) after the effective date of a final AD. No deadline applies now.
- **Note:** This is a proposed rule with no effective date; no action is required unless and until a final AD is published and effective, and the final text may differ.
- **Note:** The record has no events, so no blade exposure is recorded. Past events are irrelevant because paragraph (g) only counts exposures after the effective date.
- **Note:** Blade set serial numbers are not tracked at set level; the AD lists part numbers only, so this does not affect the match.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a V2527-A5, which is within the applicability of AD 2025-17-16, and the AD has been in force since 2025-10-10. The record says neither the TLM ALS paragraph B.1 nor the approved maintenance program yet incorporates table 1, so the revisions under (g)(1) and (g)(2) are required within 90 days after the effective date.
- **Stated timing:** Within 90 days after the effective date of 2025-10-10, i.e. by 2026-01-08, for both the TLM ALS revision (g)(1) and the air carrier program revision (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Note:** The action is a documentation revision, not a flight-cycle-based inspection, so no cycle deadline or component limit is computed.
- **Note:** The installed components list is empty. The AD requires revising the ALS and program regardless of which parts are installed, so no part matching is needed to establish that the revisions are required.
- **Note:** The record shows an air carrier operation, so (g)(2) applies in addition to (g)(1).
- **Note:** The deadline is computed as 90 days from 2025-10-10, which is 2026-01-08, and no later than that date. Reviewers should confirm the date.
- **Note:** The earlier proposed rule, 2024-26092, is superseded by the final rule and is not relied on for requirements.
- **Note:** This is a screening aid only and does not determine compliance status.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is a listed model, so AD 2025-17-16 applies and is in force (effective 2025-10-10). The ALS/TLM revision in (g)(1) is due within 90 days after the effective date, by 2026-01-08; (g)(2) applies only if the operation is air carrier, which the record does not say.
- **Stated timing:** Within 90 days after the effective date of October 10, 2025, i.e. by January 8, 2026 (paragraph (g)(1); also (g)(2) if air carrier operations).
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the engine is used in air carrier operations is unknown; this determines whether the (g)(2) revision of the approved maintenance or inspection program is also required.
- **Missing fact:** No installed component records; the HPT Stage 1 Hub (P/N 2A5001) is not confirmed. This does not change applicability, which rests on engine model, but is needed to match the table 1 parts.
- **Missing fact:** No installed component records; the HPT Stage 2 Hub (P/N 2A4802) is not confirmed. This does not change applicability, which rests on engine model, but is needed to match the table 1 parts.
- **Missing fact:** No record of whether the ALS/TLM revision has already been done; the operator's status or any AMOC claim is not given.
- **Note:** The proposed rule 2024-26092 is superseded by the final rule and was not relied on for requirements.
- **Note:** The AD requires revising the ALS/TLM and maintenance program, not directly performing the inspections; the inspections are done at piece-part exposure under other regulations once the revisions are made.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is a listed model, and its installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 matches Table 1 (limit 6,000 cycles since new). The AD is published but not effective until 2025-10-29, so no action is required on the question date; removal is tied to the next engine shop visit after the effective date.
- **Stated timing:** At the next engine shop visit after 2025-10-29, or within 100 flight cycles after the effective date, whichever occurs later. The hub has 990 cycles since new against a 6,000 limit, so the cycle limit is not the controlling factor.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The current engine flight-cycle counter is not in the record. Without it, the 100-flight-cycle point after the effective date cannot be converted to an engine cycle count.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0018 is not listed in Table 1, so it does not match.
- **Note:** The 2nd-stage hub is far below its 6,000-cycle removal limit, so the later-of wording makes the next shop visit or 100 cycles after the effective date the controlling point. The engine has no recorded events, so no shop visit is on record.
- **Note:** Whether a future event qualifies as an engine shop visit must be judged against the (i)(2) definition.
- **Note:** The record holds no AD record or AMOC claim for this AD.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is covered and the HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches table 1 (limit 4,800 cycles since new). The hub is already past that limit, so removal is due at the next engine shop visit, which cannot fall earlier than 100 flight cycles after the effective date. No shop visit is recorded, so there is no fixed deadline.
- **Stated timing:** At the next engine shop visit after 2025-10-29, or within 100 flight cycles after the effective date, whichever occurs later. The hub is already past its 4,800-cycle limit, so the later of the two is the 100-cycle point, but the action is still tied to a shop visit.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** No engine shop visit is recorded. The removal obligation is triggered by the next engine shop visit, and no deadline can be computed without one.
- **Note:** The latest cycles-since-new reading is 4,990, which is 190 cycles past the 4,800 limit. The 2025-10-29 reading was 4,950, which is also past the limit.
- **Note:** The 100-flight-cycle window from the effective date ends at engine cycle 60,100, based on 60,000 cycles at 2025-10-29. The engine is at 60,040. This only sets the earliest point at which the shop-visit obligation can bind. It is not a standalone deadline.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0019 is not listed in table 1, so it is not matched.
- **Note:** The record has no AD records or AMOC claims for this AD.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (document 2021-11960) was in force on 2022-03-01 and covers the V2533-A5, but whether it reaches this engine depends on whether the installed disk serial numbers appear in the NMSB Appendix A tables, which were not supplied. Separately, AD 2022-02-09 (2022-02574), effective 2022-03-15, will supersede this AD after the question date.
- **Stated timing:** If the disks are listed: at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. The disk cycles accumulated since that date are not in the record, so no counter value can be computed.
- **Missing fact:** Contents of IAE NMSB V2500-ENG-72-0713 Rev 1 Appendix A, Table 1, were not provided. Needed to confirm whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed.
- **Missing fact:** Contents of IAE NMSB V2500-ENG-72-0713 Rev 1 Appendix A, Table 2, were not provided. Needed to confirm whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed.
- **Missing fact:** Flight cycles accumulated by the HPT 1st-stage disk since 2021-07-13 are not recorded. Needed to compute the 3,200-cycle limit.
- **Missing fact:** Flight cycles accumulated by the HPT 2nd-stage disk since 2021-07-13 are not recorded. Needed to compute the 3,200-cycle limit.
- **Missing fact:** The events list is empty, so no engine shop visit after 2021-07-13 is documented. It is unknown whether the records are complete. Also, no USI history is recorded and no ad_records are supplied.
- **Note:** The part numbers match, but the AD lists the parts by serial number in a service bulletin that was not supplied, so a match is not confirmed.
- **Note:** Question date is 2022-03-01, before the 2022-03-15 effective date of the superseding AD 2022-02-09, which changes the compliance times to Figure 1 values, or 10 FCs after 2022-03-15 if later.
- **Note:** This is a screening aid only and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 is published but not effective until 2022-03-15, so no action is required on 2022-03-01. Whether it applies to this V2533-A5 cannot be decided, because the disk serial numbers must be checked against the service bulletin Appendix A tables, which were not supplied.
- **Stated timing:** If the disks are listed, paragraph (g)(1)/(g)(2) requires the USI within the Figure 1 compliance time or within 10 flight cycles after 2022-03-15, whichever occurs later. Figure 1 is an image not included in the text, so the deadline cannot be computed.
- **Missing fact:** Content of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1, to check whether HPT 1st-stage disk S/N SYN-DISK1-0020 (P/N 2A5001) is listed. Not supplied, so applicability cannot be decided.
- **Missing fact:** Content of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, to check whether HPT 2nd-stage disk S/N SYN-DISK2-0020 (P/N 2A4802) is listed.
- **Missing fact:** Figure 1 to paragraph (g)(1), the compliance-time table, is an image not provided. It is needed to compute the inspection deadline.
- **Missing fact:** Disk cycle accumulation and operating history are not in the record. They are needed to apply the Figure 1 threshold.
- **Missing fact:** Disk cycle accumulation is not in the record. It is needed to apply the Figure 1 threshold.
- **Note:** The engine model is in the supported scope. The part numbers match those named in the AD, but the serial numbers are unverified.
- **Note:** The AD supersedes 2021-11-15, which is the earlier in-force directive on the question date. This answer does not assess that directive.
- **Note:** The record has no events and no AD records or AMOC claims.
- **Note:** This is a screening aid only and is not a compliance determination.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The engine model V2530-A5 is in scope and the disk part numbers (2A5001, 2A4802) match the directive, but whether the installed serial numbers appear in the service bulletin Appendix A tables is not known, so applicability cannot be decided. If listed, a USI is required under (g)(1)/(g)(2) at a compliance time from Figure 1, which is not reproduced in the supplied text.
- **Stated timing:** If the disks are listed, the USI is due within the Figure 1 compliance time to paragraph (g)(1) or within 10 flight cycles after March 15, 2022, whichever is later; the Figure 1 content is not available, so no deadline can be computed.
- **Missing fact:** Whether serial numbers SYN-DISK1-0021 (Appendix A, Table 1 of NMSB V2500-ENG-72-0713 Rev 1) and SYN-DISK2-0021 (Table 2) are listed; the appendix tables were not supplied. This decides applicability.
- **Missing fact:** Content of Figure 1 to paragraph (g)(1) (image not included), which sets the compliance time for high-thrust engines such as the V2530-A5.
- **Missing fact:** Disk cycle accumulation and USI history are not in the record; needed to compute any Figure 1 threshold or credit for prior inspection.
- **Missing fact:** The events list is empty, so no prior USI or shop-visit history is recorded; absence of records is not evidence that no inspection was done.
- **Note:** AD 2022-02-09 superseded AD 2021-11-15; this screen uses the superseding document.
- **Note:** No AMOC or AD status claims were in the record.
- **Note:** The 10-flight-cycle clause counts from the effective date; the record has no cycle data to resolve it.
- **Note:** This is a screening aid and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine has an HPT 1st-stage disk P/N 2A5001 S/N PKLBSH1829 installed, which is listed in paragraph (c)(1), so the AD applies and a USI is required within 10 flight cycles after the 2021-07-19 effective date.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021. The engine had 33000 cycles at 2021-07-19, so the USI is due by 33010 engine flight cycles. At 33004 on 2021-07-20, 6 cycles remain.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** Whether the USI of the HPT 1st-stage disk has already been done, and its result. The record has no event or AD record showing it. A failed USI would require removal before further flight under (g)(3).
- **Missing fact:** Table 2 to paragraph (g)(2) was not provided (image not included), so it cannot be confirmed whether HPT 2nd-stage disk S/N SYN-DISK2-0022 is listed. The serial is not among those named in (c)(2), so it does not appear affected on the supplied text.
- **Note:** The record has no AD records or AMOC claims for this AD.
- **Note:** The 10-cycle count starts from the effective date, using the 33000 reading at 2021-07-19.
- **Note:** This is a screening result, not a compliance determination.
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
- **Summary:** The engine is a V2533-A5 with P/N 2A5001 and 2A4802 disks installed, but the appendix tables of the IAE NMSBs listing affected serial numbers were not supplied, so applicability cannot be decided. If either disk S/N is listed, a USI is due at the next engine shop visit or before that disk accumulates 3,200 FCs since July 13, 2021.
- **Stated timing:** If a disk S/N is listed: at the next engine shop visit after July 13, 2021 or before the disk accumulates 3,200 FCs since July 13, 2021, whichever occurs first.
- **Missing fact:** Contents of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (not provided): needed to determine whether HPT 1st-stage disk S/N PKLBSH1829 is listed.
- **Missing fact:** Contents of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (not provided): needed to determine whether HPT 2nd-stage disk S/N SYN-DISK2-0022 is listed.
- **Missing fact:** Disk cycles accumulated since July 13, 2021 are not in the record; the engine counter reading on the effective date is also not recorded, so the 3,200 FC deadline cannot be converted to an engine cycle count.
- **Note:** The engine record has no events, so no engine shop visit has occurred. No AD or AMOC claims are recorded.
- **Note:** The part numbers match, but the serial numbers must be checked against the NMSB tables.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and applies to the V2527M-A5 engine. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1, so removal is required at the next engine shop visit after 2025-10-29, but not before the 6,000-cycle limit and not earlier than 100 flight cycles after the effective date.
- **Stated timing:** At the next engine shop visit after October 29, 2025, provided the hub has not exceeded 6,000 cycles since new, or within 100 flight cycles after the effective date, whichever is later. The paragraph (g) wording is ambiguous: the 'whichever occurs later' compliance point could be read as the later of the shop visit and the cycle limit. No fixed engine-cycle deadline is established; the hub's cycle count at 2025-10-29 is recorded as 1,000, which conflicts with other record values.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The hub's cycles since new conflict: 3,500 at snapshot versus 1,000 at 2025-10-29 with 2,500 engine cycles flown since, which would give 3,500. This is consistent. However, the current reading is not dated, so confirm it is as of 2026-10-06. Remaining margin to the 6,000 limit is 2,500 cycles if 3,500 is current.
- **Missing fact:** No engine shop visit after 2025-10-29 is recorded, so the triggering event has not occurred. Confirm that no shop visit has occurred since the effective date.
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0023 is not in table 1, so it is not matched. Confirm that the serial number is correct.
- **Missing fact:** The record has no AD 2025-19-13 entry. The maintenance program revision cites AD 2025-17-16, a different AD, and does not address this AD.
- **Note:** The 1st-stage hub is not listed in table 1. The 3rd stage HPC blade set is not relevant to this AD.
- **Note:** The maintenance program revision references AD 2025-17-16, which is not the directive in question; it does not show anything about this AD.
- **Note:** The NPRM 2025-10764 is superseded by the final rule.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527M-A5 engine has 3rd stage HPC rotor blade set P/N 6A8688 installed, so AD 2026-17-03 applies and is in force (effective 2026-09-24). Replacement of the full blade set is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no deadline otherwise.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record shows no engine shop visit or blade exposure after 2026-09-24, so the trigger event has not been shown to occur. Any future shop visit must be checked for blade removal from the HPC stage 3 to 8 drum.
- **Missing fact:** Blade serials are not tracked at set level; individual blade P/Ns within the set are unconfirmed, and any blade replacement history is unconfirmed (e.g. whether the set was already replaced or modified to an eligible P/N such as 6A8688-001).
- **Note:** The question names 2026-16954; the correction 2026-18423 was published 2026-09-10 and fixes a typo in (g) without changing the substance.
- **Note:** The record's AD 2025-17-16 maintenance program revision relates to a different directive (the HPT hub life limits) and does not address this AD.
- **Note:** The HPT hub components are not listed by this AD and were not considered.
- **Note:** The operator's engine cycle counts do not affect the timing, which is event-based only.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 is in force (effective 2025-10-10) and covers the V2527M-A5. The only required action is the one-time ALS/TLM and maintenance-program revision within 90 days (by 2026-01-08), and the record shows a revision on 2025-12-01 that incorporates table 1, so no action is triggered now. Continuing obligations still bind.
- **Stated timing:** The 90-day window after 2025-10-10 ended 2026-01-08. The record's revision dated 2025-12-01 falls inside it. The inspection tasks apply at piece-part exposure.
- **Missing fact:** The content of Revision 48 and of the V2500-A5 TLM ALS revision was not supplied. It is the operator's assertion and needs confirming that paragraph B.1 of the Maintenance Scheduling section incorporates table 1 (TASK 72-45-11-200-006 and TASK 72-45-31-200-009) as paragraphs (g)(1) and (g)(2) require.
- **Note:** The AD lists parts by part number only and sets no hub life limit, so component cycles remaining cannot be computed from the AD. The 20,000-cycle replacement figure in the preamble comes from a comment about AMP section 18, not from the AD's regulatory text.
- **Note:** The record shows inconsistent cycles-since-new for the HPT 2nd-stage hub (3500 now versus 1000 on 2025-10-29). This does not affect the screening outcome.
- **Note:** The 3rd stage HPC rotor blade set (6A8688) is not listed in the AD and was not matched.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is within the AD applicability and the AD is in force. The installed HPT 1st-stage hub S/N SYN-HUB1-0024 is not in table 1, and the 2nd-stage hub S/N PKLBST5011 is listed only as a 1st-stage hub (P/N 2A5001), so its P/N 2A4802 does not match; no removal action is triggered now.
- **Note:** The 2nd-stage hub S/N PKLBST5011 appears in table 1 only for P/N 2A5001 (1st-stage hub, 5,500 cycle limit); the installed part is P/N 2A4802, so it is not a match. Reviewer may wish to verify the record's part number and serial number for transcription error, since the serial coincides with a listed 1st-stage hub serial.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model CFM56-5B4/3 is not one of the supported IAE V2500 models, so no applicability determination is made for AD 2025-17-16.
- **Note:** No determination is made for this engine model. The directive was effective 2025-10-10 and in force on the question date, but that does not bear on this engine.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine is within the AD applicability, and its installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in Table 1 with a 6,200 cycles-since-new removal limit. The hub has about 3,600 cycles since new, so the limit has not been reached, and removal is triggered at the next engine shop visit after the effective date.
- **Stated timing:** Remove and replace at the next engine shop visit after October 29, 2025, before exceeding 6,200 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. No fixed deadline applies until a qualifying shop visit occurs, and the hub reaches 6,200 cycles since new in about 2,600 cycles.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** The current hub cycles since new is 3,600, but the 2025-10-29 reading is 3,000 while engine cycles rose by 600 to 20,600 by 2026-03-01. This is consistent with 3,600 now. Confirm the current value, because the remaining margin to the 6,200 limit depends on it.
- **Missing fact:** The HPT 2nd-stage hub serial number SYN-HUB2-0026 is not in Table 1, so it is not matched. Confirm it against the physical part.
- **Missing fact:** Whether any future engine shop visit, as defined in paragraph (i)(2), occurs. The record shows no shop visit event after the effective date. The 2024 blend repair predates the effective date and does not trigger the action.
- **Note:** The 2nd-stage hub serial number is not listed in Table 1, so it is not matched.
- **Note:** The 2024 blend repair and the repeat inspection with no relevant indications do not alter the Table 1 listing or the required action; the AD has no provision excusing a listed hub on that basis.
- **Note:** Any AMOC claim would need to be checked; none is in the record.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this hub because it was repaired.
- The re-inspection satisfies AD 2025-19-13.
- No removal is required.
- The engine is compliant with AD 2025-19-13.
- The 2024 repair or inspection was the engine shop visit that triggered removal under paragraph (g).
- The repair resets or extends the 6,200 CSN removal limit.

## seed-027: Listed hub near its limit, with an unverified AMOC claimed to extend it

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527-A5 is within the AD, and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches Table 1 (limit 4,800 CSN). The required removal falls due at the next engine shop visit, and no shop visit is recorded. The claimed AMOC is unsupported by any FAA approval on file.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29 (the later of the 4,800 CSN limit or 100 flight cycles after the effective date). With no shop visit recorded, there is no fixed deadline now. The hub reached 4,800 CSN at engine flight cycle 15,050 (about 4,500 CSN at 15,000), so the 4,800 CSN limit has already passed. The 100-cycle point after the effective date was engine cycle 15,100 and has also passed.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** No engine shop visit is recorded. Whether any future or past event after 2025-10-29 meets the (i)(2) definition would trigger the removal.
- **Missing fact:** The claimed AMOC extending the limit to 5,300 CSN has no FAA approval reference or letter on file. It cannot be relied on without an approval under paragraph (j).
- **Missing fact:** The current CSN of 4,750 is inconsistent with the 4,500 CSN reading at 2025-10-29 plus 250 engine cycles since then (which gives 4,750). Both agree, but the hub's current CSN against the 4,800 limit should be confirmed.
- **Note:** The installed HPT 2nd-stage hub S/N SYN-HUB2-0027 is not listed in Table 1 and is not affected.
- **Note:** The hub's cycles remaining are 4,800 minus 4,750 = 50, counting from the 4,800 limit. The 100-cycle-after-effective-date floor corresponds to engine cycle 15,100, which is not yet reached on the engine counter of 15,250. This reading is ambiguous: 15,250 is already past 15,100, so the cycle floor has passed.
- **Note:** The unverified AMOC note (5,300 CSN) is a claim only and does not change the screening result.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is listed in the AD and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 matches Table 1 (limit 4,000 cycles since new). The hub is at 1,400 cycles, so removal is tied to a future engine shop visit; the operator's 'not applicable' note is contradicted by this match.
- **Stated timing:** At the next engine shop visit after October 29, 2025, before exceeding 4,000 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. The 100-cycle window from the effective date has already passed, so the later of the two is the hub's 4,000-cycle limit, and no deadline applies unless a shop visit occurs. The hub must be removed at the shop visit whenever it occurs, and in any case the shop visit does not need to occur before the limit is reached.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The 1st-stage hub serial number SYN-HUB1-0028 is not in Table 1, so it does not match. Record ok, but confirm the serial against the hub's physical data plate.
- **Missing fact:** No shop visit events are recorded; a future engine shop visit (separation of major mating flanges, excluding transport-only or field-maintenance-in-lieu removals) would trigger removal of the 2nd-stage hub.
- **Note:** The operator's record marking the AD not applicable with 'no affected hubs installed' is a claim and is inconsistent with the matched 2nd-stage hub; it should be reviewed.
- **Note:** Cycles remaining: 4,000 - 1,400 = 2,600. The 2nd-stage hub's cycles since new rose 400 from 1,000 at 2025-10-29 to 1,400, consistent with the engine's 400 cycles.
- **Note:** The 1st-stage hub S/N SYN-HUB1-0028 is not listed in Table 1.
- **Note:** Whether the 'whichever occurs later' wording leaves any outer deadline if no shop visit occurs: the text sets none, so action is event-driven.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is within the applicability of AD 2025-19-13, which is in force. The 1st-stage hub S/N PKLBSK9287 matches table 1, but the installed P/N is 2A5001-01 and the table lists 2A5001, so the match depends on a P/N interpretation. The 2nd-stage hub S/N is not listed.
- **Stated timing:** If the 1st-stage hub is an affected part, the AD requires removal at the next engine shop visit after October 29, 2025. Because the part is already past its 100-cycle limit, the 'whichever occurs later' wording points to the later of that shop visit and 100 flight cycles after the effective date. No shop visit is recorded, and the flight cycles accumulated since October 29, 2025 are not in the record, so no deadline can be computed.
- **Missing fact:** The installed P/N is 2A5001-01 and table 1 lists 2A5001. It must be confirmed whether the -01 dash variant is the listed part, because that decides whether S/N PKLBSK9287 is an affected part.
- **Missing fact:** The engine flight-cycle counter on the effective date, 2025-10-29, is not in the record. It is needed to compute the 100-cycle point after the effective date.
- **Missing fact:** The current engine flight-cycle counter is not in the record. It is needed to know how many cycles have been flown since the effective date.
- **Missing fact:** Records of any engine shop visit since 2025-10-29 are absent. The events list is empty, so the shop-visit trigger cannot be assessed, and a missing record is not evidence that none occurred.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0029 is not in table 1, so it is not an affected part.
- **Note:** The 1st-stage hub has 2400 cycles since new against a limit of 100, so it is 2300 cycles past the limit.
- **Note:** No AD or AMOC claims are recorded.
- **Note:** If the part is affected, the action is tied to the next engine shop visit, so it is event-driven. The record's missing shop-visit and cycle data stop a firm status, so this is marked for review.

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
