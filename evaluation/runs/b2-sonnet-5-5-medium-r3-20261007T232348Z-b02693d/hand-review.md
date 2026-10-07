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
- **Summary:** The engine is a V2527-A5 and the AD has been in force since 2025-10-29. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in table 1 with a 5,500 cycles-since-new removal limit. Removal and replacement is required, and the latest point is 45,050 engine flight cycles.
- **Stated timing:** Remove and replace at the next engine shop visit after 2025-10-29, which must come before the later of the hub reaching 5,500 cycles since new or 100 flight cycles after the effective date. The 5,500-cycle limit is the later of the two, so the hub must be replaced no later than about 2,400 more cycles from the 2026-09-26 reading, at engine flight cycle 45,050.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0001 has a listed P/N (2A4802) but its S/N is not listed in table 1, so it is not matched.
- **Note:** The record shows no events, so no engine shop visit after the effective date is recorded. Paragraph (g) can be read as requiring the removal at a shop visit, and the 45,050 cycle figure is the latest point by which the hub must be removed under the cycle limit. If a shop visit occurs earlier, removal is due at that visit.
- **Note:** The hub cycles-since-new values are consistent with the engine cycle readings: 1,650 on 2025-10-29 plus 1,450 cycles gives 3,100 on 2026-09-26.
- **Note:** This is a screening aid and not a compliance determination. No AMOC claims or AD records were supplied.

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2533-A5 is within the AD applicability and the AD is in force. Neither installed hub's P/N and S/N matches Table 1 (1st-stage S/N PKLBST5012 is not listed; PKLBST5011 is), so the paragraph (g) removal is not triggered on the supplied record.
- **Note:** The 1st-stage hub serial PKLBST5012 differs by one digit from listed PKLBST5011; a reviewer may wish to verify the serial against source records for transcription error.
- **Note:** The NPRM 2025-10764 was superseded by the final rule and is not relied on.
- **Note:** The record has no events and no AD or AMOC claims. This is a screening result, not a compliance determination.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2524-A5 is within the in-force AD's applicability. The HPT 1st-stage hub S/N and cycles since new are unknown, so a match to table 1 cannot be ruled in or out. The HPT 2nd-stage hub S/N is not listed, so it is not an affected part.
- **Missing fact:** HPT 1st-stage hub P/N 2A5001 matches the listed part number, but its S/N is unknown. It cannot be compared with the four listed S/Ns (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489), so whether it is affected is undetermined.
- **Missing fact:** Cycles since new for the 1st-stage hub are unknown. If the S/N matches a listed hub, this is needed to compare against the removal cycle limit (100 to 6,200) and compute any deadline.
- **Missing fact:** The engine's current flight-cycle counter and the shop visit history after 2025-10-29 would be needed to compute a deadline. The events list is empty, so no shop visit is recorded.
- **Note:** A missing or unknown S/N is not evidence that the 1st-stage hub is unaffected. Verify the S/N from records or the part itself.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) does not match any listed S/N, so it is not affected under table 1.
- **Note:** If the 1st-stage hub S/N matches a listed one, action falls at the next engine shop visit after 2025-10-29, before exceeding the removal cycle limit or within 100 flight cycles of the effective date, whichever is later. Some listed hubs may already be past their limits.
- **Note:** The NPRM 2025-10764 was superseded by the final rule 2025-18469, which has the same text.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for this directive.
- **Note:** No applicability determination is made for engine model PW1133G-JM.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and the engine model is covered. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed (limit 3,900 cycles since new) and the engine was inducted into a qualifying shop visit on 2025-11-12, so removal and replacement is triggered at that shop visit.
- **Stated timing:** Paragraph (g) requires removal and replacement at the next engine shop visit after 2025-10-29 that occurs at or after the later of the removal cycle limit or 100 flight cycles after the effective date. The hub is at 1,040 cycles since new, below the 3,900 limit, so the later date is 100 flight cycles after the effective date, i.e. engine flight cycle 18100. The shop visit induction at 18040 is before that point. Replacement is due by engine flight cycle 18100 at the latest, and the hub is in the shop now.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The shop visit qualification is only asserted by the operator record. It needs confirmation that the induction met the (i)(2) definition, i.e. separation of major mating flanges and not transport-only or field maintenance in lieu of on-wing work.
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0005 is not in table 1, so it is not matched. Confirm that the serial number is recorded correctly.
- **Note:** The hub has 1,040 cycles since new against the limit of 3,900, leaving 2,860.
- **Note:** The latest cycle is 18000 + 100 = 18100, using the engine reading at the effective date.
- **Note:** The NPRM 2025-10764 is superseded by the final rule and is not relied on.
- **Note:** No AMOC is claimed in the record.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 is within the AD's applicability, and its HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287 is listed in table 1 with a 100-cycle removal limit. Removal is required at the next engine shop visit after 2025-10-29, on or after the later of the 100-cycle limit and 100 flight cycles after the effective date; no shop visit is recorded, so no fixed deadline exists yet.
- **Stated timing:** At the next engine shop visit after 2025-10-29, but not before the later of: the hub reaching 100 cycles since new, or 100 flight cycles after the effective date (engine counter 25600). Hub cycles are 90 at 2025-11-20, so the hub limit is 10 cycles away. The later point is engine cycle 25600.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** No engine shop visit is recorded after the effective date. The shop visit trigger cannot be confirmed as occurred; if one occurs, the hub must be replaced, but only once the later of the cycle limit or 100 cycles post-effective date is reached.
- **Missing fact:** The 2nd-stage hub S/N SYN-HUB2-0006 is not listed in table 1, so it is not matched. Confirmation that the serial number is accurate is advisable.
- **Note:** Engine cycles at the effective date were 25500, so 100 flight cycles after it is engine cycle 25600; this is the earliest point at which removal is required, and only at a shop visit.
- **Note:** The hub was installed 2025-09-30 with 90 cycles since new on 2025-11-20 and 60 at 2025-10-29; the 100-cycle limit is reached about 10 cycles after 2025-11-20.
- **Note:** The 'whichever occurs later' wording makes the shop visit trigger plus later threshold controlling; the text does not give a standalone deadline without a shop visit.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 row PKLBSK9287, limit 100

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a V2531-E5 and carries two hubs listed in table 1 (HPT 1st-stage 2A5001 PKLBSS9200 and HPT 2nd-stage 2A4802 PKLBST5005). Action is due at the next engine shop visit; no shop visit is recorded, so no deadline is set yet.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the removal cycle limit or within 100 flight cycles after the effective date, whichever occurs later. The 1st-stage hub limit of 4,800 cycles since new has not been reached (500 remaining). The 2nd-stage hub limit of 4,000 has not been reached (1,700 remaining). The 100 flight cycles after the effective date were used up at engine cycle 30100. No shop visit has occurred, so the removal is triggered by the next shop visit.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** No engine shop visit is recorded. Whether and when the next shop visit occurs determines when removal is due. If one occurs, it must be checked against the AD's engine shop visit definition in (i)(2).
- **Note:** Cycles since new on 2025-12-01: 1st-stage hub 4,300 (500 remaining to 4,800); 2nd-stage hub 2,300 (1,700 remaining to 4,000). The smallest remaining is 500.
- **Note:** The engine gained 300 cycles from 2025-10-29 to 2025-12-01, so the 100-cycle window after the effective date (engine cycle 30100) has passed. The 'whichever occurs later' wording makes the cycle limit or the shop visit the controlling element. The removal is due when the shop visit occurs, and the 4,800-cycle limit would be reached in about 500 more cycles (engine cycle about 30800).
- **Note:** The record shows no AMOC claim. Screening aid only; not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows PKLBSS9200 (4,800) and PKLBST5005 (4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 is within the AD's applicability and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1 (limit 6,200 cycles since new). Removal is due at the next engine shop visit, which has not occurred; the 2nd-stage hub serial number is unknown, so it cannot be cleared.
- **Stated timing:** Remove and replace the 1st-stage hub at the next engine shop visit after October 29, 2025, at or after the later of the 6,200 cycles-since-new limit or 100 flight cycles after the effective date. Engine flight cycles by which the 100-cycle window ends: 50,100 (already passed at 50,500). The hub has 3,700 cycles remaining to the limit, so the limit is later and governs; no deadline applies until an engine shop visit occurs.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub serial number is unknown, so it cannot be compared with the table 1 2nd-stage hub entries (P/N 2A4802). A match would add a further removal obligation.
- **Missing fact:** The 2nd-stage hub cycles since new is unknown; it is needed to compute the removal limit if the serial number matches a listed entry.
- **Note:** The 1st-stage hub was at 2,000 cycles since new on 2025-10-29 and 2,500 now, consistent with the 500 engine cycles flown since; remaining to the 6,200 limit is 3,700.
- **Note:** The engine record lists no shop visit events, so no required action has been triggered yet.
- **Note:** The record's ad_records and amoc_claims are empty; no AMOC is claimed.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2522-A5 is within the AD's model applicability and the AD is in force on the question date, but the record lists no installed components, so it cannot be determined whether an affected HPT 1st- or 2nd-stage hub is installed. An empty component list is not evidence that the parts are absent.
- **Stated timing:** If an affected hub is installed: at the next engine shop visit after October 29, 2025, before exceeding the table 1 removal cycle limit, or within 100 flight cycles after October 29, 2025, whichever occurs later. No deadline can be computed from the record.
- **Missing fact:** No record of the installed HPT 1st-stage hub P/N, S/N and cycles since new. Needed to match against table 1 (P/N 2A5001) and to compute the removal cycle limit.
- **Missing fact:** No record of the installed HPT 2nd-stage hub P/N, S/N and cycles since new. Needed to match against table 1 (P/N 2A4802) and to compute the removal cycle limit.
- **Missing fact:** No event history is supplied. Engine shop visits since October 29, 2025, and the engine flight-cycle counter at the effective date, are needed to establish timing.
- **Note:** This is a screening aid only and not a compliance determination.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule 2025-18469 and is not relied on.
- **Note:** The installation prohibition binds regardless of whether any affected hub is currently installed.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made.
- **Note:** The installed HPT 1st-stage hub P/N and S/N appear in the AD table, but no matching or applicability determination is made because the engine model is outside the supported scope.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force as of 2026-10-05. Replacement of the full blade set is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no shop visit is recorded, so no deadline is triggered now.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline otherwise.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** The record has no events, so no engine shop visit after 2026-09-24 is recorded. The record lists no AD or AMOC claims.
- **Note:** The blade set serial number is not tracked at set level; the AD lists the part number only, so the match rests on P/N 6A8353.
- **Note:** Document 2026-18423 corrected paragraph (g) of the directive under question to read 'the 3rd stage HPC rotor blade is exposed' rather than 'rotor is exposed'. This does not change the outcome here.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The engine is a supported model, but its installed 3rd stage HPC rotor blade set carries P/N 6C8368, which is not P/N 6A8353 or 6A8688 and is a part eligible for installation under (h)(1)(i). The AD applicability is not met on the supplied record.
- **Missing fact:** The record tracks the blade set only at set level with no per-blade serial numbers. Confirm that every blade in the set is P/N 6C8368 and that no individual 6A8353 or 6A8688 blade is mixed in. A mixed set would change the applicability result.
- **Note:** The correction document 2026-18423 only fixes a typographical error in paragraph (g); it does not change applicability.
- **Note:** This is a screening result based on the supplied record only, not a compliance determination.
- **Note:** The engine record shows no events, so no shop visit is recorded.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC blade set P/N 6A8688, so AD 2026-17-03 applies and is in force on 2026-09-30. The shop visit was inducted 2026-09-14, before the 2026-09-24 effective date, so paragraph (g) does not require replacement for that visit, even though blade exposure occurred after the effective date.
- **Stated timing:** No deadline is triggered by the 2026-09-14 visit. Replacement would be required at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Whether the blades were replaced with parts eligible for installation during the current visit is not recorded. If the set is still P/N 6A8688 after reassembly, the next shop visit with blade exposure would trigger replacement.
- **Note:** The question was asked on 2026-16954 as published; the correction 2026-18423 only adds the omitted word 'blade' to paragraph (g), with no effect on this result.
- **Note:** The operator asserts the 2026-09-14 visit qualifies as an engine shop visit; induction preceded the effective date. This is a screening result, not a compliance determination.
- **Note:** The post-effective-date blade removal on 2026-09-30 occurred during the visit inducted before the effective date; a reviewer should confirm the induction date and the blade set's current part number.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force on 2026-10-05 (effective 2026-09-24). The 2026-10-01 shop visit was inducted after the effective date, but no 3rd-stage blade was removed from the drum, so the blade-exposure trigger is not shown; replacement is required at the next engine shop visit where the blades are exposed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed, i.e. a blade is removed from the HPC stage 3-8 drum. No fixed deadline otherwise.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** Confirmation that no 3rd-stage blade was removed from the stage 3-8 drum during the 2026-10-01 to 2026-10-04 shop visit. The record says only that the rotor was exposed for inspection with no blade removed; if any blade was removed, replacement of the full set would have been triggered by that visit.
- **Note:** The question names document 2026-16954. Its paragraph (g) omitted the word 'blade' ('the 3rd stage HPC rotor is exposed'), and correction 2026-18423 fixed it. Under either wording the outcome here is the same, but the corrected wording ties the trigger to blade exposure as defined in (h)(2).
- **Note:** Exposing the rotor for inspection is not a blade exposure under (h)(2) unless a blade was removed from the drum.
- **Note:** The blade set serial numbers are not tracked at set level; this does not affect applicability because the AD lists the part number only.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527E-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so it is within the proposed applicability. The document is only an NPRM on the question date, so it cannot require action now.
- **Stated timing:** If adopted as proposed, replacement would be due at the next 3rd stage HPC rotor blade exposure (any blade removed from the HPC stage 3 to 8 drum) after the final rule's effective date. No deadline exists until then.
- **Note:** Proposed AD only; the final rule may differ. Re-screen when a final rule is published and its effective date is known.
- **Note:** The record shows no events, so no blade exposure is recorded. Absence of recorded events does not by itself confirm none occurred.
- **Note:** Serial numbers are not tracked at set level; the applicability is by part number, so this does not affect the match.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527-A5 is a listed model, so AD 2025-17-16 applies and has been in force since 2025-10-10. The record shows neither the V2500-A5 TLM ALS paragraph B.1 nor the approved maintenance program yet incorporates table 1, so the ALS revisions required by (g)(1) and (g)(2) are due within 90 days after the effective date.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e. by January 8, 2026, for both the TLM ALS revision (g)(1) and the air carrier maintenance/inspection program revision (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Note:** The action is a documentation revision, not tied to flight cycles or shop visits, so no cycle count applies and no installed-component matching is needed. The record's empty installed_components list does not affect this.
- **Note:** The 90-day deadline is computed from October 10, 2025 and falls on January 8, 2026; the reviewer should confirm the date computation.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is a listed model, so AD 2025-17-16 applies and is in force (effective 2025-10-10). The ALS/TLM revision in (g)(1) was due within 90 days after the effective date, by 2026-01-08, and (g)(2) adds a program revision for air carrier operations, which the record does not settle.
- **Stated timing:** Within 90 days after the effective date of October 10, 2025, i.e., by January 8, 2026, for the (g)(1) revision; the same 90-day deadline applies under (g)(2) if this is an air carrier operation.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the engine is used in air carrier operations is unknown; this decides whether the (g)(2) revision of the approved maintenance or inspection program also applies.
- **Missing fact:** Whether the TLM ALS revision under (g)(1) has already been done is not in the record (no ad_records entry for 2025-17-16 was supplied).
- **Missing fact:** No installed component records were supplied for the HPT Stage 1 Hub (P/N 2A5001), so no part match is possible. The AD applies by engine model, and the table lists the parts the inspection tasks cover.
- **Missing fact:** No installed component records were supplied for the HPT Stage 2 Hub (P/N 2A4802), so no part match is possible. The AD applies by engine model, and the table lists the parts the inspection tasks cover.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The AD is a one-time ALS/program revision. It is not triggered by a shop visit or tied to component cycles, so no flight-cycle deadline is computed.
- **Note:** The 90-day deadline is calendar-based, counted from October 10, 2025.
- **Note:** The NPRM 2024-26092 had an erroneous task number (72-45-11-200-009) that the final rule corrected to 72-45-31-200-009.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is within the applicability of AD 2025-19-13, and its HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 (limit 6,000 cycles since new). The AD is not effective until 2025-10-29, so no action is required on the question date; removal is tied to a future engine shop visit.
- **Stated timing:** Not yet effective on 2025-10-15 (effective 2025-10-29). Once effective, removal and replacement is due at the next engine shop visit after the effective date, before exceeding 6,000 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. No deadline applies absent a shop visit.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine's current flight-cycle count is not in the record, so a cycle-based deadline (100 cycles after the effective date) cannot be computed. The reading of 'whichever occurs later' also depends on when a shop visit occurs.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0018 is not listed in table 1, so it does not match.
- **Note:** The record has no events, so no shop visit has occurred. Cycles remaining is 6,000 minus 990 cycles since new.
- **Note:** Because the engine has about 5,010 cycles of margin, the 'whichever occurs later' wording makes the 100-cycles-after-effective-date term the likely later bound if a shop visit occurs soon; this needs the current engine cycle count.
- **Note:** The earlier NPRM 2025-10764 is superseded by the final rule and is not relied on.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The AD is in force and the engine model is covered. The HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is a listed part, past its 4,800-cycle limit, so removal is due at the next engine shop visit or within 100 flight cycles of the effective date, whichever is later; the 2nd-stage hub is not listed.
- **Stated timing:** Required at the next engine shop visit after 2025-10-29 or within 100 flight cycles after the effective date, whichever occurs later. The cycle limit is already exceeded, so the later of the two governs. No shop visit has occurred, so the removal date depends on when the next shop visit occurs.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** No engine shop visit is recorded since the effective date. The date of the next shop visit would set the deadline. Whether any future event meets the AD's engine shop visit definition is unknown.
- **Note:** The 1st-stage hub had 4,950 cycles since new at 2025-10-29, which is 150 over the 4,800 limit. At 2025-11-05 the record shows 4,990, which is 190 over the limit, so component_cycles_remaining is -190.
- **Note:** Reading: because the limit was already exceeded on the effective date, the 'whichever occurs later' language leaves the shop-visit trigger and the 100-cycle window (to engine cycle 60100 from 60000 at the effective date) both in play. The text can be read as requiring the action only at a shop visit that occurs after 60100 cycles, or at the first shop visit if that is later. Since no shop visit has occurred, the deadline cannot be computed, so latest_engine_flight_cycles is null.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0019 is P/N 2A4802 but its serial number is not listed in table 1, so it is not matched.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2533-A5 is a supported model and AD 2021-11-15 (document 2021-11960) was in force on 2022-03-01, but applicability depends on whether the installed disk serial numbers appear in Appendix A tables of the service bulletin, which were not supplied. Part numbers match the AD, so applicability and any action cannot be settled without the serial lists.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided; needed to check whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided; needed to check whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed.
- **Missing fact:** Engine/disk flight-cycle counters and cycles accumulated since 2021-07-13 are not in the record, so a 3,200-cycle limit cannot be turned into a counter value.
- **Missing fact:** The events list is empty, so no engine shop visit after 2021-07-13 is recorded; absence of a record does not show none occurred.
- **Note:** Question concerns 2021-11960; superseding AD 2022-02-09 becomes effective 2022-03-15 with different compliance times (Figure 1) and should be reviewed.
- **Note:** Part numbers match the AD but serial numbers could not be matched, so no parts are listed as matched.
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
- **Summary:** The engine model V2533-A5 is supported and the installed disk part numbers (2A5001, 2A4802) match the AD, but the serial numbers cannot be checked against the NMSB Appendix A tables, which were not supplied. AD 2022-02-09 is published but not effective until 2022-03-15, so it cannot yet require action.
- **Stated timing:** If the engine is within applicability, paragraphs (g)(1)/(g)(2) would require the USI by the Figure 1 compliance time or within 10 flight cycles after 2022-03-15, whichever occurs later, once the AD is in force. Figure 1 is not available in the supplied text.
- **Missing fact:** Content of Appendix A, Tables 1 and 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (serial number lists) was not supplied; needed to confirm whether disk S/Ns SYN-DISK1-0020 and SYN-DISK2-0020 are listed, which decides applicability.
- **Missing fact:** Figure 1 to paragraph (g)(1) (compliance-time image) is not included in the text; needed to compute the inspection deadline.
- **Missing fact:** Disk flight-cycle accumulation is not in the record; needed to apply the Figure 1 compliance time.
- **Missing fact:** Disk flight-cycle accumulation is not in the record; needed to apply the Figure 1 compliance time.
- **Missing fact:** Current engine flight-cycle counter not in the record; needed to convert the deadline to an engine cycle count.
- **Note:** Part numbers match but the serial-number match is unconfirmed; the record is not evidence that the disks are unaffected.
- **Note:** The AD is not in force on 2022-03-01; AD 2021-11-15 (effective 2021-07-13) remains in force until it is replaced on 2022-03-15. This screen did not evaluate it because the question concerns 2022-02574.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The engine model V2530-A5 is in scope and both installed disks have the listed part numbers (2A5001 and 2A4802). Applicability cannot be decided because the serial numbers cannot be checked against the service bulletin Appendix A tables, which were not supplied.
- **Missing fact:** Content of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (serial numbers of affected HPT 1st-stage disks); needed to decide whether SYN-DISK1-0021 is listed.
- **Missing fact:** Content of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (serial numbers of affected HPT 2nd-stage disks); needed to decide whether SYN-DISK2-0021 is listed.
- **Missing fact:** Figure 1 to paragraph (g)(1), which sets the compliance time, is an image not included in the text; needed to compute any deadline if a disk is listed.
- **Missing fact:** Disk cycle counts and inspection history are not in the record, so a deadline against Figure 1 cannot be computed even if a disk is listed.
- **Missing fact:** No events are recorded, so it is unknown whether the USI was already done (and could be credited) or whether a shop visit has occurred.
- **Note:** Matching is on part number only; the serial-number check against the Appendix A tables is outstanding.
- **Note:** Superseded AD 2021-11-15 is replaced by this AD; the current text governs.
- **Note:** This is a screening aid, not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine has an HPT 1st-stage disk P/N 2A5001, S/N PKLBSH1829, which is listed in paragraph (c)(1), so the AD applies. A USI of that disk is required within 10 flight cycles after the July 19, 2021 effective date, and the AD is in force on the question date.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021. The engine had 33000 cycles on 2021-07-19, so the deadline is engine cycle 33010. At 33004 on 2021-07-20, 6 cycles remain.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** No record shows whether the USI was already done, for example under Emergency AD 2021-11-51 issued May 21, 2021. The AD says 'unless already done'.
- **Missing fact:** The 2nd-stage disk S/N SYN-DISK2-0022 does not match any serial number listed in (c)(2). Table 2 in (g)(2) was not included in the text, so it cannot be checked for this disk. This does not change the (c)(1) match.
- **Missing fact:** The content of Tables 1 and 2 to paragraphs (g)(1) and (g)(2) (images not supplied) was not available, so the table entry for the 1st-stage disk could not be checked.
- **Missing fact:** The record gives only a daily engine cycle reading for the effective date. The cycle count at the start of that day is not recorded, which could shift the baseline.
- **Note:** This is a screening aid only and not a compliance determination.
- **Note:** The record has no ad_records or amoc_claims for this AD, and none were assumed.
- **Note:** The 2nd-stage disk serial number is synthetic and does not match any listed serial number, so it is not treated as a match, and a missing or unlisted record is not evidence that the part is unaffected.
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
- **Summary:** The V2533-A5 is a supported model and the AD was in force on 2021-07-20 (effective 2021-07-13). Applicability depends on whether the installed disk serial numbers appear in Appendix A Tables 1 and 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, which were not supplied, so applicability cannot be decided.
- **Stated timing:** If either disk is listed, the USI is due at the next engine shop visit after 2021-07-13 or before that disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first.
- **Missing fact:** Appendix A Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided, so it is unknown whether HPT 1st-stage disk P/N 2A5001, S/N PKLBSH1829 is listed. Listing determines applicability under (c)(1) and the (g)(1) action.
- **Missing fact:** Appendix A Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided, so it is unknown whether HPT 2nd-stage disk P/N 2A4802, S/N SYN-DISK2-0022 is listed. Listing determines applicability under (c)(2) and the (g)(2) action.
- **Missing fact:** Disk flight cycles accumulated since 2021-07-13 are not in the record. The engine cycle count on 2021-07-13 is also missing, so the 3,200-cycle limit cannot be converted to an engine cycle deadline.
- **Note:** Part numbers match the AD, but the serial numbers could not be checked against the NMSB tables. The 1st-stage disk S/N PKLBSH1829 is not confirmed as listed.
- **Note:** The event list is empty, so no shop visit is recorded. The record does not rule out that one occurred after 2021-07-13.
- **Note:** Engine flight cycles of 33,004 on 2021-07-20 are not a disk-since-effective-date count, so no deadline is computed.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and applies to the V2527M-A5 model. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 (limit 6,000 cycles since new), so replacement is required at the next engine shop visit; none is recorded, and the hub is not yet at its limit.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 6,000 cycles-since-new limit or within 100 flight cycles after the effective date, whichever occurs later. No shop visit is recorded, so no fixed deadline can be computed. The 100-cycle window ended at engine flight cycles 20,100, and the later of the two conditions governs.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The record shows 3,500 cycles since new at the snapshot (2026-10-06) but 1,000 at 2025-10-29. The 2,500 difference matches the engine's cycles flown since then, but the two readings are inconsistent with the 2024 installation date unless the hub was not new when installed. Confirm the current count, which determines the remaining margin to 6,000.
- **Missing fact:** No engine shop visit is recorded. A future shop visit, as defined in paragraph (i)(2), will trigger the replacement requirement.
- **Missing fact:** The S/N SYN-HUB1-0023 is not listed in table 1, so it is not matched. Confirm the serial number is accurate.
- **Missing fact:** The record has no entry for AD 2025-19-13. The maintenance program entry refers to AD 2025-17-16, a different AD that was not supplied, and it is not evidence for this AD.
- **Note:** The 6,000-cycle limit minus the current 3,500 cycles since new leaves 2,500 cycles.
- **Note:** The AD text is ambiguous on the exact trigger: it reads as at the next shop visit after the effective date, with the 'whichever occurs later' language tied to the cycle limit and the 100-cycle window. Since the hub has not reached its limit, the replacement is due at the next shop visit, and no deadline in engine cycles is computed.
- **Note:** The 3rd stage HPC rotor blade set is not a part listed in this AD.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 is in force on 2026-10-06 (effective 2026-09-24). The V2527M-A5 engine has a 3rd stage HPC rotor blade set P/N 6A8688, so it is within applicability; replacement is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed.
- **Stated timing:** At the next engine shop visit after September 24, 2026 in which any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum; no fixed cycle or date deadline applies otherwise.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** No engine shop visit or blade exposure after 2026-09-24 is recorded. Any such future event would trigger replacement with eligible parts.
- **Missing fact:** The record gives only a set-level P/N 6A8688 and no individual blade serial numbers or modification status, such as a rework to P/N 6A8688-001. The record does not show whether every blade in the set is the affected P/N, but the set-level entry is enough to treat the engine as within applicability.
- **Note:** The question names document 2026-16954. Its paragraph (g) omitted the word 'blade'; the later correction 2026-18423 fixes this, and the outcome is the same under either wording.
- **Note:** The record's maintenance program revision and AD 2025-17-16 relate to a different directive, concern the HPT hubs, and have no bearing on this AD. The HPT hubs are not affected parts under this AD.
- **Note:** The record gives no AMOC claim and no AD record for this AD. The engine's cycle counts do not drive any deadline, since the trigger is an event.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527M-A5 engine is within the applicability of AD 2025-17-16, which was in force on 2026-10-06. The record shows the TLM ALS and the approved maintenance program were revised on 2025-12-01 to incorporate table 1; whether that falls within the 90-day window depends on counting from the 2025-10-10 effective date, which ends 2026-01-08. No further action is triggered now, and continuing obligations still bind.
- **Stated timing:** The 90-day revision window after the 2025-10-10 effective date ended 2026-01-08. The record shows the revision on 2025-12-01, within that window. The inspection tasks themselves are performed at piece-part exposure under other regulations.
- **Missing fact:** The content of Revision 48 and of the TLM ALS revision was not supplied. It is unconfirmed that they incorporate TASK 72-45-11-200-006 and TASK 72-45-31-200-009 in paragraph B.1 of the Maintenance Scheduling section, as (g)(1) and (g)(2) require. The operator's assertion is a claim only.
- **Note:** The record does not identify the operator's AMOC claims; none are listed.
- **Note:** Cycle counts are not used because the required action is a document revision with a calendar deadline, not a cycle-based limit.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is within the AD's applicability and the AD is in force. No installed part matches a listed P/N and S/N pair, so no removal is triggered by the supplied record; the installation prohibition continues to bind.
- **Note:** The 2nd-stage hub carries S/N PKLBST5011, which appears in table 1 only against the 1st-stage hub P/N 2A5001. Because the P/N does not match (2A4802), it is not a listed part. A reviewer may want to confirm the serial number was recorded correctly.
- **Note:** The event list is empty. No shop visit is recorded, so the shop-visit timing would matter only if a listed part were found.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model CFM56-5B4/3 is not one of the supported IAE V2500 models, so no applicability determination is made for AD 2025-17-16.
- **Note:** The directive was effective 2025-10-10, before the question date of 2026-10-06, so it is in force on that date; no determination is made for this engine.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The AD is in force and applies to the V2530-A5. Installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in Table 1 with a 6,200 cycles-since-new limit, so removal is required at the next engine shop visit; no deadline applies until that event occurs.
- **Stated timing:** At the next engine shop visit after 2025-10-29, at or after the later of reaching the 6,200 cycles-since-new limit or 100 flight cycles after the effective date (2025-10-29). No deadline applies until a shop visit occurs.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** The HPT 2nd-stage hub serial number is recorded as SYN-HUB2-0026, which is not in Table 1. Confirm the actual serial number against the physical part or its records, since a mismatch could change whether a listed 2nd-stage hub is installed.
- **Missing fact:** Whether any future maintenance qualifies as an engine shop visit under paragraph (i)(2). No shop visit event is recorded, and the repair/inspection events in 2024 predate the effective date.
- **Note:** The hub cycles-since-new reading of 3,600 is the current value (2026-03-01), up from 3,000 at 2025-10-29. This is consistent with the engine's 600 cycles flown. Remaining cycles to the limit are 6,200 - 3,600 = 2,600.
- **Note:** The 2024 blend repair and the repeat ultrasonic inspection do not remove the part from Table 1, which is keyed to P/N and S/N, and no AMOC is recorded.
- **Note:** Because the limit has not been reached, the 'whichever occurs later' wording means removal is not due at a shop visit occurring before the hub reaches 6,200 cycles since new, unless the 100-cycle window is later. The text could be read in ways that affect timing at an earlier shop visit; confirm the interpretation at the time of the visit.
- **Unresolved locator:** 2025-18469 (g) Table 1, PKLBST7489 row, limit 6,200

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
- **Summary:** The engine is a V2527-A5 and the AD is in force. HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches table 1 (limit 4,800 CSN). Removal is required at the next engine shop visit, and no shop visit is recorded.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding 4,800 CSN or within 100 flight cycles after the effective date, whichever occurs later. Under the plain reading the 100-cycle window ended at engine cycle 15,100, which has passed, so the next shop visit is the trigger. No shop visit is recorded, so no deadline can be computed.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The claimed AMOC extending the hub limit to 5,300 CSN has no FAA approval reference or letter on file. It cannot be relied on to change the 4,800 CSN limit unless an FAA-approved AMOC is shown.
- **Missing fact:** No shop visit history is recorded. Whether a shop visit meeting the AD definition occurs or has occurred since 2025-10-29 determines when removal is triggered.
- **Missing fact:** The 2nd-stage hub S/N SYN-HUB2-0027 is not on table 1, so no match. This is noted only for completeness.
- **Note:** Hub CSN is 4,750 on 2026-01-20, which is 50 cycles below the 4,800 limit (4,500 at 2025-10-29 plus 250 engine cycles agrees).
- **Note:** The unapproved 5,300 CSN AMOC claim is not accepted as evidence.
- **Note:** Screening aid only, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 row PKLBSS9200, 4,800

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is listed in the AD applicability, and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 matches Table 1 (limit 4,000 cycles since new; currently 1,400). Removal is required at the next engine shop visit, and no shop visit is recorded, so no deadline is running. The operator's 'not applicable' record is contradicted by this match.
- **Stated timing:** At the next engine shop visit after the 2025-10-29 effective date; the hub is far below its 4,000-cycle limit, so the 100-flight-cycle-from-effective-date window (8,100 engine cycles) has already passed and the later-of rule is governed by the shop visit. No shop visit is recorded, so no fixed deadline.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The 1st-stage hub serial SYN-HUB1-0028 is not in Table 1, so it is not matched. It is a synthetic placeholder and should be verified against the physical part and records.
- **Missing fact:** No shop visit is recorded. Any future event must be checked against the AD's engine shop visit definition (separation of major mating flanges, excluding transport-only or field maintenance in lieu of on-wing work) to determine whether it triggers removal.
- **Note:** The record marks the AD 'not applicable' with the note 'no affected hubs installed'. This is an operator claim, and it conflicts with the 2nd-stage hub match.
- **Note:** The 2nd-stage hub is recorded as installed 2025-06-03 with 1,400 cycles since new on the question date, but the 2025-10-29 reading is 1,000, which is consistent with 400 cycles flown since then.
- **Note:** Remaining cycles are 4,000 minus 1,400 = 2,600. The AD text says removal is at the next shop visit before exceeding the limit or within 100 cycles of the effective date, whichever is later. How this applies if a shop visit occurs before the limit is reached should be reviewed. The AD does not clearly say whether the hub may remain in service up to the limit, so confirm the interpretation.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is a listed model and the AD is in force. The installed HPT 1st-stage hub S/N PKLBSK9287 matches table 1, but its P/N is recorded as 2A5001-01 while the AD lists 2A5001, so the match needs review. If it is an affected part, removal is required at the next engine shop visit; its 100-cycle limit is already exceeded at 2,400 cycles.
- **Stated timing:** If the hub is an affected part: at the next engine shop visit after October 29, 2025, or within 100 flight cycles after October 29, 2025, whichever occurs later. The 100-cycle removal limit is already exceeded, so the 100-flight-cycle window after the effective date governs. The record has no engine flight-cycle reading at the effective date, so no deadline counter can be computed.
- **Missing fact:** The installed P/N is 2A5001-01 but table 1 lists 2A5001. It must be confirmed whether the -01 dash number is the same listed part number; this decides whether the S/N match makes the hub an affected part.
- **Missing fact:** The engine flight-cycle count at the effective date (2025-10-29) is needed to compute the 100-cycle deadline.
- **Missing fact:** The record shows no shop visits. Any engine shop visit since 2025-10-29, and whether it meets the AD definition, would show whether the replacement trigger has occurred.
- **Note:** The HPT 2nd-stage hub S/N SYN-HUB2-0029 is not listed in table 1, so it is not an affected part.
- **Note:** The record has no AD records or AMOC claims for this directive.
- **Note:** The record shows no events, so there is no evidence of an engine shop visit since the effective date.
- **Note:** If the hub is confirmed as affected, action is required: removal at the later of the next shop visit or 100 flight cycles after October 29, 2025.

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
