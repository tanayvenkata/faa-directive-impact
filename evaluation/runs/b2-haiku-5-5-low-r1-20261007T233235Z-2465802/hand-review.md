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
- **Summary:** The engine model is supported and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) matches a row in Table 1 of AD 2025-18469, which is in force from 2025-10-29. The hub must be removed at the next engine shop visit, and no later than when it exceeds its 5,500-cycle removal limit (about engine flight cycle 45050 at the current utilization), with the 100-cycle window measured from the effective date having already passed.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 5,500 cycles since new; on current utilization that is about engine flight cycle 45050. Under the literal 'whichever occurs later' wording, the 100-flight-cycle window ended at engine flight cycle 41300, so that prong does not set the deadline.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** The events list is empty, so there is no record of whether an engine shop visit has occurred since the effective date. A shop visit that separates major mating flanges would trigger the removal obligation, and its date and qualification are needed to confirm the timing.
- **Missing fact:** The current cycles-since-new value of 3100 is undated. It is consistent with the dated 1650 reading at 2025-10-29 plus the 1450 engine cycles accrued to 2026-09-26, but the hub's current count should be confirmed against its own record.
- **Missing fact:** The content of the hub's Table 1 row serial number and any operator-recorded removal or replacement history are not in the record; these were not supplied.
- **Note:** This is a screening aid, not a compliance determination. The engine's AD status is not stated here.
- **Note:** The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0001) is not listed in Table 1, so it did not match on the record provided.
- **Note:** Under the 2025-18469 applicability and table, the Table 1 row for S/N PKLBST5011 applies. Engine flight cycles were 41200 at 2025-10-29 and 42650 at 2026-09-26, so 1450 cycles accrued over that interval, consistent with the hub's 1650 to 3100 cycles-since-new change.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row 4 (2A5001, PKLBST5011, 5,500 cycles)

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 engine is within the directive's model applicability, but neither installed hub (HPT 1st-stage hub P/N 2A5001 S/N PKLBST5012; HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0002) matches a P/N and S/N listed in Table 1 to paragraph (g), so no removal action is triggered on the recorded facts. The installation prohibition in paragraph (h) still binds.
- **Missing fact:** The recorded 1st-stage hub serial number PKLBST5012 differs from the listed PKLBST5011 by one character. If the recorded serial is a transcription error, the hub could match a listed entry (removal cycle limit 5,500, and the hub is at 4,200 cycles), so the serial should be verified against the hub's physical or traceability record.
- **Note:** The engine record has no events, so no engine shop visit history is recorded. This does not change the outcome because no installed hub matches Table 1, but the paragraph (g) trigger would need review if a listed hub were later found installed.
- **Note:** The FAA did not supersede or rescind this AD; the installation prohibition continues regardless of removal status.
- **Note:** This is a screening result, not a compliance determination.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2524-A5 is within the directive's applicability, and the directive is in force. The installed HPT 1st-stage hub shares the listed part number 2A5001 but its serial number is unknown, so whether the table 1 removal requirement applies cannot be determined. The installed HPT 2nd-stage hub serial SYN-HUB2-0003 is not listed in table 1.
- **Stated timing:** If the HPT 1st-stage hub serial matches a table 1 entry, removal is due at the next engine shop visit after 2025-10-29 before exceeding that hub's listed removal cycle limit, or within 100 flight cycles of 2025-10-29, whichever occurs later. No shop visit is recorded.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub (P/N 2A5001) is unknown. Table 1 lists four serial numbers for this part number, so the table requirement cannot be assessed until the serial is known.
- **Missing fact:** Cycles since new for the HPT 1st-stage hub are unknown. These are needed to compare against the table 1 removal limit if the serial matches a listed entry.
- **Missing fact:** The engine's current flight-cycle counter is not in the record. It is needed to compute the 100-flight-cycle deadline measured from the 2025-10-29 effective date and to determine the latest engine flight-cycle count for any required action.
- **Missing fact:** The event list is empty. The record does not show whether any engine shop visit has occurred since 2025-10-29, which is the trigger for removal under paragraph (g).
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003, 5100 cycles since new) does not match any serial in table 1, so no removal requirement is shown for it on this record. The table lists serials PKLBST5005, PKLBSS9840, PKLBSS0301 and PKLBSR2100.
- **Note:** The 1st-stage hub part number 2A5001 is listed, but the serial is unknown. It is not treated as a confirmed match.
- **Note:** Even if the 1st-stage serial matches, the table 1 limits are 100, 4,800, 5,500 and 6,200 cycles since new, and the record gives no cycles since new for that hub.
- **Note:** The AD has an installation prohibition (h) that applies regardless of the removal timing, so the installed serial should be checked before any future hub installation.
- **Note:** The NPRM 2025-10764 was superseded by the final rule 2025-18469 and is not cited as an operative requirement.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not an IAE V2500 model supported by this screen, so no applicability determination is made under Federal Register document 2025-18469.
- **Note:** Engine model PW1133G-JM is outside the supported V2500 model scope of this screen; no determination of applicability or compliance is made.
- **Note:** The engine record shows no installed components and no events.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527E-A5 engine is within the directive's model scope, and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSS9840) is listed in Table 1 with a 3,900-cycle removal limit. The operator-asserted shop visit on 2025-11-12 at 18,040 cycles triggers removal and replacement with an eligible hub, due by 18,100 engine flight cycles, and the installation prohibition in paragraph (h) applies to any future installation.
- **Stated timing:** Remove the listed HPT 2nd-stage hub and replace it with an eligible part at the engine shop visit (asserted on 2025-11-12) or within 100 flight cycles of the 2025-10-29 effective date, whichever is later, which is by 18,100 engine flight cycles.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The record gives 1,040 cycles since new without a date and a dated reading of 1,000 on 2025-10-29. The 1,040 value is treated as current, but its as-of date needs confirmation; it sets the 2,860 cycles remaining figure.
- **Missing fact:** The shop visit qualification is the operator's assertion. Confirming that the 2025-11-12 induction involved separation of major mating flanges is needed before the event is treated as the triggering next shop visit.
- **Missing fact:** No removal or replacement of the listed HPT 2nd-stage hub is recorded at or after the shop visit. Whether the removal was performed by 18,100 cycles cannot be confirmed from the record.
- **Missing fact:** The HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0005) does not match any Table 1 serial number, so no listed-part match was made. Its serial number should be confirmed against the table, and it has no recorded cycle limit comparison.
- **Note:** This is a screening aid only and does not determine compliance or airworthiness of the engine or parts.
- **Note:** The shop visit qualification and the 1,040 cycles-since-new value are operator-supplied and were not independently verified.
- **Note:** The 2,860 cycles remaining is computed from the 3,900-cycle limit minus 1,040 cycles since new; if the hub's cycle count is higher as of the event date, the figure would be lower.
- **Note:** The 60-cycle margin from the 18,040 snapshot to the 18,100 deadline is short; the record should be reviewed promptly.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSS9840, limit 3,900 cycles

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine is within the AD's applicability, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSK9287) is listed in Table 1 with a 100-cycle removal limit. The hub reads 90 cycles since new, so the removal action is required at the next engine shop visit before exceeding 100 cycles since new, or within 100 flight cycles of the 2025-10-29 effective date, whichever occurs later.
- **Stated timing:** Remove the listed HPT 1st-stage hub at the next engine shop visit before it exceeds 100 cycles since new, or within 100 flight cycles from the effective date (October 29, 2025), whichever occurs later; the 100-flight-cycle limit reaches engine flight cycle 25600.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** No engine shop visit is recorded, so it is unknown whether a shop visit has occurred or when the next one will occur. This determines when the removal must be performed under the shop-visit prong of paragraph (g).
- **Missing fact:** The 90-cycle value is undated; it is assumed to be current as of the 2025-11-20 snapshot, consistent with the 60-cycle reading on 2025-10-29 and 30 engine cycles elapsed. Confirm the current count, since the 10-cycle margin depends on it.
- **Note:** The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0006) is not listed in Table 1 (listed serials PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100), so no match is found for that hub on this record. This is not a finding that the part is unaffected, because the record for it is limited to the serial number and cycles.
- **Note:** The 2025-10764 NPRM is superseded for this screen by the final rule 2025-18469, which is the in-force text.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSK9287 limit 100 cycles

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (effective 2025-10-29) applies to this V2531-E5 engine. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is listed in Table 1 with a 4,800-cycle removal limit and is at about 4,300 cycles since new, so it must be removed at the next engine shop visit before the limit, or within 100 flight cycles of the effective date if that is later. The installation prohibition in paragraph (h) already applies to this engine.
- **Stated timing:** Remove and replace the HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) at the next engine shop visit after 2025-10-29 and before exceeding 4,800 cycles since new, or within 100 flight cycles of the effective date, whichever occurs later. No shop visit is recorded in the engine record.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** The engine record has an empty events list, so it does not show whether an engine shop visit (separation of major mating H-P flanges) has occurred or is scheduled. The timing of the required removal depends on this.
- **Missing fact:** Shop visit history since 2025-10-29 is unknown. A future shop visit would trigger the removal requirement before the cycle limit.
- **Note:** The HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 is listed in Table 1 with a 4,000-cycle limit. It is currently at 2,300 cycles since new, leaving 1,700 cycles, so it does not drive the deadline.
- **Note:** The cycle counts are consistent: engine cycles rose 300 and the 1st-stage hub cycles since new rose 300 between 2025-10-29 and 2025-12-01.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 row: HPT 1st-stage hub 2A5001 PKLBSS9200, limit 4,800

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a supported V2528-D5 with an installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) that is listed in Table 1 with a 6,200-cycle removal limit. The hub must be removed at the next engine shop visit before it exceeds 6,200 cycles since new, and the HPT 2nd-stage hub cannot be screened because its serial number and cycles are unknown.
- **Stated timing:** Remove the HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 6,200 cycles since new; projected at the current accrual rate, that limit falls near engine flight cycle 54,200.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub serial number is unknown, so it cannot be checked against the Table 1 P/N 2A4802 serial numbers and the screen cannot clear or confirm that hub.
- **Missing fact:** The HPT 2nd-stage hub cycles since new are unknown, so its position relative to its listed removal limit cannot be determined.
- **Missing fact:** The events list is empty. No engine shop visit is recorded, so it cannot be determined whether the next shop visit has occurred or whether the hub was already removed.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** Projected engine cycle of about 54,200 assumes the hub's cycles since new and the engine flight cycles accrue one-for-one from the 2026-03-10 snapshot (2,500 cycles since new at engine cycle 50,500); the cycles_since_new reading at 2025-10-29 (2,000) is consistent with that rate.
- **Note:** The installed hub's installed_at date is 2024-06-03; the cycles-since-new value of 2,500 is taken as the current value at the snapshot.
- **Note:** The HPT 2nd-stage hub's serial and cycles are unknown; a missing record is not evidence that it is unaffected, so that hub remains unscreened.
- **Note:** Only the HPT 1st-stage hub is matched to Table 1. The engine's current AD status is not in the record and is not inferred here.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBST7489, limit 6,200

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The directive is in force as of the question date (effective October 29, 2025) and the engine model V2522-A5 is a supported model within its applicability. However, the engine record lists no installed components and no events, so whether any HPT 1st-stage or 2nd-stage hub with a listed P/N and S/N is installed cannot be determined; the record's absence of components is not evidence that no affected hub is installed.
- **Missing fact:** No installed component record for the HPT 1st-stage hub is provided; whether an installed hub has P/N 2A5001 and a listed S/N cannot be checked.
- **Missing fact:** No installed component record for the HPT 2nd-stage hub is provided; whether an installed hub has P/N 2A4802 and a listed S/N cannot be checked.
- **Missing fact:** No engine event history is provided; whether a future engine shop visit occurs (which triggers the removal requirement) and the engine flight-cycle counter are unknown.
- **Missing fact:** The engine flight-cycle counter is not provided, so no cycle-based deadline or remaining-cycle figure can be computed.
- **Note:** This is a screening aid and not a compliance determination. The engine record is synthetic and contains no installed components, no events, and no ad_records or amoc_claims.
- **Note:** The installation prohibition in paragraph (h) applies to any engine regardless of shop visit timing and binds for the life of the engine.
- **Note:** If no installed hub matches a listed P/N and S/N, the required removal action would not be triggered on the current record, but that conclusion requires the hub records to be supplied.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model V2500-A1 is not on this screen's supported list of IAE V2500 models, so no applicability determination is made against AD 2025-19-13.
- **Note:** Engine model V2500-A1 is outside the supported model list, so the HPT 1st-stage hub part match (2A5001 / PKLBST5011, 5,500-cycle limit) was not evaluated for applicability.
- **Note:** Record is marked synthetic; no determination is made.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The engine is a supported V2527-A5 with a 3rd stage HPC rotor blade set recorded as P/N 6A8353, which is within the directive's applicability. The directive is in force, and its full-set blade replacement is triggered only at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed; no such event is recorded, so no deadline is computed.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed (exposure meaning any 3rd stage HPC rotor blade removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline applies otherwise.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** No engine shop visit events are recorded (events list is empty). Whether the engine has been or will be inducted into a shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed cannot be determined from the record.
- **Missing fact:** Blade serial numbers are not tracked at set level, so it cannot be confirmed whether each blade in the set is P/N 6A8353 or P/N 6A8688 or a modified part; this matters for applicability and for whether blades are already eligible for installation.
- **Note:** Screening aid only; not a compliance determination. The directive's effective date is 2026-09-24, which precedes the question date of 2026-10-05, so it is in force.
- **Note:** The operator's record contains no AD status entries and no AMOC claims; none were relied on.
- **Note:** The FR correction 2026-18423 fixes the word 'blade' in paragraph (g); the reading used here is the corrected text.
- **Note:** Installed P/N 6A8353 is a listed applicability part number; the record does not indicate whether the blades are modified to 6A8353-001, which would be an eligible part.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** AD 2026-17-03 (FR 2026-16954, effective 2026-09-24) applies to V2533-A5 engines with a 3rd stage HPC rotor blade having P/N 6A8353 or 6A8688 installed. The record lists the 3rd stage HPC rotor blade set as P/N 6C8368, which is a part eligible for installation under paragraph (h)(1), not an affected P/N, so the supplied facts place this engine outside the directive.
- **Missing fact:** The record gives only a set-level P/N of 6C8368 and says serial numbers are not tracked at set level. Confirmation that every 3rd stage HPC rotor blade in the set is P/N 6C8368 (or another eligible P/N) and none is 6A8353 or 6A8688 would be needed to rule out applicability.
- **Note:** This is a screening aid, not a compliance determination. The applicability conclusion rests on the set-level P/N in the record. If any blade in the set is 6A8353 or 6A8688, the engine would fall within applicability and the required action would apply at the next engine shop visit where the 3rd stage HPC rotor blade is exposed, with no shop visit recorded in the events list.
- **Note:** The record has no events, so no shop visit is recorded, and the paragraph (g) trigger has not occurred on the record provided.
- **Unresolved locator:** 2026-18423 (g) Correction of paragraph (g) wording

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (FR 2026-16954, effective 2026-09-24) applies to this V2530-A5 engine, which has 3rd stage HPC blade P/N 6A8688 installed. The record shows a shop visit inducted 2026-09-14, before the effective date, with a blade exposure on 2026-09-30; the AD's required action is tied to a shop visit after the effective date, so the outcome turns on whether this pre-effective-date visit counts, and that needs review.
- **Stated timing:** Replacement of the full set of 3rd stage HPC rotor blades is required at the next engine shop visit after 2026-09-24, 2026 where the 3rd stage HPC rotor blade is exposed. Whether the 2026-09-14 induction, with exposure on 2026-09-30, falls within that requirement needs review.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Engine flight-cycle counter at the time of the blade exposure and at the snapshot is not in the record, so no cycle-based deadline or remaining-cycle count can be computed.
- **Missing fact:** Whether the 2026-09-14 induction was a shop visit for the AD's purposes that was entered after 2026-09-24 in the operator's accounting, and whether the blade exposure on 2026-09-30 was part of that same visit, needs confirmation from the operator records.
- **Missing fact:** Blade serial numbers are not tracked at set level, so the set-level identity and the full-set replacement scope cannot be confirmed from the record.
- **Note:** This is a screening aid, not a compliance determination. The operator's qualifies_as_engine_shop_visit 'yes' for AD 2026-17-03 is an assertion and does not settle the timing question, which depends on the induction date relative to the 2026-09-24 effective date.
- **Note:** The AD effective date is 2026-09-24; the question date is 2026-09-30, so the directive is in force.
- **Note:** The correction document 2026-18423 only changes the word 'blade' in paragraph (g) and does not change the effective date or the applicability.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2026-17-03 applies to this V2524-A5 engine because its installed 3rd stage HPC rotor blade set is P/N 6A8353, which the directive lists, and the directive has been in force since 2026-09-24. The record shows a shop visit on 2026-10-01 but states that no 3rd stage blade was removed from the stage 3-8 drum, so the directive's defined blade exposure, which triggers replacement, is not shown; continuing obligations still apply.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** The blade set serial number is not tracked at set level, so the installed blades cannot be tied to individual serial numbers for review against the directive.
- **Missing fact:** Confirmation that no 3rd stage HPC rotor blade was removed from the stage 3-8 drum during the 2026-10-01 shop visit. The exposure event records only an inspection, but the defined term in (h)(2) depends on removal, so this should be confirmed in the maintenance records.
- **Missing fact:** The engine flight-cycle counter is not in the record. It is needed to state any cycle-based deadline if a future blade exposure at a shop visit occurs.
- **Note:** This is a screening aid, not a compliance determination. The directive's defined blade exposure, not the general word 'exposed', controls the trigger, so the record facts are read against paragraph (h)(2).
- **Note:** Future shop visits must be checked against (g) and (h)(2) on their own facts. A shop visit where any 3rd stage blade is removed from the stage 3-8 drum would trigger full-set replacement at that visit.
- **Note:** The 2026-10-01 visit was asserted by the operator to qualify as an engine shop visit under the AD definition. That assertion was not independently verified here.
- **Note:** The 2026-16954 Federal Register document is the final rule; the correction 2026-18423 fixes a typographical error in paragraph (g) and both are cited.
- **Unresolved locator:** 2026-18423 (g) Required Actions (corrected wording)

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** Federal Register document 2025-20088 is a proposed rule, not an in-force AD, so it cannot require action on this engine as of 2026-01-15. The V2527E-A5 is a listed model, and the recorded 3rd stage HPC rotor blade set P/N 6A8353 falls within the proposed applicability, but no blade exposure event is recorded.
- **Missing fact:** No event records are present. The proposed required action is triggered only at the next 3rd stage HPC rotor blade exposure after the effective date, so whether an exposure has occurred cannot be determined from the record.
- **Missing fact:** Blade serial numbers are recorded as not tracked at set level. Any individual-blade identification needed for later review is unavailable.
- **Missing fact:** No final rule or effective date for this directive appears in the supplied documents. The proposal's comment period closed 2026-01-02, and a final rule would be needed before any requirement applies.
- **Note:** This is a screening aid only and not a compliance determination. The engine record does not establish whether the directive is in force; it is a proposal as of the question date.
- **Note:** If the directive is later published as a final rule, the required action would apply at the next 3rd stage HPC rotor blade exposure, defined as removal of any 3rd stage HPC rotor blade from the HPC stage 3 to 8 drum. Reviewers should recheck the authority state and the event record at that time.
- **Unresolved locator:** 2025-20088 preamble DATES and Effective date (from the Federal Register record): none

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 is in force (effective October 10, 2025) and covers V2527-A5 engines, so this engine falls within its applicability. The operator's record states that neither its approved program nor TLM ALS paragraph B.1 yet incorporates table 1 to paragraph (g), so the paragraph (g)(1) and (g)(2) revisions are due on or before January 8, 2026.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e., on or before January 8, 2026, revise TLM ALS paragraph B.1 under (g)(1) and, for air carrier operations, the existing approved maintenance or inspection program under (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** No installed component records are supplied, so the presence of HPT Stage 1 hub P/N 2A5001 or HPT Stage 2 hub P/N 2A4802 cannot be confirmed. This does not change the (g) revision obligation, which applies to the operator's maintenance documents rather than to a specific part.
- **Missing fact:** The operator's statement that neither its approved program nor TLM paragraph B.1 incorporates table 1 is a claim to verify against the revised documents. Confirmation that the revisions are complete is needed before the (g) obligation can be shown as met.
- **Note:** Screening aid only; this output is not a compliance determination.
- **Note:** The NPRM 2024-26092 was superseded by the final rule and is not relied on for the deadline.
- **Note:** The deadline is calendar-based (90 days from October 10, 2025), so no flight-cycle deadline is computed.
- **Note:** Because no installed components or events are recorded, no component-level cycle limit can be computed.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive is in force as of the question date (effective October 10, 2025) and the engine model V2522-A5 is within its applicability, but the record lists no installed components and no events, and the operator's air carrier status is unknown, so no action can be confirmed or excluded for the HPT 1st-stage and 2nd-stage hubs.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e., by January 8, 2026, for the paragraph (g)(1) ALS revision; paragraph (g)(2) applies to air carrier operations within the same period.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** No installed component records are present, so it cannot be determined whether HPT Stage 1 Hub P/N 2A5001 or HPT Stage 2 Hub P/N 2A4802 is installed; an empty list is not evidence that these parts are absent.
- **Missing fact:** Whether the operator is an air carrier operation is unknown, which determines whether paragraph (g)(2) applies to revising the existing approved maintenance or inspection program.
- **Missing fact:** Whether the operator's ICA/Time Limits Manual ALS paragraph B.1 has already been revised for the listed tasks is not recorded.
- **Missing fact:** No shop visit or piece-part exposure events are recorded, so the timing of the inspection tasks at piece-part exposure cannot be assessed.
- **Note:** The engine serial number SYN-V2500-0017 is synthetic. This is a screening aid, not a compliance determination.
- **Note:** The directive requires a one-time ALS/program revision, not a specific inspection interval; the tasks are performed at piece-part exposure per the Maintenance Scheduling section.
- **Note:** The 2024 NPRM (2024-26092) is superseded by the final rule and was not used for obligations.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is a listed model, and its installed HPT 2nd-stage hub (2A4802, S/N PKLBSR2100) is listed in Table 1 with a 6,000-cycle removal limit and 990 cycles since new, leaving 5,010 cycles. The final rule is not effective until 2025-10-29, so no action is required on the question date; once effective, removal is due at the next engine shop visit before exceeding 6,000 cycles or within 100 flight cycles of the effective date, whichever is later.
- **Stated timing:** Not yet in force on 2025-10-15. Once effective on 2025-10-29, remove the listed hub at the next engine shop visit before exceeding 6,000 cycles since new, or within 100 flight cycles from the effective date, whichever occurs later.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine flight-cycle counter at or near the effective date (2025-10-29) is not in the record, so the 100-flight-cycle alternative deadline cannot be computed.
- **Missing fact:** The events list is empty, so there is no record of whether any engine shop visit has occurred or is planned, which determines when the removal obligation would attach.
- **Missing fact:** The HPT 1st-stage hub serial number SYN-HUB1-0018 is not in Table 1 on its face, so it appears unaffected; confirm the serial number record is accurate before relying on that.
- **Note:** Authority state is published_not_yet_effective, so the directive cannot require action on the question date; the screen reports the obligation that will apply once effective.
- **Note:** The 2025-10764 NPRM is superseded by the final rule for this screen and is not relied on.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub, 2A4802, PKLBSR2100, 6000

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-18469 applies to this V2531-E5 engine. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in Table 1 with a 4,800-cycle removal limit, and its recorded cycles since new (4,990, and 4,950 at 2025-10-29) already exceed that limit, so removal and replacement is required within 100 flight cycles of the 2025-10-29 effective date, by engine cycle 60100.
- **Stated timing:** Remove and replace the listed HPT 1st-stage hub at the next engine shop visit before exceeding its limit or within 100 flight cycles of the 2025-10-29 effective date, whichever occurs later. The shop-visit prong cannot be met because the limit is already exceeded, so the operative deadline is 100 flight cycles after the effective date (engine cycle 60100).
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The undated cycles_since_new value (4,990) conflicts with the dated reading of 4,950 at 2025-10-29. The current value on 2025-11-05 is needed to confirm the exact overage, though the limit is exceeded on either reading.
- **Missing fact:** The events list is empty, so no engine shop visit history is recorded. Any shop visit since 2025-10-29 would bear on whether the next-shop-visit prong applies, though the 100-cycle prong governs here.
- **Note:** This is a screening aid, not a compliance determination. The record shows no evidence that the engine or hub is compliant or noncompliant.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0019) does not match any Table 1 entry, so no 2nd-stage match is recorded from the supplied facts.
- **Note:** The engine-cycle reading at 2025-10-29 was 60,000, so 100 flight cycles after the effective date gives 60,100; the 2025-11-05 reading is 60,040, leaving 60 cycles.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200, limit 4,800 cycles since new

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (Federal Register document 2021-11960) is in force on the question date, and the V2533-A5 is a supported model with HPT 1st- and 2nd-stage disks whose part numbers match the directive. Applicability cannot be confirmed because the serial numbers are not shown to appear in the directive's Appendix A tables, and no engine flight-cycle counter is recorded.
- **Stated timing:** For the HPT 1st-stage disk (g)(1) and the HPT 2nd-stage disk (g)(2), the USI is due at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first. Engine shop visit status for the record is not yet established, and no shop visit events are recorded.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015) is not supplied, so it cannot be confirmed whether serial number SYN-DISK1-0020 is listed for the HPT 1st-stage disk. This determines whether paragraph (c)(1) and (g)(1) apply.
- **Missing fact:** Appendix A, Table 2 of the same service information is not supplied, so it cannot be confirmed whether serial number SYN-DISK2-0020 is listed for the HPT 2nd-stage disk. This determines whether paragraph (c)(2) and (g)(2) apply.
- **Missing fact:** The engine flight-cycle counter is not recorded. It is needed to measure the 3,200-cycle limit counted from July 13, 2021 and to compute latest_engine_flight_cycles.
- **Missing fact:** Confirmation is needed of the disk's flight cycles accumulated since July 13, 2021, and of its operating history, which affects the compliance threshold.
- **Missing fact:** Confirmation is needed of the disk's flight cycles accumulated since July 13, 2021, and of its operating history, which affects the compliance threshold.
- **Missing fact:** No engine shop visit history is recorded. Whether a shop visit has occurred since July 13, 2021 determines whether the earlier shop-visit trigger has already passed.
- **Note:** Document 2021-11960 is in force on 2022-03-01. Document 2022-02574 supersedes it, but that document is effective March 15, 2022, so it does not yet control. A reviewer should recheck the superseding AD's compliance times, including the Figure 1 compliance time and the 10-flight-cycle alternative, once it takes effect.
- **Note:** The engine record shows no installed-part serial number cross-check against the directive's Appendix A tables, and the synthetic serials are not known to be listed. This screen makes no compliance determination.
- **Note:** The screen is not an AD status record for the operator.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** Engine model V2533-A5 is in scope and both installed disks carry the listed part numbers (2A5001 and 2A4802), but AD 2022-02-09 applies only if each disk's serial number appears in the Appendix A tables, which were not supplied. The directive also takes effect March 15, 2022, after the 2022-03-01 question date, so it cannot require action yet.
- **Stated timing:** If the disks are listed and the directive is in force, the USI is due within the Figure 1 compliance time to paragraph (g)(1) or within 10 flight cycles after the effective date, whichever is later; Figure 1 is not in the supplied text.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015 Rev 1) is not supplied, so it cannot be confirmed whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015 Rev 1) is not supplied, so it cannot be confirmed whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed.
- **Missing fact:** No operating history is recorded for the disk. Whether it has operated on a high-thrust model engine (V2527E, V2527M, V2528, V2530, V2533) determines the compliance time under the superseding AD.
- **Missing fact:** No operating history is recorded for the disk. Whether it has operated on a high-thrust model engine determines the compliance time under the superseding AD.
- **Missing fact:** Figure 1 to paragraph (g)(1) is an image not included in the text, so the compliance time cannot be computed even if the disks are listed.
- **Missing fact:** The event list is empty. No engine shop visit or cycle history is recorded, so the engine's flight-cycle counter and any shop-visit trigger cannot be determined.
- **Note:** Screening aid only, not a compliance determination. Nothing here states that the engine or any part is compliant or noncompliant.
- **Note:** AD 2021-11-15 (Federal Register document 2021-11960) is the directive this AD supersedes and was in force on the question date. It is outside this screen but may still bind the operator until March 15, 2022.
- **Note:** The engine record contains no ad_records or amoc_claims, so no operator AD status claim was evaluated.
- **Note:** The HPT 2nd-stage disk and 1st-stage disk serial numbers are synthetic identifiers; no Appendix A listing could be verified from the supplied text.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 is in force and covers V2530-A5 engines with listed HPT 1st-stage (P/N 2A5001) or 2nd-stage (P/N 2A4802) disks. The record's part numbers match, but applicability turns on whether the installed serial numbers appear in the NMSB Appendix A tables, which were not supplied, and the compliance time depends on Figure 1, which is not in the text provided.
- **Stated timing:** Paragraph (g)(1) and (g)(2) require the USI at the next engine shop visit or within the Figure 1 compliance time, or within 10 flight cycles after March 15, 2022, whichever occurs later. Figure 1 was not supplied, so the due point cannot be computed from the text.
- **Missing fact:** Whether HPT 1st-stage disk S/N SYN-DISK1-0021 is listed in Appendix A, Table 1, of NMSB V2500-ENG-72-0713 Rev 1 or NMSB V2500-E5-72-0015 Rev 1; applicability under paragraph (c)(1) depends on this.
- **Missing fact:** Whether HPT 2nd-stage disk S/N SYN-DISK2-0021 is listed in Appendix A, Table 2, of the same NMSB revisions; applicability under paragraph (c)(2) depends on this.
- **Missing fact:** Figure 1 to paragraph (g)(1) compliance-time table, which was not included in the supplied text, so the flight-cycle or shop-visit deadline cannot be determined.
- **Missing fact:** Confirmation of the installed 1st-stage disk serial number against the NMSB Appendix A list; the record shows SYN-DISK1-0021.
- **Missing fact:** Confirmation of the installed 2nd-stage disk serial number against the NMSB Appendix A list; the record shows SYN-DISK2-0021.
- **Missing fact:** Operating history of the 1st-stage disk, including whether it has operated on a high-thrust model engine (V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2533-A5), and its flight cycles since the effective date; needed for the compliance-time reading in paragraph (g)(3).
- **Missing fact:** Operating history of the 2nd-stage disk, including prior high-thrust engine operation and flight cycles since the effective date.
- **Missing fact:** The events list is empty, so no engine shop visit history is recorded; whether the next shop visit has occurred since 2022-03-15 cannot be determined.
- **Note:** This is a screening aid only and does not determine compliance or airworthiness.
- **Note:** The engine is a V2530-A5, which is a supported model. The installed part numbers match the listed part numbers, but serial-number listing in Appendix A is not confirmed, so no matched_parts entries are recorded.
- **Note:** Figure 1 and Appendix A were not supplied in the text. Figure 2 to paragraph (g)(3)(i) was also not supplied, though it applies to V2522/V2524/V2525/V2527 engines rather than this model.
- **Note:** The record is synthetic and the events list is empty; the engine's operating and shop-visit history must be checked before any deadline can be set.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine has an HPT 1st-stage disk P/N 2A5001 with S/N PKLBSH1829, which is listed in paragraph (c)(1), so the directive applies. A USI of that disk is required within 10 flight cycles after the July 19, 2021 effective date, which computes to engine flight cycle 33010; the engine is at 33004 as of the question date.
- **Stated timing:** Perform the ultrasonic inspection of the HPT 1st-stage disk within 10 flight cycles after July 19, 2021, i.e. by engine flight cycle 33010, using paragraph 6 of IAE NMSB V2500-ENG-72-0713 Rev 1.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** No event or record shows whether the required USI of the HPT 1st-stage disk has already been performed. Whether it was done, and at what cycle, determines whether the 10-cycle deadline still applies.
- **Missing fact:** The engine cycle reading at the effective date is recorded as 33000. The deadline depends on this value being accurate for the effective date.
- **Note:** The directive is in force as of the question date (effective July 19, 2021), and V2533-A5 is a supported model.
- **Note:** The installed HPT 2nd-stage disk (P/N 2A4802, S/N SYN-DISK2-0022) is not among the listed S/N values in paragraph (c)(2), so it does not match on the record as given. The record serial is synthetic, so this should be confirmed against the actual disk.
- **Note:** This screen is not a compliance determination. The 10-cycle deadline of 33010 is computed from the recorded cycle readings and must be verified against the operator's actual engine cycle count.
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
- **Summary:** The V2533-A5 is a supported model and AD 2021-11-15 was in force on 2021-07-20, but applicability turns on whether the installed HPT 1st-stage disk (2A5001, S/N PKLBSH1829) and HPT 2nd-stage disk (2A4802, S/N SYN-DISK2-0022) appear in the Appendix A serial-number tables of the referenced NMSBs, which are not in the record. If they do, the disks would face an inspection at the next engine shop visit or within 3,200 FCs of the effective date, whichever comes first.
- **Stated timing:** If the serial numbers are confirmed in the Appendix A tables: the USI of each disk is due at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first (paragraphs (g)(1) and (g)(2)).
- **Missing fact:** The engine flight-cycle count on the effective date (2021-07-13) is not recorded, so the 3,200-FC limit measured from the effective date cannot be converted to an engine flight-cycle deadline. The only readings are 33000 on 2021-07-19 and 33004 on 2021-07-20.
- **Missing fact:** Appendix A, Table 1 of NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015) is needed to confirm whether HPT 1st-stage disk S/N PKLBSH1829 is listed. Its absence means applicability cannot be decided.
- **Missing fact:** Appendix A, Table 2 of NMSB V2500-ENG-72-0713 Rev 1 (or NMSB V2500-E5-72-0015) is needed to confirm whether HPT 2nd-stage disk S/N SYN-DISK2-0022 is listed.
- **Missing fact:** The event list is empty. No engine shop visit is recorded, so it cannot be established whether a shop visit has occurred since the effective date. The operator must confirm its shop-visit history since 2021-07-13.
- **Note:** The directive's effective date (2021-07-13) precedes the question date, so it is in force. The screen does not state compliance status.
- **Note:** The engine record has no AD status or AMOC entries for AD 2021-11-15, so no operator claim is evaluated.
- **Note:** The 3,200-FC limit runs from the effective date, not from installation. Cycles accumulated before 2021-07-13 do not count toward it.
- **Note:** Paragraph (g)(1) and (g)(2) apply only to the V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, and V2533-A5 models, so the V2533-A5 is covered by both.
- **Note:** The matched_parts entries match on part number only. Listed serial numbers are null because the Appendix A tables were not supplied.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a listed V2527M-A5 and its installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in Table 1 with a 6,000-cycle removal limit. The hub must be removed and replaced at the next engine shop visit before it exceeds 6,000 cycles since new (about 25,000 engine cycles on the record), and no shop visit is recorded yet.
- **Stated timing:** At the next engine shop visit after the 2025-10-29 effective date and before the hub exceeds 6,000 cycles since new, or within 100 flight cycles of the effective date if that is later.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The only dated hub cycle reading is 1000 on 2025-10-29. The undated 3500 value is assumed to be current. The remaining-cycle figure depends on it.
- **Missing fact:** Engine shop visit history since 2025-10-29 is not recorded. Whether a qualifying shop visit has already occurred, which would have triggered removal, is unknown.
- **Missing fact:** The recorded revision cites AD 2025-17-16, a different AD number. It does not show removal of the listed hub under AD 2025-19-13 and is not evidence of compliance with this AD.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0023 does not appear in Table 1, so it is not matched to this AD. Its serial number is not listed, so it does not trigger removal under this AD.
- **Note:** The 3rd stage HPC rotor blade set is not addressed by this AD.
- **Note:** Deadline arithmetic assumes the hub accrues cycles at the engine rate: 2500 cycles from 22500 yields 25000. The hub's own count would reach 6,000 at the same engine count if it has flown with the engine since installation.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSR2100, limit 6,000 cycles

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The engine model is supported and the record lists a 3rd stage HPC rotor blade set with P/N 6A8688, which is within the directive's applicability. The directive requires full-set replacement of the 3rd stage HPC rotor blades at the next engine shop visit after 2026-09-24 where the blade is exposed; no such shop visit is recorded, so no fixed deadline is computed.
- **Stated timing:** At the next engine shop visit after the effective date of September 24, 2026 where the 3rd stage HPC rotor blade is exposed (exposure meaning removal from the HPC stage 3 to 8 drum). No calendar or cycle deadline applies otherwise.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Whether any engine shop visit (induction into the shop for maintenance) has occurred on or after 2026-09-24. The record contains no shop visit events, so it cannot be confirmed whether the blade exposure trigger has occurred.
- **Missing fact:** The serial number is recorded as not tracked at set level. Individual blade traceability is not needed to establish applicability, but it matters for confirming the set of blades to be replaced at a future exposure.
- **Missing fact:** No operator AD status record for AD 2026-17-03 is present, so the operator's own recorded status cannot be checked against this screen.
- **Note:** The directive is in force as of 2026-10-06 because its effective date is 2026-09-24. A later correction (2026-18423) fixed a typographical omission of 'blade' in paragraph (g) without changing the requirement.
- **Note:** The engine cycle readings show 22500 flight cycles on 2026-10-06. No flight-cycle deadline applies because the trigger is a shop visit event, not a cycle count.
- **Note:** The operator's maintenance program revision (Revision 48, 2025-12-01) incorporates AD 2025-17-16 table 1, which is a different AD. It is not evidence of compliance with AD 2026-17-03 and was not used to settle this screen.
- **Note:** The 'HPT 1st-stage hub' and 'HPT 2nd-stage hub' components are not listed in the directive and were not matched.
- **Note:** This is a screening aid and not a compliance determination; it does not state that the engine is compliant or noncompliant.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 (Federal Register 2025-17066, effective 2025-10-10) applies to V2527M-A5 engines, and the record shows the approved program and V2500-A5 TLM ALS were revised on 2025-12-01, inside the 90-day window that ended about 2026-01-08, so no new action is triggered now. The hub piece-part inspections remain binding at piece-part exposure.
- **Stated timing:** The ALS and approved program revision was due within 90 days after 2025-10-10 (by about 2026-01-08). The record shows it was done 2025-12-01. The hub inspections apply at each piece-part exposure.
- **Missing fact:** The event detail does not confirm that the revision was made to paragraph B.1 of the Maintenance Scheduling section of the ALS in the applicable TLM, with the correct TLM P/N (2A4408 for V2500-A5), as paragraph (g)(1) requires. Confirming this is needed to close the (g)(1) obligation.
- **Missing fact:** The operator record states Revision 48 incorporates table 1, but it does not confirm that the revision covered both the TLM ALS and the air carrier approved maintenance or inspection program under paragraph (g)(2), or that the revision date falls within the compliance window.
- **Missing fact:** The HPT 2nd-stage hub has conflicting cycles-since-new values (3500 at the installation record and 1000 at 2025-10-29). This does not change the AD's requirements, which are piece-part inspections with no cycle limit, but the record should be reconciled.
- **Missing fact:** No dated reading is given for the HPT 1st-stage hub cycles since new. The AD sets no cycle limit, so this does not change the screen, but it is needed for any component-life review.
- **Missing fact:** The content of TASK 72-45-11-200-006 and TASK 72-45-31-200-009 and the TLM B.1 paragraph is not in the supplied documents. Their inspection thresholds are not known from the material given.
- **Note:** This is a screening aid, not a compliance determination. The record shows an operator-asserted program revision dated 2025-12-01, which falls inside the window; the operator's status claim is not verified against source documents.
- **Note:** The engine is at 22500 cycles on 2026-10-06. No AD cycle limit is stated, so no cycle-based deadline is computed.
- **Note:** The preamble notes that the SIAEC 20,000-cycle replacement reference is outside the AD text and is not used here.
- **Note:** The record does not show any piece-part exposure event, so the hub inspections are not triggered on the record as given.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2528-D5 is within the directive's applicability and the directive is in force. Neither installed hub's part number and serial number pair matches a row in Table 1 to paragraph (g), so no removal is triggered on the current record, but the installation prohibition in paragraph (h) still binds.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The 2nd-stage hub record shows P/N 2A4802 with S/N PKLBST5011. That serial appears in Table 1 only against P/N 2A5001 (1st-stage hub), so the pair does not match a listed 2nd-stage entry. Reviewers should verify the recorded part number and serial number against the physical part documentation.
- **Note:** The directive applies by P/N and S/N pair, so a serial-only match is not treated as a match here.
- **Note:** The engine record has no events, so no engine shop visit is recorded. Any future shop visit would need review under paragraph (g) and definition (i)(2).
- **Note:** The 1st-stage hub serial SYN-HUB1-0024 is synthetic and is not listed in Table 1.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model recorded is a CFM56-5B4/3, which is not among the IAE V2500 models supported by this screen, so no applicability determination is made under Federal Register document 2025-17066.
- **Note:** The engine record lists model CFM56-5B4/3 with serial SYN-CFM56-0025; this is outside the supported V2500 model scope, so no applicability or compliance conclusion is drawn.
- **Note:** The directive is in force as of its effective date of October 10, 2025.
- **Note:** installed_components and events are empty; no component or event data was evaluated.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine has an installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489, which is listed in Table 1 with a 6,200 cycles-since-new removal limit. The hub is at 3,600 cycles since new, so it must be removed and replaced at the next engine shop visit before it exceeds 6,200 cycles, which is about 23,200 engine flight cycles on the current accumulation rate.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29 and before the hub exceeds 6,200 cycles since new. The alternative 100-flight-cycle window from the effective date ended at about engine cycle 20,100 with no removal recorded.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** Whether an engine shop visit has occurred or is scheduled after 2025-10-29. None is recorded, so the removal deadline depends on the next shop visit date, which is not known.
- **Missing fact:** The hub cycles-since-new reading on the snapshot date is not separately recorded (only 3,600 as the current value and 3,000 at 2025-10-29). Remaining cycles assume one-for-one accumulation with engine cycles since 2025-10-29, which matched the record.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0026 is not in Table 1, so no 2nd-stage match is found; this is not a determination about that part's status.
- **Note:** The 2024 blend repair and 2024 inspection of the listed hub predate the effective date and do not change the Table 1 removal limit.
- **Note:** This is a screening aid only and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), row HPT 1st-stage hub, 2A5001, PKLBST7489, limit 6,200

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
- **Summary:** The V2527-A5 engine is within the directive's applicability, and its installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is listed in table 1 with a 4,800-cycle removal limit. The hub is at 4,750 cycles since new, so it must be removed at the next engine shop visit before exceeding 4,800 cycles, with the 100-flight-cycle clock from the 2025-10-29 effective date running to 15,100 engine cycles, which has already passed; the later of the two deadlines gives 15,300 engine cycles.
- **Stated timing:** Remove and replace the listed HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before the hub exceeds 4,800 cycles since new, or within 100 flight cycles of the effective date, whichever occurs later. On the record, that is by engine flight cycle 15,300; the 100-cycle date (15,100) is already exceeded at 15,250 cycles.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** No engine shop visit event is recorded. Whether and when the next shop visit occurs determines when the removal must be performed, and the record cannot show whether it is before the hub exceeds 4,800 cycles.
- **Missing fact:** The operator's AMOC note cites a 5,300-cycle removal limit, but no FAA approval letter is on file (approval_reference unknown). The AMOC cannot be relied on, so the 4,800-cycle limit in table 1 is used.
- **Note:** Screening aid only; this is not a compliance determination. The HPT 2nd-stage hub S/N SYN-HUB2-0027 is not listed in table 1 and does not match. The record shows the hub at 4,500 cycles since new on 2025-10-29 and 4,750 on 2026-01-20, consistent with the 250 engine cycles flown in that period.
- **Note:** The directive's 100-cycle language is ambiguous; the primary reading gives 15,300 and the alternative gives 15,100 (already passed).
- **Unresolved locator:** 2025-18469 (g) Table 1 row: HPT 1st-stage hub, 2A5001, PKLBSS9200, limit 4,800 cycles

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (effective 2025-10-29) applies to this V2524-A5 engine. The installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) is listed in Table 1 with a 4,000-cycle removal limit, and the hub's 1,400 cycles since new leaves 2,600 cycles before that limit, so removal is required at the next engine shop visit before the limit or within 100 flight cycles of the effective date, whichever is later. The operator's 'not_applicable' record conflicts with the installed hub and should be reviewed.
- **Stated timing:** Remove the listed HPT 2nd-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 4,000 cycles since new, or within 100 flight cycles of 2025-10-29, whichever occurs later. On the engine record's cycle readings, the later date is reached at about engine flight cycle 11,000; the 100-cycle window closed at about engine flight cycle 8,100 and the engine is already at 8,400.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** No engine shop visit events are recorded. Whether an engine shop visit has occurred since 2025-10-29, which would have triggered the removal, cannot be confirmed from the record.
- **Missing fact:** The operator's recorded status is not_applicable with the note 'no affected hubs installed', but the installed HPT 2nd-stage hub matches a Table 1 listing. The basis for the note needs to be reviewed against the installed component record.
- **Missing fact:** The HPT 1st-stage hub serial number SYN-HUB1-0028 does not match any Table 1 serial number for P/N 2A5001 on the face of the record. Confirming its serial number against the Table 1 list would settle whether this hub is also affected.
- **Note:** Hub cycles since new were 1,000 at engine cycle 8,000 (2025-10-29) and 1,400 at engine cycle 8,400 (2026-02-10), so the hub accrues one cycle per engine flight cycle in this record. This projection gives the 11,000 date.
- **Note:** The HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0028) does not match any listed serial number, so it is not matched on the face of the record.
- **Note:** This screen is not a compliance determination. The operator's not_applicable entry is a claim to check and does not settle the outcome.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBST5005, removal cycle limit 4,000

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is a listed model, and the installed HPT 1st-stage hub (S/N PKLBSK9287) matches a Table 1 row with a 100-cycle removal limit. The hub shows 2400 cycles since new, so it is already past that limit. Under paragraph (g), removal is due at the next engine shop visit or within 100 flight cycles of the 2025-10-29 effective date, whichever is later; the engine's cycle count on that date is not in the record, so no flight-cycle deadline can be computed.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after 2025-10-29 or within 100 flight cycles of 2025-10-29, whichever occurs later. The record shows no shop visit since the effective date.
- **Missing fact:** Installed P/N is recorded as 2A5001-01 while Table 1 lists 2A5001. The suffix must be confirmed as the same part number before the match is final.
- **Missing fact:** The engine flight-cycle counter on the 2025-10-29 effective date is not recorded. It is needed to compute the 100-flight-cycle deadline.
- **Missing fact:** No engine shop visit history is recorded. Whether a shop visit has occurred or is scheduled determines the earlier trigger for removal.
- **Missing fact:** The installed HPT 2nd-stage hub S/N SYN-HUB2-0029 does not appear in Table 1, but the record does not confirm that the hub was checked against the full Table 1 list for the 2A4802 part number.
- **Note:** This is a screening aid, not a compliance determination. The hub is recorded at 2400 cycles since new against a 100-cycle limit, so it is past its listed limit. Because the paragraph (g) deadline is the later of two triggers, the flight-cycle deadline depends on the engine cycle count at the effective date, which is missing.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0029) is not listed in Table 1 and is not matched.
- **Note:** The operator's record contains no AD status or AMOC claims for this directive.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row for S/N PKLBSK9287 (removal cycle limit 100)

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
