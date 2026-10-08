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
- **Summary:** The V2527-A5 engine is within the AD applicability and its HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in table 1. Removal is required at the next engine shop visit, and no shop visit is recorded, so there is no deadline until one occurs. The cycles-since-new data conflict and must be reconciled.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 5,500 cycles-since-new limit or within 100 flight cycles after the effective date, whichever occurs later. Under the 2025-10-29 reading (1,650 CSN), the limit would be reached about 3,850 cycles after that date, at engine cycle 45,050. No shop visit is recorded, so no deadline can be fixed now.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** The hub's cycles since new are inconsistent: 1,650 on 2025-10-29 and 3,100 now, although engine cycles rose only 1,450 (3,100 is exactly 1,650 plus 1,450). The current value is thus consistent, but the undated 3,100 and the 2023 install date should be confirmed, because the remaining cycles depend on them.
- **Missing fact:** The 2nd-stage hub S/N is a placeholder (SYN-HUB2-0001) and does not match any listed S/N. Its true serial number should be confirmed before it is cleared.
- **Missing fact:** No engine shop visit is recorded. The record cannot show whether any past visit after 2025-10-29 exposed the hub, and any future visit triggers removal.
- **Note:** The earlier NPRM 2025-10764 was superseded by the final rule.
- **Note:** The 2nd-stage hub is not matched, because its S/N is a placeholder and not on the list; this is not evidence that it is unaffected.
- **Note:** Any claimed AMOC or AD record entries were not supplied and are not relied on.

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2533-A5 is within the AD applicability and the AD is in force. Neither installed hub has a P/N and S/N listed in table 1 (the 1st-stage hub S/N PKLBST5012 differs from listed PKLBST5011), so the paragraph (g) removal is not triggered; the installation prohibition continues to bind.
- **Note:** The 1st-stage hub S/N PKLBST5012 is one digit off listed PKLBST5011; a reviewer may wish to confirm the record serial number is transcribed correctly.
- **Note:** The record has no shop visit events; none is needed since no listed part is installed.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2524-A5 is within the in-force AD 2025-19-13 applicability. The HPT 1st-stage hub P/N 2A5001 has an unknown serial number and cycles since new, so whether it is a listed hub cannot be determined; the 2nd-stage hub serial is not in Table 1.
- **Stated timing:** If the 1st-stage hub proves to be a listed S/N, removal is due at the next engine shop visit after 2025-10-29, before exceeding the table limit or within 100 flight cycles after the effective date, whichever occurs later. No shop visit is recorded.
- **Missing fact:** The 1st-stage hub P/N 2A5001 matches the listed part number, but its serial number is unknown, so a match to a Table 1 S/N (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489) cannot be ruled in or out.
- **Missing fact:** The cycles since new of the 1st-stage hub are unknown; they are needed to compare against the removal cycle limit if the hub is a listed one.
- **Missing fact:** No events are recorded, so it is not confirmed whether any engine shop visit has occurred since 2025-10-29. The hub condition is the open question.
- **Note:** An unknown serial number is not evidence that the hub is unaffected.
- **Note:** The 2nd-stage hub P/N 2A4802 matches a listed part number, but its S/N is not in Table 1, so it is not matched.
- **Note:** The NPRM 2025-10764 is superseded by the final rule.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for this directive.
- **Note:** No applicability determination is made for this engine model.
- **Note:** The directive's effective date of 2025-10-29 precedes the question date of 2026-09-26, so the directive itself is in force.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is covered and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed in Table 1 (limit 3,900 cycles since new). A qualifying shop visit occurred 2025-11-12 after the effective date, so removal and replacement is required; the 100-flight-cycle window from the effective date ends at engine cycle 18100.
- **Stated timing:** At the next engine shop visit after 2025-10-29, at the later of reaching the 3,900 cycle limit or 100 flight cycles after the effective date. The hub is at 1,040 cycles, far below its limit, so the 100-cycle date governs: by engine flight cycle 18,100. The shop visit already induced on 2025-11-12 (engine cycle 18,040) is the next shop visit, so the hub is to be removed and replaced by 18,100 as read here.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The shop visit qualification is only asserted by the operator record; confirm the induction meets the AD definition (separation of major mating flanges, not transport-only or field maintenance in lieu of on-wing).
- **Missing fact:** The 1st-stage hub serial SYN-HUB1-0005 is not in Table 1, so it is not matched; no missing data, but confirm the serial is recorded correctly.
- **Note:** Screening aid only; not a compliance determination.
- **Note:** Engine cycles at the effective date were 18,000, so 100 cycles after gives 18,100; current reading is 18,040, leaving 60 cycles.
- **Note:** Component remaining cycles computed as 3,900 minus 1,040.
- **Note:** No AMOC is claimed in the record.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and the engine model is covered. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287 is listed in table 1 with a 100-cycle removal limit. Removal is triggered at the next engine shop visit, no earlier than 100 flight cycles after the effective date, so no shop visit-independent deadline is established.
- **Stated timing:** At the next engine shop visit after 2025-10-29, or within 100 flight cycles after the effective date, whichever occurs later. The record shows no shop visit yet, so there is no fixed deadline apart from the 100-cycle floor (engine cycle 25600 by the 2025-10-29 reading).
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** No engine shop visit is recorded. The timing of the next shop visit determines when removal is due; the record cannot show whether an event qualifies under paragraph (i)(2).
- **Note:** The hub's cycles since new (90) are 10 below the listed limit of 100. The 100-cycle limit will be passed soon, but under the 'whichever occurs later' wording removal is still tied to the next shop visit.
- **Note:** The hub was installed 2025-09-30, before the effective date, so the paragraph (h) prohibition does not apply to that installation. It would apply to any later installation of a listed hub.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0006 is not listed in table 1 and is not matched.
- **Note:** The record shows no AD records or AMOC claims.
- **Unresolved locator:** 2025-18469 (g) table 1, row PKLBSK9287

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and the engine model is covered. The installed HPT 1st-stage hub PKLBSS9200 and HPT 2nd-stage hub PKLBST5005 match Table 1 serial numbers. Removal is required at the next engine shop visit, and no shop visit is recorded, so there is no deadline until one occurs.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before the removal cycle limit or within 100 flight cycles after the effective date, whichever occurs later. The record shows no shop visit, so no fixed deadline can be computed.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Note:** Cycles remaining are computed on 2025-12-01. The 1st-stage hub is at 4,300 against a 4,800 limit, which leaves 500. The 2nd-stage hub is at 2,300 against a 4,000 limit, which leaves 1,700. The smallest is reported.
- **Note:** The record does not show a shop visit, so the event-triggered removal is not yet due. Once a shop visit occurs, the later of the limit or 100 cycles after the effective date governs, which the text does not reduce to a single engine cycle count.
- **Note:** This is a screening aid only and not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows PKLBSS9200 (4,800) and PKLBST5005 (4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 is within the AD and the 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed (limit 6,200 cycles since new). Removal is due at the next engine shop visit, or within 100 flight cycles after the effective date if later; no shop visit is recorded, so action is tied to that event. The 2nd-stage hub serial number is unknown, so its match to the table cannot be settled.
- **Stated timing:** At the next engine shop visit after 2025-10-29, at or after the later of the hub reaching 6,200 cycles since new or 100 flight cycles after the effective date; no deadline until a shop visit occurs.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The 2nd-stage hub serial number is unknown, so it cannot be checked against the four listed 2A4802 serial numbers; a match would add a further removal obligation.
- **Missing fact:** The 2nd-stage hub cycles since new are unknown; needed to compute the removal limit if the part is listed.
- **Note:** Hub cycles since new are 2,500 on 2026-03-10, so 3,700 remain before 6,200. The limit is not reached, so removal is not due before it is; the shop-visit trigger would come only at or after the limit is reached.
- **Note:** Because the 'whichever occurs later' wording makes removal due at a shop visit once the hub passes 6,200 cycles, no engine flight-cycle deadline can be computed without a shop visit date.
- **Note:** No shop visits or AMOC claims are recorded.

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2522-A5 is within the AD's applicability and the AD is in force. The record lists no installed components, so whether an affected HPT 1st- or 2nd-stage hub is installed cannot be determined.
- **Missing fact:** No record of the installed HPT 1st-stage hub P/N, S/N and cycles since new; needed to check against table 1 and the removal cycle limit.
- **Missing fact:** No record of the installed HPT 2nd-stage hub P/N, S/N and cycles since new; needed to check against table 1 and the removal cycle limit.
- **Missing fact:** No event history; shop visits after October 29, 2025 (the effective date) are needed to determine whether the shop-visit trigger in (g) has occurred.
- **Note:** A missing or empty component record is not evidence that affected hubs are absent.
- **Note:** The installation prohibition binds regardless of whether an affected hub is currently installed.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made.
- **Note:** No determination is made on whether the AD applies to this engine model or the installed hub.
- **Note:** The directive was effective 2025-10-29 and is in force on the question date.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and is in force on the question date. Replacement of the full blade set is required only at the next engine shop visit after September 24, 2026 where a 3rd stage blade is exposed; no deadline otherwise.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** The question names document 2026-16954; the correction 2026-18423 fixes a typographical omission in (g) without changing the substance for this screen.
- **Note:** The record shows no events, so no shop visit after the effective date is recorded; no action is triggered now.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The engine is a supported model, but the record shows 3rd stage HPC rotor blades with P/N 6C8368, which is not P/N 6A8353 or 6A8688. The AD applicability is limited to engines with those part numbers installed, so the engine is outside it on the supplied facts.
- **Note:** Blade set serial number is not tracked at set level; this does not affect the result because the part number is not an affected one.
- **Note:** The record lists a single blade set part number; if individual blades of mixed part numbers were installed, the result could differ. The record shows no such mixing.
- **Note:** Correction 2026-18423 only fixed a typo in (g) and does not change this outcome.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has 3rd stage HPC blades P/N 6A8688, so AD 2026-17-03 applies and is in force on 2026-09-30. The shop visit was inducted 2026-09-14, before the 2026-09-24 effective date, so paragraph (g) is not triggered by that visit.
- **Stated timing:** Required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; the 2026-09-14 visit does not count as it was inducted before the effective date.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Note:** The blade removal on 2026-09-30 occurred after the effective date but during a visit inducted 2026-09-14, before it. Under (g) as revised, the trigger is a shop visit after the effective date, so the removal alone does not trigger the action.
- **Note:** The earlier NPRM text keyed the action to blade exposure after the effective date, which would have triggered on the 2026-09-30 removal. The final rule replaced that with the shop-visit wording.
- **Note:** The correction document 2026-18423 only fixes a typographical error; the cited paragraph text is the same in substance.
- **Note:** This is a screening result, not a compliance determination. Any future shop visit with blade exposure would trigger replacement.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 has 3rd stage HPC rotor blade P/N 6A8353 installed, so AD 2026-17-03 applies and is in force as of 2026-10-05. The 2026-10-01 shop visit was inducted after the 2026-09-24 effective date, but the HPC rotor was exposed without any 3rd-stage blade being removed from the drum, so the replacement is not triggered by that visit on the supplied facts. Replacement is due at the next engine shop visit where a 3rd stage blade is exposed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed (removed from the stage 3-8 drum); no deadline otherwise.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** Confirmation that no 3rd stage blade was removed from the stage 3-8 drum at any point during the 2026-10-01 to 2026-10-04 shop visit. The record states only that none was removed when the rotor was exposed on 2026-10-02. A removal at another time in the visit would trigger replacement under paragraph (g) as corrected.
- **Missing fact:** Serial numbers are not tracked at set level, so individual blade identity and any mixed-set status cannot be confirmed. The AD lists part numbers only.
- **Note:** The question names document 2026-16954. Its paragraph (g) as published read 'the 3rd stage HPC rotor is exposed'. Correction 2026-18423 restored 'blade', which ties exposure to the blade removal definition in (h)(2). Under the uncorrected wording, exposing the rotor for inspection on 2026-10-02 might be argued to have triggered replacement. Under the corrected wording it does not on the supplied facts. This is flagged for review.
- **Note:** The operator's record asserts the visit qualifies as an engine shop visit; it is consistent with the (h)(3) definition. The record is not treated as settling the outcome.
- **Note:** No AMOC or AD record claim was supplied.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527E-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so it falls within the proposed applicability. The document is only an NPRM and cannot require action on the question date; no exposure event is recorded.
- **Stated timing:** If adopted as proposed, replacement of the full blade set would be due at the next 3rd stage HPC rotor blade exposure after the effective date of a final rule. No deadline exists now.
- **Note:** Proposed rule only; the final text and effective date could change. Re-screen if a final rule is published.
- **Note:** The record lists no events, so no blade exposure is shown. An empty event list does not by itself confirm that no exposure has occurred.
- **Note:** Blades modified to P/N 6A8353-001 would be eligible parts under the proposal; the record shows the installed P/N as 6A8353 without a suffix.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527-A5 is within the applicability of AD 2025-17-16, which is in force (effective 2025-10-10). The operator is an air carrier and its record shows neither the TLM ALS paragraph B.1 nor the approved maintenance program yet incorporates table 1, so revisions are due within 90 days after the effective date.
- **Stated timing:** Within 90 days after October 10, 2025, i.e. by January 8, 2026, for both the TLM ALS paragraph B.1 revision (g)(1) and the air carrier maintenance/inspection program revision (g)(2).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Note:** Deadline computed as 90 days from 2025-10-10, which is 2026-01-08. The question date is within the window, so the action is not yet overdue.
- **Note:** Applicability is by engine model; the empty installed_components list does not affect it. The required action is a documentation revision, so no flight-cycle deadline applies.
- **Note:** This is a screening aid only, not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is a listed model, so AD 2025-17-16 applies and is in force (effective 2025-10-10). The paragraph (g)(1) ICA/TLM revision is due within 90 days after the effective date; the (g)(2) program revision depends on whether this is air carrier operation, which is unknown.
- **Stated timing:** Within 90 days after October 10, 2025, i.e., by January 8, 2026, for the paragraph (g)(1) TLM/ICA revision. If air carrier operation, the paragraph (g)(2) program revision is due by the same date.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the engine is operated in air carrier operations is unknown; this determines whether the paragraph (g)(2) revision of the approved maintenance or inspection program is also required.
- **Missing fact:** Whether the paragraph (g)(1) and (g)(2) revisions have already been incorporated is not in the record (no ad_records supplied).
- **Note:** The AD applies by engine model regardless of installed parts; no component records were supplied, so no parts are matched. Table 1 lists HPT Stage 1 Hub P/N 2A5001 and HPT Stage 2 Hub P/N 2A4802, but these are inspection tasks inserted in the ALS, not a part-based applicability condition.
- **Note:** The 90-day deadline is calendar-based; no flight-cycle deadline applies.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is within the AD's applicability, and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 with a 6,000-cycle removal limit. The AD is not effective until 2025-10-29, so no action is required yet; removal is tied to the next engine shop visit after the effective date.
- **Stated timing:** Not yet in force on 2025-10-15 (effective 2025-10-29). Once effective, remove and replace the hub at the next engine shop visit after the effective date, before exceeding 6,000 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. No deadline until a shop visit occurs.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** Current engine flight-cycle count is not in the record, so the 100-cycle-after-effective-date limit cannot be converted to an engine cycle counter value.
- **Note:** Component cycles remaining = 6,000 - 990 = 5,010.
- **Note:** The HPT 1st-stage hub S/N SYN-HUB1-0018 is not listed in table 1 and does not match.
- **Note:** No events are recorded, so no shop visit has occurred.
- **Note:** Because the limit is far from reached, the 'whichever occurs later' wording means the requirement is effectively tied to the first shop visit after the effective date and the 100-cycle window; the record does not settle this timing exactly.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The AD is in force and the engine model is covered. The installed HPT 1st-stage hub 2A5001 S/N PKLBSS9200 is listed in table 1 and is already past its 4,800-cycle limit, so replacement is due at the next engine shop visit, but no later than the 100-cycle floor allows only after that visit; no shop visit has occurred.
- **Stated timing:** Remove and replace at the next engine shop visit after 2025-10-29. The hub is already past its 4,800 cycles-since-new limit, so the 100-flight-cycle-from-effective-date alternative controls: the 'whichever occurs later' point is engine cycle 60100. The action is still triggered by a shop visit, and the AD text is ambiguous on whether the deadline is the shop visit or the later of that and 60100.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** No engine shop visit is recorded; whether and when the next shop visit occurs determines when the removal is triggered.
- **Missing fact:** The 2nd-stage hub serial SYN-HUB2-0019 is not in table 1, so it does not match; no missing fact but confirm the serial against the physical part record.
- **Note:** Hub cycles since new were 4,950 on 2025-10-29 and 4,990 on 2025-11-05, consistent with 40 engine cycles; limit 4,800 exceeded by 190 cycles at the question date.
- **Note:** The 60100 figure is 60000 at the effective date plus 100 cycles.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, PKLBSS9200 row, 4,800 cycles

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (2021-11960) was in force on 2022-03-01 and the V2533-A5 is a listed model with the P/Ns 2A5001 and 2A4802 installed. Whether it applies depends on the disk serial numbers appearing in the NMSB Appendix A tables, which were not supplied. Superseding AD 2022-02-09 is not effective until 2022-03-15.
- **Stated timing:** If the disks are listed: at the next engine shop visit after 2021-07-13 or before the disk has accumulated 3,200 FCs since 2021-07-13, whichever occurs first. No shop visit events are recorded, and cycle counts since the effective date are not supplied, so no deadline can be computed.
- **Missing fact:** Content of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1: whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed. This determines applicability.
- **Missing fact:** Content of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1: whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed. This determines applicability.
- **Missing fact:** Flight cycles accumulated by the HPT 1st-stage disk since 2021-07-13, needed to measure against the 3,200 FC limit.
- **Missing fact:** Flight cycles accumulated by the HPT 2nd-stage disk since 2021-07-13, needed to measure against the 3,200 FC limit.
- **Missing fact:** The events list is empty, so it is unknown whether any engine shop visit has occurred since 2021-07-13 or whether a USI was already done. Empty events is not evidence that none occurred.
- **Note:** The engine record lists no serial-number-specific listing status, so matches are by part number only.
- **Note:** The superseding AD 2022-02-09 takes effect 2022-03-15 and will replace this AD's requirements from then on.
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
- **Summary:** The V2533-A5 is a listed model with disks of P/N 2A5001 and 2A4802, but the serial numbers cannot be checked against the NMSB Appendix A tables, which were not supplied. AD 2022-02-09 is a final rule not effective until 2022-03-15, so on 2022-03-01 it cannot yet require action.
- **Missing fact:** Contents of Appendix A, Tables 1 and 2, of IAE NMSB V2500-ENG-72-0713 Rev 1, needed to confirm whether disk S/Ns SYN-DISK1-0020 and SYN-DISK2-0020 are listed, which decides applicability.
- **Missing fact:** Figure 1 to paragraph (g)(1) (image not included) gives the compliance time for high-thrust engines such as the V2533-A5. Without it no flight-cycle deadline can be computed.
- **Missing fact:** Disk flight-cycle history is not in the record and would be needed to apply the Figure 1 threshold.
- **Missing fact:** Disk flight-cycle history is not in the record and would be needed to apply the Figure 1 threshold.
- **Note:** The record shows no events and no ad_records or amoc_claims.
- **Note:** Once the AD takes effect, the (g)(1) and (g)(2) inspection deadlines will depend on the Figure 1 values and the disks' cycle counts.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2530-A5 is a listed model and the installed disks have the listed part numbers (2A5001 and 2A4802). Whether the serial numbers appear in Appendix A, Tables 1 and 2 of the service bulletin is not supplied, so applicability cannot be decided.
- **Stated timing:** If the disks are listed, paragraphs (g)(1) and (g)(2) require the USI within the compliance time in Figure 1 (not reproduced in the supplied text) or within 10 flight cycles after March 15, 2022, whichever occurs later. That 10-cycle window has long passed. The Figure 1 threshold cannot be computed.
- **Missing fact:** Content of Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1: whether HPT 1st-stage disk S/N SYN-DISK1-0021 is listed. This decides applicability under (c)(1).
- **Missing fact:** Content of Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1: whether HPT 2nd-stage disk S/N SYN-DISK2-0021 is listed. This decides applicability under (c)(2).
- **Missing fact:** Figure 1 to paragraph (g)(1) (image not provided): the compliance threshold in flight cycles or shop-visit terms.
- **Missing fact:** Disk cycle counts and inspection history are not in the record. They are needed to measure the Figure 1 threshold and to show whether the USI was already done.
- **Missing fact:** Same for the 2nd-stage disk: its cycle count and USI history are needed to measure Figure 1 and to show whether the USI was already done.
- **Missing fact:** No AD record for 2022-02-09 is supplied, and events is empty. A missing record is not evidence that the inspection was done or is unneeded.
- **Note:** The AD took effect March 15, 2022, and was in force on the question date. It supersedes AD 2021-11-15 (document 2021-11960).
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
- **Summary:** The V2533-A5 engine has an HPT 1st-stage disk P/N 2A5001 S/N PKLBSH1829, which is listed in paragraph (c)(1), so the AD applies. A USI of that disk is required within 10 flight cycles after the July 19, 2021 effective date, which is by 33010 engine flight cycles.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021 (engine at 33000 cycles on that date), so by engine cycle 33010. 4 cycles used by 2021-07-20; 6 remain.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** Table 1 and Table 2 to paragraph (g) are images not included in the text; the listed serial numbers in paragraph (c) were used instead. The tables could add or limit the disks requiring the USI.
- **Missing fact:** The 2nd-stage disk serial number SYN-DISK2-0022 does not match any serial listed in (c)(2), so it is not matched. Confirmation of the actual serial number is needed.
- **Missing fact:** No record of USI accomplishment or of any AMOC was supplied, so whether the USI has already been done is unconfirmed.
- **Note:** Cycle count of 33000 on the effective date is taken from the record reading at 2021-07-19.
- **Note:** This is a screening aid only and not a compliance determination.
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
- **Summary:** The V2533-A5 is a supported, listed model and the AD is in force on 2021-07-20. Applicability depends on whether the installed disk serial numbers appear in Appendix A Tables 1 and 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, and that content was not supplied.
- **Stated timing:** If a disk serial number is listed: at the next engine shop visit after July 13, 2021, or before that disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first.
- **Missing fact:** Appendix A Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided, so it cannot be confirmed whether HPT 1st-stage disk S/N PKLBSH1829 is listed.
- **Missing fact:** Appendix A Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 was not provided, so it cannot be confirmed whether HPT 2nd-stage disk S/N SYN-DISK2-0022 is listed.
- **Missing fact:** Disk cycles accumulated since July 13, 2021 are not in the record. They are needed to compute the 3,200-cycle limit and the engine cycle count at which it falls, if the disk is listed.
- **Missing fact:** Disk cycles accumulated since July 13, 2021 are not in the record. They are needed to compute the 3,200-cycle limit and the engine cycle count at which it falls, if the disk is listed.
- **Note:** Both part numbers match the AD, but applicability turns on the serial number lists, which were not provided.
- **Note:** The engine record shows no events, so no shop visit has been recorded since the effective date.
- **Note:** The engine flight-cycle counter cannot be converted into a disk-cycle deadline without the disk cycles since July 13, 2021.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and applies to the V2527M-A5 model. The installed HPT 2nd-stage hub 2A4802 S/N PKLBSR2100 is listed in table 1, so it must be replaced at the next engine shop visit. No deadline applies until that event.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 6,000 cycles-since-new limit or within 100 flight cycles after the effective date, whichever occurs later. Reading the 'whichever occurs later' as the later of the two bounds, this gives about 22,500 flight cycles by the 6,000-cycle limit. No shop visit is recorded, so no concrete deadline can be computed from the record.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The hub shows 3,500 cycles since new on 2026-10-06 but 1,000 at 2025-10-29. Those two readings conflict with the 2,500 engine cycles flown between those dates, which would give 3,500 on 2025-10-29 and 6,000 on 2026-10-06. The 2,500 cycles remaining uses the stated 3,500 current value. If the hub accumulated the engine's 2,500 cycles since the 2025-10-29 reading, it would be at the limit now.
- **Missing fact:** No engine shop visit is recorded. An event that meets the AD paragraph (i)(2) definition triggers the removal.
- **Missing fact:** The HPT 1st-stage hub S/N is a synthetic placeholder, SYN-HUB1-0023, which is not in table 1. Confirm the actual S/N, since the part is not matched.
- **Missing fact:** No AD record or AMOC claim for AD 2025-19-13 is given. The program revision refers to AD 2025-17-16, a different AD, so it does not address this AD.
- **Note:** Reading (g) as shop visit after the effective date, taken at the later of the cycle limit or 100 cycles after the effective date, removal is tied to a shop visit. No shop visit is on record, so action is event-driven.
- **Note:** The record is internally inconsistent on the hub's cycles since new; resolve it before relying on the remaining-cycles figure.
- **Note:** The 3rd stage HPC rotor blade set is not listed in this AD.
- **Note:** This is a screening aid only and not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (in force since 2026-09-24) applies: V2527M-A5 engine with 3rd stage HPC rotor blade set P/N 6A8688 installed. Replacement with eligible blades is required at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed (removed from the stage 3-8 drum); no deadline otherwise.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum). No calendar or cycle deadline.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** No shop visit after 2026-09-24 is recorded; whether and when a future shop visit exposes a 3rd stage HPC rotor blade determines when replacement is due.
- **Note:** The maintenance program revision and AD 2025-17-16 in the record concern other parts and do not address this AD.
- **Note:** Blade set serial numbers are not tracked at set level; individual blade P/Ns should be confirmed at the shop visit.
- **Note:** The engine's ad_records and amoc_claims hold no entry for this AD.
- **Note:** The 2026-18423 correction only fixes a typographical error in paragraph (g) and does not change the requirement.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527M-A5 is a listed model and the AD is in force (effective 2025-10-10). The only required action is the ALS/program revision, and the record shows it was made on 2025-12-01, within 90 days of the effective date; no further action is triggered by this AD text, and continuing obligations still bind.
- **Stated timing:** The 90-day window after the 2025-10-10 effective date ended 2026-01-08; the record shows the revision on 2025-12-01, so no action is currently due.
- **Missing fact:** The content of the revised TLM ALS and Revision 48 was not supplied, so whether it incorporates table 1 tasks (TASK 72-45-11-200-006 and TASK 72-45-31-200-009) in paragraph B.1 of the Maintenance Scheduling section cannot be confirmed; only the operator's assertion is available.
- **Missing fact:** The engine-record entry only mentions the V2500-A5 TLM; it does not confirm the revision was made to the TLM P/N 2A4408 TASK 05-10-00-990-000-B00 listed in (g)(1)(i).
- **Note:** The AD requires only the revisions; the table 1 inspections are performed at piece-part exposure under other regulations once incorporated.
- **Note:** The record shows the revision on 2025-12-01 and the operator is an air carrier, so both (g)(1) and (g)(2) are asserted done in the one entry; these are operator assertions to verify.
- **Note:** The 3rd stage HPC rotor blade set is not listed in this AD.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model is within the applicability of AD 2025-19-13, which is in force. Neither installed hub matches a P/N and S/N pair in table 1 (the 2nd-stage hub S/N PKLBST5011 is listed only as a 1st-stage hub with P/N 2A5001), so no removal is triggered by the record. The installation prohibition continues to bind.
- **Note:** The 2nd-stage hub serial PKLBST5011 appears in table 1 only for 1st-stage hub P/N 2A5001. The installed part has P/N 2A4802, so it is not matched. Recommend confirming the serial and part number on the record against the physical part data plate.
- **Note:** The 1st-stage hub S/N SYN-HUB1-0024 is not listed in table 1.
- **Note:** The proposed rule 2025-10764 is superseded by the final rule.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model CFM56-5B4/3 is not one of the supported IAE V2500 models, so no applicability determination is made.
- **Note:** No determination of applicability is made for this engine model.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is covered and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1 (limit 6,200 cycles since new). Removal is required at the next engine shop visit; the hub is at 3,600 cycles since new, so the limit does not control and the 100-cycle window after the effective date has already passed.
- **Stated timing:** At the next engine shop visit after October 29, 2025 (the later of that shop visit or the removal cycle limit / 100 flight cycles after the effective date, so the shop visit governs). No fixed deadline otherwise. Installation prohibition for listed hubs applies now.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** The HPT 2nd-stage hub serial number is a synthetic placeholder (SYN-HUB2-0026); it should be confirmed against table 1 serial numbers, though it does not match any listed S/N as recorded.
- **Missing fact:** The cycles-since-new current reading (3,600) conflicts with the 3,000 reading at 2025-10-29 plus 600 engine cycles since; consistent, but confirm the hub's cycles since new.
- **Note:** The 2024 blend repair and repeat ultrasonic inspection of the hub do not remove it from table 1; the AD offers no exception for them.
- **Note:** No shop visit is recorded since the effective date, so removal is not yet triggered by an event.
- **Note:** No AMOC is claimed in the record.
- **Note:** This is a screening aid, not a compliance determination.

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
- **Summary:** The engine is a listed model and its HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches table 1 (limit 4,800 CSN). The AD is in force, and removal is due at the next engine shop visit, which is not before the later of the 4,800 CSN limit or 100 flight cycles after 2025-10-29.
- **Stated timing:** At the next engine shop visit after 2025-10-29, which may not be before the later of (a) the hub reaching 4,800 CSN and (b) 100 flight cycles after the effective date. With no shop visit recorded, no event has triggered removal yet. The cycle floor is engine flight cycle 15,100 (and 4,800 CSN is engine cycle 15,300).
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The claimed AMOC extending the removal limit to 5,300 CSN has no FAA approval reference or letter. It cannot be relied on, so the 4,800 CSN table limit is used.
- **Missing fact:** No engine shop visit is recorded. Whether and when a shop visit under paragraph (i)(2) occurs determines when removal is triggered.
- **Note:** The 1st-stage hub is 4,750 CSN at 2026-01-20 (50 cycles below the 4,800 limit). The record is consistent: 4,500 CSN at engine cycle 15,000 plus 250 cycles gives 4,750 CSN.
- **Note:** The hub reaches 4,800 CSN at engine cycle 15,300. The 100-cycle floor is engine cycle 15,100, already passed. So removal is due at the first shop visit, if it occurs after the hub reaches 4,800 CSN; a shop visit earlier than that is not yet required to remove it.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0027 is not listed in table 1, so it is not matched.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, PKLBSS9200 row, 4,800 cycles

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is listed and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 matches Table 1 (limit 4,000 cycles since new). The hub is at 1,400 cycles, so removal is due at the next engine shop visit, and no deadline applies until then. The 'not applicable' record is a claim that does not fit the installed hub.
- **Stated timing:** At the next engine shop visit after October 29, 2025, before exceeding the 4,000-cycle removal limit or within 100 flight cycles after the effective date, whichever occurs later. The 100-cycle window from the effective date has already passed, so the shop visit event controls. No fixed date is set without a shop visit.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0028 is not in Table 1, so it does not match. This hub is not an affected part, but the hub S/N should be confirmed against the physical part.
- **Missing fact:** The record shows 1,000 cycles since new at 2025-10-29 and 1,400 at the question date, while the engine flew 400 cycles in the same span. This is consistent, but the current 1,400 should be confirmed because the remaining-cycle count depends on it.
- **Missing fact:** No shop visit is recorded. Any future engine shop visit, as defined in (i)(2), would trigger removal and replacement of the 2nd-stage hub.
- **Note:** The record's 'not applicable / no affected hubs installed' entry conflicts with the installed hub PKLBST5005 listed in Table 1 and should be reviewed.
- **Note:** The engine has no events recorded, so no shop visit has been triggered.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2525-D5 is within the AD applicability and the AD is in force. The HPT 1st-stage hub S/N PKLBSK9287 matches the table serial number but the installed P/N is 2A5001-01 versus listed 2A5001, so whether it is an affected part needs review. The 2nd-stage hub S/N is not listed.
- **Stated timing:** If the 1st-stage hub is confirmed affected: at the next engine shop visit after October 29, 2025, at or after the later of exceeding the 100-cycle removal limit or 100 flight cycles from the effective date. The hub is already past the 100-cycle limit, so the later criterion is the 100 flight cycles after the effective date. No shop visit is recorded.
- **Missing fact:** Installed P/N is 2A5001-01 while the AD lists 2A5001; confirm whether the -01 dash number is the same listed part. If so, the hub is affected and removal is required.
- **Missing fact:** Engine flight-cycle counter at the effective date (2025-10-29) is not in the record; needed to compute the 100-cycle-after-effective-date point.
- **Missing fact:** No engine shop visit is recorded; the removal is triggered at the next shop visit after the effective date, so any such visit and its qualification under (i)(2) must be confirmed.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0029 is not listed in table 1, so no action arises from it.
- **Note:** The 1st-stage hub is 2300 cycles past its listed limit (2400 vs 100).
- **Note:** This is a screening aid only, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, row PKLBSK9287, limit 100

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
