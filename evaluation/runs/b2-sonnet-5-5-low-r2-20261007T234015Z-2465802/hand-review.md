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
- **Summary:** The V2527-A5 is within the applicability and its HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 is listed in Table 1 (limit 5,500 cycles since new). The required removal is tied to the next engine shop visit; no shop visit is recorded, so no deadline is triggered now. The cycles-since-new data conflict, so the position relative to the limit needs review.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding the 5,500-cycle limit or within 100 flight cycles after the effective date, whichever occurs later. The 100-cycle window after 2025-10-29 ended at engine cycle 41,300 and has passed, so the shop visit is the operative trigger. No shop visit is recorded.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** Current cycles_since_new (3,100) conflicts with the 2025-10-29 reading of 1,650 plus 1,450 engine cycles flown since (about 3,100, which is consistent only if the hub's cycles track the engine's). The reading history is unclear, so confirm the hub's actual cycles since new; the 2,400 remaining cycles uses 3,100.
- **Missing fact:** The 2nd-stage hub serial number is a synthetic placeholder (SYN-HUB2-0001) and is not in Table 1, so there is no match; confirm the actual serial number.
- **Missing fact:** No engine shop visit is recorded. Confirm whether any shop visit under paragraph (i)(2) has occurred since 2025-10-29, since that would have triggered the removal.
- **Note:** Screening aid only; not a compliance determination.
- **Note:** The NPRM 2025-10764 is superseded by the final rule.
- **Note:** No AMOC or AD records were supplied.
- **Unresolved locator:** 2025-18469 (g) Table 1, row PKLBST5011, 5,500 cycles

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2533-A5 is within the AD applicability, and the AD is in force on the question date. Neither installed hub has a P/N and S/N pair listed in table 1 (the 1st-stage hub S/N PKLBST5012 differs from listed PKLBST5011), so paragraph (g) is not triggered on the supplied record.
- **Note:** PKLBST5012 is a near-match to listed PKLBST5011 but is a different serial number; a reviewer may wish to confirm the serial number was transcribed correctly from the part records.
- **Note:** The AD applies to the engine model regardless of installed hubs, so the installation prohibition binds on this engine.
- **Note:** This is a screening result only, not a compliance determination.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model is within AD 2025-19-13 applicability and the AD is in force. The HPT 1st-stage hub serial number and cycles since new are unknown, so a match to table 1 cannot be ruled in or out; the 2nd-stage hub serial is not listed.
- **Missing fact:** The 1st-stage hub P/N 2A5001 matches the listed part number, but its serial number is unknown. It cannot be compared to the four listed serial numbers, so whether paragraph (g) applies is undetermined.
- **Missing fact:** The cycles since new of the 1st-stage hub is unknown. If the serial is listed, it is needed to compare against the removal cycle limit (100 to 6,200).
- **Missing fact:** The effective-date flight-cycle baseline and whether any engine shop visit has occurred or is planned are not in the record, and the record shows no events. These would be needed to fix the timing.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0003 is not listed in table 1, so it is not an affected part under this reading.
- **Note:** An unknown serial number is not evidence that the 1st-stage hub is unaffected.
- **Note:** Screening aid only, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the supported IAE V2500 models, so no applicability determination is made for this directive.
- **Note:** No determination is made on applicability or required action for this engine model.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and covers the V2527E-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed in Table 1 with a 3,900-cycle limit. The recorded shop visit on 2025-11-12 is after the effective date and the hub is under its limit, so the 100-cycle alternative is the later date and removal is due within 100 flight cycles after the effective date.
- **Stated timing:** Because the 'whichever occurs later' wording is applied, the later of the next shop visit before exceeding the removal limit or 100 flight cycles after 2025-10-29 governs. The hub is at about 1,040 cycles against a 3,900 limit, so the limit is not reached. The 100-cycle point after the effective date is engine flight cycle 18,100. The engine is already in a qualifying shop visit (asserted) at 18,040, so removal and replacement of the hub is due by engine flight cycle 18,100.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The operator's record asserts the 2025-11-12 induction is an engine shop visit under the AD definition; the separation of major mating flanges and the exclusions in (i)(2) should be confirmed.
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0005 is not listed in Table 1, so it does not match. This is noted only because the hub's identity should be confirmed from the records.
- **Note:** The cycle limit is expressed in cycles since new; the hub had 1,000 cycles at 2025-10-29 and 1,040 on 2025-11-12, so 2,860 cycles remain to the 3,900 limit.
- **Note:** The 100-cycle deadline is computed from the engine counter of 18,000 at the effective date.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and the engine model is covered. The installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287 is listed in table 1 with a removal limit of 100 cycles since new, so removal is required at the next engine shop visit, which has not yet occurred.
- **Stated timing:** At the next engine shop visit after 2025-10-29, at the later of: before the hub exceeds 100 cycles since new, or within 100 flight cycles after the effective date. Because the hub has used 90 of 100 cycles and the 100-flight-cycle window runs later, the engine-cycle deadline is 25600 if the 'later of' reading applies. No shop visit is recorded, so the action is event-triggered.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** The HPT 2nd-stage hub serial number SYN-HUB2-0006 is not in table 1, so no match was made. No other record in the supplied engine record contradicts this.
- **Missing fact:** No engine shop visit is recorded. Whether and when one occurs determines when the removal is triggered.
- **Note:** The hub was installed 2025-09-30 and had 60 cycles since new at 2025-10-29, then 90 at 2025-11-20, consistent with 30 engine cycles over that period.
- **Note:** The hub's cycles at the effective date (60) are below its 100-cycle limit, so the later-of reading applies the 100-flight-cycle window from the effective date.
- **Note:** The hub was installed before the effective date, so the paragraph (h) prohibition was not breached by its installation.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, row PKLBSK9287

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and applies to the V2531-E5. Both installed hubs match Table 1 entries, so removal is required at the next engine shop visit after 2025-10-29, no earlier than 100 flight cycles after the effective date, and not before the applicable limit is exceeded. No shop visit is recorded, so there is no deadline now.
- **Stated timing:** At the next engine shop visit after 2025-10-29, at the later of (a) before exceeding the removal cycle limit and (b) 100 flight cycles after the effective date (engine cycle 30100, already passed). The 1st-stage hub limit is 4,800 CSN and the 2nd-stage hub limit is 4,000 CSN. The hubs are at 4,300 and 2,300 CSN, so the cycle-limit prong is not yet reached. No shop visit is recorded, so no fixed date is established.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Note:** Smallest remaining cycles: 1st-stage hub 4,800-4,300=500; the 2nd-stage hub has 1,700 remaining.
- **Note:** Removal at the next shop visit is required even if it occurs before the limit, once the 100-cycle window after the effective date has passed (engine cycle 30100 passed). The 'whichever occurs later' wording is ambiguous on this point, so the later-of reading is applied literally. Review the exact reading with the authority.
- **Note:** No events are recorded, so no shop visit has occurred. No AD or AMOC claims were supplied.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows PKLBSS9200 and PKLBST5005

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 is within the AD, and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is listed in table 1 (limit 6,200 cycles since new). Removal is due at the next engine shop visit, which has not yet occurred. The 2nd-stage hub serial number is unknown, so it cannot be cleared.
- **Stated timing:** Under (g), the action is due at the next engine shop visit after Oct 29, 2025, at or after the later of reaching the 6,200 cycles-since-new limit or 100 flight cycles after the effective date (engine counter 50,100). The hub had 2,500 cycles at the 2026-03-10 reading, so the limit is not yet reached; no shop visit is recorded. The 'whichever occurs later' reading is applied.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub serial number is unknown, so a match to the table 1 2A4802 entries cannot be ruled in or out. If it matches, a separate removal obligation applies.
- **Missing fact:** The 2nd-stage hub cycles since new are unknown, which are needed to compare against its removal cycle limit if it is a listed serial number.
- **Note:** The record shows no events, so no engine shop visit has been recorded since the effective date.
- **Note:** The 3,700 remaining cycles is 6,200 minus 2,500 at the latest reading.
- **Note:** The 1st-stage hub's cycles since new were 2,000 on 2025-10-29, below its limit. The engine counter after 100 cycles from the effective date is 50,100, already passed, so the limit governs the 'later' timing.
- **Note:** No AMOC is claimed in the record.

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine model V2522-A5 is within the AD applicability and the AD is in force. The record lists no installed components, so whether an affected HPT 1st- or 2nd-stage hub is installed cannot be determined; an empty record is not evidence the parts are absent.
- **Missing fact:** No record of the installed HPT 1st-stage hub P/N, S/N and cycles since new; needed to match against table 1 to paragraph (g).
- **Missing fact:** No record of the installed HPT 2nd-stage hub P/N, S/N and cycles since new; needed to match against table 1 to paragraph (g).
- **Missing fact:** No shop visit history; needed to identify the next engine shop visit after October 29, 2025 and the engine flight-cycle counter.
- **Note:** The earlier NPRM 2025-10764 is superseded by the final rule and was not relied on for requirements.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made.
- **Note:** The installed hub P/N and S/N appear in the AD table, but because the model is outside the supported scope no match or determination is made.
- **Note:** The AD was effective 2025-10-29, so it is in force on the question date.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527-A5 is a listed model with 3rd stage HPC rotor blades P/N 6A8353 installed, so the AD applies and is in force on 2026-10-05. Replacement of the full blade set is required only at the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed; no shop visit is recorded, so no deadline is set.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no deadline otherwise.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** The event list is empty, so no shop visit after the effective date is recorded. Absence of recorded events is not confirmation that none has occurred.
- **Note:** Blade serial numbers are not tracked at set level; the AD lists part numbers only.
- **Note:** The correction document 2026-18423 fixes a typographical error in paragraph (g) and does not change the substance.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** The engine is a supported model, but the record shows 3rd stage HPC rotor blades with P/N 6C8368, which is not P/N 6A8353 or 6A8688 and is a part eligible for installation under (h)(1)(i). The AD applicability requires an installed 6A8353 or 6A8688 blade, so the engine falls outside it on the supplied record.
- **Note:** Blade set serial number is not tracked at set level; the determination relies on the recorded set part number 6C8368. If individual blades of a different P/N are mixed in the set, this would need to be confirmed against the blade-level records.
- **Note:** Question directive 2026-16954 was corrected by 2026-18423 (adds 'blade' in paragraph (g)); the correction does not change this outcome.
- **Note:** This is a screening aid and not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 engine has P/N 6A8688 3rd stage HPC blades installed, so AD 2026-17-03 applies. The shop visit was inducted 2026-09-14, before the 2026-09-24 effective date, so the paragraph (g) replacement is not triggered by that visit even though blade exposure occurred on 2026-09-30.
- **Stated timing:** No deadline now. Replacement is due at the next engine shop visit after 2026-09-24 in which a 3rd stage HPC rotor blade is exposed.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The blade exposure on 2026-09-30 is after the effective date, but the visit was inducted 2026-09-14, before it. Paragraph (g) is keyed to the shop visit after the effective date, per the FAA's stated intent in the preamble.
- **Note:** The blades remain P/N 6A8688, so the obligation remains open for the next qualifying shop visit.
- **Note:** The record shows the blades are still P/N 6A8688, and no replacement is recorded.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so AD 2026-17-03 applies and has been in force since 2026-09-24. The 2026-10-01 shop visit began after the effective date, but no 3rd-stage blade was removed from the drum, so no replacement was triggered by it; action is due at the next engine shop visit where the blades are exposed.
- **Stated timing:** At the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed (removed from the stage 3-8 drum). No deadline applies until that event.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** The record gives P/N 6A8353 for the set and does not track serial numbers at set level. Confirm that every blade in the set has the listed P/N and that none has been modified to an eligible P/N (6A8353-001), since a modified set would change the result.
- **Note:** The question names 2026-16954, but its paragraph (g) omitted the word 'blade', and correction 2026-18423 restores it. The outcome is the same under either wording because no blade was removed.
- **Note:** The exposure on 2026-10-02 was an inspection exposure of the rotor and no blade was removed, so it is not a blade exposure under (h)(2).
- **Note:** Whether the operator's record is right that the visit qualifies as an engine shop visit does not change the outcome here.

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527E-A5 engine has 3rd stage HPC rotor blades P/N 6A8353 installed, so it is within the proposed applicability. The document is only an NPRM on the question date, so no action is required now.
- **Stated timing:** None while proposed. If adopted as written, replacement of the full blade set would be due at the next 3rd stage HPC rotor blade exposure after the effective date of a final AD.
- **Note:** Proposed rule only; the final text may change after comments (due 2026-01-02).
- **Note:** The record shows no events, so no blade exposure is recorded.
- **Note:** Blade set serial numbers are not tracked at set level; this does not affect applicability because the AD lists part numbers only.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527-A5 is a listed model, so AD 2025-17-16 applies and was in force on the question date (effective 2025-10-10). The record says the TLM ALS paragraph B.1 and the approved maintenance program do not yet incorporate table 1, so the revisions are required within 90 days after the effective date.
- **Stated timing:** Within 90 days after the effective date of 2025-10-10, i.e. by 2026-01-08, under both (g)(1) and (g)(2). The question date of 2025-11-15 falls inside that window.
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Note:** The AD requires revising documents (the TLM ALS and the maintenance program). It does not depend on installed parts, and no component records were supplied or needed.
- **Note:** The 90-day deadline is computed as 2025-10-10 plus 90 days, which gives 2026-01-08. Verify the date.
- **Note:** The operator record says it is an air carrier operation, so both (g)(1) and (g)(2) are relevant.
- **Note:** The earlier NPRM (2024-26092) is superseded by the final rule and is not relied on for requirements.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is within the applicability of AD 2025-17-16, which is in force on 2025-11-15. The required ALS/TLM revision is due within 90 days after the effective date, i.e. by 2026-01-08; the air carrier program revision depends on an unknown operator fact.
- **Stated timing:** Paragraph (g)(1) TLM revision within 90 days after the 2025-10-10 effective date, i.e. by 2026-01-08. If air carrier operation, the (g)(2) program revision is due by the same date.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the engine is used in air carrier operations is unknown; this determines whether paragraph (g)(2) (revision of the approved maintenance or inspection program) also applies.
- **Missing fact:** Whether the TLM revision under (g)(1) and any program revision under (g)(2) have already been done is not in the record (no AD records supplied).
- **Note:** The action is a documentation revision applying to the engine model; it does not depend on installed parts, so the empty component list does not affect applicability.
- **Note:** The proposal 2024-26092 is superseded by the final rule and was not relied on.
- **Note:** 90 days after 2025-10-10 is 2026-01-08. No flight-cycle deadline applies.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is a listed model and its HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 matches Table 1 (limit 6,000 cycles since new). The AD is published but not effective until 2025-10-29, so no action is required yet; removal is tied to a future engine shop visit.
- **Stated timing:** At the next engine shop visit after the effective date (2025-10-29), before exceeding the 6,000 cycles-since-new limit or within 100 flight cycles after the effective date, whichever occurs later. No deadline absent a shop visit.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** Engine flight-cycle counter is not in the record, so the 100-cycle-from-effective-date outer bound cannot be expressed as an engine cycle count.
- **Note:** The 1st-stage hub S/N SYN-HUB1-0018 is not listed in Table 1 and is not matched.
- **Note:** Remaining cycles computed as 6,000 minus 990 = 5,010.
- **Note:** No events are recorded, so no shop visit has occurred or is known to be planned.
- **Note:** Screening aid only; not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The AD is in force and the engine model is covered. The installed HPT 1st-stage hub 2A5001 S/N PKLBSS9200 is listed in Table 1, and its removal cycle limit of 4,800 is already exceeded. Replacement is therefore due at the next engine shop visit, and no later than 100 flight cycles after the effective date if that is later than the limit.
- **Stated timing:** Replace at the next engine shop visit after 2025-10-29. Because the cycle limit was already exceeded on the effective date, the 'whichever occurs later' language points to the later of the shop visit and 100 flight cycles after the effective date. The 100-cycle point is engine cycle 60100. A literal reading gives the later of the two events. Whether the AD requires removal by 60100 even without a shop visit is ambiguous.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The 2nd-stage hub S/N is a synthetic placeholder, SYN-HUB2-0019. It does not match any Table 1 entry, so it is not treated as affected. Confirm the actual S/N against the physical part and its records.
- **Missing fact:** No shop visits are recorded. The next engine shop visit, which triggers removal under the AD definition, has not occurred or is not known.
- **Missing fact:** The hub's cycles since new on 2025-11-05 is 4990, but the 2025-10-29 reading is 4950. The two readings differ by 40, which matches the engine cycle change. Confirm the current value.
- **Note:** Component cycles remaining is computed as 4,800 minus 4,990, which is -190 on 2025-11-05.
- **Note:** The 100-cycle point is computed from the engine count on the effective date, 60,000, giving 60,100. The engine is at 60,040 on 2025-11-05.
- **Note:** The NPRM 2025-10764 is superseded by the final rule and is not relied on.
- **Note:** No AMOC claims or AD records were supplied.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (2021-11960) was in force on 2022-03-01 and covers the V2533-A5, but whether the installed disk serial numbers appear in the NMSB Appendix A tables is not known, so applicability cannot be decided. If listed, (g)(1)/(g)(2) would apply, with a deadline that cannot be computed without flight-cycle data.
- **Stated timing:** If the disks are listed: at the next engine shop visit after 2021-07-13 or before the disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. The record has no cycle counts and no shop visit events.
- **Missing fact:** Appendix A Table 1 and Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 were not supplied, so it is unknown whether HPT 1st-stage disk S/N SYN-DISK1-0020 or HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed. This decides applicability.
- **Missing fact:** Flight cycles accumulated by the disk since 2021-07-13 are not in the record, so the 3,200-cycle limit cannot be computed.
- **Missing fact:** Flight cycles accumulated by the disk since 2021-07-13 are not in the record, so the 3,200-cycle limit cannot be computed.
- **Missing fact:** No AD status record or USI accomplishment record is given. Whether the USI was already done is unknown.
- **Note:** The part numbers match those named in paragraph (c), but the serial numbers could not be checked against the listing.
- **Note:** AD 2022-02-09 (2022-02574) supersedes this AD effective 2022-03-15. That is after the question date, so this question concerns AD 2021-11-15 only, and the superseding AD will need its own screen.
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
- **Summary:** AD 2022-02-09 is published but not effective until 2022-03-15, so it cannot require action on 2022-03-01. The engine model is in scope and carries the listed part numbers, but the serial numbers cannot be checked against the service bulletin tables, which were not supplied, so applicability is unknown.
- **Stated timing:** Not yet in force. After the effective date of 2022-03-15, if the disks are listed, the inspection is due per Figure 1 to paragraph (g)(1) (image not provided) or within 10 FCs after the effective date, whichever is later.
- **Missing fact:** Whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1 (the tables were not provided). It decides applicability.
- **Missing fact:** Whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713 Rev 1 (the tables were not provided). It decides applicability.
- **Missing fact:** Figure 1 to paragraph (g)(1), which sets the compliance threshold, is an image that was not supplied. Without it no deadline can be computed.
- **Missing fact:** Disk cycle counts and history are not in the record. They are needed to apply the Figure 1 threshold.
- **Missing fact:** Disk cycle counts and history are not in the record. They are needed to apply the Figure 1 threshold.
- **Note:** This is a screening aid only and not a compliance determination.
- **Note:** The V2533-A5 is a high-thrust model, so the (g)(1) and (g)(2) paths would apply if the serial numbers are listed.
- **Note:** The record shows no events, so no shop visit or prior inspection is recorded.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The V2530-A5 is a supported model with installed HPT disks of P/N 2A5001 and 2A4802, but applicability depends on whether the disk serial numbers appear in Appendix A of the service bulletin, which was not supplied. Action status cannot be set until that is confirmed.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (not provided): needed to confirm whether HPT 1st-stage disk S/N SYN-DISK1-0021 is listed.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (not provided): needed to confirm whether HPT 2nd-stage disk S/N SYN-DISK2-0021 is listed.
- **Missing fact:** Figure 1 to paragraph (g)(1) compliance time (image not included in the text): needed to compute the inspection deadline if the disks are listed.
- **Missing fact:** Current engine/disk flight cycle counts and any prior USI record are not in the engine record; needed to compute a deadline.
- **Note:** Part numbers match the directive's listed part numbers, but serial numbers cannot be checked against the unsupplied Appendix A tables.
- **Note:** The record has no events, so no prior USI or shop visit is recorded. Missing records are not evidence the disks are unaffected.
- **Note:** AD 2022-02-09 supersedes AD 2021-11-15.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The engine is a V2533-A5 with an HPT 1st-stage disk P/N 2A5001, S/N PKLBSH1829, which is listed in paragraph (c)(1). The AD is in force on the question date, and a USI of the 1st-stage disk is due within 10 flight cycles after the July 19, 2021 effective date.
- **Stated timing:** Within 10 flight cycles after the effective date of July 19, 2021, i.e. by engine flight cycle counter 33010 (counter was 33000 on 2021-07-19). 4 cycles have been flown since then, leaving 6.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** Table 1 and Table 2 to paragraph (g) are images not included in the text, so inclusion of the 1st-stage disk in Table 1 could not be checked. Paragraph (c) still lists S/N PKLBSH1829 for applicability.
- **Note:** The 2nd-stage disk S/N SYN-DISK2-0022 does not match any serial number listed in (c)(2), so it does not trigger applicability or paragraph (g)(2).
- **Note:** The deadline is computed from the cycle reading of 33000 on the effective date. No record shows the USI has been done; none is in the events list.
- **Note:** This is a screening aid, not a compliance determination.
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
- **Summary:** The V2533-A5 is a supported model and the AD is in force (effective 2021-07-13). Applicability depends on whether the installed disk serial numbers appear in Appendix A Tables 1 and 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, which were not supplied, so the screen cannot decide it.
- **Stated timing:** If either disk is listed: at the next engine shop visit after 2021-07-13 or before that disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. The disk cycle count since the effective date is not in the record.
- **Missing fact:** Content of Appendix A Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1, needed to check whether HPT 1st-stage disk S/N PKLBSH1829 (P/N 2A5001) is listed.
- **Missing fact:** Content of Appendix A Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, needed to check whether HPT 2nd-stage disk S/N SYN-DISK2-0022 (P/N 2A4802) is listed.
- **Missing fact:** HPT 1st-stage disk flight cycles accumulated since 2021-07-13, needed to compute the 3,200-cycle limit if the disk is listed.
- **Missing fact:** HPT 2nd-stage disk flight cycles accumulated since 2021-07-13, needed to compute the 3,200-cycle limit if the disk is listed.
- **Note:** Part numbers match, but serial numbers cannot be checked against the listing without the NMSB. The record has no events, so no shop visit is recorded since the effective date.
- **Note:** Engine cycle counts (33,000 on 2021-07-19 and 33,004 on 2021-07-20) are engine totals, not disk cycles since the effective date, so no deadline counter can be computed.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 is in force and applies to the V2527M-A5. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 (limit 6,000 cycles since new), so removal is required at the next engine shop visit; no shop visit is recorded, so no date can be set.
- **Stated timing:** At the next engine shop visit after 2025-10-29, before exceeding 6,000 cycles since new or within 100 flight cycles after the effective date, whichever occurs later. No shop visit is recorded, so no fixed deadline can be computed.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The 2nd-stage hub shows 1,000 cycles since new on 2025-10-29 but 3,500 at 2026-10-06 with engine cycles up 2,500. This is consistent (1,000+2,500), but the 1,000 reading against installation in 2024 should be confirmed. The 2,500 remaining uses the current 3,500 figure.
- **Missing fact:** No engine shop visit is recorded after 2025-10-29. Any future shop visit meeting the paragraph (i)(2) definition would trigger removal of the hub.
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0023 does not match any listed S/N, so it is not an affected part on the record. The record's S/N should still be verified against the hardware.
- **Missing fact:** The record has no entry for AD 2025-19-13. The maintenance program revision cites AD 2025-17-16, a different AD that was not supplied, so it cannot be used for this AD.
- **Note:** The 2nd-stage hub has 2,500 cycles remaining to the 6,000 limit (3,500 now). Under the 'whichever occurs later' wording, the deadline is tied to a shop visit rather than a fixed cycle count.
- **Note:** The 2025-12-01 maintenance program revision refers to AD 2025-17-16, not this AD, and does not show action under 2025-19-13.
- **Note:** The 3rd stage HPC rotor blade set is not listed in this AD and is not relevant.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (in force since 2026-09-24) applies: V2527M-A5 engine with 3rd stage HPC blade set P/N 6A8688 installed. Replacement with eligible parts is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed; no such event is recorded, so no deadline is set.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** No engine shop visit or blade exposure after 2026-09-24 is recorded; whether one has occurred is unconfirmed. Such an event would trigger the replacement.
- **Note:** The record's maintenance program revision cites AD 2025-17-16, a different directive; it does not address this AD and is not evidence of action under it.
- **Note:** The HPT hub records relate to other directives and are not relevant to this AD.
- **Note:** The correction document 2026-18423 fixes a typographical error in paragraph (g); the screen uses the corrected wording.
- **Note:** The record has no shop visit entries, so none is assumed. This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527M-A5 is within the applicability of AD 2025-17-16, which was in force from 2025-10-10. The recorded 2025-12-01 revision of the V2500-A5 TLM ALS and the approved maintenance program falls within the 90-day window, so no further action is triggered by the record, subject to verification.
- **Stated timing:** The 90-day window after the 2025-10-10 effective date ended 2026-01-08. The recorded revision on 2025-12-01 is within it.
- **Missing fact:** The content of Revision 48 and the TLM ALS revision was not supplied, so it cannot be confirmed that they incorporate table 1 (TASK 72-45-11-200-006 and TASK 72-45-31-200-009) in paragraph B.1 of the Maintenance Scheduling section as required.
- **Note:** The AD requires only the ALS and program revisions. The inspections themselves happen at piece-part exposure under other regulations.
- **Note:** The operator's record is an assertion that has not been verified.
- **Note:** The engine-record data in the cycle readings are not used for any deadline, because the AD sets no cycle-based compliance time.
- **Note:** The cycles_since_new figures for the HPT 2nd-stage hub are inconsistent: 3500 at snapshot against 1000 on 2025-10-29, with 2500 engine cycles flown since. They also exceed the 3500 value implied by installation. This does not affect the screen.
- **Note:** The 3rd stage HPC rotor blade set is not listed in the AD and is not matched.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is within the AD applicability and the AD is in force. Neither installed hub matches a listed P/N and S/N pair (the 2nd-stage hub S/N PKLBST5011 is listed only against P/N 2A5001, not 2A4802), so no removal is triggered by the supplied facts.
- **Note:** The 2nd-stage hub S/N PKLBST5011 matches a serial listed for the 1st-stage hub P/N 2A5001, but the P/N differs. Verify the installed hub's P/N and S/N against the data plate or records in case of a transcription error. If it were actually P/N 2A5001, the screen would change.
- **Note:** The engine record contains no events, so no engine shop visit is recorded.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model CFM56-5B4/3 is not one of the supported IAE V2500 models, so no applicability determination is made.
- **Note:** No determination is made about this engine against the directive.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a listed model and carries HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489, which is in table 1 (limit 6,200 cycles since new). Removal is tied to the next engine shop visit after 2025-10-29, and no shop visit is recorded, so action is required on that event.
- **Stated timing:** At the next engine shop visit after October 29, 2025, provided the hub has not exceeded 6,200 cycles since new at that point; if it has, then within 100 flight cycles after the effective date. The text says 'whichever occurs later', so no deadline applies absent a shop visit.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** No engine shop visit after 2025-10-29 is recorded, so the trigger event has not been shown to occur. The future shop visit date and the hub cycles since new at that time are needed.
- **Missing fact:** The current cycles-since-new is 3600, but the 2025-10-29 reading is 3000 and the cycles accrued (600) match the engine's 600 cycles since then. Confirm the 3600 reading for the cycles remaining calculation (6,200 - 3,600 = 2,600).
- **Missing fact:** The 2nd-stage hub S/N SYN-HUB2-0026 is not in table 1, so it does not match. Confirm the S/N is accurate.
- **Note:** The 2024 blend repair and the repeat ultrasonic inspection do not appear in the AD as terminating or exempting the hub, and no AMOC is recorded.
- **Note:** Cycles since new of 3600 is below the 6,200 limit, so the removal is event-driven and not deadline-driven.
- **Note:** Screening aid only; not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1, PKLBST7489 row, 6,200 cycles

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
- **Summary:** The engine is a listed model and its HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches Table 1 (limit 4,800 CSN). The required removal is due at the next engine shop visit, and no later than that visit's timing allows; no shop visit is recorded, so no deadline is fixed now.
- **Stated timing:** At the next engine shop visit after 2025-10-29. The wording 'before exceeding the limit or within 100 flight cycles after the effective date, whichever occurs later' makes the removal limit the later point only if it falls after the 100-cycle point. The hub reached 4,500 CSN on 2025-10-29 and 4,750 CSN now, so 50 cycles remain to 4,800 CSN. The 100-flight-cycle point from the effective date is engine cycle 15,100, which has already passed (engine now at 15,250). The 4,800 CSN limit corresponds to engine cycle about 15,300. Removal is therefore due at the next shop visit, which must occur before the hub exceeds 4,800 CSN (about engine cycle 15,300) under the reading that the later point governs.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The operator's note claims an AMOC extends the limit to 5,300 CSN, but no FAA approval letter or reference is on file. Without an approved AMOC under paragraph (j), the Table 1 limit of 4,800 CSN is used.
- **Missing fact:** The 2nd-stage hub serial number SYN-HUB2-0027 does not match any listed serial number, so no match was made; the record appears sufficient but should be verified against the part's physical identification.
- **Missing fact:** No engine shop visit is recorded, so the trigger event has not occurred; future shop visits must be checked against the definition in paragraph (i)(2).
- **Note:** The 1st-stage hub has 50 cycles left to 4,800 CSN; the record's top-level cycles_since_new of 4,750 is consistent with 4,500 at 2025-10-29 plus 250 engine cycles.
- **Note:** The claimed 5,300 CSN AMOC is not evidence and was not applied.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine model is listed in the AD and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 matches Table 1 (limit 4,000 cycles since new). The hub is at 1,400 cycles, so the removal is tied to the next engine shop visit; the 'not applicable' record is an operator claim and conflicts with the match.
- **Stated timing:** At the next engine shop visit after 2025-10-29, which is not before 100 flight cycles after the effective date (the later of that and the 4,000-cycle limit applies). The hub is below its limit, so the limit-based date is the later one. No shop visit has occurred, so no deadline is fixed now.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The 1st-stage hub S/N SYN-HUB1-0028 is not in Table 1, so it is not matched. Confirm that the serial number is accurate.
- **Missing fact:** No shop visits are recorded. Any future event must be checked against the AD definition of engine shop visit (i)(2) to see if it triggers removal.
- **Note:** The record's 'not_applicable / no affected hubs installed' entry is an operator assertion and conflicts with the S/N match to PKLBST5005; it should be reviewed.
- **Note:** Hub cycles since new are 1,400 on 2026-02-10, 2,600 below the 4,000 limit. The record's 2025-10-29 reading of 1,000 plus 400 engine cycles is consistent with this.
- **Note:** The 2nd-stage hub was installed 2025-06-03, before the effective date, so the installation prohibition in (h) does not apply to that installation.
- **Note:** This is a screening aid, not a compliance determination.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2525-D5 is within the applicability of in-force AD 2025-19-13. The installed 1st-stage hub serial PKLBSK9287 matches table 1, but the installed part number is 2A5001-01 versus listed 2A5001, so the match needs review. If it matches, the 100-cycle removal limit is already exceeded (2400 cycles) and removal is due at the next engine shop visit, with no shop visit recorded.
- **Stated timing:** If the 1st-stage hub is an affected part: at the next engine shop visit after October 29, 2025, or within 100 flight cycles after the effective date, whichever occurs later. The cycle limit is already passed, so the shop visit governs; no shop visit is recorded yet. The effective-date engine cycle count is not given.
- **Missing fact:** Installed P/N is 2A5001-01, while table 1 lists 2A5001 for S/N PKLBSK9287. Need confirmation whether the -01 dash number is the same part for table 1 purposes; this decides whether the removal requirement is triggered.
- **Missing fact:** Engine flight cycles at the effective date are not recorded, so the 100-flight-cycle deadline cannot be computed as an engine counter.
- **Missing fact:** No shop visit events are recorded; any future shop visit (separation of major mating flanges, per (i)(2)) would trigger removal if the hub is affected.
- **Note:** The 2nd-stage hub S/N SYN-HUB2-0029 is not listed in table 1 and is not matched.
- **Note:** The NPRM 2025-10764 is superseded by the final rule.
- **Note:** No AMOC or AD record claims were supplied.

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
