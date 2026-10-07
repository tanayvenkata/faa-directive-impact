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
- **Summary:** The V2527-A5 is within the applicability, and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in Table 1 (5,500 cycles-since-new limit). Removal and replacement is required at the next engine shop visit, which must occur before the hub exceeds 5,500 cycles since new. No shop visit is recorded.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before the hub exceeds 5,500 cycles since new (engine flight cycle 45050 on the record's counts). The 100-flight-cycle alternative ended at engine flight cycle 41300, which is earlier, and the text uses the later of the two.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** No engine shop visit is recorded since 2025-10-29. Any future shop visit must be checked against the AD's engine shop visit definition, since it triggers the removal.
- **Missing fact:** The 2nd-stage hub S/N SYN-HUB2-0001 is a synthetic placeholder. Confirm the actual S/N against Table 1; it does not match any listed S/N as recorded.
- **Note:** Cycles since new at the effective date were 1650 (engine 41200), so the 5,500 limit falls at engine cycle 45050. This matches the current 3100 cycles since new at engine cycle 42650, which leaves 2400 cycles.
- **Note:** The record's ad_records and amoc_claims are empty, so no operator claims were checked.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 is a listed model, so the AD applies. Neither installed hub has a P/N and S/N pair listed in table 1 (the 1st-stage hub S/N PKLBST5012 differs from listed PKLBST5011), so the paragraph (g) removal is not triggered; the installation prohibition and other continuing obligations still bind.
- **Note:** This is a screening aid only, not a compliance determination.
- **Note:** The 1st-stage hub serial PKLBST5012 is one character off listed PKLBST5011; the record's serial should be verified against the hub's data plate and records to rule out a transcription error.
- **Note:** The 2nd-stage hub serial SYN-HUB2-0002 is not in table 1.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2524-A5 is within the AD applicability and the AD is in force. The HPT 1st-stage hub P/N 2A5001 is installed with an unknown serial number and unknown cycles, so it cannot be matched to Table 1; the 2nd-stage hub serial is not listed.
- **Missing fact:** Serial number of the installed HPT 1st-stage hub (P/N 2A5001) is unknown; needed to determine whether it is one of the four listed S/Ns in Table 1 and so whether paragraph (g) applies.
- **Missing fact:** Cycles since new of the 1st-stage hub is unknown; needed to compare against the removal cycle limit if the S/N is listed.
- **Missing fact:** No shop visit events are recorded, so the next engine shop visit timing cannot be established.
- **Note:** HPT 2nd-stage hub S/N SYN-HUB2-0003 does not appear in Table 1, so it is not an affected part on the supplied facts.
- **Note:** Unknown serial is not evidence the 1st-stage hub is unaffected; the serial must be verified from records or the part.
- **Note:** If the 1st-stage hub S/N is found to be listed, the action would be tied to the next engine shop visit and the applicable cycle limit or 100 flight cycles after the effective date, whichever is later.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for this directive.
- **Note:** No determination is made on whether this directive applies to this engine model.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The AD is in force and the engine model is covered. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed with a 3,900-cycle removal limit and is at 1,040 cycles since new. The 11-12-2025 shop visit induction is recorded as qualifying, so removal and replacement falls due at that visit, and the 100-cycle-from-effective-date window is also open.
- **Stated timing:** Paragraph (g) says to act at the next engine shop visit after the effective date, before exceeding the removal cycle limit or within 100 flight cycles after the effective date, whichever occurs later. The cycle limit (3,900) is far from reached, so the later date governs. On the effective-date reading, the 100-cycle window ends at engine flight cycle 18,100 (18,000+100). The shop visit began at cycle 18,040 and is the next shop visit, so the hub is due to be removed at this visit, and no later than cycle 18,100 on that reading.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The operator asserts the induction is an engine shop visit under the AD definition. The flange separation and the exclusions in (i)(2) (transport only; field maintenance in lieu of on-wing) should be confirmed, since this affects whether the shop-visit trigger has occurred.
- **Missing fact:** The 1st-stage hub serial SYN-HUB1-0005 is not in table 1, so no match. It is not an affected part on the supplied data.
- **Note:** The 2nd-stage hub's cycles since new were 1,000 at 2025-10-29 and 1,040 now, which is consistent with engine cycles of 18,000 to 18,040.
- **Note:** Remaining cycles = 3,900 - 1,040 = 2,860.
- **Note:** The 1st-stage hub serial is not listed, so that hub is not an affected part on the supplied data.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and the engine model is covered. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287 is listed in Table 1 with a 100 cycles-since-new limit, so removal and replacement is required at the next engine shop visit, no earlier than 100 flight cycles after the effective date.
- **Stated timing:** At the next engine shop visit after 2025-10-29, but not before the later of reaching the 100 cycles-since-new limit or 100 flight cycles after the effective date. 'Whichever occurs later' means the deadline is the later of the two; here that is 100 flight cycles after the effective date (engine cycle 25,600). No shop visit is recorded, so no deadline has been triggered by an event.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** No engine shop visit is recorded. The next shop visit that meets the AD's definition triggers the removal, so whether and when one occurs must be tracked.
- **Missing fact:** The 2nd-stage hub S/N SYN-HUB2-0006 is not in Table 1, so it does not match. The P/N 2A4802 matches a listed part number, but the serial number is not listed.
- **Missing fact:** The hub's cycles since new is 90 in the snapshot, but its readings show 60 at 2025-10-29, which is inconsistent with the engine's 30 cycles since then. The current value should be confirmed against the engine counter.
- **Note:** The hub's recorded 90 cycles since new is below the 100 limit, leaving 10 cycles; the limit would be reached at about engine cycle 25,540.
- **Note:** The hub was installed on 2025-09-30, which is before the effective date, so the installation prohibition in (h) is not shown as breached. The installation date was before the AD took effect.
- **Note:** The 100 flight cycles from the effective date count from engine cycle 25,500, giving 25,600; 30 cycles have elapsed as of 2025-11-20.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, row PKLBSK9287, limit 100

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a listed model and carries two hubs matching Table 1 (1st-stage S/N PKLBSS9200, 2nd-stage S/N PKLBST5005). Removal is tied to the next engine shop visit, which has not occurred (events empty), so action is required on that event; the latest-of-limit-or-100-cycles rule applies at that visit.
- **Stated timing:** At the next engine shop visit after 2025-10-29, at or after the later of reaching the removal cycle limit (4,800 CSN for the 1st-stage hub; 4,000 CSN for the 2nd-stage hub) or 100 flight cycles after the effective date (engine counter 30,100). No deadline applies unless a shop visit occurs. Replacement parts must not be Table 1 parts.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Note:** Smallest remaining cycles: 1st-stage hub 4,800 - 4,300 = 500 cycles; 2nd-stage hub 4,000 - 2,300 = 1,700 cycles. Cycle counts are as of 2025-12-01.
- **Note:** No events are recorded, so no shop visit has occurred. If one occurs, the hubs would be removed at that visit since 100 cycles after the effective date (engine counter 30,100) has already passed, and the visit would occur before either hub reaches its limit, the later-of condition being the 100-cycle point already elapsed versus the cycle limit; the reviewer should confirm the reading of 'whichever occurs later' with the FAA.
- **Note:** The hubs have not yet reached their removal cycle limits, so the required action is not triggered until a shop visit occurs, and under the 'later' reading may not be due until the limits are reached; the text is ambiguous on this point and should be reviewed.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows PKLBSS9200 and PKLBST5005

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 is within the applicability and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1 (limit 6,200 cycles since new). Removal is required at the next engine shop visit, which has not occurred; no deadline applies until then. The HPT 2nd-stage hub serial number is unknown, so its status cannot be settled.
- **Stated timing:** At the next engine shop visit after 2025-10-29, at or after the later of reaching the 6,200 cycles-since-new limit or 100 flight cycles after the effective date. The later-of reading puts the 1st-stage hub removal at the first shop visit once the hub has passed 6,200 cycles since new; no shop visit is recorded yet.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub serial number is unknown, so it cannot be compared to the table 1 listed 2A4802 serial numbers; a match would add a removal obligation.
- **Missing fact:** Cycles since new of the 2nd-stage hub are unknown, needed to apply the removal cycle limit if its serial number is listed.
- **Note:** The 1st-stage hub has 2,500 cycles since new at 2026-03-10 (2,000 at 2025-10-29), so 3,700 cycles remain before the 6,200 limit.
- **Note:** No engine shop visit is recorded in events, so the shop-visit trigger has not occurred on this record.
- **Note:** Because the hub is far below its limit, the 'whichever occurs later' wording means removal is not due at a shop visit before the hub reaches 6,200 cycles since new, apart from the 100-cycle floor; this interpretation should be reviewed.
- **Note:** The engine flight-cycle deadline cannot be computed because it depends on a future shop visit.

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2522-A5 is within the AD's applicability and the AD is in force, but the record lists no installed HPT 1st-stage or 2nd-stage hub, so whether a Table 1 part is installed cannot be determined. The paragraph (g) action depends on that fact.
- **Missing fact:** No record of the installed HPT 1st-stage hub P/N, S/N and cycles since new; needed to check against Table 1 (P/N 2A5001). An empty record is not evidence the part is absent or unaffected.
- **Missing fact:** No record of the installed HPT 2nd-stage hub P/N, S/N and cycles since new; needed to check against Table 1 (P/N 2A4802). An empty record is not evidence the part is absent or unaffected.
- **Missing fact:** No event history, so engine shop visits since the effective date (October 29, 2025) and flight cycles since then cannot be established for the paragraph (g) timing.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule 2025-18469 and was not relied on for authority.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made.
- **Note:** The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 appears in the AD table, but no part matching or timing analysis was done because the engine model is outside supported scope.
- **Note:** AD 2025-19-13 was effective 2025-10-29 and is in force on the question date.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force as of 2026-10-05. Replacement of the full blade set is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no deadline otherwise.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** The record shows no events, so no shop visit after the effective date is recorded; this does not show that none has occurred. A shop visit that began before 2026-09-24 does not trigger paragraph (g).
- **Note:** The correction document 2026-18423 fixed a typo in (g) (omitted 'blade'); the substance is unchanged, and the effective date remains September 24, 2026.
- **Note:** Serial numbers are not tracked at set level; the AD lists the part number only, so this does not affect the match.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The V2533-A5 is a supported model, but the record shows the 3rd stage HPC rotor blade set at P/N 6C8368, which is not an affected P/N (6A8353 or 6A8688), so the engine is outside the applicability of paragraph (c). The AD was in force on the question date (effective 2026-09-24).
- **Missing fact:** The record gives one part number for the blade set and no serial numbers at set level. If any individual blade installed is actually P/N 6A8353 or 6A8688 (a mixed set), the engine would fall within applicability, so the individual blade part numbers should be confirmed.
- **Note:** The record shows no events and no shop visit, so no action would be triggered even if the engine were within applicability.
- **Note:** Screening aid only; not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC blade set P/N 6A8688, so AD 2026-17-03 applies and is in force on 2026-09-30. The shop visit was inducted 2026-09-14, before the 2026-09-24 effective date, and paragraph (g) covers only visits after the effective date, so the replacement is not triggered by this visit.
- **Stated timing:** No deadline now. Replacement is required at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed (removed from the stage 3-8 drum).
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Note:** The blade exposure on 2026-09-30 occurred after the effective date but during a visit inducted before it. Under the (g) wording (shop visit after the effective date) and the FAA's stated intent, this visit does not trigger the requirement.
- **Note:** The correction document 2026-18423 changes only the wording of paragraph (g), not the substance or effective date.
- **Note:** Because the blades are exposed now, the operator may wish to confirm which blade P/N is installed at reassembly. If the set is replaced with eligible parts during this visit, the (g) requirement would be met by that replacement. This screen does not determine compliance status.
- **Note:** The record shows no AMOC claims or AD records for this AD.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force on 2026-10-05 (effective 2026-09-24). The 2026-10-01 shop visit was inducted after the effective date, but the record shows no 3rd-stage blade was removed from the drum, so on the AD's definition of exposure the replacement is not yet triggered and is due at the next qualifying shop visit.
- **Stated timing:** At the next engine shop visit (induction for maintenance) after 2026-09-24 in which a 3rd stage HPC rotor blade is exposed (removed from the stage 3-8 drum); no deadline otherwise.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** Confirmation that no 3rd stage HPC rotor blade was removed from the stage 3-8 drum during the 2026-10-01 to 2026-10-04 visit. The record says only that the rotor was exposed for inspection with no blade removed. If any blade was removed, paragraph (g) was triggered at that visit and the full-set replacement would be required by then.
- **Note:** The question names document 2026-16954, but its paragraph (g) says 'the 3rd stage HPC rotor is exposed'. Correction 2026-18423 fixes this to 'rotor blade'. Under the original wording, HPC rotor exposure for inspection on 2026-10-02 might arguably trigger replacement, which would make the action due at that visit. The corrected text was used here because it is the controlling published text.
- **Note:** The rotor exposure on 2026-10-02 does not meet the (h)(2) blade-exposure definition on the record as given.
- **Note:** The shop visit induction (2026-10-01) was after the effective date, so the visit is not excluded by the exception for visits inducted before it.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527E-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so it is within the proposed applicability. The document is only an NPRM and not in force on 2026-01-15, so no action is required now.
- **Stated timing:** If adopted as proposed, replacement would be due at the next 3rd stage HPC rotor blade exposure after the final rule's effective date. No deadline applies now.
- **Note:** Comment period closed January 2, 2026; a final rule may change the requirements.
- **Note:** The record shows no events, so no blade exposure has been recorded. Under proposed (h)(2), exposure means any 3rd stage blade removed from the HPC stage 3 to 8 drum.
- **Note:** The record does not indicate whether the blades are already a part eligible for installation. P/N 6A8353 as installed is a listed affected P/N; a -001 modification would change the P/N.
- **Note:** This screening aid is not a compliance determination.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a V2527-A5, within the applicability of AD 2025-17-16, which is in force as of 2025-11-15 (effective 2025-10-10). The record shows neither the TLM ALS paragraph B.1 nor the approved maintenance program yet incorporates table 1, so the paragraph (g) revisions are required within 90 days after the effective date, by 2026-01-08.
- **Stated timing:** Within 90 days after the effective date of October 10, 2025, i.e., by January 8, 2026, for both the (g)(1) TLM ALS revision and the (g)(2) air carrier maintenance/inspection program revision.
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Note:** The action is a documentation revision, not tied to part presence or cycles, so the empty installed_components list does not affect the outcome.
- **Note:** The record says the operator is an air carrier, so both (g)(1) and (g)(2) apply. The 90-day count from October 10, 2025 ends January 8, 2026.
- **Note:** The 2024 NPRM (2024-26092) is superseded by the final rule; the final rule's table references Task 72-45-31-200-009 for the Stage 2 hub.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is a listed model, so AD 2025-17-16 applies and is in force on the question date. The ALS/TLM revision in (g)(1) was due within 90 days after 2025-10-10, i.e. by 2026-01-08; whether (g)(2) also applies depends on air carrier status, which is unknown.
- **Stated timing:** Paragraph (g)(1): within 90 days after the October 10, 2025 effective date, i.e. by January 8, 2026. Paragraph (g)(2), if air carrier operations: same 90-day period.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the engine is used in air carrier operations is unknown; this determines whether the (g)(2) revision of the approved maintenance or inspection program is also required.
- **Missing fact:** The record gives no evidence whether the (g)(1) TLM/ALS revision (and (g)(2), if applicable) has already been done; this is not recorded, so it is not established.
- **Note:** Applicability is by engine model only, so the empty installed_components list does not affect applicability; the AD does not depend on the hubs being installed.
- **Note:** The final rule 2025-17066 supersedes the proposal 2024-26092 for this screen; the proposal corrected task 72-45-11-200-009 to 72-45-31-200-009 in the final rule.
- **Note:** The 90-day date is computed from the effective date and has no engine flight-cycle limit. This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is within the applicability of AD 2025-19-13, and its installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1. The AD is published but not effective until 2025-10-29, so no action is required on the question date; removal is tied to a future engine shop visit.
- **Stated timing:** Not yet effective (effective 2025-10-29). Once effective, remove and replace the hub at the next engine shop visit after 2025-10-29 that occurs at or after the later of: the hub exceeding its 6,000 cycles-since-new removal limit, or 100 flight cycles after the effective date. No deadline applies absent such a shop visit.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** Current engine flight-cycle count is not in the record, so the 100-cycles-after-effective-date point cannot be converted to an engine cycle counter value.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0018 is not listed in table 1 and is not matched.
- **Note:** The hub has 990 cycles since new against a 6,000 limit, leaving 5,010 cycles; with the limit far off, the 100-cycles-after-effective-date condition would likely be the later one.
- **Note:** The record shows no events, so no shop visit has occurred; a shop visit before 2025-10-29 would not count as it must be after the effective date.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The AD is in force and the engine model is covered. The installed HPT 1st-stage hub 2A5001 S/N PKLBSS9200 matches table 1 (limit 4,800 cycles since new) and is already past that limit. Removal is due at the next engine shop visit, and no later than 100 flight cycles after the effective date only if that is the later of the two conditions.
- **Stated timing:** Paragraph (g) requires removal at the next engine shop visit after 2025-10-29, before exceeding the removal cycle limit or within 100 flight cycles after the effective date, whichever occurs later. The limit was already exceeded, so the 100-cycle point (engine flight cycles 60100) is the later one. No shop visit is recorded yet. The text can be read two ways: the 100-cycle point may be a hard deadline, or removal may wait for the next shop visit. Under the first reading, the engine must not fly past 60100 cycles without a shop visit.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The HPT 2nd-stage hub serial number SYN-HUB2-0019 is not listed in table 1, so it does not match. This is not a missing fact, but confirm that the record serial number is accurate.
- **Missing fact:** No shop visits are recorded. Whether a future event qualifies as an engine shop visit under paragraph (i)(2) is needed to determine when removal is triggered.
- **Note:** Hub cycles since new were 4,950 at 2025-10-29 and 4,990 at 2025-11-05, which is 190 over the 4,800 limit (-190). The 40 engine cycles flown match the 40 hub cycles added.
- **Note:** The 2nd-stage hub serial SYN-HUB2-0019 is not in table 1, and a non-listed serial is not affected by paragraph (g). Its part-number match alone does not trigger action.
- **Note:** The NPRM 2025-10764 is superseded by the final rule and was not relied on.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, row PKLBSS9200, 4,800 cycles

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (2021-11960) was in force on 2022-03-01, and the V2533-A5 is a listed model with disks of the listed part numbers. Applicability turns on whether the disk serial numbers appear in the NMSB Appendix A tables, which were not supplied. Separately, AD 2022-02-09 (2022-02574) supersedes this AD effective 2022-03-15, so the superseding AD will replace it two weeks after the question date.
- **Stated timing:** If the serial numbers are listed: at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. The cycles accumulated since 2021-07-13 are not in the record.
- **Missing fact:** Content of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1, to check whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed. Without it, applicability under (c)(1) cannot be decided.
- **Missing fact:** Content of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, to check whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed. Without it, applicability under (c)(2) cannot be decided.
- **Missing fact:** Flight cycles accumulated by the HPT 1st-stage disk since 2021-07-13 are needed to compute the 3,200-cycle limit.
- **Missing fact:** Flight cycles accumulated by the HPT 2nd-stage disk since 2021-07-13 are needed to compute the 3,200-cycle limit.
- **Missing fact:** The events list is empty. It is not confirmed whether any engine shop visit has occurred since 2021-07-13, which would trigger the inspection. Neither is it confirmed whether any USI has been done.
- **Note:** The serial numbers are synthetic and cannot be checked against the real NMSB tables.
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** From 2022-03-15 the requirements are in AD 2022-02-09, which uses Figure 1 compliance times that were not provided as text, and adds a 10-FC minimum after 2022-03-15.
- **Note:** No ad_records or amoc_claims are present in the record.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2021-11960 (g)(1) V2533-A5 high-thrust group

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2533-A5 is a supported model with P/N 2A5001 and 2A4802 disks installed, but the serial numbers cannot be checked against the NMSB Appendix A tables, which were not supplied. AD 2022-02-09 is not effective until 2022-03-15, so on 2022-03-01 it cannot yet require action.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not supplied, so S/N SYN-DISK1-0020 cannot be checked against it. A match would make (c)(1) apply.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not supplied, so S/N SYN-DISK2-0020 cannot be checked against it. A match would make (c)(2) apply.
- **Missing fact:** Figure 1 to paragraph (g)(1), the compliance-time table, is an image that was not included, so no deadline can be computed.
- **Missing fact:** The disk's accumulated flight cycles and the engine's current cycle count are not in the record. They would be needed to apply the Figure 1 threshold.
- **Note:** Part numbers match the AD's listed P/Ns (2A5001 and 2A4802), but the serial numbers are not confirmed against the Appendix A tables, so no part is recorded as matched.
- **Note:** The AD supersedes AD 2021-11-15, which was in force on the question date. It has different compliance language, but it is not the directive asked about.
- **Note:** The record has no events, so no shop visit or other event information is available.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The engine model V2530-A5 is supported and both installed disk part numbers (2A5001, 2A4802) match the AD's listed part numbers. Applicability cannot be decided because the AD limits it to serial numbers in the NMSB Appendix A tables, which were not supplied, and the Figure 1 compliance times are in an image that was not included.
- **Missing fact:** Contents of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 to confirm whether HPT 1st-stage disk S/N SYN-DISK1-0021 is listed; needed to decide applicability.
- **Missing fact:** Contents of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 to confirm whether HPT 2nd-stage disk S/N SYN-DISK2-0021 is listed; needed to decide applicability.
- **Missing fact:** Figure 1 to paragraph (g)(1) (image not provided) giving the compliance time for high-thrust engines; needed to compute any deadline.
- **Missing fact:** Flight cycles accumulated by the HPT 1st-stage disk; needed to apply the Figure 1 threshold if the disk is listed.
- **Missing fact:** Flight cycles accumulated by the HPT 2nd-stage disk; needed to apply the Figure 1 threshold if the disk is listed.
- **Missing fact:** No record of whether the USI was already done or credited; the record has no AD status or inspection history.
- **Note:** The engine record contains no flight-cycle counters, no AD records, and no events.
- **Note:** The superseded AD 2021-11-15 (document 2021-11960) is no longer the operative directive.
- **Note:** This is a screening aid only, not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a V2533-A5 with an HPT 1st-stage disk P/N 2A5001 S/N PKLBSH1829, which is listed in paragraph (c)(1), so the AD applies. A USI of the 1st-stage disk is required within 10 flight cycles after the 2021-07-19 effective date.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021. The engine counter was 33000 on 2021-07-19, so the deadline is engine flight cycle 33010. At 33004 on 2021-07-20, 6 cycles remain.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** Whether the USI has already been done, or whether an AMOC applies, is not shown. The record has no ad_records or amoc_claims for this AD.
- **Missing fact:** Tables 1 and 2 of paragraphs (g)(1) and (g)(2) are images not supplied in the text. Whether the 1st-stage disk is in Table 1 cannot be confirmed from them. Applicability itself rests on the (c)(1) serial list.
- **Note:** The 2nd-stage disk S/N SYN-DISK2-0022 is not among the serials listed in (c)(2), so it does not trigger (g)(2). The engine is covered through the 1st-stage disk.
- **Note:** The deadline is computed from the 2021-07-19 reading of 33000 cycles, plus 10.
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
- **Summary:** The V2533-A5 is a supported model and the AD is in force (effective 2021-07-13), but applicability depends on whether the installed disk serial numbers appear in the Appendix A tables of the NMSB, which were not supplied. The part numbers match the AD (2A5001 and 2A4802), but the serial numbers cannot be checked.
- **Stated timing:** If either disk S/N is listed: USI at the next engine shop visit after 2021-07-13 or before that disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first.
- **Missing fact:** Content of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided; needed to determine whether HPT 1st-stage disk S/N PKLBSH1829 is listed.
- **Missing fact:** Content of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided; needed to determine whether HPT 2nd-stage disk S/N SYN-DISK2-0022 is listed.
- **Missing fact:** The disks' flight cycles accumulated since 2021-07-13 are not in the record. The engine cycle reading on 2021-07-13 is also absent, so the 3,200-cycle deadline cannot be converted to an engine cycle count.
- **Missing fact:** Engine flight-cycle reading on the effective date (2021-07-13) is missing, so the 3,200-FC limit cannot be converted to an engine counter value. It is also unconfirmed that the disks have been in the engine since that date.
- **Note:** The record has no events, so no engine shop visit since 2021-07-13 is shown. Absence of events is not proof that none occurred.
- **Note:** Engine flight cycles were 33,004 on 2021-07-20, but the 2021-07-13 reading is missing, so the deadline cannot be computed.
- **Note:** If the disks are listed, the 3,200-FC limit runs from 2021-07-13, not from total disk life.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and applies to the V2527M-A5 model. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 matches table 1 (limit 6,000 cycles since new), so replacement is required at the next engine shop visit, with no fixed deadline absent that event.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 6,000 cycles-since-new limit or within 100 flight cycles after the effective date, whichever occurs later. No shop visit is recorded, so no fixed calendar deadline can be computed.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The hub's cycles-since-new readings conflict: 3,500 is shown as current, but a reading of 1,000 is dated 2025-10-29 while the engine accrued 2,500 cycles after that date. The current 3,500 is used for the remaining-cycles figure, but the hub's actual cycles should be confirmed.
- **Missing fact:** No engine shop visit after 2025-10-29 is recorded, so it is not known whether the action trigger has occurred. If one occurred, the hub would have to be removed then, because a hub that remains installed at that shop visit still has to be replaced under the whichever-occurs-later wording once cycles are within the limit.
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0023 is not listed in table 1, so it is not matched.
- **Note:** The maintenance program revision cites AD 2025-17-16, a different AD from the one in question (2025-19-13). It is not evidence that this AD's requirements have been addressed.
- **Note:** Component cycles remaining is 6,000 minus 3,500 = 2,500 using the current record value. If the 2025-10-29 reading of 1,000 plus 2,500 accrued cycles (3,500) is right, the figures agree.
- **Note:** The 3rd stage HPC rotor blade set is not listed in this AD.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (document 2026-16954, as corrected by 2026-18423) is in force on the question date and applies: the V2527M-A5 engine has a 3rd stage HPC rotor blade set with P/N 6A8688 installed. Replacement with eligible parts is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no deadline applies until then.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum). No calendar or cycle deadline applies.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record shows no engine shop visit or blade exposure after 2026-09-24, so none is shown to have triggered the replacement. Any future shop visit that exposes the blades would trigger it.
- **Missing fact:** Blade serials are not tracked at set level, so individual blade P/Ns and any prior modification to an eligible P/N (6A8688-001) cannot be confirmed. The set is recorded as P/N 6A8688, which is an affected P/N.
- **Note:** The operator record contains no AD record or AMOC claim for AD 2026-17-03. The only entries concern AD 2025-17-16, which is a different directive and has no bearing on this screen.
- **Note:** The HPT hub records are unrelated to this AD and were not used.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527M-A5 is a listed model, and AD 2025-17-16 was in force on 2026-10-06 (effective 2025-10-10). The only required action is the one-time ALS and maintenance program revision. The record shows that revision made on 2025-12-01, within 90 days of the effective date, so no further action is triggered by this screen.
- **Stated timing:** The revision was due within 90 days after 2025-10-10, i.e. by 2026-01-08. The record shows it was made on 2025-12-01. Nothing further is due now.
- **Missing fact:** The revision content was not supplied. The record states table 1 was incorporated, but the revised TLM paragraph B.1 and the program text were not seen, so it cannot be confirmed that they match table 1 (TASK 72-45-11-200-006 and TASK 72-45-31-200-009).
- **Missing fact:** The record shows only the V2500-A5 TLM (P/N 2A4408) was revised. That is the TLM for this A5 model, so no other TLM is expected to be needed.
- **Note:** The record's revision date of 2025-12-01 is before the 2026-01-08 deadline. This is a screening observation, not a compliance determination.
- **Note:** The AD requires only the revision, not performing the inspection tasks directly. Per the final rule preamble, the tasks apply at piece-part exposure.
- **Note:** The HPT hub cycle counts (3500 since new) are not relevant to a deadline under this AD, so no component cycle remaining figure is computed.
- **Note:** The 3rd stage HPC rotor blade set is not listed in this AD and was not matched.
- **Note:** The record's cycles_since_new readings for the HPT 2nd-stage hub (1000 at 2025-10-29 against 3500 now) are inconsistent with the engine cycle readings (2500 cycles flown since). The inconsistency does not affect this screen.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is within the AD applicability, and the AD is in force on 2026-10-06. No installed part matches table 1 on both P/N and S/N, so no removal is triggered; the 2nd-stage hub S/N PKLBST5011 is listed only as a 1st-stage hub with a different P/N (2A5001).
- **Note:** S/N PKLBST5011 appears in table 1 only against P/N 2A5001 (HPT 1st-stage hub, 5,500 cycle limit). The installed 2nd-stage hub is P/N 2A4802, so it is not a match; the record should be checked for a possible data-entry error in the serial number or part number.
- **Note:** No matched parts, so no cycle limit applies and the remaining-cycles figure is not computed.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model CFM56-5B4/3 is not one of the supported IAE V2500 models, so no applicability determination is made for AD 2025-17-16.
- **Note:** The directive's authority state on the question date (2026-10-06) is in_force, since the effective date was 2025-10-10, but no applicability determination is made for this engine model.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is covered and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1 (limit 6,200 cycles since new). The AD is in force; removal and replacement is due at the next engine shop visit, which has not occurred, and no deadline is established until then.
- **Stated timing:** At the next engine shop visit after October 29, 2025, at the later of reaching the 6,200 cycles-since-new removal limit or 100 flight cycles after the effective date. Because the shop-visit trigger is a future event, no date is fixed. The 100-flight-cycle point after the effective date is engine counter 20,100, already passed. The hub reaches 6,200 cycles at about engine counter 23,200 on the 2026-03-01 reading.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** No engine shop visit since 2025-10-29 is recorded, and no event has a qualifies_as_engine_shop_visit determination. The record does not show whether a shop visit occurred or when the next one will. This determines when removal is triggered.
- **Missing fact:** The 2nd-stage hub S/N SYN-HUB2-0026 is not listed in table 1, so it was not matched. Please confirm the serial number is the actual one; it looks like a placeholder.
- **Note:** Cycles since new: 3,600 at 2026-03-01 (the 2025-10-29 reading was 3,000, and the engine accrued 600 cycles since, which is consistent). Remaining to 6,200 is 2,600.
- **Note:** The 2024 blend repair and repeat ultrasonic inspection with no indications do not remove the hub from table 1; the AD has no exception for them. No AMOC is claimed.
- **Note:** Whether any past maintenance qualified as an engine shop visit is not recorded after the effective date, so no removal is currently triggered on the record.

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
- **Summary:** The engine model is covered and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches Table 1 (limit 4,800 CSN). Removal is due at the next engine shop visit, and no shop visit has occurred. The cycle limit alone does not fix a deadline.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding 4,800 CSN or within 100 flight cycles after the effective date, whichever occurs later. The 100-cycle window after the effective date has already passed (engine cycles 15,000 to 15,100). Because the hub is now at 4,750 CSN, the 4,800 CSN limit has not been reached. No shop visit is recorded, so the action is event-driven and no fixed deadline can be computed.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The planning note claims an AMOC extending the limit to 5,300 CSN, but no FAA approval reference or letter is on file. An unapproved claim cannot be relied on to change the 4,800 CSN limit under paragraph (j).
- **Missing fact:** Current hub CSN is 4,750 on the snapshot, while the 2025-10-29 reading was 4,500 and engine cycles rose 250 since then. These are consistent, but the hub CSN at the time of any future shop visit must be confirmed against the 4,800 limit.
- **Missing fact:** The 2nd-stage hub S/N SYN-HUB2-0027 does not match any Table 1 serial number, so no match is made. Confirm that the record S/N is the actual stamped S/N.
- **Note:** The record has no events, so no engine shop visit is shown. The action is triggered at the next one.
- **Note:** The hub is 50 cycles below the 4,800 CSN limit. If a shop visit occurs after the hub passes 4,800 CSN, removal applies at that visit because the 100-cycle window has already passed.
- **Note:** The claimed 5,300 CSN AMOC is unverified and was not applied.
- **Note:** The 2nd-stage hub is not matched to Table 1 on the supplied S/N.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is listed and the installed HPT 2nd-stage hub 2A4802 S/N PKLBST5005 matches Table 1 (limit 4,000 cycles since new). Removal is tied to the next engine shop visit after 2025-10-29, and no shop visit is recorded, so no deadline is fixed now.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 4,000 cycles-since-new limit or within 100 flight cycles after the effective date, whichever occurs later. No qualifying shop visit is recorded, so action is due when one occurs. Because the hub is only at 1,400 cycles, the 'whichever occurs later' wording means the later date is controlling.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0028 is not in Table 1, so it does not match. The record shows no conflict, but the hub identity should be confirmed against the physical part.
- **Missing fact:** No engine shop visit is recorded. Any future shop visit must be checked against the paragraph (i)(2) definition to see whether it triggers removal.
- **Note:** The operator record marks the AD 'not applicable: no affected hubs installed'. This conflicts with the record: hub PKLBST5005 is listed in Table 1, and the AD applies to the engine model regardless of hub. That claim does not settle the outcome.
- **Note:** The 2nd-stage hub's cycles-since-new is 1,400 at 2026-02-10 (1,000 at 2025-10-29), so 2,600 cycles remain to the 4,000 limit.
- **Note:** The installed_at date of 2025-06-03 precedes the AD effective date, so the hub was installed before the AD; the installation prohibition is not triggered by that installation.
- **Note:** The earlier NPRM 2025-10764 is superseded by the final rule.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is a listed model and the AD is in force. The HPT 1st-stage hub S/N PKLBSK9287 matches table 1, but the installed P/N is 2A5001-01 versus listed 2A5001, so the match needs review. If it is the listed part, its 100-cycle limit is already exceeded, and removal is due at the next engine shop visit. The 2nd-stage hub S/N is not listed.
- **Stated timing:** If the 1st-stage hub is an affected part: at the next engine shop visit after October 29, 2025, since the 100-cycle removal limit has already passed (the later-of 100 flight cycles from the effective date is also applicable). The count of cycles since the effective date is not in the record.
- **Missing fact:** Installed P/N is 2A5001-01, while table 1 lists 2A5001 for S/N PKLBSK9287. Confirm whether the -01 dash number is the same part as the listed P/N; this decides whether the hub is affected.
- **Missing fact:** No events are recorded. The record shows no engine shop visit after October 29, 2025, so it cannot be confirmed whether a qualifying shop visit has occurred or when the next one will be.
- **Missing fact:** Engine flight cycles accrued since the effective date (October 29, 2025) are not given, so the 100-flight-cycle point from the effective date cannot be computed.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0029 is not in table 1 and was not matched.
- **Note:** Component cycles remaining is 100 minus 2400, which is -2300, assuming the 1st-stage hub is the listed part.
- **Note:** The record has no AD record or AMOC claim for this AD.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
