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
- **Summary:** The V2527-A5 is within the AD's applicability and its HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in Table 1 (limit 5,500 cycles since new). No engine shop visit is recorded, so removal is triggered only at the next engine shop visit, and the cycle-limit fact conflicts in the record.
- **Stated timing:** At the next engine shop visit after October 29, 2025, at the later of reaching the 5,500 cycles-since-new limit or 100 flight cycles after the effective date (engine counter 41,300). No deadline applies absent a shop visit.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** Current cycles since new (3,100) conflicts with the 2025-10-29 reading of 1,650 plus 1,450 engine cycles flown since (about 3,100 is consistent only if the hub flew those cycles; confirm). The remaining margin to the 5,500 limit depends on this value.
- **Missing fact:** The serial number SYN-HUB2-0001 is not in Table 1, so no match, but confirm it is the true serial number of the installed part.
- **Missing fact:** No shop visits are recorded. A future event meeting the AD's engine shop visit definition would trigger the removal.
- **Note:** The 1st-stage hub is below its 5,500 limit, and the 100-cycle window after the effective date ended at engine cycle 41,300, so the removal is due at the next shop visit.
- **Note:** Screening aid only; not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, PKLBST5011 row, 5,500 cycles

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 is a listed model, so the AD applies, but neither installed hub P/N and S/N matches Table 1 (the 1st-stage hub S/N PKLBST5012 differs from listed PKLBST5011), so the paragraph (g) removal is not triggered on the record. The installation prohibition and other obligations continue to bind.
- **Note:** PKLBST5012 is one character off listed PKLBST5011; the serial number on the record should be verified against the part's physical data plate.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 is within the AD's model applicability and the AD is in force, but the HPT 1st-stage hub serial number is unknown, so a match to table 1 cannot be ruled in or out. The 2nd-stage hub S/N SYN-HUB2-0003 is not listed in table 1.
- **Missing fact:** The 1st-stage hub P/N 2A5001 matches the listed P/N, but the S/N is unknown. It must be compared with the four listed S/Ns (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489) to decide whether paragraph (g) is triggered.
- **Missing fact:** Cycles since new for the 1st-stage hub are unknown. If the S/N is a listed one, they are needed to compare against the removal cycle limit (100 to 6,200) and compute the deadline.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) does not match any listed S/N, so it does not trigger paragraph (g) on the record as given.
- **Note:** The record has no events, so no engine shop visit is recorded since the effective date.
- **Note:** If the 1st-stage hub S/N is found to be listed, paragraph (g) applies at the next engine shop visit after the effective date, before exceeding the applicable removal cycle limit or within 100 flight cycles of the effective date, whichever occurs later. The record gives no flight cycles since the effective date.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for this screen.
- **Note:** No determination is made on whether the directive applies to this engine model.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and covers the V2527E-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed (limit 3,900 cycles since new, about 2,860 cycles remaining). The 2025-11-12 shop visit is after the effective date and is recorded as qualifying, so removal and replacement is triggered at that visit.
- **Stated timing:** Paragraph (g) requires removal at the next engine shop visit after 2025-10-29, but not before the removal cycle limit is reached or within 100 flight cycles after the effective date, whichever is later. The cycle limit (3,900) has not been reached, so on the stated reading the later date is 100 flight cycles after the effective date: engine flight cycle 18100. The 2025-11-12 shop visit (cycle 18040) is within that window, so removal is due by engine cycle 18100, and the part must not be reinstalled.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0005 is not listed in table 1, so it is not matched. The serial number is recorded, so this is only a confirmation item.
- **Missing fact:** The shop visit qualification is asserted by the operator record. Confirm it meets the paragraph (i)(2) definition (flange separation, not transport-only or field maintenance).
- **Note:** The 2nd-stage hub has 1,040 cycles since new against a 3,900 limit, so 2,860 cycles remain.
- **Note:** The replacement hub must have a P/N and S/N not listed in table 1.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and the V2530-A5 engine has an HPT 1st-stage hub (P/N 2A5001, S/N PKLBSK9287) listed in table 1, so removal and replacement is required at the next engine shop visit; no shop visit has occurred. The 2nd-stage hub S/N is not listed.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 100 cycles-since-new limit or within 100 flight cycles after the effective date, whichever occurs later. The 100-cycle limit is already exceeded, so the later date is the 100 flight cycles after the effective date; that window ends at engine flight cycle 25600. The engine is at 25530, leaving 70 cycles. The removal is tied to a shop visit, with no deadline absent one.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Note:** Hub cycles-since-new is 90 at 2025-11-20 versus the limit of 100 per the record. Cycles remaining is computed as 100-90=10, so the sign in component_cycles_remaining reflects the interpretation that the limit is not yet exceeded only if the record is read that way; verify.
- **Note:** The record shows the hub at 60 cycles since new at 2025-10-29 and 90 at 2025-11-20, while the engine accrued 30 cycles; the figures are consistent.
- **Note:** The hub was installed 2025-09-30, after the NPRM but before the effective date; installation is not barred by (h) since that applies after the effective date.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, row PKLBSK9287, limit 100

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a listed model and has two hubs matching Table 1 (HPT 1st-stage 2A5001/PKLBSS9200 and HPT 2nd-stage 2A4802/PKLBST5005). Removal is tied to the next engine shop visit after 2025-10-29; no shop visit is recorded, so action is due on that event, not before.
- **Stated timing:** At the next engine shop visit after October 29, 2025, or within 100 flight cycles after the effective date, whichever occurs later. No shop visit is recorded, so no fixed deadline can be computed.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** No engine shop visit is recorded since the effective date. A future shop visit, or confirmation that none has occurred, determines when removal is due. The record cannot show if the hubs would be past their limits at that visit.
- **Note:** Current cycles since new on 2025-12-01: 1st-stage hub 4300 (limit 4800, 500 remaining); 2nd-stage hub 2300 (limit 4000, 1700 remaining). The smallest remaining is 500.
- **Note:** The hub cycle counts are on the record's own readings. Engine flight cycles rose 300 from 2025-10-29 to 2025-12-01, matching the hub increases.
- **Note:** The removal requirement binds only at a shop visit, so the 'whichever is later' wording leaves no fixed date before one occurs.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows PKLBSS9200 (4,800) and PKLBST5005 (4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 is within the AD, and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1 (limit 6,200 cycles since new). Removal is due at the next engine shop visit, which is the later of that visit-or-limit point and 100 flight cycles after the effective date; no shop visit has occurred. The 2nd-stage hub serial number is unknown, so it cannot be cleared.
- **Stated timing:** At the next engine shop visit after 2025-10-29, and not before the hub exceeds 6,200 cycles since new or 100 flight cycles after the effective date, whichever is later. The 100-cycle point is engine cycle 50,100, already passed (engine at 50,500), so the hub is now removable at the next shop visit. The hub has 3,700 cycles remaining before reaching 6,200.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The 2nd-stage hub serial number is unknown. It must be checked against table 1 (P/N 2A4802 is a listed part number), and a match would bring in another removal requirement.
- **Missing fact:** The 2nd-stage hub cycles since new are unknown, needed to compare against the removal cycle limit if its serial number matches a listed entry.
- **Note:** No shop visit is recorded (events empty), so no removal is currently triggered by an event.
- **Note:** The 1st-stage hub cycles since new were 2,000 at 2025-10-29 and 2,500 at 2026-03-10, consistent with the 500 engine cycles flown; remaining is 6,200 minus 2,500.
- **Note:** The record lists no ad_records or amoc_claims for this AD.
- **Unresolved locator:** 2025-18469 (g) Table 1, PKLBST7489 row

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2522-A5 is within the AD applicability and the AD is in force on the question date. The record lists no installed components, so it cannot be determined whether an affected HPT 1st-stage or 2nd-stage hub is installed; an empty record is not evidence that the parts are absent.
- **Missing fact:** No record of the installed HPT 1st-stage hub P/N, S/N and cycles since new; needed to match against table 1 and compute the removal cycle limit.
- **Missing fact:** No record of the installed HPT 2nd-stage hub P/N, S/N and cycles since new; needed to match against table 1 and compute the removal cycle limit.
- **Missing fact:** No shop visit history; needed to identify the next engine shop visit after October 29, 2025 and the engine flight-cycle counter for the 100-cycle window.
- **Note:** The proposed rule 2025-10764 was superseded by the final rule 2025-18469.
- **Note:** Screening aid only; not a compliance determination.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made.
- **Note:** The directive 2025-18469 was effective 2025-10-29 and is in force on the question date, but no determination is made for an unsupported model.
- **Note:** The installed hub P/N and S/N appear in table 1, but no applicability determination is made for this unsupported model.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force on 2026-10-05. Replacement of the full blade set is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no deadline is triggered otherwise.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** The question names document 2026-16954. Its paragraph (g) omitted the word 'blade' and was corrected by 2026-18423; the correction does not change the outcome here.
- **Note:** No shop-visit events are recorded, so no event has triggered replacement. The record does not show any prior blade replacement or AMOC claim.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The V2533-A5 is a supported model, but the record shows 3rd stage HPC rotor blade set P/N 6C8368, which is not P/N 6A8353 or 6A8688, so the engine is outside the AD's applicability on the supplied facts.
- **Note:** Blade set is tracked at set level without a serial number; the record shows one part number for the set. If individual blades with different P/Ns (6A8353 or 6A8688) are actually installed in the set, this conclusion would change.
- **Note:** This is a screening result, not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC blade set P/N 6A8688, so AD 2026-17-03 applies and is in force on 2026-09-30. The shop visit was inducted 2026-09-14, before the 2026-09-24 effective date, so the paragraph (g) replacement is not triggered by that visit.
- **Stated timing:** Replacement is due at the next engine shop visit after 2026-09-24 in which the 3rd stage HPC rotor blade is exposed. The 2026-09-14 visit does not count, and no deadline applies until then.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Note:** The blade removal on 2026-09-30 falls after the effective date, but the visit was inducted 2026-09-14, before it. Under (g) as adopted and (h)(3), the shop visit is measured from induction, so this visit is not one 'after the effective date'.
- **Note:** A reviewer may wish to confirm this reading. If the blades are reinstalled, or if the engine is inducted again after 2026-09-24, the requirement will apply at that later visit.
- **Note:** Correction document 2026-18423 fixes a typographical error in (g) and does not change the substance.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force on 2026-10-05. The 2026-10-01 shop visit was inducted after the 2026-09-24 effective date, but no 3rd stage blade was removed from the drum, so no blade exposure occurred and replacement is not yet triggered; it is due at the next qualifying shop visit where a blade is exposed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed (removed from the stage 3-8 drum); no deadline otherwise.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** The record states the 2026-10-02 HPC rotor exposure involved no 3rd-stage blade removal from the stage 3-8 drum. This should be confirmed against work records, because any blade removal during the 2026-10-01 to 2026-10-04 visit would trigger replacement under (g).
- **Note:** Paragraph (g) as originally published in 2026-16954 reads 'rotor is exposed'; the correction in 2026-18423 changes it to 'rotor blade is exposed'. Under either wording, the record shows no blade removal, so the conclusion is the same.
- **Note:** The 2026-10-01 induction was after the effective date, so it was a shop visit within the AD period, but it did not expose a blade per the record.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527E-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so it is within the proposed applicability. The document is only an NPRM on the question date, so it cannot require action now.
- **Stated timing:** If adopted as proposed, replacement of the full blade set would be due at the next 3rd stage HPC rotor blade exposure after the final rule's effective date. No effective date exists yet.
- **Note:** Proposed text may change after comments (due 2026-01-02) before any final rule.
- **Note:** The record shows no events, so no blade exposure is recorded. Even after a final rule, action would arise only at a future exposure.
- **Note:** Blades are tracked at set level only; the record does not show whether the installed blades are already modified to -001 or an eligible P/N. This is not needed now.
- **Note:** This screening is not a compliance determination.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527-A5 is a listed model, so AD 2025-17-16 applies. The AD has been in force since 2025-10-10, and the record shows neither the V2500-A5 TLM ALS paragraph B.1 nor the approved maintenance program yet incorporates table 1; both revisions are due within 90 days after the effective date.
- **Stated timing:** Within 90 days after the effective date of October 10, 2025, i.e. by January 8, 2026, for both the TLM ALS revision under (g)(1) and, because this is air carrier operation, the program revision under (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Note:** The record has no installed component entries, but the required action is a documentation revision that does not depend on part installation, so no parts are matched.
- **Note:** The 90-day deadline is calendar-based, so no flight-cycle count is computed.
- **Note:** The AD requires the revisions only; the inspection tasks themselves are performed under other regulations once incorporated.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model V2522-A5 is within the AD applicability and the AD was in force on the question date (effective 2025-10-10). The paragraph (g)(1) ALS/TLM revision was due within 90 days after the effective date, and paragraph (g)(2) applies only if this is an air carrier operation, which is unknown.
- **Stated timing:** Paragraph (g)(1): within 90 days after October 10, 2025, i.e. by January 8, 2026. Paragraph (g)(2), if air carrier operations: same 90-day deadline.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the engine is used in air carrier operations is unknown; this determines whether paragraph (g)(2) (revision of the approved maintenance or inspection program) applies.
- **Missing fact:** Whether the TLM ALS revision under (g)(1) has already been done is not in the record (no ad_records supplied), so completion cannot be confirmed.
- **Note:** The AD requires only revision of the ALS/program, so no installed-part matching or cycle computation is needed; the hub part numbers in Table 1 (2A5001, 2A4802) are inspection tasks at piece-part exposure.
- **Note:** The proposed rule 2024-26092 is superseded by the final rule and was not relied on for requirements.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is within the AD's applicability, and its HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in Table 1 (limit 6,000 cycles since new). The AD is published but not effective until 2025-10-29, so no action is required yet; removal is tied to a future engine shop visit.
- **Stated timing:** Not yet in force on 2025-10-15 (effective 2025-10-29). Once in force, remove at the next engine shop visit after the effective date, before the hub exceeds 6,000 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. The hub has 990 cycles, so the later limit is the 100-flight-cycle window. No fixed deadline is computable because the engine's flight-cycle counter at the effective date is not supplied.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** Engine flight-cycle counter at the 2025-10-29 effective date is not supplied. It is needed to convert the 100-flight-cycle window into an engine cycle deadline.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0018 is not listed in Table 1, so it is not matched.
- **Note:** No events are recorded, so no engine shop visit has occurred. The NPRM 2025-10764 is superseded by the final rule.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is covered and the HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches table 1 (limit 4,800 cycles since new). The hub is already past its limit, so removal falls due at the next engine shop visit after 2025-10-29, but not later than that visit; no shop visit is recorded.
- **Stated timing:** At the next engine shop visit after 2025-10-29. The limit has already been exceeded, so the later-of date is 100 flight cycles after the effective date, which is engine cycle 60100. The shop-visit trigger is the controlling event. No deadline applies if no shop visit occurs.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The 2nd-stage hub S/N SYN-HUB2-0019 is not in table 1, so it does not match. Its identity as recorded should be confirmed.
- **Note:** Hub cycles since new were 4950 on 2025-10-29 and 4990 on 2025-11-05, which is 190 over the 4,800 limit; the limit was already exceeded before the effective date.
- **Note:** The 40 engine cycles flown between readings match the 40-cycle hub increase.
- **Note:** No events are recorded, so no engine shop visit after the effective date is shown. The record does not show whether one has occurred.
- **Note:** The operator has no recorded AMOC or AD record for this AD.
- **Note:** This is a screening aid only, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, PKLBSS9200 row

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The engine model V2533-A5 is supported and AD 2021-11-15 (2021-11960) was in force on 2022-03-01, but applicability depends on whether the installed disk serial numbers appear in the service bulletin Appendix A tables, which were not supplied. The record also gives no flight-cycle or shop visit data.
- **Stated timing:** If the disks are listed: at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 FCs since July 13, 2021, whichever occurs first (g)(1)/(g)(2). No shop visit events are recorded, and the FC accumulation since the effective date is not supplied.
- **Missing fact:** Content of IAE NMSB V2500-ENG-72-0713 Rev 1 Appendix A Tables 1 and 2 was not provided; needed to determine whether serials SYN-DISK1-0020 and SYN-DISK2-0020 are listed.
- **Missing fact:** Flight cycles accumulated by the HPT 1st-stage disk since July 13, 2021, needed to compute the 3,200 FC limit.
- **Missing fact:** Flight cycles accumulated by the HPT 2nd-stage disk since July 13, 2021, needed to compute the 3,200 FC limit.
- **Missing fact:** No AD record or USI accomplishment is supplied, so whether the USI was already done is unknown.
- **Note:** Part numbers match, but the serial-number match was not confirmed because the Appendix A list was not supplied, so matched_parts is provisional.
- **Note:** AD 2022-02-09 (2022-02574) supersedes this AD effective 2022-03-15, after the question date, so 2021-11960 remains the AD in force on 2022-03-01.
- **Note:** This is a screening aid only and not a compliance determination.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 is published but not effective until 2022-03-15, so no action is required on 2022-03-01. The engine model is in scope and both disks have the listed part numbers, but their serial numbers cannot be checked against the NMSB Appendix A tables, which were not supplied.
- **Stated timing:** Not yet in force. Once effective on 2022-03-15, (g)(1)/(g)(2) would require the USI within the Figure 1 compliance time or within 10 FCs after the effective date, whichever is later. Figure 1 was not provided, so no deadline can be computed.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (listed HPT 1st-stage disk serial numbers) was not supplied. It is needed to confirm that S/N SYN-DISK1-0020 is listed.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (listed HPT 2nd-stage disk serial numbers) was not supplied. It is needed to confirm that S/N SYN-DISK2-0020 is listed.
- **Missing fact:** Figure 1 to paragraph (g)(1), the compliance-time table, is an image that was not included in the text. It is needed to compute any deadline.
- **Missing fact:** Disk cycle accumulation is not in the record. It is needed to apply the Figure 1 thresholds.
- **Missing fact:** Disk cycle accumulation is not in the record. It is needed to apply the Figure 1 thresholds.
- **Note:** The record shows no events, so no shop visit history is available.
- **Note:** Matched parts are by part number only. The serial numbers still need to be checked against the NMSB tables.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2530-A5 is a listed model and the installed disks carry the listed part numbers (2A5001 and 2A4802). Applicability depends on whether the disk serial numbers appear in Appendix A, Tables 1 and 2 of the service bulletin, and that appendix was not supplied. The compliance times in Figure 1 were also not supplied.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided, so it cannot be confirmed whether HPT 1st-stage disk S/N SYN-DISK1-0021 is listed. Listing determines applicability under (c)(1).
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided, so it cannot be confirmed whether HPT 2nd-stage disk S/N SYN-DISK2-0021 is listed. Listing determines applicability under (c)(2).
- **Missing fact:** Figure 1 to paragraph (g)(1) was an image not included in the text, so the compliance time for a V2530-A5 cannot be computed.
- **Missing fact:** Disk flight-cycle counts and the engine flight-cycle counter are not in the record, so a cycle-based deadline cannot be computed even if the disks are listed.
- **Missing fact:** The event list is empty, so there is no shop visit or inspection history. Any prior USI of either disk is not documented, which matters for credit and timing.
- **Note:** This is a screening result only and not a compliance determination.
- **Note:** The effective date of March 15, 2022 has passed, and the 10-FC grace period after it has long elapsed. The Figure 1 time is unknown, so the status cannot be set.
- **Note:** The previous AD 2021-11-15 is superseded by this document.
- **Note:** Serial numbers are synthetic and cannot be checked against the real service bulletin list.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine has an HPT 1st-stage disk P/N 2A5001, S/N PKLBSH1829, which is listed in paragraph (c)(1), so the AD applies. A USI of that disk is required within 10 flight cycles after the July 19, 2021 effective date, i.e. by engine flight cycle 33010.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021 (engine at 33000 cycles on that date), so by 33010 engine flight cycles; 4 cycles used as of 2021-07-20.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** The 2nd-stage disk S/N SYN-DISK2-0022 is not among the serials in paragraph (c)(2); Table 2 to paragraph (g)(2) is an image not provided, so it cannot be checked. It does not change the applicability or the 1st-stage deadline.
- **Missing fact:** No record of whether the USI has already been done (paragraph (f) 'unless already done') or of any AMOC claimed.
- **Note:** The 10-cycle count starts from the engine cycle reading on the effective date (33000).
- **Note:** Screening aid only; not a compliance determination.
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
- **Summary:** The V2533-A5 is a supported model and the AD is in force (effective 2021-07-13). Whether it applies depends on whether the installed disk serial numbers appear in Appendix A Tables 1 and 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, and that service bulletin content was not supplied.
- **Stated timing:** If either disk is listed: at the next engine shop visit after 2021-07-13 or before that disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. The disk cycle count at the effective date is not supplied.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided, so it cannot be confirmed whether HPT 1st-stage disk S/N PKLBSH1829 (P/N 2A5001) is listed.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided, so it cannot be confirmed whether HPT 2nd-stage disk S/N SYN-DISK2-0022 (P/N 2A4802) is listed.
- **Missing fact:** Disk cycle counts, and the counts at the 2021-07-13 effective date, are not recorded. They are needed to compute the 3,200-cycle limit.
- **Missing fact:** No shop visit events are recorded since 2021-07-13, so it is unknown whether an engine shop visit has occurred that would have triggered the inspection.
- **Note:** The installed part numbers match the AD's part numbers, but the serial numbers cannot be matched without the NMSB tables.
- **Note:** The 1st-stage disk serial number has a real-looking format, while the 2nd-stage serial number is synthetic.
- **Note:** Engine flight cycles (33,004) are not disk cycles, so no engine-cycle deadline can be computed.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and applies to the V2527M-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1, so it must be removed at the next engine shop visit; no deadline applies without such a visit.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 6,000 cycles-since-new limit or within 100 flight cycles after the effective date, whichever occurs later. No shop visit is recorded, so no fixed deadline can be computed.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The hub's cycles since new at 2026-10-06 is recorded as 3500, but the 2025-10-29 reading was 1000. The two readings are inconsistent given the engine accrued 2500 cycles in between, so the 2500 remaining is based on the snapshot value and needs confirmation.
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0023 is not listed in table 1, so it is not matched. Its listing status depends on the serial number being correct.
- **Missing fact:** No engine shop visit is recorded since 2025-10-29. A future shop visit would trigger removal of the 2nd-stage hub.
- **Missing fact:** The record holds no entry for AD 2025-19-13. The maintenance program revision cites AD 2025-17-16, which is a different AD and is not supplied, so it does not address this AD.
- **Note:** The record's maintenance program revision refers to AD 2025-17-16, not this AD, and does not show action under AD 2025-19-13.
- **Note:** The wording of (g) combines the shop visit with the cycle limit or 100 cycles, and is read here as requiring removal at the next shop visit.
- **Note:** The proposed rule 2025-10764 was superseded by the final rule.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 is in force on 2026-10-06 (effective 2026-09-24) and applies to this V2527M-A5 engine because it has a 3rd stage HPC rotor blade set P/N 6A8688 installed. Replacement is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no deadline is triggered otherwise.
- **Stated timing:** At the next engine shop visit after September 24, 2026 in which any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum; no calendar or cycle deadline otherwise.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** No engine shop visit or blade-exposure event after 2026-09-24 is recorded, so it is not known whether the action has been triggered. Any such event must be checked against the AD's definitions of shop visit and blade exposure.
- **Missing fact:** Blade set serials are not tracked at set level; the AD lists the part number only, so applicability rests on the P/N. Confirm that all installed blades are P/N 6A8688 or 6A8353 and whether any were already replaced or modified to an eligible P/N.
- **Note:** The record's maintenance program revision cites AD 2025-17-16, a different directive, and does not bear on this AD.
- **Note:** The HPT hub records are unrelated to this AD and were not used.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527M-A5 engine is within the applicability of AD 2025-17-16, which was in force on 2026-10-06 (effective 2025-10-10). The record shows the TLM ALS and the approved maintenance program were revised on 2025-12-01, within 90 days of the effective date (deadline 2026-01-08), so no further action is triggered by this screen.
- **Stated timing:** The paragraph (g)(1) and (g)(2) revisions were due within 90 days after 2025-10-10, that is by 2026-01-08. The record shows both were revised on 2025-12-01.
- **Missing fact:** The content of Revision 48 and the TLM ALS revision was not supplied. Whether they incorporate table 1 tasks 72-45-11-200-006 and 72-45-31-200-009 in paragraph B.1 of the Maintenance Scheduling section of each applicable TLM cannot be confirmed from the record summary alone.
- **Missing fact:** The record gives conflicting cycles-since-new for the HPT 2nd-stage hub: 1000 at 2025-10-29 versus 3500 current, while it was installed 2024-01-09. This should be reconciled. It does not change the screening outcome because the AD sets no cycle threshold.
- **Note:** This is a screening aid only and not a compliance determination.
- **Note:** The AD requires revising the ALS and program; the inspections themselves apply at piece-part exposure under the revised program.
- **Note:** No engine-cycle deadline applies because the AD uses a calendar-based compliance time.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model is within the AD applicability and the AD is in force. The installed hubs do not match a listed P/N and S/N pair (the 2nd-stage hub S/N PKLBST5011 is listed only under P/N 2A5001 as a 1st-stage hub, and the installed 2nd-stage hub is P/N 2A4802), so no removal action is triggered by the record; the installation prohibition continues to bind.
- **Note:** Installed 2nd-stage hub S/N PKLBST5011 matches a serial listed in Table 1 only for the 1st-stage hub P/N 2A5001; the P/N 2A4802 differs, so it is not treated as a match. Reviewer may wish to verify the serial number and part number against the hub's records for a possible data entry error.
- **Note:** The installed 1st-stage hub S/N SYN-HUB1-0024 is not listed in Table 1.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model CFM56-5B4/3 is not one of the supported IAE V2500 models, so no applicability determination is made.
- **Note:** No applicability determination was made for this engine model.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is covered and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1 (limit 6,200 cycles since new). Removal is required at the next engine shop visit after 2025-10-29, and no deadline applies until such a visit occurs.
- **Stated timing:** At the next engine shop visit after October 29, 2025, which must be before the hub exceeds 6,200 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. No shop visit is recorded, so no fixed date can be computed.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** The 2nd-stage hub serial number is a synthetic placeholder, not a real S/N. It cannot be matched against the table 1 serial numbers, so it is unconfirmed whether it is a listed part.
- **Missing fact:** No engine shop visit after 2025-10-29 is recorded. A future shop visit triggers the removal requirement.
- **Note:** Cycles remaining is 6,200 minus the current 3,600 cycles since new, which is 2,600. The record's cycles_since_new reading of 3,000 at 2025-10-29 and 3,600 now is consistent with the 600 engine cycles flown in that period.
- **Note:** The 2024 blend repair and clean repeat ultrasonic inspection do not appear in the AD as an exception or terminating action. Any AMOC would need to be approved under paragraph (j).
- **Note:** The cycle limit is not reached, but the removal trigger is the shop visit. Shop-visit status of any future event should be checked against the (i)(2) definition.

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
- **Summary:** The engine model is covered, and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches Table 1 (limit 4,800 CSN). The AD is in force, but the removal is tied to the next engine shop visit, and the record shows none, so no deadline is set until one occurs.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding 4,800 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. The 100-cycle window ended at engine cycle 15,100. Because the hub is under its 4,800 limit and no shop visit has occurred, the removal is triggered only when a shop visit occurs. The hub must not be allowed to bypass the shop visit requirement, and the installation prohibition applies now.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The planning note claims an AMOC extending the limit to 5,300 CSN, but no FAA approval reference or letter is on file. Without an approved AMOC under paragraph (j) it cannot be relied on to change the 4,800 limit.
- **Missing fact:** No shop visit events are recorded. Whether and when the next engine shop visit (as defined in (i)(2)) occurs determines when removal is due.
- **Missing fact:** The 2nd-stage hub S/N SYN-HUB2-0027 is not in Table 1 and so is not matched, but the record is synthetic and the identity should be confirmed.
- **Note:** Hub CSN on 2026-01-20 is 4,750, so 50 cycles remain to the 4,800 limit (about 250 cycles flown since 2025-10-29 at 4,500 CSN matches 4,750).
- **Note:** If the hub passes 4,800 CSN before a shop visit, the 'whichever occurs later' wording means removal is still at the next shop visit; the text does not require removal outside a shop visit.
- **Note:** The claimed 5,300 CSN AMOC is unverified and was not used.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is listed and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 matches table 1 (limit 4,000 cycles since new). Action is due at the next engine shop visit; the hub is at 1,400 cycles, so the removal limit is not yet exceeded, and the 'later of' timing means removal is tied to a shop visit, not a calendar date.
- **Stated timing:** At the next engine shop visit after October 29, 2025, before exceeding 4,000 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. No deadline arises without a shop visit.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0028 is not in table 1, so it does not match. Confirm the serial number is correct, since a mismatch would change the result.
- **Missing fact:** The 2nd-stage hub shows 1,400 cycles now and 1,000 at 2025-10-29 while the engine flew 400 cycles over the same period. This is consistent, but the installed date of 2025-06-03 precedes the effective date and the cycle count should be confirmed.
- **Note:** The operator's record marking the AD not applicable with 'no affected hubs installed' is contradicted by the 2nd-stage hub match; the AD applies to all listed models regardless.
- **Note:** No events are recorded, so no shop visit has occurred that would trigger removal.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is within the AD applicability and the AD is in force. The 1st-stage hub S/N PKLBSK9287 appears in Table 1, but the installed P/N is 2A5001-01 versus listed 2A5001, so the match needs review. If it matches, the removal limit of 100 cycles is already exceeded and removal is due at the next engine shop visit.
- **Stated timing:** If the part matches: at the next engine shop visit after October 29, 2025 (the limit of 100 cycles since new is already passed, so the later-of 100 flight cycles from the effective date applies). No shop visit is recorded, so the deadline cannot be computed.
- **Missing fact:** Installed P/N is 2A5001-01 while Table 1 lists 2A5001 for S/N PKLBSK9287. Confirm whether the -01 dash suffix is the same listed part; it determines whether the hub is an affected part.
- **Missing fact:** Current engine flight-cycle counter and the counter at the effective date (2025-10-29) are not supplied, so the 100-flight-cycle point cannot be computed.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0029 is not listed in Table 1, so it is not matched.
- **Note:** The record has no events, so no engine shop visit since the effective date is recorded; action is tied to the next shop visit.
- **Note:** The part-number suffix mismatch is not resolved by the AD text; this screen does not determine the hub's status.

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
