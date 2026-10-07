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
- **Summary:** The engine is a supported V2527-A5 with an installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) that is listed in Table 1 with a 5,500-cycle removal limit. The hub has about 2,400 cycles remaining, so it must be removed at the next engine shop visit before it exceeds that limit, and the 100-cycle alternative window from the effective date has already passed.
- **Stated timing:** At the next engine shop visit after the October 29, 2025 effective date and before the hub exceeds 5,500 cycles since new (engine flight cycle about 45,050 at the current utilization rate of about 1,450 cycles per year); the 100-flight-cycle alternative (engine cycle 41,300) has already passed, so the governing deadline depends on how the 'whichever occurs later' clause is read.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** events[] contains no engine shop visit record; the next engine shop visit date and whether it has occurred since the effective date are not confirmed
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new[2026-09-26] is not dated; the 3,100 value is assumed to be current, consistent with 1,650 at 2025-10-29 plus 1,450 engine cycles elapsed
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0001) does not match any Table 1 entry, so no 2nd-stage removal obligation is indicated by the supplied record.
- **Note:** The engine's cycle counter read 41,200 on 2025-10-29 and 42,650 on 2026-09-26, so 1,450 cycles were flown in the interval.
- **Note:** The hub's dated reading of 1,650 cycles on 2025-10-29 plus 1,450 elapsed engine cycles matches the undated current value of 3,100, supporting the 2,400 remaining cycles figure.
- **Note:** The operator's record contains no AD status claim or AMOC for this directive.

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine is a supported V2533-A5 within the applicability of AD 2025-19-13, which is in force since October 29, 2025. Neither installed hub's part number and serial number matches a P/N and S/N pair in Table 1 to paragraph (g), so no removal is triggered by the supplied record, but the installation prohibition in paragraph (h) continues to apply.
- **Missing fact:** installed_components[HPT 1st-stage hub].serial_number should be verified against the physical hub data plate, because PKLBST5012 is close to the Table 1 listed serial PKLBST5011 (5,500 cycles) and a transcription error would change the result
- **Missing fact:** installed_components[HPT 2nd-stage hub].serial_number should be confirmed as SYN-HUB2-0002 from source records
- **Missing fact:** events[] is empty, so no engine shop visit history is recorded; a future shop visit separating major mating flanges would trigger the paragraph (g) review
- **Note:** This is a screening aid, not a compliance determination. The result reflects only the supplied record: neither installed hub matches a listed P/N and S/N pair.
- **Note:** The record has no events, so the paragraph (g) shop-visit trigger cannot be evaluated for the past and is not established by the record.
- **Note:** The hub cycles since new (4,200) are not compared against any limit because no installed serial number is listed in Table 1.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g)

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2025-19-13 is in force on the question date and covers the V2524-A5, which is a listed model, so the engine is within its applicability. The screen cannot finish because the installed HPT 1st-stage hub has an unknown serial number and unknown cycles since new, so it cannot be tested against Table 1; the installed HPT 2nd-stage hub (S/N SYN-HUB2-0003) does not match any Table 1 entry.
- **Stated timing:** If the 1st-stage hub is a Table 1 unit: remove and replace at the next engine shop visit after October 29, 2025 before exceeding its listed removal cycle limit, or within 100 flight cycles of October 29, 2025, whichever occurs later. No shop visit is recorded.
- **Missing fact:** installed_components[HPT 1st-stage hub].serial_number: needed to test whether the installed P/N 2A5001 hub is one of the four listed serial numbers in Table 1
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new: needed to compare against the listed removal cycle limit for the matching serial number, if any
- **Missing fact:** engine flight-cycle counter for SYN-V2500-0003: needed to compute the 100-flight-cycle deadline from October 29, 2025 and any remaining cycles; no engine cycle field is in the record
- **Missing fact:** events: no engine shop visit is recorded, so whether any shop visit has occurred or will occur since October 29, 2025 is unknown
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003, 5100 cycles since new) matches a listed P/N but its serial number is not in Table 1, so the record does not place it in the table; this is not a finding that it is eligible for installation.
- **Note:** The 1st-stage hub P/N 2A5001 matches a listed P/N, but with the serial number unknown it is not established as a listed unit, and it is not recorded as matched.
- **Note:** The record has no engine flight-cycle counter, so the 100-flight-cycle deadline cannot be computed.
- **Note:** The June 2025 NPRM text was superseded by the final rule; the final rule text was used for this screen.
- **Note:** This is a screening aid only and does not state compliance, airworthiness, or return-to-service status.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not an IAE V2500 model listed in the supported scope, so this screen makes no applicability determination under Federal Register document 2025-18469.
- **Note:** The engine model PW1133G-JM is a Pratt & Whitney model and is not among the supported IAE V2500 models.
- **Note:** The installed_components and events lists are empty; no part-level or shop-visit comparison was performed because scope was not met.
- **Note:** This is a screening aid only and does not constitute a compliance determination.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is supported and the recorded HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSS9840) matches a listed row of AD 2025-19-13 table 1, so the hub must be removed at the next engine shop visit after October 29, 2025, or within 100 flight cycles of that date, whichever is later. The operator record shows a qualifying shop visit induction on 2025-11-12 at 18040 cycles, but does not show whether the hub was removed at that visit.
- **Stated timing:** At the next engine shop visit after October 29, 2025 (the 2025-11-12 induction, if it is the first such visit) and before the later of the listed removal cycle limit (3,900 cycles since new for this hub) or 100 flight cycles from the October 29, 2025 effective date, which gives engine flight cycle 18100.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** installed_components[HPT 2nd-stage hub].removal_status (whether the hub with P/N 2A4802 and S/N PKLBSS9840 was removed from service at the 2025-11-12 shop visit)
- **Missing fact:** events[shop_visit_induction 2025-11-12].qualifies_as_engine_shop_visit[AD 2025-19-13] (operator assertion of 'yes' needs confirmation that the separation of major mating flanges occurred)
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new[2025-11-12] (current cycles since new is recorded as 1040 without a date; the most recent dated reading is 1000 at 2025-10-29)
- **Note:** This is a screening aid and not a compliance determination. The removal status of the matched hub is not in the record, so the outcome depends on whether it was removed at the 2025-11-12 shop visit.
- **Note:** The HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0005) does not match any listed table 1 row, so it is not matched to this AD on the supplied facts. The table is a closed list of serial numbers.
- **Note:** The 2025-10-29 engine reading of 18000 cycles is treated as the effective-date cycle count; the 100-cycle window therefore ends at 18100.
- **Note:** The NPRM 2025-10764 is superseded for this screen by the final rule 2025-18469, which is the authority relied on.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine is within the scope of AD 2025-19-13, which was effective October 29, 2025. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSK9287) matches a Table 1 row with a 100-cycle removal limit, and the record shows about 90 cycles since new, so removal and replacement is required at the next engine shop visit or within 100 flight cycles of the effective date, whichever occurs later. The record shows no shop visit yet.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit before exceeding 100 cycles since new, or within 100 flight cycles of the October 29, 2025 effective date, whichever occurs later.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new[2025-11-20] is not recorded; the only undated cycles_since_new of 90 conflicts with the dated reading of 60 on 2025-10-29 and needs confirmation of its date
- **Missing fact:** events: no engine shop visit event is recorded, so whether a shop visit has occurred or is scheduled is unknown
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new is recorded without a date and cannot be checked against the 4,000, 3,900, 5,000 or 6,000 cycle limits for the listed hub serial numbers
- **Note:** Screening aid only; this is not a compliance determination and does not state that the engine or any part is compliant, noncompliant, airworthy, or approved for return to service.
- **Note:** The second installed hub (P/N 2A4802, S/N SYN-HUB2-0006) does not match any Table 1 row, so no action is triggered by it on the supplied facts.
- **Note:** The 100-cycle limit and the 100-flight-cycle clause are read together. The 25600 deadline is the later of the two, so the 25540 limit-based reading is shown as an alternative.
- **Note:** The record shows 25530 engine flight cycles on 2025-11-20 and 25500 on 2025-10-29, which is the effective date. Cycles since new of 60 on 2025-10-29 and 90 at the snapshot are consistent with 30 cycles flown between those dates.
- **Note:** Cycles since new of 90 without a date conflicts with the dated 60 reading as a timeline, so the 90-cycle figure should be confirmed before relying on the 10-cycle margin.
- **Note:** Installation date 2025-09-30 predates the AD's effective date, so this record does not show an installation after the effective date.

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 is a supported model within the AD's applicability, and the AD is in force since its October 29, 2025 effective date. Both installed hubs (HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 and HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005) are listed in Table 1, so removal is required at the next engine shop visit before the hub exceeds its removal cycle limit; the 1st-stage hub reaches its 4,800-cycle limit first, at about engine cycle 30,800.
- **Stated timing:** Remove and replace both listed hubs at the next engine shop visit after October 29, 2025, and before the HPT 1st-stage hub exceeds 4,800 cycles since new (about engine flight cycle 30,800). Under the alternative reading that the 100-flight-cycle date (engine cycle 30,100) is the operative deadline, the action is already overdue.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** events[] is empty, so the record does not show whether an engine shop visit has occurred since October 29, 2025; installed_components and events should be checked for any shop visit after the effective date.
- **Missing fact:** Whether the HPT 1st-stage hub and HPT 2nd-stage hub installed on this engine have been removed or replaced; the record shows both still installed.
- **Missing fact:** Confirmation that the cycles_since_new values (1st-stage 4,300; 2nd-stage 2,300 at snapshot) are current and match the engine flight-cycle counter, since they are consistent with the dated October 29, 2025 readings plus 300 cycles.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The 1st-stage hub has 500 cycles remaining to its 4,800 limit and the 2nd-stage hub has 1,700 cycles remaining to its 4,000 limit, so the 1st-stage hub drives the earliest deadline.
- **Note:** Engine cycles rose 300 between October 29 and December 1, 2025, and each hub's cycles since new rose by the same 300, so the readings are internally consistent.
- **Note:** The AD's removal is tied to an engine shop visit, and the record contains no shop visit event, so the action timing depends on whether a shop visit occurs before the limit is reached.
- **Note:** The FAA states the AD is a terminating action only for the removal portion; the installation prohibition continues to apply.

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a supported V2528-D5 and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) is listed in Table 1 with a 6,200-cycle removal limit. The hub must be removed and replaced at the next engine shop visit before it exceeds 6,200 cycles since new, which at the current cycle rate is engine flight cycle 54,200; the alternative 100-cycle clause from the effective date has already passed, so the reviewer should confirm which reading applies.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 6,200 cycles since new (about 3,700 further cycles). Under the alternative reading, the 100-flight-cycle window ended at engine flight cycle 50,100, which has passed.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** installed_components[HPT 2nd-stage hub].serial_number: the record shows 'unknown', so it cannot be checked against the Table 1 2A4802 serial numbers.
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new: unknown, so the hub cannot be checked against its Table 1 removal cycle limit.
- **Missing fact:** events: no engine shop visit events are recorded, so the timing of the next shop visit and whether it has occurred cannot be confirmed.
- **Missing fact:** Whether the 2A5001 hub S/N PKLBST7489 has been removed or replaced since the 2025-10-29 reading is not recorded.
- **Missing fact:** Operator confirmation of the intended reading of the 100-flight-cycle clause in paragraph (g).
- **Note:** This is a screening aid and not a compliance determination. The engine's cycle counts are taken from the record as supplied.
- **Note:** The 1st-stage hub cycles since new are 2,000 at 2025-10-29 (engine flight cycle 50,000) and 2,500 at 2026-03-10 (engine flight cycle 50,500). Both readings are consistent with 500 engine cycles over the same interval.
- **Note:** The 2nd-stage hub record is incomplete, so this screen does not evaluate it. The serial number must be confirmed against the four 2A4802 entries in Table 1 before the 2nd-stage hub can be cleared or flagged.
- **Note:** The record contains no engine shop visit events. The absence of an event is not evidence that no shop visit has occurred.

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2522-A5 is within the applicability of AD 2025-19-13 (effective October 29, 2025), so the directive applies to this engine. The record lists no installed components and no events, so it cannot be determined whether any listed HPT 1st-stage or 2nd-stage hub is installed, and the required-action timing cannot be established.
- **Stated timing:** At the next engine shop visit after October 29, 2025, before exceeding the applicable removal cycle limit in table 1, or within 100 flight cycles from October 29, 2025, whichever occurs later. No shop visit is recorded and no flight-cycle counter is supplied, so no calendar or cycle deadline can be computed. The installation prohibition in paragraph (h) applies from October 29, 2025 regardless.
- **Missing fact:** installed_components[HPT 1st-stage hub].part_number
- **Missing fact:** installed_components[HPT 1st-stage hub].serial_number
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new
- **Missing fact:** installed_components[HPT 2nd-stage hub].part_number
- **Missing fact:** installed_components[HPT 2nd-stage hub].serial_number
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new
- **Missing fact:** engine.flight_cycles
- **Missing fact:** events[engine shop visit] (whether any engine shop visit has occurred or is scheduled, as defined in paragraph (i)(2))
- **Missing fact:** engine.flight_cycles[2025-10-29] (engine flight-cycle counter at the AD effective date, needed for the 100-cycle limit)
- **Note:** The engine record has an empty installed_components list. Under the screening conventions, an absent or unknown record is not evidence that the listed hubs are absent or unaffected, so no hub-level match can be made.
- **Note:** The record contains no events, so no engine shop visit is recorded and the record does not show whether any engine shop visit has occurred since October 29, 2025.
- **Note:** The directive is in force as of the question date (effective October 29, 2025). The proposed rule 2025-10764 is superseded by the final rule for this screen and was not used to set the deadline.
- **Note:** The final rule states that the installation prohibition in paragraph (h) continues after all affected hubs are removed, so the applicability does not end with removal.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model V2500-A1 is not among the supported IAE V2500 models for this screen, so no applicability determination is made and no action is triggered by this screen.
- **Note:** The engine model V2500-A1 is outside the screen's supported model list, so this result makes no applicability determination under the directive.
- **Note:** The record lists an installed HPT 1st-stage hub with P/N 2A5001 and S/N PKLBST5011, which appears in table 1 to paragraph (g). That observation is not an applicability or compliance determination for this engine.
- **Note:** The screen does not state any compliance status for this engine or part.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The engine is a supported V2527-A5 with a 3rd stage HPC rotor blade set recorded as P/N 6A8353, which is listed in the directive's applicability, and AD 2026-17-03 has been in force since September 24, 2026. Its replacement requirement is triggered only at the next engine shop visit after that date where the 3rd stage HPC rotor blade is exposed, and the record shows no events, so no such shop visit is recorded.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed; no calendar or cycle deadline applies before that event.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** events[] is empty; a dated engine shop visit history since 2026-09-24 is needed to determine whether an engine shop visit with blade exposure has occurred
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].serial_number is recorded as 'not tracked at set level'; set-level blade serial or traceability is not available to confirm each blade's P/N
- **Missing fact:** engine.engine_flight_cycles counter is not present in the engine record, so no cycle-based figure can be computed
- **Missing fact:** Whether every blade in the installed set is P/N 6A8353 (the record gives one P/N for the set) is not confirmed
- **Missing fact:** Whether the set was already replaced with parts eligible for installation (P/N 6C8368, 6C8403, a later approved P/N, or 6A8353-001/6A8688-001) is not recorded; no ad_records or amoc_claims are present
- **Note:** This is a screening aid, not a compliance determination. The record shows no engine shop visit events, so the trigger has not been recorded as met; this is not a finding that the engine is or is not in compliance.
- **Note:** The 2026 final rule supersedes the 2025 NPRM wording; the NPRM's 'next 3rd stage HPC rotor blade exposure' language is not the operative text.
- **Note:** Paragraph (h)(2) defines exposure as removal of any 3rd stage blade from the HPC stage 3 to 8 drum, which is narrower in practice than a full engine shop visit and is the event to watch during any shop visit.
- **Note:** Replacement with new or reworked blades under the directive is the required outcome of the trigger; the cost figures in the preamble are not part of the directive requirement.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The engine is a supported V2533-A5 and the directive is in force as of 2026-10-05. The only installed 3rd stage HPC rotor blade set is recorded as P/N 6C8368, which is a part eligible for installation under the directive, not one of the listed applicability P/Ns (6A8353 or 6A8688), so the screen places the engine outside the directive's applicability on these facts.
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].part_number confirmation that every blade in the set is P/N 6C8368 or another eligible P/N, not 6A8353 or 6A8688, since the record gives one set-level P/N and the serial is not tracked at set level
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].serial_number or per-blade P/N records, because the set serial is recorded as not tracked
- **Note:** This is a screening aid, not a compliance determination. The event list is empty, so no engine shop visit or blade exposure is recorded.
- **Note:** If any blade in the set is actually P/N 6A8353 or 6A8688, applicability would need to be re-screened; the set-level record alone cannot exclude mixed P/Ns.
- **Note:** The 2026-18423 correction only changes paragraph (g) wording from 'blade' to 'blade is exposed'; it does not change the applicability analysis here.
- **Note:** If the engine later undergoes a shop visit with the HPC stage 3 to 8 drum exposed and an applicable blade is present, the replacement obligation in paragraph (g) would need review then.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC rotor blade set P/N 6A8688, which is listed in AD 2026-17-03, so the AD applies. The only shop visit that the record says qualifies was inducted 2026-09-14, before the AD's 2026-09-24 effective date, so the replacement trigger (the next engine shop visit after the effective date with the blade exposed) is not met on the facts given.
- **Stated timing:** Replace the full set of 3rd stage HPC rotor blades with parts eligible for installation at the next engine shop visit after 2026-09-24 in which the 3rd stage HPC rotor blade is exposed. No action is due from the 2026-09-14 induction.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** engine.flight_cycles: the engine flight-cycle counter, needed to state any cycle-based deadline or limit
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].serial_number: blade serial numbers are not tracked at set level, so the individual blades cannot be identified
- **Missing fact:** operator.ad_records[AD 2026-17-03]: the operator's recorded AD status, which is a claim to check and is not part of this screen's conclusion
- **Missing fact:** Confirmation of whether the 2026-09-14 induction was an engine shop visit under paragraph (h)(3) (the operator's qualifies flag is asserted, not verified); the induction date precedes the effective date, so the flag does not change the outcome
- **Missing fact:** Confirmation of the exact 2026-09-30 exposure facts, including whether the removed blade was 6A8688 or 6A8353 and whether it was removed from the HPC stage 3 to 8 drum
- **Note:** The operator's record marks the 2026-09-14 induction as qualifying as an engine shop visit, but that induction predates the 2026-09-24 effective date, so the AD's trigger does not fall on it. The 2026-09-30 blade removal occurred during that earlier visit.
- **Note:** This is a screening aid. It makes no compliance determination and does not state that the engine or any part is compliant or noncompliant or approved for return to service.
- **Note:** The correction at 2026-18423 changes paragraph (g) from 'rotor is exposed' to 'blade is exposed'. Under either wording, the trigger still depends on a shop visit after the effective date, so the outcome above does not change.
- **Note:** The record does not include an engine flight-cycle counter, so no cycle-based deadline can be computed. The next qualifying shop visit will need to be checked against the effective date when it occurs.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2026-17-03 (as corrected) applies to this V2524-A5 engine because it has 3rd stage HPC rotor blade P/N 6A8353 installed, and it was in force by 2026-10-05. The 2026-10-01 shop visit is recorded as qualifying and came after the 2026-09-24 effective date, but the record says no 3rd-stage blade was removed from the stage 3-8 drum, so the AD's defined blade exposure is not shown and the replacement trigger needs review.
- **Stated timing:** Replacement of the full 3rd stage HPC rotor blade set was due at the engine shop visit after 2026-09-24 where a blade was exposed. If a blade was removed from the stage 3-8 drum during the 2026-10-01 to 2026-10-04 visit, that requirement was due before the engine returned to service on 2026-10-04, and this screen cannot confirm a later date.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** Whether any 3rd stage HPC rotor blade was removed from the HPC stage 3 to 8 drum during the 2026-10-01 shop visit (the AD's defined blade exposure in paragraph (h)(2)); the record states none was removed but also says the HPC rotor was exposed.
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].serial_number (set-level serial not tracked, so the blade set's identity and any prior replacement cannot be confirmed)
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].part_number confirmed as the original 6A8353 blades still installed, with no prior replacement to 6C8368, 6C8403, a later approved P/N, or 6A8353-001/6A8688-001
- **Missing fact:** engine.total_flight_cycles or the engine flight-cycle counter at the question date (not supplied)
- **Missing fact:** operators[AD 2026-17-03] or ad_records[AD 2026-17-03]: operator's recorded AD status for this engine (not supplied)
- **Note:** This is a screening aid, not a compliance determination; no statement of compliance or airworthiness is made.
- **Note:** The 2026-10-01 shop visit is recorded by the operator as qualifying as an engine shop visit under AD 2026-17-03; that assertion was not independently verified.
- **Note:** The record's 2026-10-02 event says the HPC rotor was exposed for inspection but no blade was removed from the stage 3-8 drum. The AD defines exposure by blade removal, so the record does not establish the trigger, but the record's wording is close enough that a reviewer should confirm with maintenance records.
- **Note:** If a blade removal is confirmed, the replacement obligation attached to the 2026-10-01 shop visit, before the 2026-10-04 return to service, and no cycle-based deadline can be computed from the record.
- **Note:** The NPRM (2025-20088) and its differing paragraph (g) wording are superseded by the final rule and are not relied on. The final rule's paragraph (g) is amended by the correction 2026-18423.
- **Note:** No alternative reading with a computed flight-cycle deadline is listed because the record has no cycle counter.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2527E-A5 is a supported model, and its installed 3rd stage HPC rotor blade set is recorded as P/N 6A8353, which the proposed applicability paragraph lists. However, Federal Register document 2025-20088 is an NPRM with no effective date, so it cannot yet require any action on this engine as of 2026-01-15.
- **Missing fact:** events[] (no 3rd stage HPC rotor blade exposure history is recorded; a future exposure would be the trigger if the AD is adopted in final form)
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].serial_number (recorded as not tracked at set level; set-level serial status does not affect the P/N-based applicability text)
- **Note:** This is a screening aid only. The directive is a proposal, not a final rule, so it does not impose a required action on this engine as of the question date; the applicability finding is limited to the proposed text.
- **Note:** If the proposal is adopted as a final rule with an effective date, the replacement action would be triggered only at the next 3rd stage HPC rotor blade exposure after that effective date, and the event history would then need to be checked.
- **Note:** The engine record does not state whether any 3rd stage HPC rotor blade has been removed from the stage 3 to 8 drum since the record began; this is not evidence either way.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 is in force (effective October 10, 2025) and applies to the V2527-A5 engine, which is a supported model. The operator's record states that neither its approved maintenance program nor TLM ALS paragraph B.1 yet includes table 1 to paragraph (g), so the required ALS and program revisions must be made by January 8, 2026, which is still open as of the question date.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e., by January 8, 2026: revise paragraph B.1 of the Maintenance Scheduling section of the ALS in the applicable TLM under (g)(1), and, for air carrier operations, revise the existing approved maintenance or inspection program under (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** engine.total_flight_cycles[2025-11-15] (engine flight-cycle counter is not in the record, so no cycle-based figure can be given)
- **Missing fact:** operator.maintenance_program_revision: the record does not state whether the revision is the approved program identified for air carrier operations; confirm which approved maintenance or inspection program applies to this engine
- **Missing fact:** TLM applicability: the record does not state the TLM revision or P/N (2A4408 for V2500-A5 per (g)(1)(i)) in use for this engine, so the applicable TLM cannot be confirmed from the record
- **Missing fact:** installed_components: no component records are provided, so the HPT Stage 1 hub (P/N 2A5001) and HPT Stage 2 hub (P/N 2A4802) installation status cannot be checked against table 1
- **Note:** Screening aid only, not a compliance determination. The operator's statement that neither the program nor the TLM ALS yet incorporates table 1 is an operator assertion; it is treated as the record's status, not as a verified finding.
- **Note:** The deadline of January 8, 2026 has not passed as of 2025-11-15, so the record does not show a missed deadline.
- **Note:** The NPRM (2024-26092) was superseded by the final rule for this analysis; the final rule text was used. The final rule's revised (g)(1) and (g)(2) and the corrected task numbers (72-45-31-200-009) govern.
- **Note:** The inspection tasks are performed at piece-part exposure under the TLM, so the record's event and installed-component fields, which are empty, would be needed to determine whether any inspection has been triggered by a shop visit.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 (effective October 10, 2025) covers IAE AG V2522-A5 engines, and this engine's model is in its applicability list, so the one-time ALS/TLM revision in paragraph (g)(1) applies and is due by January 8, 2026. The record has no installed HPT hub components and no cycle counter, so the piece-part hub inspections and the air carrier program revision in (g)(2) cannot be screened.
- **Stated timing:** Revise paragraph B.1 of the Maintenance Scheduling section of the ALS in the applicable TLM within 90 days after the October 10, 2025 effective date, i.e., by January 8, 2026; for air carrier operations, revise the existing approved maintenance or inspection program within the same 90 days. The HPT stage 1 and stage 2 hub inspections are due at piece-part exposure.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** installed_components[HPT Stage 1 Hub] (P/N 2A5001) record, including serial number and piece-part exposure history, is absent; the record lists no installed components
- **Missing fact:** installed_components[HPT Stage 2 Hub] (P/N 2A4802) record, including serial number and piece-part exposure history, is absent; the record lists no installed components
- **Missing fact:** operator.air_carrier_operation is unknown, so it cannot be established whether paragraph (g)(2) applies
- **Missing fact:** engine.total_flight_cycles (engine flight-cycle counter) is not supplied, so no cycle-based deadline can be computed
- **Missing fact:** Whether the operator's TLM or ALS revision for paragraph (g)(1) has already been made is not recorded
- **Note:** The engine record contains no installed components, no events, no ad_records, and no cycle counter, so hub-specific screening and cycle-based deadlines cannot be completed.
- **Note:** The January 8, 2026 date counts 90 days from the October 10, 2025 effective date stated in the Federal Register record. A reviewer should note that counting from the September 5, 2025 publication date would give December 4, 2025; the directive text ties the period to the effective date, so that alternative is not adopted here.
- **Note:** The final rule says the piece-part hub inspections are performed under other regulations once the ALS or program is revised, so the record needs the hub serial and exposure history before any inspection status can be assessed.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model is in the supported scope and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) matches a row of Table 1, so the directive applies to this engine. The directive is not yet effective (October 29, 2025), and no engine shop visit is recorded, so the removal action is triggered only by a future shop visit after the effective date.
- **Stated timing:** Not yet effective (effective October 29, 2025). Once effective, remove and replace the listed hub at the next engine shop visit after October 29, 2025, before exceeding its 6,000-cycle removal limit or within 100 flight cycles from the effective date, whichever occurs later.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** engine.flight_cycles_counter[2025-10-15] (engine flight-cycle counter, needed to compute any engine-cycle deadline)
- **Missing fact:** engine.flight_cycles_counter[2025-10-29] (engine flight-cycle counter on the directive's effective date, needed for the 100-flight-cycle window)
- **Missing fact:** events[] (confirmation of whether any engine shop visit occurs after 2025-10-29; none is recorded)
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new[2025-10-15] (confirm the 990-cycle value is current as of the question date)
- **Missing fact:** Confirmation of the reading of the 'whichever occurs later' deadline in paragraph (g); the directive text does not state whether the 100-flight-cycle window runs independently of a shop visit
- **Note:** Screening aid only; this is not a compliance determination. The engine record shows no engine shop visit events, and the record is silent on the engine's own flight-cycle counter, so no engine-cycle deadline can be computed.
- **Note:** The HPT 1st-stage hub (S/N SYN-HUB1-0018) is not listed in Table 1 and is not matched; its 2000 cycles_since_new do not bear on this directive's limits.
- **Note:** Paragraph (g)'s timing wording admits two readings: removal at the next post-effective shop visit before the cycle limit, or within 100 flight cycles of October 29, 2025 regardless of shop visit. The record lacks the engine-cycle data needed to compare them, so no alternative deadline is stated.
- **Note:** The hub's remaining cycles (5,010) are computed from the listed 6,000-cycle limit and the 990 cycles since new recorded on 2025-10-15.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a listed V2531-E5 and the directive is in force as of the question date. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in table 1 with a 4,800-cycle removal limit and its recorded cycles since new (4,990) already exceed that limit, so paragraph (g) requires removal and replacement by the later of the two prongs, which is 100 flight cycles from the October 29, 2025 effective date (engine flight cycle 60,100).
- **Stated timing:** Remove and replace the listed HPT 1st-stage hub within 100 flight cycles of the AD effective date of October 29, 2025, i.e., by engine flight cycle 60100, because the 4,800-cycle limit has already been exceeded and the shop-visit prong cannot be met before exceeding it. Do not install any listed hub after the effective date.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new: reconcile the top-level value 4990 with the dated reading 4950 at 2025-10-29 to confirm the current cycles since new
- **Missing fact:** installed_components[HPT 2nd-stage hub].serial_number: serial SYN-HUB2-0019 is not in table 1 for P/N 2A4802, so confirm it is correctly recorded and that the hub is not a listed serial
- **Missing fact:** installed_components[HPT 2nd-stage hub].installed_at: installation date not recorded, so its install history cannot be confirmed
- **Missing fact:** events: no engine shop visit history is recorded; whether any event qualifies as an engine shop visit cannot be determined from the record
- **Missing fact:** engine.engine_cycle_readings[2025-10-29]: confirm the 60000 flight-cycle reading is the value at the effective date for the 100-cycle count
- **Note:** This is a screening aid and not a compliance determination; the record is synthetic.
- **Note:** The record's top-level cycles_since_new of 4990 for the HPT 1st-stage hub exceeds the 4,800 limit; the dated 2025-10-29 reading of 4950 also exceeds it, so the result does not depend on which value is used. Using 4950 would give a remaining value of -150.
- **Note:** The HPT 2nd-stage hub with S/N SYN-HUB2-0019 does not match any listed P/N and S/N combination in table 1, so no 2nd-stage hub action is shown on this record, but this depends on confirming the serial number.
- **Note:** No engine shop visit events are recorded, so the shop-visit prong cannot be evaluated and the 100-cycle prong governs the deadline.

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (FR 2021-11960) was in force on 2022-03-01, but it is superseded by FR 2022-02574 (AD 2022-02-09), effective 2022-03-15. The V2533-A5 engine has installed HPT 1st-stage and 2nd-stage disks whose part numbers match the directive, but applicability turns on whether the disk serial numbers appear in the Appendix A tables of the service bulletins, which were not supplied, and the record has no engine cycle counter or shop-visit history since 2021-07-13.
- **Stated timing:** If the disk serial numbers are listed, the USI is due at the next engine shop visit after 2021-07-13 or before the HPT disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. No shop visit is recorded in the events list, but the record does not confirm that none occurred.
- **Missing fact:** installed_components[HPT 1st-stage disk].serial_number confirmation that SYN-DISK1-0020 is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713, Revision 1 (the service bulletin text was not supplied)
- **Missing fact:** installed_components[HPT 2nd-stage disk].serial_number confirmation that SYN-DISK2-0020 is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713, Revision 1 (the service bulletin text was not supplied)
- **Missing fact:** engine flight-cycle counter for SYN-V2500-0020 and the flight cycles accumulated by each disk since 2021-07-13 (no engine cycle field in the record)
- **Missing fact:** events[] history confirming whether any engine shop visit, as defined in paragraph (h)(1), occurred on or after 2021-07-13 and whether it qualifies_as_engine_shop_visit for AD 2021-11-15
- **Missing fact:** whether either disk has operated in a high-thrust engine, which affects compliance timing under the superseding AD 2022-02-09 (not yet effective on the question date)
- **Note:** This is a screening aid, not a compliance determination. The record does not establish that either disk is listed, so the answer is needs_review rather than applies.
- **Note:** AD 2021-11-15 is in force on 2022-03-01, but FR Doc 2022-02574 supersedes it effective 2022-03-15. The superseding AD's compliance times for disks that have operated in high-thrust engines are shorter; the Figure 1 compliance table is an image not included in the supplied text, so those times cannot be computed here.
- **Note:** The record lists no installed-component history and no engine flight-cycle counter, so no cycle-based deadline or remaining-cycles figure can be computed.
- **Note:** Synthetic record (SYN- identifiers).
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (FR doc 2022-02574) is published but not effective until March 15, 2022, so it cannot require action on the March 1, 2022 question date. The V2533-A5 engine has installed HPT disks whose part numbers match the directive, but their serial numbers cannot be checked against the Appendix A tables, which were not supplied, and the Figure 1 compliance times are also missing.
- **Missing fact:** installed_components[HPT 1st-stage disk].serial_number is not confirmed against Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713, Revision 1 (the Table 1 listing was not supplied)
- **Missing fact:** installed_components[HPT 2nd-stage disk].serial_number is not confirmed against Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713, Revision 1 (the Table 2 listing was not supplied)
- **Missing fact:** Figure 1 to paragraph (g)(1) of AD 2022-02574, which sets the compliance time for the V2533-A5 USI, was not supplied (it is an image in the text)
- **Missing fact:** The engine-flight-cycle counter at the directive's effective date (March 15, 2022) is not recorded, so no cycle deadline can be computed
- **Missing fact:** events[] is empty; the record does not show whether any engine shop visit has occurred, and the operator record does not state whether any event qualifies as an engine shop visit
- **Missing fact:** installed_components[HPT 1st-stage disk] and installed_components[HPT 2nd-stage disk] operating history: whether either disk has operated on a high-thrust model engine (V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, or V2533-A5), which affects the compliance tier under (g)(3)(ii) and (g)(4)(ii) for low-thrust models
- **Note:** This is a screening aid, not a compliance determination. Nothing here states that the engine or its disks are compliant or noncompliant, or approved for return to service.
- **Note:** The engine model V2533-A5 is a supported model. The engine serial number and disk serial numbers are synthetic (SYN-) identifiers.
- **Note:** AD 2021-11-15 (FR 2021-11960, Amendment 39-21577, effective July 13, 2021) was in force on March 1, 2022, and is superseded by AD 2022-02-09 effective March 15, 2022. Its requirements are not evaluated here and may need separate review by the reviewer for the period before March 15, 2022.
- **Note:** The Figure 1 timing and the Appendix A serial number tables are needed before any deadline or applicability can be finalized. Do not infer a deadline from the 3,200-cycle or 10-cycle language in the text, since the Figure 1 compliance times were not supplied.
- **Note:** The events list is empty. The record does not say whether an engine shop visit has occurred, so this is not evidence that no shop visit occurred or that no part is affected.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (superseding AD 2021-11-15) is in force on the question date and covers V2530-A5 engines. Both installed disks carry part numbers listed for the V2530-A5 (2A5001 for the HPT 1st-stage disk, 2A4802 for the HPT 2nd-stage disk), but applicability also turns on whether each serial number appears in Appendix A of the referenced NMSB, which was not supplied, and the Figure 1 compliance time was not reproduced, so no deadline can be computed.
- **Stated timing:** Under paragraphs (g)(1) and (g)(2), the USI of each disk is due within the compliance time in Figure 1 to paragraph (g)(1), or within 10 flight cycles after 2022-03-15, whichever occurs later. Figure 1 was not reproduced in the supplied text, so the due point cannot be stated. The record shows no engine shop visit events, so none is established as having occurred.
- **Missing fact:** Whether serial SYN-DISK1-0021 (HPT 1st-stage disk, P/N 2A5001) is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713, Revision 1 (installed_components[HPT 1st-stage disk].serial_number is recorded but the listing is not in the supplied text)
- **Missing fact:** Whether serial SYN-DISK2-0021 (HPT 2nd-stage disk, P/N 2A4802) is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713, Revision 1
- **Missing fact:** Content of Figure 1 to paragraph (g)(1) (the compliance time for the V2530-A5 USI), which is not reproduced in the supplied text
- **Missing fact:** engine.flight_cycles at the question date, needed to test the 10-flight-cycle floor and any cycle-based limit
- **Missing fact:** Whether any engine shop visit (separation of H-P flanges, as defined in paragraph (h)(1)) has occurred since 2022-03-15; events is empty and that is not evidence that none occurred
- **Missing fact:** Whether either disk already received a USI under the prior AD 2021-11-15 or any other documented inspection that could be relied on, which is not recorded in the engine record
- **Note:** Screening aid only; this is not a compliance determination. The engine record's installed disk serial numbers are SYN- synthetic identifiers, and the Appendix A tables that would confirm listing were not supplied.
- **Note:** The engine model V2530-A5 is within the supported scope list.
- **Note:** The V2530-A5 is a high-thrust model, so paragraphs (g)(1) and (g)(2) apply directly; the low-thrust paragraphs (g)(3) and (g)(4) and the thrust-history condition in the 2022 AD do not drive this engine's timing.
- **Note:** Paragraph (i) credit for previous actions refers only to NMSB V2500-E5-72-0015 for V2531-E5 engines and does not apply to this V2530-A5 record.
- **Note:** The record contains no flight-cycle counter, so no cycle-based deadline can be computed.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The installed HPT 1st-stage disk (P/N 2A5001, S/N PKLBSH1829) matches paragraph (c)(1) of this in-force AD on a listed V2533-A5 engine, so the AD applies. A one-time ultrasonic inspection is required within 10 flight cycles after the July 19, 2021 effective date, which is engine flight cycle 33010 on the record's reading, and the record shows no USI event.
- **Stated timing:** Perform the ultrasonic inspection of the HPT 1st-stage disk within 10 flight cycles after the July 19, 2021 effective date, i.e., by engine flight cycle 33010 (6 cycles after the 2021-07-20 snapshot of 33004).
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** operator.ultrasonic_inspection_status or events[] record of an HPT 1st-stage disk USI under IAE NMSB V2500-ENG-72-0713 (none recorded; events is empty)
- **Missing fact:** ad_records[2021-11-51] operator-recorded AD status for this engine (not supplied)
- **Missing fact:** Content of Table 1 to paragraph (g)(1) and Table 2 to paragraph (g)(2), which are provided only as images and were not supplied; the applicability text in (c) was used instead
- **Missing fact:** Confirmation of the engine flight-cycle count at the July 19, 2021 effective date beyond the single reading of 33000 in engine_cycle_readings
- **Note:** Screening aid only; this is not a compliance determination. The record contains no USI event, so whether the inspection has already been performed cannot be determined from the record.
- **Note:** The HPT 2nd-stage disk S/N SYN-DISK2-0022 is not among the listed serials in paragraph (c)(2), so it does not match that paragraph on the record as supplied.
- **Note:** The HPT 1st-stage disk match relies on the serial PKLBSH1829 appearing in paragraph (c)(1).
- **Note:** The directive is interim action; the root cause was still under investigation when issued.
- **Expected missing fact (judge on meaning):** table 1 to paragraph (g)(1) content (image-only; transcription decided in E3)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 accomplishment instructions (unavailable incorporated material)
- **Unresolved locator:** 2021-14268 (g) (g)(1)
- **Unresolved locator:** 2021-14268 (g) (g)(3)
- **Unresolved locator:** 2021-14268 preamble DATES

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-022/2021-11960: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The directive is in force on 2021-07-20 and the V2533-A5 model is within its supported model list. Whether the installed HPT 1st-stage disk (2A5001, S/N PKLBSH1829) and HPT 2nd-stage disk (2A4802, S/N SYN-DISK2-0022) are within the directive depends on serial numbers listed in NMSB tables that were not supplied, so applicability cannot be decided from this record.
- **Stated timing:** If the serial numbers are listed, the USI of each disk is due at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. No shop visit is recorded in the supplied events, and the cycle count on 2021-07-13 is not supplied.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015 for V2531-E5 only) listing the HPT 1st-stage disk serial numbers, needed to confirm whether installed_components[HPT 1st-stage disk].serial_number PKLBSH1829 is within the directive
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 listing the HPT 2nd-stage disk serial numbers, needed to confirm whether installed_components[HPT 2nd-stage disk].serial_number SYN-DISK2-0022 is within the directive
- **Missing fact:** Engine flight-cycle count on 2021-07-13 (the directive effective date), needed to compute the 3,200-cycle deadline; engine.engine_cycle_readings[2021-07-13]
- **Missing fact:** Engine shop visit history since 2021-07-13 as defined in paragraph (h)(1), needed to determine whether a shop visit has occurred; the events list is empty, which does not show that no shop visit occurred
- **Missing fact:** Confirmation of the disks' current status and time since last piece-part inspection, needed if a USI is performed and the piece-part note in (g)(1) applies
- **Note:** This is a screening aid and not a compliance determination. The applicability and action answers depend on serial numbers in NMSB Appendix A tables, which were not supplied.
- **Note:** Cycle bound: the engine read 33000 cycles on 2021-07-19, and cycles are non-decreasing, so cycles on 2021-07-13 were at most 33000. The 3,200-cycle deadline is therefore at most 36,200 cycles, but the exact deadline needs the 2021-07-13 reading.
- **Note:** The engine record's ad_records and amoc_claims are not present, so no operator AD status or AMOC claim is considered.
- **Note:** The engine serial number and part serial numbers are synthetic identifiers (SYN-) except PKLBSH1829, and this screen does not treat them as evidence of any status.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (FR 2025-18469, effective 2025-10-29) applies to this V2527M-A5 engine. The installed HPT 2nd-stage hub P/N 2A4802, S/N PKLBSR2100 is listed in table 1 with a 6,000-cycle removal limit and is recorded at 3,500 cycles since new, so it must be removed at the next engine shop visit before it exceeds 6,000 cycles (engine cycle 25,000). The 100-flight-cycle alternative date (engine cycle 20,100) has already passed on the record's counter, which is an interpretation point for review.
- **Stated timing:** Remove and replace at the next engine shop visit after 2025-10-29 and before the hub reaches 6,000 cycles since new (engine flight cycle 25,000). The 100-flight-cycle date (engine flight cycle 20,100) has already passed under the 'whichever occurs later' reading; under the alternative reading it is already past.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** events[engine shop visit] – whether an engine shop visit (separation of major mating H-P flanges, not excluded under (i)(2)) has occurred since 2025-10-29; the event list shows only a maintenance program revision, so none is recorded
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new[2026-10-06] – the top-level cycles_since_new of 3,500 has no stated as-of date; it is consistent with the 1,000 reading on 2025-10-29 plus 2,500 engine cycles, but confirmation is needed
- **Missing fact:** ad_records[AD 2025-19-13] – the operator's recorded AD status for this directive is absent, so no operator claim is available to check
- **Missing fact:** installed_components[HPT 1st-stage hub].serial_number – confirm that SYN-HUB1-0023 is the correct serial; it is not listed in table 1, so no match is found on the present record
- **Note:** The record's engine counter is 20,000 cycles on 2025-10-29 and 22,500 on 2026-10-06, so 2,500 cycles elapsed. The hub's cycles since new (1,000 on 2025-10-29, 3,500 on the snapshot) advance at the same rate and are consistent.
- **Note:** The operator's maintenance program revision (2025-12-01) cites AD 2025-17-16 table 1, which is a different directive. It does not appear in this directive's table 1 and does not establish compliance with AD 2025-19-13.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0023 is not in table 1 of this directive, so this screen does not match it; this is not a clearance of that hub for other purposes.
- **Note:** The 3rd stage HPC rotor blade set is outside this directive's scope and was not screened.
- **Note:** This is a screening aid only. It is not a compliance determination and does not state that the engine is compliant or noncompliant, airworthy, or approved for return to service.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The engine is a supported V2527M-A5 with a 3rd stage HPC rotor blade set P/N 6A8688 recorded as installed, which is within the directive's applicability, and the directive is in force as of 2026-10-06. Required replacement of the full blade set is triggered only at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed; the record shows no such shop visit, so no deadline is computed.
- **Stated timing:** At the next engine shop visit after the effective date of AD 2026-17-03 (September 24, 2026) where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no fixed calendar or cycle deadline applies.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** events[] shop visit record: whether the engine has been inducted into the shop for maintenance on or after 2026-09-24 (the record lists only a 2025-12-01 maintenance program revision event)
- **Missing fact:** events[] shop visit record: whether any 3rd stage HPC rotor blade was removed from the HPC stage 3 to 8 drum at that shop visit (exposure), which the record does not indicate
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].serial_number: the set is recorded as not tracked at set level, so the individual blade serial numbers and whether all blades are P/N 6A8688 are unconfirmed
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].cycles_since_new: not recorded, so blade age cannot be evaluated against any limit
- **Missing fact:** Whether the operator's planned shop visit would use parts eligible for installation (P/N 6C8368, 6C8403, a later approved P/N, or 6A8353-001/6A8688-001 modified blades) cannot be determined from the record
- **Note:** The record's 2025-12-01 maintenance program revision cites AD 2025-17-16, which is not the directive under question and was not evaluated here.
- **Note:** HPT 1st-stage and 2nd-stage hub entries are not 3rd stage HPC rotor blades and do not bear on this directive.
- **Note:** The corrected paragraph (g) reads 'blade is exposed'; the original published text read 'rotor is exposed'. This screen uses the corrected text.
- **Note:** Whether an induction on the effective date itself, 2026-09-24, counts as 'after the effective date' is not addressed by the text; a reviewer should confirm this for any shop visit near that date.
- **Note:** The engine snapshot is 22500 engine flight cycles on 2026-10-06; no cycle-based deadline is computed because the trigger is an event, not a cycle count.
- **Note:** This is a screening aid only and does not make a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 is in force (effective 2025-10-10) and applies to this supported V2527M-A5 engine. The one-time ALS and approved-program revision was due by 2026-01-08, and the record shows a revision dated 2025-12-01, which is operator-asserted and falls within that window, so no required action is triggered now. The hub inspections incorporated into the program at piece-part exposure remain continuing obligations, and an HPT 2nd-stage hub cycle-count conflict needs review.
- **Stated timing:** The paragraph (g)(1) TLM ALS revision and paragraph (g)(2) approved maintenance program revision were due within 90 days after 2025-10-10, i.e. by 2026-01-08. The record shows the revision on 2025-12-01. The table 1 inspections apply at piece-part exposure.
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new: the top-level value is 3500 at installation on 2024-01-09, but the dated reading at 2025-10-29 is 1000; the conflict needs confirmation of the correct cycle count and any hub refurbishment or replacement history.
- **Missing fact:** installed_components[HPT 1st-stage hub].installed_at and cycles_since_new_readings: no installation date or dated cycle reading is recorded for the 1st-stage hub.
- **Missing fact:** engine.maintenance_program_revision and the TLM ALS revision of 2025-12-01: the record is operator-asserted; the approved document text showing revision of paragraph B.1 of the Maintenance Scheduling section with table 1 tasks 72-45-11-200-006 and 72-45-31-200-009 is not supplied.
- **Missing fact:** events: no piece-part exposure or engine shop visit events are recorded, so whether the table 1 hub inspections have been performed or are due is unknown; installed_components[HPT 1st-stage hub] and installed_components[HPT 2nd-stage hub] would need piece-part exposure history.
- **Missing fact:** ad_records[2025-17-16]: no operator AD status record is supplied for this directive.
- **Note:** Effective date 2025-10-10 with 90 days gives 2026-01-08; the record's 2025-12-01 revision is within that window. This is a screening aid, not a compliance determination.
- **Note:** The record's maintenance_program_revision event and operator.maintenance_program_revision are operator assertions and were not independently verified.
- **Note:** The AD sets no component life limit; the 20,000-cycle replacement reference appears only in a preamble comment, so no component_cycles_remaining is computed.
- **Note:** The engine's cycle count on 2026-01-08 is not recorded, so no cycle-based deadline is computed.
- **Note:** The 3rd stage HPC rotor blade set (P/N 6A8688) is not listed in the directive and was not matched.
- **Unresolved locator:** 2025-17066 (g) Table 1 to paragraph (g)
- **Unresolved locator:** 2025-17066 preamble Discussion of Final Airworthiness Directive, Request To Clarify Responsibility for Required Actions

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine is a supported V2528-D5 within the directive's applicability, and the directive is in force. Neither installed hub matches a P/N and S/N pair in Table 1 to paragraph (g), so no removal is triggered now, but the installation prohibition in paragraph (h) still binds.
- **Stated timing:** No removal deadline is triggered by the supplied record. Paragraph (g) would apply only if an installed hub matched a listed P/N and S/N pair, and the deadline would then be the next engine shop visit or 100 flight cycles after October 29, 2025, whichever is later, and before the listed removal cycle limit is exceeded. Paragraph (h) applies from October 29, 2025.
- **Missing fact:** installed_components[HPT 2nd-stage hub].serial_number: confirm the physical serial marking of the 2nd-stage hub, because the recorded S/N PKLBST5011 is listed in Table 1 only with P/N 2A5001 (1st-stage hub), not with P/N 2A4802
- **Missing fact:** installed_components[HPT 1st-stage hub].serial_number: confirm the physical serial marking of the 1st-stage hub, since the recorded S/N SYN-HUB1-0024 is not in Table 1
- **Missing fact:** events: no engine shop visit events are recorded, so whether a shop visit has occurred or is planned is unknown; this would matter only if a listed part were installed
- **Note:** This is a screening aid, not a compliance determination. The result addresses only the installed components supplied in the record.
- **Note:** The 2nd-stage hub's S/N PKLBST5011 appears in Table 1 only under the 1st-stage hub P/N 2A5001. Under the table's P/N-and-S/N pairing, it does not match the 2nd-stage hub P/N 2A4802. Because this could be a transcription error, the physical marking should be verified against the record.
- **Note:** No ad_records or amoc_claims were supplied, so no operator-recorded AD status or AMOC claim was assessed.
- **Note:** Cycles since new are 3000 for both hubs. These values are informational only, because no matched listed part exists for a cycle-limit comparison.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g)

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine record lists a CFM56-5B4/3 model, which is not among the IAE V2500 models this screen supports, so no applicability determination is made under AD 2025-17-16 (Federal Register document 2025-17066).
- **Note:** The engine model CFM56-5B4/3 is outside the supported V2500 model scope of this screen, so no applicability or compliance determination was made.
- **Note:** The directive is in force with an effective date of October 10, 2025, but it does not reach this engine model under the stated applicability.
- **Note:** The engine record has no installed components and no events, which is noted only for completeness and does not bear on the scope determination.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine has an installed HPT 1st-stage hub whose P/N 2A5001 and S/N PKLBST7489 match a row in table 1 to paragraph (g) of AD 2025-19-13, so the removal-and-replacement requirement is triggered. The removal is due at the next engine shop visit before the hub exceeds its 6,200 cycles-since-new limit, with 2,600 cycles remaining.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 6,200 cycles since new, or within 100 flight cycles of the 2025-10-29 effective date, whichever occurs later. The 100-flight-cycle window ended at engine cycle 20,100, and the engine is now at 20,600, so the operative deadline is the next shop visit, subject to the cycle limit.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** installed_components[HPT 1st-stage hub].shop_visit_status: whether an engine shop visit (induction with separation of major mating H-P flanges, excluding the paragraph (i)(2) exceptions) has occurred since 2025-10-29, and when the next one is planned
- **Missing fact:** events[engine shop visit]: whether the 2024-06-10 overhaul-shop repair of hub PKLBST7489 involved an engine shop visit; the record has no qualifies_as_engine_shop_visit determination for it
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new[2026-03-01]: the top-level 3,600 value is taken as current; it is consistent with the 3,000 reading on 2025-10-29 plus 600 engine cycles since then, but this is not confirmed by a dated reading
- **Missing fact:** the record has no ad_records or amoc_claims for AD 2025-19-13, so the operator's recorded status and any claimed alternative means of compliance are unknown
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0026) has a listed P/N but an S/N that is not in table 1, so it is not matched to a listed part on this record.
- **Note:** Cycles remaining (2,600) are computed from the top-level cycles-since-new value of 3,600 against the 6,200 limit. The latest engine cycle of 23,200 assumes the hub accrues one cycle per engine flight cycle from the 20,600 reading, which matches the 600-cycle change observed since 2025-10-29.
- **Note:** The 2024 blend repair and the 2024 inspection predate the effective date. They do not alter the directive's removal requirement, which is keyed to P/N, S/N, cycles since new, and the next engine shop visit.
- **Note:** The 2025-10764 NPRM is superseded by the final rule 2025-18469 for this screen. This screen is not a compliance determination.

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
- **Summary:** The engine model is supported and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in Table 1 with a 4,800-cycle removal limit. The record shows 4,750 cycles since new, so removal must occur at the next engine shop visit before the hub exceeds 4,800 cycles, projected at engine flight cycle 15,300, because the 100-cycle alternative window ended at 15,100.
- **Stated timing:** At the next engine shop visit after the October 29, 2025 effective date and before the hub exceeds 4,800 cycles since new (projected at engine flight cycle 15,300). No shop visit is recorded, and the 100-cycle window from the effective date (engine flight cycle 15,100) has already passed.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new[2026-01-20] (the 4,750 value is undated; confirm it is current)
- **Missing fact:** events[] (no engine shop visit recorded; confirm whether any shop visit with separation of major mating engine flanges has occurred or is scheduled since 2025-10-29)
- **Missing fact:** amoc_claims[AD 2025-19-13].approval_reference (no FAA AMOC approval letter is on file; the claimed 5,300 CSN limit cannot be relied on without an approval)
- **Missing fact:** installed_components[HPT 2nd-stage hub].installation_date (installation history of the HPT 2nd-stage hub is needed only if its serial number is later found to be listed)
- **Note:** This is a screening aid and not a compliance determination. The matched hub is shown only as a match to a listed part and serial number.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0027) is not listed in Table 1 and was not matched. Its S/N should be verified against the listed S/Ns.
- **Note:** The operator's AMOC claim (5,300 CSN) is a claim to check only. It has no FAA approval reference and does not change the 4,800-cycle limit in this screen.
- **Note:** The engine's cycles advanced 250 between 2025-10-29 and 2026-01-20, matching the hub's cycle increase of 250, so the projection assumes one hub cycle per engine flight cycle.
- **Note:** The 2020 installation predates the effective date, and no installation event is recorded after it, so the installation prohibition is not triggered by the record.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a supported V2524-A5 and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) is listed in Table 1 of the directive, so the directive applies. Removal is required at the next engine shop visit before the hub exceeds its 4,000-cycle limit; the operator's N/A marking conflicts with the installed-part record.
- **Stated timing:** Remove the HPT 2nd-stage hub (S/N PKLBST5005) at the next engine shop visit, and before it exceeds 4,000 cycles since new (about 2,600 cycles from the 2026-02-10 reading, roughly engine flight cycle 11,000). The 100-flight-cycle alternative in paragraph (g) would have ended about engine flight cycle 8,100, which is already past, so the 'whichever occurs later' reading governs.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new[2026-02-10] (the current record shows 1400 with no date, while the 2025-10-29 reading is 1000; confirm the current value)
- **Missing fact:** events (no engine shop visit is recorded; confirm whether one is scheduled and its date and engine flight-cycle count)
- **Missing fact:** Confirmation that the hub's cycles since new track one-for-one with engine flight cycles since 2025-10-29 (the 400-cycle increase matches the engine record, but this is not confirmed)
- **Missing fact:** Whether the HPT 1st-stage hub S/N SYN-HUB1-0028 has been verified against the Table 1 list, which the record indicates it is not
- **Note:** The operator's ad_records entry marks AD 2025-19-13 as not_applicable with the note 'no affected hubs installed'. The installed HPT 2nd-stage hub (S/N PKLBST5005) matches Table 1, so that claim conflicts with the record and should be reviewed. This screen does not treat the record entry as evidence.
- **Note:** The 2nd-stage hub was installed on 2025-06-03, before the effective date, so the installation prohibition in (h) is not shown to have been triggered by that installation.
- **Note:** The HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0028) does not match any Table 1 entry on the supplied data, so no action is shown for it.
- **Note:** The 100-flight-cycle clause is already past under the 'whichever later' reading, and the analysis depends on the hub's cycles tracking engine flight cycles one-for-one. Confirm both with the maintenance records.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2525-D5 is within the directive, and the directive is in force (effective October 29, 2025). The installed HPT 1st-stage hub has the listed serial number PKLBSK9287, but its recorded P/N is 2A5001-01 rather than the listed 2A5001; if that suffix is a dash-number of the same part, its 2400 cycles since new exceed the 100-cycle removal limit, which would require removal and replacement.
- **Stated timing:** If the P/N match is confirmed: remove and replace the HPT 1st-stage hub at the next engine shop visit before exceeding 100 cycles since new, or within 100 flight cycles after October 29, 2025, whichever occurs later. The 100-cycle limit has already been exceeded, so the operative deadline is 100 flight cycles after October 29, 2025, and the engine's cycle count at that date is not in the record.
- **Missing fact:** installed_components[HPT 1st-stage hub].part_number: confirmation whether 2A5001-01 is the listed P/N 2A5001 (dash-number variant) or a different part number
- **Missing fact:** engine.total_flight_cycles (engine flight-cycle counter) as of 2026-02-01, needed to determine whether the 100-flight-cycle window after October 29, 2025 has already elapsed
- **Missing fact:** engine flight-cycle counter on October 29, 2025, needed to compute the latest engine flight-cycle count for the required action
- **Missing fact:** events: no engine shop visit or other event is recorded; any future shop visit would need to be checked against the removal requirement
- **Missing fact:** installed_components[HPT 2nd-stage hub]: serial number SYN-HUB2-0029 is not in table 1; confirm it against the listed serial numbers and the operator's records
- **Note:** This is a screening aid only and does not determine compliance or airworthiness.
- **Note:** The HPT 1st-stage hub P/N in the record (2A5001-01) differs from the table P/N (2A5001); the serial number matches exactly.
- **Note:** Under the 'whichever occurs later' wording, the 100-flight-cycle window after October 29, 2025 controls because the 100-cycle limit is already exceeded; the engine cycle count at that date is needed to say whether the window has passed.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0029) is not listed in table 1, so the record shows no match for it.
- **Note:** No ad_records or amoc_claims were supplied, and no events are recorded.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row PKLBSK9287, limit 100 cycles

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
