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
- **Summary:** The engine is a supported V2527-A5 with an installed HPT 1st-stage hub matching listed P/N 2A5001 and S/N PKLBST5011, which has a 5,500 cycles-since-new removal limit. Under AD 2025-18469 the hub must be removed at the next engine shop visit before it exceeds that limit, or within 100 flight cycles of the effective date if that is later; the later deadline governs, so the removal is due at the next shop visit and before 5,500 cycles since new.
- **Stated timing:** Remove and replace the matched HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 5,500 cycles since new; the 100-flight-cycle alternative is treated as the earlier deadline and does not govern under the 'whichever occurs later' wording.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** The date and engine cycle count of the next engine shop visit are not in the record. The shop-visit trigger cannot be dated, and the deadline is computed only from the cycle limit.
- **Missing fact:** The hub cycles since new are recorded only as 3100 without a date. This was derived from the 2025-10-29 reading of 1650 plus 1,450 engine cycles elapsed to 2026-09-26. The figure should be confirmed because it drives the remaining-cycles calculation.
- **Missing fact:** Whether the engine has already undergone a shop visit since the effective date is not shown. No events are recorded, so the record cannot confirm that no qualifying shop visit has occurred.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0001 is not listed in table 1 and is not matched; the record's cycles-since-new field is undated.
- **Note:** Engine cycles: 41,200 at 2025-10-29 and 42,650 at 2026-09-26, so 1,450 cycles elapsed. Projecting at that rate, the hub reaches 5,500 CSN after about 2,400 more cycles, or about 45,050 engine cycles.
- **Note:** The latest-cycles figure is a projection that assumes the hub's cycles accrue at the same rate as the engine. It is not a fixed deadline and depends on when the next shop visit occurs.
- **Note:** The removal is required at the earlier of the next shop visit or the 5,500-cycle limit. Because the record does not show when a shop visit will occur, the deadline cannot be fixed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBST5011, limit 5,500 cycles

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine is a supported V2533-A5 within the directive's applicability. Neither installed hub matches a P/N and S/N pair in Table 1 to paragraph (g) on the current record, so no removal is triggered now, but the installation prohibition in paragraph (h) continues to bind.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The installed 1st-stage hub serial PKLBST5012 differs by one character from the listed serial PKLBST5011 (5,500-cycle limit). The record shows no match, but a reviewer may wish to confirm the serial was transcribed correctly from the hub data plate.
- **Note:** The installed hubs have 4,200 cycles since new. Had either serial matched a listed pair, the limits would have been relevant, but no listed pair matched.
- **Note:** The engine record shows no events, so no engine shop visit is recorded. Future shop visits and any future hub installation should be screened against Table 1.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub rows and HPT 2nd-stage hub rows

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 is a supported model within this in-force AD's applicability. The installed HPT 1st-stage hub (P/N 2A5001) has an unknown serial number and unknown cycles since new, so it cannot be checked against Table 1, and no engine shop visit is recorded. The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) is not a listed serial number.
- **Stated timing:** For a listed hub, remove it at the next engine shop visit after 2025-10-29 before exceeding its Table 1 removal cycle limit, or within 100 flight cycles from 2025-10-29, whichever occurs later. No shop visit is recorded, so no deadline is computed yet.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub is unknown. Table 1 lists four 2A5001 serial numbers with removal limits, so this must be checked to tell whether the hub is affected.
- **Missing fact:** Cycles since new for the HPT 1st-stage hub are unknown. They are needed to compare against the Table 1 removal cycle limit if the serial number matches.
- **Missing fact:** Whether any engine shop visit has occurred or is planned is not recorded (events is empty). A shop visit after 2025-10-29 would trigger the removal requirement, so the event history must be confirmed.
- **Note:** The installed HPT 2nd-stage hub (S/N SYN-HUB2-0003) does not match any Table 1 serial number, so it is not matched on the record as given.
- **Note:** This is a screening aid, not a compliance determination. The installation prohibition in paragraph (h) continues to apply regardless of shop visit status.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not an IAE V2500 model supported by this screen, so no applicability determination is made under Federal Register document 2025-18469.
- **Note:** The engine record lists model PW1133G-JM, a Pratt & Whitney model, which is outside the supported V2500 scope of this screen.
- **Note:** No installed components or events are recorded, and no applicability determination is made.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527E-A5 engine is within AD 2025-19-13's applicability, and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed in Table 1 with a 3,900-cycle removal limit. The 2025-11-12 shop visit, recorded as qualifying, is the next engine shop visit after the effective date, so the record indicates the hub must be removed at that visit unless the record shows it was already removed.
- **Stated timing:** Required at the next engine shop visit after the October 29, 2025 effective date. The 2025-11-12 induction (engine cycle 18040) is recorded as qualifying, so removal of the listed hub is due at that visit. Under the 'whichever occurs later' wording, the alternative reading below would allow removal up to the removal limit.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** Record does not show whether the listed hub was removed during the 2025-11-12 shop visit. Removal or replacement with an eligible part is needed to determine whether the required action has been done.
- **Missing fact:** The shop visit qualification is an operator assertion. The induction detail (separation of major mating flanges) appears to meet the AD definition, but the record should be confirmed.
- **Missing fact:** HPT 1st-stage hub P/N 2A5001 S/N SYN-HUB1-0005 is not in Table 1 by serial number, so no match is found. Its cycles since new (1,040) are recorded only at the snapshot, so the hub's status cannot be confirmed without the hub-specific Table 1 comparison by the reviewer.
- **Note:** This is a screening aid, not a compliance determination. Compliance status for the engine or hub is not stated here.
- **Note:** The AD's effective date is October 29, 2025, and the question date is November 12, 2025, so the AD is in force.
- **Note:** Engine flight-cycle readings are consistent with the hub's cycles since new: 1,000 on 2025-10-29 and 1,040 on 2025-11-12, with 40 engine cycles elapsed.
- **Note:** Remaining cycles to the hub limit are computed from the snapshot value of 1,040 cycles since new; the limit is 3,900, so 2,860 cycles remain.
- **Note:** The HPT 1st-stage hub's serial number is not in Table 1, so it is not treated as an affected part on this record.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSS9840, removal cycle limit 3,900

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine is within the directive's applicability, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSK9287) is listed in Table 1 with a 100-cycle removal limit. The hub reads 90 cycles since new, so the removal action is required at the next engine shop visit before the limit is exceeded, or within the paragraph (g) window, and the installation prohibition in paragraph (h) also applies.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 100 cycles since new, or within 100 flight cycles of 2025-10-29 (by engine cycle 25600), whichever occurs later, per paragraph (g). Under the conservative reading used here, the hub reaches its limit at about engine cycle 25540.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** The hub's cycles since new are inconsistent: 90 in the current record but 60 on 2025-10-29, and the hub was recorded as installed 2025-09-30 with 90 cycles. The current value must be confirmed because it sets the remaining cycles and deadline.
- **Missing fact:** No events are recorded, so there is no confirmed engine shop visit date. Whether a shop visit has occurred or is scheduled before the limit is unknown and affects the timing of removal.
- **Missing fact:** The HPT 2nd-stage hub's part number and serial number do not match any Table 1 row, so no removal is indicated from this record. Its installation history is still needed to confirm it was not an affected part, since the record carries no dated reading.
- **Note:** Synthetic record; screening aid only, not a compliance determination.
- **Note:** The directive is effective 2025-10-29 and in force on the question date 2025-11-20.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0006) is not listed in Table 1 and was not matched.
- **Note:** The engine flight-cycle reading was 25500 on 2025-10-29 and 25530 on 2025-11-20, so the hub's remaining 10 cycles correspond to about engine cycle 25540 if hub and engine cycles accumulate one-for-one.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row for 2A5001 / PKLBSK9287, limit 100 cycles

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 is a listed model, and the record shows an HPT 1st-stage hub (2A5001, S/N PKLBSS9200) that is in Table 1 with a 4,800-cycle removal limit. The hub has about 500 cycles left, so it must be removed at the next shop visit or before reaching that limit, and the later of the two deadlines governs. This is a screening aid, not a compliance determination.
- **Stated timing:** Remove and replace the listed HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before exceeding 4,800 cycles since new, or within 100 flight cycles of 2025-10-29 if that is later. The later deadline governs, so the removal is due before the engine reaches 30,800 flight cycles.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** No engine shop visit events are recorded. Whether a shop visit has occurred or will occur before the limit affects when the removal must be done, though not the 30,800-cycle outer deadline.
- **Missing fact:** The current cycles-since-new value of 4,300 is undated; the only dated reading is 4,000 on 2025-10-29. The remaining-cycle figure depends on the 4,300 value being current on the question date.
- **Missing fact:** The Federal Register text does not state how many cycles pass per engine flight cycle for the hub; this screen assumes hub cycles track engine flight cycles one-for-one, which the record's readings support.
- **Note:** Engine flight cycles were 30,000 on 2025-10-29 and 30,300 on 2025-12-01. The 100-cycle window from the effective date ended at 30,100 and is earlier than the cycle-limit deadline, so under the 'whichever occurs later' wording it does not control.
- **Note:** The HPT 2nd-stage hub (PKLBST5005) has 1,700 cycles remaining against its 4,000-cycle limit and is not the controlling part.
- **Note:** The screen does not state or imply compliance status or return-to-service status for either hub or the engine.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200 (limit 4,800) and HPT 2nd-stage hub row 2A4802 / PKLBST5005 (limit 4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 is a listed model, and the directive is in force since 2025-10-29. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) is in Table 1 with a 6,200-cycle removal limit and 2,500 cycles since new, so it must be removed at the next engine shop visit before exceeding that limit, or within 100 flight cycles of 2025-10-29 if that is later. The HPT 2nd-stage hub cannot be screened because its serial number and cycles are unknown.
- **Stated timing:** Remove the affected HPT 1st-stage hub at the next engine shop visit, before it exceeds 6,200 cycles since new (reached at about engine cycle 54,200), or within 100 flight cycles of the 2025-10-29 effective date (engine cycle 50,100) if that is later. Under the literal 'whichever occurs later' reading, the controlling date is the shop-visit/limit date. The 50,100 date has already passed at the current engine count of 50,500.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub serial number is unknown, so it cannot be checked against the Table 1 P/N 2A4802 serial numbers. The hub may or may not be an affected part.
- **Missing fact:** Cycles since new for the HPT 2nd-stage hub are unknown, so its removal limit (3,900 to 6,000 cycles depending on S/N) cannot be checked if the serial number is listed.
- **Missing fact:** No engine shop visit events are recorded, so the next shop visit date is unknown and the shop-visit trigger cannot be confirmed.
- **Missing fact:** The 2,500-cycle figure has no date. It appears consistent with the 2,000-cycle reading at 2025-10-29 plus 500 engine cycles elapsed, but the as-of date should be confirmed.
- **Note:** This is a screening aid, not a compliance determination. The hub's cycles-since-new value of 2,500 was taken as current at the 2026-03-10 snapshot.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule for this screen and was not relied on.
- **Note:** Under the (i)(2) shop-visit definition, a shop visit requires separation of major mating engine flanges, H-P, and is not established by the record, which has no events.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBST7489, limit 6,200

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The directive is in force as of the question date (effective October 29, 2025) and the engine model V2522-A5 is within the supported scope and the listed applicability. However, the engine record shows no installed components and no events, so whether any listed HPT 1st-stage or 2nd-stage hub is installed cannot be determined and the required-action status cannot be screened.
- **Missing fact:** No record of whether an HPT 1st-stage hub is installed; the installed components list is empty, and a missing record is not evidence that the part is absent. Its P/N and S/N are needed to match against Table 1 to paragraph (g).
- **Missing fact:** No record of whether an HPT 2nd-stage hub is installed; its P/N and S/N are needed to match against Table 1 to paragraph (g).
- **Missing fact:** No engine event history is recorded, so it is unknown whether an engine shop visit has occurred or will occur after the effective date, which controls when removal is due.
- **Missing fact:** Engine flight-cycle counter is not recorded, so the cycle-based deadline (removal cycle limit or 100 flight cycles from the effective date, whichever is later) cannot be computed.
- **Note:** This is a screening aid, not a compliance determination. The engine record is synthetic and has no installed components or events, so no part has been matched and no compliance status is stated.
- **Note:** Once the installed hub records are supplied, match each HPT 1st-stage and 2nd-stage hub P/N and S/N against Table 1 and compute the removal deadline from the listed cycle limit and the next engine shop visit, bounded by 100 flight cycles after October 29, 2025.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made against AD 2025-19-13.
- **Note:** Engine model recorded as V2500-A1 is outside the supported model list, so the screen makes no applicability determination.
- **Note:** The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 matches a row in Table 1 of the directive, but the directive's applicability is not determined for this engine model and this match is not a compliance finding.
- **Note:** The directive is in force with an effective date of October 29, 2025, and the question date is 2026-09-26.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine record lists 3rd stage HPC rotor blade set P/N 6A8353, which is within the directive's applicability. The directive is in force since September 24, 2026, and requires replacing the full set of 3rd stage HPC rotor blades with parts eligible for installation at the next engine shop visit after that date where the blade is exposed; the record shows no events, so no shop visit is recorded.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum). No fixed calendar or cycle deadline applies otherwise.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** No engine shop visit events are recorded. Whether an engine shop visit has occurred since September 24, 2026 with the 3rd stage HPC rotor blade exposed cannot be determined, so the trigger for the required action is unconfirmed.
- **Missing fact:** The blade set serial number is recorded as not tracked at set level. Blade-level identification is needed to confirm the installed blades are P/N 6A8353 and to track any replacement against parts eligible for installation.
- **Note:** This is a screening aid, not a compliance determination. The record shows no shop visit events, so no action has been triggered yet on the record as supplied.
- **Note:** The earlier NPRM 2025-20088 proposed a flight-independent exposure trigger; it is superseded by the final rule and was not used.
- **Note:** The blade set serial number is not tracked at set level, so blade-by-blade P/N verification is not possible from the record.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The engine is a supported V2533-A5 and the directive is in force as of 2026-10-05. The record lists the 3rd stage HPC rotor blade set as P/N 6C8368, which is a listed eligible part rather than 6A8353 or 6A8688, but the set is recorded at set level only, so the absence of 6A8353 or 6A8688 blades cannot be confirmed. No engine shop visit is recorded, so no replacement is triggered now.
- **Stated timing:** Replacement of the full set of 3rd stage HPC rotor blades with parts eligible for installation is due at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum), if the applicability condition is met.
- **Missing fact:** Per-blade part numbers for the 3rd stage HPC rotor blade set are needed. The set is recorded only as 6C8368. Confirming that no blade is P/N 6A8353 or 6A8688 is needed to decide whether the directive applies.
- **Missing fact:** The events list is empty. Whether any engine shop visit has occurred or is scheduled after 2026-09-24 with 3rd stage HPC rotor blade exposure is unknown, and that event would trigger the required action.
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** The record's serial_number is 'not tracked at set level', so no serial-level blade identification is available.
- **Note:** The installed 6C8368 part number is a listed eligible part, which would not by itself meet the applicability condition. If all blades are confirmed as 6C8368 or other eligible P/N, the directive would not apply to this engine.
- **Note:** The 2026-18423 correction does not change the required action or deadline. It only fixes a typographical omission of the word 'blade' in paragraph (g).
- **Note:** Under the directive, replacement with reworked blades or new blades is an acceptable compliance option; the FAA's cost notes are not part of the operative requirement.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The engine is a supported V2530-A5 with a 3rd stage HPC rotor blade set of P/N 6A8688 installed, so the directive applies and is in force as of 2026-09-30. The only recorded shop visit was inducted 2026-09-14, before the 2026-09-24 effective date, and the directive's paragraph (g) reaches only the next engine shop visit after the effective date, so no replacement is triggered by this visit on the record as given.
- **Stated timing:** Replacement of the full 3rd stage HPC rotor blade set is due at the next engine shop visit after 2026-09-24 in which the 3rd stage HPC rotor blade is exposed; no deadline applies to the 2026-09-14 visit under the preamble's stated intent.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The engine flight-cycle counter is not in the record, so no cycle-based deadline can be computed for any reading of the directive.
- **Missing fact:** Blade serial numbers are not tracked at set level; the set's P/N match is established but individual blade identity and whether the full set is still the original set cannot be confirmed.
- **Missing fact:** The operator asserts the 2026-09-14 induction qualifies as an engine shop visit, but the induction predates the 2026-09-24 effective date, so whether the 2026-09-30 blade exposure falls under paragraph (g) depends on the reading of the induction date and needs confirmation.
- **Note:** Screening aid only; this is not a compliance determination. The 2026-09-14 induction predates the effective date, and the preamble states the FAA did not intend engines inducted before the effective date to comply. A reviewer should confirm that reading, because the blade exposure occurred on 2026-09-30, after the effective date. If that reading is adopted, replacement of the full blade set would be due immediately and no cycle-based deadline can be computed from the record.
- **Note:** The operator's qualifies_as_engine_shop_visit assertion of 'yes' for the 2026-09-14 induction is a claim to check, not settling evidence.
- **Note:** Replacement with reworked blades or new blades are both acceptable options under the directive's definition of parts eligible for installation, per the final rule preamble.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2026-17-03 (FR 2026-16954, effective 2026-09-24) applies to this V2524-A5 engine because installed 3rd stage HPC rotor blade set P/N 6A8353 is listed. The only shop visit (2026-10-01) is after the effective date and is recorded as qualifying, but the record says no 3rd-stage blade was removed from the stage 3-8 drum, so no '3rd stage HPC rotor blade exposure' as defined in paragraph (h)(2) is recorded and no replacement is triggered on these facts.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** Set-level serial number is not tracked, so the blade set cannot be individually identified against the directive's part eligible for installation records.
- **Missing fact:** Confirmation that no 3rd stage HPC rotor blade was removed from the HPC stage 3 to 8 drum during the 2026-10-01 shop visit or the 2026-10-02 exposure, since paragraph (h)(2) defines exposure by blade removal, not by rotor exposure alone.
- **Missing fact:** Engine flight-cycle counter, which would be needed to compute any deadline if a blade exposure is later confirmed.
- **Note:** Ambiguity: the published (g) text in 2026-16954 says 'the 3rd stage HPC rotor is exposed' and the correction 2026-18423 says 'the 3rd stage HPC rotor blade is exposed'. If the rotor-exposure wording were read alone, the 2026-10-02 event would arguably trigger action at the 2026-10-01 shop visit, with the deadline at the close of that visit (2026-10-04), which is already past. The defined term in (h)(2) favors the no-removal reading, but a reviewer should confirm.
- **Note:** The operator's qualifies_as_engine_shop_visit assertion is recorded as 'yes' for AD 2026-17-03 and is taken as a claim, not as a settled fact.
- **Note:** This screen does not state compliance or noncompliance; it only reports the recorded facts against the directive text.
- **Note:** Engine flight-cycle count and blade set history were not supplied, so no deadline or remaining-cycle figure can be computed.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** Document 2025-20088 is a proposed rule (NPRM) with no effective date, so it cannot require action as of 2026-01-15. The engine is a supported V2527E-A5 with a 3rd stage HPC rotor blade set recorded as P/N 6A8353, which matches the proposed applicability, but the record does not show whether a blade exposure has occurred.
- **Missing fact:** No event records are present; the record does not show whether any 3rd stage HPC rotor blade has been removed from the HPC stage 3 to 8 drum, which would be the proposed trigger for replacement. Needed to determine whether any action would be triggered if the rule is adopted.
- **Missing fact:** Serial number is not tracked at set level, so the blade set cannot be confirmed to be a 6A8353 set on a per-blade basis; the part number is recorded only at set level.
- **Note:** The directive is a proposed rule; authority_state is proposed and it cannot require action until a final rule is published and effective.
- **Note:** Even if adopted, the proposed action is tied to a future blade exposure event, not a fixed flight-cycle deadline.
- **Note:** This is a screening aid only and does not state compliance or airworthiness status.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 (Federal Register document 2025-17066) is in force from its October 10, 2025 effective date and covers the V2527-A5, a supported model. As an air carrier operation, the operator must revise paragraph B.1 of the V2500-A5 TLM ALS and its approved maintenance program by January 8, 2026; the record states neither revision is yet incorporated.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e., on or before January 8, 2026, for both the TLM ALS revision under (g)(1) and the air carrier maintenance program revision under (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** No HPT Stage 1 Hub (P/N 2A5001) component record is present; the engine record lists no installed components. This does not change the ALS and program revision deadline, but it is needed to determine later inspection obligations at piece-part exposure.
- **Missing fact:** No HPT Stage 2 Hub (P/N 2A4802) component record is present; needed to determine later inspection obligations at piece-part exposure under TASK 72-45-31-200-009.
- **Note:** This is a screening aid only and not a compliance determination. The operator's record states that Revision 47 (2025-06-01) and TLM ALS paragraph B.1 do not yet incorporate table 1 to paragraph (g); the 2026-01-08 deadline is therefore the operative date to track.
- **Note:** The engine record has no installed components and no events, so no part-level inspection or cycle-based limit can be computed.
- **Note:** The NPRM (2024-26092) is superseded for this question by the final rule; its 90-day timing was tied to a then-unknown effective date and does not govern.
- **Note:** No AMOC claims are recorded in the engine record.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive is in force on the question date (effective October 10, 2025) and the engine model V2522-A5 is within its applicability list, but the record has no installed components and no events, so the HPT stage 1 and stage 2 hub part numbers cannot be checked against the installed parts. Whether the air carrier revision in paragraph (g)(2) applies is also unknown because the operator's air carrier status is unknown.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e., by January 8, 2026, for the ALS/TLM revision under paragraph (g)(1); paragraph (g)(2) applies to air carrier operations on the same 90-day schedule.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** No installed component record for the HPT Stage 1 Hub (listed P/N 2A5001) is present, so it cannot be determined whether the engine carries the listed hub.
- **Missing fact:** No installed component record for the HPT Stage 2 Hub (listed P/N 2A4802) is present, so it cannot be determined whether the engine carries the listed hub.
- **Missing fact:** Whether the operator is an air carrier operation is unknown; paragraph (g)(2) applies only to air carrier operations.
- **Missing fact:** No event history is recorded, so no shop visit or piece-part exposure has been documented; the inspection tasks are tied to piece-part exposure in the Maintenance Scheduling section.
- **Missing fact:** The record gives no record of whether the operator has already revised the TLM ALS or the approved maintenance program; no ad_records entry is present to show this.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The record is synthetic, with an empty installed_components list and no events; a missing record is not evidence that the hubs are absent.
- **Note:** The 2024 NPRM (2024-26092) is superseded for this purpose by the final rule and is cited only as background; the final rule's text controls.
- **Note:** The engine serial number SYN-V2500-0017 has no associated engine flight-cycle counter, so no latest_engine_flight_cycles can be computed; the deadline is calendar-based.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2525-D5 is within the supported scope and the directive's applicability. The directive is a final rule effective October 29, 2025, so it cannot require action on the question date. The installed HPT 2nd-stage hub matches a Table 1 entry (P/N 2A4802, S/N PKLBSR2100, limit 6,000 cycles) with 990 cycles since new, leaving 5,010 cycles, and its removal is due at the next shop visit after the effective date or within 100 flight cycles of it, whichever is later.
- **Stated timing:** The directive is not yet effective (effective October 29, 2025). Once effective, removal is required at the next engine shop visit after that date before exceeding 6,000 cycles since new for the HPT 2nd-stage hub, or within 100 flight cycles from the effective date, whichever occurs later. No shop visit is recorded.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine flight-cycle counter as of the effective date is not in the record, so the 100-flight-cycle window and any engine-cycle deadline cannot be computed.
- **Missing fact:** No engine event history is recorded; the next shop visit after October 29, 2025 cannot be identified, and the record does not show whether any shop visit has already occurred since the directive was published.
- **Missing fact:** The installed HPT 1st-stage hub serial number SYN-HUB1-0018 is not listed in Table 1, so it does not match the directive on the current record. This should be confirmed against the Table 1 serial numbers.
- **Note:** This is a screening aid only and not a compliance determination. The directive is not in force on 2025-10-15, so no action is required yet; the screen should be rerun on or after October 29, 2025.
- **Note:** The HPT 2nd-stage hub with S/N PKLBSR2100 has 5,010 cycles remaining before its listed limit, but the removal deadline depends on the next shop visit or the engine flight-cycle counter, neither of which is recorded.
- **Note:** The 2025-10764 NPRM is superseded by the final rule and is not relied on for the outcome.
- **Note:** No operator AD status record or AMOC claim was supplied, so none was assessed.
- **Unresolved locator:** 2025-18469 (g) Required Actions; Table 1 to Paragraph (g), HPT 2nd-stage hub row PKLBSR2100

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a supported V2531-E5 with an installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) that is listed in Table 1 with a 4,800-cycle removal limit. The recorded cycles since new (4,990, and 4,950 on 2025-10-29) already exceed that limit, so the hub must be removed and replaced within 100 flight cycles of the 2025-10-29 effective date, which means by engine flight cycle 60,100 (or at a later next shop visit if that falls later).
- **Stated timing:** Remove and replace the affected HPT 1st-stage hub at the next engine shop visit after the 2025-10-29 effective date or within 100 flight cycles of that date (by engine flight cycle 60,100), whichever occurs later. The removal cycle limit is already exceeded, so the shop-visit timing cannot be confirmed from the record.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The undated cycles_since_new value of 4,990 is used here as the current count; the only dated reading is 4,950 on 2025-10-29. Either value exceeds the 4,800 limit, but the exact current count should be confirmed.
- **Missing fact:** The events list is empty, so it is unknown whether an engine shop visit has occurred or is scheduled after 2025-10-29; this determines when the hub removal is due under the shop-visit prong.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0019) does not match any Table 1 entry, so it is not a matched part on this record; the record does not show its S/N against the listed hubs beyond that comparison.
- **Note:** The 100-cycle limit counts from the 2025-10-29 effective date, when the engine was at 60,000 cycles; the latest snapshot is 60,040, leaving about 60 cycles.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row for P/N 2A5001, S/N PKLBSS9200, limit 4,800

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** Engine model V2533-A5 is in the supported scope and within AD 2021-11-15's model list, and both installed disks carry the listed part numbers (2A5001 and 2A4802). Applicability cannot be decided because the disk serial numbers are not confirmed against the Appendix A tables, and the record has no engine shop visit history or flight-cycle count. AD 2021-11960 is still in force on 2022-03-01 but is superseded by 2022-02574 effective 2022-03-15.
- **Stated timing:** Under paragraphs (g)(1) and (g)(2), the USI of each disk is due at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 FCs since 2021-07-13, whichever occurs first. Under the superseding AD 2022-02574, the compliance time for high-thrust engines (including V2533-A5) is set by a figure not included in the text provided, so the deadline cannot be fixed from the supplied text.
- **Missing fact:** The HPT 1st-stage disk serial number SYN-DISK1-0020 must be checked against Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Revision 1 to confirm applicability under paragraph (c)(1); the NMSB was not supplied.
- **Missing fact:** The HPT 2nd-stage disk serial number SYN-DISK2-0020 must be checked against Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713 Revision 1 to confirm applicability under paragraph (c)(2); the NMSB was not supplied.
- **Missing fact:** No engine shop visit history is recorded, so it is unknown whether a shop visit has occurred since 2021-07-13 that would trigger the at-next-shop-visit requirement.
- **Missing fact:** The engine flight-cycle count since 2021-07-13 is not in the record, so the 3,200-FC limit cannot be computed.
- **Missing fact:** The Figure 1 compliance times referenced by AD 2022-02574 are not included in the text, so the superseding compliance time for this engine cannot be determined.
- **Note:** Question date 2022-03-01 falls before the 2022-03-15 effective date of superseding AD 2022-02574, so AD 2021-11960 is still in force on that date. The superseding AD is noted because it changes compliance times for high-thrust engines.
- **Note:** The record contains no ad_records or amoc_claims entries, so no operator status claim was reviewed.
- **Note:** Part numbers 2A5001 and 2A4802 match the directive's listed part numbers, but serial-number matching to Appendix A is not confirmed, so no matched_parts entry is recorded.
- **Note:** This is a screening aid only and does not determine compliance or airworthiness.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2021-11960 (c) Applicability, items (1) and (2)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 supersedes AD 2021-11-15 and takes effect March 15, 2022, so it cannot require action on the 2022-03-01 question date. Applicability cannot be decided because the installed HPT 1st-stage and 2nd-stage disk serial numbers have not been checked against the Appendix A serial lists, which were not supplied, and the Figure 1 compliance time is not in the text provided.
- **Stated timing:** Not yet effective. Once effective, the USI for a V2533-A5 is due at the next engine shop visit after March 15, 2022, or within the Figure 1 compliance time, or within 10 flight cycles after the effective date, whichever occurs later. Figure 1 was not provided.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015 Rev 1) was not supplied. Whether HPT 1st-stage disk P/N 2A5001, S/N SYN-DISK1-0020, is listed there determines applicability under paragraph (c)(1) and the (g)(1) requirement.
- **Missing fact:** Appendix A, Table 2 of the same NMSB was not supplied. Whether HPT 2nd-stage disk P/N 2A4802, S/N SYN-DISK2-0020, is listed there determines applicability under paragraph (c)(2) and the (g)(2) requirement.
- **Missing fact:** Figure 1 to paragraph (g)(1) of AD 2022-02-09 is an image not included in the text, so the compliance time for the V2533-A5 cannot be computed.
- **Missing fact:** The event history is empty. Whether any engine shop visit has occurred since the disks were installed, and whether the disks have any prior operating history, cannot be confirmed from the record.
- **Note:** This is a screening aid only. It is not a compliance determination, and it does not state that any engine or part is compliant, noncompliant, or airworthy.
- **Note:** AD 2021-11-15 (Federal Register document 2021-11960) is the directive this AD supersedes. It remains the directive in force on 2022-03-01 and was not screened here. Under it, the V2533-A5 disks would face a shop-visit or 3,200 FC deadline measured from July 13, 2021.
- **Note:** The matched part numbers are shown with listed_serial_number null because the directive lists serial numbers in appendices that were not supplied. The part-number match is not a serial-number match.
- **Note:** The record contains no operator AD status or AMOC claims for this engine.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (document 2022-02574) is in force and covers V2530-A5 engines with HPT 1st-stage disk P/N 2A5001 and HPT 2nd-stage disk P/N 2A4802 whose serial numbers are listed in the NMSB Appendix A tables. The installed disk part numbers match, but the supplied text does not include those serial-number tables, so applicability and the Figure 1 compliance time cannot be determined from the record.
- **Stated timing:** For V2530-A5 engines under paragraph (g)(1) and (g)(2), the USI is due within the compliance time in Figure 1 to paragraph (g)(1), or within 10 flight cycles after March 15, 2022, whichever is later. Figure 1 is not included in the supplied text, so the due date cannot be computed.
- **Missing fact:** Serial number SYN-DISK1-0021 must be checked against Appendix A, Table 1 of NMSB V2500-ENG-72-0713 Revision 1 (or NMSB V2500-E5-72-0015 Revision 1). The tables are not in the supplied text, so the disk's listing status is unknown.
- **Missing fact:** Serial number SYN-DISK2-0021 must be checked against Appendix A, Table 2 of NMSB V2500-ENG-72-0713 Revision 1 (or NMSB V2500-E5-72-0015 Revision 1). The tables are not in the supplied text, so the disk's listing status is unknown.
- **Missing fact:** Figure 1 to paragraph (g)(1), which sets the compliance time for the USI, is not in the supplied text. It is needed to state the due date.
- **Missing fact:** The engine's flight-cycle counter and the date of the last engine shop visit are not in the record. Without them the 3,200-cycle and shop-visit deadlines cannot be computed.
- **Missing fact:** The events list is empty, so there is no record of any engine shop visit or of prior operation of these disks on high-thrust engines. Either fact could affect the compliance time.
- **Note:** Supported model: V2530-A5 is on the supported list. The directive is in force on 2026-10-06 (effective 2022-03-15).
- **Note:** This directive supersedes AD 2021-11-15 (document 2021-11960). The 2021 text is not the operative requirement.
- **Note:** No ad_records or amoc_claims were supplied, so the operator's recorded AD status is unknown.
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
- **Summary:** The V2533-A5 engine has an installed HPT 1st-stage disk, P/N 2A5001, S/N PKLBSH1829, which is listed in paragraph (c)(1) of the directive, so the directive applies. The ultrasonic inspection of that disk under paragraph (g)(1) was due within 10 flight cycles after the July 19, 2021 effective date, which is engine flight cycle 33010 on the reading used here; the engine was at 33004 on 2021-07-20.
- **Stated timing:** Perform the ultrasonic inspection of the HPT 1st-stage disk per IAE NMSB V2500-ENG-72-0713 paragraph 6 within 10 flight cycles after July 19, 2021 (by engine flight cycle 33010); if the disk does not pass, remove it before further flight.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** No record of whether the required USI of the HPT 1st-stage disk has already been performed or what its result was. Without this, it cannot be established whether the 10-cycle action is still open.
- **Missing fact:** The installed HPT 2nd-stage disk (P/N 2A4802, S/N SYN-DISK2-0022) is not in the paragraph (c)(2) serial list. Its absence from the list does not confirm it is unaffected, so the record should be checked against the listed serials and the directive's Table 2 before concluding the 2nd-stage disk is outside the directive.
- **Note:** This is a screening aid only and does not determine compliance or airworthiness of the engine or any part.
- **Note:** The engine record lists no events and no AD status record for AD 2021-11-51, so the USI status is unknown.
- **Note:** The 2nd-stage disk serial SYN-DISK2-0022 is not in the paragraph (c)(2) list; this does not by itself establish the disk is outside the directive, and the missing-facts entry above should be checked.
- **Note:** Remaining cycles to the 33010 deadline from the 2021-07-20 reading of 33004 is 6 cycles, but component_cycles_remaining is left null because it measures part life limits, not this inspection window.
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
- **Summary:** The V2533-A5 is a supported model and the directive is in force, but the installed HPT 1st-stage disk (P/N 2A5001, S/N PKLBSH1829) and HPT 2nd-stage disk (P/N 2A4802, S/N SYN-DISK2-0022) cannot be checked against the serial-number tables in Appendix A, and the engine cycle count on the effective date is not recorded. The inspection obligation is therefore not confirmed as triggered, and the deadline cannot be computed.
- **Stated timing:** For V2533-A5 engines, each affected disk must undergo a USI at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first, if the serial number is listed in Appendix A. No engine shop visit is recorded.
- **Missing fact:** Whether S/N PKLBSH1829 is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1 is not confirmed; the Appendix A tables were not supplied. This determines whether paragraph (g)(1) applies.
- **Missing fact:** Whether S/N SYN-DISK2-0022 is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713 Rev 1 is not confirmed; the Appendix A tables were not supplied. This determines whether paragraph (g)(2) applies.
- **Missing fact:** Engine flight-cycle count on the July 13, 2021 effective date is not recorded, so the 3,200-FC limit since the effective date cannot be converted to an engine cycle counter value.
- **Missing fact:** Appendix A, Tables 1 and 2, of the referenced NMSB (not supplied) are needed to check serial-number listing for both disks.
- **Note:** The directive is in force as of July 13, 2021, and the question date is July 20, 2021. The model V2533-A5 is within the supported scope.
- **Note:** Both installed part numbers match the directive's listed part numbers, but serial-number listing in Appendix A cannot be verified from the supplied text.
- **Note:** The events list is empty, so no engine shop visit is recorded. The engine reading on July 20, 2021 is 33004 FCs, which is after the effective date, but the cycle count on July 13, 2021 is missing.
- **Note:** Under the 3,200-FC limit, the disks would be due no later than 3,200 FCs after the effective date, and the engine's cycle count is about 33004 on July 20, 2021. A precise deadline needs the July 13, 2021 count.
- **Note:** No compliance or airworthiness determination is made. This is a screening aid only.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is listed and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) matches table 1 to paragraph (g), which has a 6,000-cycle removal limit. The record shows no engine shop visit or hub removal, and the 100-flight-cycle window from the 2025-10-29 effective date ended at engine cycle 20,100, before the 22,500 cycles shown on 2026-10-06, so the required action needs review and may be overdue.
- **Stated timing:** Remove the matched HPT 2nd-stage hub at the next engine shop visit after 2025-10-29 before it exceeds 6,000 cycles since new, or within 100 flight cycles of 2025-10-29 (engine cycle 20,100), whichever occurs later. The 100-cycle limit has already passed on the question date.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** Whether any engine shop visit (separation of major H-P mating flanges, excluding the paragraph (i)(2) exceptions) has occurred since 2025-10-29. The record lists none, and this determines whether the shop-visit prong of paragraph (g) has been triggered.
- **Missing fact:** The dated reading of 1,000 cycles since new on 2025-10-29 conflicts with the undated cycles_since_new of 3,500 and the installed date of 2024-01-09. The current value determines the 2,500 cycles remaining to the 6,000 limit.
- **Missing fact:** Confirmation of the hub's current cycles since new is needed to confirm the remaining-cycles figure, because the hub may not accumulate cycles one-for-one with engine flight cycles.
- **Note:** Authority is in force: the rule is effective 2025-10-29 and the question date is 2026-10-06.
- **Note:** The HPT 1st-stage hub (S/N SYN-HUB1-0023) does not match any serial number in table 1, so it is not matched. Its record is incomplete, but this is not evidence that it is unaffected.
- **Note:** The 3rd stage HPC rotor blade set is not listed in this directive and is outside this screen.
- **Note:** The maintenance program revision event refers to AD 2025-17-16, which is a different directive and is not assessed here.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSR2100, limit 6,000 cycles

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527M-A5 engine is a supported model and the installed 3rd stage HPC rotor blade set is recorded as P/N 6A8688, which the directive lists, so the directive applies. The required blade-set replacement is triggered only at the next engine shop visit after 2026-09-24 where the blades are exposed, and the record shows no such shop visit.
- **Stated timing:** At the next engine shop visit after the effective date of 2026-09-24 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum), replace the full set of 3rd stage HPC rotor blades with parts eligible for installation. No deadline in flight cycles applies.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Engine shop visit history since 2026-09-24 is not in the record. The only event is a maintenance program revision on 2025-12-01, which is not a shop visit. Whether an engine shop visit with blade exposure has occurred or will occur determines whether and when replacement is required.
- **Missing fact:** The blade set serial is recorded as not tracked at set level, so the installed blades cannot be confirmed individually against the P/N 6A8688 listing or against the 6C8368/6C8403 replacement parts.
- **Missing fact:** Whether the 3rd stage HPC rotor blades were exposed at any shop visit, and whether the blade set is the original set, is not documented; these facts bear on whether the next shop visit triggers replacement.
- **Note:** The directive is in force as of 2026-09-24, so the question date of 2026-10-06 is after its effective date.
- **Note:** The correction document 2026-18423 fixes a typographical omission ('blade') in paragraph (g) and does not change the substance of the requirement.
- **Note:** No ad_records or amoc_claims were supplied, so no operator AD status or AMOC claim was assessed.
- **Note:** Engine cycle readings (20000 on 2025-10-29 and 22500 on 2026-10-06) are not used because no flight-cycle deadline is computed for this event-triggered action.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 is in force (effective 2025-10-10) and covers the V2527M-A5. The one-time ALS and air carrier program revisions were due by 2026-01-08, and the operator record shows them made on 2025-12-01, so no required action is triggered now. The piece-part exposure inspections of the HPT hubs remain continuing obligations.
- **Stated timing:** The ALS and maintenance program revisions were due within 90 days after 2025-10-10 (by 2026-01-08); the record shows them done 2025-12-01. The hub inspections are due at piece-part exposure.
- **Missing fact:** The revision event is the operator's own statement. Confirmation that the TLM paragraph B.1 text includes TASK 72-45-11-200-006 and TASK 72-45-31-200-009 for the applicable TLM is not in the record.
- **Missing fact:** The record lists cycles since new for the HPT 1st-stage hub but has no dated reading and no piece-part exposure history, so its status at the next exposure cannot be checked.
- **Missing fact:** The record shows a dated reading on 2025-10-29 but no later reading, so the hub's cycles at the question date are not confirmed.
- **Missing fact:** The directive gives no cycle limit for the hubs; the inspection thresholds are in the referenced TLM tasks, which are not in the supplied text.
- **Note:** The record's maintenance_program_revision entry and the 2025-12-01 event are operator claims. They are checked against the directive's text but not verified against the actual TLM or program document.
- **Note:** The record gives no shop-visit events, so whether a piece-part exposure has occurred is unknown. This screen does not state that either hub is compliant or noncompliant.
- **Note:** The HPT 2nd-stage hub has 3500 cycles since new at installation and 1000 at 2025-10-29, and the engine reads 22500 cycles on 2026-10-06. These internal inconsistencies should be reviewed.
- **Note:** The 3rd stage HPC rotor blade set (6A8688) is not listed in the directive and is not matched.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is a supported model within the applicability of AD 2025-19-13 (effective 2025-10-29, in force on the question date). Neither recorded hub matches a P/N and S/N pair in Table 1, so no removal is triggered now, but the installation prohibition in paragraph (h) continues to bind.
- **Missing fact:** The recorded HPT 2nd-stage hub carries serial number PKLBST5011, which Table 1 lists only under P/N 2A5001 (1st-stage hub). The P/N recorded as 2A4802 should be verified against the hub's documentation. If the part is actually P/N 2A5001, it would be a listed 1st-stage hub with a 5,500-cycle removal limit, and the required action timing would change.
- **Missing fact:** No events are recorded. Shop-visit status is needed only if a listed part is found installed, so it does not affect the current screen.
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** The 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0024) is not listed in Table 1 because its serial number does not appear there.
- **Note:** Table 1 requires both P/N and S/N to match. The 2nd-stage hub's serial PKLBST5011 appears in Table 1 only under P/N 2A5001, so there is no match for P/N 2A4802.
- **Note:** Both installed hubs show 3000 cycles since new. This does not change the outcome because neither part is a listed part.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model recorded is CFM56-5B4/3, which is not among the IAE V2500 models supported by this screen, so no applicability determination is made against Federal Register document 2025-17066.
- **Note:** The engine record model CFM56-5B4/3 is a CFM International model, not an IAE V2500 model; this screen does not evaluate it against the directive.
- **Note:** The installed_components and events lists are empty; no part or event facts were evaluated.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 is a listed model, and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in Table 1 with a 6,200-cycle removal limit. The hub has 3,600 cycles since new, so it must be removed at the next engine shop visit before it exceeds 6,200 cycles, which is about engine flight cycle 23,200 on the current accrual rate. The listed hub also cannot be installed in any engine after the October 29, 2025 effective date.
- **Stated timing:** Remove the hub at the next engine shop visit, and in any case before it exceeds 6,200 cycles since new (about engine flight cycle 23,200 at the current accrual rate). Installation of the listed hub is prohibited after October 29, 2025.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** The 3,600 cycles-since-new reading has no date. The 2025-10-29 reading was 3,000, which implies the hub accrues cycles with the engine, but the current value needs confirmation because it sets the remaining-cycle figure and the deadline.
- **Missing fact:** No engine shop visit after the October 29, 2025 effective date is recorded. The record does not show whether a shop visit has occurred or is scheduled, which determines when the hub removal must be performed.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0026 is not listed in Table 1, so no action is triggered for that hub on this record.
- **Note:** The 2024-06-10 blend repair and 2024-06-12 inspection of hub PKLBST7489 predate the effective date and do not change the removal requirement. No record field states whether the 2024 repair event meets the AD's engine shop visit definition, and the repair is not an engine shop visit event for this AD on the record given.
- **Note:** The hub was installed 2024-07-02, before the effective date, so the installation prohibition is not shown to have been breached on this record.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row for P/N 2A5001, S/N PKLBST7489, limit 6,200 cycles

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
- **Summary:** The V2527-A5 engine has HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 installed, which is listed in Table 1 with a 4,800-cycle removal limit. The hub is at 4,750 CSN, so removal at the next engine shop visit before the limit is reached is required, and the 100-flight-cycle alternative clause from the effective date (cycle 15,100) has already passed. The operator's 5,300 CSN AMOC claim has no FAA approval on file and cannot be relied on.
- **Stated timing:** Remove the affected hub at the next engine shop visit after 2025-10-29 and before it exceeds 4,800 CSN, which is about 50 cycles away (engine flight cycle about 15,300). Under the alternative reading that the 100-cycle clause governs, removal was due by engine flight cycle 15,100 and is already overdue.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** No engine shop visit is recorded. Whether and when the next shop visit occurs determines when removal must be performed under paragraph (g), so the schedule of the next shop visit is needed.
- **Missing fact:** The claimed AMOC extending the hub limit to 5,300 CSN has no approval letter or approval reference (unknown). Without an FAA-approved AMOC under paragraph (j), the 4,800-cycle limit in Table 1 governs.
- **Missing fact:** The current CSN is taken as 4,750 from the installed record. Confirmation that this value is current at the 2026-01-20 snapshot is needed to fix the cycles remaining.
- **Note:** The HPT 2nd-stage hub, P/N 2A4802, S/N SYN-HUB2-0027, is not listed in Table 1 (listed S/Ns are PKLBS-series), so it is not matched and no removal is triggered by it on this record.
- **Note:** The 1st-stage hub CSN rose from 4,500 at 2025-10-29 to 4,750 now, matching the 250 engine cycles over the same period.
- **Note:** This is a screening aid, not a compliance determination. The NPRM 2025-10764 was superseded by the final rule 2025-18469, which was relied on here.
- **Unresolved locator:** 2025-18469 (g) Table 1 row: HPT 1st-stage hub, 2A5001, PKLBSS9200, 4,800

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2524-A5 engine is in scope, and its installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) is listed in Table 1 with a 4,000-cycle removal limit. Under paragraph (g), that hub must be removed at the next engine shop visit before it exceeds 4,000 cycles since new, or within 100 flight cycles of the effective date if that is later; the hub has about 2,600 cycles left, so the next shop visit must occur before engine flight cycle ~11,000. The operator's 'not_applicable' AD record conflicts with this installed part.
- **Stated timing:** Remove and replace the HPT 2nd-stage hub at the next engine shop visit after October 29, 2025 and before it exceeds 4,000 cycles since new (about 2,600 more cycles at the current rate, i.e. around engine flight cycle 11,000). The alternative 100-flight-cycle window from the effective date ended at engine flight cycle 8,100 and has already passed on the record.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The hub's cycles since new are recorded as 1400 without a dated reading, while the only dated reading is 1000 at 2025-10-29. A current dated reading is needed to confirm the 2,600 cycles remaining and the flight-cycle deadline.
- **Missing fact:** The installed HPT 1st-stage hub serial number (SYN-HUB1-0028) is not listed in Table 1 for P/N 2A5001, so it does not match the table on this record. Its cycles-since-new history is also not recorded, so this match cannot be fully confirmed.
- **Missing fact:** The operator's recorded status 'not_applicable' with the note 'no affected hubs installed' conflicts with the installed HPT 2nd-stage hub, which matches Table 1. This claim cannot be relied on and needs review.
- **Note:** This is a screening aid, not a compliance determination. The operator's AD status record is contradicted by the installed hub match and should be reviewed.
- **Note:** The HPT 2nd-stage hub was installed on 2025-06-03, before the effective date, so the installation prohibition in (h) is not triggered by that installation itself.
- **Note:** The deadline projection assumes the hub accumulates cycles one-for-one with engine flight cycles, based on the recorded readings (1000 at 8000 and 1400 at 8400). The projection is an estimate and should be confirmed.
- **Note:** The 2025-10-29 engine cycle reading (8000) was used as the effective-date count for the 100-cycle window.
- **Note:** No engine shop visit events are recorded, so no shop visit has yet triggered the removal requirement.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row 1 (P/N 2A4802, S/N PKLBST5005, limit 4,000)

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model is listed and the installed HPT 1st-stage hub's serial number (PKLBSK9287) matches a Table 1 entry with a 100-cycle removal limit; the hub shows 2400 cycles since new, so it is past that limit. Removal at the next engine shop visit, or within 100 flight cycles of the 2025-10-29 effective date, whichever is later, is required, subject to confirming the part-number suffix.
- **Stated timing:** At the next engine shop visit after 2025-10-29 or within 100 flight cycles from 2025-10-29, whichever occurs later; the installed hub already exceeds its listed 100-cycle removal limit.
- **Missing fact:** Installed P/N is recorded as 2A5001-01, while Table 1 lists P/N 2A5001. The dash suffix must be confirmed as the same listed part number before the match is final. The serial number matches exactly.
- **Missing fact:** Engine flight-cycle counter on the effective date is needed to compute the 100-flight-cycle deadline and the latest engine flight-cycle count for removal.
- **Missing fact:** No events are recorded. Whether any engine shop visit (separation of major mating H-P flanges) has occurred or is scheduled is unknown and determines when removal is due.
- **Missing fact:** The installed HPT 2nd-stage hub serial number SYN-HUB2-0029 is not in Table 1 for P/N 2A4802, so no match is found on the supplied record. Confirm the S/N is correct.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The directive is in force: effective 2025-10-29, before the 2026-02-01 question date.
- **Note:** The 2400 cycles-since-new figure for the HPT 1st-stage hub exceeds the 100-cycle limit listed for its S/N. The 2nd-stage hub has no Table 1 match on its serial number.
- **Note:** The 2025-10-29 effective date is the anchor for the 100-flight-cycle window, but the engine flight-cycle counter on that date is not in the record, so no cycle deadline can be computed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row P/N 2A5001, S/N PKLBSK9287, limit 100 cycles

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
