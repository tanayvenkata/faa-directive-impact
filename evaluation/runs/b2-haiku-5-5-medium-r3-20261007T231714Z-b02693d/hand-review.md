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
- **Summary:** The engine is a supported V2527-A5 and carries an HPT 1st-stage hub whose P/N and S/N (2A5001, PKLBST5011) are listed in Table 1 to paragraph (g) with a 5,500-cycle removal limit; the directive is in force and requires removal at the next engine shop visit before that limit is exceeded, or within 100 flight cycles of the effective date, whichever is later. The HPT 2nd-stage hub (2A4802, SYN-HUB2-0001) is not a listed serial number, so it does not trigger the removal requirement on these facts.
- **Stated timing:** Remove the listed HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 5,500 cycles since new; on this record that limit is reached at about engine flight cycle 45,050. The 100-flight-cycle alternative clause (engine flight cycle 41,300) is earlier and has already passed, so the reading that gives the later deadline controls, subject to review.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** Only a 2025-10-29 cycles-since-new reading (1,650) is recorded for the listed hub. The current value is inferred as 3,100 from the top-level field and engine cycle growth of 1,450, but a dated reading at the question date is needed to confirm the remaining cycles and the projected 5,500-cycle point.
- **Missing fact:** No engine events are recorded. Whether an engine shop visit (as defined in paragraph (i)(2)) has occurred or is scheduled since the effective date is unknown; a shop visit would start the removal window earlier and must be checked.
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** Effective date 2025-10-29 comes from the Federal Register record; the directive is in force on the question date 2026-09-26.
- **Note:** Engine cycle readings: 41,200 at 2025-10-29 and 42,650 at 2026-09-26 (1,450 cycles). The hub's cycles-since-new of 1,650 on 2025-10-29 plus 1,450 gives 3,100, matching the top-level field.
- **Note:** The projected 45,050 assumes the hub accumulates one cycle per engine flight cycle, as the record implies.
- **Note:** The HPT 2nd-stage hub (2A4802, SYN-HUB2-0001) is not in Table 1 and is not matched; the installation prohibition in (h) still applies to listed hubs in any engine.
- **Note:** No ad_records or amoc_claims were supplied for this directive.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBST5011, limit 5,500 cycles since new

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 engine is within the directive's applicability, and the in-force effective date (2025-10-29) precedes the question date. Neither installed hub matches a P/N and S/N in Table 1: the HPT 1st-stage hub is 2A5001 S/N PKLBST5012, while Table 1 lists PKLBST5011, and the HPT 2nd-stage hub is 2A4802 S/N SYN-HUB2-0002, which is not listed, so no removal is triggered on these facts.
- **Missing fact:** The recorded HPT 1st-stage hub serial number PKLBST5012 differs by one character from the listed serial PKLBST5011 for P/N 2A5001. The recorded value should be verified against the hub's nameplate or shop records to rule out a transcription error, because a match would trigger the removal requirement with a 5,500-cycle limit.
- **Note:** The engine record has an empty events list, so no engine shop visit is recorded. This does not bear on the outcome because no listed part is recorded as installed.
- **Note:** The result depends on the recorded serial numbers. If the 1st-stage hub serial PKLBST5012 is confirmed as recorded, the installed hub is not listed. If it is actually PKLBST5011, paragraph (g) would require removal at the next engine shop visit or within 100 flight cycles of 2025-10-29, whichever is later, before the 5,500-cycle limit is exceeded, and the installed hub is at 4,200 cycles since new.
- **Note:** This screen is not a compliance determination.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 is a listed model and AD 2025-19-13 (effective 2025-10-29) is in force, so the engine is within applicability. Whether the installed HPT 1st-stage hub (P/N 2A5001) is an affected part cannot be decided because its serial number is unknown, and the installed HPT 2nd-stage hub (S/N SYN-HUB2-0003) is not listed in table 1.
- **Stated timing:** Removal is required at the next engine shop visit after 2025-10-29 before exceeding the listed removal cycle limit, or within 100 flight cycles from 2025-10-29, whichever occurs later, if the hub is a listed part. The installation prohibition in (h) applies from 2025-10-29.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub is unknown. Table 1 lists 1st-stage hub serial numbers by P/N 2A5001, so this fact is needed to decide whether the hub is a listed part.
- **Missing fact:** Cycles since new for the HPT 1st-stage hub are unknown. Table 1 gives a removal cycle limit for each listed serial number, so the cycle count is needed to compute any deadline or remaining cycles if the hub is listed.
- **Missing fact:** The engine flight-cycle counter is not in the record. The 100-flight-cycle window runs from the effective date, so the current engine cycle count and the cycle count at 2025-10-29 are needed to compute a deadline.
- **Missing fact:** The engine event history is empty. Whether any engine shop visit has occurred since 2025-10-29 is unknown, and the shop visit determines when removal is due for a listed hub.
- **Note:** The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) does not match any S/N in table 1 for that P/N, so it is not an affected part on this record. Its 5100 cycles since new are not relevant to the table limits.
- **Note:** An unknown serial number is not evidence that the 1st-stage hub is unaffected. The 1st-stage hub must be resolved before any conclusion about its status.
- **Note:** The record shows no engine shop visit events. Shop visit status is unknown and is needed for the timing analysis.
- **Note:** This screen is not a compliance determination. The 100-flight-cycle window runs from 2025-10-29, and the required engine cycle counter is not in the record, so no deadline is computed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub rows (P/N 2A5001) and HPT 2nd-stage hub rows (P/N 2A4802)

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the IAE V2500 models supported by this screen, so no applicability determination is made under Federal Register document 2025-18469. The directive is in force as of the question date, but no determination is made for this engine.
- **Note:** The engine record lists model PW1133G-JM, serial number SYN-PW1100-0004, with no installed components and no events. No applicability determination was made because the model is outside the supported scope.
- **Note:** The directive's effective date is October 29, 2025, which precedes the question date of 2026-09-26, so it is in force.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527E-A5 is a supported model and AD 2025-19-13 has been in force since 2025-10-29. The record lists HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840, which is in Table 1 with a 3,900-cycle removal limit, so removal is required at the next engine shop visit after the effective date (the 2025-11-12 induction at 18040 cycles, which the operator asserts qualifies) and no later than 18100 cycles.
- **Stated timing:** Remove the listed HPT 2nd-stage hub at the next engine shop visit after 2025-10-29 (the 2025-11-12 induction, 18040 cycles) before exceeding its 3,900-cycle limit, or within 100 flight cycles of the effective date, whichever is later; the later clock ends at 18100 engine flight cycles.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The record does not show whether the HPT 2nd-stage hub PKLBSS9840 was removed from service during the 2025-11-12 shop visit. Removal status is needed to determine whether the required action has been done.
- **Missing fact:** The only dated cycles-since-new reading is 1000 on 2025-10-29; the current value of 1040 is undated. The remaining-cycle figure depends on which reading is current.
- **Missing fact:** The shop-visit qualification is the operator's assertion ('yes') and has not been independently confirmed. The detail (separation of major mating flanges) appears to meet the AD definition, but the operator's assertion should be verified.
- **Note:** Authority state is in force because the final rule is effective 2025-10-29, before the question date of 2025-11-12. The 2025-10-764 NPRM is not relied on because the final rule governs.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0005 with P/N 2A5001 does not match any Table 1 serial (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489). The record does not show a match for that hub.
- **Note:** The 2nd-stage hub's 1040 cycles since new is above the 1000 reading dated 2025-10-29. Using 1040 gives 2860 cycles remaining; using 1000 would give 2900.
- **Note:** The engine accumulated 18040 cycles against an effective-date reading of 18000, so 40 cycles had elapsed since the effective date. The 100-cycle window runs through 18100.
- **Note:** This is a screening aid. It does not determine compliance, airworthiness, or return-to-service status.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row for 2A4802 / PKLBSS9840, limit 3,900 cycles since new

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (effective 2025-10-29) applies to V2530-A5 engines. The installed HPT 1st-stage hub P/N 2A5001, S/N PKLBSK9287 is listed in table 1 with a 100-cycle removal limit and shows 90 cycles since new, so it must be removed at the next engine shop visit before exceeding 100 cycles, or within 100 flight cycles of the effective date, whichever occurs later.
- **Stated timing:** Remove the listed HPT 1st-stage hub at the next engine shop visit after 2025-10-29 before it exceeds 100 cycles since new, or within 100 flight cycles from 2025-10-29 (engine cycle 25600), whichever occurs later. No shop visit is recorded yet.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** No engine events are recorded, so it is unknown whether any engine shop visit has occurred since the effective date. The next qualifying shop visit determines when removal is due under the shop-visit prong.
- **Missing fact:** The top-level cycles_since_new value of 90 is undated. It is taken as the value at the 2025-11-20 snapshot; the dated reading of 60 on 2025-10-29 is consistent with it. Confirming the current value matters because the 10-cycle margin depends on it.
- **Note:** The NPRM 2025-10764 is superseded for this screen by the final rule 2025-18469, which is in force. The NPRM was not relied on.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0006 does not match any table 1 entry, so it is not a matched part on this record. Its installed record is not a basis for action under this AD.
- **Note:** The record shows the 1st-stage hub installed 2025-09-30, before the effective date, so the installation prohibition in paragraph (h) is not triggered by the current record.
- **Note:** Engine cycles rose 30 from 2025-10-29 to 2025-11-20, and the hub's cycles rose 30 over the same period, so the readings are consistent.
- **Note:** This is a screening aid and does not determine compliance or return-to-service status.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row, P/N 2A5001, S/N PKLBSK9287, limit 100 cycles

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine has an HPT 1st-stage hub (2A5001, S/N PKLBSS9200) and an HPT 2nd-stage hub (2A4802, S/N PKLBST5005), both listed in Table 1 of AD 2025-19-13. The 1st-stage hub has 4,300 cycles since new against a 4,800-cycle limit, so it must be removed at the next engine shop visit and before it exceeds that limit, which equals engine cycle 30800 on the current cycle rate; no shop visit is recorded.
- **Stated timing:** Remove and replace the listed hub(s) at the next engine shop visit after 2025-10-29, and before the hub exceeds its removal cycle limit. The 1st-stage hub (limit 4,800 cycles since new) reaches that limit at engine flight cycle 30800, assuming it accumulates cycles one-for-one with the engine. The 100-flight-cycle alternative (engine cycle 30100) has already passed at 30300 and is superseded by the later shop-visit clause.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** No engine shop visit event is recorded. Whether and when the next shop visit occurs determines when the hub must be removed, so the operator must confirm the shop visit schedule against the 30800-cycle limit.
- **Missing fact:** The 1st-stage hub cycles since new are given as 4,300 on the current snapshot and 4,000 on 2025-10-29. A dated reading on 2025-12-01 would confirm the accumulation rate used for the limit calculation.
- **Missing fact:** The 2nd-stage hub has a dated reading only for 2025-10-29 (2,000 cycles). Its limit of 4,000 cycles since new is 1,700 cycles away and is not the controlling limit, but a current reading would confirm this.
- **Missing fact:** The AD's Table 1 lists hub serial numbers, and the record is compared against the Federal Register table only. Whether the installed hub's record and any maintenance history match the listed serial numbers is outside the engine record; the screen relies on the record as given.
- **Note:** Synthetic record. Engine cycles 30,000 on 2025-10-29 and 30,300 on 2025-12-01; component cycles were assumed to accumulate one-for-one with engine flight cycles, which the readings support (hub 1: 4,000 to 4,300 over 300 engine cycles).
- **Note:** The 2nd-stage hub limit (4,000) is reached at engine cycle 32,000, which is later than the 1st-stage hub limit. The 1st-stage hub is therefore the controlling component.
- **Note:** This is a screening aid only and does not state compliance or noncompliance.
- **Note:** The 2025-10764 proposed rule was not relied on, because the in-force AD text is the final rule 2025-18469.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), rows for 2A5001 PKLBSS9200 (limit 4,800) and 2A4802 PKLBST5005 (limit 4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 is a listed model, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) matches Table 1 with a 6,200-cycle removal limit. Under paragraph (g), the hub must be removed at the next engine shop visit and before it exceeds 6,200 cycles since new, which is about engine flight cycle 54,200 on the record's counters. The HPT 2nd-stage hub cannot be assessed because its serial number and cycles are unknown.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the HPT 1st-stage hub exceeds 6,200 cycles since new (about engine flight cycle 54,200), under paragraph (g) of AD 2025-19-13.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub serial number is unknown. Without it, the screen cannot tell whether the hub is a Table 1 listed part (P/N 2A4802 is listed with four serial numbers).
- **Missing fact:** The HPT 2nd-stage hub cycles since new are unknown. Without them, the removal limit (3,900 to 6,000 cycles depending on serial number) cannot be checked even if the serial number is listed.
- **Missing fact:** No events are recorded. Whether an engine shop visit has occurred or will occur is therefore unknown, and it determines when removal is triggered.
- **Note:** Authority state is in force: the final rule was published 2025-09-24 and is effective 2025-10-29, before the 2026-03-10 question date. The 2025-10764 NPRM was superseded by the final rule and was not used for the obligation.
- **Note:** Engine cycles were 50,000 on the effective date and 50,500 on 2026-03-10. The first-stage hub read 2,000 cycles since new on 2025-10-29 and 2,500 in the current undated field, which is consistent with 500 cycles of operation.
- **Note:** The first-stage hub was installed 2024-06-03, before the effective date, so the record shows no installation after the effective date.
- **Note:** This screen does not determine compliance status. The 2nd-stage hub remains unassessed until its serial number and cycles since new are confirmed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row for 2A5001 / PKLBST7489 (limit 6,200)

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2522-A5 is within the applicability of AD 2025-18469, which was effective October 29, 2025, so it was in force on the question date. The engine record lists no installed components and no events, so it cannot be determined whether an HPT 1st-stage or 2nd-stage hub with a listed P/N and S/N is installed, and the required-action status cannot be screened.
- **Stated timing:** Under paragraph (g), remove affected hubs at the next engine shop visit after October 29, 2025 before exceeding the listed removal cycle limit, or within 100 flight cycles of October 29, 2025, whichever occurs later. No shop visit is recorded, and the engine flight-cycle count is not supplied, so no date can be computed.
- **Missing fact:** No HPT 1st-stage hub record is present. Whether a hub with P/N 2A5001 and one of the listed S/Ns (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489) is installed is needed to determine whether paragraph (g) applies. An absent record is not evidence that the hub is absent.
- **Missing fact:** No HPT 2nd-stage hub record is present. Whether a hub with P/N 2A4802 and one of the listed S/Ns (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100) is installed is needed to determine whether paragraph (g) applies.
- **Missing fact:** No engine event history is recorded. Whether any engine shop visit has occurred since October 29, 2025, and whether it meets the AD's engine shop visit definition, is needed to determine when the removal action is due.
- **Missing fact:** The engine flight-cycle counter is not supplied. It is needed to compute the 100-flight-cycle deadline from October 29, 2025 and to compare installed hubs against their removal cycle limits.
- **Note:** This is a screening aid only and does not determine compliance, airworthiness, or return-to-service status.
- **Note:** The engine record is synthetic and has no installed components and no events. Absence of records is not evidence that listed hubs are absent or unaffected.
- **Note:** The FR document 2025-10764 (NPRM) is superseded by the final rule 2025-18469 for this screen; only the final rule was used to answer.
- **Note:** If no listed hub is installed, paragraph (h) still prohibits installing listed hubs in any engine, so the continuing obligations remain relevant.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model is V2500-A1, which is not among the V2500 models this screen supports, so no applicability determination is made against FR document 2025-18469.
- **Note:** The directive is in force as of the question date, with an effective date of 2025-10-29.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011, 2000 cycles since new) appears in Table 1 to paragraph (g), but no applicability or part-status determination is made because the engine model is outside the supported scope.
- **Note:** The engine record has no shop visit events, so none were evaluated.
- **Unresolved locator:** 2025-18469 (c) Applicability paragraph listing supported IAE AG V2500 models

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The engine is a supported V2527-A5 with a 3rd stage HPC rotor blade set recorded as P/N 6A8353, which is a listed part, so the directive applies and is in force. Replacement of the full set is required only at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed, and the record shows no events, so no event has been triggered on the facts supplied.
- **Stated timing:** At the next engine shop visit after the effective date of September 24, 2026 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum), replace the full set of 3rd stage HPC rotor blades with parts eligible for installation.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** No engine event history is recorded. Whether the engine has been inducted into a shop visit on or after 2026-09-24, and whether the 3rd stage HPC rotor blades were exposed at that visit, cannot be determined, so the trigger has not been confirmed either way.
- **Missing fact:** Serial numbers are not tracked at set level, so the individual blade identities and whether each blade is a listed part cannot be confirmed from the record; the set is matched on part number only.
- **Note:** This is a screening aid, not a compliance determination; the record shows no shop visit events, so no required action is confirmed as triggered.
- **Note:** The applicable text is the final rule 2026-16954 as corrected by 2026-18423, not the November 2025 NPRM, which used a different trigger (next blade exposure) and was superseded.
- **Note:** The record lists P/N 6A8353, which is a listed part; the record does not show whether a part eligible for installation is already fitted.
- **Note:** The engine's shop visit history and whether any inducted visit occurred after 2026-09-24 should be reviewed.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** AD 2026-17-03 (FR 2026-16954, as corrected by 2026-18423) applies to V2533-A5 engines with a 3rd stage HPC rotor blade of P/N 6A8353 or 6A8688 installed. The record lists the installed 3rd stage HPC rotor blade set as P/N 6C8368, a part eligible for installation, not an affected P/N, so the supplied facts place the engine outside the directive, subject to per-blade confirmation.
- **Missing fact:** The record gives one set-level P/N (6C8368). The directive applies by individual blade P/N (6A8353 or 6A8688), so each installed 3rd stage HPC rotor blade's P/N should be confirmed. A mixed set containing any 6A8353 or 6A8688 blade would bring the engine within the applicability.
- **Missing fact:** The set serial number is not tracked, so individual blade identity cannot be confirmed from the record. This is needed to verify per-blade P/N applicability.
- **Note:** Authority state: the final rule 2026-16954 has an effective date of 2026-09-24, which precedes the 2026-10-05 question date, so it is in force. Correction 2026-18423 changes only the word 'blade' in paragraph (g).
- **Note:** The engine model V2533-A5 is within the supported scope.
- **Note:** The events list is empty, so no engine shop visit or blade exposure is recorded.
- **Note:** This is a screening aid and not a compliance determination. If any installed 3rd stage HPC rotor blade is confirmed as P/N 6A8353 or 6A8688, the directive's shop-visit exposure requirement must be re-screened.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has a 3rd stage HPC rotor blade set recorded as P/N 6A8688, which is within the directive's applicability. Whether the replacement requirement is triggered depends on whether the 2026-09-14 shop visit, which predates the 2026-09-24 effective date, counts as an engine shop visit after the effective date, so the screen needs review.
- **Stated timing:** Replacement of the full 3rd stage HPC rotor blade set is required at the next engine shop visit after the effective date (September 24, 2026) where a 3rd stage HPC rotor blade is exposed. The 2026-09-14 induction predates that date, but a blade exposure was recorded on 2026-09-30, after the effective date, during that visit. Whether this triggers the requirement needs review.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The engine flight-cycle counter is not supplied, so no cycle-based deadline can be computed.
- **Missing fact:** Blade serial numbers are not tracked at set level, so it cannot be confirmed which blades were removed or whether the full set is still installed at the same P/N.
- **Missing fact:** The operator's record says the 2026-09-14 induction qualifies as an engine shop visit, but that induction predates the effective date, so whether it falls within paragraph (g) turns on the interpretation above rather than on this flag.
- **Missing fact:** The state of the rotor blade set after the 2026-09-30 exposure, including whether replacement with parts eligible for installation under paragraph (h)(1) has already been done, is not recorded.
- **Note:** This is a screening aid, not a compliance determination. Nothing here states that the engine or any part is compliant or noncompliant, airworthy, or approved for return to service.
- **Note:** The operator's qualifies_as_engine_shop_visit flag for AD 2026-17-03 is an assertion to check, not evidence that settles the outcome. Under the directive's definition, the shop visit is the induction, which occurred before the effective date.
- **Note:** Authority state is in force: the final rule is effective September 24, 2026, and the question date is September 30, 2026. The September 10, 2026 correction keeps that effective date.
- **Note:** The record supports that a blade was removed from the stage 3-8 drum on 2026-09-30, which meets the exposure definition in paragraph (h)(2) and occurred after the effective date, while the induction occurred before it.
- **Note:** No cycle counter or blade serial tracking is supplied, so no cycle-based deadline or component cycles remaining can be computed. The placeholder cycle values in alternative readings are not computed deadlines.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a supported V2524-A5 with a 3rd stage HPC rotor blade set listed as P/N 6A8353, and AD 2026-17-03 is in force as of 2026-10-05. The 2026-10-01 shop visit followed the 2026-09-24 effective date, but the record states that no 3rd-stage blade was removed from the stage 3-8 drum, so the blade-exposure trigger in paragraph (g) is not shown and no blade replacement is triggered on these facts.
- **Stated timing:** No deadline is set by the record. The replacement obligation attaches at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed, meaning any blade is removed from the HPC stage 3 to 8 drum.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** The engine flight-cycle counter is not in the record, so no cycle-based deadline can be computed if a blade exposure later occurs.
- **Missing fact:** Blade serial numbers are not tracked at set level. This does not change the part-number match, but a reviewer may want the individual blade records to confirm no blade was removed from the drum during the 2026-10-01 visit.
- **Missing fact:** The record describes the 2026-10-02 event as the HPC rotor being exposed for inspection with no 3rd-stage blade removed from the drum. Confirmation from the maintenance work package that no blade was removed during the 2026-10-01 to 2026-10-04 visit would settle whether the paragraph (g) trigger occurred. This document is not part of the engine record.
- **Note:** The record's qualifies_as_engine_shop_visit assertion is the operator's claim; the induction also matches the AD's own definition in (h)(3) on its face.
- **Note:** The 2026-10-02 component_exposure entry records the HPC rotor as exposed for inspection, which is not the same as the AD's defined blade exposure (a blade removed from the stage 3 to 8 drum). That distinction drives the no-action result.
- **Note:** If the 2026-10-01 visit did in fact remove any 3rd stage blade from the drum, paragraph (g) would be triggered by that visit, and the replacement would then be due at that visit with no cycle-based deadline computable from this record.
- **Note:** No engine flight-cycle count is supplied, so no latest_engine_flight_cycles value can be computed.
- **Note:** This is a screening aid only and does not determine compliance or airworthiness of the engine.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** This is a proposed rule, not yet in force, so it cannot require action now. The supported V2527E-A5 engine has an installed 3rd stage HPC rotor blade set recorded as P/N 6A8353, which matches the proposed applicability paragraph, so the engine would fall within scope if the AD is adopted. The proposed action would be triggered only at a future 3rd stage HPC rotor blade exposure after an effective date, and no effective date exists.
- **Missing fact:** No final rule or effective date for this directive appears in the supplied record; the document is an NPRM whose comment period closed January 2, 2026. The required action cannot be due until a final AD is published and effective.
- **Missing fact:** The event list is empty, so there is no record of 3rd stage HPC rotor blade removals from the HPC stage 3 to 8 drum. Whether a future exposure would trigger the proposed replacement cannot be assessed from history.
- **Missing fact:** Serial numbers are not tracked at set level. The directive lists the part number only, so this does not block the screen, but any future replacement record should track blade-level identity.
- **Note:** This is a screening aid, not a compliance determination. The output does not state that the engine or any part is compliant or noncompliant.
- **Note:** The engine record has no ad_records or amoc_claims entries for this directive, and none were needed to reach this result.
- **Note:** Re-screen once a final rule is published and has an effective date, and again if any 3rd stage HPC rotor blade exposure is recorded.
- **Unresolved locator:** 2025-20088 (h) Definitions paragraphs (h)(1) and (h)(2)
- **Unresolved locator:** 2025-20088 preamble Document header: Type Proposed Rule; Effective date none

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 (FR 2025-17066, effective 2025-10-10) applies to V2527-A5 engines. The record shows the operator has not yet incorporated table 1 to paragraph (g) into its approved maintenance program or the V2500-A5 TLM ALS, so a required revision is due within 90 days of the effective date, by 2026-01-08.
- **Stated timing:** Revise paragraph B.1 of the Maintenance Scheduling section of the ALS in the applicable TLM under (g)(1), and revise the approved maintenance or inspection program under (g)(2) for air carrier operations, within 90 days after 2025-10-10, i.e., by 2026-01-08.
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** No installed component record for the HPT Stage 1 Hub (P/N 2A5001) is present, so the hub's part and serial numbers and cycle history cannot be checked. This does not affect the program-revision obligation but is needed for any later inspection or limit review.
- **Missing fact:** No installed component record for the HPT Stage 2 Hub (P/N 2A4802) is present, so its identifiers and cycle history cannot be checked.
- **Missing fact:** The operator record does not state which TLM (V2500-A5, V2500-D5, or V2500-E5) governs this engine. Paragraph (g)(1) names a different P/N and TLM for each, so the correct one must be confirmed to identify the document to revise.
- **Missing fact:** The record says neither the approved program nor the TLM ALS has yet incorporated table 1. Confirmation that the revision is complete and the date it was made is needed to close the (g)(1) and (g)(2) actions.
- **Note:** This is a screening aid, not a compliance determination. The operator's record shows the program revision has not been incorporated, so the screen points to a required action rather than a finding of noncompliance.
- **Note:** The deadline is computed from the stated effective date of 2025-10-10 in the final rule. The FR publication date of 2025-09-05 is not the effective date, so a deadline of 2025-12-04 is not used.
- **Note:** No engine flight-cycle counter is in the record, so latest_engine_flight_cycles is null. The hub cycle limits cannot be computed because no hub components are recorded.
- **Note:** The events list is empty. The required action is a documentation revision, so no shop visit event is needed to trigger it.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model V2522-A5 is listed in the directive's applicability, and the final rule is effective 2025-10-10, so the paragraph (g)(1) ALS/TLM revision is required within 90 days, by 2026-01-08. The paragraph (g)(2) program revision applies to air carrier operations, and the record does not show whether this operator is one.
- **Stated timing:** Within 90 days after the 2025-10-10 effective date, i.e., by 2026-01-08, for the paragraph (g)(1) Time Limits Manual Maintenance Scheduling revision; for air carrier operations, the paragraph (g)(2) approved maintenance or inspection program revision is due on the same 90-day schedule.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the operator conducts air carrier operations is unknown. This determines whether the paragraph (g)(2) revision of the existing approved maintenance or inspection program applies in addition to the paragraph (g)(1) TLM revision.
- **Missing fact:** No engine flight-cycle counter is recorded. The 2025-17066 text sets a calendar deadline, not a cycle limit, so this does not change the deadline, but the cycle count is needed for any later piece-part exposure or cycle-based planning.
- **Missing fact:** No HPT Stage 1 Hub (P/N 2A5001) record is present. The directive's TASK 72-45-11-200-006 inspection is performed at piece-part exposure, so the hub's installed status and cycles matter for later inspection planning, though not for the 90-day manual revision.
- **Missing fact:** No HPT Stage 2 Hub (P/N 2A4802) record is present. The directive's TASK 72-45-31-200-009 inspection is performed at piece-part exposure, so the hub's installed status and cycles matter for later inspection planning, though not for the 90-day manual revision.
- **Missing fact:** Whether the operator's current Time Limits Manual revision and approved maintenance program already include the tasks 72-45-11-200-006 and 72-45-31-200-009 is not in the record. The engine record does not show the operator's AD status, so this cannot be confirmed from the record.
- **Note:** This is a screening aid and not a compliance determination. The record contains no installed components and no events, so nothing in the record shows a hub part's status or any shop visit.
- **Note:** The 2025-17066 rule text describes the inspection tasks as performed at piece-part exposure, which is governed by other regulations. The AD's own required actions are the one-time manual and program revisions.
- **Note:** The 2024-26092 NPRM is superseded for this screen by the final rule 2025-17066, which is in force on the question date.
- **Unresolved locator:** 2025-17066 (g)(1) Table 1 to Paragraph (g) rows HPT Stage 1 Hub 2A5001 and HPT Stage 2 Hub 2A4802

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is a listed model, and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) matches Table 1 with a 6,000-cycle removal limit and 990 cycles since new, leaving 5,010 cycles. AD 2025-19-13 becomes effective 2025-10-29, so no required action is triggered on the 2025-10-15 question date, though the obligations take effect on that date.
- **Stated timing:** Once effective on 2025-10-29: at the next engine shop visit after 2025-10-29 before exceeding the listed removal cycle limit, or within 100 flight cycles of 2025-10-29, whichever occurs later, remove the listed hub and replace it with an eligible part. The installation prohibition applies from 2025-10-29.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** No engine events are recorded, so no shop visit has been identified after the 2025-10-29 effective date. Whether a future induction qualifies as an engine shop visit under paragraph (i)(2) cannot be determined from the record.
- **Missing fact:** The current engine flight-cycle counter is not in the record. It is needed to compute the 100-flight-cycle deadline measured from the effective date and to confirm the engine's position relative to the hub limit.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0018 is not listed in Table 1, so it does not match a listed part on this record. This is not evidence that the hub is unaffected, because the record may be incomplete.
- **Note:** The question date precedes the 2025-10-29 effective date, so the AD cannot yet require action. Screening result is a review aid only and is not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSR2100, limit 6,000

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** Directive 2025-18469 is in force (effective 2025-10-29) and covers V2531-E5 engines. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in Table 1 with a 4,800-cycle removal limit, and the record shows 4,990 cycles since new, so removal and replacement is required by the later of the two paragraph (g) deadlines, which is engine cycle 60100 (60 cycles remain at the 60040 snapshot).
- **Stated timing:** Remove the affected HPT 1st-stage hub from service and replace it with a part eligible for installation within 100 flight cycles of the 2025-10-29 effective date (engine cycle 60100). The removal cycle limit is already exceeded, so the next-shop-visit prong cannot be met before the limit and the later 100-cycle window governs.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The current cycles_since_new value (4,990) and the dated 2025-10-29 reading (4,950) differ and the current value has no date; the exact figure should be confirmed, though both exceed the 4,800 limit.
- **Missing fact:** No engine events are recorded; whether any engine shop visit occurs before the deadline is not shown, though the 100-cycle window applies regardless.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0019) does not match any Table 1 entry, so no 2nd-stage action is indicated from the supplied record.
- **Note:** No engine shop visit event is recorded, so the shop-visit prong cannot be evaluated; the cycle-based deadline controls here.
- **Note:** This is a screening aid, not a compliance determination; the outcome reflects the supplied record and directive text only.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200, limit 4,800 cycles
- **Unresolved locator:** 2025-18469 preamble Effective date 2025-10-29 in document header and DATES

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2533-A5 engine's installed HPT 1st-stage disk (P/N 2A5001) and HPT 2nd-stage disk (P/N 2A4802) match the directive's part numbers, so the high-thrust USI requirement of paragraphs (g)(1) and (g)(2) may apply. Whether it is triggered depends on Appendix A serial-number listings and on engine cycles since July 13, 2021, which the record does not supply, so the screen needs review.
- **Stated timing:** Perform the USI of each affected disk at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first. The record has no shop-visit events and no cycles-since-effective-date data.
- **Missing fact:** The directive applies only to HPT 1st-stage disks whose serial number is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1. The Appendix A table is not in the supplied text, so the listing of SYN-DISK1-0020 cannot be confirmed.
- **Missing fact:** The directive applies only to HPT 2nd-stage disks whose serial number is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713 Rev 1. The Appendix A table is not in the supplied text, so the listing of SYN-DISK2-0020 cannot be confirmed.
- **Missing fact:** The engine record has no flight-cycle counter, and the 3,200-cycle limit runs from the July 13, 2021 effective date. Cycles accumulated since that date are needed to decide whether the limit has been reached.
- **Missing fact:** The event list is empty. The record does not show whether an engine shop visit (separation of H-P flanges) has occurred since July 13, 2021, which would trigger the USI before the cycle limit. An empty list does not establish that no shop visit occurred.
- **Missing fact:** Whether any HPT disk was previously inspected under the directive or has a documented USI result is not in the record. Such evidence would bear on whether the requirement is already addressed.
- **Note:** Synthetic engine SYN-ENG-020 (V2533-A5, serial SYN-V2500-0020) was screened as of 2022-03-01 against AD 2021-11960 (AD 2021-11-15, effective July 13, 2021).
- **Note:** AD 2022-02-09 (document 2022-02574) supersedes AD 2021-11-15 effective March 15, 2022. It is not yet in effect on the question date, so it was not applied here, but a reviewer should check it, since its compliance times for high-thrust engines may be shorter.
- **Note:** The V2533-A5 is a high-thrust model under the superseding AD's preamble, so the shorter compliance time it sets may matter once effective.
- **Note:** The Appendix A serial-number tables for NMSB V2500-ENG-72-0713 Rev 1 are not in the supplied text. Without them, serial-number listing cannot be confirmed.
- **Note:** The compliance figures and tables referenced by the superseding AD are not in the supplied text.
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
- **Summary:** Directive 2022-02574 takes effect March 15, 2022, so it cannot require action on the question date of 2022-03-01. The installed HPT 1st-stage and 2nd-stage disk part numbers match the directive, but applicability depends on whether their serial numbers appear in the service bulletin appendix tables, which are not in the supplied text.
- **Missing fact:** Appendix A, Table 1 (HPT 1st-stage disk P/N 2A5001) of IAE NMSB V2500-ENG-72-0713, Revision 1, is not in the supplied text. Whether serial number SYN-DISK1-0020 is listed determines whether the disk falls within paragraph (c)(1).
- **Missing fact:** Appendix A, Table 2 (HPT 2nd-stage disk P/N 2A4802) of IAE NMSB V2500-ENG-72-0713, Revision 1, is not in the supplied text. Whether serial number SYN-DISK2-0020 is listed determines whether the disk falls within paragraph (c)(2).
- **Missing fact:** Figure 1 to paragraph (g)(1), which sets the compliance time for a high-thrust engine, is not in the supplied text (it is an image). The due point for the USI cannot be confirmed without it.
- **Missing fact:** The engine record has no engine flight-cycle counter and no event history (events is empty). Shop-visit status and cycles since the effective date are needed to compute the deadline under paragraphs (g)(1) and (g)(2).
- **Note:** Screening aid only, not a compliance determination. Authority state is published_not_yet_effective, so no action is required on 2022-03-01.
- **Note:** The V2533-A5 is a high-thrust model, so the high-thrust compliance path applies, not the low-thrust HPT-module-removal path.
- **Note:** Until March 15, 2022, AD 2021-11-15 (Amendment 39-21577) is in force and has a similar USI requirement with compliance keyed to its July 13, 2021 effective date. This screen did not evaluate that AD; a reviewer should check it.
- **Note:** Serial numbers in the record are synthetic placeholders. They must be checked against the actual NMSB appendix tables, which were not supplied.
- **Note:** The record has no engine flight-cycle counter and no event history, so no deadline can be computed.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (FR 2022-02574) supersedes AD 2021-11-15 and is in force on the question date. The V2530-A5 is a supported model with a P/N 2A5001 HPT 1st-stage disk and a P/N 2A4802 HPT 2nd-stage disk installed, but applicability turns on whether those serial numbers appear in the Appendix A tables, which are not in the supplied text, and the compliance time depends on Figure 1, which is also not supplied.
- **Stated timing:** For high-thrust model engines such as the V2530-A5, the USI of each disk is due at the next engine shop visit or within the Figure 1 compliance time, whichever is later, but in no case earlier than 10 flight cycles after March 15, 2022. Figure 1 is not included in the supplied text, so the due date cannot be computed.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (and NMSB V2500-E5-72-0015 Rev 1) is not in the supplied text. Whether HPT 1st-stage disk S/N SYN-DISK1-0021 is listed there determines whether paragraph (c)(1) and paragraph (g)(1) apply.
- **Missing fact:** Appendix A, Table 2 of the same NMSB documents is not in the supplied text. Whether HPT 2nd-stage disk S/N SYN-DISK2-0021 is listed there determines whether paragraph (c)(2) and paragraph (g)(2) apply.
- **Missing fact:** Figure 1 to paragraph (g)(1) (the compliance-time figure) is an image that is not included in the supplied text. It is needed to compute the USI due date in flight cycles.
- **Missing fact:** The engine flight-cycle counter is not in the record. It is needed to compare the engine against the Figure 1 compliance time and the 10-flight-cycle floor.
- **Missing fact:** No operator AD status record for this directive is in the engine record. Whether the USI has already been done, and under which NMSB revision, cannot be confirmed.
- **Missing fact:** The events list is empty. The record does not show whether an engine shop visit has occurred or whether any disk was inspected or replaced, so the trigger for the USI cannot be confirmed.
- **Note:** This is a screening aid only and is not a compliance determination. The engine record was not assessed for airworthiness, and no return-to-service conclusion is drawn.
- **Note:** The V2530-A5 is a high-thrust model under the directive's preamble, so the Figure 1 timing applies rather than the low-thrust Figure 2 timing.
- **Note:** The engine record contains no ad_records or amoc_claims entries, so no operator-asserted AD status or alternative method of compliance was available to check.
- **Note:** The serial numbers in the record are synthetic (SYN- prefix). Their listing status must be checked against the NMSB Appendix A tables before any applicability is confirmed.
- **Note:** Paragraph (i) credit for previous actions applies only to actions taken under NMSB V2500-E5-72-0015 original issue for V2531-E5 engines, so it does not apply to this V2530-A5 record.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2022-02574 (c) Applicability: V2530-A5 with HPT 1st-stage disk P/N 2A5001 and HPT 2nd-stage disk P/N 2A4802, each with a serial number listed in Appendix A

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2021-11-51 (Federal Register 2021-14268) is in force on the question date and applies to this V2533-A5 engine, whose installed HPT 1st-stage disk (P/N 2A5001, S/N PKLBSH1829) is in the listed population. A USI of that disk is required within 10 flight cycles after July 19, 2021, which is by engine cycle 33010; the record shows 33004 cycles on 2021-07-20 and no USI event, so 6 cycles remain on the screen.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021, i.e., by engine flight cycle 33010, unless the USI was already done.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** No USI event is recorded for the HPT 1st-stage disk. The AD says 'unless already done', so a recorded USI performed per NMSB V2500-ENG-72-0713 paragraph 6 and its result is needed to settle whether the action is still outstanding.
- **Missing fact:** The Table 1 image to paragraph (g)(1) and Table 2 image to paragraph (g)(2) are not included in the supplied text. They may define the affected population beyond the serial numbers listed in paragraph (c), so the full population cannot be confirmed from the text supplied.
- **Missing fact:** The installed HPT 2nd-stage disk serial SYN-DISK2-0022 does not match any serial listed in paragraph (c)(2) for P/N 2A4802, so it is not matched on the text supplied. Confirm against Table 2 to paragraph (g)(2), which is not included in the text.
- **Note:** Screening aid only; this is not a compliance determination. The engine record has no ad_records or amoc_claims entries for this AD, so no operator AD status is asserted.
- **Note:** Deadline computed from the 33000 engine-cycle reading on 2021-07-19, the effective date. The 33004 reading on 2021-07-20 is the latest recorded count.
- **Note:** Paragraph (c)(2) lists HPT 2nd-stage disk serials; the installed S/N SYN-DISK2-0022 is not among them, so that disk is not matched on the text supplied.
- **Note:** Synthetic record (SYN- identifiers).
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
- **Summary:** The V2533-A5 is a supported model and both installed disk part numbers (2A5001 and 2A4802) match the directive's paragraph (c) part numbers, but applicability depends on whether the installed serial numbers appear in the Appendix A tables of the NMSB, which are not in the supplied text. The directive is in force (effective 2021-07-13), so the required USI would be due at the next engine shop visit or within 3,200 flight cycles after 2021-07-13, whichever occurs first, if the serials are listed.
- **Stated timing:** If the serial numbers are listed in Appendix A, the USI of each affected disk is due at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. The engine has no recorded shop visit (events is empty).
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015 for V2531-E5) is not in the supplied text. Whether HPT 1st-stage disk S/N PKLBSH1829 is listed is needed to establish applicability under paragraph (c)(1).
- **Missing fact:** Appendix A, Table 2 of the same NMSB is not in the supplied text. Whether HPT 2nd-stage disk S/N SYN-DISK2-0022 is listed is needed to establish applicability under paragraph (c)(2).
- **Missing fact:** Engine flight cycles on the effective date are not recorded, so the 3,200-cycle limit counted from 2021-07-13 cannot be computed. Only the 2021-07-19 and 2021-07-20 readings are available.
- **Missing fact:** No engine shop visit history is recorded. Whether an engine shop visit has occurred or will occur after 2021-07-13 determines the earlier of the two deadlines.
- **Note:** This is a screening aid only. It does not establish compliance or noncompliance, and it does not establish airworthiness.
- **Note:** The engine is a V2533-A5, which is a supported model. Both installed disks match the directive's part numbers, but the serial-number match cannot be confirmed from the supplied text.
- **Note:** The engine record shows cycles 33000 on 2021-07-19 and 33004 on 2021-07-20. The cycle count at the effective date is not recorded, so the 3,200-cycle deadline cannot be computed.
- **Note:** The NPRM and FR text say the NMSB is the source for the appendix serial lists, and the NMSB text was not provided. Matched parts are left empty because no serial-number match was confirmed.
- **Note:** No operator AD status or AMOC claims were provided in the record.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527M-A5 engine is a supported model, and its HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) is listed in table 1 of AD 2025-18469, which was effective 2025-10-29. The hub's removal cycle limit is 6,000 cycles since new and it shows 3,500, so removal is required at the next engine shop visit before it exceeds that limit, or within 100 flight cycles of the effective date if that is later.
- **Stated timing:** Remove the hub at the next engine shop visit, and in any case before it exceeds 6,000 cycles since new (about 2,500 cycles from the 2026-10-06 snapshot). The 100-flight-cycle window from the effective date (engine cycles 20,100) has already passed; under the 'whichever occurs later' wording, the shop-visit and cycle-limit deadline controls.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The only dated cycles-since-new reading for the HPT 2nd-stage hub is 1,000 at 2025-10-29. The current value of 3,500 is undated. The projected limit date of engine cycle 25,000 assumes the hub accumulates cycles one-for-one with engine flight cycles since 2025-10-29, which should be confirmed.
- **Missing fact:** The engine record shows no engine shop visit since the effective date of 2025-10-29. Whether one has occurred or is scheduled matters for the timing of removal, because the required removal is due at the next shop visit or before the hub exceeds its cycle limit, whichever is later.
- **Missing fact:** The maintenance program revision of 2025-12-01 cites AD 2025-17-16, a different AD number from the directive under review. The record does not show the AD status or compliance record for AD 2025-18469 itself, and this screen does not rely on the operator's program revision as evidence of compliance.
- **Note:** This is a screening aid, not a compliance determination. The status of the HPT 2nd-stage hub under this AD is not established by this screen.
- **Note:** The HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0023) does not match any table 1 serial number, so it is not a listed part under this AD on the supplied facts. Its cycles-since-new value of 3,500 is undated.
- **Note:** The 3rd stage HPC rotor blade set is not addressed by this AD and was not matched.
- **Note:** The 2026-10-06 engine cycle reading of 22,500 is used as the current count. The 2025-10-29 reading of 20,000 is used as the effective-date count for the 100-cycle window.
- **Note:** Projected deadline: if the hub accumulates one cycle per engine flight cycle from the 2025-10-29 reading of 1,000 hub cycles, it reaches 6,000 at engine cycle 25,000.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), row HPT 2nd-stage hub, 2A4802, PKLBSR2100, limit 6,000

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527M-A5 engine lists an installed 3rd stage HPC rotor blade set with P/N 6A8688, which is within the directive's applicability, and the directive is in force since 2026-09-24. Replacement of the full 3rd stage HPC rotor blade set with parts eligible for installation is required at the next engine shop visit after 2026-09-24 where the blade is exposed; no such shop visit is recorded, so no deadline is computed.
- **Stated timing:** At the next engine shop visit after the effective date of 2026-09-24 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline applies before that event.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The blade set serial number is recorded as not tracked at set level, so the installed blades cannot be traced individually; this does not change the applicability match on P/N 6A8688 but limits traceability for the replacement record.
- **Missing fact:** No engine shop visit after 2026-09-24 is recorded. Whether and when the engine is inducted for maintenance with the 3rd stage HPC rotor blade exposed is unknown and determines when the replacement is required.
- **Missing fact:** No operator confirmation is recorded of whether any 3rd stage HPC rotor blade set was already replaced with parts eligible for installation, for example under IAE AG SB V2500-ENG-72-0716, which the FAA said would demonstrate compliance with this AD.
- **Note:** The directive is a final rule effective 2026-09-24, so it is in force on the question date 2026-10-06 and can require action.
- **Note:** The correction document 2026-18423 fixes only the omitted word 'blade' in paragraph (g); the event-triggered obligation is the same under either version.
- **Note:** The events list contains only a maintenance program revision dated 2025-12-01 that incorporates table 1 of AD 2025-17-16. That is a different AD and does not satisfy or address this directive.
- **Note:** The record's engine_cycle_readings show 22500 cycles on 2026-10-06; no cycle-based deadline applies to this directive.
- **Note:** The screen does not determine compliance; it identifies that the required replacement is triggered only at a qualifying future shop visit with blade exposure.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 (effective 2025-10-10) applies to this V2527M-A5 engine, and its one-time ALS/maintenance program revision was due by 2026-01-08. The record shows the revision on 2025-12-01, so no action is triggered now, but the piece-part inspections in the revised TLM paragraph B.1 still bind at each piece-part exposure.
- **Stated timing:** The one-time revision of TLM Maintenance Scheduling paragraph B.1 and the air carrier maintenance program was due within 90 days after 2025-10-10, i.e. by 2026-01-08; the record shows it was made 2025-12-01. The HPT 1st-stage hub (2A5001) and HPT 2nd-stage hub (2A4802) inspections are due at each piece-part exposure.
- **Missing fact:** The HPT 1st-stage hub record has a cycles_since_new value but no dated reading and no installed_at date, so its exposure history cannot be tied to the AD timeline. This does not change the one-time revision outcome, but it is needed to track piece-part exposure events.
- **Missing fact:** No piece-part exposure or shop visit event is recorded for either hub since the revision. Whether TASK 72-45-11-200-006 or TASK 72-45-31-200-009 was performed at any exposure cannot be confirmed from the record.
- **Missing fact:** The TLM revision text itself (paragraph B.1 with both tasks) was not supplied. The record only summarizes it, so the revised content is taken from the operator's description.
- **Note:** This is a screening aid, not a compliance determination. The operator record of the revision is a claim checked against the directive text; the revised TLM content was not supplied.
- **Note:** The 90-day deadline is date-based, so engine flight cycles do not set the deadline. The directive sets no cycle limit, and the AUSI interval is not stated in the directive text, so component cycles remaining cannot be computed.
- **Note:** The 3rd stage HPC rotor blade set (6A8688) is not listed in the directive and is not matched.
- **Note:** Under either a publication-date or effective-date reading of the 90-day period, the 2025-12-01 revision falls within the window, so no alternative reading changes the outcome.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 engine is within the applicability of AD 2025-19-13, which is in force since its October 29, 2025 effective date. Neither installed hub matches a P/N and S/N pair in Table 1 to paragraph (g), so no removal is triggered on the record provided, but the installation prohibition in paragraph (h) still binds.
- **Missing fact:** The installed HPT 2nd-stage hub (P/N 2A4802) carries serial number PKLBST5011, which Table 1 lists only under P/N 2A5001 (HPT 1st-stage hub). The P/N and S/N pairing should be verified against the part's records; if the hub is actually a listed part, the removal requirement would apply.
- **Missing fact:** The events list is empty, so the record does not show whether any engine shop visit has occurred. This matters only if a listed hub is later found installed, because removal is tied to the next engine shop visit after the effective date.
- **Note:** The question date (2026-10-06) is after the October 29, 2025 effective date, so the final rule is in force. The June 2025 NPRM (2025-10764) is superseded by the final rule and was used only for background.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0024) has a serial number not in Table 1, so it is not a listed part.
- **Note:** The HPT 2nd-stage hub's serial number PKLBST5011 appears in Table 1 only with P/N 2A5001, so the P/N and S/N pair does not match the listed 2A4802 entries. This is a screening result on the record as provided and is not a compliance determination.
- **Note:** Installed hubs show 3000 cycles since new, which is above several Table 1 limits. Those limits apply only to matched listed parts, and none are matched here.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine record lists a CFM56-5B4/3 model, which is not among the IAE V2500 models supported by this screen, so no applicability determination is made under Federal Register document 2025-17066.
- **Note:** The engine model CFM56-5B4/3 is a CFM International engine and is not an IAE V2500 model covered by this directive or by this screen.
- **Note:** No installed components, events, or AD records were supplied, so no further screening was performed.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a listed V2530-A5 and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) matches a Table 1 entry with a 6,200-cycle removal limit. At 3,600 cycles since new, 2,600 cycles remain, so removal and replacement is required at the next engine shop visit before that limit is reached.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29 and before the hub exceeds 6,200 cycles since new, which is about 2,600 cycles after the 2026-03-01 snapshot. The 100-flight-cycle alternative under paragraph (g) ended at engine cycle 20100 and is treated as the earlier bound, not the controlling deadline.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** No engine shop visit since 2025-10-29 is recorded. Whether a shop visit has occurred, and whether the hub was removed at it, determines whether the required action has been completed; this screen cannot confirm either.
- **Note:** The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0026) does not match any Table 1 entry, so it is not counted as affected under the screen.
- **Note:** The installed 1st-stage hub's cycles_since_new is 3,600 with no date. The dated reading of 3,000 on 2025-10-29 plus 600 engine cycles to 2026-03-01 is consistent with 3,600 at the snapshot.
- **Note:** The 2024-06-10 blend repair and 2024-06-12 inspection predate the 2025-10-29 effective date. The screen does not treat them as a compliance or serviceability finding.
- **Note:** The engine-cycle readings (20,000 on 2025-10-29, 20,600 on 2026-03-01) are used for the cycle projection.
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
- **Summary:** The engine model is supported, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200, table limit 4,800 cycles since new) is listed in the directive. The record shows 4,750 cycles since new, so removal is due at the next engine shop visit before the limit is exceeded, and no later than engine flight cycle 15,300 under the later-of reading.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit before its cycles since new exceed 4,800 (about 50 cycles away), and in any case by engine flight cycle 15,300. No shop visit is recorded, and the 100-flight-cycle term from the 2025-10-29 effective date ended at engine flight cycle 15,100.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The 4,750 cycles-since-new figure is undated; the only dated reading is 4,500 on 2025-10-29. The value is assumed current as of the 2026-01-20 snapshot, and the deadline depends on it.
- **Missing fact:** No FAA AMOC approval reference or approval letter is on file, so the claimed 5,300-cycle limit cannot be used to set the removal deadline.
- **Missing fact:** Confirmation that no engine shop visit has occurred since the effective date. The events list is empty, but whether a shop visit (as defined in paragraph (i)(2)) has been or will be inducted determines when removal is triggered.
- **Note:** This is a screening aid, not a compliance determination. Synthetic record (SYN- identifiers).
- **Note:** Final rule 2025-18469 is in force (effective 2025-10-29) on the question date; the 2025-10764 NPRM was superseded and was not relied on.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0027) is not in table 1, so it is not matched and does not drive a deadline.
- **Note:** Cycles since new for the 1st-stage hub rose 250 from 2025-10-29 to the snapshot, matching the 250 engine-cycle increase, so the projection assumes one hub cycle per engine flight cycle.
- **Note:** The 15,300 deadline is the engine flight cycle at which the hub would reach 4,800 cycles since new, under the 1:1 assumption.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200, limit 4,800
- **Unresolved locator:** 2025-18469 preamble Request To Add Terminating Action and Request To Supersede or Cancel responses

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2524-A5 is a listed model, and AD 2025-19-13 (effective 2025-10-29) is in force on the question date. The installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) matches Table 1 with a 4,000-cycle removal limit, so the hub must be removed and replaced at the next engine shop visit, and no later than 4,000 cycles since new. The operator's N/A record ('no affected hubs installed') is contradicted by this record.
- **Stated timing:** Remove and replace the HPT 2nd-stage hub (S/N PKLBST5005) at the next engine shop visit after 2025-10-29, and before the hub exceeds 4,000 cycles since new. The paragraph (g) alternative of 100 flight cycles from the effective date (engine cycle 8,100) has already passed on the record (engine at 8,400 on 2026-02-10), and the 'whichever occurs later' wording makes the shop visit the operative event, bounded by the 4,000-cycle limit. No shop visit is recorded.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** No engine shop visit events are recorded. Whether a shop visit has occurred since 2025-10-29 determines whether the required removal has already been triggered, so this must be confirmed.
- **Missing fact:** The 1,400 cycles-since-new reading has no date. The timing and the 2,600 remaining figure assume it is current as of the 2026-02-10 snapshot.
- **Missing fact:** The operator's recorded N/A status says no affected hubs are installed. The record shows a listed hub installed, so the status claim needs review against the hub identification.
- **Missing fact:** The 4,000-cycle end point is estimated at engine cycle 11,000 by assuming the hub accrues cycles one-for-one with engine flight cycles since 2025-10-29, which the record supports only roughly (both rose by 400 cycles). Confirm the hub's own cycle accrual and whether it has stayed on this engine.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0028) is not listed in Table 1 by serial number, so it does not match on the record provided.
- **Note:** The 2nd-stage hub is recorded as installed since 2025-06-03, and the installed-at date and the engine record both need confirmation.
- **Note:** The cycle accrual estimate assumes one-for-one with engine flight cycles since 2025-10-29.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row for 2A4802 / PKLBST5005

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is a supported model, and the installed HPT 1st-stage hub serial PKLBSK9287 matches a serial listed in table 1 under P/N 2A5001, with a 100-cycle removal limit. The hub has 2400 cycles since new, so it is already past that limit, and removal is required at the next engine shop visit or within 100 flight cycles of the 2025-10-29 effective date, whichever occurs later. The installed P/N is recorded as 2A5001-01, so the P/N match needs confirmation, and the engine flight-cycle count at the effective date is not in the record, so no cycle deadline can be computed.
- **Stated timing:** Remove the affected HPT 1st-stage hub at the next engine shop visit after 2025-10-29 or within 100 flight cycles from 2025-10-29, whichever occurs later. The hub is already past its 100-cycle removal limit. The engine flight-cycle count on 2025-10-29 is needed to convert the 100-cycle prong into a cycle number.
- **Missing fact:** The installed P/N is recorded as 2A5001-01, while table 1 lists P/N 2A5001. Confirm whether the dash suffix is a configuration variant of the listed P/N. If it is not the same P/N, the hub would not match table 1 and the required action would not be triggered by this hub.
- **Missing fact:** The engine flight-cycle counter as of the effective date 2025-10-29 is not in the record. It is needed to compute the 100-flight-cycle prong of the deadline and so the latest engine flight-cycle number.
- **Missing fact:** No shop-visit events are recorded. Whether and when the next engine shop visit occurs after 2025-10-29 determines which prong of the 'whichever occurs later' deadline governs.
- **Missing fact:** The screen relies on the stated serial and cycles-since-new values for the installed hub. Those values are taken as recorded and have not been verified against the physical part.
- **Note:** This is a screening aid, not a compliance determination. The record reports the engine and hub data only and has not been verified against the physical part.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0029) is not listed in table 1 by serial number, so it does not match the table on the record provided.
- **Note:** The 2A5001-01 P/N question is the main open interpretation. If the suffix is a different part number, this hub would not match table 1, and the required action would be removed from this engine's screen. The reviewer should resolve that before relying on the timing.
- **Note:** The hub's cycles-since-new (2400) exceed its 100-cycle limit, so the shop-visit prong of paragraph (g) does not defer removal for this part.
- **Note:** The NPRM 2025-10764 was not relied on. The final rule 2025-18469 controls.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 1 (P/N 2A5001, S/N PKLBSK9287, removal cycle limit 100)

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
