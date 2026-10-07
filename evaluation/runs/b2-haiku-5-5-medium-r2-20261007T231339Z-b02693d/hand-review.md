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
- **Summary:** The V2527-A5 engine is a supported model within the directive's applicability, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) is listed in Table 1 to paragraph (g). The hub has 3100 cycles since new against a 5,500-cycle removal limit, so removal is required at the next engine shop visit before that limit is reached, which is about 2,400 cycles away.
- **Stated timing:** Remove and replace the listed HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 5,500 cycles since new, whichever is later under paragraph (g). No shop visit is recorded. The hub-cycle limit is reached at about engine flight cycle 45,050 if hub and engine cycles accrue together. The 100-flight-cycle alternative ended at engine flight cycle 41,300, before the snapshot.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** The current 3,100 cycles-since-new value has no reading date. It is consistent with the dated 1,650 reading at 2025-10-29 plus the 1,450 engine cycles since then, but the hub count should be confirmed as of the question date to fix the remaining-cycle figure.
- **Missing fact:** Whether the engine will undergo an engine shop visit (induction with separation of major mating H-P flanges, not excepted under paragraph (i)(2)) before the hub reaches 5,500 cycles is not in the record. This determines when the removal must occur.
- **Note:** This is a screening aid and not a compliance determination. It does not state that the engine or any part is compliant or noncompliant, or approved for return to service.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0001) matches the listed part number but its serial number is not in Table 1, so it is not an affected hub on the supplied facts.
- **Note:** The 2025-10764 NPRM was superseded by the final rule 2025-18469 and is not relied on.
- **Note:** The engine and hub cycle counts both rose by 1,450 between 2025-10-29 and 2026-09-26, which supports a one-to-one projection for the 45,050 estimate.
- **Note:** No ad_records or AMOC claims were supplied, so no operator status or alternative method is evaluated.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row for 2A5001 / PKLBST5011, limit 5,500 cycles since new

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 engine is within the applicability of AD 2025-19-13 (Federal Register document 2025-18469), which took effect October 29, 2025. Neither installed hub matches a P/N and S/N listed in Table 1 to paragraph (g), so no removal is triggered on the record as given, but the installation prohibition in paragraph (h) continues to bind.
- **Note:** The installed HPT 1st-stage hub serial PKLBST5012 is close to the listed serial PKLBST5011 (P/N 2A5001, 5,500-cycle limit). The two serials differ, so the installed hub is not treated as listed; a reviewer should confirm the serial against the hub's data plate or the maintenance release to rule out a transcription error.
- **Note:** The installed hubs show 4,200 cycles since new, which would be below the 5,500 limit for PKLBST5011 if that serial were the installed one; this is not used for the determination because the serial does not match.
- **Note:** The events list is empty. This is not evidence that no shop visit occurred, but no shop visit affects the outcome while no listed hub is installed.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub rows (2A5001 with PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489) and HPT 2nd-stage hub rows (2A4802 with PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100)

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 is a supported model within the directive's applicability, and the in-force AD (effective 2025-10-29) applies. The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) is not a listed serial number. The HPT 1st-stage hub's P/N 2A5001 is listed, but its serial number and cycles since new are unknown, so whether the removal requirement is triggered cannot be determined.
- **Stated timing:** For a 1st-stage hub that is listed in table 1 to paragraph (g), removal is required at the next engine shop visit after 2025-10-29 before exceeding its listed removal cycle limit, or within 100 flight cycles of 2025-10-29, whichever occurs later. The applicable limit depends on the hub serial number, which is not recorded.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub is unknown. Table 1 lists four 2A5001 serial numbers with removal limits from 100 to 6,200 cycles, so the hub cannot be matched or cleared without its S/N.
- **Missing fact:** The cycles since new of the HPT 1st-stage hub are unknown. These are needed to compare against the listed removal cycle limit once the serial number is known.
- **Missing fact:** The engine flight-cycle counter is not in the record. It is needed to compute the 100-flight-cycle window from 2025-10-29 and any latest-cycle deadline.
- **Missing fact:** The events list is empty, so no engine shop visit history is recorded. Whether a shop visit has occurred since 2025-10-29, which would have triggered removal, cannot be determined.
- **Note:** This is a screening aid, not a compliance determination. The 2nd-stage hub (S/N SYN-HUB2-0003, 5,100 cycles) does not match any table 1 2A4802 serial number, so it is not identified as an affected part. Its cycle count was not compared against any limit.
- **Note:** The 1st-stage hub P/N 2A5001 is a P/N-level match only, so it is not recorded as a matched part. Matching requires its serial number.
- **Note:** The events list is empty. No shop visit is recorded, but that is not evidence that none occurred.
- **Note:** Because the 100-flight-cycle window from 2025-10-29 runs independently of the shop-visit trigger, the reviewer should confirm the engine's cycle count since 2025-10-29 and whether the 1st-stage hub is a listed serial number. If it is, the required action may already be due.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub rows (P/N 2A5001) and HPT 2nd-stage hub rows (P/N 2A4802)

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not an IAE V2500 model supported by this screen, so no applicability determination is made under Federal Register document 2025-18469.
- **Note:** The engine record shows engine_model PW1133G-JM with no installed components and no events; this is outside the supported V2500 model list, so no applicability determination was made.
- **Note:** The directive itself is in force with an effective date of October 29, 2025, but that does not affect the scope decision for this engine model.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is listed and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSS9840) matches Table 1 of the AD, which is in force since 2025-10-29. The operator record asserts that the 2025-11-12 shop induction qualifies as an engine shop visit, so the removal requirement is triggered at that event, with the latest engine flight-cycle count being 18100.
- **Stated timing:** At the next engine shop visit after 2025-10-29, which the record places on 2025-11-12, remove the listed hub and replace it with an eligible part, and do so before exceeding its 3,900-cycle removal limit or within 100 flight cycles of the effective date (by engine cycle 18100), whichever occurs later.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The current cycles-since-new (1040) is undated; the only dated reading is 1000 at 2025-10-29. The remaining-cycle figure depends on this value being current at the snapshot.
- **Missing fact:** The record does not show whether the listed hub was removed and replaced during the 2025-11-12 shop visit. The screen cannot tell whether the required action has been completed, and it does not make a compliance determination.
- **Missing fact:** The qualifying shop visit determination ('yes') is an operator assertion, and the event source note says it was asserted by the synthetic operator record. The removal trigger depends on this determination.
- **Note:** This is a screening aid and not a compliance determination.
- **Note:** The HPT 1st-stage hub recorded with S/N SYN-HUB1-0005 does not appear in Table 1 to paragraph (g), so it does not match a listed part. This is not evidence of eligibility beyond the table itself.
- **Note:** The engine cycle counter was 18000 on 2025-10-29 (effective date) and 18040 on 2025-11-12, so the 100-cycle floor is counted from 18000 to 18100.
- **Note:** Once a listed hub is removed and replaced, the installation prohibition in paragraph (h) continues to apply; the FAA's comment responses in the final rule state that removal does not make the AD inapplicable.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row P/N 2A4802, S/N PKLBSS9840, removal cycle limit 3,900

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and applies to V2530-A5 engines. The installed HPT 1st-stage hub P/N 2A5001, S/N PKLBSK9287 is listed in Table 1 with a 100-cycle removal limit; the record shows 90 cycles since new, so removal is required at the next engine shop visit before the limit is exceeded or within 100 flight cycles of the effective date, whichever is later.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 100 cycles since new, or within 100 flight cycles of the 2025-10-29 effective date (engine cycles 25500 plus 100), whichever occurs later; the record has no shop visit scheduled.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** The current cycles-since-new value of 90 is undated, while the only dated reading (2025-10-29) is 60, which conflicts with 90 at installation on 2025-09-30. The current count is needed to compute the remaining cycles and the removal deadline.
- **Missing fact:** The event list is empty, so it is unknown whether any engine shop visit has occurred or is scheduled after 2025-10-29, which determines when removal is triggered.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0006) is not listed in Table 1, so it is not matched by this screen.
- **Note:** The engine is a V2530-A5, which is within the supported scope.
- **Note:** The engine flight-cycle reading of 25500 on 2025-10-29 is taken as the effective-date count for the 100-flight-cycle window.
- **Unresolved locator:** 2025-18469 (g) Table 1 row: HPT 1st-stage hub, 2A5001, PKLBSK9287, limit 100 cycles

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine has an installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) listed in Table 1 of AD 2025-19-13, which must be removed at the next engine shop visit before exceeding its 4,800-cycle removal limit, or within 100 flight cycles of the 2025-10-29 effective date, whichever is later. The hub has 500 cycles remaining, so on the primary reading the removal is due by engine cycle 30,800. The HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) is also listed, with 1,700 cycles remaining against a 4,000-cycle limit.
- **Stated timing:** Remove the HPT 1st-stage hub at the next engine shop visit before it exceeds 4,800 cycles since new, or within 100 flight cycles of 2025-10-29, whichever occurs later. On the primary reading this is before engine cycle 30,800. Under the alternative reading that the 100-cycle window controls, the deadline was engine cycle 30,100 and has passed.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** The 4,300 cycles-since-new figure for the HPT 1st-stage hub is undated, so it is not confirmed as current on 2025-12-01. The remaining-cycle and deadline calculations depend on it.
- **Missing fact:** No events are recorded, so it is unknown whether an engine shop visit is scheduled or has occurred. The removal timing depends on when the next shop visit occurs relative to the 4,800-cycle limit.
- **Note:** This is a screening aid and not a compliance determination. It does not state whether the engine or any part is compliant, airworthy, or approved for return to service.
- **Note:** Cycle figures are taken from the engine record. The 1st-stage hub's engine-cycle deadline assumes its cycles-since-new accumulate one-for-one with engine flight cycles, as the record readings show (4,000 at engine 30,000; 4,300 at engine 30,300).
- **Note:** Installation dates (2021-05-11 and 2023-02-20) precede the effective date, so the installation prohibition in paragraph (h) is not triggered by the recorded installations.
- **Note:** The HPT 2nd-stage hub has 1,700 cycles remaining, so the 1st-stage hub is the binding component (smallest remaining).
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), rows for P/N 2A5001 S/N PKLBSS9200 (limit 4,800) and P/N 2A4802 S/N PKLBST5005 (limit 4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) matches a row of Table 1 to paragraph (g) of AD 2025-18469, which is in force since 2025-10-29, so the AD applies to this V2528-D5 engine. The required removal is due at the next engine shop visit before the hub exceeds its 6,200 cycles-since-new limit, or within 100 flight cycles of the effective date, whichever occurs later; the record shows no shop visit, and the 100-cycle window ended at engine cycle 50100 while the engine is at 50500.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the HPT 1st-stage hub exceeds 6,200 cycles since new, or within 100 flight cycles of 2025-10-29 (engine cycle 50100), whichever occurs later. The record shows no shop visit, so the shop-visit condition governs, and the 100-cycle figure is already past.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The serial number of the installed HPT 2nd-stage hub is unknown. Its P/N 2A4802 is listed in Table 1, so whether it is an affected hub cannot be decided until the S/N is known.
- **Missing fact:** Cycles since new for the HPT 2nd-stage hub are unknown. If its S/N matches a Table 1 row, the removal cycle limit (3,900 to 6,000 depending on S/N) could not be checked without this value.
- **Missing fact:** The record shows 2,500 cycles since new without a date, and 2,000 at 2025-10-29. Both values cannot describe the same date, and the hub's current cycles since new drives the remaining-cycles figure and the shop-visit deadline. The 2,500 value was used as current.
- **Missing fact:** No events are recorded, so it is unknown whether an engine shop visit has occurred since 2025-10-29. Any shop visit after that date would start the removal obligation under paragraph (g).
- **Missing fact:** Engine cycle readings are available only at 2025-10-29 and 2026-03-10. The cycle count at the time of any future shop visit cannot be known in advance.
- **Note:** This is a screening aid and not a compliance determination. The record is treated as the operator's claims and is not evidence that the engine is compliant or noncompliant.
- **Note:** The engine model V2528-D5 is within the supported scope.
- **Note:** Cycle arithmetic: the hub's cycles since new (2,500) are 3,700 below its 6,200 limit. The engine cycle count at which the hub reaches the limit, assuming one-for-one accumulation (as the 2025-10-29 readings suggest), is about 54,200.
- **Note:** The 2nd-stage hub P/N 2A4802 is listed, but its S/N is unknown, so the applicability of that part is not decided here.
- **Note:** The 2025-10764 NPRM was not relied on; the final rule 2025-18469 governs.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row, P/N 2A5001, S/N PKLBST7489, removal cycle limit 6,200

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a supported V2522-A5 model within the applicability of AD 2025-19-13 (Federal Register document 2025-18469), which took effect October 29, 2025. The engine record lists no installed components and no events, so it cannot be determined whether any HPT 1st-stage or 2nd-stage hub with a listed P/N and S/N is installed, and the required-action timing cannot be set.
- **Stated timing:** Under paragraph (g), for an engine with a listed hub, remove and replace the hub at the next engine shop visit after October 29, 2025 before exceeding the listed removal cycle limit, or within 100 flight cycles from October 29, 2025, whichever occurs later. The shop visit status and the engine cycle count at the effective date are not in the record.
- **Missing fact:** No record of the HPT 1st-stage hub installed on this engine. Its P/N and S/N must be checked against Table 1 to paragraph (g); an absent record is not evidence that no listed hub is installed.
- **Missing fact:** No record of the HPT 2nd-stage hub installed on this engine. Its P/N and S/N must be checked against Table 1 to paragraph (g).
- **Missing fact:** The engine's flight-cycle counter is not in the record, so the 100-flight-cycle window and any removal cycle limit cannot be computed.
- **Missing fact:** No event records are supplied. Whether a future engine shop visit occurs, and whether it meets the paragraph (i)(2) definition, determines when required action falls due.
- **Missing fact:** The engine's hub cycles since new are not in the record. These are needed to compare each listed hub against its removal cycle limit.
- **Note:** This is a screening aid, not a compliance determination. The engine is within the AD's applicability by model, but no hub records were supplied, so the action status is needs_review rather than a finding about any hub.
- **Note:** The record has an empty installed_components list and an empty events list. Under the record conventions, these gaps are not evidence that no listed hub is installed or that no shop visit has occurred.
- **Note:** The NPRM 2025-10764 was superseded by the final rule and is not relied on for the outcome.
- **Note:** The AD's compliance deadline is not a fixed date; it depends on the next engine shop visit after October 29, 2025 or 100 flight cycles after that date, whichever is later.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model V2500-A1 is not among the IAE V2500 models this screen supports, so no applicability determination is made against AD 2025-19-13 (Federal Register document 2025-18469).
- **Note:** The engine record lists model V2500-A1, which is not one of the supported models (V2522-A5, V2524-A5, V2525-D5, V2527-A5, V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2531-E5, V2533-A5). No applicability or compliance determination is made.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) appears in Table 1 of the directive, but that comparison is not an applicability finding for this engine model.
- **Note:** The directive took effect October 29, 2025, so it is in force on the question date of 2026-09-26.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (c) Applicability paragraph listing the supported V2500 models

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The engine is a supported V2527-A5 with 3rd stage HPC rotor blade P/N 6A8353 recorded as installed, and AD 2026-17-03 has been in force since its September 24, 2026 effective date. The directive requires replacement of the full blade set with parts eligible for installation at the next engine shop visit after that date where the 3rd stage HPC rotor blade is exposed; the record lists no events, so no such shop visit is recorded and no cycle or calendar deadline applies.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed (blade removed from the HPC stage 3 to 8 drum); no fixed deadline otherwise.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** The events list is empty. It does not establish whether any engine shop visit has occurred since September 24, 2026, or whether the 3rd stage HPC rotor blade was exposed during one. Whether the replacement trigger has occurred cannot be determined from the record.
- **Missing fact:** Operator confirmation of the engine shop visit history (induction dates and whether any induction after September 24, 2026 exposed the 3rd stage HPC rotor blade) is needed to know whether the required action has been triggered.
- **Note:** Authority state: AD 2026-17-03 (document 2026-16954) has an effective date of September 24, 2026, which precedes the question date of October 5, 2026, so it is in force. Correction 2026-18423 fixes paragraph (g) wording only and does not change the effective date.
- **Note:** The proposed rule 2025-20088 was superseded by the final rule and was not relied on for the deadline; the final rule's engine shop visit trigger governs.
- **Note:** The installed blade set's serial number is not tracked at set level. This does not affect applicability because the directive lists the part number only.
- **Note:** No ad_records or amoc_claims are present in the engine record, so there is no operator-asserted AD status or AMOC claim to check.
- **Note:** This is a screening aid and not a compliance determination. The engine's compliance status cannot be stated from this record.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** AD 2026-17-03 (Federal Register 2026-16954, effective September 24, 2026) is in force on the question date and covers V2533-A5 engines with 3rd stage HPC rotor blades P/N 6A8353 or 6A8688 installed. The record lists the installed 3rd stage HPC rotor blade set as P/N 6C8368, which is a part eligible for installation under the AD and is not a listed P/N, so the screen does not place this engine within the applicability as recorded. This is a screening aid, not a compliance determination.
- **Missing fact:** The record gives the blade set at set level as P/N 6C8368 and states serial numbers are not tracked at set level. Confirmation that every 3rd stage HPC rotor blade in the set is P/N 6C8368 (and not 6A8353 or 6A8688) would firmly settle applicability; the set-level entry alone does not show each blade's P/N.
- **Missing fact:** The events list is empty. No engine shop visit or 3rd stage HPC rotor blade exposure is recorded. If a future shop visit exposes the blades and any blade is 6A8353 or 6A8688, the AD's required action would need to be reassessed.
- **Note:** Engine model V2533-A5 is within the supported scope.
- **Note:** The AD is in force, with effective date September 24, 2026, and the question date is October 5, 2026.
- **Note:** The applicability screen rests on the set-level P/N 6C8368 entry. Individual blade P/Ns are not tracked, so a mixed set cannot be ruled out from the record alone.
- **Note:** The operator's records were not treated as evidence of compliance or of AD status.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC rotor blade P/N 6A8688 installed, which is within the directive's applicability. The record's shop visit induction (2026-09-14) predates the AD's effective date (2026-09-24), so paragraph (g) is not triggered by that visit, even though a blade exposure is recorded on 2026-09-30.
- **Stated timing:** Paragraph (g) applies at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed; the recorded 2026-09-14 induction is before that date.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Confirmation that the 2026-09-14 induction is the engine shop visit the operator reports, and whether the engine remains in that visit. The operator's qualifies_as_engine_shop_visit flag is an assertion, and the induction date determines whether paragraph (g) is triggered.
- **Missing fact:** Set-level serial number is not tracked, so blade-level identification for the removed blade is not available in the record. This does not change the part-number match but limits traceability of the exposed blade.
- **Note:** The induction (2026-09-14) is before the effective date (2026-09-24), so the paragraph (g) trigger has not occurred on this record. The blade exposure recorded on 2026-09-30 falls after the effective date but occurred during the pre-effective-date visit, so it is not a new shop visit under paragraph (g).
- **Note:** If the engine is inducted into a new shop visit on or after 2026-09-24 with a 3rd stage HPC rotor blade exposure, replacement of the full blade set with parts eligible for installation would be required at that visit.
- **Note:** Under the FAA's preamble, the intent is that engines already inducted before the effective date are not required to comply.
- **Note:** The operator's qualifies_as_engine_shop_visit flag is an assertion and was not independently verified.
- **Note:** Engine flight-cycle counter is not in the record, so no cycle-based deadline can be computed.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2026-17-03 applies to this V2524-A5 because the record lists 3rd stage HPC rotor blade P/N 6A8353, and the directive is in force. The 2026-10-01 shop visit is after the 2026-09-24 effective date, but the 2026-10-02 event records that no 3rd stage blade was removed from the stage 3-8 drum, so the directive's defined blade exposure has not occurred and no replacement is triggered on this record.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** The blade set serial number is not tracked at set level, so the serial cannot be compared with any listed serial. The directive lists the part number only, so this does not change the applicability finding, but the record does not identify individual blades.
- **Missing fact:** The engine flight-cycle counter is not in the record. It would be needed to express any future deadline in cycles, for example if a later shop visit exposes the blades.
- **Note:** This is a screening aid, not a compliance determination. The record does not establish compliance or noncompliance, airworthiness, or return-to-service status.
- **Note:** Interpretive note: paragraph (g) uses the phrase 'the 3rd stage HPC rotor blade is exposed', but the defined term in (h)(2) is blade removal from the stage 3-8 drum. The 2026-10-02 entry says the rotor was exposed for inspection with no blade removed, so the defined term controls here. If a reviewer reads rotor exposure alone as exposure, the replacement requirement would already be due at the closed 2026-10-01 shop visit. That reading cannot be given a cycle count because the record has no flight-cycle counter, so it is not listed as an alternative reading.
- **Note:** The shop visit qualification of 'yes' for AD 2026-17-03 is the operator's assertion and is consistent with the directive's definition in (h)(3).
- **Note:** The record does not state whether any blades were removed during the 2026-10-01 visit apart from the 2026-10-02 exposure entry. A reviewer should confirm that no 3rd stage blade was removed from the drum at any point in that visit.
- **Note:** Operator records are claims to check, not evidence that settles the outcome. No AMOC claims are recorded.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** This is a proposed rule (NPRM) with no effective date, so it cannot require action on 2026-01-15. The V2527E-A5 is a supported model and the installed 3rd stage HPC rotor blade set is listed as P/N 6A8353, which falls within the proposed applicability, but no blade exposure event is recorded.
- **Missing fact:** The directive is a proposal published 2025-11-18 with no effective date; it becomes a requirement only if adopted as a final rule. The required action is tied to the next 3rd stage HPC rotor blade exposure after that effective date, which cannot be determined from the record.
- **Missing fact:** Serial number is not tracked at set level, so individual blade P/Ns (6A8353 or 6A8688) and any blade-level identification cannot be confirmed against the proposed applicability and definitions.
- **Missing fact:** The events list is empty. No 3rd stage HPC rotor blade exposure (removal from the HPC stage 3 to 8 drum) is recorded, and future exposure events would determine when the proposed replacement would apply.
- **Note:** This is a screening aid, not a compliance determination. The answer reflects only the proposed rule text as of the question date and does not establish any final AD status.
- **Note:** If the rule is adopted as a final rule with a later effective date, the applicability and action analysis must be rerun against the then-current text and the engine record, including any blade exposure events.
- **Note:** The record lists the blade set P/N as 6A8353 without serial tracking; a reviewer should confirm the individual blade part numbers if the rule is later adopted.
- **Unresolved locator:** 2025-20088 preamble Dates and Effective date record

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527-A5 engine is within AD 2025-17-16's applicability, and the directive is in force (effective 2025-10-10). The operator's record says neither its approved program nor paragraph B.1 of the V2500-A5 TLM ALS yet incorporates table 1 to paragraph (g), so the one-time revisions due within 90 days of the effective date (by 2026-01-08) remain to be done.
- **Stated timing:** Within 90 days after the 2025-10-10 effective date, i.e., by 2026-01-08. The deadline is calendar-based, not flight-cycle based.
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** No installed component records are supplied, so it cannot be determined whether an HPT Stage 1 hub (P/N 2A5001) is installed. This does not change the required ALS and maintenance program revisions, but it bears on when the piece-part inspection tasks would apply.
- **Missing fact:** No installed component records are supplied, so it cannot be determined whether an HPT Stage 2 hub (P/N 2A4802) is installed. This does not change the required revisions, but it bears on when the piece-part inspection tasks would apply.
- **Note:** This is a screening aid, not a compliance determination. The status described here comes from the operator's own record, which states the required revisions are not yet incorporated.
- **Note:** The governing document is the final rule 2025-17066, which is in force on 2025-11-15. The 2024-26092 NPRM was not relied on; the final rule's text controls.
- **Note:** The 90-day period runs from the 2025-10-10 effective date, not from the 2025-09-05 publication date. Counting from publication would give an earlier, incorrect date of 2025-12-04.
- **Note:** No installed components or events are recorded, so no HPT hub serial or cycle data is available. The directive's deadline here is calendar-based, so no flight-cycle deadline or component cycles remaining can be computed.
- **Note:** The directive's piece-part inspection tasks are performed under other regulations once the ALS and program are revised; the record does not show any shop visit or piece-part exposure event.
- **Unresolved locator:** 2025-17066 preamble Discussion of comments: responses on paragraph (g) and piece-part exposure

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model V2522-A5 is within the applicability of AD 2025-17-16, which took effect October 10, 2025. The required revision of the airworthiness limitations section (ALS) of the Time Limits Manual, and for air carrier operations the approved maintenance program, is due within 90 days of the effective date, by January 8, 2026; this is a time-based action, not a cycle-based one.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e., by January 8, 2026: revise paragraph B.1 of the Maintenance Scheduling section of the ALS in the applicable TLM (g)(1); for air carrier operations, also revise the existing approved maintenance or inspection program (g)(2).
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the operator conducts air carrier operations is unknown. This determines whether the paragraph (g)(2) revision of the existing approved maintenance or inspection program applies in addition to the paragraph (g)(1) TLM ALS revision.
- **Missing fact:** No installed component records are present, so it cannot be confirmed whether the engine has an HPT Stage 1 hub P/N 2A5001 or an HPT Stage 2 hub P/N 2A4802. These part numbers matter for the listed inspections at piece-part exposure, though not for the ALS revision itself.
- **Missing fact:** The current content of the operator's TLM ALS and maintenance program, and whether TASK 72-45-11-200-006 and TASK 72-45-31-200-009 are already incorporated, are not in the engine record and were not provided.
- **Note:** This is a screening aid, not a compliance determination. The record contains no installed components, no events, and no ad_records or AMOC claims, so no compliance status is inferred.
- **Note:** The 90-day deadline is calculated from the October 10, 2025 effective date and is not tied to engine flight cycles.
- **Note:** The engine record is synthetic (SYN- identifiers). The applicability result rests on the engine model alone.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2525-D5 is supported and listed in the AD, and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) matches a Table 1 row with a 6,000-cycle removal limit, leaving 5,010 cycles. The final rule is not effective until October 29, 2025, so it cannot require action on the question date of October 15, 2025; the removal obligation applies at the next engine shop visit after that date or within 100 flight cycles of it, whichever is later.
- **Stated timing:** Not yet in force on 2025-10-15. Once effective on 2025-10-29, remove the listed hub at the next engine shop visit after the effective date before exceeding the removal cycle limit, or within 100 flight cycles from the effective date, whichever occurs later.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine's current flight-cycle counter is not in the record, so the latest engine flight-cycle count for the shop-visit deadline and the 100-cycle window cannot be computed.
- **Missing fact:** Shop visit history is not recorded (events is empty). Whether an engine shop visit has occurred or is scheduled after 2025-10-29 determines when the removal is due.
- **Note:** The installed 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0018) does not match any Table 1 serial number, so the record shows no match for that hub; this is not evidence that it is unaffected for other reasons.
- **Note:** Because the AD is not yet effective, no action is required on the question date; the obligations described become binding on 2025-10-29.
- **Note:** The engine record has no flight-cycle counter, so no engine-cycle deadline could be computed.
- **Note:** The 2025-10764 NPRM was superseded by the final rule 2025-18469 and was not used to set the outcome.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row for 2A4802 / PKLBSR2100 (limit 6,000 cycles)

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (effective 2025-10-29) applies to this V2531-E5 engine, which has an HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) listed in Table 1 with a 4,800-cycle removal limit. The hub's recorded 4,990 cycles since new already exceed that limit, so removal and replacement is required by the later of the 100-flight-cycle window from the effective date (engine cycle 60,100) or the next engine shop visit.
- **Stated timing:** Remove and replace the HPT 1st-stage hub with a part eligible for installation by the later of: 100 engine flight cycles after the 2025-10-29 effective date (engine flight cycle 60,100), or the next engine shop visit after the effective date. The hub is already past its 4,800-cycle limit, so the 'before exceeding' prong cannot be met and the 100-cycle window is the operative deadline unless a later shop visit occurs.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The 4,990 cycles-since-new value has no date. The only dated reading is 4,950 on 2025-10-29. The component-cycles-remaining figure of -190 assumes 4,990 is current; at the effective date the hub was 150 cycles past limit.
- **Missing fact:** The events list is empty, so there is no record of a next engine shop visit after the effective date. The timing depends on whether a shop visit occurs before or after engine cycle 60,100.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0019) does not match any serial in Table 1, so no action is triggered for it on this record.
- **Note:** The 2025-18469 AD's 100-flight-cycle window and shop-visit prong are read as stated in paragraph (g); reviewers should confirm the interpretation of 'whichever occurs later' against the FAA's intent.
- **Note:** Engine cycle readings: 60,000 on 2025-10-29 and 60,040 on 2025-11-05.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 1st-stage hub row 2A5001 / PKLBSS9200, limit 4,800 cycles

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** Directive 2021-11-15 (Federal Register 2021-11960) is in force on 2022-03-01 and covers IAE V2533-A5 engines with listed HPT 1st- and 2nd-stage disks. The engine's installed disk part numbers match, but applicability cannot be confirmed because the Appendix A serial-number tables are not in the supplied text and the record has no engine cycle counter or shop-visit history.
- **Stated timing:** For V2533-A5 engines, the HPT 1st-stage disk (g)(1) and HPT 2nd-stage disk (g)(2) USI is due at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 FCs since July 13, 2021, whichever occurs first. No shop visit is recorded, so the trigger cannot yet be dated.
- **Missing fact:** Appendix A, Table 1 (HPT 1st-stage disk S/N) and Table 2 (HPT 2nd-stage disk S/N) of IAE NMSB V2500-ENG-72-0713 Revision 1 are not in the supplied text. Without them, it cannot be confirmed whether SYN-DISK1-0020 or SYN-DISK2-0020 is a listed serial number, which determines applicability.
- **Missing fact:** Engine flight-cycle counter is absent. It is needed to compute the 3,200 FC limit from July 13, 2021.
- **Missing fact:** Flight cycles accumulated by the HPT 1st-stage disk since July 13, 2021 are absent. They are needed to compute the 3,200 FC limit.
- **Missing fact:** Flight cycles accumulated by the HPT 2nd-stage disk since July 13, 2021 are absent. They are needed to compute the 3,200 FC limit.
- **Missing fact:** No engine events are recorded. Whether any engine shop visit has occurred since July 13, 2021 is unknown, and that determines whether the shop-visit trigger has already been met.
- **Missing fact:** No operator AD status record for 2021-11-15 is present, so the operator's recorded status cannot be checked against the directive.
- **Missing fact:** Whether the disk has operated in a high-thrust model engine is unknown. This matters for the superseding AD 2022-02-09, which takes effect 2022-03-15.
- **Note:** Question date is 2022-03-01. AD 2021-11-15 (2021-11960) is in force; the superseding AD 2022-02-09 (2022-02574) is published but effective March 15, 2022, so it cannot require action yet. The superseding AD adds shortened compliance times for disks previously operated on high-thrust engines such as V2533-A5. Under the superseding AD, V2533-A5 compliance is governed by its Figure 1 time or 10 FCs after March 15, 2022, whichever is later; Figure 1 is not in the supplied text, so no deadline can be computed from it.
- **Note:** Part numbers 2A5001 and 2A4802 match the listed disk part numbers. Serial-number matching is not possible from the supplied text because the Appendix A tables are absent, so no matched_parts entry is recorded.
- **Note:** The engine record holds no ad_records or amoc_claims, so there is no operator AD status or alternative method of compliance to check.
- **Note:** This is a screening aid only and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2021-11960 (g)(1) V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2533-A5 HPT 1st-stage disk row
- **Unresolved locator:** 2021-11960 (g)(2) V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2533-A5 HPT 2nd-stage disk row

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (FR 2022-02574) is a final rule effective March 15, 2022, so on the 2022-03-01 question date it cannot yet require action. The V2533-A5 engine is a supported model and both installed disk part numbers (2A5001 and 2A4802) match the directive, but the disk serial numbers are not shown to be listed in Appendix A, so applicability cannot be decided from the record.
- **Stated timing:** Not in force until March 15, 2022. Once effective, the USI compliance time depends on the Figure 1 table (not supplied) and on whether each disk has operated in a high-thrust engine, so no deadline can be stated now.
- **Missing fact:** Whether serial number SYN-DISK1-0020 is listed in Appendix A, Table 1, of the referenced IAE NMSB documents. The Appendix A tables are not in the supplied text, so applicability of paragraph (c)(1) cannot be confirmed.
- **Missing fact:** Whether serial number SYN-DISK2-0020 is listed in Appendix A, Table 2, of the referenced IAE NMSB documents. The Appendix A tables are not in the supplied text, so applicability of paragraph (c)(2) cannot be confirmed.
- **Missing fact:** Appendix A Tables 1 and 2 of IAE NMSB V2500-ENG-72-0713 Revision 1 and IAE NMSB V2500-E5-72-0015 Revision 1, which list the eligible disk serial numbers, were not supplied.
- **Missing fact:** Figure 1 and Figure 2 to paragraph (g) (compliance time tables) were not included in the supplied text, so the USI due point cannot be computed.
- **Missing fact:** Operating history of each disk: whether either disk has operated in a V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, or V2533-A5 engine. This determines which compliance path applies under paragraph (g)(3) or (g)(4) for low-thrust models, and the V2533-A5 is a high-thrust model under the directive.
- **Missing fact:** The event history is empty. Shop-visit history is needed to determine whether the next engine shop visit triggers the inspection under paragraphs (g)(1), (g)(2), (g)(5), or (g)(6).
- **Note:** This is a screening aid only and not a compliance determination. The directive is not yet effective on the question date, so no action can be required by it on 2022-03-01.
- **Note:** AD 2021-11-15 (FR 2021-11960, effective July 13, 2021) is still in force on the question date and is superseded by 2022-02574 effective March 15, 2022. A reviewer should check the 2021-11-15 requirements separately, since they may apply until March 15, 2022.
- **Note:** The engine record has no events and no ad_records or amoc_claims. The absence of records is not evidence that the disks are unaffected.
- **Note:** Serial numbers in the record are synthetic (SYN- prefix). The Appendix A tables that would confirm applicability were not supplied.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 is in force and covers V2530-A5 engines with an HPT 1st-stage disk P/N 2A5001 or HPT 2nd-stage disk P/N 2A4802 whose serial numbers appear in the NMSB Appendix A tables. The record's part numbers match, but the Appendix A serial lists and the Figure 1 compliance time were not supplied, and the record has no engine flight-cycle counter, so applicability and any deadline cannot be determined.
- **Stated timing:** Required USI of the HPT 1st-stage and 2nd-stage disks is due within the compliance time in Figure 1 to paragraph (g)(1), or within 10 flight cycles after March 15, 2022, whichever occurs later. Figure 1 was not included in the supplied text, so the due point cannot be stated.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015 Rev 1) is needed to confirm whether HPT 1st-stage disk S/N SYN-DISK1-0021 is listed. The directive applies only to listed serial numbers.
- **Missing fact:** Appendix A, Table 2 of the same NMSB is needed to confirm whether HPT 2nd-stage disk S/N SYN-DISK2-0021 is listed.
- **Missing fact:** Figure 1 to paragraph (g)(1) of AD 2022-02-09 is needed to determine the compliance time for the USI. The image was not included in the supplied text.
- **Missing fact:** The engine flight-cycle counter is not in the record. It is needed to compute the 10-flight-cycle floor after March 15, 2022 and any cycle-based compliance point.
- **Missing fact:** The events list is empty. The operator's record shows no engine shop visit, so it is unknown whether a shop visit has occurred that would trigger the Figure 1 compliance time.
- **Missing fact:** No operator AD status record for AD 2022-02-09 is present. Any recorded status is an operator claim and was not used.
- **Note:** Screening aid only. This output does not state that any engine or part is compliant or noncompliant, airworthy, or approved for return to service.
- **Note:** The engine model V2530-A5 is within the supported scope.
- **Note:** Both listed part numbers match the record. The applicability decision depends on the serial numbers appearing in the NMSB Appendix A tables, which were not supplied.
- **Note:** AD 2021-11-15 is superseded by AD 2022-02-09 and was not used for the deadline. Its 3,200-FC and next-shop-visit terms are not the operative terms for this engine.
- **Note:** The engine record has no flight-cycle counter and no ad_records entry, so no cycle-based deadline or operator-recorded status could be assessed.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine has an installed HPT 1st-stage disk (P/N 2A5001, S/N PKLBSH1829) that is listed in paragraph (c)(1), so the directive applies. The ultrasonic inspection of that disk is required within 10 flight cycles after the July 19, 2021 effective date, which is engine cycle 33010 on the record's reading; the engine was at 33004 on 2021-07-20, leaving 6 cycles. This is a screening result, not a compliance determination.
- **Stated timing:** Perform the ultrasonic inspection of the HPT 1st-stage disk within 10 flight cycles after the July 19, 2021 effective date (by engine flight cycle 33010 on the record's counting). If the disk does not pass the USI, remove it before further flight.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** No event records are supplied, so there is no record of whether the required ultrasonic inspection of the HPT 1st-stage disk has been performed or of its result. The USI status and result decide whether any further removal action applies.
- **Missing fact:** The HPT 2nd-stage disk (P/N 2A4802, S/N SYN-DISK2-0022) is not among the serial numbers listed in paragraph (c)(2), so it is not matched. Confirm the serial number against the directive's list before relying on that result. The Table 2 image in the Federal Register text was not provided and could not be checked.
- **Note:** Engine model V2533-A5 is within the supported scope and is listed in the directive applicability paragraph (c).
- **Note:** Engine cycle readings: 33000 on 2021-07-19 and 33004 on 2021-07-20. The deadline of 33010 is computed as 33000 plus 10 cycles.
- **Note:** The directive sets no component life limit, so component_cycles_remaining is null.
- **Note:** The directive is an interim action (urgent USI) and the root cause remains under investigation, so later FAA action may change these requirements.
- **Note:** No ad_records or amoc_claims were supplied, so the operator's recorded status for this AD is unknown.
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
- **Summary:** The directive is in force on 2021-07-20 and V2533-A5 is a supported model. Both installed disks match the directive's part numbers, but the applicability serial-number listings (Appendix A of the NMSB) were not supplied, and the cycle count at the 2021-07-13 effective date is missing, so the 3,200-cycle deadline cannot be computed.
- **Stated timing:** For the HPT 1st-stage disk (g)(1) and HPT 2nd-stage disk (g)(2): at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 FCs since 2021-07-13, whichever occurs first. No shop visit is recorded in the events list.
- **Missing fact:** Whether HPT 1st-stage disk serial PKLBSH1829 (P/N 2A5001) is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1 or V2500-E5-72-0015. The appendix is not in the supplied text, and this listing is required for applicability under (c)(1).
- **Missing fact:** Whether HPT 2nd-stage disk serial SYN-DISK2-0022 (P/N 2A4802) is listed in Appendix A, Table 2, of the same NMSB. This listing is required for applicability under (c)(2).
- **Missing fact:** Engine flight-cycle count on the 2021-07-13 effective date is missing. Cycles since the effective date, and therefore the 3,200-FC limit in (g)(1) and (g)(2), cannot be calculated from the readings supplied (only 2021-07-19 and 2021-07-20 are given).
- **Missing fact:** No shop-visit events are recorded. The events list is empty, which does not show that no engine shop visit has occurred since the effective date. Whether a shop visit has occurred determines the trigger under (g)(1) and (g)(2).
- **Note:** Screening aid only, not a compliance determination. The NMSB appendix serial lists are not in the supplied text, so the serial-number listing for both installed disks is unconfirmed.
- **Note:** The engine record is marked synthetic. Its serial numbers (PKLBSH1829 and SYN-DISK2-0022) cannot be checked against the directive text supplied.
- **Note:** Engine shop visit status is unknown. The empty events list is not evidence that no shop visit occurred.
- **Note:** Engine was at 33004 FCs on 2021-07-20; the effective-date cycle count is needed before any deadline can be stated.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527M-A5 is a supported model and the directive is in force. The installed HPT 2nd-stage hub P/N 2A4802, S/N PKLBSR2100 is listed in table 1 with a 6,000-cycle removal limit and shows 3,500 cycles since new, so it must be removed and replaced at the next engine shop visit after 2025-10-29 and before it exceeds 6,000 cycles since new.
- **Stated timing:** Remove and replace the listed HPT 2nd-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 6,000 cycles since new (engine flight cycle 25,000 on the current utilization). No shop visit is recorded since the effective date. The 100-flight-cycle alternative window from the effective date ended at engine flight cycle 20,100.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** Whether any engine shop visit (separation of major mating H-P flanges, not a transportation-only or on-wing field-maintenance exception) has occurred since 2025-10-29. A shop visit would have triggered removal of the listed hub, and the event list shows none.
- **Missing fact:** The top-level cycles_since_new of 3,500 is undated, while the only dated reading (2025-10-29) is 1,000. The 2,500-cycle difference matches engine utilization over the period, but a dated current reading would confirm the 2,500 remaining-cycle figure.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0023 does not match any serial in table 1, so no 1st-stage hub match was found on the record.
- **Note:** The maintenance program revision on 2025-12-01 cites AD 2025-17-16, a different directive. It is not an AMOC or compliance record for AD 2025-18469 and does not satisfy paragraph (g).
- **Note:** The 3rd stage HPC rotor blade set is not addressed by this directive.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row P/N 2A4802, S/N PKLBSR2100, removal cycle limit 6,000

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (Federal Register 2026-16954, corrected by 2026-18423) is in force as of its September 24, 2026 effective date. The record shows a V2527M-A5 engine with a 3rd stage HPC rotor blade set listed as P/N 6A8688, so the directive applies. Its replacement requirement is triggered only at the next engine shop visit after the effective date where the 3rd stage HPC rotor blade is exposed, and the record shows no such event.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed; no fixed calendar or cycle deadline applies otherwise.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record contains no engine shop visit event. Whether the engine has been inducted into a shop visit on or after 2026-09-24, and whether the 3rd stage HPC rotor blade was exposed at that visit, is not shown and determines whether the replacement is triggered.
- **Missing fact:** The blade set serial is recorded as not tracked at set level, so the individual blade serials and their eligibility cannot be confirmed from the record.
- **Note:** This is a screening aid, not a compliance determination. The record does not establish whether the engine is compliant or noncompliant with this AD.
- **Note:** The maintenance_program_revision event of 2025-12-01 cites AD 2025-17-16 table 1, which is a different directive and does not satisfy or reference AD 2026-17-03.
- **Note:** The engine record gives no cycles-since-new value for the 3rd stage blade set, and no component limit applies to this directive, so no cycle-based remaining figure is computed.
- **Note:** Under paragraph (h)(2), exposure means removal of any 3rd stage blade from the HPC stage 3 to 8 drum. Under paragraph (h)(3), an engine shop visit means induction into the shop for maintenance. Both definitions should be checked against shop records when the next event occurs.
- **Note:** The record's engine cycle readings (20000 on 2025-10-29 and 22500 on 2026-10-06) do not bear on the trigger, which is event-based.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 (effective 2025-10-10) applies to this V2527M-A5 engine, and its one-time ALS and maintenance-program revision was due by 2026-01-08. The record shows an operator-recorded revision dated 2025-12-01, within that window, so no further required action is triggered on this screen, though the continuing piece-part inspection obligations still bind.
- **Stated timing:** One-time revision due within 90 days after the 2025-10-10 effective date, i.e. by 2026-01-08. The record shows the revision dated 2025-12-01. The inspections themselves are performed at piece-part exposure under the revised TLM paragraph B.1.
- **Missing fact:** The record gives one operator-stated revision (Revision 48, 2025-12-01) covering both the TLM ALS paragraph B.1 revision under (g)(1) and the air-carrier program revision under (g)(2). Separate confirmation of each revision, with the table 1 tasks and P/N 2A4408 TLM reference, is not in the record; this is an operator claim to be checked, not confirmed evidence.
- **Missing fact:** No installation date is recorded for the HPT 1st-stage hub, so its service history and piece-part exposure timing cannot be traced from the record.
- **Missing fact:** Only a single cycles_since_new value (3500) is recorded for the HPT 1st-stage hub with no dated reading, so its current cycle count cannot be dated.
- **Missing fact:** The directive text sets no cycle limit for the HPT hubs, and the record does not state the engine manual's replacement or inspection thresholds, so no component cycle margin can be computed from this screen.
- **Note:** The screen is not a compliance determination. The 2025-12-01 revision is an operator-asserted record and is treated as a claim to check.
- **Note:** The directive requires only a one-time revision; the inspections it incorporates are performed at piece-part exposure under the revised TLM, which the record does not show as having occurred.
- **Note:** The HPC 3rd stage blade set (P/N 6A8688) is not listed in the directive and is not matched.
- **Note:** The 2025-17066 preamble states the EMM revision does not by itself satisfy (g)(2) for operators with an existing approved program, so the operator's program revision must be confirmed separately.
- **Note:** Engine cycle readings: 20000 on 2025-10-29 and 22500 on 2026-10-06; the directive sets no engine cycle deadline.
- **Unresolved locator:** 2025-17066 preamble Discussion of comments: task references and piece-part exposure

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 engine is within the applicability of AD 2025-19-13 (Federal Register document 2025-18469, effective 2025-10-29). Neither installed hub matches a part number and serial number pair in Table 1, so no removal is triggered on the record as supplied, but the installation prohibition in paragraph (h) continues to bind.
- **Missing fact:** The recorded HPT 2nd-stage hub serial number PKLBST5011 is a serial number listed in Table 1 for HPT 1st-stage hubs (P/N 2A5001), not for HPT 2nd-stage hubs (P/N 2A4802). The record should be confirmed, because a P/N and S/N match would be needed to trigger paragraph (g).
- **Missing fact:** No engine events are recorded. Paragraph (g) is tied to the next engine shop visit, so shop-visit history matters if any listed hub is later found installed.
- **Note:** The NPRM (2025-10764) was superseded by the final rule for this screen and was not relied on for obligations.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0024 does not appear in Table 1, so the first hub does not match on serial number.
- **Note:** The HPT 2nd-stage hub serial number PKLBST5011 appears in Table 1 only under P/N 2A5001 (1st-stage), so the pair does not match as a 2nd-stage hub. Verify the record, since a mis-keyed part number could change the outcome.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine record lists a CFM56-5B4/3 model, which is not among the IAE V2500 models this screen supports, so no applicability determination is made under AD 2025-17-16 (Federal Register document 2025-17066).
- **Note:** The engine model recorded as CFM56-5B4/3 is outside the supported V2500 model list for this screen.
- **Note:** No installed components or events are recorded, and no determination of compliance or airworthiness is made.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The AD applies to this V2530-A5 engine, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) is listed in Table 1 with a 6,200-cycle removal limit. The record shows no engine shop visit since the 2025-10-29 effective date, so removal is due at the next engine shop visit before the hub exceeds 6,200 cycles since new, which projects to about engine flight cycle 23,200.
- **Stated timing:** Remove the hub at the next engine shop visit after 2025-10-29 and before the hub exceeds 6,200 cycles since new (projected engine flight cycle about 23,200). Under the later-of wording, the 100-flight-cycle fallback (engine flight cycle 20,100) has already passed at the 2026-03-01 snapshot (20,600), so the shop-visit deadline governs only if that fallback is not read as an independent hard deadline.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** Whether any engine shop visit (separation of major mating H-P engine flanges, excluding the listed transportation and on-wing field maintenance exceptions) has occurred or is scheduled after 2025-10-29. The record lists no such event, and the shop-visit trigger determines when removal is due.
- **Missing fact:** Current cycles since new are recorded as 3600 without a dated reading at the 2026-03-01 snapshot; the arithmetic from the 2025-10-29 reading (3000 cycles at engine flight cycle 20000) to engine flight cycle 20600 is consistent, but a dated current reading would confirm the remaining-cycle figure.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0026) does not match any Table 1 row, so it is not a matched part; this is a match result only, not a determination on its eligibility.
- **Note:** The 2024 blend repair and 2024 repeat inspection of hub PKLBST7489 predate the effective date and are not treated as an AD compliance event; the record does not indicate whether they satisfy any other requirement.
- **Note:** The record field qualifies_as_engine_shop_visit is absent from the events, so no event is treated as an engine shop visit under this AD.
- **Note:** This screen is not a compliance determination, and the AD text should be checked against the operator's own records before any action is taken.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row P/N 2A5001 S/N PKLBST7489, limit 6,200 cycles

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
- **Summary:** The V2527-A5 engine is a supported model, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in Table 1 to paragraph (g) with a 4,800-cycle removal limit. The hub's CSN is 4,750, so the screen indicates removal is required by engine flight cycle 15,300 (the later of the cycle-limit date and 100 cycles after the 2025-10-29 effective date). The operator's unverified AMOC claim does not change this screen.
- **Stated timing:** Remove the listed HPT 1st-stage hub at the next engine shop visit, and no later than engine flight cycle 15,300 (about 50 cycles from the 2026-01-20 reading), before the 4,800 CSN limit is exceeded.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The AMOC claim to extend the hub removal limit to 5,300 CSN has no FAA approval reference on file (approval_reference is unknown and no approval letter is on file). Without an approved AMOC under paragraph (j), the 4,800-cycle limit in Table 1 governs this screen.
- **Missing fact:** No next engine shop visit date or event is recorded. The removal obligation is tied to the next shop visit, so the actual timing depends on when that visit occurs or whether it occurs before 15,300 cycles.
- **Note:** Screening aid only; this is not a compliance determination and does not state the engine is compliant or noncompliant.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0027) shares a listed P/N, but its S/N is not in Table 1, so it is not matched on the table basis. Confirm the S/N before relying on that result.
- **Note:** The engine-cycle and CSN readings are consistent: both rose by 250 between 2025-10-29 and 2026-01-20. The 4,750 CSN is taken from the current component record.
- **Note:** The effective date of 2025-10-29 is taken from the Federal Register record. The Table 1 limit is applied as published in the final rule.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row for P/N 2A5001 and S/N PKLBSS9200 (limit 4,800 cycles since new)

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a listed V2524-A5 and its installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) matches Table 1 of the directive, which is in force since 2025-10-29. Removal is required at the next engine shop visit, before the hub exceeds 4,000 cycles since new, or within 100 flight cycles of the effective date if that is later.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 4,000 cycles since new, or within 100 flight cycles of the effective date (engine cycle 8100), whichever occurs later. The 100-cycle point (8100) has already passed at the 8400 engine cycles on the snapshot, so the next shop visit governs the removal point.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** No planned or known date for the next engine shop visit is in the record. Its timing determines when the removal must occur, and whether the 100-cycle clause or the shop-visit clause controls.
- **Missing fact:** The 1400 cycles-since-new value is undated. The record also shows installed_at 2025-06-03 with 1400 cycles, yet the 2025-10-29 reading is 1000, which is lower and inconsistent with a rising count. The remaining-cycle figure of 2600 depends on which value is correct.
- **Missing fact:** No dated cycles-since-new reading at the 2026-02-10 snapshot. The current hub count is needed to confirm the 2600 cycles remaining before the 4,000-cycle limit.
- **Note:** Screening aid only, not a compliance determination. The ad_records entry marking AD 2025-19-13 as not_applicable, with the note 'no affected hubs installed', conflicts with the installed HPT 2nd-stage hub P/N 2A4802, S/N PKLBST5005, which is listed in Table 1. That entry is an operator claim to check and does not settle the outcome.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0028) does not match any S/N in Table 1 on this record, so it is not matched here.
- **Note:** Engine flight cycles are 8000 at 2025-10-29 and 8400 at 2026-02-10. The hub cycle readings (1000 at 2025-10-29 and 1400 currently) show 400 hub cycles over the same 400 engine cycles.
- **Note:** The installation prohibition in (h) does not by itself require removal; the hub was installed on 2025-06-03, before the effective date.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row P/N 2A4802, S/N PKLBST5005, limit 4,000 cycles since new

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model is in scope, and the installed HPT 1st-stage hub matches the directive's table by serial number PKLBSK9287 and base part number 2A5001. Its 2,400 cycles since new already exceed the 100-cycle removal limit, so the operative deadline is 100 flight cycles after the 2025-10-29 effective date, with the P/N suffix and the engine's flight-cycle count to be confirmed.
- **Stated timing:** Remove the hub and replace it with an eligible part within 100 flight cycles after the 2025-10-29 effective date. The next-shop-visit option cannot be used because the removal limit is already exceeded.
- **Missing fact:** The engine flight-cycle counter on 2025-10-29 is not in the record, so the 100-flight-cycle deadline cannot be converted to a counter value.
- **Missing fact:** The installed P/N is 2A5001-01 and the directive lists 2A5001. The suffix must be confirmed as the same listed part before the hub is treated as an affected part. If it is not the same part, the required action would not apply.
- **Missing fact:** The events list is empty. Any engine shop visit after 2025-10-29 would need to be recorded, because it would change the timing of the removal.
- **Note:** The installed HPT 2nd-stage hub, P/N 2A4802 with S/N SYN-HUB2-0029, does not match any S/N in table 1, so it is not matched to the directive on this record.
- **Note:** The 2A5001-01 P/N suffix was not addressed in the directive text. This screen treats it as a probable match on base P/N and exact S/N, which needs confirmation.
- **Note:** The hub's 2,400 cycles since new exceed the listed 100-cycle limit. The cycles_since_new figure is the part's count, not the engine's flight-cycle counter.
- **Note:** No engine shop visit is recorded after the effective date. The removal is due within 100 flight cycles after 2025-10-29, so the engine's flight-cycle count at that date is needed to convert the deadline to a counter value.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 1st-stage hub row, P/N 2A5001, S/N PKLBSK9287, removal cycle limit 100

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
