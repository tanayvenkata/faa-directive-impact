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
- **Summary:** AD 2025-19-13 is in force and covers the V2527-A5 model. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in table 1, so removal and replacement is triggered at the next engine shop visit, no later than engine flight cycle 45050. The record shows no shop visit since the effective date.
- **Stated timing:** At the next engine shop visit after 2025-10-29, by the later of the 5,500 cycles-since-new limit or 100 flight cycles after the effective date. The cycle limit is the later date, at engine flight cycle 45050 (2,400 hub cycles from 3,100 CSN).
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Note:** The 1st-stage hub had 1,650 CSN at 2025-10-29 and 3,100 CSN now. This is consistent with the 1,450 engine cycles flown since the effective date (41200 to 42650).
- **Note:** The 2.5% figure does not apply here. The 1st-stage hub deadline is 41200 + (5,500 − 1,650) = 45050 engine flight cycles.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0001) does not match any listed S/N, so it is not matched under table 1.
- **Note:** The events list is empty, so no shop visit is recorded since the effective date. This is a record of no events, not proof that none occurred.
- **Note:** The record contains no AD status entry or AMOC claim for this AD.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2533-A5 is within the AD applicability and the AD is in force. Neither installed hub (HPT 1st-stage S/N PKLBST5012, HPT 2nd-stage S/N SYN-HUB2-0002) matches an S/N in table 1 to paragraph (g), so no removal action is triggered by paragraph (g); the installation prohibition still binds.
- **Note:** The 1st-stage hub S/N PKLBST5012 differs by one digit from listed S/N PKLBST5011; the record value should be verified against the part's physical data plate/records to rule out a transcription error.
- **Note:** The 2nd-stage hub S/N is a synthetic identifier and is not in table 1.
- **Note:** This is a screening aid only, not a compliance determination. The NPRM 2025-10764 is superseded by the final rule and was not relied on.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 is a listed model, so AD 2025-19-13 applies, and it was in force on 2026-09-26. Whether paragraph (g) is triggered cannot be decided because the HPT 1st-stage hub serial number is unknown. The 2nd-stage hub serial is not in Table 1.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub (P/N 2A5001) is unknown. It must be compared with the four listed S/Ns in Table 1 (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489). An unknown serial is not evidence that the part is unaffected.
- **Missing fact:** The cycles since new of the 1st-stage hub are unknown. If the hub proves to be a listed S/N, they are needed to compare against its removal cycle limit (100 to 6,200 cycles) and to compute any deadline.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) has a listed P/N but its S/N does not appear in Table 1, so it is not an affected part on these facts.
- **Note:** The 1st-stage hub P/N 2A5001 matches the listed P/N, but no listed S/N can be matched while the S/N is unknown, so no part is recorded as matched.
- **Note:** The engine record shows no events, so no engine shop visit since 2025-10-29 is recorded. If the hub is later confirmed as a listed S/N, paragraph (g) action would fall due at the next engine shop visit, subject to the cycle-limit and 100-flight-cycle timing.
- **Note:** The record contains no ad_records or amoc_claims for this AD. This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for AD 2025-19-13.
- **Note:** No determination of applicability, action, or timing is made for this engine model.
- **Note:** The engine record contains no installed components or events; these were not evaluated.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 has been in force since 2025-10-29 and covers the V2527E-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is a listed part with a 3,900 cycles-since-new limit, and the record shows a qualifying shop visit induction on 2025-11-12. Removal and replacement is therefore required, no later than engine flight cycle 18100 on the primary reading.
- **Stated timing:** Primary reading: the hub must be removed and replaced at the next shop visit after the effective date, or within 100 flight cycles after 2025-10-29 (engine cycle 18000 to 18100), whichever is later. The 2025-11-12 induction at 18040 is that shop visit if it meets the AD definition, so the later date is 18100 flight cycles.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Note:** The HPT 1st-stage hub (2A5001, S/N SYN-HUB1-0005) is not listed in table 1 (S/Ns PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489), so it was not matched.
- **Note:** Shop visit status rests on the operator's assertion for the 2025-11-12 induction (flange separation, qualifies 'yes'). A reviewer should confirm that it was not solely for transport or for field maintenance in lieu of on-wing work under paragraph (i)(2).
- **Note:** If the induction did not qualify, the shop-visit trigger would remain open for a later visit; the 100-flight-cycle date of 18100 would still be the earliest the 'whichever later' clause allows.
- **Note:** The record carries no AMOC claim or AD record for this AD.
- **Note:** Hub cycles since new were 1000 on 2025-10-29 and 1040 on 2025-11-12, consistent with 40 engine cycles flown. Remaining to the 3,900 limit is 2860.
- **Note:** This is a screening aid and is not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287 is listed in table 1 with a 100-cycle removal limit. Removal and replacement is required at the next engine shop visit, which must occur no later than the later of the hub reaching 100 cycles since new or 100 flight cycles after the effective date, i.e. engine flight cycle 25600.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29. Under the 'whichever occurs later' wording, the deadline is the later of the hub reaching 100 cycles since new (engine cycle 25540) and 100 flight cycles after the effective date (engine cycle 25600). That is engine cycle 25600, 70 cycles after the 25530 reading on 2025-11-20. The hub has 10 cycles left before its 100-cycle limit.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Note:** The record shows no engine shop visit events, so the removal has not been triggered by a shop visit yet. The shop visit itself must happen before the deadline.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0006 is not listed in table 1 and was not matched.
- **Note:** The hub's cycles since new rose from 60 at engine cycle 25500 to 90 at 25530, which is consistent with the engine counter.
- **Note:** The 1st-stage hub was installed 2025-09-30, before the effective date, so the paragraph (h) installation prohibition does not appear to have been triggered by its installation.
- **Note:** The record has no ad_records or amoc_claims entries for this AD.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 was in force on 2025-12-01 (effective 2025-10-29). The V2531-E5 engine has two installed hubs listed in table 1, so removal and replacement is required. The earliest limit is the HPT 1st-stage hub PKLBSS9200, with a 4,800-cycle limit.
- **Stated timing:** Remove and replace at the next engine shop visit, no later than the later of the hub's removal cycle limit or 100 flight cycles after 2025-10-29. For the 1st-stage hub PKLBSS9200 (limit 4,800 CSN) this is engine flight cycle 30,800, about 500 cycles from the 2025-12-01 reading. For the 2nd-stage hub PKLBST5005 (limit 4,000 CSN) it is engine flight cycle 32,000.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Note:** Cycle computation: the engine was at 30,000 FC on 2025-10-29 and the 1st-stage hub was at 4,000 CSN. The limit of 4,800 is reached 800 cycles later, at engine FC 30,800. The 100-FC floor (30,100) is earlier, so the later date governs.
- **Note:** The 2nd-stage hub PKLBST5005 had 2,000 CSN at the effective date and 2,300 now. Its limit of 4,000 gives 1,700 cycles remaining and an engine FC deadline of 32,000. The 1st-stage hub has 500 cycles remaining (4,800 minus 4,300).
- **Note:** Paragraph (g) ties removal to the next engine shop visit and also sets cycle-based timing. The record shows no shop visit since the effective date. This screen reads the cycle limit as the outer deadline for the 1st-stage hub, but the precise interaction should be confirmed by the reviewer.
- **Note:** No AD records or AMOC claims were supplied. This is a screening result only, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, rows PKLBSS9200 (4,800) and PKLBST5005 (4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 is within the applicability of AD 2025-19-13, which has been in force since 2025-10-29. Its installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in Table 1 with a 6,200 cycles-since-new limit, so removal and replacement is required, and the latest engine flight-cycle count for it is 54,200. The 2nd-stage hub serial number is unknown, so that part cannot be cleared.
- **Stated timing:** Remove and replace the 1st-stage hub at the next engine shop visit after 2025-10-29, before the hub exceeds 6,200 cycles since new (engine flight cycles 54,200). The 100-flight-cycle alternative (engine cycle 50,100) is earlier, so under the 'whichever occurs later' wording the 6,200-cycle limit sets the deadline. No engine shop visit is recorded since the effective date.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The 2nd-stage hub serial number is unknown. Its P/N 2A4802 is a listed part number, so it cannot be compared with the four listed serial numbers (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100). It is therefore unknown whether the hub is affected.
- **Missing fact:** The 2nd-stage hub cycles since new are unknown. If its serial number matches a listed entry, they are needed to compute the removal limit (3,900 to 6,000 cycles).
- **Missing fact:** No shop visits are recorded since 2025-10-29. Whether the next engine shop visit has occurred or will occur before engine cycle 54,200 cannot be confirmed.
- **Note:** Hub cycle computation: 2,000 cycles since new at engine cycle 50,000 (the effective date) gives 6,200 at engine cycle 54,200. The current reading is 2,500 cycles since new at engine cycle 50,500, which leaves 3,700 cycles.
- **Note:** The 2nd-stage hub is not cleared. Its P/N 2A4802 is listed and its serial number is unknown, so the unknown record is not evidence that it is unaffected. If it matches a listed serial number, its smallest limit (3,900 cycles) could come into play and shorten the deadline.
- **Note:** The 1st-stage hub's recorded cycles since new increased consistently with the engine counter (500 cycles each) between the two readings.
- **Note:** The NPRM (2025-10764) was superseded by the final rule and the final rule text governs. The ad_records and amoc_claims fields were not supplied, so no claimed status or AMOC was assessed.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2522-A5 is within the AD's applicability and the AD is in force on the question date, but the record lists no installed components, so it cannot be determined whether an affected HPT 1st-stage or 2nd-stage hub is installed. The absence of component records is not evidence that no affected hub is installed.
- **Missing fact:** No record of the installed HPT 1st-stage hub (P/N, S/N, cycles since new). Needed to check against table 1 to paragraph (g) (P/N 2A5001 with listed S/Ns) and to compute the removal cycle limit.
- **Missing fact:** No record of the installed HPT 2nd-stage hub (P/N, S/N, cycles since new). Needed to check against table 1 to paragraph (g) (P/N 2A4802 with listed S/Ns) and to compute the removal cycle limit.
- **Missing fact:** No event history, so it is unknown whether any engine shop visit (per paragraph (i)(2)) has occurred after the effective date of October 29, 2025, or the engine's current flight-cycle counter.
- **Note:** The NPRM 2025-10764 was superseded by the final rule 2025-18469; the final rule governs.
- **Note:** This is a screening aid only and not a compliance determination.
- **Note:** Installed hub records must be supplied to determine whether paragraph (g) is triggered.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made.
- **Note:** The installed HPT 1st-stage hub P/N and S/N appear in the AD's table 1, but because the engine model is outside the supported scope, no matching or applicability determination is made.
- **Note:** The engine model should be verified by the reviewer against the AD applicability and the engine's type certificate data.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies; it has been in force since 2026-09-24. No replacement is due now, but the full blade set must be replaced with parts eligible for installation at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum). There is no fixed calendar or cycle deadline.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** The engine record lists no events, so no shop visit after the effective date is recorded and no action is triggered now. Confirm the event history is complete.
- **Note:** The correction document 2026-18423 fixes a typographical error in paragraph (g), which now reads 'blade is exposed'. It does not change the effective date or the substance. The question names 2026-16954, and its paragraph (g) is read as corrected.
- **Note:** The NPRM 2025-20088 proposed 'next 3rd stage HPC rotor blade exposure'. The final rule replaced that with the engine shop visit trigger, and the final rule governs.
- **Note:** The blade set serial number is not tracked at the set level. The AD lists the part number only, so the match rests on P/N 6A8353.
- **Note:** No AMOC is claimed in the record. This is a screening result, not a compliance determination.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The engine is a supported model (V2533-A5), but the record shows 3rd stage HPC rotor blades with P/N 6C8368, which is not one of the affected P/Ns 6A8353 or 6A8688, so the AD's applicability condition is not met on the supplied facts.
- **Note:** The record gives the blade set as P/N 6C8368 with no serial tracked at set level; the screen relies on that recorded part number. If the set actually contains any individual blade with P/N 6A8353 or 6A8688, the result would change.
- **Note:** Paragraph (g) as published in 2026-16954 omitted the word 'blade'; correction 2026-18423 restores it. This does not affect this outcome.
- **Note:** This is a screening result only and not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 is in force (effective 2026-09-24) and applies to this V2530-A5 because P/N 6A8688 3rd stage HPC blades are installed. The blade exposure on 2026-09-30 occurred during a shop visit inducted 2026-09-14, before the effective date, so paragraph (g) does not appear to be triggered by that visit; replacement is required at a later qualifying shop visit.
- **Stated timing:** No deadline now. Replacement of the full blade set with parts eligible for installation is due at the next engine shop visit inducted after 2026-09-24 in which a 3rd stage HPC rotor blade is exposed.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record still lists P/N 6A8688 as installed. It does not show whether the blade set was replaced with parts eligible for installation (P/N 6C8368, 6C8403, a later approved P/N, or modified 6A8353-001 or 6A8688-001) after the 2026-09-30 exposure. This affects whether the engine remains within the applicability.
- **Missing fact:** The record does not show that the 2026-09-14 induction was a single continuous visit that was not re-inducted after 2026-09-24. A new induction after the effective date with blade exposure would trigger paragraph (g).
- **Note:** The operator record asserts the 2026-09-14 induction qualifies as an engine shop visit under the AD. The induction pre-dates the effective date, so the exposure on 2026-09-30 is read as falling within a pre-effective-date visit.
- **Note:** Reading the AD only by the NPRM's 'next exposure after the effective date' wording would reach the 2026-09-30 exposure. The final text and the FAA's comment response tie the trigger to shop visit induction after the effective date, and that reading is used here.
- **Note:** This is a screening result only and not a compliance determination. The record does not say whether the blades were replaced during the visit, and the installed P/N remains 6A8688.
- **Note:** No engine flight-cycle data are supplied, so no cycle-based deadline can be computed.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a V2524-A5 with 3rd stage HPC rotor blade P/N 6A8353 installed, so AD 2026-17-03 applies and is in force (effective 2026-09-24). On the corrected paragraph (g), the 2026-10-01 shop visit did not expose a blade because none was removed from the stage 3-8 drum, so replacement is not triggered now; it is required at the next engine shop visit where a 3rd stage blade is exposed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum), replace the full set of 3rd stage HPC rotor blades with parts eligible for installation. No deadline applies until that event.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** The record shows only the HPC rotor exposure for inspection on 2026-10-02 and states no 3rd-stage blade was removed. Confirm that no 3rd stage blade was removed from the stage 3-8 drum at any time during the 2026-10-01 to 2026-10-04 shop visit. A removal would be a blade exposure and would trigger replacement.
- **Note:** Correction 2026-18423 fixed a typographical error in (g) of 2026-16954, and the corrected text is used here. The uncorrected text said 'rotor is exposed', which could be read to treat the 2026-10-02 rotor exposure as a trigger. The corrected wording requires a blade to be exposed, and (h)(2) defines that as removal from the drum.
- **Note:** The record has no engine flight-cycle counter, and no cycle-based limit applies, so no cycle deadline is computed.
- **Note:** The part serial number is not tracked at set level. Applicability rests on the part number only, since the AD lists part numbers only.
- **Note:** This is a screening aid and not a compliance determination.
- **Note:** The record's AD and AMOC claims were not relied on. None were supplied for this AD.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine is a supported model with 3rd stage HPC rotor blades P/N 6A8353 installed, so it is within the proposed AD's applicability. The document is only an NPRM on the question date, so it cannot require action now.
- **Stated timing:** None while the document is only proposed. If adopted as written, replacement of the full blade set would be due at the next 3rd stage HPC rotor blade exposure (any such blade removed from the HPC stage 3 to 8 drum) after the final rule's effective date.
- **Note:** This is a screening aid only, not a compliance determination.
- **Note:** The proposed AD has no effective date and could change before a final rule, so no obligation exists now.
- **Note:** The engine record shows no events, so no blade exposure is recorded. This is not evidence that none will occur or has occurred.
- **Note:** The blade set P/N 6A8353 is not shown as modified to the -001 eligible configuration; if adopted, the blades would be affected unless reworked to 6A8353-001 or replaced with an eligible P/N.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 applies to this V2527-A5 engine and has been in force since 2025-10-10. The operator's record says the paragraph (g)(1) TLM ALS revision and the paragraph (g)(2) air carrier program revision are not yet incorporated, so both are required by the deadline below.
- **Stated timing:** Within 90 days after the effective date of October 10, 2025, which is by January 8, 2026, for both the TLM ALS revision under (g)(1) and the air carrier maintenance or inspection program revision under (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Note:** The record's installed_components list is empty, so no installed part was matched to the HPT hubs in table 1 (P/N 2A5001, 2A4802). The (g) requirements are manual and program revisions that follow from engine model applicability, not from part installation.
- **Note:** The record statement that neither the approved program nor TLM paragraph B.1 yet incorporates table 1 is the operator's assertion. It was not independently verified.
- **Note:** Proposed rule 2024-26092 is the earlier NPRM. The final rule 2025-17066 controls, and it corrected the HPT Stage 2 Hub task reference to TASK 72-45-31-200-009.
- **Note:** Per the preamble, the inspection tasks are done at piece-part exposure and are required through other FAA regulations once the ALS and program are revised. The AD itself requires the revisions.
- **Note:** No amoc_claims are recorded.
- **Note:** This is a screening result only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is a listed model, so AD 2025-17-16 applies and is in force (effective 2025-10-10). Paragraph (g)(1) requires the TLM ALS revision within 90 days after the effective date, which is 2026-01-08. Paragraph (g)(2) also applies if this is an air carrier operation, and the record does not say.
- **Stated timing:** Paragraph (g)(1): within 90 days after October 10, 2025, i.e. by January 8, 2026. Paragraph (g)(2), if air carrier operation: same 90-day deadline for revising the approved maintenance or inspection program.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether this is an air carrier operation is unknown. This decides whether paragraph (g)(2) (revision of the approved maintenance or inspection program) also applies.
- **Missing fact:** The record does not show whether the ALS/TLM revision incorporating the table 1 tasks (HPT Stage 1 Hub TASK 72-45-11-200-006 and HPT Stage 2 Hub TASK 72-45-31-200-009) has already been made. No ad_records entry for AD 2025-17-16 was supplied.
- **Missing fact:** No installed component records were supplied, so the HPT 1st-stage hub (P/N 2A5001) cannot be matched. The paragraph (g) revision is not conditioned on part installation, so this does not change the action.
- **Missing fact:** No installed component record was supplied for the HPT 2nd-stage hub (P/N 2A4802). The paragraph (g) revision is not conditioned on part installation, so this does not change the action.
- **Note:** The 90-day deadline is calendar-based, not a flight-cycle compliance time, so no engine flight-cycle deadline or component cycle margin is computed.
- **Note:** The proposed AD in 2024-26092 is superseded by the final rule 2025-17066; the final rule's table 1 uses TASK 72-45-31-200-009 for the HPT Stage 2 Hub.
- **Note:** The required action is a documentation revision. The inspection tasks themselves are performed at piece-part exposure under other regulations, as explained in the preamble comment responses.
- **Note:** This is a screening aid only and does not determine compliance status.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is within the AD's applicability, and its HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 (limit 6,000 cycles since new). The AD is published but not effective until 2025-10-29, so nothing is required on the question date; removal is tied to the next engine shop visit after the effective date.
- **Stated timing:** Not yet in force (effective 2025-10-29). After that date, remove and replace the hub at the next engine shop visit after the effective date, before exceeding 6,000 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. No deadline applies if no shop visit occurs.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine flight-cycle counter at the effective date (2025-10-29) is not in the record, so the 100-flight-cycle-after-effective-date limit cannot be converted into an engine cycle count. The shop visit date is also unknown.
- **Missing fact:** The HPT 1st-stage hub S/N SYN-HUB1-0018 is not listed in table 1, so it is not matched. Its P/N matches the listed P/N but the S/N differs, so no action is triggered for it.
- **Note:** Component cycles remaining = 6,000 - 990 = 5,010 cycles before the listed removal cycle limit.
- **Note:** The AD is not yet in force on the question date, so no action can be required yet. This is a screening result only, not a compliance determination.
- **Note:** The record has no events, so no shop visit has occurred or been recorded. Any future shop visit after 2025-10-29 should be checked against the (i)(2) definition.
- **Note:** The 2025-10-29 effective date comes from the final rule 2025-18469. The earlier NPRM 2025-10764 is superseded and is not relied on.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine is within the applicability of AD 2025-19-13, which was in force on 2025-11-05. Its installed HPT 1st-stage hub P/N 2A5001, S/N PKLBSS9200 is listed in table 1 with a 4,800-cycle removal limit, and the hub was already past that limit (4,950 CSN) on the effective date. On the text as written, the removal and replacement deadline is therefore 100 flight cycles after the effective date.
- **Stated timing:** Because the 4,800-cycle limit was already exceeded on the effective date (2025-10-29), the later of the two compliance points is 100 flight cycles after the effective date. That is engine flight cycle 60,100, based on 60,000 engine flight cycles on 2025-10-29. As of 2025-11-05 the engine is at 60,040, so 60 engine flight cycles remain.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** No engine shop visit is recorded. Paragraph (g) is worded around the next engine shop visit after the effective date, so whether and when a qualifying shop visit occurs affects how the deadline is read. See the notes.
- **Note:** The hub had 4,950 cycles since new on 2025-10-29 and 4,990 on 2025-11-05, consistent with the engine's 40 cycles flown in that period. Against the 4,800 limit it is 190 cycles past, hence -190.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0019 is not listed in table 1, so it is not matched and no action is triggered by it.
- **Note:** Paragraph (g) says 'at the next engine shop visit ... before exceeding the limit or within 100 flight cycles from the effective date, whichever occurs later'. This screen reads that as a deadline of engine flight cycle 60,100 for removal and replacement. A narrower reading ties the action to a shop visit, which would give no fixed cycle deadline. The record shows no shop visit, and this should be confirmed with the FAA or by AMOC review.
- **Note:** No AMOC or AD record claims were supplied for this AD. This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (document 2021-11960) was in force on 2022-03-01, and the V2533-A5 is a model it lists. Applicability turns on whether the installed disk serial numbers appear in Appendix A, Tables 1 and 2 of IAE NMSB V2500-ENG-72-0713 Rev 1. That content was not supplied, so applicability cannot be decided.
- **Stated timing:** If either serial number is listed, paragraphs (g)(1) and (g)(2) require a USI at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first. The record shows no events, so no shop visit is recorded, and no cycle counts are given, so no deadline can be computed.
- **Missing fact:** Whether serial number SYN-DISK1-0020 (P/N 2A5001) is listed in Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1. The table was not supplied and is needed to decide applicability under (c)(1).
- **Missing fact:** Whether serial number SYN-DISK2-0020 (P/N 2A4802) is listed in Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1. The table was not supplied and is needed to decide applicability under (c)(2).
- **Missing fact:** Flight cycles accumulated by the HPT 1st-stage disk since July 13, 2021, or its cycle count at that date. Needed to compute the 3,200-cycle limit if the disk is listed.
- **Missing fact:** Flight cycles accumulated by the HPT 2nd-stage disk since July 13, 2021, or its cycle count at that date. Needed to compute the 3,200-cycle limit if the disk is listed.
- **Note:** The installed part numbers (2A5001 and 2A4802) match the AD's part numbers, but a serial match against the NMSB tables is required, so no part is recorded as matched.
- **Note:** The question concerns AD 2021-11-15. On 2022-03-01 it remains in force. Superseding AD 2022-02-09 (document 2022-02574) takes effect March 15, 2022 and will replace it, with different compliance times (Figure 1, or within 10 FCs after the effective date, whichever is later). The V2531-E5 service bulletin reference also changes there, but that does not affect this V2533-A5.
- **Note:** The record shows no events, so no engine shop visit is recorded. A missing record does not show that none occurred.
- **Note:** No AMOC or AD record claims were supplied.
- **Note:** This is a screening aid and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2533-A5 is a supported model, and the installed disk part numbers (2A5001 and 2A4802) match the part numbers in AD 2022-02-09. Whether either disk serial number is listed in the NMSB Appendix A tables is not known. The AD is also not effective until 2022-03-15, so it cannot require action on 2022-03-01.
- **Missing fact:** Content of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (HPT 1st-stage disk serial numbers). It is needed to decide whether SYN-DISK1-0020 is a listed disk, which decides applicability under paragraph (c)(1).
- **Missing fact:** Content of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (HPT 2nd-stage disk serial numbers). It is needed to decide whether SYN-DISK2-0020 is a listed disk, which decides applicability under paragraph (c)(2).
- **Missing fact:** Figure 1 to paragraph (g)(1) (compliance-time table) was an image not supplied. It is needed to compute the inspection deadline if either disk is listed.
- **Missing fact:** Current engine flight-cycle counter and each disk's accumulated flight cycles are not in the record. They would be needed to convert the Figure 1 compliance time into a flight-cycle deadline.
- **Note:** No action is required under this AD on 2022-03-01, because it takes effect 2022-03-15. Nothing in this screen should be read as a compliance determination.
- **Note:** The engine has no recorded events, so no shop-visit or prior-inspection credit is shown. The record does not state whether the disks were ever listed or inspected.
- **Note:** The predecessor AD 2021-11-15 (document 2021-11960) remains in effect until superseded on 2022-03-15. Its applicability also depends on the same NMSB serial-number listing, which was not supplied. This screen addresses only document 2022-02574.
- **Note:** Part numbers match, but the serial numbers cannot be matched without the NMSB Appendix A tables, so no matched parts are reported.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 is in force and the V2530-A5 is a listed model. The installed disk part numbers (2A5001 and 2A4802) match, but applicability turns on whether the disk serial numbers appear in Appendix A Tables 1 and 2 of the incorporated service bulletin, which was not supplied.
- **Missing fact:** Contents of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1, needed to check whether HPT 1st-stage disk S/N SYN-DISK1-0021 is listed. Applicability under (c)(1) depends on this.
- **Missing fact:** Contents of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, needed to check whether HPT 2nd-stage disk S/N SYN-DISK2-0021 is listed. Applicability under (c)(2) depends on this.
- **Missing fact:** Figure 1 to paragraph (g)(1) (the compliance-time table) was not included in the text supplied. The inspection deadline for a V2530-A5 cannot be computed without it.
- **Missing fact:** The record gives no flight-cycle counts for the engine or either disk (cycles since new or since the last shop visit or inspection). It also has no history of prior USI or other applicable shop visits. These are needed to apply Figure 1 if the disks are listed.
- **Note:** The engine record has no ad_records or amoc_claims and no events, so no prior inspection or credit is claimed. This screen does not treat that as evidence that no action has been done.
- **Note:** Part numbers match the AD's listed P/Ns, but a serial-number match to the service bulletin tables is not established, so no part is recorded as matched.
- **Note:** If the serials are listed, the V2530-A5 falls under paragraphs (g)(1) and (g)(2), the high-thrust group. Figure 1 would then govern the deadline, with the 10-FC-after-effective-date floor.
- **Note:** Given the March 15, 2022 effective date, the Figure 1 compliance time may already have passed. This cannot be assessed without Figure 1 and the disk cycle history.
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
- **Summary:** The V2533-A5 engine has an HPT 1st-stage disk, P/N 2A5001, S/N PKLBSH1829, which is listed in paragraph (c)(1). The AD is in force on 2021-07-20, so a USI of that disk is required within 10 flight cycles after the 2021-07-19 effective date.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021. The engine was at 33000 cycles on 2021-07-19, so the due point is engine cycle 33010. At 33004 cycles on 2021-07-20, 6 cycles remain. If the USI finds the disk fails, remove it from service and replace it with a part eligible for installation before further flight.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** Table 1 to paragraph (g)(1) is an image not included in the supplied text. Paragraph (g)(1) applies to disks listed in that table. The S/N match is made to the paragraph (c)(1) list, so the table content should be confirmed.
- **Missing fact:** The record does not show whether the USI has already been done. The engine record has no events and no ad_records entry for this AD. Prior accomplishment would affect the action, since the AD is to be done 'unless already done'.
- **Note:** The HPT 2nd-stage disk, P/N 2A4802, S/N SYN-DISK2-0022, is not in the paragraph (c)(2) serial list. It does not trigger (g)(2) on the supplied text.
- **Note:** The deadline of cycle 33010 uses the 2021-07-19 reading of 33000 cycles as the cycle count at the effective date. The record does not say whether that reading was taken at the start or the end of the day.
- **Note:** This is a screening aid only and is not a compliance determination.
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
- **Summary:** AD 2021-11-15 was in force on 2021-07-20 and covers the V2533-A5. Both installed disk part numbers (2A5001 and 2A4802) match the AD, but the AD applies only to serial numbers listed in the NMSB Appendix A tables, which were not supplied. Applicability therefore cannot be decided.
- **Stated timing:** If either serial number is listed, paragraphs (g)(1) and (g)(2) require a USI at the next engine shop visit after 2021-07-13 or before that disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. The record shows no events, so no shop visit has occurred. The 3,200-cycle limit cannot be turned into an engine-cycle deadline from the supplied record.
- **Missing fact:** Contents of Appendix A, Table 1 (HPT 1st-stage disk serial numbers) of IAE NMSB V2500-ENG-72-0713 Rev 1. Needed to see whether S/N PKLBSH1829 is listed, which decides applicability under (c)(1).
- **Missing fact:** Contents of Appendix A, Table 2 (HPT 2nd-stage disk serial numbers) of IAE NMSB V2500-ENG-72-0713 Rev 1. Needed to see whether S/N SYN-DISK2-0022 is listed, which decides applicability under (c)(2).
- **Missing fact:** Engine flight-cycle reading at the effective date (2021-07-13). The record has readings only for 2021-07-19 and 2021-07-20. This reading is needed to anchor the 3,200-cycle limit.
- **Missing fact:** The disks' own flight-cycle counts are not in the record. The AD counts cycles on the disk, which may differ from the engine counter if the disk was moved between engines. These counts are needed to compute remaining cycles.
- **Note:** The installed part numbers match the AD, but the serial numbers cannot be matched to the NMSB tables without those tables, so no parts are listed as matched.
- **Note:** The 1st-stage disk S/N PKLBSH1829 may be a real serial number. Check it against Table 1.
- **Note:** The 2nd-stage disk S/N SYN-DISK2-0022 is synthetic. Check it against Table 2.
- **Note:** The events list is empty, so no engine shop visit is recorded since the effective date.
- **Note:** If either serial number is listed, the 3,200-cycle limit counts from 2021-07-13. The engine counter was 33,000 on 2021-07-19 and 33,004 on 2021-07-20, so the 07-13 reading is needed to anchor it.
- **Note:** This is a screening aid only, not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers the V2527M-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 (limit 6,000 cycles since new), so paragraph (g) removal and replacement is required at the next engine shop visit, and in any case before the hub passes 6,000 cycles since new. At 3,500 cycles since new, that limit is reached at engine flight cycle 25,000.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29, before the hub exceeds 6,000 cycles since new (engine flight cycle 25,000). The 100-flight-cycle alternative from the effective date (engine cycle 20,100) is earlier than the limit, and the text says 'whichever occurs later'. 2,500 cycles remain as of 2026-10-06 (engine at 22,500).
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The record shows no engine shop visit events since 2025-10-29. Confirm whether any event meeting the paragraph (i)(2) definition has occurred. If one has, the listed hub should have been removed at that visit, and the record shows it still installed.
- **Missing fact:** The 1st-stage hub S/N 'SYN-HUB1-0023' is not in table 1, so no match is made. Confirm the serial number as recorded against the physical part.
- **Note:** Cycles since new are 1,000 at 2025-10-29 and 3,500 at 2026-10-06. This agrees with the engine's 2,500 cycles flown (20,000 to 22,500).
- **Note:** The 6,000 limit is reached at engine flight cycle 20,000 + (6,000 − 1,000) = 25,000.
- **Note:** The 1st-stage hub S/N is not listed in table 1, so no 1st-stage hub action is triggered by the record. The 3rd stage HPC blade set is not covered by this AD.
- **Note:** The maintenance program revision (Revision 48) refers to AD 2025-17-16, a different AD. It is not an AMOC and is not evidence of action under AD 2025-19-13. No AMOC claim is recorded.
- **Note:** The proposal 2025-10764 was superseded by the final rule, whose requirements are the same.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (a) effective date 2025-10-29

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527M-A5 engine has a 3rd stage HPC rotor blade set with P/N 6A8688, so AD 2026-17-03 applies. It is in force as of 2026-10-06 (effective 2026-09-24). The blade replacement is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed. The record shows no such event yet.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum). There is no calendar or cycle deadline outside that event.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Note:** The record lists the blade set as P/N 6A8688, not the modified -001 P/N, so it is treated as an affected part. The serial number is not tracked at set level, but the AD lists the part number only.
- **Note:** The record shows no engine shop visit or blade exposure after 2026-09-24, so no replacement is triggered now. The only event listed is a maintenance program revision dated 2025-12-01.
- **Note:** The shop visit is defined as induction of an engine into the shop for maintenance, and the correction document 2026-18423 changes only the word 'blade' in (g). An engine inducted before 2026-09-24 is not captured under this wording, per the preamble discussion in 2026-16954.
- **Note:** The HPT hub records and the maintenance program revision for AD 2025-17-16 do not relate to this AD. No AMOC is claimed in the record.
- **Note:** The NPRM 2025-20088 was superseded by the final rule, and the final text of 2026-16954 as corrected by 2026-18423 was used.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 is in force (effective 2025-10-10) and covers the V2527M-A5 model. The 90-day revision window ended 2026-01-08, and the record shows the TLM ALS and air-carrier maintenance program revised on 2025-12-01, so no further required action is triggered by the supplied facts. The continuing obligations still bind.
- **Stated timing:** The paragraph (g)(1) and (g)(2) revisions were due within 90 days after 2025-10-10, that is by 2026-01-08. The record dates the revisions 2025-12-01, inside that window. No further deadline is triggered.
- **Note:** The AD is applicable by engine model. The hub part numbers were matched only to the Table 1 parts, which are the subject of the added ALS inspections. The AD sets no cycle limit, so no component cycle margin is computed.
- **Note:** The 20,000-cycle replacement figure appears only in a comment response about AMP section 18, not in the AD's regulatory text. The hub cycles-since-new values (3500) are not used for any AD determination.
- **Note:** The 2025-12-01 maintenance_program_revision event and Revision 48 are what the operator records say. The revised content, including TASK 72-45-11-200-006 and TASK 72-45-31-200-009, was not supplied and should be confirmed against the actual TLM and program revisions.
- **Note:** The record has no ad_records or amoc_claims entries for this AD, so no operator-asserted AD status or AMOC was relied on.
- **Note:** The earlier proposed rule 2024-26092 was superseded by the final rule 2025-17066 and was not relied on. Its Table 1 had a task reference that the final rule corrected.
- **Note:** This is a screening result only and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is within the AD's model applicability, and the AD was in force on 2026-10-06 (effective 2025-10-29). Neither installed hub matches a P/N and S/N pair in table 1 to paragraph (g), so the paragraph (g) removal is not triggered. The installation prohibition in paragraph (h) still binds.
- **Note:** The 2nd-stage hub serial number PKLBST5011 matches a table 1 serial number, but that serial is listed for 1st-stage hub P/N 2A5001. The installed part is a 2nd-stage hub with P/N 2A4802, and the P/N and S/N pair is not listed. A reviewer may want to confirm that the serial number or part number was not mis-recorded, since the match on serial alone is unusual.
- **Note:** If the 2nd-stage hub record were found to be wrong, the table 1 match would need to be redone against the corrected identifiers.
- **Note:** Screening result only, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model in the record is CFM56-5B4/3, which is not one of the supported IAE V2500 models, so no applicability determination is made for this directive.
- **Note:** No applicability determination is made for this engine model.
- **Note:** The authority state reflects that the final rule was effective 2025-10-10, before the question date of 2026-10-06.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 was in force on 2026-03-01 and covers the V2530-A5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1 with a 6,200 cycles-since-new removal limit, so removal and replacement is required at the next engine shop visit, with that visit timed against the removal limit.
- **Stated timing:** Remove and replace hub PKLBST7489 at the next engine shop visit after 2025-10-29. Under the 'whichever occurs later' wording, the visit is due before the hub exceeds 6,200 cycles since new, which is engine flight cycle 23,200. The 100-flight-cycle alternative (engine cycle 20,100) is earlier, so the later 6,200-cycle limit governs.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Note:** Hub cycles since new were 3,000 at 2025-10-29 and 3,600 at 2026-03-01, consistent with the 600-cycle engine counter increase (20,000 to 20,600). The limit is reached at engine cycle 23,200 on either basis.
- **Note:** The 2024 blend repair and repeat ultrasonic inspection of PKLBST7489 predate the effective date. The AD has no exception for repaired or reinspected hubs, so they do not remove the hub from table 1.
- **Note:** The record shows no engine shop visit after 2025-10-29. The record lists no AD record or AMOC claim for this AD.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0026 (P/N 2A4802) is not listed in table 1, so no match was made for it.
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
- **Summary:** AD 2025-19-13 has been in force since 2025-10-29 and covers this V2527-A5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is listed in table 1 with a 4,800 cycles-since-new removal limit, and it is at 4,750, so 50 cycles remain. Removal and replacement is therefore required by engine flight cycle 15,300.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29, before the hub exceeds 4,800 CSN. That limit is reached at engine flight cycle 15,300, which is 50 cycles after the 15,250 reading on 2026-01-20. The 100-flight-cycle date (engine cycle 15,100) has already passed, so the later date, 15,300, applies.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The planning note says an AMOC extends the hub removal limit to 5,300 CSN, but no FAA approval reference or letter is on file. Without a verified approval under paragraph (j) it cannot be relied on to change the 4,800 CSN limit.
- **Missing fact:** No engine shop visit is recorded since 2025-10-29. If one has occurred, it would be the removal opportunity, and the record should be checked for it.
- **Note:** Engine cycle 15,300 is computed as 15,250 plus 50 remaining hub cycles. The hub counter is consistent with the engine counter: 4,500 CSN at engine cycle 15,000 on 2025-10-29, and 4,750 CSN at 15,250 on 2026-01-20.
- **Note:** The 100 flight cycles from the effective date end at engine cycle 15,100. That is earlier than the limit-based date, so the later date, 15,300, applies.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0027 is not listed in table 1, so it is not matched. Paragraph (h) still bars installing any listed hub.
- **Note:** The claimed 5,300 CSN AMOC has no FAA approval on file. If it were accepted, the date would move to about engine cycle 15,800, but this screen does not rely on it.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2524-A5 is within the applicability of AD 2025-19-13, which was in force on 2026-02-10. Its installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 is listed in table 1 with a 4,000 cycles-since-new removal limit, so removal and replacement is required at the next engine shop visit, before the hub exceeds 4,000 cycles since new.
- **Stated timing:** At the next engine shop visit after 2025-10-29, and before the hub exceeds 4,000 cycles since new. At the 400 cycles flown since the effective date the hub is at 1,400 CSN, which leaves 2,600 cycles, so the engine counter reaches 11,000. The 100-cycles-from-effective-date alternative (engine counter 8,100) has passed, and 'whichever occurs later' selects the later limit.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Note:** The operator's ad_records entry marks the AD not applicable because 'no affected hubs installed'. The 2nd-stage hub S/N PKLBST5005 appears in table 1, so that note is not supported by the AD text. The record is a claim to check, not evidence.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0028 is not listed in table 1, so it is not an affected part. Listed hubs are matched by P/N and S/N together.
- **Note:** Cycle arithmetic: the hub was at 1,000 CSN at engine counter 8,000 on 2025-10-29, and at 1,400 CSN at 8,400 on 2026-02-10, so the readings are consistent. The 4,000 limit falls at engine counter 11,000, with 2,600 cycles remaining.
- **Note:** No engine shop visit is recorded in events. Wording of (g) can be read as requiring removal only at a shop visit, with the cycle limit as an outer bound. This answer takes 11,000 as the outer cycle bound and does not treat the AD as satisfied by there being no shop visit yet.
- **Note:** The hub was installed 2025-06-03, before the effective date, so the paragraph (h) installation prohibition does not reach that installation.
- **Note:** This is a screening aid only and does not state a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is within the applicability of AD 2025-19-13, which has been in force since 2025-10-29. The installed HPT 1st-stage hub has serial number PKLBSK9287, which is listed in table 1 with a 100-cycle removal limit, and the hub is at 2,400 cycles since new. The installed part number is 2A5001-01 against the listed 2A5001, and the engine-cycle count needed to fix the deadline is not in the record, so the outcome needs review.
- **Stated timing:** Paragraph (g) requires removal and replacement at the next engine shop visit after 2025-10-29, before exceeding the removal limit or within 100 flight cycles after the effective date, whichever is later. The hub is already past its 100-cycle limit, so the 100-flight-cycle-from-effective-date prong appears to control. A deadline counter cannot be computed because the engine flight-cycle count at 2025-10-29 is not in the record. No shop visit is recorded.
- **Missing fact:** Engine flight-cycle counter on the effective date (2025-10-29). It is needed to compute the 100-flight-cycle deadline in paragraph (g). The current counter at the 2026-02-01 snapshot is also needed to see whether that point has passed.
- **Missing fact:** Installed P/N is 2A5001-01, while table 1 lists 2A5001 for S/N PKLBSK9287. The record does not confirm whether the -01 suffix is the same listed part. The serial number matches exactly, so this is treated as a probable match pending confirmation.
- **Missing fact:** The record shows no events. It does not confirm that no engine shop visit has occurred since 2025-10-29. A qualifying shop visit would trigger the paragraph (g) removal.
- **Missing fact:** Interpretation of paragraph (g): whether removal is required only at the next engine shop visit, or also by a flight-cycle deadline when the removal limit has already been exceeded. The AD text does not resolve this.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0029 (P/N 2A4802) is not listed in table 1, so it is not matched.
- **Note:** The NPRM 2025-10764 is not operative because the final rule 2025-18469 has been published and is in force.
- **Note:** The record has no ad_records or amoc_claims, so no operator claim was checked.
- **Note:** This is a screening result only, not a compliance determination.

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
