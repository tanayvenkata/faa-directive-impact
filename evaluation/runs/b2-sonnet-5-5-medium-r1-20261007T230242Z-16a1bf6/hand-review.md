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
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers the V2527-A5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in table 1 with a 5,500 cycles-since-new removal limit. Removal and replacement is triggered at the next engine shop visit, and none is recorded. The hub is at 3,100 cycles, so 2,400 remain to the limit.
- **Stated timing:** At the next engine shop visit after 2025-10-29, no later than the later of the 5,500 cycles-since-new limit (engine flight cycle 45,050) or 100 flight cycles after the effective date (engine flight cycle 41,300). The later date is engine flight cycle 45,050. No shop visit is recorded yet.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** events: no engine shop visit is recorded, so whether and when the next shop visit occurs is unknown (events[] entries with qualifies_as_engine_shop_visit for AD 2025-19-13)
- **Note:** The 1st-stage hub was 1,650 cycles since new at engine flight cycle 41,200 and is 3,100 now (42,650). The 1,450-cycle engine difference matches the hub's increase. The limit is reached at engine flight cycle 45,050.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0001 is not in table 1, so no 2nd-stage hub is matched.
- **Note:** The NPRM 2025-10764 was superseded by the final rule, which adopts it as proposed.
- **Note:** This is a screening result, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 1st-stage hub PKLBST5011, 5,500

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine is a V2533-A5, a model within paragraph (c), and the AD is in force on the question date. Neither installed hub's P/N and S/N matches table 1 (the 1st-stage hub S/N PKLBST5012 differs from listed PKLBST5011), so the paragraph (g) removal is not triggered; the paragraph (h) installation prohibition still binds.
- **Note:** The 1st-stage hub S/N PKLBST5012 is close to listed PKLBST5011 but is a different serial number; a record transcription error would be worth verifying against the part's data plate.
- **Note:** The NPRM 2025-10764 was superseded by the final rule; the final rule text is identical in the relevant paragraphs.
- **Note:** No events or AD/AMOC records were supplied; none were needed for this outcome.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows for P/N 2A5001 and 2A4802

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2524-A5 is within the in-force AD 2025-19-13 applicability, but the HPT 1st-stage hub serial number is unknown, so it cannot be determined whether that hub is a listed part. The HPT 2nd-stage hub S/N SYN-HUB2-0003 is not listed in table 1, so it is not an affected part.
- **Missing fact:** installed_components[HPT 1st-stage hub].serial_number
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new
- **Missing fact:** events: no engine shop visit after 2025-10-29 is recorded, so the shop-visit trigger cannot be evaluated; the engine flight-cycle counter on 2025-10-29 is also not in the record
- **Note:** An unknown serial number is not evidence that the 1st-stage hub is unaffected. The P/N 2A5001 matches the listed 1st-stage hub P/N, so the S/N is decisive.
- **Note:** If the 1st-stage hub S/N is one of the four listed, action would be due at the next engine shop visit after 2025-10-29, at the later of the removal cycle limit being reached or 100 flight cycles after the effective date. PKLBSK9287 has a limit of only 100 cycles since new.
- **Note:** The 2nd-stage hub (5,100 cycles since new) has an unlisted S/N, so no removal is triggered for it.
- **Note:** No engine shop visit events are recorded.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g)

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for AD 2025-19-13.
- **Note:** The AD is effective 2025-10-29, so it is in force on the question date 2026-09-26.
- **Note:** No determination is made for this engine model.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 applies to this V2527E-A5 engine and has been in force since 2025-10-29. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed in table 1 (limit 3,900 cycles since new), so removal and replacement is required under paragraph (g). The deadline reading is ambiguous, as shown in the alternative readings.
- **Stated timing:** Under the 'whichever occurs later' reading, removal is due by the later of 100 flight cycles after 2025-10-29 (engine FC 18100) and the hub reaching 3,900 cycles since new (engine FC 20900). The shop visit induction on 2025-11-12 is the next shop visit after the effective date, so removal at this visit is the conservative reading.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** Confirmation that the 2025-11-12 induction meets the AD's engine shop visit definition in paragraph (i)(2). The record only asserts this (events[2025-11-12].qualifies_as_engine_shop_visit); it is not evidence that settles the point.
- **Missing fact:** Whether the agency intends removal at the next shop visit even when the cycle limit has not yet been reached (interpretation of paragraph (g)).
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0005 is not in table 1, so it is not matched.
- **Note:** The 2nd-stage hub cycles since new were 1,000 at engine FC 18000 and 1,040 at engine FC 18040, consistent with the engine counter. The remaining 2,860 cycles equal 3,900 minus 1,040.
- **Note:** Engine FC 20900 is 18040 plus 2,860.
- **Note:** The shop visit qualification is operator-asserted and should be verified.
- **Note:** This is a screening aid only and does not determine compliance.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 2nd-stage hub 2A4802 PKLBSS9840, limit 3,900

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and covers the V2530-A5. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287 is listed in Table 1, so removal and replacement is required at the next engine shop visit, no earlier than the later of the 100-cycle limit or 100 flight cycles after the effective date. No shop visit is recorded, so no deadline is currently fixed.
- **Stated timing:** At the next engine shop visit after 2025-10-29, but not before the later of (a) the hub reaching 100 cycles since new or (b) 100 flight cycles after the effective date (engine counter 25600). Once either has been reached, the next shop visit triggers removal. No shop visit is recorded, so there is no fixed deadline now.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** events: no engine shop visit is recorded after 2025-10-29; a future shop visit (with its qualifies_as_engine_shop_visit determination for AD 2025-19-13) would trigger the action
- **Missing fact:** ad_records[2025-19-13]: no operator AD status or AMOC claim supplied
- **Missing fact:** amoc_claims[2025-19-13]: none supplied
- **Note:** The hub's cycles since new are 90 on 2025-11-20 (60 on 2025-10-29). The engine counter advanced 30 cycles between those dates, consistent with the hub's 30-cycle gain, so the listed limit of 100 is 10 cycles away (component_cycles_remaining = 10).
- **Note:** The hub was installed 2025-09-30, before the effective date, so paragraph (h) does not apply to that installation.
- **Note:** The 100-flight-cycle window from the effective date runs to engine counter 25600 (25500 + 100). The 'whichever occurs later' wording combines with the hub limit; the hub reaches 100 cycles since new at about engine counter 25540, so the 25600 date is the later one. Removal is therefore tied to the next shop visit, which cannot be required before 25600.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0006 is not listed in Table 1, so it does not match.
- **Note:** This is a screening aid only and does not determine compliance status.
- **Unresolved locator:** 2025-18469 (g) Table 1, S/N PKLBSK9287, limit 100

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force on 2025-12-01 and the V2531-E5 engine is within its applicability. Both installed hubs match Table 1 entries, so removal and replacement is required at the next engine shop visit, with the deadline set by the 'whichever occurs later' wording. No shop visit has occurred, so no deadline can be fixed now.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the removal cycle limit or within 100 flight cycles after the effective date, whichever occurs later. The 1st-stage hub limit (4,800 cycles since new) is reached about 500 cycles after the 2025-12-01 reading. The 2nd-stage hub limit (4,000) is reached about 1,700 cycles after. No shop visit is recorded, so no firm deadline can be computed.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** events: no engine shop visit is recorded after 2025-10-29; whether and when the next shop visit occurs is unknown, and the deadline depends on it
- **Missing fact:** The AD's 'whichever occurs later' wording is unclear about whether the limit or 100 cycles is the later bound; this matters once a shop visit date is known
- **Note:** Cycles since new on 2025-12-01: 1st-stage hub 4,300, leaving 500 to its 4,800 limit; 2nd-stage hub 2,300, leaving 1,700 to its 4,000 limit. The smallest value is reported.
- **Note:** The engine gained 300 cycles from 2025-10-29 to 2025-12-01, and the 100 cycles after the effective date have already passed (engine at 30,300 vs 30,000), so the 100-cycle bound is not the controlling one for the later date.
- **Note:** The record has no ad_records or amoc_claims for this AD, and none are assumed.
- **Note:** This is a screening result, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows PKLBSS9200 (4,800) and PKLBST5005 (4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is within the AD applicability and the AD has been in force since 2025-10-29. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in Table 1 with a 6,200 cycles-since-new limit, so removal is due at the next engine shop visit. The HPT 2nd-stage hub S/N is unknown, so its status cannot be determined.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after 2025-10-29, at or before the later of reaching 6,200 cycles since new or 100 flight cycles after the effective date. No shop visit is recorded, so no deadline has been triggered yet. The 100-cycle floor falls at engine flight cycles 50,100, which is already passed. The 6,200-cycle limit is about 3,700 cycles away, so the shop visit controls.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** installed_components[HPT 2nd-stage hub].serial_number
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new
- **Missing fact:** events: no engine shop visit recorded since 2025-10-29; any future shop visit must be assessed against the AD (i)(2) definition
- **Missing fact:** amoc_claims[2025-19-13]: none claimed in the record
- **Note:** The 1st-stage hub had 2,000 cycles since new at 2025-10-29 and 2,500 at 2026-03-10, consistent with the engine's 500 cycles over the same period. Remaining cycles to the 6,200 limit are 6,200 - 2,500 = 3,700.
- **Note:** Because the 100-cycle floor has passed and the cycle limit has not been reached, the 'whichever occurs later' wording makes the cycle limit the later point. No shop visit has been recorded, so the action is event-driven. A reviewer should confirm that reading.
- **Note:** The HPT 2nd-stage hub could match one of the four listed 2A4802 serial numbers (limits 3,900 to 6,000 cycles since new). Its serial number and cycles since new must be established before it can be cleared.
- **Note:** This is a screening aid only and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 1st-stage hub 2A5001 PKLBST7489, 6,200

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2522-A5 is a listed model, so AD 2025-19-13 (in force since 2025-10-29) applies. The record has no installed-component data, so whether the engine carries a Table 1 hub, and whether any action is triggered, cannot be determined.
- **Missing fact:** installed_components[HPT 1st-stage hub]
- **Missing fact:** installed_components[HPT 2nd-stage hub]
- **Missing fact:** installed_components[HPT 1st-stage hub].part_number and serial_number
- **Missing fact:** installed_components[HPT 2nd-stage hub].part_number and serial_number
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new
- **Missing fact:** events: engine shop visit history after 2025-10-29, including whether any event meets the AD's engine shop visit definition
- **Missing fact:** engine flight-cycle counter (engine.flight_cycles) at 2025-10-29 and at the question date
- **Missing fact:** ad_records[2025-19-13]: operator-recorded status of this AD
- **Note:** An empty installed_components list does not show that the hubs are absent or unaffected.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The supplied NPRM 2025-10764 is superseded by the final rule; the final rule governs.
- **Unresolved locator:** 2025-18469 (g) Table 1

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made for AD 2025-19-13.
- **Note:** No determination is made on applicability or action for this engine because the model is outside the supported scope.
- **Note:** The installed hub P/N and S/N appear in the AD table, but that is not evaluated here because the engine model is unsupported.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 (effective 2026-09-24, in force on 2026-10-05) applies. Replacement is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no such event is recorded.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no deadline otherwise.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** Whether the installed blade set has already been replaced or modified to an eligible P/N (6C8368, 6C8403, later approved, or 6A8353-001/6A8688-001) per SB V2500-ENG-72-0716; the record shows P/N 6A8353 only, with no serial tracking at set level (installed_components[3rd stage HPC rotor blade set].serial_number).
- **Note:** The question names document 2026-16954; the later correction 2026-18423 only fixes a typo in (g) and does not change the result.
- **Note:** The events list is empty, so no shop visit after the effective date is recorded; this is a screening result only, not a compliance determination.
- **Note:** The 2026-16954 preamble says replacement per SB V2500-ENG-72-0716 changes the part numbers to eligible ones; the record does not show this was done.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The V2533-A5 is a supported model, but the record shows the 3rd stage HPC rotor blade set at P/N 6C8368, which is not P/N 6A8353 or 6A8688, so the AD 2026-17-03 applicability condition is not met on the supplied facts.
- **Note:** Record gives one P/N for the blade set and does not track serials at set level; individual blades within the set are not itemized. If any individual blade of P/N 6A8353 or 6A8688 were installed, this result would change.
- **Note:** Correction 2026-18423 only restores the word 'blade' in paragraph (g); it does not change applicability.
- **Note:** The record has no events, so no shop visit is shown.
- **Unresolved locator:** 2026-16954 (h)(1) (h)(1)(i)

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC blade set P/N 6A8688, so AD 2026-17-03 applies. The visit was inducted 2026-09-14, before the 2026-09-24 effective date, and paragraph (g) only reaches shop visits after the effective date, so the blade exposure on 2026-09-30 does not trigger replacement now.
- **Stated timing:** No deadline now. Paragraph (g) is tied to the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed. The visit inducted 2026-09-14 is not that visit.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Whether the blades were replaced with parts eligible for installation (paragraph (h)(1)) during the 2026-09-14 visit; installed_components[3rd stage HPC rotor blade set].part_number[2026-09-30] still shows 6A8688.
- **Missing fact:** Whether the induction date of 2026-09-14 is accurate and whether the engine was re-inducted after 2026-09-24; events[shop_visit_induction].
- **Note:** The question names 2026-16954, but correction 2026-18423 amends paragraph (g) by adding the omitted word 'blade'. The result is the same under either text.
- **Note:** The preamble says the AD is not intended to require compliance from engines inducted before the effective date. The exposure on 2026-09-30 occurred after the effective date but within a visit inducted before it.
- **Note:** This is a screening result, not a compliance determination. The engine still shows P/N 6A8688 blades, so the obligation remains for a later qualifying shop visit unless the blades are replaced with eligible parts.
- **Unresolved locator:** 2026-16954 preamble Request To Revise Compliance Language

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 engine has 3rd stage HPC rotor blades P/N 6A8353, so AD 2026-17-03 applies and is in force (effective 2026-09-24). The 2026-10-01 shop visit came after the effective date, but no 3rd-stage blade was removed from the drum, so the blades were not exposed; replacement is required only at a future shop visit where a blade is exposed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 in which a 3rd stage HPC rotor blade is exposed (removed from the stage 3-8 drum); no deadline otherwise.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** Whether the record's statement that no 3rd-stage blade was removed during the 2026-10-01 to 2026-10-04 visit is confirmed by shop work records (events[2026-10-02] detail)
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].serial_number: individual blade serial numbers or confirmation that all blades in the set are P/N 6A8353 (not tracked at set level)
- **Note:** The 2026-10-01 induction qualifies as an engine shop visit after the effective date, but the AD trigger also needs a blade exposure, and the record shows the rotor was exposed for inspection with no blade removed.
- **Note:** The original 2026-16954 text of (g) said 'the 3rd stage HPC rotor is exposed'; the correction 2026-18423 changed this to 'rotor blade'. Under either wording the record shows no blade removal, so the result is the same, but the corrected wording ties the trigger to blade exposure.
- **Note:** The operator's record states the visit qualifies as an engine shop visit; this matches the AD's definition in (h)(3). That claim is the operator's assertion.
- **Note:** This is a screening result, not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The document is a proposed rule (NPRM) that is not yet in force, so it cannot require action. The V2527E-A5 engine has 3rd stage HPC rotor blades with P/N 6A8353, which would fall within the proposed applicability if the AD is adopted as written.
- **Stated timing:** If adopted as proposed, replacement of the full blade set would be due at the next 3rd stage HPC rotor blade exposure (any blade removed from the HPC stage 3 to 8 drum) after the effective date. No deadline applies now.
- **Missing fact:** Whether the final rule is issued and its effective date and any changes from the proposal.
- **Missing fact:** Whether the installed blades are the unmodified P/N 6A8353 or already modified to 6A8353-001 (record shows only 6A8353; modification status would be shown at installed_components[3rd stage HPC rotor blade set].part_number).
- **Note:** Proposed rule only; no action is required while it is not in force.
- **Note:** The engine record has no events, so no blade exposure is recorded.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-20088 (c) Applicability
- **Unresolved locator:** 2025-20088 (g) Required Actions
- **Unresolved locator:** 2025-20088 (h)(2) Definitions
- **Unresolved locator:** 2025-20088 (h)(1) Definitions
- **Unresolved locator:** 2025-20088 preamble Header

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 is in force (effective 2025-10-10) and applies to the V2527-A5 model. The record shows neither the V2500-A5 TLM ALS paragraph B.1 nor the approved maintenance program yet incorporates table 1, and the 90-day period after the effective date ends 2026-01-08, so the revisions are required by then.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e., by January 8, 2026, for both the TLM ALS paragraph B.1 revision under (g)(1) and the air carrier maintenance program revision under (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** installed_components[HPT Stage 1 Hub]
- **Missing fact:** installed_components[HPT Stage 2 Hub]
- **Note:** The applicability is by engine model, so the missing hub records do not affect applicability or the (g) revision requirement. Part numbers matter only for what the table 1 inspections cover when the parts are exposed.
- **Note:** The required actions are document revisions. The inspection tasks themselves are performed under other regulations at piece-part exposure.
- **Note:** The 90-day period after 2025-10-10 ends 2026-01-08. No engine flight-cycle deadline applies.
- **Note:** The operator record shows air_carrier_operation yes, so (g)(2) applies in addition to (g)(1).
- **Note:** This is a screening aid only and not a compliance determination.
- **Unresolved locator:** 2025-17066 (g)(1) Table 1 to paragraph (g)

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is a listed model, so AD 2025-17-16 applies and is in force on 2025-11-15 (effective 2025-10-10). The paragraph (g)(1) ALS revision deadline of 90 days after the effective date has passed; whether the record shows it was done, and whether (g)(2) applies, cannot be determined from the supplied record.
- **Stated timing:** Paragraph (g)(1) and, for air carrier operations, (g)(2): within 90 days after October 10, 2025, i.e. by January 8, 2026. This is a calendar deadline, not a flight-cycle deadline.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** operator.air_carrier_operation (unknown; determines whether paragraph (g)(2) applies)
- **Missing fact:** ad_records[2025-17-16] (no record of whether the paragraph (g)(1) TLM ALS revision and any (g)(2) program revision were done)
- **Missing fact:** installed_components[HPT Stage 1 Hub] (P/N 2A5001 presence not recorded)
- **Missing fact:** installed_components[HPT Stage 2 Hub] (P/N 2A4802 presence not recorded)
- **Note:** The AD requires documentation revisions rather than part replacement, so the installed hub part numbers do not affect applicability, which depends on engine model. The record has no installed components or events.
- **Note:** The (g)(1)/(g)(2) deadline is January 8, 2026, which is after the question date. The record does not show whether the revisions are already done.
- **Note:** The final rule's Table 1 cites TASK 72-45-31-200-009 for the HPT Stage 2 Hub; the NPRM's TASK 72-45-11-200-009 was corrected.
- **Note:** This is a screening result, not a compliance determination.
- **Unresolved locator:** 2025-17066 (g)(1) Table 1 to paragraph (g)

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is a listed model and its HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 matches Table 1 (limit 6,000 cycles since new). The AD is published but not effective until 2025-10-29, so no action is required yet; removal would be due at the next engine shop visit after the effective date, or within 100 flight cycles after the effective date if that is later.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding 6,000 cycles since new or within 100 flight cycles from the effective date, whichever occurs later. No deadline arises until such a shop visit. The AD is not yet effective on the question date.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** Engine total flight-cycle counter at the effective date (2025-10-29), needed to compute the 100-flight-cycle point; not in the record (engine.flight_cycles_since_new[2025-10-29])
- **Missing fact:** Whether and when a future engine shop visit occurs after 2025-10-29 (events)
- **Note:** Component cycles remaining = 6,000 - 990 = 5,010 for the 2nd-stage hub, as of the record snapshot.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0018 is not in Table 1 and is not matched.
- **Note:** The NPRM 2025-10764 is superseded by the final rule; its text is the same in substance.
- **Note:** The record has no events, so no shop visit has occurred or is recorded.
- **Note:** Because the limit is far off, the 100-flight-cycle-from-effective-date term would likely be the later one, but this depends on the engine cycle count at the effective date and on the shop visit timing.
- **Note:** This is a screening aid only, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 2nd-stage hub 2A4802 PKLBSR2100, 6,000

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and covers the V2531-E5. The HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches table 1 (limit 4,800 cycles since new). Its limit was already exceeded at the effective date, so removal is due at the next engine shop visit, or within 100 flight cycles after the effective date if that is later.
- **Stated timing:** At the next engine shop visit after 2025-10-29. Because the cycle limit was already exceeded at the effective date, the 'whichever occurs later' clause makes the 100-flight-cycle point the later one. The 100-cycle point is engine flight cycle 60100. No shop visit is recorded yet.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** events: no engine shop visit is recorded, so the date of the next shop visit is unknown; events[] would need an entry with qualifies_as_engine_shop_visit for AD 2025-19-13
- **Missing fact:** installed_components[HPT 2nd-stage hub].serial_number: SYN-HUB2-0019 does not match any table 1 serial number, so it is not matched, but it is a synthetic identifier and should be confirmed against the physical part
- **Missing fact:** amoc_claims[2025-19-13]: none recorded, so no alternative method of compliance is claimed
- **Note:** The cycles-since-new reading at the effective date was 4950, against a limit of 4800: 150 cycles over. The record's current figure of 4990 is 190 over, giving -190 now; the -150 reported is the figure at the effective date.
- **Note:** The 2nd-stage hub is not matched to the table on serial number, so no action is triggered for it from the supplied facts.
- **Note:** The NPRM 2025-10764 is superseded by the final rule; this answer relies on the final rule.
- **Note:** The engine record shows 60000 cycles at the effective date and 60040 on 2025-11-05, so 40 cycles have been flown since the effective date and 60 of the 100 remain.
- **Unresolved locator:** 2025-18469 (g) Table 1, PKLBSS9200 row, limit 4,800

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (document 2021-11960) was in force on 2022-03-01 and the V2533-A5 is a listed model, but the record does not show that the installed disk serial numbers appear in the NMSB Appendix A tables, so applicability cannot be decided. Also, AD 2022-02-09 (effective 2022-03-15) will supersede this AD, but it was not yet effective on the question date.
- **Stated timing:** If the disks are listed, paragraphs (g)(1) and (g)(2) require the USI at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 FCs since 2021-07-13, whichever occurs first. The record cannot show where that point falls.
- **Missing fact:** Whether serial number SYN-DISK1-0020 is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713, Revision 1 (content of the service bulletin, which was not provided)
- **Missing fact:** Whether serial number SYN-DISK2-0020 is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713, Revision 1 (content of the service bulletin, which was not provided)
- **Missing fact:** installed_components[HPT 1st-stage disk].flight_cycles_since_2021-07-13 (cycles accumulated since the effective date)
- **Missing fact:** installed_components[HPT 2nd-stage disk].flight_cycles_since_2021-07-13 (cycles accumulated since the effective date)
- **Missing fact:** ad_records[2021-11-15] (whether the USI was already done, with the date and cycle count)
- **Missing fact:** engine.flight_cycles_since_new[2022-03-01] (engine flight-cycle counter, needed to compute a deadline)
- **Note:** The part numbers match the P/Ns named in paragraph (c), but the serial numbers could not be checked against the NMSB tables, so no parts are listed as matched.
- **Note:** The events list is empty. An empty list is not evidence that no shop visit occurred.
- **Note:** The superseding AD 2022-02-09 takes effect 2022-03-15 and has different compliance wording, so it should be reviewed ahead of that date.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2021-11960 (c) (c)(1) and (c)(2)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 is published but not effective until 2022-03-15, so it cannot require action on 2022-03-01. The engine model is covered and the disk part numbers match, but the listed serial numbers in the service bulletin appendices were not supplied, so applicability cannot be decided.
- **Stated timing:** No action is required before the 2022-03-15 effective date. If the disks are listed, the (g)(1)/(g)(2) inspection is due by the Figure 1 compliance time or within 10 FCs after 2022-03-15, whichever is later. The Figure 1 content was not provided.
- **Missing fact:** Whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed in Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 or V2500-E5-72-0015 Rev 1 (content of the service bulletin was not supplied)
- **Missing fact:** Whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed in Appendix A, Table 2 of the same service bulletins (content not supplied)
- **Missing fact:** Figure 1 to paragraph (g)(1) compliance time (image not included in the text)
- **Missing fact:** installed_components[HPT 1st-stage disk].flight_cycles_since_new or cycles accumulated (not in record)
- **Missing fact:** installed_components[HPT 2nd-stage disk].flight_cycles_since_new or cycles accumulated (not in record)
- **Missing fact:** Engine flight-cycle counter at the effective date (not in record)
- **Note:** The record shows no events, so no shop visit or prior USI is recorded. This does not show that no action was done.
- **Note:** The AD supersedes 2021-11-15, which became effective 2021-07-13 and may bind this engine until 2022-03-15 if the disks are listed. That AD was not evaluated here, as only 2022-02574 was asked about.
- **Note:** This is a screening aid only and not a compliance determination.
- **Unresolved locator:** 2022-02574 (c) (c)(1) and (c)(2)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 is in force and the V2530-A5 is a listed model with the correct part numbers (2A5001 and 2A4802). Applicability cannot be decided because the NMSB Appendix A tables were not supplied, so the disk serial numbers cannot be checked against them.
- **Missing fact:** Content of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Revision 1 (to check HPT 1st-stage disk S/N SYN-DISK1-0021); not part of the engine record
- **Missing fact:** Content of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Revision 1 (to check HPT 2nd-stage disk S/N SYN-DISK2-0021); not part of the engine record
- **Missing fact:** Compliance time in Figure 1 to paragraph (g)(1), which is an image not included in the text
- **Missing fact:** installed_components[HPT 1st-stage disk].flight_cycles_since_new
- **Missing fact:** installed_components[HPT 2nd-stage disk].flight_cycles_since_new
- **Missing fact:** ad_records[2022-02-09]
- **Missing fact:** Whether the USI of either disk has already been done (no ad_records entry or events)
- **Note:** No disk is matched to a listed part because the serial-number lists were not provided.
- **Note:** The record has no flight-cycle counts, no AD records and no events, so no deadline can be computed.
- **Note:** If a serial number is found in the NMSB tables, the (g)(1)/(g)(2) USI would apply, with timing set by Figure 1.
- **Note:** This is a screening aid only and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2022-02574 (c) (c)(1) and (c)(2)
- **Unresolved locator:** 2022-02574 (g)(1) (g)(1) and (g)(2)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine has an HPT 1st-stage disk P/N 2A5001, S/N PKLBSH1829, which is listed in paragraph (c)(1), so the AD applies and a USI is required within 10 flight cycles after the July 19, 2021 effective date.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021 (engine was at 33000 cycles on that date), so by 33010 engine flight cycles. 4 cycles have been accumulated as of 2021-07-20.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** Whether the USI of the HPT 1st-stage disk has already been done per NMSB V2500-ENG-72-0713 (paragraph (f) 'unless already done'); the record has no ad_records or events showing it.
- **Missing fact:** Table 2 to paragraph (g)(2) is an image not provided, so it cannot be confirmed whether the 2nd-stage disk is listed there; its S/N SYN-DISK2-0022 does not match any (c)(2) serial number.
- **Missing fact:** Table 1 to paragraph (g)(1) is an image not provided; it is not confirmed that the 1st-stage disk is listed there, though (c)(1) lists its serial number.
- **Note:** Cycle count at the effective date (33000 on 2021-07-19) is used as the baseline; the deadline is 33010 cycles. Engine at 33004 on 2021-07-20, so 6 cycles remain before that limit.
- **Note:** The 10 flight cycles run from the effective date, not from the question date.
- **Note:** Screening aid only; not a compliance determination.
- **Expected missing fact (judge on meaning):** table 1 to paragraph (g)(1) content (image-only; transcription decided in E3)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 accomplishment instructions (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-022/2021-11960: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2533-A5 is a listed model and the AD is in force on 2021-07-20, but the record does not show whether the installed HPT disk serial numbers appear in the Appendix A tables of the service bulletins, which are not supplied. Applicability and any (g)(1)/(g)(2) action therefore cannot be decided.
- **Missing fact:** Content of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Revision 1 (was not provided): whether HPT 1st-stage disk S/N PKLBSH1829 is listed.
- **Missing fact:** Content of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Revision 1 (was not provided): whether HPT 2nd-stage disk S/N SYN-DISK2-0022 is listed.
- **Missing fact:** Part-level flight cycle accumulation of each HPT disk since 2021-07-13 (installed_components[HPT 1st-stage disk].cycles_since_effective_date and installed_components[HPT 2nd-stage disk].cycles_since_effective_date); the record has only engine cycle readings.
- **Missing fact:** Whether the engine has had an engine shop visit since 2021-07-13 (events list is empty, so none recorded, but confirm events).
- **Note:** Part numbers match the AD's P/Ns (2A5001 and 2A4802), but the serial numbers cannot be checked without the Appendix A tables.
- **Note:** If a disk is listed, the 3,200-FC limit counts from 2021-07-13 on that disk. Engine cycles at 2021-07-19 and 2021-07-20 (33,000 and 33,004) do not establish the engine count on the effective date, so a deadline cannot be computed from the record.
- **Note:** The 2nd-stage disk serial number is synthetic-looking and may not be a real listed serial number; check it against the table.
- **Note:** This is a screening aid only and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)
- **Unresolved locator:** 2021-11960 (c) (c)(1) and (c)(2)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and applies to the V2527M-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 matches table 1 (limit 6,000 cycles since new), so replacement is due at the next engine shop visit; no shop visit is recorded, so no deadline is fixed now.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 6,000 cycles-since-new removal limit or within 100 flight cycles after the effective date, whichever occurs later. The hub is already past the 100-cycle window, so the later date is set by the 6,000 limit (see notes). No shop visit is recorded.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** installed_components[HPT 2nd-stage hub].cycles_since_new[2026-10-06] - the hub's cycles since new at the question date is unclear: 3500 is shown without a date, while the 2025-10-29 reading was 1000 and the engine flew 2500 cycles since then. 1000+2500=3500 is consistent with the 3500 figure.
- **Missing fact:** events[engine shop visit] - no engine shop visit is recorded, so the trigger event has not been shown to occur.
- **Missing fact:** installed_components[HPT 1st-stage hub].serial_number - S/N SYN-HUB1-0023 is not in table 1, so the 1st-stage hub is not matched; no further fact is needed unless the record is wrong.
- **Missing fact:** ad_records[2025-19-13] - no record of this AD's status is supplied.
- **Missing fact:** The record cites AD 2025-17-16 for the maintenance program revision, which is not the AD in question and was not supplied.
- **Note:** The hub is at 3,500 cycles since new against the 6,000 limit, leaving 2,500 cycles. The 'whichever occurs later' wording means the required action falls at the next shop visit after the later of the limit being reached or 100 flight cycles after the effective date; this was not computed as a fixed engine-cycle deadline because the shop visit is an event.
- **Note:** The 100-flight-cycle window after 2025-10-29 ended at engine cycle 20,100. The removal limit is reached when the hub hits 6,000 cycles since new, which at 3,500 cycles at 22,500 engine cycles would be around engine cycle 25,000 at the same usage rate. Whether this sets a deadline on a shop visit before that point is a reading of paragraph (g) a reviewer should confirm.
- **Note:** The maintenance program revision cites AD 2025-17-16, not AD 2025-19-13, and does not address this AD's hub requirement.
- **Note:** The 3rd stage HPC rotor blade set is not a part listed in this AD.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 2nd-stage hub PKLBSR2100, 6,000

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (as corrected by 2026-18423) is in force on 2026-10-06 and applies to this V2527M-A5 engine because the installed 3rd stage HPC rotor blade set is P/N 6A8688. Replacement is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no deadline is set otherwise.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline otherwise.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Whether any engine shop visit (induction into the shop for maintenance) has occurred since 2026-09-24 and whether a 3rd stage HPC blade was removed from the drum; events[] has no shop-visit entry.
- **Missing fact:** Confirmation that the installed blades are still P/N 6A8688 (the set is not serial-tracked) and that none are already modified to 6A8688-001 or replaced with eligible P/N: installed_components[3rd stage HPC rotor blade set].serial_number
- **Missing fact:** installed_components[3rd stage HPC rotor blade set].installed_at
- **Note:** The record's maintenance program revision relates to AD 2025-17-16, a different directive, and is not an AMOC or evidence about this AD.
- **Note:** The HPT hub components are not listed in this AD and are irrelevant to it.
- **Note:** No ad_records or amoc_claims entry exists for this AD.
- **Note:** The AD text offers no cycle-based limit, so latest engine flight cycles and component cycles remaining cannot be computed.
- **Note:** This is a screening aid only, not a compliance determination.
- **Unresolved locator:** 2026-16954 (a) Effective date
- **Unresolved locator:** 2026-18423 (g) Correction

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-17-16 is in force (effective 2025-10-10) and covers V2527M-A5 engines. The 90-day revision deadline was 2026-01-08. The record shows the TLM ALS and the approved program were revised on 2025-12-01 to incorporate table 1, so no further action is triggered by the supplied facts.
- **Stated timing:** The 90-day revision window after the 2025-10-10 effective date ended 2026-01-08. The record shows the revision was done 2025-12-01, inside that window, so no deadline remains open.
- **Missing fact:** The content of Revision 48 and the revised TLM ALS is not supplied, so it cannot be confirmed that they incorporate table 1 tasks 72-45-11-200-006 and 72-45-31-200-009 into paragraph B.1 of the Maintenance Scheduling section.
- **Note:** The AD requires only the ALS and program revisions. The inspection tasks themselves are performed at piece-part exposure under the revised program and other regulations, not directly by this AD.
- **Note:** The record's cycles_since_new figures for the HPT 2nd-stage hub are inconsistent: 1000 at 2025-10-29 against 3500 now, though the engine accrued 2500 cycles since then. They do not change this screening, since the AD sets no hub cycle limit.
- **Note:** Revision of the approved program and TLM ALS is an operator-recorded event and not independently verified. This screen is not a compliance determination.
- **Note:** The engine record has no applicable AMOC claims.
- **Unresolved locator:** 2025-17066 preamble DATES
- **Unresolved locator:** 2025-17066 (g)(1) Table 1 to paragraph (g)
- **Unresolved locator:** 2025-17066 (i) (i)(2)

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine is a V2528-D5 and falls within AD 2025-19-13 applicability, which is in force on 2026-10-06. The installed HPT 2nd-stage hub S/N PKLBST5011 is not a listed 2nd-stage hub (that S/N is listed only as a 1st-stage hub, P/N 2A5001), and the 1st-stage hub S/N is not listed, so no paragraph (g) removal is triggered now.
- **Note:** The 2nd-stage hub S/N PKLBST5011 matches a table 1 S/N only for the 1st-stage hub P/N 2A5001, whereas the installed part is P/N 2A4802 in the 2nd-stage position, so P/N and S/N do not both match any row.
- **Note:** The installed 1st-stage hub S/N SYN-HUB1-0024 is not in table 1.
- **Note:** This is a screening result only, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows for HPT 1st-stage and 2nd-stage hubs

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model CFM56-5B4/3 is not one of the supported IAE V2500 models, so no applicability determination is made for AD 2025-17-16.
- **Note:** No determination is made about this engine against the directive.
- **Note:** The directive's effective date of 2025-10-10 is before the question date of 2026-10-06, so it is in force on that date.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and the V2530-A5 engine is within its applicability. Installed HPT 1st-stage hub 2A5001 PKLBST7489 is listed in Table 1 with a 6,200-cycle removal limit, so removal and replacement is required at the next engine shop visit; no shop visit is recorded since the effective date.
- **Stated timing:** At the next engine shop visit after 2025-10-29, which is the later of the hub reaching 6,200 cycles since new and 100 flight cycles after the effective date. With the hub at 3,000 CSN on 2025-10-29 and engine flight cycles of 20,000, the 100-cycle window ended at engine flight cycle 20,100, which has passed. The limit is reached about 3,200 hub cycles after 2025-10-29, around engine flight cycle 23,200 if the hub accrues cycles at the engine rate. No deadline applies unless and until a shop visit occurs.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** events[engine shop visit]: no engine shop visit after 2025-10-29 is recorded; whether any future event qualifies under paragraph (i)(2) must be confirmed
- **Missing fact:** installed_components[HPT 1st-stage hub].cycles_since_new[2026-03-01]: the current value of 3600 is the only snapshot reading, and it is consistent with the 2025-10-29 reading plus 600 engine cycles
- **Missing fact:** installed_components[HPT 2nd-stage hub].serial_number: SYN-HUB2-0026 is not a listed S/N, so the 2nd-stage hub is not matched. Confirm the record is accurate
- **Missing fact:** ad_records[2025-19-13]: no operator AD record or AMOC claim was supplied
- **Note:** Remaining cycles are 6,200 minus 3,600 = 2,600, as of the 2026-03-01 snapshot.
- **Note:** The 2024 blend repair and repeat ultrasonic inspection of the hub do not change its Table 1 listing, and the AD has no provision excusing a hub for them.
- **Note:** The NPRM 2025-10764 is superseded by the final rule and was not used for the obligations.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 row PKLBST7489, 6,200

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
- **Summary:** The V2527-A5 is within the applicability, and its HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches table 1 (limit 4,800 CSN). The removal is due at the next engine shop visit after 2025-10-29, no earlier than the later of the 4,800 CSN limit or 100 flight cycles after the effective date. No shop visit is recorded, so no deadline is fixed now.
- **Stated timing:** At the next engine shop visit after 2025-10-29, but not before the hub exceeds 4,800 CSN or 100 flight cycles after the effective date, whichever is later. The 100-cycle point is engine cycle 15,100. The hub is at 4,750 CSN, so about 50 cycles remain before the limit, and engine cycle 15,300 would be the 4,800 CSN point if it is used. If a shop visit occurs before that, the later threshold governs, i.e. engine cycle 15,300.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** events: no engine shop visit is recorded after 2025-10-29; future shop visit event needed
- **Missing fact:** AMOC approval: no FAA approval letter on file (amoc_claims[AD 2025-19-13].approval_reference)
- **Missing fact:** installed_components[HPT 2nd-stage hub].serial_number: SYN-HUB2-0027 is not on the table; confirmed not listed, but record is synthetic and should be verified against the physical part
- **Note:** The claimed AMOC (5,300 CSN) has no approval reference or FAA letter and cannot be relied on; the 4,800 CSN limit from the table was used.
- **Note:** Hub CSN at 2025-10-29 was 4,500, and 250 engine cycles since then gives 4,750, consistent with the current reading.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0027 does not match any table 1 entry, so it triggers no action under (g).
- **Note:** This is a screening aid only, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 row PKLBSS9200, 4,800

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force (effective 2025-10-29) and applies to the V2524-A5 engine. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 is listed in table 1, so removal is required at the next engine shop visit; no shop visit is recorded, so no deadline is fixed yet.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 4,000 cycles-since-new removal limit or within 100 flight cycles after the effective date, whichever occurs later. No shop visit is recorded, so no fixed deadline can be computed.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** installed_components[HPT 1st-stage hub].serial_number is a synthetic S/N (SYN-HUB1-0028) that does not match the table 1 hub S/Ns, so it is not matched; confirm the actual hub identity against the table.
- **Missing fact:** events: no shop visit is recorded; any future engine shop visit, and whether it meets the paragraph (i)(2) definition, would trigger removal.
- **Note:** The operator's record marks the AD not applicable because 'no affected hubs installed'. This conflicts with the AD text: applicability is by engine model, and the 2nd-stage hub S/N PKLBST5005 is listed.
- **Note:** The hub has 1,400 cycles since new against the 4,000 limit, leaving 2,600 cycles. The 100-cycle-from-effective-date alternative ends at engine cycle 8,100 (8,000 on 2025-10-29 plus 100), which is already passed (8,400). The 'whichever occurs later' wording therefore does not create a fixed deadline; the action remains tied to the next shop visit.
- **Note:** The 1st-stage hub S/N is not on the table; this is not proof it is unaffected, as the record uses a placeholder identifier.
- **Note:** The hub's installed_at date (2025-06-03) predates the AD, and its cycles-since-new count (1,000 at 2025-10-29, 1,400 now) is consistent with the engine's 400 cycles.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 2nd-stage hub 2A4802 PKLBST5005, limit 4,000

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is a listed model and the AD was in force on 2026-02-01. The HPT 1st-stage hub S/N PKLBSK9287 matches table 1 by serial number, but its installed P/N is 2A5001-01 versus listed 2A5001, so the match needs review. The 2nd-stage hub S/N is not listed.
- **Stated timing:** If the 1st-stage hub is confirmed as the listed part: at the next engine shop visit after 2025-10-29, before exceeding the 100-cycle removal limit or within 100 flight cycles after 2025-10-29, whichever occurs later. The hub is already past its 100-cycle limit, so the 100-cycles-from-effective-date prong would govern. The engine cycle count on 2025-10-29 is not in the record, so no deadline can be computed.
- **Missing fact:** Whether installed P/N 2A5001-01 is the same part as listed P/N 2A5001 (a dash-number variant); confirm with the manufacturer or FAA. Settled by installed_components[HPT 1st-stage hub].part_number.
- **Missing fact:** Engine flight-cycle counter as of the effective date 2025-10-29 (engine.flight_cycles[2025-10-29]), needed to compute the 100-cycle deadline.
- **Missing fact:** Whether any engine shop visit has occurred since 2025-10-29; the events list is empty, which does not by itself confirm none occurred (events).
- **Missing fact:** Whether the shop visit is a trigger under the AD definition; none is recorded so far.
- **Note:** The hub shows 2400 cycles since new against a limit of 100, so 2300 cycles past the limit if the listing applies.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0029) is not in table 1 and so is not affected.
- **Note:** The AD ties action to an engine shop visit; the record shows no events, so if the 1st-stage hub match is confirmed, action is tied to a future shop visit.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, HPT 1st-stage hub 2A5001 PKLBSK9287, limit 100

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
