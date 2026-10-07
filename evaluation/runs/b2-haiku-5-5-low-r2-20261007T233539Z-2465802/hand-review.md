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
- **Summary:** Engine model V2527-A5 is within the directive's applicability, and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in Table 1 with a 5,500-cycle removal limit. Using the record's 3,100 cycles since new as of 2026-09-26, about 2,400 cycles remain, so the hub must be removed at the next engine shop visit before it exceeds 5,500 cycles since new, which is about engine cycle 45,050. This is a screening result, not a compliance determination.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after the 2025-10-29 effective date and before it exceeds 5,500 cycles since new (about engine flight cycle 45,050). The 'within 100 flight cycles of the effective date' clause, which would have ended about engine cycle 41,300, has already passed, so the later shop-visit deadline governs under the directive's 'whichever occurs later' wording.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** No engine events are recorded, so there is no shop visit on record. Whether a future induction will be an engine shop visit under paragraph (i)(2), and so trigger removal, cannot be determined from the record.
- **Missing fact:** The 3,100 cycles-since-new figure is undated. It matches the 1,650 reading at 2025-10-29 plus 1,450 engine cycles elapsed, but a dated current reading would confirm the remaining-cycle figure of 2,400.
- **Note:** The installed HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0001 does not match any Table 1 serial (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100), so it is not identified as an affected part on this record. It has no dated cycles-since-new reading.
- **Note:** The engine record shows 1,450 engine cycles between 2025-10-29 and 2026-09-26 (41,200 to 42,650), consistent with the hub's cycles since new rising from 1,650 to 3,100 over the same period.
- **Note:** The directive's installation prohibition in paragraph (h) applies to any future installation of listed hubs, regardless of shop visit timing.
- **Note:** This screen does not determine compliance, airworthiness, or return-to-service status.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBST5011, limit 5,500

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2533-A5 is within the directive's applicability, and the directive is in force. Neither installed hub matches a P/N and S/N listed in Table 1 to paragraph (g), so no removal action is triggered on these facts, though the installation prohibition and continuing obligations still bind.
- **Missing fact:** The installed HPT 1st-stage hub serial number PKLBST5012 is close to the listed serial PKLBST5011 (P/N 2A5001, 5,500-cycle limit) but is not identical. The non-match depends on this recorded serial being correct, so it should be verified against the hub's physical data plate or pedigree documents.
- **Missing fact:** The installed HPT 2nd-stage hub serial SYN-HUB2-0002 is not in Table 1. The non-match depends on the recorded serial being accurate; no verification source is in the record.
- **Note:** The engine's installed hub cycles since new (4,200) are not relevant to a deadline because neither hub is a listed P/N and S/N.
- **Note:** The events list is empty, so no shop visit history is recorded; this does not change the outcome because no listed part is installed.
- **Note:** This screen is not a compliance determination.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 is a listed model and the AD is in force (effective 2025-10-29), so the AD applies. The installed HPT 2nd-stage hub (S/N SYN-HUB2-0003) is not in Table 1, but the HPT 1st-stage hub has a listed P/N (2A5001) with an unknown serial number and unknown cycles, so whether it is an affected part cannot be determined.
- **Stated timing:** Remove any listed HPT 1st-stage or 2nd-stage hub at the next engine shop visit after 2025-10-29, before exceeding its Table 1 removal cycle limit, or within 100 flight cycles from 2025-10-29, whichever occurs later. No engine shop visit is recorded. The installation prohibition applies now to any listed hub.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub (P/N 2A5001) is unknown. Table 1 lists specific serial numbers for this P/N, so the hub cannot be confirmed as listed or not listed.
- **Missing fact:** Cycles since new for the HPT 1st-stage hub are unknown. These are needed to compare against the Table 1 removal cycle limit if the serial number matches a listed hub.
- **Missing fact:** No engine flight-cycle counter is in the record, so the 100-flight-cycle window from the effective date cannot be converted to a cycle number.
- **Missing fact:** No events are recorded, so no engine shop visit date is known. The timing of the required action depends on the next engine shop visit.
- **Note:** This is a screening aid, not a compliance determination. The record does not establish whether any installed hub is an affected part.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) does not match any Table 1 entry, so its 5100 cycles do not bear on the table limits.
- **Note:** If the 1st-stage hub serial matches a Table 1 entry, its removal limit would need to be compared with the 5100-cycle figure only if that figure applied to it; the record gives no cycles for the 1st-stage hub.
- **Note:** The record is synthetic (SYN- identifiers).

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the IAE V2500 models supported by this screen, so no applicability determination is made under Federal Register document 2025-18469.
- **Note:** The engine record lists model PW1133G-JM with serial number SYN-PW1100-0004, a Pratt & Whitney PW1100G-series model outside the supported V2500 scope.
- **Note:** No installed components or events are recorded; no determination was made on those points because the engine is outside scope.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (effective 2025-10-29) applies to this V2527E-A5 engine. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed in Table 1 with a 3,900-cycle removal limit and is at 1040 cycles since new, so it must be removed and replaced at the next engine shop visit after the effective date, or within 100 flight cycles of the effective date if later. The 2025-11-12 shop visit qualifies per the operator record, and the record does not show whether the hub was removed at it.
- **Stated timing:** At the next engine shop visit after 2025-10-29 (the 2025-11-12 induction, which the operator record says qualifies), before the 3,900-cycle limit is exceeded or within 100 flight cycles of the effective date, whichever is later.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The record does not say whether the affected HPT 2nd-stage hub (2A4802 / PKLBSS9840) was removed and replaced during the 2025-11-12 shop visit. Whether the hub is still installed determines whether the required action has been done.
- **Missing fact:** The HPT 1st-stage hub S/N SYN-HUB1-0005 is not in Table 1, so it does not match a listed part. The record does not confirm the hub's installed_at date, which is not needed for this match but would help confirm the installation history.
- **Note:** Screening aid only, not a compliance determination. Hub cycles since new are 1040 on 2025-11-12 (1000 on 2025-10-29), consistent with 40 engine cycles elapsed between 18000 and 18040.
- **Note:** The 100-cycle window is measured from the effective date, when the engine was at 18000 cycles, giving 18100. The 3,900-cycle limit is not the controlling constraint for this hub.
- **Note:** The shop visit qualification is the operator's own assertion and is not verified here.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine is a listed model, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSK9287) is in Table 1 with a 100-cycle removal limit, so removal at the next engine shop visit or within 100 flight cycles of the 2025-10-29 effective date (whichever is later) is required. The HPT 2nd-stage hub (S/N SYN-HUB2-0006) does not match any listed serial number.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after 2025-10-29 before exceeding 100 cycles since new, or within 100 flight cycles of 2025-10-29, whichever occurs later. No shop visit is recorded; the 100-flight-cycle limit is engine cycle 25600.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** The record gives 90 cycles since new with no date, yet a dated reading of 60 cycles since new at 2025-10-29 is also recorded. Cycles since new should not decrease, and the 2025-09-30 installation date is inconsistent with both values. The current value controls the cycles-remaining figure, so this must be confirmed.
- **Missing fact:** No engine shop visit is recorded. Whether a shop visit is planned before the hub exceeds its limit affects the timing reading.
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** The 2025-10-29 engine cycle reading (25500) is used as the effective-date cycle count.
- **Note:** The directive is in force as of the question date, since its effective date of 2025-10-29 has passed.

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine is within the directive's scope, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in Table 1 with a 4,800-cycle removal limit. The hub has about 500 cycles remaining; removal is required at the next engine shop visit before that limit, or within 100 cycles of the effective date, whichever is later, and no removal is recorded.
- **Stated timing:** Remove the HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 4,800 cycles since new (about engine cycle 30,800), or within 100 flight cycles of the 2025-10-29 effective date (by engine cycle 30,100), whichever occurs later. The 100-cycle window has already passed with no removal recorded.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** No engine events are recorded. Whether a shop visit has occurred since 2025-10-29, and whether the hub was removed, must be confirmed because it determines whether the shop-visit deadline or the 100-cycle deadline governs.
- **Note:** The 1st-stage hub's cycles since new are 4,000 on 2025-10-29 and 4,300 now, consistent with 300 engine cycles elapsed (30,000 to 30,300).
- **Note:** The 2nd-stage hub (PKLBST5005) is listed with a 4,000-cycle limit and has about 1,700 cycles remaining. Its removal timing is governed by the same paragraph (g) but is not the controlling limit here.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200 (4,800 cycles)
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBST5005 (4,000 cycles)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a supported V2528-D5 with an installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) that is listed in Table 1 with a 6,200-cycle removal limit, so the AD applies. The hub is at 2,500 cycles since new, and the record shows no engine shop visit yet, so removal is due at the next engine shop visit before the hub exceeds 6,200 cycles, and no later than engine cycle 54,200 on the current utilization. The 2nd-stage hub cannot be assessed because its serial number and cycles since new are unknown.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after 2025-10-29, before it exceeds 6,200 cycles since new. The 100-flight-cycle alternative (engine cycle 50,100) has already passed, so under the later-of reading the shop visit governs.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The serial number of the installed HPT 2nd-stage hub is unknown, so it cannot be checked against the Table 1 2nd-stage hub serial numbers.
- **Missing fact:** Cycles since new for the HPT 2nd-stage hub are unknown, so a removal limit cannot be assessed for that hub.
- **Missing fact:** The only dated cycles-since-new reading is 2,000 at 2025-10-29; the 2,500 value is not dated, so the current count used for the remaining-cycles figure should be confirmed.
- **Missing fact:** No engine shop visit is recorded in the events list. The timing of the next shop visit determines when removal is due, so it should be tracked.
- **Note:** Screening aid only; this is not a compliance determination. The engine record's operator AD status is not used as evidence.
- **Note:** Engine cycles rose from 50,000 (2025-10-29) to 50,500 (2026-03-10), and the hub rose from 2,000 to 2,500 cycles since new over the same period, which is consistent.
- **Note:** The Federal Register text says the 1st-stage hub listing is 2A5001 with S/N PKLBST7489, which matches the installed hub exactly.
- **Note:** The unknown 2nd-stage hub data should not be read as evidence that the hub is unaffected.
- **Note:** If the shop visit is delayed, the hub will exceed its limit at engine cycle 54,200 on the current pace; the cycle projection assumes constant utilization.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row P/N 2A5001, S/N PKLBST7489, limit 6,200

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The directive is in force as of the question date (effective October 29, 2025) and the engine model V2522-A5 is supported and within the listed models. However, the engine record lists no installed components and no events, so whether any installed HPT 1st-stage or 2nd-stage hub has a P/N and S/N in Table 1 cannot be determined; applicability and required action cannot be established from the record.
- **Missing fact:** No installed component record for the HPT 1st-stage hub is supplied. Whether an installed hub has P/N 2A5001 and a listed S/N in Table 1 to paragraph (g) must be confirmed before applicability can be decided.
- **Missing fact:** No installed component record for the HPT 2nd-stage hub is supplied. Whether an installed hub has P/N 2A4802 and a listed S/N in Table 1 to paragraph (g) must be confirmed before applicability can be decided.
- **Missing fact:** No engine event history is supplied, so it is unknown whether any engine shop visit has occurred or would occur after the effective date, which controls the timing of the removal requirement.
- **Missing fact:** No operator AD status record for this directive is supplied. Any recorded status is a claim to check and cannot settle the outcome.
- **Note:** The directive is a final rule published 2025-09-24 with effective date October 29, 2025, so it is in force on the question date.
- **Note:** The record has no installed components and no events; an absence of records is not evidence that affected hubs are absent.
- **Note:** If a listed hub is later found installed, the 100-flight-cycle or next-shop-visit timing in paragraph (g) would need to be recomputed from the then-current engine cycle count, which is not supplied here.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model V2500-A1 is not on the screen's supported list of IAE V2500 models, so no applicability determination is made against AD 2025-19-13.
- **Note:** Engine model V2500-A1 is outside the supported scope for this screen; no applicability or compliance conclusion is drawn.
- **Note:** The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 matches a row in Table 1 of the AD, but this is not evaluated because the engine model is out of scope.
- **Note:** The directive is in force effective October 29, 2025, as of the question date.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The engine is a supported V2527-A5 with an installed 3rd stage HPC rotor blade set listed as P/N 6A8353, which falls within the directive's applicability. Replacement of the full blade set is required at the next engine shop visit after the 2026-09-24 effective date where the 3rd stage HPC rotor blade is exposed; the record shows no events, so no deadline is computed.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum).
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** No events are recorded. Whether the engine has had an engine shop visit on or after 2026-09-24, and whether the 3rd stage HPC rotor blades were exposed at that visit, is not shown. This determines whether the required replacement has been triggered.
- **Missing fact:** The blade set serial number is not tracked at set level, so the individual blades cannot be confirmed as P/N 6A8353 base or as parts eligible for installation (for example P/N 6A8353-001, 6C8368, or 6C8403).
- **Note:** The directive was published as a final rule effective 2026-09-24, so it is in force on 2026-10-05. The correction 2026-18423 corrects paragraph (g) to say 'blade is exposed' and is the operative text; the timing is unchanged.
- **Note:** The engine record has no events. This screen does not establish whether any shop visit since the effective date exposed the blades. A missing or empty events list is not evidence that no shop visit occurred.
- **Note:** The installed blade set is recorded only at P/N 6A8353 with serial not tracked at set level. A blade modified to P/N 6A8353-001 is a part eligible for installation, but the record does not show the modification status.
- **Note:** No ad_records or amoc_claims are present for this directive. This screen does not state compliance status and is not an operator AD status record.
- **Note:** Under the directive's wording, the required replacement is triggered by a future engine shop visit with blade exposure, so no fixed flight-cycle deadline can be computed.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** AD 2026-17-03 (FR 2026-16954, effective 2026-09-24) applies to V2533-A5 engines with a 3rd stage HPC rotor blade having P/N 6A8353 or 6A8688 installed. The recorded 3rd stage HPC rotor blade set is P/N 6C8368, which the AD lists as a part eligible for installation, so the supplied record places the engine outside the directive's applicability.
- **Missing fact:** The record gives only a set-level part number of 6C8368. Confirmation that every individual 3rd stage HPC rotor blade is P/N 6C8368 (or another eligible P/N) and that no blade is P/N 6A8353 or 6A8688 is needed to rule out a mixed set, since the applicability turns on any blade with an affected P/N installed.
- **Note:** This is a screening aid, not a compliance determination. No finding of compliance or noncompliance is made.
- **Note:** Even though applicability does not apply on the record as given, paragraph (g) would be triggered only at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor is exposed, if any blade were an affected P/N. The engine record contains no events, so no shop visit is recorded.
- **Note:** The synthetic record does not track blade serial numbers at set level and the record contains no events.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The engine is a supported V2530-A5 with 3rd stage HPC blades P/N 6A8688 installed, so the directive applies. The only shop visit was inducted 2026-09-14, before the 2026-09-24 effective date, so the paragraph (g) replacement trigger ('next engine shop visit after the effective date') is not met by that visit, though the blade exposure on 2026-09-30 needs review.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Blade serial numbers are not tracked at set level, so the installed P/N 6A8688 match cannot be tied to a serial-level record; this does not change the applicability match but limits traceability of the blades removed on 2026-09-30.
- **Missing fact:** The record does not state whether the blade removed from the stage 3-8 drum on 2026-09-30 was a 6A8688 blade or whether the full set was removed and replaced; this matters if a later shop visit occurs after the effective date.
- **Missing fact:** The FAA's intent (correction 2026-18423 and the preamble response to United Airlines) is that the paragraph (g) trigger is the shop visit occurring after the effective date; the reviewer should confirm with the FAA that an induction before the effective date with exposure after it does not trigger replacement.
- **Note:** Not a compliance determination. The operator's qualifies_as_engine_shop_visit 'yes' assertion is about the 2026-09-14 induction; that induction meets the definition in (h)(3) but predates the effective date, so it does not start the paragraph (g) obligation.
- **Note:** If the exposure on 2026-09-30 were read as the triggering event, replacement of the full blade set would be due immediately; no flight-cycle counter was supplied, so no cycle deadline can be computed. Reviewer should resolve this reading before relying on no_action_triggered.
- **Note:** Continuing obligation: if the engine is inducted again after 2026-09-24 and blades are exposed, paragraph (g) replacement applies. Parts eligible for installation are listed in (h)(1).

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2026-17-03 (FR 2026-16954, effective 2026-09-24) applies to this V2524-A5 engine, which has 3rd stage HPC rotor blade P/N 6A8353 installed. The 2026-10-01 shop visit was after the effective date, but the recorded event exposed the HPC rotor without removing any 3rd stage blade from the stage 3-8 drum, so the blade-exposure trigger in paragraph (h)(2) is not shown; replacement of the full blade set is required at the next engine shop visit where a 3rd stage blade is exposed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum; no fixed deadline otherwise.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** No engine flight-cycle counter is in the record, so no cycle-based deadline can be computed.
- **Missing fact:** Confirmation that no 3rd stage HPC rotor blade was removed from the stage 3-8 drum during the 2026-10-01 visit beyond the stated exposure note; the trigger depends on the blade-removal definition, not the rotor-inspection exposure.
- **Missing fact:** Whether the operator reads paragraph (g) of the uncorrected 2026-16954 text ('the 3rd stage HPC rotor is exposed') as triggered by the 2026-10-02 rotor inspection. The published correction 2026-18423 changes this to 'blade is exposed', which the record does not meet.
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** The 2026-10-01 shop visit was inducted after the effective date and is recorded by the operator as qualifying as an engine shop visit, which is an operator assertion to check.
- **Note:** The 2026-10-02 event states the HPC rotor was exposed but no 3rd stage blade was removed, so the (h)(2) blade-exposure definition is not shown. Under the uncorrected wording 'rotor is exposed', that visit could have triggered replacement; the corrected wording governs and the visit has closed, with the engine returned to service on 2026-10-04.
- **Note:** Blade set serial numbers are not tracked at set level, so blade-level identification cannot be confirmed from the record.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** Federal Register document 2025-20088 is a proposed rule, not yet in force on 2026-01-15, so it cannot require action. The engine model (V2527E-A5) is within the proposed scope, and the installed 3rd stage HPC rotor blade set is recorded as P/N 6A8353, which the proposal lists, but the record shows no 3rd stage blade exposure event.
- **Missing fact:** Blade serial numbers are not tracked at set level, so the individual blade identities and whether each blade is a listed part cannot be confirmed from the record.
- **Missing fact:** The events list is empty. No record shows whether any 3rd stage HPC rotor blade has been removed from the HPC stage 3 to 8 drum (the proposed exposure trigger), so an exposure event cannot be ruled in or out.
- **Missing fact:** The directive has not been published as a final rule with an effective date; whether it will be adopted, in what form, and with what effective date is not known from the supplied document.
- **Note:** This is a screening aid, not a compliance determination. The directive is a proposal and creates no obligation as of the question date.
- **Note:** Any future final rule should be checked for its effective date and final text before this screen is relied on.
- **Note:** Because the directive's required action is tied to a future blade exposure after the effective date, no deadline can be computed even if the rule is adopted as proposed.
- **Unresolved locator:** 2025-20088 preamble DATES and Effective date record

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 is in force (effective 2025-10-10) and covers the V2527-A5 engine, which is in the supported scope, for an air carrier operation. The operator's record states that neither its approved program nor TLM ALS paragraph B.1 yet incorporates table 1, so the one-time revisions under (g)(1) and (g)(2) are required by 2026-01-08 and are not yet recorded as done.
- **Stated timing:** Within 90 days after the effective date of 2025-10-10, i.e., on or before 2026-01-08, revise TLM ALS paragraph B.1 (g)(1) and the approved maintenance or inspection program (g)(2) for air carrier operations.
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** No installed component record for the HPT Stage 1 Hub (P/N 2A5001) is supplied, so it cannot be determined whether the part is installed or when piece-part exposure would occur; this does not affect the revision obligation but bears on the piece-part inspection under B.1.
- **Missing fact:** No installed component record for the HPT Stage 2 Hub (P/N 2A4802) is supplied, so its installed status and piece-part exposure history are unknown.
- **Missing fact:** The actual revision date and content of the operator's approved program and the TLM ALS are not confirmed beyond the operator's statement that they are not yet revised; the operator should confirm the revision status before the deadline.
- **Note:** This is a screening aid, not a compliance determination; the operator's record statement that revisions are not yet incorporated is a claim to verify.
- **Note:** The 90-day period runs from the 2025-10-10 effective date, giving 2026-01-08. The Federal Register publication date (2025-09-05) would give 2025-12-04 under a publication-date reading, but the directive text ties the period to the effective date, so that reading is not adopted here.
- **Note:** No flight-cycle deadline is stated, so latest_engine_flight_cycles is null.
- **Note:** The operator record lists no installed components and no events, so no part-level match or piece-part exposure can be assessed.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive is in force as of the question date (effective October 10, 2025) and the engine model V2522-A5 is within its applicability, but the record lists no installed components (including no HPT Stage 1 or Stage 2 hub) and does not state whether the operator conducts air carrier operations, so no action trigger can be determined from the supplied facts.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** No record of the HPT Stage 1 hub (P/N 2A5001) installed on the engine; the record lists no installed components, so it cannot be determined whether this listed part is present.
- **Missing fact:** No record of the HPT Stage 2 hub (P/N 2A4802) installed on the engine; the record lists no installed components, so it cannot be determined whether this listed part is present.
- **Missing fact:** Operator air carrier status is unknown; paragraph (g)(2) applies to air carrier operations and the operator's approved maintenance or inspection program depends on this fact.
- **Missing fact:** Engine has no recorded shop visit or event history, so whether a piece-part exposure has occurred, which triggers the inspection task reference, cannot be determined.
- **Note:** Screening aid only; not a compliance determination.
- **Note:** The directive requires a one-time ALS and program revision, due within 90 days after October 10, 2025, which is January 8, 2026; the record does not establish the engine's installed hub parts or operator status, so the timing is not fully determined here.
- **Note:** Paragraph (g)(1) requires revision of the TLM for the listed V2500-A5 P/N 2A4408 TLM, which is an operator-facing document; the record does not show the operator's TLM revision status.
- **Note:** The 2024 NPRM (2024-26092) is superseded by the final rule for this screen and was not relied on for requirements.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The final rule takes effect 2025-10-29, after the question date, so no action is triggered on 2025-10-15. The installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) matches a Table 1 entry with a 6,000-cycle removal limit and has 990 cycles since new, leaving 5,010 cycles, so the engine falls within the directive once effective.
- **Stated timing:** Once effective on 2025-10-29, remove the listed hub at the next engine shop visit before exceeding 6,000 cycles since new, or within 100 flight cycles from 2025-10-29, whichever occurs later. The installation prohibition in paragraph (h) applies from 2025-10-29.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine flight-cycle counter is not in the record, so the latest engine flight-cycle deadline cannot be computed. It is needed to fix the 100-flight-cycle window from the effective date.
- **Missing fact:** The events list is empty, so there is no shop-visit history. Whether a future engine shop visit occurs before the limit is needed to schedule the required removal.
- **Missing fact:** The HPT 1st-stage hub serial SYN-HUB1-0018 is not in Table 1, so it is not matched. This relies on the operator's record being complete and accurate for that hub; the installed hub's cycles are recorded but the serial cannot be verified against the table from the supplied text alone.
- **Note:** This is a screening aid, not a compliance determination. The answer does not state that the engine or any part is compliant or noncompliant.
- **Note:** The removal cycle limit of 6,000 cycles is not the binding constraint on the current figures; the earlier of the shop-visit trigger or the 100-flight-cycle window governs the timing once effective.
- **Note:** No ad_records or amoc_claims were supplied, so no operator AD status or AMOC claim was assessed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSR2100, limit 6,000 cycles

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a listed V2531-E5 and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is in Table 1 with a 4,800-cycle removal limit. The hub's recorded 4,990 cycles since new already exceed that limit, so removal is required at the next engine shop visit or within 100 flight cycles of the 2025-10-29 effective date (engine cycle 60,100), whichever occurs later; the 100-cycle backstop sets the latest date.
- **Stated timing:** Remove the HPT 1st-stage hub at the next engine shop visit after 2025-10-29 or within 100 flight cycles of the effective date, whichever is later; under the reading applied here, the latest engine flight-cycle count is 60,100 (60 cycles from the 2025-11-05 reading of 60,040). The limit is already exceeded, so the shop-visit portion of the requirement is not a future deadline.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The events list is empty, so it is unknown whether an engine shop visit has occurred since the effective date. A shop visit would change the removal timing under paragraph (g), and the record does not show one.
- **Missing fact:** The record gives 4,990 cycles since new without a date and 4,950 at 2025-10-29. The current figure is taken as 4,990 at the 2025-11-05 snapshot. Either value exceeds the 4,800 limit, so the conclusion does not change.
- **Note:** This is a screening aid, not a compliance determination. The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0019) is not listed in Table 1, so no match is made for it on this record.
- **Note:** The engine cycle count at the effective date is taken as 60,000 from the 2025-10-29 reading. The 100-cycle period is counted from that reading to reach 60,100.
- **Note:** The operator's AD status record and any AMOC claims were not supplied; none were evaluated.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row, P/N 2A5001, S/N PKLBSS9200, limit 4,800

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** Directive 2021-11960 (AD 2021-11-15) is in force on the question date, and this V2533-A5 engine has HPT 1st- and 2nd-stage disks with listed part numbers 2A5001 and 2A4802. Applicability cannot be decided because the serial numbers have not been checked against the Appendix A tables, which were not supplied, and no engine flight-cycle count is recorded. This is a screening aid, not a compliance determination.
- **Stated timing:** If the disk serial numbers are listed in Appendix A, the USI is due at the next engine shop visit after 2021-07-13 or before the disk reaches 3,200 FCs since 2021-07-13, whichever occurs first. Superseding AD 2022-02-09 (effective 2022-03-15) changes the compliance times for disks that have operated in high-thrust engines, so it must be reviewed once effective.
- **Missing fact:** Serial number SYN-DISK1-0020 must be checked against Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1 (or V2500-E5-72-0015 for E5 engines). The appendix tables were not supplied, so listing cannot be confirmed.
- **Missing fact:** Serial number SYN-DISK2-0020 must be checked against Appendix A, Table 2, of the applicable NMSB. The appendix tables were not supplied, so listing cannot be confirmed.
- **Missing fact:** No engine flight-cycle counter is recorded. The 3,200-FC limit runs from the 2021-07-13 effective date, so the cycles accrued since then are needed to compute any deadline.
- **Missing fact:** The contents of IAE NMSB V2500-ENG-72-0713 Rev 1 and NMSB V2500-E5-72-0015 (Appendix A tables, USI procedures) were not supplied.
- **Missing fact:** The event history is empty. Whether any engine shop visit has occurred since 2021-07-13 is unknown, and that would start or end the shop-visit compliance window.
- **Missing fact:** The record does not show whether the disk has operated in a high-thrust engine (V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2533-A5). This does not change this V2533-A5 engine's obligation but matters for the superseding AD.
- **Note:** Authority state is in_force for 2021-11960 on 2022-03-01. Superseding AD 2022-02574 was published 2022-02-08 and is effective 2022-03-15, so it is not yet in force on the question date but must be reviewed for the V2533-A5 engine.
- **Note:** Part numbers match the directive, but serial-number listing in Appendix A is unverified. The matched_parts listed_serial_number fields are null because the tables were not supplied.
- **Note:** The record has no shop-visit events, no cycle counter, and no thrust-history data, so no deadline or remaining-cycle figure can be computed.
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
- **Summary:** The engine model V2533-A5 is in scope and both installed disk part numbers match the directive, but the directive is not effective until 2022-03-15 and the disk serial numbers cannot be checked against the Appendix A serial-number tables, which were not supplied. No action can be determined from the record, and no action is required on the question date.
- **Missing fact:** The HPT 1st-stage disk serial number SYN-DISK1-0020 must be checked against Appendix A, Table 1, of the referenced NMSB (V2500-ENG-72-0713 Rev 1 or V2500-E5-72-0015 Rev 1). Applicability depends on this check.
- **Missing fact:** The HPT 2nd-stage disk serial number SYN-DISK2-0020 must be checked against Appendix A, Table 2, of the referenced NMSB. Applicability depends on this check.
- **Missing fact:** Appendix A serial-number tables of the referenced NMSB are not included in the supplied text, so the serial-number listing cannot be confirmed.
- **Missing fact:** Figure 1 to paragraph (g)(1), which sets the compliance times, is an image not included in the supplied text, so the due date cannot be computed.
- **Missing fact:** Engine flight-cycle counter and disk cycle history are not in the record. The record has no events and no ad_records, so it is unknown whether either disk has operated on a high-thrust engine (V2527E-A5, V2527M-A5, V2528-D5, V2530-A5 or V2533-A5), which would set the shorter compliance time.
- **Missing fact:** Engine shop visit history is not recorded. Shop-visit timing would govern the required inspection if the disk is listed, so the record cannot confirm whether any shop visit has occurred.
- **Note:** The record has no ad_records or amoc_claims, so there is no operator AD status to check.
- **Note:** Because the directive is effective 2022-03-15, it cannot require action on 2022-03-01. Re-screen once the Appendix A serial-number tables and the Figure 1 compliance times are available, and once the disks' operating history is documented.
- **Note:** This is a screening aid and not a compliance determination.
- **Unresolved locator:** 2022-02574 (c) Applicability, items (1) and (2)
- **Unresolved locator:** 2022-02574 (g)(3) V2522-A5, V2524-A5, V2525-D5, V2527-A5 only

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 covers V2530-A5 engines with an HPT 1st-stage disk P/N 2A5001 or HPT 2nd-stage disk P/N 2A4802 whose serial number is listed in the NMSB Appendix A tables. Both installed part numbers match, but the Appendix A serial lists are not in the supplied record or Federal Register text, and the Figure 1 compliance time is not supplied, so applicability and any deadline cannot be settled.
- **Stated timing:** Under paragraphs (g)(1) and (g)(2), the USI is due within the Figure 1 compliance time or 10 flight cycles after March 15, 2022, whichever is later. Figure 1 is not in the supplied text, so the due date cannot be computed.
- **Missing fact:** Serial SYN-DISK1-0021 must be checked against Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Revision 1 or V2500-E5-72-0015 Revision 1 to decide whether paragraph (c)(1) applies. The Appendix A lists are not in the supplied text.
- **Missing fact:** Serial SYN-DISK2-0021 must be checked against Appendix A, Table 2, of the same NMSBs to decide whether paragraph (c)(2) applies.
- **Missing fact:** Figure 1 to paragraph (g)(1) is not included in the supplied text. It sets the compliance time that decides the USI deadline for V2530-A5 disks.
- **Missing fact:** Whether either disk has operated in a high-thrust model engine matters for the (g)(3)(ii) and (g)(4)(ii) readings, but this applies only to low-thrust models. For V2530-A5 the (g)(1) and (g)(2) timing governs, so this is a check, not a missing input.
- **Missing fact:** The record has no engine flight-cycle counter or accumulated cycles for either disk, so the 10-cycle and cycle-based deadlines cannot be computed.
- **Missing fact:** The events list is empty. Whether an engine shop visit has occurred since March 15, 2022 is unknown, and a shop visit would trigger the (g)(1) and (g)(2) timing.
- **Note:** This is a screening aid, not a compliance determination. The engine's serial-number eligibility, Figure 1 timing, and cycle counts must be checked before any status is set.
- **Note:** The record has no ad_records or amoc_claims, so no operator AD status claim is evaluated.
- **Note:** The synthetic record (SYN- identifiers) has no shop visit events, so event-triggered timing cannot be evaluated.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a supported V2533-A5 with an installed HPT 1st-stage disk P/N 2A5001, S/N PKLBSH1829, which is listed in paragraph (c)(1). The directive was effective July 19, 2021, so a USI of that disk is required within 10 flight cycles after the effective date, which computes to engine flight cycles 33010; the engine was at 33004 on 2021-07-20, leaving 6 cycles. Nothing in the record shows the USI has been done.
- **Stated timing:** Within 10 flight cycles after the July 19, 2021 effective date, i.e. by engine flight cycle 33010 (about 6 cycles after the 2021-07-20 reading of 33004).
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** No event record shows whether the required ultrasonic inspection of the HPT 1st-stage disk has already been performed. If it has, the record must show the inspection and its result before the deadline is assessed as met.
- **Missing fact:** The disk's accumulated cycles since new are not in the record, so no component cycle figure can be computed. The USI result and pass/fail status are also not in the record; the paragraph (g)(3) removal obligation depends on them.
- **Note:** The screen covers only the HPT 1st-stage disk. The HPT 2nd-stage disk (P/N 2A4802, S/N SYN-DISK2-0022) does not match the serial numbers in paragraph (c)(2) on the record provided. Its status should be confirmed against the full list before closing.
- **Note:** The Table 1 and Table 2 images are not included in the text provided. Applicability here relies on the serial numbers stated in paragraph (c).
- **Note:** This is a screening aid, not a compliance determination. The operator's AD status record and any AMOC are not in the record, and none is assessed here.
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
- **Summary:** The directive is in force and covers V2533-A5 engines with an HPT 1st-stage disk P/N 2A5001 or HPT 2nd-stage disk P/N 2A4802 whose serial numbers are listed in the NMSB appendix tables, which were not supplied, so applicability cannot be decided for either installed disk. If the disks are listed, a USI is due at the next engine shop visit or before 3,200 FCs after July 13, 2021, whichever is first, but the cycle count at the effective date is missing, so no deadline can be computed.
- **Stated timing:** For each listed disk: at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first. No shop visit is recorded.
- **Missing fact:** Serial number PKLBSH1829 must be checked against Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1 (or V2500-E5-72-0015) to confirm whether the HPT 1st-stage disk is within the directive's population. The appendix tables were not supplied.
- **Missing fact:** Serial number SYN-DISK2-0022 must be checked against Appendix A, Table 2, of the NMSB to confirm whether the HPT 2nd-stage disk is within the population. The tables were not supplied.
- **Missing fact:** The engine flight-cycle count on the effective date (July 13, 2021) is needed because the 3,200-FC limit runs from the effective date. Only the 2021-07-19 and 2021-07-20 readings are recorded, so the deadline cannot be computed. The count on 2021-07-19 (33000) bounds the effective-date count from above.
- **Missing fact:** No engine events are recorded. It is unknown whether an engine shop visit has occurred or will occur since July 13, 2021, and whether any such visit meets the AD's engine shop visit definition. The absence of a recorded event is not evidence that no shop visit occurred.
- **Missing fact:** Whether the installed disks' serial numbers appear in the NMSB appendix tables is not part of the engine record; the document content was not supplied.
- **Note:** The engine model V2533-A5 is within the supported scope.
- **Note:** The FR record gives the 3,200-FC limit from the effective date of July 13, 2021. The current reading (33004 on 2021-07-20) is not enough to compute the deadline without the effective-date count.
- **Note:** Because the effective-date count is at most 33000, any deadline computed from it would be at most 36200 FCs. This is a bound only, not a deadline.
- **Note:** This is a screening aid, not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 applies to this V2527M-A5 engine, which has an installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) listed in Table 1 with a 6,000-cycle removal limit. The hub has 3,500 cycles since new, so 2,500 cycles remain, and removal is required at the next engine shop visit before that limit is exceeded. The HPT 1st-stage hub (S/N SYN-HUB1-0023) is not a listed serial number, so it is not matched.
- **Stated timing:** At the next engine shop visit after 2025-10-29, and before the hub exceeds 6,000 cycles since new (about 2,500 more cycles), or within 100 flight cycles of the effective date if that is later. The 100-cycle window measured from the effective date (engine cycles 20,100) has already passed, so the shop-visit and cycle-limit deadline controls under the 'whichever occurs later' wording.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The 3,500 cycles-since-new value has no date, while the only dated reading (1,000 at 2025-10-29) is older. The 3,500 value is assumed to be current as of the question date. Confirmation is needed because the remaining-cycle figure depends on it.
- **Missing fact:** No engine shop visit is recorded. The timing of the next shop visit is unknown, so whether removal can be done before the 6,000-cycle limit is not established.
- **Missing fact:** The HPT 1st-stage hub serial number SYN-HUB1-0023 is not among the Table 1 serial numbers for P/N 2A5001, so no match is recorded. Its cycles-since-new value is 3,500 but has no limit to compare against because it is not listed.
- **Missing fact:** The record has no operator AD status entry for AD 2025-19-13. The only related entry is a maintenance program revision citing AD 2025-17-16, a different AD, so it does not show that this AD's Table 1 part has been addressed.
- **Note:** Screening aid only. This is not a compliance determination, and it does not state that any part is compliant or noncompliant.
- **Note:** The engine's cycle count rose from 20,000 on 2025-10-29 to 22,500 on 2026-10-06, a difference of 2,500, which matches the hub's cycles-since-new change from 1,000 to 3,500. This supports treating 3,500 as the current count.
- **Note:** The latest_engine_flight_cycles value of 25,000 assumes the hub accumulates cycles at the same rate as the engine while installed. Confirm this assumption against the hub's own cycle record.
- **Note:** The 2025-12-01 maintenance program revision cites AD 2025-17-16 and is not an engine shop visit under this AD's definition. It does not satisfy this AD.
- **Note:** The HPT 1st-stage hub is not listed in Table 1 by serial number, so no removal action is triggered for it on this record.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (Federal Register 2026-16954, as corrected by 2026-18423) is in force on 2026-10-06 with a 2026-09-24 effective date. The engine is a supported V2527M-A5 with 3rd stage HPC rotor blade set P/N 6A8688 recorded as installed, so it is within applicability. Required action (full set replacement with parts eligible for installation) is triggered only at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed; no such event is recorded, so no action is due now and no cycle deadline can be computed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed (blade removed from the HPC stage 3 to 8 drum), replace the full set of 3rd stage HPC rotor blades with parts eligible for installation.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The blade set serial number is recorded as not tracked at set level, so the record cannot confirm the set's identity or blade-level exposure history against the AD definitions.
- **Missing fact:** No engine shop visit after the 2026-09-24 effective date is recorded. Whether one occurs, and whether the 3rd stage HPC rotor blade is exposed at it, is needed to determine when the replacement is due.
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** The 2025-20088 NPRM text (replacement at the next 3rd stage exposure after the effective date) was superseded by the final rule's shop-visit wording, so the final rule's wording was applied.
- **Note:** The operator's maintenance program revision (2025-12-01) references AD 2025-17-16 table 1 and is not an AD status record for 2026-17-03; it was not used to clear or trigger the requirement.
- **Note:** The engine cycle readings (20000 on 2025-10-29; 22500 on 2026-10-06) are not used because no shop visit deadline is established.
- **Note:** No amoc_claims were supplied, and no AMOC is claimed.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 (effective 2025-10-10) applies to the V2527M-A5 engine. The record shows the one-time TLM ALS and air-carrier program revision dated 2025-12-01, inside the 90-day window that ended about 2026-01-08, but the HPT 1st- and 2nd-stage hub inspections must be carried out at piece-part exposure, and no such exposure is recorded.
- **Stated timing:** The ALS and program revisions were due within 90 days of 2025-10-10 (by about 2026-01-08) and are recorded as done 2025-12-01. The hub inspections (TASK 72-45-11-200-006 for P/N 2A5001 and TASK 72-45-31-200-009 for P/N 2A4802) are due at the next piece-part exposure of the engine.
- **Missing fact:** Evidence that the Revision 48 TLM ALS paragraph B.1 update (P/N 2A4408, V2500-A5 TLM) and the air-carrier maintenance program update were actually made is only an operator assertion; confirm the revised documents contain the table 1 tasks.
- **Missing fact:** The HPT 2nd-stage hub shows cycles_since_new 3500 on the component record but 1000 on the 2025-10-29 reading; the conflict must be resolved before any cycle-based reasoning about the hub.
- **Missing fact:** No piece-part exposure or shop visit is recorded, so it is unknown whether the hub inspections have been or will become due; the next piece-part exposure date is needed.
- **Missing fact:** The HPT 1st-stage hub record has no dated cycle reading, so its current cycles are unverified.
- **Missing fact:** The inspection thresholds (AUSI intervals) are in the TLM task text, which was not supplied; they are needed to assess the hubs at the next piece-part exposure.
- **Note:** Screening aid only; this is not a compliance determination. The engine record is synthetic.
- **Note:** The engine is at 22500 cycles on the question date, but the directive is time-based for the ALS revision and event-based for the hub inspections, so no cycle deadline is computed.
- **Note:** The 3rd stage HPC rotor blade set (6A8688) is not listed in the directive and is not matched.
- **Note:** Applicability and in-force status are based on the Federal Register record supplied; no later amendment was provided.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is a listed model and AD 2025-19-13 (effective October 29, 2025) is in force, so the directive applies to this engine. Neither installed hub matches a P/N and S/N pair in Table 1: the 1st-stage hub serial SYN-HUB1-0024 is not listed, and serial PKLBST5011 is listed only under P/N 2A5001, not under the recorded P/N 2A4802. No removal action is triggered now, but the installation prohibition applies.
- **Missing fact:** The recorded 2nd-stage hub P/N is 2A4802 with S/N PKLBST5011, but Table 1 lists serial PKLBST5011 only under P/N 2A5001 (1st-stage hub). Confirming the recorded P/N and S/N is needed to settle whether this hub is a listed part; if the P/N were misrecorded, the removal requirement could apply.
- **Missing fact:** Only the current installed hub records are given; the record does not show whether either hub's P/N and S/N pair has been verified against the Table 1 list. Records of hub history and any prior shop visit that exposed these hubs are absent.
- **Note:** This is a screening aid, not a compliance determination. The engine record shows no engine shop visit events, so the shop-visit trigger in paragraph (g) has not occurred on the record provided.
- **Note:** The 2nd-stage hub serial PKLBST5011 also appears in Table 1 under the 1st-stage hub P/N 2A5001, which suggests a possible record or transcription discrepancy worth verifying against source documents.
- **Note:** The engine record is synthetic (SYN- identifiers appear in the serial number and asset ID).

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model recorded is CFM56-5B4/3, which is not among the IAE V2500 models supported by this screen, so no applicability determination is made under Federal Register document 2025-17066.
- **Note:** The engine record lists model CFM56-5B4/3, a CFM International model, not an IAE V2500 model; the screen therefore does not assess this engine against the directive.
- **Note:** The engine record contains no installed components and no events.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine is within the applicability of AD 2025-19-13, which is in force effective 2025-10-29. Installed HPT 1st-stage hub P/N 2A5001, S/N PKLBST7489 is listed in Table 1 with a 6,200-cycle removal limit and has 3,600 cycles since new, so removal and replacement is required at the next engine shop visit before the limit is exceeded, subject to the 100-flight-cycle clause discussed in the alternative readings.
- **Stated timing:** Remove and replace the hub at the next engine shop visit after 2025-10-29 and before the hub exceeds 6,200 cycles since new (about 2,600 cycles from the 2026-03-01 reading). The 100-flight-cycle alternative from the effective date (engine cycle 20,100) has already passed, so the reading that applies to the 'whichever occurs later' clause needs confirmation.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** No engine shop visit after the 2025-10-29 effective date is recorded. Whether one has occurred determines whether the removal has been performed and whether the next shop visit is the trigger for removal.
- **Missing fact:** The second-stage hub S/N SYN-HUB2-0026 (P/N 2A4802) is not listed in Table 1, so it is not matched to the directive on the supplied facts. Its listed-serial status depends on the operator's confirmation of the S/N against the table.
- **Note:** The 2024 blend repair and the 2024 repeat ultrasonic inspection were before the effective date and do not change the AD status; the repair is not an engine shop visit under the record's dated events, and the AD does not provide a repair-based exemption.
- **Note:** The hub cycles since new (3,000 on 2025-10-29, 3,600 on 2026-03-01) track the engine cycle change (20,000 to 20,600), which supports the 2,600-cycle projection.
- **Note:** The 2025-10764 proposal was not relied on; the final rule 2025-18469 governs.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 row: HPT 1st-stage hub, 2A5001, PKLBST7489, 6,200 cycles

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
- **Summary:** The V2527-A5 engine is within the directive's applicability, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in Table 1 with a 4,800-cycle removal limit. The hub is at 4,750 cycles since new, so it must be removed at the next engine shop visit before reaching that limit, which is about 15,300 engine flight cycles.
- **Stated timing:** Remove and replace the listed HPT 1st-stage hub at the next engine shop visit, and before the hub exceeds 4,800 cycles since new (about 15,300 engine flight cycles). The 100-flight-cycle alternative from the effective date (about 15,100 cycles) has already passed, so the later of the two governs.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** No engine shop visit events are recorded. Whether a shop visit has occurred since the effective date, and whether the hub was removed, is needed to confirm the required action has been completed.
- **Missing fact:** The current cycles-since-new reading is shown as 4,750 without a date. It is taken here as the snapshot value; confirmation is needed because the remaining-cycle count depends on it.
- **Missing fact:** The operator claims an AMOC extending the hub limit to 5,300 cycles since new, but no FAA approval is on file (approval_reference unknown). The claim cannot be relied on, so the 4,800-cycle limit is applied.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0027) is not listed in Table 1, so it does not match the table on these facts. This is not a clearance; the screen covers only the listed serials.
- **Note:** The operator's AMOC note (5,300 cycles since new) has no FAA approval on file and is not used to set the limit.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a supported V2524-A5 and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) matches a row in Table 1 to paragraph (g), so the AD applies. Removal is required at the next engine shop visit before the hub exceeds its 4,000-cycle limit, and the installation prohibition in paragraph (h) already applies to any install after 2025-10-29. The operator's N/A status for AD 2025-19-13 conflicts with this record and is not evidence of compliance.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the HPT 2nd-stage hub exceeds 4,000 cycles since new, or within 100 flight cycles of 2025-10-29, whichever occurs later. No shop visit is recorded, so no calendar deadline is set.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** No engine shop visit history is recorded. Whether a shop visit has occurred since 2025-10-29, and whether it met the AD's shop visit definition, determines whether the removal obligation has been triggered.
- **Missing fact:** The current cycles_since_new value (1400) is undated, while the only dated reading is 1000 at 2025-10-29. The current value and its date need confirmation to set the remaining cycles precisely.
- **Missing fact:** The recorded N/A status states no affected hubs are installed, but the record shows an installed hub matching Table 1. The status needs review against the actual installed hub.
- **Note:** This is a screening aid, not a compliance determination. The 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0028) does not appear in Table 1 and is not matched on this record.
- **Note:** The directive's engine flight-cycle figures use the record's readings: 8000 at 2025-10-29 and 8400 at 2026-02-10. The component remaining cycles assume the hub's cycles since new increase one-for-one with engine cycles, which is consistent with the dated readings.
- **Note:** The AD's ad_records entry is an operator claim and was checked against the installed hub record, not accepted as evidence.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row for PKLBST5005 (limit 4,000 cycles since new)

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is a supported model within the AD's applicability, and the AD is in force (effective 2025-10-29). The installed HPT 1st-stage hub has the listed serial number PKLBSK9287 (listed P/N 2A5001, 100-cycle limit) but records 2400 cycles since new and is recorded as P/N 2A5001-01, so whether the P/N match holds and whether the 100-flight-cycle deadline from 2025-10-29 has passed cannot be settled from the record.
- **Stated timing:** Remove and replace at the next engine shop visit after 2025-10-29 before exceeding the 100-cycle limit, or within 100 flight cycles from 2025-10-29, whichever occurs later. The cycle limit is already exceeded, so the operative deadline is 100 flight cycles after 2025-10-29, which needs the engine flight-cycle count on that date.
- **Missing fact:** The engine flight-cycle count on 2025-10-29 (effective date) is not in the record, so the deadline of 100 flight cycles from that date cannot be computed.
- **Missing fact:** Installed P/N is recorded as 2A5001-01, while Table 1 lists P/N 2A5001. Whether the dash suffix is the same listed part must be confirmed; the S/N matches.
- **Missing fact:** No event history is recorded, so shop visits after 2025-10-29 and whether any engine flanges were separated cannot be checked.
- **Missing fact:** Whether the HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0029) is a listed part cannot be confirmed from the record; its S/N is not in Table 1, so no match is found on the supplied data.
- **Note:** This is a screening aid, not a compliance determination. The hub's recorded 2400 cycles since new exceeds the 100-cycle limit listed for its serial number.
- **Note:** The record has no engine flight-cycle counter, so the 100-flight-cycle deadline from 2025-10-29 cannot be computed. If the P/N match is confirmed and that deadline has passed on the record, the hub would be outside the AD's compliance window and needs immediate review.
- **Note:** The second-stage hub is not listed by serial number, so no action on it is indicated by the supplied data.
- **Note:** The operator's AD status record and any AMOC claims were not supplied.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row P/N 2A5001, S/N PKLBSK9287, limit 100 cycles

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
