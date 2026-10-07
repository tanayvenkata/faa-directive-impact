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
- **Summary:** The engine model is supported and the directive is in force since 2025-10-29. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) is listed in Table 1 with a 5,500-cycle removal limit and shows 3,100 cycles since new, so the hub must be removed at the next engine shop visit before it exceeds 5,500 cycles, which by the record's cycle trend is about engine flight cycle 45,050. The installed HPT 2nd-stage hub (S/N SYN-HUB2-0001) is not listed in Table 1.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 5,500 cycles since new (about engine flight cycle 45,050). Under the alternative reading, the 100-flight-cycle window ended at engine flight cycle 41,300, which has already passed.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** The record has no engine shop visit events. Whether an engine shop visit has occurred or is scheduled after 2025-10-29 determines when the removal must be performed, and the operator's qualifies_as_engine_shop_visit determination for any such event is needed.
- **Missing fact:** The undated cycles_since_new value of 3,100 is taken as the current count. It is consistent with the 1,650 reading on 2025-10-29 plus 1,450 engine cycles, but the current reading should be confirmed because the remaining-cycle figure depends on it.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The 2A4802 HPT 2nd-stage hub installed with S/N SYN-HUB2-0001 is not listed in Table 1, so no 2nd-stage action is indicated from the supplied facts.
- **Note:** The engine cycle deadline assumes the hub accrues cycles at the same rate as the engine, which the record supports: the hub gained 1,450 cycles while the engine gained 1,450 cycles from 2025-10-29 to 2026-09-26.
- **Note:** The record lists 2023-04-18 as the installation date, which predates the effective date. The installation prohibition in paragraph (h) therefore does not bear on this hub unless it is removed and reinstalled.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row for P/N 2A5001, S/N PKLBST5011, limit 5,500 cycles since new

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 engine is within the directive's applicability, and the in-force AD is effective October 29, 2025. Neither installed hub's part number and serial number pair matches a row in Table 1 to paragraph (g), so no removal is triggered by the supplied record, but the installation prohibition in paragraph (h) still binds.
- **Note:** This is a screening aid, not a compliance determination. The conclusion covers only the two installed hub records supplied, and it depends on the serial numbers in the record being accurate.
- **Note:** The engine record has no events, so no engine shop visit is recorded. This does not change the outcome because no installed hub matches a listed part number and serial number pair.
- **Note:** The directive's installation prohibition in paragraph (h) applies to any future installation of a listed hub in any engine, so records of future hub installations should be checked against Table 1.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 is a listed model and AD 2025-19-13 (FR 2025-18469) took effect 2025-10-29, so the directive applies to this engine. The installed HPT 2nd-stage hub (2A4802, S/N SYN-HUB2-0003) does not match any Table 1 serial number, but the HPT 1st-stage hub's serial number and cycles since new are unknown, so whether its removal requirement is triggered cannot be determined.
- **Stated timing:** If the HPT 1st-stage hub is a Table 1 listed hub, removal is due at the next engine shop visit after 2025-10-29 before exceeding its listed cycle limit, or within 100 flight cycles of 2025-10-29, whichever occurs later. No shop visit is recorded and the engine flight-cycle counter is not in the record, so the date cannot be computed.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub (P/N 2A5001) is unknown. Table 1 lists four 2A5001 serial numbers with limits from 100 to 6,200 cycles, so the removal requirement cannot be assessed without it.
- **Missing fact:** The cycles since new for the installed HPT 1st-stage hub are unknown. This is needed to compare against the applicable Table 1 removal cycle limit and to compute any remaining cycles.
- **Missing fact:** The engine flight-cycle counter is not in the engine record. It is needed to compute the 100-flight-cycle window from 2025-10-29 and any deadline in flight cycles.
- **Missing fact:** Shop visit history is not in the record (events is empty). It is needed to determine whether an engine shop visit has occurred since 2025-10-29, which would trigger the removal requirement.
- **Note:** This is a screening aid, not a compliance determination. The record does not show whether the AD's removal requirement has been met or is outstanding.
- **Note:** The installed HPT 2nd-stage hub S/N SYN-HUB2-0003 does not appear in Table 1 for P/N 2A4802, so on the supplied facts that part does not match a listed hub; its 5,100 cycles since new do not create a Table 1 limit for it.
- **Note:** The 2A5001 HPT 1st-stage hub is a P/N match only. Its serial number must be confirmed against the four listed serial numbers before any removal deadline can be set.
- **Note:** The 100-flight-cycle alternative runs from 2025-10-29, which is before the question date. Without the engine flight-cycle counter, that count cannot be evaluated.
- **Note:** The record's synthetic flag is true; identifiers starting with SYN- are synthetic.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not an IAE V2500 model supported by this screen, so no applicability determination is made under Federal Register document 2025-18469.
- **Note:** The engine record lists model PW1133G-JM with serial number SYN-PW1100-0004, which is not among the supported IAE V2500 models.
- **Note:** The installed_components and events lists are empty; no component or event facts were evaluated.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527E-A5 engine is a listed model, and AD 2025-19-13 was in force on 2025-11-12. The installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSS9840) is listed in Table 1, and the 2025-11-12 shop visit is recorded as qualifying, so the hub must be removed and replaced under paragraph (g), with the deadline the later of the shop visit or 100 cycles after the effective date.
- **Stated timing:** Remove and replace the listed HPT 2nd-stage hub at the next engine shop visit after 2025-10-29 (the 2025-11-12 induction is recorded as that visit), before exceeding its removal cycle limit of 3,900 cycles since new, or within 100 flight cycles of the effective date, whichever occurs later. Read literally, the later of the two is engine cycle 18,100 (18,000 at the effective date plus 100).
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The 1040 cycles-since-new value has no date. The only dated reading is 1000 at 2025-10-29. Confirming that 1040 is the value as of 2025-11-12 matters for the remaining-cycles figure against the 3,900 limit.
- **Missing fact:** The shop visit's qualification as an engine shop visit under paragraph (i)(2) is operator-asserted. The detail states flange separation for maintenance, which fits the definition, but the qualification has not been independently verified.
- **Missing fact:** No operator AD status record for AD 2025-19-13 appears in the engine record. This screen does not rely on any recorded status, and the absence does not show whether the hub has been removed.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0005) is not among the four listed 1st-stage serial numbers, so it is not matched here. This is a screen against the table as printed, not a determination about the part.
- **Note:** The engine cycle readings (18,000 at 2025-10-29, 18,040 at 2025-11-12) and the hub's cycles-since-new (1,000 to 1,040) move together, consistent with 40 cycles in the interval.
- **Note:** Removal is required regardless of the cycle limit, because the shop visit is recorded as qualifying. The 2,860 remaining cycles figure is only the distance to the cycle limit.
- **Note:** This is a screening aid, not a compliance determination. Nothing here states the engine or any part is compliant, noncompliant, or airworthy.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSS9840, removal cycle limit 3,900

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine is within the directive's applicability, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSK9287) is listed in Table 1 with a 100-cycle removal limit, so removal is required. Under the 'whichever occurs later' wording, the latest engine flight-cycle deadline is 25600 (100 flight cycles after the 2025-10-29 effective date), although the hub reaches its 100-cycle limit around engine cycle 25540. The HPT 2nd-stage hub (S/N SYN-HUB2-0006) is not listed in Table 1.
- **Stated timing:** Remove and replace the listed HPT 1st-stage hub at the next engine shop visit before exceeding 100 cycles since new, or within 100 flight cycles of the 2025-10-29 effective date, whichever occurs later. That is engine flight cycle 25600.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** No engine shop visit or other event is recorded. Whether a shop visit occurs before the deadline affects how the removal is scheduled, though the 100-flight-cycle limit applies regardless.
- **Missing fact:** The 90 cycles-since-new value has no date. It is assumed to be current at the 2025-11-20 snapshot, consistent with the dated reading of 60 on 2025-10-29 and the 30 engine cycles flown in between.
- **Note:** Screening aid only, not a compliance determination. The engine cycle reading on 2025-10-29 (25500) is treated as the effective-date cycle count.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0006) does not match any Table 1 entry, so it is not matched to the directive on the record provided.
- **Note:** The first-stage hub was installed 2025-09-30, before the effective date. The installation prohibition in paragraph (h) applies only to installations after 2025-10-29, and this record does not show a post-effective-date installation.
- **Note:** The directive is in force on the question date (effective 2025-10-29). The 2025-06-13 NPRM is superseded by the final rule and is not relied on for requirements.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSK9287, limit 100 cycles

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine has an installed HPT 1st-stage hub (2A5001, S/N PKLBSS9200) listed in Table 1 of AD 2025-19-13, which was in force on 2025-12-01. Required removal is due at the next engine shop visit before the hub exceeds 4,800 cycles since new, or within 100 flight cycles of 2025-10-29, whichever occurs later; the hub has about 500 cycles remaining, so the required action is due by engine flight cycle 30800 on the later-of reading.
- **Stated timing:** Remove and replace the listed HPT 1st-stage hub at the next engine shop visit after 2025-10-29 before exceeding 4,800 cycles since new, or within 100 flight cycles from 2025-10-29, whichever occurs later. The 100-flight-cycle date was engine flight cycle 30100, which the engine had already passed on 2025-12-01 (30300).
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** The record lists no events, so it is unknown whether or when the engine's next shop visit (separation of major mating H-P flanges) will occur. The shop-visit trigger in paragraph (g) cannot be assessed against the record.
- **Missing fact:** The 4,300 cycles-since-new value is undated. It is assumed to be current as of 2025-12-01 and is consistent with the 4,000 reading on 2025-10-29 plus the 300 engine cycles elapsed. The remaining-cycles figure depends on this value.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) is also listed with a 4,000-cycle limit. It is installed at 2,300 cycles since new, leaving 1,700 cycles, so it is not the controlling limit.
- **Note:** The 2025-10764 NPRM was the proposed version and is not relied on; the in-force final rule is 2025-18469.
- **Note:** The engine's 30,000 cycle reading on 2025-10-29 and 30,300 on 2025-12-01 imply 300 cycles in about 33 days. If that rate continues, the 500 remaining hub cycles would be used in roughly 55 days.
- **Note:** Requirements in paragraph (g) are triggered by the engine's next shop visit and the cycle limit. The AD does not set a calendar deadline, so the time-based 100-cycle window has already elapsed and the action is likely overdue under the alternative reading.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200, limit 4,800 cycles since new; HPT 2nd-stage hub row 2A4802 / PKLBST5005, limit 4,000 cycles since new

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive is in force (effective 2025-10-29) and applies to this supported V2528-D5 engine. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) matches a Table 1 row with a 6,200 cycles-since-new removal limit, so it must be removed at the next engine shop visit before that limit is exceeded; the record shows 3,700 cycles remaining and no shop visit recorded. The installed HPT 2nd-stage hub cannot be screened because its serial number and cycles since new are unknown.
- **Stated timing:** Remove the matched HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 6,200 cycles since new, or within 100 flight cycles from 2025-10-29 if that is later. No shop visit is recorded yet, so the deadline is event-driven.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The serial number of the installed HPT 2nd-stage hub is unknown, so it cannot be checked against the Table 1 P/N 2A4802 serial numbers.
- **Missing fact:** Cycles since new for the installed HPT 2nd-stage hub are unknown, so the removal limit cannot be compared even if the serial number is listed.
- **Missing fact:** The record shows no engine shop visit. Whether and when the next shop visit occurs determines when the 1st-stage hub must be removed.
- **Missing fact:** The 2,500 cycles-since-new value for the 1st-stage hub has no date. Only a 2,000 reading dated 2025-10-29 is recorded, so the remaining-cycles figure assumes 2,500 is current as of the snapshot.
- **Note:** This is a screening aid, not a compliance determination. The 1st-stage hub match is a screen only, and the hub must still be verified against the installed part record.
- **Note:** The HPT 2nd-stage hub cannot be screened: its serial and cycles since new are unknown. A missing record is not evidence that the hub is unaffected.
- **Note:** Because the hub limit is measured in hub cycles since new, and the record gives no hub-to-engine cycle mapping, no engine flight-cycle deadline is computed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row for P/N 2A5001 and S/N PKLBST7489 with removal cycle limit 6,200

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2025-18469 applies to the supported V2522-A5 model and took effect October 29, 2025. The engine record lists no installed components and no events, so whether any listed HPT 1st- or 2nd-stage hub is installed cannot be determined, and the required removal timing cannot be computed.
- **Stated timing:** At the next engine shop visit after October 29, 2025, before exceeding the applicable removal cycle limit in Table 1 to paragraph (g), or within 100 flight cycles from October 29, 2025, whichever occurs later, if a listed hub is installed.
- **Missing fact:** No HPT 1st-stage hub record is present. Whether a hub with P/N 2A5001 and a serial number listed in Table 1 is installed is needed to decide whether paragraph (g) applies. An absent record is not evidence that the hub is absent.
- **Missing fact:** No HPT 2nd-stage hub record is present. Whether a hub with P/N 2A4802 and a serial number listed in Table 1 is installed is needed to decide whether paragraph (g) applies.
- **Missing fact:** The engine flight-cycle counter is not in the record. It is needed to compute the 100-flight-cycle window and any cycle-limit deadline, and to compare a hub's cycles since new against its limit.
- **Missing fact:** No engine shop visit history is recorded. Whether a shop visit has occurred or will occur after October 29, 2025, is needed to set the timing of paragraph (g) and to know whether the installation prohibition in paragraph (h) has been reached.
- **Note:** This is a screening aid, not a compliance determination. The engine record has no installed components and no events, so no listed hub has been confirmed as installed or absent.
- **Note:** Because the record is empty, the screen cannot establish whether paragraph (g) removal is due. Once the hub records and cycle counter are supplied, the screen can compare each installed hub's serial number and cycles since new against Table 1.
- **Note:** The AD's installation prohibition in paragraph (h) continues to bind regardless of the removal outcome.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model is recorded as V2500-A1, which is not among the supported V2522-A5, V2524-A5, V2525-D5, V2527-A5, V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2531-E5, or V2533-A5 models, so this screen makes no applicability determination under this directive.
- **Note:** The engine record lists model V2500-A1, which is outside the supported model scope for this screen; no applicability, cycle, or part-match determination was made.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) appears in Table 1 of the directive, but it was not evaluated because the engine model is outside the supported scope.
- **Note:** This output is a screening aid only and is not a compliance determination.
- **Unresolved locator:** 2025-18469 (c) Applicability paragraph listing IAE AG V2522-A5, V2524-A5, V2525-D5, V2527-A5, V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2531-E5, and V2533-A5 engines
- **Unresolved locator:** 2025-18469 preamble Effective date October 29, 2025 in the Federal Register record

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has a recorded 3rd stage HPC rotor blade set with P/N 6A8353, which is within the directive's applicability, and the directive has been in force since September 24, 2026. Replacement of the full blade set is required only at the next engine shop visit after that date where the 3rd stage HPC rotor blade is exposed, and the record shows no such event, so no action is triggered on the question date.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed (the blade is removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline applies otherwise.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** No engine shop visit events are recorded. Whether any shop visit after 2026-09-24 exposes the 3rd stage HPC rotor blade cannot be determined, so whether the replacement obligation has been triggered is unknown.
- **Missing fact:** The serial number is recorded as not tracked at set level. This does not affect applicability, which turns on P/N, but a set-level or per-blade record would be needed to confirm the full set is replaced when the event occurs.
- **Note:** The screen uses the final rule 2026-16954 as corrected by 2026-18423. The proposed rule 2025-20088 is superseded for this purpose, and its 'next 3rd stage HPC rotor blade exposure' wording was replaced by the engine shop visit trigger.
- **Note:** The engine record has no ad_records or amoc_claims entries for this directive, so no operator AD status claim is evaluated.
- **Note:** This is a screening aid only and does not state whether the engine or any part is compliant, airworthy, or approved for return to service.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The V2533-A5 is a supported model and AD 2026-17-03 (FR 2026-16954, effective 2026-09-24) is in force on the question date. The engine record lists the installed 3rd stage HPC rotor blade set as P/N 6C8368, which the AD names as a part eligible for installation, not as an affected P/N (6A8353 or 6A8688), so the engine does not appear to fall within the applicability paragraph.
- **Missing fact:** Blade serial numbers are not tracked at set level, so the record cannot confirm that every blade in the set is P/N 6C8368 and that no 6A8353 or 6A8688 blade is installed. Individual blade part-number traceability would confirm the applicability screen.
- **Missing fact:** The events list is empty, so no engine shop visit or 3rd stage HPC rotor blade exposure is recorded. This would matter only if the applicability question were resolved the other way.
- **Note:** This is a screening aid, not a compliance determination. The answer addresses only applicability to the recorded installed P/N and does not state that the engine is compliant or airworthy.
- **Note:** If blade-level records show any 6A8353 or 6A8688 blade installed, the AD would apply, and the required action would trigger at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed, with latest engine flight cycles unknown from this record.
- **Note:** The 2026-18423 correction is included because it changes the operative wording of paragraph (g), though it does not change the applicability analysis.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 applies to this V2530-A5 engine because a 3rd stage HPC rotor blade set with P/N 6A8688 is recorded as installed. The required blade-set replacement is triggered only at the next engine shop visit after the 2026-09-24 effective date where the blade is exposed; the 2026-09-14 induction predates that date, so no action is triggered by the record as supplied.
- **Stated timing:** At the next engine shop visit after 2026-09-24 (the AD's effective date) in which a 3rd stage HPC rotor blade is exposed. No calendar deadline applies before that event.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The engine flight-cycle counter is not in the record. It is not needed for this screen because the obligation is tied to a shop-visit event, but it would be needed to express any cycle-based deadline.
- **Missing fact:** The blade set serial is recorded as not tracked at set level, so individual blade serials cannot be confirmed. The AD keys on part number, so this does not block the match, but it limits traceability of the blade set.
- **Missing fact:** The induction on 2026-09-14 is recorded as an engine shop visit, but the operator's 'yes' classification is an assertion. The timing of the induction relative to the 2026-09-24 effective date controls the result, and the exact induction timestamp is needed to confirm it preceded the effective date.
- **Note:** The 2026-09-14 induction is before the 2026-09-24 effective date, so under paragraph (g) it cannot be the qualifying shop visit even though the operator marks it as an engine shop visit under the AD definition.
- **Note:** The blade removal on 2026-09-30 occurred during that pre-effective-date visit. Because the required action is keyed to a shop visit after the effective date, this record does not trigger replacement now. A reviewer should confirm with the FAA or the operator if the exposure date is intended to control.
- **Note:** If a later shop visit occurs after 2026-09-24 and a 3rd stage HPC rotor blade is exposed, the full blade set replacement would be required at that visit.
- **Note:** The screen does not determine compliance status, and the operator's recorded classification is an assertion to be checked.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2026-17-03 (FR 2026-16954, effective 2026-09-24, typo corrected by FR 2026-18423) applies because the engine is a V2524-A5 with 3rd stage HPC rotor blade P/N 6A8353 installed. The 2026-10-01 shop visit occurred after the effective date and is recorded as a qualifying engine shop visit, but the record states no 3rd stage blade was removed from the stage 3 to 8 drum, so the defined blade exposure that triggers blade-set replacement is not shown and no replacement is triggered on this record.
- **Stated timing:** Replacement of the full 3rd stage HPC rotor blade set is due at the next engine shop visit after 2026-09-24 in which a 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum; no such removal is recorded for the 2026-10-01 visit.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** Engine flight-cycle counter is not supplied, so no cycle-based deadline can be computed if a future qualifying blade exposure occurs.
- **Missing fact:** The record does not confirm that no 3rd stage blade was removed during the 2026-10-02 HPC rotor exposure beyond the operator's detail note; whether any blade was removed from the stage 3 to 8 drum controls whether replacement is triggered.
- **Missing fact:** Paragraph (g) as corrected refers to the 3rd stage HPC rotor blade being exposed, while paragraph (h)(2) defines exposure as removal from the drum; the record shows an inspection exposure without removal, so the reviewer should confirm the defined term governs.
- **Note:** Screening aid only; this is not a compliance determination. The shop-visit qualification and the no-removal statement are operator assertions in the synthetic record and were not independently verified.
- **Note:** The shop visit of 2026-10-01 closed and the engine returned to service on 2026-10-04. If a reviewer reads paragraph (g) as triggered by any rotor opening rather than blade removal under (h)(2), replacement would have been due at that visit, but the cycle counter needed to state a deadline is not supplied.
- **Note:** The blade set serial number is not tracked at set level, so the listed serial number is null.
- **Note:** The record includes no AMOC claims or other AD records for this directive.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model is supported and the installed 3rd stage HPC rotor blade set is recorded as P/N 6A8353, which falls within the proposed directive's applicability. However, Federal Register document 2025-20088 is a notice of proposed rulemaking with no effective date, so it cannot require action on the question date.
- **Missing fact:** The blade set is recorded as not tracked at set level, so individual blade serial numbers are unavailable. This would matter if the directive's applicability or part-eligibility status needed to be checked blade by blade.
- **Missing fact:** The events list is empty. The directive's required action is triggered by a 3rd stage HPC rotor blade exposure (removal from the HPC stage 3 to 8 drum), so any future or past exposure event would need to be recorded to assess timing if the directive is adopted.
- **Missing fact:** A final rule adopting this proposal, with an effective date, has not been provided. Without it, the required action in paragraph (g) cannot be assessed as binding.
- **Note:** This is a screening aid, not a compliance determination. The answer does not state that the engine or its blades are compliant or noncompliant.
- **Note:** The directive is a proposal only and cannot require action until a final rule is published and effective. The comment deadline of January 2, 2026 precedes the question date of January 15, 2026.
- **Note:** The engine record contains no AD status records or AMOC claims, and no events are recorded.
- **Unresolved locator:** 2025-20088 preamble Summary and DATES sections

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 (FR 2025-17066) is in force (effective 2025-10-10) and covers V2527-A5 engines. The operator is an air carrier whose record says neither its approved program nor TLM paragraph B.1 yet incorporates table 1, so the paragraph (g) revisions are required by 2026-01-08 (90 days after the effective date).
- **Stated timing:** Within 90 days after the 2025-10-10 effective date, i.e. on or before 2026-01-08: revise TLM paragraph B.1 of the Maintenance Scheduling ALS (g)(1), and for air carrier operations revise the existing approved maintenance or inspection program (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** No installed component record for the HPT Stage 1 hub (P/N 2A5001) is supplied. Its piece-part exposure inspection (TASK 72-45-11-200-006) cannot be tracked without it. A missing record is not evidence that the part is absent.
- **Missing fact:** No installed component record for the HPT Stage 2 hub (P/N 2A4802) is supplied. Its piece-part exposure inspection (TASK 72-45-31-200-009) cannot be tracked without it. A missing record is not evidence that the part is absent.
- **Missing fact:** The record states that neither the approved program nor TLM paragraph B.1 yet incorporates table 1. Confirmation that the (g)(1) and (g)(2) revisions are completed by 2026-01-08 is needed to close the action; this screen does not treat the current record as compliant or noncompliant.
- **Note:** This is a screening aid, not a compliance determination. The engine record contains no installed component records and no events, so no hub-level status can be assessed.
- **Note:** The 90-day period runs from the 2025-10-10 effective date to 2026-01-08. The record shows the required revisions are not yet incorporated, so action is required within that window.
- **Note:** The NPRM 2024-26092 is superseded by the final rule and was not relied on for the deadline. The final rule's paragraph (g) text, as amended, governs.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** Engine model V2522-A5 is within the applicability of AD 2025-17-16 (Federal Register 2025-17066), which took effect 2025-10-10. The required one-time revision of the airworthiness limitations section (TLM paragraph B.1 and, for air carrier operations, the approved maintenance program) to add the HPT Stage 1 and Stage 2 hub inspections is due within 90 days of the effective date, by 2026-01-08.
- **Stated timing:** Within 90 days after the 2025-10-10 effective date, i.e., by 2026-01-08, for the paragraph (g)(1) TLM revision and, for air carrier operations, the paragraph (g)(2) maintenance program revision.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the operator conducts air carrier operations is unknown. This determines whether the paragraph (g)(2) revision of the approved maintenance or inspection program applies in addition to the paragraph (g)(1) TLM revision.
- **Missing fact:** No record shows whether the TLM Maintenance Scheduling paragraph B.1 revision or the (g)(2) program revision has been made. The record cannot confirm the status of the required action.
- **Missing fact:** No installed component record for the HPT Stage 1 hub (P/N 2A5001) is present. Its inspection task applies at piece-part exposure, so the installed hub identity and its exposure history are needed to see whether the inspection is triggered.
- **Missing fact:** No installed component record for the HPT Stage 2 hub (P/N 2A4802) is present. Its inspection task applies at piece-part exposure, so the installed hub identity and its exposure history are needed to see whether the inspection is triggered.
- **Missing fact:** The engine flight-cycle counter is not supplied, so the cycle-based deadline cannot be computed. The directive sets a calendar deadline, not a cycle limit.
- **Note:** This is a screening aid, not a compliance determination. The directive requires a one-time revision of the ALS and maintenance program. It does not by itself require the hub inspections on a set schedule. Under the directive's preamble, the inspections are performed at piece-part exposure under the TLM.
- **Note:** The deadline of 2026-01-08 is computed as 90 days after the 2025-10-10 effective date.
- **Note:** The engine record has no installed components, events, or AD status entries. Nothing in the record confirms or rules out the required revision.
- **Note:** The record does not give the operator's EMM or TLM version, so which TLM P/N applies to this engine cannot be confirmed from the record.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is a supported model within the AD's applicability, and installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 matches a Table 1 row with a 6,000-cycle removal limit (5,010 cycles remain at 990 cycles since new). The AD does not take effect until 2025-10-29, so it cannot require action on the 2025-10-15 question date, though the removal requirement will apply from that date.
- **Stated timing:** Not yet in force on 2025-10-15. Once effective on 2025-10-29, remove the listed hub at the next engine shop visit after that date before exceeding the removal cycle limit, or within 100 flight cycles from the effective date, whichever occurs later. The 2nd-stage hub must be removed before exceeding 6,000 cycles since new.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine flight-cycle counter is not in the record, so the 100-flight-cycle window from the 2025-10-29 effective date cannot be converted into an engine cycle number.
- **Missing fact:** The events list is empty, so there is no record of whether any engine shop visit has occurred or is scheduled after 2025-10-29. The next-shop-visit trigger cannot be assessed.
- **Missing fact:** Whether the HPT 1st-stage hub S/N SYN-HUB1-0018 is the installed serial number is confirmed by the record, but it is not in Table 1, so the record supports no match. Verification of the S/N against the record is still needed for the 1st-stage hub before the AD is assessed as complete.
- **Note:** The question date (2025-10-15) falls before the 2025-10-29 effective date, so no action is required now. Continuing obligations apply once the AD is effective.
- **Note:** The 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0018) is not in Table 1 and is not a matched part on this record.
- **Note:** The 2nd-stage hub's 5,010 remaining cycles is a count to the table limit only. It is not a compliance determination and does not establish that the part is compliant or noncompliant.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSR2100, limit 6,000 cycles

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 is a listed model, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) matches Table 1, whose removal limit is 4,800 cycles since new. The hub's recorded cycles since new (4,950 or 4,990) already exceed that limit, so removal is required at the later of the next engine shop visit or 100 flight cycles after the 2025-10-29 effective date (engine cycle 60,100); this is a screening result, not a compliance determination.
- **Stated timing:** Remove the affected HPT 1st-stage hub and replace it with an eligible part at the next engine shop visit after 2025-10-29 or within 100 flight cycles of the effective date, whichever is later. Because the hub is already past its 4,800-cycle removal limit, the shop-visit timing cannot be relied on to meet the cycle limit, so this needs immediate reviewer attention.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The record gives 4,990 cycles since new with no date, but the dated reading on 2025-10-29 is 4,950. The current value affects the remaining-cycle figure (-190 or -150), though both show the hub is past its 4,800-cycle limit.
- **Missing fact:** The events list is empty. Whether an engine shop visit (separation of major mating H-P flanges) has occurred or is scheduled after 2025-10-29 is unknown, and that event would set the removal timing under paragraph (g).
- **Note:** The AD was published as a final rule on 2025-09-24 with effective date 2025-10-29 and is in force on the question date 2025-11-05.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0019) is not listed in Table 1, so it does not match the table on this record.
- **Note:** The engine cycle reading of 60,000 on 2025-10-29 is used as the effective-date cycle count, which gives 60,100 as the 100-cycle point.
- **Note:** No ad_records or amoc_claims are present, so no operator AD status or alternative method of compliance is evaluated.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200, limit 4,800 cycles

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The engine model is in the supported V2533-A5 scope, but applicability cannot be decided because the record does not show whether the installed HPT 1st-stage disk (P/N 2A5001) and HPT 2nd-stage disk (P/N 2A4802) serial numbers appear in the Appendix A lists of the referenced NMSBs. AD 2021-11-15 remains in force on 2022-03-01 but is superseded by AD 2022-02-09, effective 2022-03-15, which changes the compliance times for disks that have operated on high-thrust engines.
- **Stated timing:** Under 2021-11960 paragraph (g)(1), if the disk serial is listed, the USI is due at the next engine shop visit after 2021-07-13 or before 3,200 flight cycles accumulate since that date, whichever occurs first. The superseding 2022-02574 replaces these with the Figure 1 compliance time, or 10 flight cycles after 2022-03-15 if later; that figure is not reproduced in the text supplied.
- **Missing fact:** Whether the HPT 1st-stage disk serial number appears in Appendix A, Table 1 of the referenced NMSB is not shown; this decides whether paragraph (g)(1) or (g)(3)/(g)(5) applies.
- **Missing fact:** Whether the HPT 2nd-stage disk serial number appears in Appendix A, Table 2 of the referenced NMSB is not shown; this decides whether paragraph (g)(2) or (g)(4)/(g)(6) applies.
- **Missing fact:** No engine flight-cycle counter is recorded, so the 3,200-cycle limit cannot be computed.
- **Missing fact:** No engine event or shop-visit history is recorded, so whether a qualifying engine shop visit has occurred since 2021-07-13 is unknown.
- **Missing fact:** Appendix A serial lists of IAE NMSB V2500-ENG-72-0713 Rev 1 and the Figure 1 compliance table of AD 2022-02574 are not included in the supplied text.
- **Missing fact:** Operating history of each installed disk on high-thrust engines (V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2533-A5) is not recorded; under the superseding AD this determines the shortened compliance time.
- **Note:** Question date 2022-03-01 falls before the 2022-03-15 effective date of AD 2022-02-09, so AD 2021-11-15 is still in force on the question date; the superseding AD is published but not yet effective.
- **Note:** The engine record is synthetic and contains no flight-cycle counter, events, or qualifying shop visit information.
- **Note:** The disk serial numbers SYN-DISK1-0020 and SYN-DISK2-0020 have not been checked against any listing in the supplied text.
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
- **Summary:** Directive 2022-02-09 (FR document 2022-02574) takes effect March 15, 2022, after the 2022-03-01 question date, so it cannot require action yet. The V2533-A5 model is in scope and both installed disk part numbers (2A5001, 2A4802) match the directive, but Appendix A serial-number lists and the disks' prior engine operation are not in the record, so applicability cannot be confirmed.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015 Rev 1) is not supplied, so it cannot be confirmed whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed for P/N 2A5001.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015 Rev 1) is not supplied, so it cannot be confirmed whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed for P/N 2A4802.
- **Missing fact:** Whether the HPT 1st-stage disk has operated on a V2527E-A5, V2527M-A5, V2528-D5, V2530-A5 or V2533-A5 engine determines which compliance time in paragraph (g)(3) applies; the record does not state this.
- **Missing fact:** Whether the HPT 2nd-stage disk has operated on a high-thrust model engine determines which compliance time in paragraph (g)(4) applies; the record does not state this.
- **Missing fact:** The engine flight-cycle counter is not in the record, so no compliance deadline could be computed even if the directive were in force and applicable.
- **Missing fact:** The events list is empty. This is not evidence that no engine shop visit has occurred or that the disks were not removed; the next engine shop visit governs the compliance time under paragraphs (g)(1) and (g)(2).
- **Note:** Screening aid only. This output does not state compliance or noncompliance, airworthiness, or return-to-service status.
- **Note:** Authority state is published_not_yet_effective on 2022-03-01, so no action can be required until March 15, 2022. Once effective, the directive's applicability and timing must be rechecked.
- **Note:** Serial numbers in the record (SYN-DISK1-0020, SYN-DISK2-0020) are synthetic and cannot be checked against the Appendix A tables, which were not supplied.
- **Note:** Superseded AD 2021-11-15 (FR document 2021-11960) is not analyzed; it is replaced by this directive per paragraph (b).

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (FR 2022-02574) is in force and covers V2530-A5 engines with an HPT 1st-stage disk P/N 2A5001 or HPT 2nd-stage disk P/N 2A4802 whose serial number is listed in the NMSB appendix tables. Both installed disks match the listed part numbers, but the appendix serial lists and Figure 1 compliance times are not in the text provided, so applicability and the deadline cannot be determined.
- **Stated timing:** Under paragraph (g)(1) and (g)(2), the USI is due within the compliance time in Figure 1 to paragraph (g)(1), or within 10 flight cycles after March 15, 2022, whichever is later. Figure 1 was not supplied, so the due date cannot be stated. No engine shop visit is recorded in the events list.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (and NMSB V2500-E5-72-0015 Rev 1 if applicable) is not in the supplied text. Whether HPT 1st-stage disk serial SYN-DISK1-0021 is listed there is needed to decide applicability under paragraph (c)(1).
- **Missing fact:** Appendix A, Table 2 of the same NMSB documents is not in the supplied text. Whether HPT 2nd-stage disk serial SYN-DISK2-0021 is listed there is needed to decide applicability under paragraph (c)(2).
- **Missing fact:** Figure 1 to paragraph (g)(1) is an image that was not supplied. Its compliance time is needed to compute the USI due date for both disks.
- **Missing fact:** The engine record has no current engine flight-cycle counter. It is needed to compute the 10-flight-cycle floor and any cycle-based deadline.
- **Missing fact:** The events list is empty. The record does not show whether an engine shop visit has occurred since March 15, 2022, which would trigger the (g)(1) and (g)(2) inspection requirement.
- **Note:** Screening aid only, not a compliance determination. No ad_records or amoc_claims were supplied, so no operator AD status claim is evaluated.
- **Note:** The directive itself (paragraph (g)(1) and (g)(2)) reads the V2530-A5 as a high-thrust model, so the low-thrust paragraph (g)(3) and (g)(4) do not apply to this engine model.
- **Note:** The matched_parts entries match on part number only. Serial-number listing is unconfirmed because the appendix tables were not supplied.
- **Note:** The engine record has no flight cycle counter, disk operating history, or AMOC claims. None of these were assumed.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a supported V2533-A5 with an installed HPT 1st-stage disk P/N 2A5001, S/N PKLBSH1829, which is listed in paragraph (c)(1) of the directive, so the directive applies. The ultrasonic inspection of that disk was due within 10 flight cycles after the July 19, 2021 effective date, which by the engine cycle counter is 33010 flight cycles; the record shows no completed inspection, and the current count is 33004.
- **Stated timing:** Perform the ultrasonic inspection of the HPT 1st-stage disk within 10 flight cycles after the July 19, 2021 effective date, i.e. by engine flight cycle 33010, unless already done. If the disk does not pass the inspection, remove it before further flight.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** The record contains no ad_records entry or event showing that the USI of the HPT 1st-stage disk (IAE NMSB V2500-ENG-72-0713) was already performed. Whether the inspection is already done determines whether the action is still outstanding; a missing record is not evidence that it was not done.
- **Missing fact:** The installed HPT 2nd-stage disk serial SYN-DISK2-0022 does not appear in paragraph (c)(2)'s list (PKLBR87800, PKLBR88708, PKLBR89452, PKLBSA9907, PKLBSH9246, PKLBSC8066, PKLBSC8077, PKLBSG2213). On the record as given it does not match, but the screen relies on the serial as recorded, so confirm it.
- **Note:** This is a screening aid, not a compliance determination. The engine record shows 33000 cycles on 2021-07-19 and 33004 on 2021-07-20, leaving 6 cycles before the 33010 deadline if the inspection has not been done.
- **Note:** The engine model V2533-A5 is in the supported scope and is listed in the directive's applicability paragraph (c).
- **Note:** The HPT 2nd-stage disk serial SYN-DISK2-0022 is not in the list in paragraph (c)(2), so no second-stage match is reported. The inspection requirement for the first-stage disk is independent of that.
- **Note:** The record has no AMOC claims and no event records.
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
- **Summary:** The directive is in force (effective 2021-07-13) and covers V2533-A5 engines with listed HPT 1st- and 2nd-stage disks, but applicability cannot be decided because the record does not show whether serial numbers PKLBSH1829 and SYN-DISK2-0022 appear in the Appendix A Table 1 or Table 2 listings, which were not supplied. If listed, the first required action is due at the next engine shop visit or before 3,200 flight cycles accumulate since 2021-07-13, whichever occurs first; that count cannot be computed from the record.
- **Stated timing:** For each listed disk: at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first (paragraphs (g)(1) and (g)(2)). Not computable without the engine cycle count on 2021-07-13 and the Appendix A listings.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015) is needed to confirm whether HPT 1st-stage disk P/N 2A5001, S/N PKLBSH1829 is listed. Without it the applicability cannot be determined.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015) is needed to confirm whether HPT 2nd-stage disk P/N 2A4802, S/N SYN-DISK2-0022 is listed.
- **Missing fact:** Engine flight-cycle count on the effective date is needed to compute the 3,200-cycle limit counted from 2021-07-13. The record has readings only for 2021-07-19 and 2021-07-20.
- **Missing fact:** Cycles accumulated by this disk since 2021-07-13 are needed to determine the 3,200-cycle limit. No such field is recorded.
- **Missing fact:** Cycles accumulated by this disk since 2021-07-13 are needed to determine the 3,200-cycle limit. No such field is recorded.
- **Missing fact:** The record's events list is empty. Whether any engine shop visit has occurred since 2021-07-13 is not recorded, and this affects the timing of paragraphs (g)(1), (g)(2), (g)(5) and (g)(6).
- **Note:** Synthetic engine record. Screening aid only, not a compliance determination.
- **Note:** Engine model V2533-A5 is within the supported scope and is listed in the directive applicability paragraph (c).
- **Note:** The 3,200-cycle limit runs from the directive effective date, not from part installation. The record does not show cycles at the effective date, so the deadline cannot be computed.
- **Note:** The 6,700-cycle and HPT module removal alternatives in (g)(3) and (g)(4) apply only to V2522-A5, V2524-A5, V2525-D5, and V2527-A5, not to V2533-A5.
- **Note:** The events list is empty, so no engine shop visit is recorded for this directive.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)
- **Unresolved locator:** 2021-11960 (c) Applicability items (1) and (2)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527M-A5 is a supported model, and installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in Table 1 to paragraph (g) of AD 2025-19-13, so the hub must be removed at the next engine shop visit before it exceeds its 6,000-cycle removal limit. The 100-flight-cycle fallback from the effective date (engine cycle 20,100) has already passed, and no shop visit is recorded.
- **Stated timing:** Remove the listed HPT 2nd-stage hub at the next engine shop visit and before it exceeds 6,000 cycles since new (about engine flight cycle 25,000 on the current record). The fallback of 100 flight cycles after the 2025-10-29 effective date (engine cycle 20,100) has already passed with no removal recorded, so a reviewer should confirm the reading that applies.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The record gives cycles_since_new 3500 with no date, and the only dated reading is 1000 at 2025-10-29. The current hub cycles since new must be confirmed because it sets the remaining cycles and the 6,000-cycle removal deadline.
- **Missing fact:** No engine shop visit event is recorded. Whether and when the next shop visit occurs determines when the hub must be removed, so the event history must be confirmed.
- **Missing fact:** The installed HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0023) does not match any S/N in Table 1 on the record as given. Its P/N is listed, but the serial is not, so this hub is not matched. Confirm the serial number and any prior cycle history.
- **Missing fact:** The HPT 1st-stage hub has cycles_since_new 3500 with no date. This is not matched to a listed serial, but its serial should be confirmed.
- **Missing fact:** The record cites a maintenance program revision that incorporates table 1 of AD 2025-17-16. That is a different AD and does not show removal under AD 2025-19-13.
- **Missing fact:** The full text of AD 2025-17-16 is not supplied, so it is not assessed here.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** Table 1 lists the HPT 2nd-stage hub with serial PKLBSR2100, which matches the installed hub. The HPT 1st-stage hub with serial SYN-HUB1-0023 is not listed.
- **Note:** Hub cycles since new are inferred from the 1000-cycle reading at 2025-10-29 plus 2,500 engine cycles accrued through 2026-10-06, which gives 3,500 and agrees with the undated field. This assumes the hub accrues cycles one-for-one with the engine.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527M-A5 engine has a 3rd stage HPC rotor blade set recorded as P/N 6A8688, which is within this AD's applicability. The AD, effective 2026-09-24, requires replacing the full set of 3rd stage HPC rotor blades with parts eligible for installation at the next engine shop visit after that date where the blade is exposed; the record shows no such shop visit, so no action is triggered now.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline applies before that event.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record contains no engine shop visit event on or after 2026-09-24. Whether an induction into the shop for maintenance has occurred or is planned is not recorded, so the trigger cannot be confirmed either way. A missing record is not evidence that no shop visit occurred.
- **Missing fact:** The blade set serial number is recorded as not tracked at set level. Whether each installed blade carries an eligible P/N at the exposure point cannot be checked from the record, although the directive concerns the full set.
- **Note:** The directive is treated as in force because its effective date of 2026-09-24 precedes the 2026-10-06 question date.
- **Note:** The 2025-12-01 maintenance program revision cites AD 2025-17-16 table 1, which is a different AD. It does not bear on this directive and was not evaluated here.
- **Note:** No ad_records or amoc_claims were supplied, so no operator AD status or AMOC claim was assessed.
- **Note:** The HPT hub components are not listed in this directive and were not matched.
- **Note:** The engine is at 22500 flight cycles, but no cycle limit applies because the trigger is an event, not a cycle count.
- **Note:** This is a screening aid only and does not state compliance status or return-to-service status.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 is in force (effective 2025-10-10) and applies to this V2527M-A5 engine. The one-time ALS/TLM and air carrier program revision was due by 2026-01-08 and the record shows it was made on 2025-12-01, so no required action is triggered now; the piece-part inspections of the HPT stage 1 and stage 2 hubs are performed under other regulations at piece-part exposure.
- **Stated timing:** The paragraph (g)(1) TLM revision and paragraph (g)(2) air carrier program revision were due within 90 days after 2025-10-10, i.e., by 2026-01-08. The operator's record shows the revision on 2025-12-01. The hub inspections are required at piece-part exposure under the revised TLM.
- **Missing fact:** The record does not show the paragraph (g)(1) TLM revision as a separate entry (P/N 2A4408 TASK 05-10-00-990-000-B00, paragraph B.1). The single event describes the program and TLM revision, so the operator's assertion should be checked against the revised TLM and program pages.
- **Missing fact:** Whether any piece-part exposure or qualifying shop visit has occurred or will occur, which would make the HPT 1st-stage and 2nd-stage hub inspections (TASK 72-45-11-200-006 and TASK 72-45-31-200-009) due, is not in the record.
- **Missing fact:** The HPT 2nd-stage hub shows 3500 cycles since new at installation and 1000 cycles since new on 2025-10-29. These readings conflict and should be reconciled, since the hub's cycle history matters for piece-part exposure planning, though the directive sets no cycle limit.
- **Note:** This is a screening aid, not a compliance determination. The record's 2025-12-01 revision event is the operator's assertion and has not been verified against the revised TLM or program pages.
- **Note:** The 90-day deadline from the 2025-10-10 effective date is 2026-01-08. The record's revision date of 2025-12-01 falls within that window.
- **Note:** The directive does not set a cycle-based deadline or cycle limit for the hubs. The inspections are required at piece-part exposure under the revised TLM, so no cycle remaining figure is computed.
- **Note:** The engine's current flight-cycle counter is 22500 on 2026-10-06. The record's earlier reading of 20000 is dated 2025-10-29.
- **Note:** Both matched hubs list only part numbers in the directive, so listed serial numbers are null.
- **Note:** The 3rd stage HPC rotor blade set is not listed in the directive and was not matched.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 engine is a supported model within the directive's applicability, and the directive was effective October 29, 2025. Neither installed hub matches a P/N and S/N pair in Table 1 to paragraph (g), so no removal is triggered on the record as supplied, but the installation prohibition still applies.
- **Missing fact:** The recorded P/N 2A4802 is not confirmed. The S/N PKLBST5011 is listed in Table 1 only under P/N 2A5001 (1st-stage hub). If the P/N is wrong, the hub could be a listed part with a different removal limit, so the P/N should be verified against the physical part or its documentation.
- **Missing fact:** Engine shop visit history is not recorded (events is empty). Whether any shop visit occurred or will occur matters for the timing of the required action if either hub later matches Table 1.
- **Note:** The screen is not a compliance determination. Neither installed hub's P/N and S/N pair matches Table 1. The 2nd-stage hub's S/N PKLBST5011 appears in Table 1 only under P/N 2A5001, so the pair does not match.
- **Note:** Engine record shows no events, so no engine shop visit is recorded. The synthetic record identifiers are not evidence of part status beyond what is stated.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model recorded is a CFM56-5B4/3, which is not among the IAE V2500 models this screen supports, so no applicability determination is made against AD 2025-17-16 (Federal Register document 2025-17066).
- **Note:** The engine record lists model CFM56-5B4/3, which is outside the supported IAE V2500 model list for this screen; no applicability or compliance determination is made.
- **Note:** The installed_components and events lists are empty, and no AD records or AMOC claims are supplied.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a listed V2530-A5 with HPT 1st-stage hub P/N 2A5001, S/N PKLBST7489 installed, which is in Table 1 with a 6,200-cycle removal limit; the hub is at about 3,600 cycles since new, and removal is required at the next engine shop visit before that limit, or within 100 flight cycles of the 2025-10-29 effective date if that is later. The record shows the 100-cycle date (engine cycle 20,100) has already passed, so the reading that governs timing needs review.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29 and before it exceeds 6,200 cycles since new, or within 100 flight cycles of 2025-10-29 (engine cycle 20,100), whichever occurs later. No shop visit after the effective date appears in the record; the 100-cycle date has passed on the record's counters.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** The component's cycles-since-new value of 3,600 has no date. The dated reading of 3,000 at 2025-10-29 plus the 600 engine cycles since then is consistent with 3,600 as of 2026-03-01, but the current value should be confirmed, since the remaining-cycle figure depends on it.
- **Missing fact:** The record does not show whether any engine shop visit, as defined in paragraph (i)(2), has occurred or is scheduled since 2025-10-29. That event would set the removal date under paragraph (g), and the record lists none.
- **Missing fact:** The record does not show whether the engine's cycle counter and the hub's cycles-since-new move one-for-one. The calculation assumes they do, as the 600-cycle change in both readings suggests.
- **Note:** This is a screening aid and not a compliance determination. The record's AD status and any claims about the hub are not evidence that settles the outcome.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0026) does not match any Table 1 entry, so it is not an affected part on this record.
- **Note:** The 2024 blend repair and the 2024 repeat inspection do not change the table 1 match, which is by P/N and S/N. The record does not indicate whether the repair counts as a shop visit, but no shop visit after the effective date is recorded.
- **Note:** The engine's cycle counter was 20,000 on the effective date and 20,600 on 2026-03-01 per the record, so the record indicates the 100-cycle date has passed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBST7489, limit 6,200 cycles since new

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
- **Summary:** The screen indicates action is required. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in Table 1 with a 4,800-cycle removal limit, and the record shows 4,750 cycles since new, leaving about 50 cycles. The hub must be removed at the next engine shop visit before the limit is exceeded. The 100-flight-cycle alternative (about engine cycle 15,100) has already passed, and the operator's claimed 5,300-cycle AMOC has no FAA approval on file, so it cannot be relied on.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 4,800 cycles since new. The 100-flight-cycle alternative date (about 15,100 engine flight cycles) has already passed. Based on the current 1:1 cycle relationship, the cycle-based limit falls at about 15,300 engine flight cycles.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** No engine shop visit history is recorded. Whether a shop visit has occurred or is scheduled determines when the paragraph (g) removal must be performed, so the event record is needed to confirm timing.
- **Missing fact:** The 4,750 CSN value has no date stamp. The 4,800-cycle limit margin of 50 cycles depends on this value being current as of the 2026-01-20 snapshot.
- **Missing fact:** The AMOC approval reference is unknown and no FAA approval letter is on file. Without an approved AMOC, the 4,800-cycle limit in Table 1 governs.
- **Note:** This is a screening aid, not a compliance determination. The cycle-based deadline assumes engine flight cycles and the hub's cycles since new accumulate one-for-one, which the record's readings support (250 cycles on each between 2025-10-29 and 2026-01-20).
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0027) does not match any Table 1 serial number, so it is not matched. Confirm the serial number against the table, since a transcription error would change the result.
- **Note:** No amoc_claims approval is on file. The operator's planning record is a claim to check, not evidence that a 5,300-cycle limit applies.
- **Unresolved locator:** 2025-18469 (g) Table 1 row: HPT 1st-stage hub, 2A5001, PKLBSS9200, 4,800 cycles

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (Federal Register document 2025-18469, effective 2025-10-29) is in force on the question date. The installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) matches a listed P/N and S/N with a 4,000-cycle removal limit, so removal and replacement is required at the next engine shop visit before that limit is exceeded (about engine cycle 11,000), or within 100 flight cycles of the effective date, whichever occurs later. The operator's N/A marking conflicts with the record and cannot settle the outcome.
- **Stated timing:** Remove and replace the HPT 2nd-stage hub at the next engine shop visit after 2025-10-29 and before the hub exceeds 4,000 cycles since new, or within 100 flight cycles from the effective date, whichever occurs later. No shop visit is recorded, so the latest engine flight cycle is about 11,000.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** No engine events are recorded, so it is unknown whether a shop visit has occurred or will occur after 2025-10-29. The timing of the required removal depends on this.
- **Missing fact:** The current cycles_since_new value of 1400 is undated. It is assumed to be the 2026-02-10 value, consistent with the dated reading of 1000 on 2025-10-29 and 400 engine cycles since. The date should be confirmed because the remaining-cycles figure depends on it.
- **Missing fact:** The operator's recorded status of not_applicable with the note 'no affected hubs installed' conflicts with the installed HPT 2nd-stage hub, which matches table 1 of the AD. This claim needs to be checked and corrected against the record.
- **Note:** This is a screening aid, not a compliance determination. The 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0028) is not listed in table 1 by serial number, so it does not match on this record. Its S/N is not in the table and it is not treated as affected.
- **Note:** The 2nd-stage hub was installed 2025-06-03, before the effective date, so the installation prohibition in (h) is not triggered by that installation. Any future installation of the listed hub would be prohibited.
- **Note:** The record has an operator AD status claim (not_applicable) that conflicts with the matched part. It was checked and not used to settle the outcome.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), row HPT 2nd-stage hub 2A4802 / PKLBST5005, limit 4,000 cycles

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2025-18469 is in force (effective 2025-10-29) and covers the V2525-D5. The installed HPT 1st-stage hub S/N PKLBSK9287 matches a listed serial, with P/N 2A5001-01 that appears to be listed P/N 2A5001. Its 2400 cycles since new exceed the 100-cycle removal limit, so removal would be urgent if the match is confirmed, but the P/N suffix and the engine flight-cycle count at 2025-10-29 must be confirmed before a deadline can be fixed.
- **Stated timing:** If the hub is confirmed as listed, removal is due at the later of the next engine shop visit after 2025-10-29 and 100 flight cycles after 2025-10-29. The hub's removal limit of 100 cycles since new has already been passed, so the 100-flight-cycle window after the effective date is the operative limit.
- **Missing fact:** The installed hub is recorded as P/N 2A5001-01, while the directive lists P/N 2A5001. Whether the -01 suffix is the listed part number determines whether this hub is covered by table 1 to paragraph (g).
- **Missing fact:** The engine flight-cycle counter on the directive effective date is not in the record. It is needed to compute the 100-flight-cycle deadline in paragraph (g).
- **Missing fact:** The record contains no engine shop visit events. Whether and when the next engine shop visit occurs after 2025-10-29 determines the other half of the paragraph (g) deadline.
- **Note:** This is a screening aid, not a compliance determination. The HPT 2nd-stage hub S/N SYN-HUB2-0029 is not in table 1 and is not treated as affected, although its P/N 2A4802 is a listed P/N.
- **Note:** The HPT 1st-stage hub's 2400 cycles since new far exceed the 100-cycle limit listed for its serial, so confirming the P/N match is urgent.
- **Note:** The directive's effective date is 2025-10-29, and the question date is 2026-02-01, so the directive is in force on the question date.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSK9287, limit 100 cycles

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
