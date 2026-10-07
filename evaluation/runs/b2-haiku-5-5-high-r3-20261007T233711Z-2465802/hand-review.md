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
- **Summary:** Directive 2025-18469 is in force (effective 2025-10-29) and applies to this V2527-A5 engine. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) is listed in Table 1 with a 5,500-cycle removal limit, and the record shows 3,100 cycles since new, so 2,400 cycles remain; the hub must be removed at the next engine shop visit before that limit is reached.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 5,500 cycles since new (about engine flight cycle 45,050 on the record's figures). The 100-flight-cycle window from the effective date (engine flight cycle 41,300) is earlier than this and has already passed, so under the whichever-occurs-later wording it does not control.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** The record lists no events. Whether an engine shop visit (induction with separation of major mating H-P flanges, excluding the listed exceptions) has occurred since 2025-10-29 is not recorded. Any such shop visit would trigger removal of the listed hub before the cycle limit is exceeded and would need to be checked.
- **Missing fact:** No operator AD status entry for this directive is supplied. This screen does not rely on any operator-recorded status, but the operator's own record would need to be checked against this result.
- **Note:** Screening aid only; not a compliance determination. The engine's cycle readings are consistent with the part's cycles: 1,650 cycles since new at 2025-10-29 plus 1,450 engine flight cycles through 2026-09-26 gives 3,100. This assumes part cycles accrue one-for-one with engine flight cycles since installation on this engine in 2023; the latest engine flight cycle figure depends on that assumption.
- **Note:** The installed_components cycles_since_new value of 3100 has no date; it is treated as the value at the 2026-09-26 snapshot.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0001) is not matched: its serial number does not appear in Table 1, so it is not an affected part on this record. Table 1 lists only the 2A4802 hubs with S/Ns PKLBST5005, PKLBSS9840, PKLBSS0301 and PKLBSR2100.
- **Note:** The record gives no evidence that the 2A4802 hub was recorded with an event or dated reading, so no second-stage cycle check was needed.
- **Note:** The directive is in force on the question date, so authority_state is in_force.
- **Note:** Removing the listed hub does not end the AD: the installation prohibition in paragraph (h) continues to apply to all engines in the listed models.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row for 2A5001 / PKLBST5011, limit 5,500 cycles since new

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 engine is within the applicability of AD 2025-19-13, but neither installed hub's part number and serial number pair appears in Table 1 to paragraph (g), so no removal action is triggered on the current record. The installation prohibition in paragraph (h) continues to bind.
- **Note:** The recorded HPT 1st-stage hub serial number PKLBST5012 differs by one character from the listed serial PKLBST5011. Matching is on the exact P/N and S/N pair, so this hub is not treated as listed, but a reviewer should verify the recorded serial against the physical part or its records, because a transcription error would change the result.
- **Note:** The recorded HPT 2nd-stage hub serial SYN-HUB2-0002 is not in Table 1.
- **Note:** No cycle-based deadline is computed because no listed part is matched. The 4,200 cycles-since-new values are therefore not compared against any table limit.
- **Note:** The events list is empty, so no engine shop visit is recorded. This does not affect the outcome on the current record.
- **Note:** The NPRM (2025-10764) is superseded by the final rule for this analysis. The final rule governs and is cited here.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub rows and HPT 2nd-stage hub rows

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 is a listed model and AD 2025-19-13 (effective 2025-10-29) is in force on the question date, so the engine is within applicability. Whether a removal obligation is triggered cannot be settled: the installed HPT 1st-stage hub (P/N 2A5001) has an unknown serial number and cycle count, and the installed HPT 2nd-stage hub (S/N SYN-HUB2-0003) is not among the Table 1 serial numbers.
- **Stated timing:** If the HPT 1st-stage hub is a listed hub, removal is due at the next engine shop visit after 2025-10-29 before exceeding its listed cycle limit, or within 100 flight cycles of 2025-10-29, whichever occurs later. No shop visit is recorded and the engine flight-cycle count is not supplied, so the deadline cannot be computed.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub (P/N 2A5001) is unknown. Table 1 lists four serial numbers for this P/N with different cycle limits, and the P/N alone does not establish whether this hub is an affected part.
- **Missing fact:** The cycles since new for the installed HPT 1st-stage hub are unknown. Even if its serial number matches Table 1, the applicable removal cycle limit cannot be compared with its cycle count.
- **Missing fact:** The engine flight-cycle counter is not supplied in the engine record. It is needed to compute the 100-flight-cycle window from the effective date and any cycle-based deadline.
- **Missing fact:** The record lists no events, so it is unknown whether an engine shop visit (as defined in paragraph (i)(2)) has occurred or is scheduled since 2025-10-29. Shop-visit history determines when the removal obligation in paragraph (g) would be triggered.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) does not match any Table 1 P/N and S/N pair, so no removal limit is applied to it. This is not a finding that the part is eligible for installation or otherwise acceptable.
- **Note:** P/N 2A5001 matches the HPT 1st-stage hub P/N in Table 1, but a P/N match alone does not identify an affected part. The serial number must be confirmed.
- **Note:** The engine record contains no events, so the shop-visit trigger and the 100-flight-cycle window cannot be evaluated.
- **Note:** This is a screening aid. It does not determine compliance status, airworthiness, or return-to-service eligibility.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model is PW1133G-JM, which is not one of the IAE V2500 models this screen supports, so no applicability determination is made against Federal Register document 2025-18469. The directive is in force as of the question date (effective October 29, 2025), but this screen does not evaluate it for this engine.
- **Note:** The engine record reports engine_model PW1133G-JM and serial number SYN-PW1100-0004, and it has no installed_components and no events.
- **Note:** The screen returns outside_supported_scope with action_status none and makes no applicability determination, as the supported-scope rule requires.
- **Note:** This output is a screening aid only and is not a compliance determination or a statement about airworthiness or return to service.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (effective 2025-10-29) applies to this supported V2527E-A5 engine. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed in Table 1 with a 3,900-cycle removal limit (1,040 cycles since new now), and the 2025-11-12 shop visit qualifies as an engine shop visit, so removal is required by engine flight cycle 18100.
- **Stated timing:** Remove the listed HPT 2nd-stage hub at the engine shop visit inducted 2025-11-12, and in any case no later than 100 flight cycles after the 2025-10-29 effective date (engine flight cycle 18100), whichever occurs later.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The 1,040 cycles-since-new value is undated. It was used as the current count for the 2,860-cycle remaining calculation; confirm it reflects the 2025-11-12 snapshot.
- **Missing fact:** The record does not show whether the affected HPT 2nd-stage hub was removed and replaced during the 2025-11-12 shop visit. Whether the removal obligation has been met cannot be determined from the record.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The HPT 1st-stage hub with P/N 2A5001 and S/N SYN-HUB1-0005 does not match any Table 1 entry, so it is not a matched part on this record.
- **Note:** Engine flight cycles were 18000 on the effective date and 18040 on 2025-11-12, so the 100-cycle window ends at 18100.
- **Note:** The shop visit qualification is the operator's assertion, taken as recorded for this screen.
- **Note:** The hub's cycles-since-new rose from 1000 on 2025-10-29 to 1040 now, consistent with the 40 engine cycles flown in the same period.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row for 2A4802 / PKLBSS9840, limit 3,900 cycles

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a supported V2530-A5 with an installed HPT 1st-stage hub whose P/N 2A5001 and S/N PKLBSK9287 are listed in Table 1 of AD 2025-18469, which took effect 2025-10-29. The hub shows 90 cycles since new against a 100-cycle removal limit, so removal at the next engine shop visit is required before the limit is exceeded, and no shop visit is recorded yet.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the HPT 1st-stage hub exceeds 100 cycles since new (about engine flight cycle 25540), or within 100 flight cycles of the 2025-10-29 effective date (engine flight cycle 25600), whichever occurs later under the directive text. This screen uses the earlier, more conservative limit.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** No engine events are recorded after the effective date, so it is not known whether or when the next engine shop visit will occur. That timing controls when removal must be done.
- **Note:** This is a screening aid only and does not state that the engine or any part is compliant, airworthy, or approved for return to service.
- **Note:** The installed HPT 1st-stage hub shows 90 cycles since new in the current component record. Its earlier reading was 60 cycles on 2025-10-29, and engine cycles rose from 25500 to 25530 over the same period, so the 30-cycle increase is internally consistent. The top-level cycles_since_new field carries no date, so it is taken as current as of the 2025-11-20 snapshot.
- **Note:** The installed HPT 2nd-stage hub (S/N SYN-HUB2-0006) does not match any P/N and S/N pair in Table 1. The record does not show it as an affected part, so no removal action is triggered for it on this record.
- **Note:** The HPT 1st-stage hub was installed on 2025-09-30, before the effective date, so the installation prohibition in paragraph (h) is not triggered on this record.
- **Note:** No engine shop visit is recorded, so the removal obligation has not yet been triggered by a shop-visit event.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row, P/N 2A5001, S/N PKLBSK9287, removal cycle limit 100

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine is a supported model within the directive's applicability, and both installed hubs, HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 and HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005, are listed in Table 1 to paragraph (g). Removal and replacement is required at the next engine shop visit before the hub exceeds its listed removal cycle limit, which for the 1st-stage hub is about 30,500 engine flight cycles; no shop visit is recorded.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the HPT 1st-stage hub (PKLBSS9200) exceeds 4,800 cycles since new, about 500 engine flight cycles from the 2025-12-01 reading (about 30,500 engine flight cycles). The HPT 2nd-stage hub (PKLBST5005) limit of 4,000 cycles since new is about 1,700 cycles away. The 100-flight-cycle alternative from 2025-10-29 (30,100) is addressed in alternative_readings.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** No engine events are recorded. Whether an engine shop visit has occurred or is scheduled since 2025-10-29 determines when the paragraph (g) removal must be done, and the events list does not show one.
- **Missing fact:** The only dated cycles-since-new reading for the 1st-stage hub is 4,000 on 2025-10-29. The current value of 4,300 is not dated, and the 4,800-cycle limit computation depends on it being current as of 2025-12-01.
- **Missing fact:** The only dated cycles-since-new reading for the 2nd-stage hub is 2,000 on 2025-10-29. The current value of 2,300 is not dated, so the 1,700-cycle remaining figure depends on it being current.
- **Missing fact:** The paragraph (g) 'whichever occurs later' wording admits more than one reading of the deadline. The screen gives the cycle-limit reading as primary and the 100-cycle reading as an alternative; the FAA's intent should be confirmed if the operator disputes the deadline.
- **Note:** The 2025-10764 NPRM was superseded by the final rule 2025-18469, which is effective 2025-10-29 and in force on the 2025-12-01 question date. The screen relies only on the final rule.
- **Note:** Both listed hubs are subject to the paragraph (g) removal at the next shop visit. The 1st-stage hub reaches its limit first, at about 30,500 engine cycles. The 2nd-stage hub limit is about 32,000 engine cycles on the same count, based on 1,700 cycles remaining.
- **Note:** Cycle counts are taken from the record as given. The engine cycle reading (30,000 on 2025-10-29 and 30,300 on 2025-12-01) and the hub cycle readings both advance by 300, which is consistent.
- **Note:** This is a screening aid, not a compliance determination. It does not state that the engine or parts are compliant or noncompliant, or airworthy or approved for return to service.
- **Note:** The record shows no AMOC claims and no ad_records entries for this directive.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200, limit 4,800 cycles since new
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBST5005, limit 4,000 cycles since new

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 engine is within the applicability of AD 2025-19-13, which has been in force since 2025-10-29, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) is listed in Table 1 with a 6,200-cycle removal limit; the hub is recorded at 2,500 cycles since new. Removal and replacement is required at the next engine shop visit before the limit is reached, or within 100 flight cycles of the effective date if that is later, and no shop visit is recorded yet.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the HPT 1st-stage hub exceeds 6,200 cycles since new (about engine flight cycle 54,200), or within 100 engine flight cycles of the effective date (engine flight cycle 50,100), whichever occurs later.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub serial number is unknown, so the FAA's Table 1 listing for that hub cannot be checked and its applicability is undetermined. This does not change the 1st-stage hub finding.
- **Missing fact:** The HPT 2nd-stage hub cycles since new are unknown, so its removal cycle limit cannot be evaluated even if its serial number is later matched to Table 1.
- **Missing fact:** The only dated cycles-since-new reading for the HPT 1st-stage hub is 2,000 on 2025-10-29; the 2,500 value has no date. The remaining-cycle figure assumes 2,500 is current as of the 2026-03-10 snapshot and should be confirmed.
- **Missing fact:** The record contains no engine shop visit event and no scheduled shop visit date. Whether and when a qualifying shop visit occurs before the 6,200-cycle limit determines the deadline and cannot be settled from the record.
- **Note:** The screen uses the Federal Register final rule 2025-18469, effective 2025-10-29. The NPRM 2025-10764 is a proposal and was not relied on for requirements; its paragraph (g) text is the same as the final rule's.
- **Note:** The 100-flight-cycle floor is computed from the engine flight-cycle reading of 50,000 on 2025-10-29, the effective date, giving 50,100. The snapshot reading on 2026-03-10 is 50,500, so that floor has passed with no removal recorded.
- **Note:** The 54,200 figure assumes the hub accrues cycles one-for-one with engine flight cycles from 2025-10-29, which matches the recorded change from 2,000 to 2,500 cycles against 50,000 to 50,500 engine cycles.
- **Note:** The record lists no AD status claims or AMOC claims for this directive, so none were evaluated.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row, P/N 2A5001, S/N PKLBST7489, removal cycle limit 6,200

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2522-A5 is within the applicability of AD 2025-19-13 (FR document 2025-18469), which was effective 2025-10-29. The record has no installed HPT 1st-stage or 2nd-stage hub entries, no ad_records, no events, and no cycle counter, so whether the table 1 removal requirement is triggered cannot be determined.
- **Stated timing:** Remove listed hubs at the next engine shop visit after 2025-10-29 before exceeding the listed removal cycle limit, or within 100 flight cycles from 2025-10-29, whichever occurs later. The shop-visit and cycle facts needed to date this are not in the record.
- **Missing fact:** No HPT 1st-stage hub record is supplied. Whether an installed hub carries P/N 2A5001 with a listed S/N (table 1 to paragraph (g)) is needed to decide whether the removal requirement applies. An empty installed_components list is not evidence that no hub is installed.
- **Missing fact:** No HPT 2nd-stage hub record is supplied. Whether an installed hub carries P/N 2A4802 with a listed S/N (table 1 to paragraph (g)) is needed to decide whether the removal requirement applies.
- **Missing fact:** No engine flight-cycle counter is supplied. It is needed to compute the 100-flight-cycle window from the effective date, the removal cycle limits, and the cycles remaining for any listed hub.
- **Missing fact:** No operator AD status record for AD 2025-19-13 is supplied. It is a claim to check only, but its absence leaves the operator's recorded status unknown.
- **Missing fact:** No shop-visit history is supplied (events is empty). The next engine shop visit after 2025-10-29 is the trigger for removal, and whether any prior event qualifies as an engine shop visit under paragraph (i)(2) is unknown.
- **Note:** The engine record is synthetic and contains no installed components, events, ad_records, or cycle counter, so no hub is matched and no removal deadline or cycle count can be computed.
- **Note:** The 100-flight-cycle window runs from 2025-10-29. Without a cycle counter, the later of the two deadlines cannot be determined for this engine.
- **Note:** Because the question date is 2026-09-26, the 100-flight-cycle window may already have passed. If so, the removal timing could fall at the next shop visit, but that depends on missing cycle and event facts.
- **Note:** The NPRM 2025-10764 proposed the same requirements. The final rule 2025-18469 is the controlling text. The AD table lists P/N and S/N pairs; a hub matching only the P/N without a listed S/N would not match table 1.
- **Note:** This screen does not state that the engine is compliant or noncompliant, or approved for return to service.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model is V2500-A1, which is not among the V2522-A5, V2524-A5, V2525-D5, V2527-A5, V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2531-E5, or V2533-A5 models this screen supports, so no applicability determination is made. The directive is in force as of the question date, having become effective October 29, 2025.
- **Note:** The engine record lists model V2500-A1, which is outside the supported model list for this screen. No applicability, compliance, or action determination is given.
- **Note:** The record includes an HPT 1st-stage hub with P/N 2A5001 and S/N PKLBST5011, which corresponds to a row in table 1 to paragraph (g) of the directive. That match is noted for reviewer awareness only and was not evaluated because the engine is outside supported scope.
- **Note:** The record has no engine shop visit events, and the record does not include an AD status or AMOC entry for this directive.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has a 3rd stage HPC rotor blade set recorded at P/N 6A8353, which falls within the directive's applicability, and the directive is in force since its September 24, 2026 effective date. Full-set blade replacement is required only at the next engine shop visit after that date where the 3rd stage HPC rotor blade is exposed, and the record shows no such event.
- **Stated timing:** At the next engine shop visit (induction of the engine into the shop for maintenance) after September 24, 2026 where any 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline applies before that event.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** The events list is empty, so the record shows no engine shop visit after the September 24, 2026 effective date. Confirmation is needed that no shop visit has been inducted since then and that no 3rd stage HPC rotor blade exposure has occurred, because an empty list does not establish that no such event happened.
- **Missing fact:** The set is recorded as not tracked at set level, and only one set-level part number (6A8353) is given. Individual blade part numbers (6A8353 or 6A8688) and whether any blade is already a part eligible for installation (P/N 6C8368, 6C8403, a later approved P/N, or 6A8353-001/6A8688-001) are not recorded, which matters for the replacement scope at the future event.
- **Missing fact:** Whether a future engine shop visit will expose the 3rd stage HPC rotor blades (removal from the HPC stage 3 to 8 drum) is a future fact not in the engine record.
- **Note:** This is a screening aid and does not determine compliance or return-to-service status; the screen only identifies the applicable requirement and the event that triggers it.
- **Note:** The engine model V2527-A5 is within the supported scope list, and the installed blade P/N matches the directive's listed P/N 6A8353.
- **Note:** The 2025-20088 NPRM was superseded by the final rule 2026-16954 and was not relied on for the requirement; the correction 2026-18423 affects only the wording of paragraph (g).
- **Note:** The record's events list is empty; under the screening conventions this is not evidence that no shop visit has occurred, so the action is treated as triggered only on a future shop visit with blade exposure, and the record should be checked for any post-effective-date shop visit.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The record lists the installed 3rd stage HPC rotor blade set as P/N 6C8368, which is a part eligible for installation under paragraph (h)(1), not one of the applicable P/Ns 6A8353 or 6A8688 named in paragraph (c), so the supplied facts place this V2533-A5 engine outside the directive's applicability. No engine shop visit is recorded, so no required action is triggered on this record.
- **Missing fact:** The record gives one set-level P/N (6C8368) and states serial numbers are not tracked at set level. Applicability turns on whether any installed 3rd stage HPC rotor blade is P/N 6A8353 or 6A8688, so confirmation of the individual blade P/Ns (for example from the removal or build records) would be needed to rule out a mixed set.
- **Note:** The screen is based only on the supplied record and the directive text; it is not a compliance determination.
- **Note:** The record contains no ad_records, amoc_claims, or events, so no operator AD status or AMOC claim was evaluated.
- **Note:** If the individual blades are later shown to include P/N 6A8353 or 6A8688, the applicability conclusion would change; the paragraph (g) action would then be triggered only at the next engine shop visit where a 3rd stage HPC rotor blade is exposed, with no calendar or cycle deadline.
- **Note:** The question date is after the 2026-09-24 effective date, so the directive is in force for this screen.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The directive applies to this V2530-A5 engine because a 3rd stage HPC rotor blade set with P/N 6A8688 is recorded as installed. The only recorded engine shop visit was inducted 2026-09-14, before the 2026-09-24 effective date, so the paragraph (g) replacement trigger is not met by that visit, even though the 2026-09-30 blade exposure occurred during it.
- **Stated timing:** No deadline arises from this visit. Paragraph (g) attaches to the next engine shop visit inducted after September 24, 2026 in which a 3rd stage HPC rotor blade is exposed, and replacement is then required with parts eligible for installation.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The induction date of 2026-09-14 is the operator's assertion. It is the fact that places this visit before the 2026-09-24 effective date, so the operator should confirm it against shop records. If the induction actually occurred on or after 2026-09-24, paragraph (g) would be triggered by the 2026-09-30 exposure and the answer would change.
- **Missing fact:** Serial number is not tracked at set level. The directive matches on part number only, so this gap does not change applicability, but it limits traceability of the blade set.
- **Missing fact:** No engine flight-cycle counter is recorded. It is not needed for this screen because the required action is event-driven, but it would be needed to compute any cycle-based deadline if a future shop-visit trigger arises.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The operator record marks the 2026-09-14 induction as a qualifying engine shop visit for AD 2026-17-03. That flag is the operator's assertion. The screen relies on the induction date relative to the effective date, not on the flag.
- **Note:** The 2026-09-30 blade exposure is after the effective date, but it occurred within a visit inducted before the effective date. The preamble's stated intent is that such engines are not required to comply, so this is treated as not triggering paragraph (g).
- **Note:** An alternative reading would treat the post-effective-date exposure itself as the trigger and require immediate blade replacement. The preamble does not support that reading, and no cycle-based deadline can be computed from the record, so no alternative reading is listed.
- **Note:** Replacement with reworked or new blades is the required action when triggered. Replacement with reworked blades is described in the preamble as the cost-effective option, and new blades are an acceptable option.
- **Note:** The record has no field linking this induction to a return-to-service status, and nothing here indicates whether the engine is airworthy or in compliance.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a supported V2524-A5 with a 3rd stage HPC rotor blade set listed as P/N 6A8353, so it is within the AD's applicability. The 2026-10-01 shop visit occurred after the 2026-09-24 effective date and meets the engine shop visit definition, but the record states no 3rd-stage blade was removed from the stage 3-8 drum, so the replacement requirement was not triggered by that visit and will be triggered at a later shop visit that exposes the blades as defined.
- **Stated timing:** Not triggered by the 2026-10-01 shop visit on this record. Replacement of the full 3rd stage HPC rotor blade set is due at the next engine shop visit after 2026-09-24 in which a 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** No operator AD status record for AD 2026-17-03 is included in the engine record. This screen does not depend on it, but the operator's recorded status is an unverified claim and was not supplied.
- **Missing fact:** The 2026-10-02 event says the HPC rotor was exposed for inspection and that no 3rd-stage blade was removed from the stage 3-8 drum. The AD defines exposure by blade removal, so this operator assertion is what keeps the requirement untriggered. If blade removal from the drum occurred, the analysis would change.
- **Note:** Action status is set to action_required_on_event, not a current deadline. The requirement is triggered only by a future shop visit that exposes a 3rd stage HPC rotor blade as defined in (h)(2).
- **Note:** The 2026-10-01 shop visit is after the effective date and meets (h)(3), per the operator's assertion. The record shows no blade removal from the stage 3-8 drum, so (h)(2) is not met for that visit.
- **Note:** The uncorrected paragraph (g) in 2026-16954 says rotor is exposed. Under that wording the 2026-10-02 rotor exposure entry could be argued as a trigger. The later correction 2026-18423 restores blade is exposed, and this screen follows the corrected text. A reviewer should confirm the corrected text governs.
- **Note:** No latest_engine_flight_cycles or component_cycles_remaining is given because the trigger is an event, not a cycle count, and the record has no engine cycle counter.
- **Note:** Nothing here is a compliance or airworthiness determination. The screen relies on the operator's asserted event entries and the stated absence of blade removal.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The proposed AD's applicability text covers this V2527E-A5 engine because its 3rd stage HPC rotor blade set is recorded as P/N 6A8353. The document is an NPRM dated 2025-11-18 with no effective date, so it cannot require action on the question date of 2026-01-15.
- **Stated timing:** No deadline is set. If adopted as proposed, the full set of 3rd stage HPC rotor blades would be due for replacement at the next 3rd stage HPC rotor blade exposure (removal of any blade from the HPC stage 3 to 8 drum) after the final rule's effective date, which is not yet established.
- **Missing fact:** The blade set is recorded as 'not tracked at set level', so the individual blade serial numbers and whether all blades are P/N 6A8353 cannot be confirmed. This matters for the matched-part check and for any later replacement scope.
- **Missing fact:** No final rule or effective date for this AD appears in the supplied documents. The proposal cannot require action until a final rule is published and takes effect, and the proposed deadline depends on that effective date.
- **Missing fact:** The engine record has no 3rd stage HPC rotor blade exposure history (events list is empty). Whether a future exposure occurs, and so when the replacement would fall due, cannot be determined.
- **Note:** This is a screening aid, not a compliance determination. The document is a proposed rule, so it does not impose any present obligation on the operator. Comments were due January 2, 2026, which is before the question date. Check the Federal Register for a final rule and its effective date before treating any action as required.
- **Note:** The engine record has no ad_records or amoc_claims entries for this directive, so no operator AD status or AMOC claim was assessed.
- **Note:** The matched part is the blade set P/N only. The directive lists no serial number, so listed_serial_number is null.
- **Unresolved locator:** 2025-20088 (c) Applicability paragraph listing V2527E-A5 engines with 3rd stage HPC rotor blade P/N 6A8353 or 6A8688 installed
- **Unresolved locator:** 2025-20088 preamble DATES and Summary sections

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** Directive 2025-17-16 (FR doc 2025-17066) is in force with an effective date of October 10, 2025, and covers the V2527-A5 engine. The operator's record states that neither its approved maintenance program nor TLM paragraph B.1 yet incorporates table 1 to paragraph (g), so the required revision is shown as outstanding and is due by January 8, 2026.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e., on or before January 8, 2026, for both the TLM ALS paragraph B.1 revision under (g)(1) and, for air carrier operations, the approved maintenance or inspection program revision under (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** The engine record has no engine flight-cycle counter. The AD compliance time is calendar-based, so the January 8, 2026 due date does not depend on it, but no cycle-based figure can be stated.
- **Missing fact:** Operator-side confirmation of which TLM part number and revision applies to this engine (the V2500-A5 TLM, P/N 2A4408, under (g)(1)(i)). The record gives only the operator's statement that paragraph B.1 is not yet revised; the revision date and the operator's planned completion date are not recorded.
- **Note:** The question date (2025-11-15) is before the January 8, 2026 due date, so the required revision is not yet overdue on the record as provided.
- **Note:** The 2024 NPRM (2024-26092) was superseded by the final rule and was not used for the deadline. The final rule's paragraph (g) is the operative text.
- **Note:** The operator record states that neither the approved program nor TLM paragraph B.1 incorporates table 1. The record does not show the HPT hub part records (installed_components is empty). The ALS revision obligation depends on the engine model, not on the presence of hub records, so this does not change the action status.
- **Note:** The alternative reading of counting 90 days from the September 5, 2025 publication date (about December 4, 2025) is not supported by the AD text, which runs the compliance time from the effective date. It is not listed as an alternative reading.
- **Note:** This is a screening aid only and does not determine compliance, airworthiness, or return-to-service status.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is a listed engine model under AD 2025-17-16 (FR 2025-17066), which took effect October 10, 2025. Revising the Maintenance Scheduling paragraph B.1 of the ALS in the applicable TLM (paragraph (g)(1)) is due within 90 days of the effective date, by January 8, 2026; the record does not show whether it has been done, and the air carrier status needed for paragraph (g)(2) is unknown.
- **Stated timing:** Paragraph (g)(1) revision of the ALS Maintenance Scheduling paragraph B.1 in the applicable TLM is due within 90 days after the October 10, 2025 effective date, i.e., by January 8, 2026. Paragraph (g)(2), for air carrier operations, is on the same 90-day clock if the operator is an air carrier.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** No AD status record for AD 2025-17-16 is present, so it cannot be determined whether the paragraph (g)(1) TLM revision has already been made. This screen does not treat its absence as evidence either way.
- **Missing fact:** Whether the operator conducts air carrier operations is unknown. This decides whether the paragraph (g)(2) revision of the existing approved maintenance or inspection program applies.
- **Missing fact:** No installed component record exists for the HPT Stage 1 Hub (P/N 2A5001), so it cannot be confirmed whether that part is installed. The inspections in Table 1 apply at piece-part exposure for this part.
- **Missing fact:** No installed component record exists for the HPT Stage 2 Hub (P/N 2A4802), so it cannot be confirmed whether that part is installed. The inspections in Table 1 apply at piece-part exposure for this part.
- **Missing fact:** The engine record has no flight-cycle counter. The AD deadline is calendar-based, so cycles do not change the deadline, but they are needed for any cycle-based tracking of the piece-part inspections.
- **Missing fact:** The operator's current ICA/TLM and approved maintenance program revision status is not in the record. This is needed to confirm whether the required revisions are already reflected in the operator's documents.
- **Note:** This is a screening aid only. It does not state compliance or noncompliance, airworthiness, or return-to-service status.
- **Note:** The record has no ad_records or amoc_claims entries and no events, so no operator claim about AD status was evaluated.
- **Note:** The 2024 NPRM (2024-26092) was superseded by the final rule; the final rule's paragraph (g) (TLM paragraph B.1 and air carrier program revision) controls the requirements and deadline.
- **Note:** Table 1 inspections are tied to piece-part exposure in the TLM per the preamble; no engine shop visit data was supplied, so no exposure event is established.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** Final rule 2025-18469 (AD 2025-19-13) takes effect 2025-10-29, so on 2025-10-15 it cannot yet require action. The engine is a listed V2525-D5 with an installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) that matches Table 1 (6,000-cycle limit, 990 cycles since new, 5,010 remaining); the HPT 1st-stage hub S/N SYN-HUB1-0018 is not listed.
- **Stated timing:** Per paragraph (g), from the effective date 2025-10-29: at the next engine shop visit before exceeding 6,000 cycles since new, or within 100 flight cycles of the effective date, whichever occurs later. No shop visit is recorded, and the engine flight-cycle counter is not in the record.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine flight-cycle counter is not recorded. It is needed to compute the 100-flight-cycle date after 2025-10-29 and to fix the latest engine flight-cycle count for the required action.
- **Missing fact:** No engine shop visit is recorded, and the date of the next shop visit is unknown. The removal deadline depends on that event, so the timing cannot be fixed from the record.
- **Note:** This is a screening aid, not a compliance determination; no compliance status is stated.
- **Note:** The directive is not in force on 2025-10-15 (effective 2025-10-29), so no action is currently triggered by it. The applicability and installed-part match are shown for planning only.
- **Note:** The 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0018) is not listed in Table 1, so it does not match. Its S/N should be confirmed against the Table 1 entries.
- **Note:** The 5,010 remaining cycles is the hub's cycles-since-new against its 6,000-cycle limit, not an engine flight-cycle count.
- **Note:** The 'whichever occurs later' wording in paragraph (g) leaves the deadline unclear without the engine flight-cycle counter and the next shop visit date. Readings were not given numeric deadlines because the inputs needed to compute them are missing.
- **Note:** No ad_records or amoc_claims were supplied for this engine.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model V2531-E5 is within the directive's applicability, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is a listed part with a 4,800-cycle removal limit. The recorded cycles since new (4,990) are above that limit, so removal is required at the next engine shop visit or within 100 engine flight cycles of the effective date (engine cycle 60,100), whichever occurs later.
- **Stated timing:** Remove the listed HPT 1st-stage hub at the next engine shop visit after 29 October 2025, or within 100 engine flight cycles of 29 October 2025 (by engine flight cycle 60,100), whichever occurs later. The recorded cycles since new already exceed the 4,800-cycle listed removal limit, so the before-exceeding prong cannot be met as written. No engine shop visit is recorded.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** No engine events are recorded, so it is not known whether an engine shop visit has occurred or is scheduled. The next shop visit determines when the shop-visit prong of the deadline falls, and the final deadline is the later of that event and cycle 60,100.
- **Missing fact:** The current cycles-since-new value of 4,990 is undated. The only dated reading is 4,950 on 2025-10-29. The current value should be confirmed as of the question date because it drives the remaining-cycles figure.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0019) is not among the listed serial numbers in table 1 (listed 2A4802 serials are PKLBST5005, PKLBSS9840, PKLBSS0301, and PKLBSR2100), so it does not match on the record. Its record has no dated cycle reading.
- **Note:** The HPT 1st-stage hub was installed on 2019-03-12, before the effective date, so the existing installation is not by itself an installation-prohibition event under paragraph (h). Any future installation of this hub in any engine would fall under paragraph (h).
- **Note:** The engine cycle counter was 60,000 on 2025-10-29 (effective date) and 60,040 on 2025-11-05. The 100-cycle window is computed from the 60,000 reading, taking that reading to correspond to the effective date.
- **Note:** The NPRM (2025-10764) was superseded by the final rule and is not relied on. The final rule governs the screen.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row with P/N 2A5001 and S/N PKLBSS9200 (removal cycle limit 4,800)

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (Federal Register 2021-11960) is in force on 2022-03-01 and covers V2533-A5 engines with HPT 1st- and 2nd-stage disks whose serial numbers are listed in the NMSB appendices. The record matches both part numbers (2A5001, 2A4802) but does not show whether the serial numbers are listed, and the disks' cycles since the 2021-07-13 effective date are not recorded, so applicability and the deadline cannot be determined.
- **Stated timing:** If the serial numbers are listed in the NMSB appendices, the USI of each disk is due at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first. The record has no shop visit events and no disk cycle counts, so the date cannot be computed.
- **Missing fact:** Whether HPT 1st-stage disk P/N 2A5001, S/N SYN-DISK1-0020, is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1 (or Table 1 of NMSB V2500-E5-72-0015). Applicability under paragraph (c)(1) depends on this, and the NMSB text was not supplied.
- **Missing fact:** Whether HPT 2nd-stage disk P/N 2A4802, S/N SYN-DISK2-0020, is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713 Rev 1 (or Table 2 of NMSB V2500-E5-72-0015). Applicability under paragraph (c)(2) depends on this, and the NMSB text was not supplied.
- **Missing fact:** Flight cycles accumulated by the HPT 1st-stage disk since the 2021-07-13 effective date are needed to compute the 3,200-cycle limit in paragraph (g)(1). None are recorded.
- **Missing fact:** Flight cycles accumulated by the HPT 2nd-stage disk since the 2021-07-13 effective date are needed to compute the 3,200-cycle limit in paragraph (g)(2). None are recorded.
- **Missing fact:** Engine shop visit history since 2021-07-13. The events list is empty, which does not show that no engine shop visit has occurred. Whether a shop visit has occurred determines whether the 'next engine shop visit' trigger has already passed.
- **Missing fact:** No operator AD status record for AD 2021-11-15 is present. The operator's recorded status is not evidence either way and is not supplied.
- **Note:** Synthetic record (SYN- identifiers). Question date 2022-03-01 falls after publication of the superseding AD 2022-02-09 (Federal Register 2022-02574, published 2022-02-08) but before its effective date of 2022-03-15. AD 2021-11-15 therefore remains the operative directive on the question date.
- **Note:** The superseding AD's compliance figure (Figure 1 to paragraph (g)(1)) is not included in the supplied text. The superseding AD shortens compliance for disks previously operated on high-thrust engines, and the V2533-A5 is a high-thrust model, so this reading should be checked once effective.
- **Note:** The installed part numbers 2A5001 and 2A4802 match the part numbers named in the directive. Matching requires the serial numbers to be in the NMSB Appendix A tables, which were not supplied, so no part is listed in matched_parts.
- **Note:** No engine flight-cycle counter is in the record, so the 3,200-cycle limit cannot be computed.
- **Note:** This is a screening aid, not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (Federal Register 2022-02574) covers V2533-A5 engines with listed HPT 1st-stage and 2nd-stage disks but is not effective until March 15, 2022, so no action can be required on the March 1, 2022 question date. The record matches both disk part numbers, but the serial numbers cannot be checked against the Appendix A tables, so applicability and the due point remain open.
- **Stated timing:** Once the directive is in force on March 15, 2022 and if the disks are within its applicability: USI of the HPT 1st-stage disk under (g)(1) and of the HPT 2nd-stage disk under (g)(2) are due at the compliance time in Figure 1 to paragraph (g)(1), or within 10 flight cycles after the effective date, whichever occurs later. Figure 1 is an image not included in the supplied text.
- **Missing fact:** Serial number SYN-DISK1-0020 must be checked against Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Revision 1. Applicability under paragraph (c)(1) depends on this listing, and the NMSB was not supplied.
- **Missing fact:** Serial number SYN-DISK2-0020 must be checked against Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Revision 1. Applicability under paragraph (c)(2) depends on this listing, and the NMSB was not supplied.
- **Missing fact:** The compliance-time table in Figure 1 to paragraph (g)(1) is an image not included in the supplied text. It is needed to set the due point for both USIs.
- **Missing fact:** IAE NMSB V2500-ENG-72-0713 Revision 1, including its Appendix A tables and Accomplishment Instructions, was not supplied.
- **Missing fact:** The engine flight-cycle counter as of March 15, 2022 and since then is not in the record. It is needed to test the 10-flight-cycle limit and any cycle-based deadline.
- **Missing fact:** The engine shop-visit history is not recorded (events list is empty). An engine shop visit, which separates H-P flanges per paragraph (h)(1), would trigger the shop-visit limb of the deadline, so the date of the next shop visit is needed.
- **Note:** Question date 2022-03-01 is before the 2022-03-15 effective date, so the directive cannot require action on the question date. Re-screen on or after March 15, 2022 after the serial numbers and Figure 1 are checked.
- **Note:** This is a screening aid only. It does not state that any engine or part is compliant or noncompliant, and it does not show return-to-service status.
- **Note:** The record has no ad_records or amoc_claims entries, so no operator AD status or alternative method of compliance is supplied or evaluated.
- **Note:** The events list is empty. That does not show that no engine shop visit or disk removal occurred.
- **Note:** The engine model V2533-A5 is within the supported scope and is a high-thrust model under the preamble. The low-thrust paths in (g)(3) and (g)(4) do not apply to this engine.
- **Note:** Serial numbers SYN-DISK1-0020 and SYN-DISK2-0020 are synthetic. Listed serial numbers are null because the NMSB Appendix A tables were not supplied, so the matched_parts entries show a part-number match only.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The engine is a supported V2530-A5 with installed HPT 1st-stage disk P/N 2A5001 and HPT 2nd-stage disk P/N 2A4802, but applicability turns on whether the disk serial numbers appear in Appendix A of the referenced NMSBs, which was not supplied. The compliance time for this engine model is set by Figure 1 to paragraph (g)(1), which was also not supplied, and no engine or disk cycle counts are recorded, so no deadline can be computed.
- **Stated timing:** For a V2530-A5 with a listed disk, the USI under paragraph (g)(1) or (g)(2) is due within the compliance time in Figure 1 to paragraph (g)(1) or within 10 flight cycles after March 15, 2022, whichever occurs later; Figure 1 was not supplied, so the due date cannot be determined.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Revision 1 is not supplied; it is needed to confirm whether HPT 1st-stage disk serial SYN-DISK1-0021 (P/N 2A5001) is a listed affected disk, which decides whether paragraph (g)(1) applies.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Revision 1 is not supplied; it is needed to confirm whether HPT 2nd-stage disk serial SYN-DISK2-0021 (P/N 2A4802) is a listed affected disk, which decides whether paragraph (g)(2) applies.
- **Missing fact:** Figure 1 to paragraph (g)(1) (image not included in the text supplied) sets the compliance time for the V2530-A5 USI; without it the due date cannot be computed.
- **Missing fact:** The engine flight-cycle counter is not recorded, so the cycle-based deadline and remaining cycles cannot be computed.
- **Missing fact:** Cycles the HPT 1st-stage disk has accumulated since March 15, 2022 are not recorded; needed for the Figure 1 compliance time and the 10-cycle floor.
- **Missing fact:** Cycles the HPT 2nd-stage disk has accumulated since March 15, 2022 are not recorded; needed for the Figure 1 compliance time and the 10-cycle floor.
- **Missing fact:** The event history is empty, so it is unknown whether an engine shop visit has occurred since the AD effective date, which is a trigger in the superseded text and may affect the Figure 1 timing.
- **Note:** Screening aid only. This is not a compliance determination, and nothing here says the engine or its disks are compliant or noncompliant.
- **Note:** The record is synthetic (SYN- identifiers). The disk part numbers match the directive, but the serial numbers were not checked against Appendix A because the tables were not supplied.
- **Note:** Paragraph (g)(1) of the 2021 AD (3,200 FCs from its effective date) is superseded by 2022-02-09 and is not the operative timing.
- **Note:** The record contains no ad_records or amoc_claims for 2022-02-09 or 2021-11-15, so there is no operator AD status claim to check.
- **Note:** The engine flight-cycle counter and disk cycle history are absent; the snapshot is dated 2026-10-06, so the 10-cycle floor has long passed, and only Figure 1 timing could matter.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2021-11-51 (FR 2021-14268) is in force on the question date and applies to this V2533-A5 engine because the installed HPT 1st-stage disk (P/N 2A5001, S/N PKLBSH1829) is on the listed serial numbers. A one-time ultrasonic inspection is due within 10 flight cycles after the July 19, 2021 effective date, which is engine cycle 33010; the 33004-cycle snapshot leaves 6 cycles. The installed HPT 2nd-stage disk (S/N SYN-DISK2-0022) is not on the listed 2nd-stage serials.
- **Stated timing:** Within 10 flight cycles after the AD effective date of July 19, 2021 (engine cycle 33000 on that date), so by engine flight cycle 33010; 6 cycles remain at the 2021-07-20 snapshot of 33004.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** The record lists no events and contains no record of the paragraph (g)(1) ultrasonic inspection of the HPT 1st-stage disk, so whether it was performed by cycle 33010 cannot be confirmed from the record.
- **Missing fact:** The record contains no operator AD status entry for this AD, so the operator's recorded status cannot be checked against the required action.
- **Missing fact:** The USI result (pass or fail) is not in the record. If the disk does not pass, paragraph (g)(3) requires removal before further flight.
- **Missing fact:** The Appendix A Tables 1 and 2 listing of the disk in IAE NMSB V2500-ENG-72-0713 is not in the supplied text. It determines whether the disk is a part eligible for installation under paragraph (h) if it is replaced.
- **Note:** This is a screening aid. It identifies the directive's applicability and timing from the supplied record and does not determine compliance status.
- **Note:** The 33010 deadline is derived from the cycle reading of 33000 on the effective date. The 2021-07-20 reading of 33004 shows 4 cycles already flown after the effective date.
- **Note:** The engine record has no ad_records or amoc_claims entries for this AD, so no operator-asserted status or AMOC is considered.
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
- **Summary:** The engine model (V2533-A5) is in the directive's list and both installed disks match the directive's part numbers (2A5001 and 2A4802), but the directive applies only to disks whose serial numbers appear in the NMSB Appendix A tables, which were not supplied, and the 3,200-FC deadline runs from the July 13, 2021 effective date, for which no engine cycle reading is recorded. The applicability and deadline therefore cannot be determined from this record.
- **Stated timing:** If the disk serial numbers are listed in the NMSB Appendix A tables, each affected disk must be inspected (USI) at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 FCs since July 13, 2021, whichever occurs first; an inspection that does not pass requires removal before further flight.
- **Missing fact:** Whether HPT 1st-stage disk P/N 2A5001 S/N PKLBSH1829 is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1 (applicable to the V2533-A5 under paragraph (g)(1)); the NMSB table is not part of the engine record and was not supplied.
- **Missing fact:** Whether HPT 2nd-stage disk P/N 2A4802 S/N SYN-DISK2-0022 is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713 Rev 1 (applicable to the V2533-A5 under paragraph (g)(2)); the NMSB table is not part of the engine record and was not supplied.
- **Missing fact:** Engine flight-cycle count on the July 13, 2021 effective date is not recorded, so the 3,200-FC limit measured from the effective date cannot be converted into an engine cycle deadline.
- **Missing fact:** Disk flight cycles accumulated since July 13, 2021 are not recorded for the HPT 1st-stage disk; the 3,200-FC limit applies to disk cycles since the effective date.
- **Missing fact:** Disk flight cycles accumulated since July 13, 2021 are not recorded for the HPT 2nd-stage disk; the 3,200-FC limit applies to disk cycles since the effective date.
- **Note:** Engine snapshot shows 33,004 engine flight cycles on 2021-07-20, but the 3,200-FC limit is measured from the July 13, 2021 effective date for each disk, so an engine cycle count alone does not give a deadline.
- **Note:** The events list is empty, so no engine shop visit is recorded; an engine shop visit after July 13, 2021 would trigger the USI for the V2533-A5 disks if the serial numbers are listed.
- **Note:** The directive lists serial numbers in NMSB Appendix A tables that were not supplied; matched_parts reflects part-number matches only.
- **Note:** Synthetic record (SYN- identifiers). This is a screening aid and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527M-A5 engine is within the directive's applicability, and its installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) is listed in table 1 with a 6,000-cycle removal limit. At 3,500 cycles since new the hub has about 2,500 cycles remaining, so removal is required at the next engine shop visit and before the hub exceeds 6,000 cycles since new.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 6,000 cycles since new, which at the current 1:1 accumulation is about engine flight cycle 25,000. The alternative 100-flight-cycle window from the 2025-10-29 effective date (about engine flight cycle 20,100) has already passed at the current 22,500 cycles; see alternative_readings.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The only dated cycles-since-new reading for the listed hub is 1,000 at 2025-10-29. The current value of 3,500 is undated. It is consistent with the 2,500 engine cycles accrued since then, but a dated reading at the question date is needed to confirm the remaining cycles before the 6,000-cycle limit.
- **Missing fact:** The events list contains no engine shop visit since the 2025-10-29 effective date. Whether any engine shop visit (as defined in paragraph (i)(2)) occurred and whether the hub was removed at it must be confirmed. A missing record is not evidence that no shop visit occurred. If a qualifying shop visit occurred while this hub was installed, the removal was due at that visit.
- **Note:** This is a screening aid, not a compliance determination. Nothing here states that the engine or any part is compliant or noncompliant, airworthy, or approved for return to service.
- **Note:** The projection of 25,000 engine cycles assumes the hub stays installed on this engine and accrues cycles at the same rate as the engine, which the 2025-10-29 to 2026-10-06 readings support (2,500 hub cycles over 2,500 engine cycles).
- **Note:** The 2025-12-01 maintenance program revision cites AD 2025-17-16, not AD 2025-18469, and does not record removal of the listed hub. It is not evidence of compliance with this directive.
- **Note:** No ad_records or amoc_claims were supplied, so no operator AD status or alternative method of compliance was checked.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0023 is not among the table 1 serials for P/N 2A5001 and is not matched. The 3rd stage HPC rotor blade set is not a component this directive lists.
- **Note:** The NPRM 2025-10764 was superseded by final rule 2025-18469 and is not relied upon for requirements.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** Directive 2026-16954, as corrected by 2026-18423, is in force from 2026-09-24 and applies to this V2527M-A5 engine because its installed 3rd stage HPC rotor blade set is P/N 6A8688. Full-set replacement with parts eligible for installation is required at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed; the record shows no such shop visit, so no deadline has been triggered yet.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no fixed calendar or cycle deadline.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** No engine shop visit (induction of the engine into the shop for maintenance) after 2026-09-24 is recorded in the events list. Whether one has occurred, or is planned, determines whether the blade replacement is now due; the only recorded event is a 2025-12-01 maintenance program revision.
- **Missing fact:** Whether any 3rd stage HPC rotor blade has been removed from the HPC stage 3 to 8 drum (blade exposure) is not recorded. Exposure at a shop visit is the trigger for the replacement requirement.
- **Missing fact:** The blade set serial number is recorded as not tracked at set level. This does not affect applicability, which rests on the P/N, but it limits traceability of which blades were replaced or reworked.
- **Missing fact:** No operator AD status record for AD 2026-17-03 (Amendment 39-23446) is supplied, so the operator's own recorded status cannot be checked against this screen.
- **Note:** This is a screening aid, not a compliance determination; nothing here states that the engine or any part is compliant, noncompliant, or approved for return to service.
- **Note:** The engine model V2527M-A5 is within the supported scope.
- **Note:** The 2025-12-01 maintenance program revision cites AD 2025-17-16 table 1, which is a different directive. It was not treated as evidence of action under 2026-16954.
- **Note:** No ad_records or amoc_claims are supplied for this AD, so no operator-asserted status or alternative method of compliance was checked.
- **Note:** The engine cycle counter (22500 at 2026-10-06) does not set a deadline because the required action is event-driven rather than cycle-driven.
- **Note:** The HPT 1st-stage and 2nd-stage hub entries are not parts listed in this directive and were not matched.
- **Note:** The original 2026-16954 paragraph (g) contained the typo 'rotor is exposed'; the corrected text in 2026-18423 was used. The deadline is the same under either wording.
- **Note:** The 2025-20088 NPRM was superseded by the final rule and was not relied on for the operative requirement.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 applies to the V2527M-A5 engine and is in force (effective 2025-10-10). The record shows a maintenance program and TLM ALS revision dated 2025-12-01, inside the 90-day window that ended 2026-01-08, and no piece-part exposure event is recorded, so no action is triggered now; this screen does not determine compliance.
- **Stated timing:** The one-time TLM ALS revision (paragraph (g)(1)) and the air carrier maintenance program revision (paragraph (g)(2)) were due within 90 days after 2025-10-10, i.e. by 2026-01-08. The table 1 hub inspections are required at piece-part exposure under the revised TLM paragraph B.1.
- **Missing fact:** Confirmation that Revision 48 revises paragraph B.1 of the Maintenance Scheduling section of the ALS in the TLM applicable to this V2527M-A5 engine (P/N 2A4408, V2500-A5 TLM) and the air carrier maintenance program; the record gives only an operator statement.
- **Missing fact:** No operator AD status record for AD 2025-17-16 is supplied, so the operator's recorded status cannot be checked against the directive.
- **Missing fact:** Whether any piece-part exposure or shop visit has occurred (or is planned) that would expose the HPT 1st-stage hub or HPT 2nd-stage hub, which would trigger the table 1 inspections. No such event is recorded.
- **Missing fact:** The HPT 1st-stage hub cycles_since_new (3500) has no dated reading, so its current age cannot be confirmed against the engine record date.
- **Note:** This is a screening aid. It does not state that the engine or any part is compliant, noncompliant, or airworthy.
- **Note:** The 90-day window from 2025-10-10 ends 2026-01-08; the record's 2025-12-01 revision date falls inside it, but the revision itself is an operator statement, not verified evidence.
- **Note:** The directive sets no cycle limit. Any cycle-based replacement limit for the hubs comes from the operator's approved maintenance program and is not in the directive text or the record, so no cycle remaining is computed.
- **Note:** The record describes the revised TLM as V2500-A5. Confirm it is the TLM applicable to this V2527M-A5 engine.
- **Note:** The installed 3rd stage HPC rotor blade set (P/N 6A8688) is not a part listed in the directive and is not matched.
- **Note:** The engine cycle readings (20000 on 2025-10-29; 22500 on 2026-10-06) do not change the calendar-based deadline.
- **Note:** The directive is a stand-alone AD and does not supersede AD 2004-12-08; the FAA rejected a supersedure request in the preamble.
- **Unresolved locator:** 2025-17066 preamble Effective date stated in DATES and paragraph (a)

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** Engine model V2528-D5 is within the applicability of in-force AD 2025-19-13 (Federal Register 2025-18469, effective 2025-10-29). Neither installed hub matches a P/N and S/N pair listed in Table 1 to paragraph (g), so no removal action is triggered on this record, but the paragraph (h) installation prohibition still binds.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** Table 1 lists serial PKLBST5011 only under P/N 2A5001 (HPT 1st-stage hub). The installed HPT 2nd-stage hub carries P/N 2A4802 with that same serial. Because the AD requires both P/N and S/N to match, this is not a listed pair. Verify the recorded P/N of the 2nd-stage hub, since a recording error would change the outcome.
- **Note:** The events list is empty, so no engine shop visit is recorded. If a shop visit occurs, or a hub is installed or changed, rescreen the engine against table 1 and paragraph (g).
- **Note:** No ad_records or amoc_claims were supplied, so the screen does not evaluate any operator-asserted AD status or AMOC.
- **Note:** The NPRM (2025-10764) was adopted without substantive change, so the final rule 2025-18469 governs the question date.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub rows and HPT 2nd-stage hub rows

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model recorded is CFM56-5B4/3, which is not among the IAE V2500 models this screen supports, so no applicability determination is made against directive 2025-17066. The directive is in force as of the question date (effective October 10, 2025).
- **Note:** The engine record shows model CFM56-5B4/3, serial SYN-CFM56-0025, which is outside the screen's supported V2500 model list, so this screen makes no applicability or compliance determination for it.
- **Note:** The record is marked synthetic (SYN- identifiers); this result does not depend on the installed components, events, or operator fields, which are empty or non-engine-specific.
- **Note:** Confirm the engine model against the engine record before relying on this result; if the model was recorded in error, rerun the screen with the correct model.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 is a listed model and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) is in Table 1 of the directive effective 2025-10-29, so the directive applies. Removal is required at the next engine shop visit before the hub exceeds its 6,200-cycle limit (about 2,600 cycles remain), or within 100 flight cycles of the effective date, whichever is later; no post-effective-date shop visit is recorded.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 6,200 cycles since new (3,600 now), or within 100 flight cycles of the effective date (engine cycle 20,100), whichever occurs later. Under the plain reading the later date is the shop-visit date before the 6,200-cycle limit.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** The record does not show whether any engine shop visit (as defined in paragraph (i)(2)) has occurred since 2025-10-29. No event after the effective date is listed, and no qualifies_as_engine_shop_visit determination is given. This fact controls whether removal is already due.
- **Missing fact:** The projected latest engine cycle assumes the hub accrues cycles at the same rate as the engine. This matches the observed 600 hub cycles over 600 engine cycles, but it is an estimate, not a recorded fact.
- **Missing fact:** No operator AD status record for this directive is provided. It does not change the screen result but should be reconciled with the removal requirement.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The 2024 blend repair and 2024 ultrasonic inspection of hub PKLBST7489 predate the effective date. The directive does not address them, and they do not change the removal requirement.
- **Note:** The installed HPT 2nd-stage hub (S/N SYN-HUB2-0026) is not listed in Table 1 and is not matched.
- **Note:** The installation prohibition in (h) applies to any future installation of hub PKLBST7489 in any engine. This installation occurred before the effective date.
- **Note:** Document 2025-10764 is the NPRM and was not relied on; the final rule 2025-18469 governs.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row 4

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
- **Summary:** The V2527-A5 engine is within the applicability of AD 2025-19-13, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in Table 1 with a 4,800 cycles-since-new removal limit. At 4,750 CSN the hub has 50 cycles remaining, so removal is required at the next engine shop visit before that limit, and no later than engine flight cycle 15300.
- **Stated timing:** Remove the listed HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 4,800 cycles since new, or within 100 flight cycles of the 2025-10-29 effective date, whichever is later. The later of these is the shop-visit limit, which at 1:1 accrual is engine flight cycle 15300. The engine was at 15250 on 2026-01-20.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The events list is empty. Whether any engine shop visit (separation of major mating engine flanges, H-P) has occurred since 2025-10-29 is not recorded. This determines whether the next-shop-visit trigger has already occurred and whether removal can be scheduled at that visit.
- **Missing fact:** The operator's planning record claims an AMOC that extends the hub removal limit to 5,300 CSN. The approval reference is unknown and no FAA approval letter is on file. Under paragraph (j) an AMOC must be approved by the FAA before use, so the claim cannot be relied on, and the 4,800 CSN limit in Table 1 applies until an approval is shown.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The 15300 deadline assumes the hub accrues cycles 1:1 with engine flight cycles. The record supports this: engine cycles rose 250 (15000 to 15250) while hub CSN rose 250 (4500 to 4750) between 2025-10-29 and 2026-01-20.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0027) does not match any Table 1 entry, so no removal obligation was identified for it on this record. The Table 1 entries are for S/N PKLBST5005, PKLBSS9840, PKLBSS0301, and PKLBSR2100.
- **Note:** The planning-record AMOC note (5,300 CSN) has no FAA approval on file and was not used to set any deadline.
- **Note:** The directive is in force, effective 2025-10-29, and the question date is 2026-01-20. The NPRM 2025-10764 was superseded by the final rule and was not relied on.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200, removal limit 4,800 cycles since new

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2524-A5 engine is within the directive's applicability, and its installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) matches a Table 1 entry with a 4,000-cycle removal limit. At 1,400 cycles since new, the hub must be removed at the next engine shop visit and before it exceeds 4,000 cycles; the operator's N/A record conflicts with the installed-part record and needs review.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 4,000 cycles since new (about 2,600 more cycles). Under the directive's 'whichever occurs later' wording, the 100-flight-cycle window from the effective date (engine cycle 8,100) has already passed at 8,400 cycles, so the shop-visit trigger governs.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** No events are recorded. Whether any engine shop visit occurred after 2025-10-29, and whether the operator's qualifies_as_engine_shop_visit determination applies, is unknown. A shop visit would have triggered removal of this hub at that time, and the record does not show whether the hub was removed.
- **Missing fact:** The current cycles-since-new value of 1,400 is undated. The dated reading is 1,000 at 2025-10-29. The remaining-cycle figure assumes 1,400 is current as of the snapshot and that the hub accumulates cycles one-for-one with engine flight cycles, which the two readings support but do not confirm.
- **Note:** The ad_records entry marks AD 2025-19-13 as not_applicable with the note 'no affected hubs installed'. The installed HPT 2nd-stage hub matches Table 1 by P/N 2A4802 and S/N PKLBST5005, so this operator claim conflicts with the record and should be checked.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0028) does not match any Table 1 entry, so it is not matched on this record.
- **Note:** The hub was installed on 2025-06-03, before the effective date. The installation prohibition in paragraph (h) applies to future installations, while the removal obligation in paragraph (g) applies to the installed hub.
- **Note:** The cycle projection assumes the hub keeps accumulating cycles at the one-for-one rate seen between 2025-10-29 and 2026-02-10. The shop-visit timing itself cannot be computed from the record.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), row: HPT 2nd-stage hub, 2A4802, PKLBST5005, limit 4,000 cycles since new

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a listed V2525-D5 and the installed HPT 1st-stage hub with S/N PKLBSK9287 appears in Table 1 with a 100-cycle removal limit, while the record shows 2400 cycles since new. Removal is required at the next engine shop visit or within 100 flight cycles of the 29 October 2025 effective date, whichever occurs later, and the installed P/N 2A5001-01 must be confirmed against the listed P/N 2A5001. This is a screening aid, not a compliance determination.
- **Stated timing:** Remove the affected HPT 1st-stage hub from service and replace it with a part eligible for installation at the next engine shop visit after 29 October 2025 or within 100 flight cycles of 29 October 2025, whichever occurs later. The listed 100-cycle removal limit is already exceeded on the record (2400 cycles since new), so the 'before exceeding' limit cannot be met and the later-of rule governs.
- **Missing fact:** The engine flight-cycle counter as of the 29 October 2025 effective date is not in the record. It is needed to compute the 100-flight-cycle window and the latest engine flight-cycle count for removal.
- **Missing fact:** The installed P/N is recorded as 2A5001-01, while Table 1 lists P/N 2A5001. The dash suffix must be confirmed as the same listed part before the hub is treated as matched to the listed entry.
- **Missing fact:** No engine shop visit event is recorded. Whether and when a future shop visit occurs determines the shop-visit leg of the later-of deadline.
- **Note:** The record is synthetic (SYN- identifiers) and contains no engine flight-cycle counter, so latest_engine_flight_cycles cannot be computed.
- **Note:** The installed HPT 2nd-stage hub has P/N 2A4802, which is a listed P/N, but its S/N SYN-HUB2-0029 is not in Table 1, so the record does not match it to the table.
- **Note:** The 2025-18469 effective date of 29 October 2025 is before the question date of 1 February 2026, so the directive is in force.
- **Note:** The record's cycles-since-new value of 2400 for the HPT 1st-stage hub is taken from the record as stated and was not verified.
- **Note:** If the P/N suffix -01 is confirmed as the same listed part, the hub is treated as matched and removal is required on the timing above; if it is not the listed part, the match fails and the review changes.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row, P/N 2A5001, S/N PKLBSK9287, removal cycle limit 100

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
