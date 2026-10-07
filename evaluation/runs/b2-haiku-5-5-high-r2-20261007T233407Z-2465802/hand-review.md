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
- **Summary:** The V2527-A5 engine has an HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) listed in Table 1 to paragraph (g) with a 5,500-cycle removal limit. The hub shows 3,100 cycles since new, leaving 2,400 cycles, so the hub must be removed at the next engine shop visit before that limit is reached, and no shop visit is recorded.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 5,500 cycles since new. At the current accrual rate that limit is reached at engine flight cycle 45,050. The 100-flight-cycle alternative in paragraph (g) ran out at engine flight cycle 41,300, before the 2026-09-26 snapshot.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** No engine events are recorded. Shop visits since 2025-10-29 are needed to tell whether the removal trigger (next engine shop visit) has already occurred and whether the hub was removed at it.
- **Missing fact:** The cycles-since-new value of 3,100 has no reading date. It is treated as the value at the 2026-09-26 snapshot, and it is consistent with the dated reading of 1,650 on 2025-10-29 plus 1,450 engine cycles. The date should be confirmed because the remaining-cycle figure depends on it.
- **Note:** This is a screening aid and not a compliance determination. The answer relies on the final rule 2025-18469, which is in force. The NPRM 2025-10764 was not relied on.
- **Note:** The 2,400-cycle remaining figure and the engine cycle 45,050 assume the hub accrues one cycle per engine flight cycle from the 2026-09-26 snapshot.
- **Note:** The HPT 2nd-stage hub SYN-HUB2-0001 (P/N 2A4802) does not match any serial number in Table 1, so it is not a matched part. Its installation and cycle records are incomplete, but that does not change this screen.
- **Note:** The engine record contains no ad_records or amoc_claims, so no operator AD status or alternative method of compliance is asserted.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row, P/N 2A5001, S/N PKLBST5011, removal cycle limit 5,500

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 engine is within the applicability of AD 2025-18469, which took effect October 29, 2025. Neither installed hub matches a P/N and S/N pair in Table 1 to paragraph (g) (HPT 1st-stage hub P/N 2A5001 S/N PKLBST5012; HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0002), so the record triggers no removal action now, but the installation prohibition in paragraph (h) continues to bind.
- **Note:** The installed 1st-stage hub serial PKLBST5012 is one character away from listed serial PKLBST5011 (limit 5,500 cycles) but is not the same serial; the screen treats it as not listed. If the serial was transcribed incorrectly, the hub would need to be rechecked against the listed serial.
- **Note:** The events list is empty, so no engine shop visit history is recorded. This does not change the outcome because no listed hub is recorded as installed.
- **Note:** The record does not show whether listed hubs are held as spares elsewhere; the installation prohibition in paragraph (h) applies to any engine regardless of where the hub is held.
- **Note:** This screen is not a compliance determination. The NPRM 2025-10764 was superseded for this purpose by the final rule 2025-18469, which is the document relied on here.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2025-18469 is in force and covers the V2524-A5, and the installed HPT 1st-stage hub carries listed P/N 2A5001, so the removal requirement in paragraph (g) may apply. Its serial number and cycles since new are unknown, so the screen cannot tell whether that hub is one of the listed serials or how close it is to its removal limit. The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) does not match any listed serial.
- **Stated timing:** For a listed hub, removal is due at the next engine shop visit after 2025-10-29 before the hub exceeds its listed removal cycle limit, or within 100 flight cycles of 2025-10-29, whichever occurs later. The engine record has no shop visit events and no engine flight-cycle count, so the deadline cannot be computed.
- **Missing fact:** The serial number of the installed 2A5001 HPT 1st-stage hub is unknown. The AD lists four 2A5001 serials in table 1 to paragraph (g); without this serial the screen cannot tell whether the hub is an affected part.
- **Missing fact:** The cycles since new of the installed HPT 1st-stage hub are unknown. If the serial is listed, the hub's removal cycle limit (100 to 6,200 cycles depending on serial) can only be compared against this count.
- **Missing fact:** The engine's current flight-cycle count is not in the record. It is needed to tell whether the 100-flight-cycle window from 2025-10-29 has already passed and to compute any latest_engine_flight_cycles value.
- **Missing fact:** The events list is empty. Whether any engine shop visit (separation of major mating H-P flanges) occurred after 2025-10-29 is not recorded, and a shop visit would trigger the removal requirement for a listed hub.
- **Note:** This is a screening aid, not a compliance determination. Nothing here states that any engine or hub is compliant or noncompliant, or that it is airworthy or approved for return to service.
- **Note:** The installed HPT 2nd-stage hub has P/N 2A4802, which the AD lists, but serial SYN-HUB2-0003 is not in table 1. On this record it does not match a listed part. Its 5100 cycles since new are not compared against any limit because no listed serial matches.
- **Note:** The record has no ad_records or amoc_claims entries for this AD, so no operator AD status or AMOC claim was assessed.
- **Note:** The 100-flight-cycle window runs from the effective date, 2025-10-29, and the record does not contain engine flight cycles to measure it.
- **Note:** The NPRM 2025-10764 was superseded by the final rule 2025-18469 and was not relied on for any requirement.
- **Note:** If the 1st-stage hub serial is one of the four listed 2A5001 serials, the hub's cycles since new would determine whether its removal limit has already been exceeded, and the 100-flight-cycle window could already have passed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub P/N 2A5001 (serials PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489) and HPT 2nd-stage hub P/N 2A4802 (serials PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100)

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model in the record is PW1133G-JM, which is not one of the IAE V2500 models this screen supports, so no applicability determination is made against this AD. The AD (effective October 29, 2025) is in force on the question date, but this screen does not evaluate it for this engine.
- **Note:** The engine record lists engine_model PW1133G-JM, serial SYN-PW1100-0004, and is marked synthetic. This screen supports only the listed IAE V2500 models, so no applicability determination is made and the AD's compliance paragraphs were not applied.
- **Note:** The record has no installed_components and no events, so no part-level matching was performed.
- **Note:** This output is a screening aid only and is not a compliance determination or a statement about airworthiness or return to service.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2527E-A5 engine is within the directive's applicability, and its installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSS9840) is listed in Table 1 to paragraph (g). The operator's record shows an engine shop visit inducted on 2025-11-12, which the operator asserts qualifies under the directive, so removal and replacement of that hub is required at this shop visit and no later than engine flight cycle 18100 under the later-of reading.
- **Stated timing:** Remove and replace the listed HPT 2nd-stage hub at the engine shop visit (induction recorded 2025-11-12, at 18040 engine flight cycles). Under the later-of reading of paragraph (g), the latest compliance point is 100 flight cycles after the 2025-10-29 effective date, which is engine flight cycle 18100.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The record does not show whether the listed HPT 2nd-stage hub (S/N PKLBSS9840) was removed and replaced with a part eligible for installation during the 2025-11-12 shop visit. Removal status determines whether the paragraph (g) action is complete.
- **Missing fact:** The only dated cycles-since-new reading is 1000 on 2025-10-29; the undated value of 1040 is assumed to be current on 2025-11-12. A dated reading would confirm the value used for the remaining-cycles calculation against the 3900 limit.
- **Missing fact:** The qualifies_as_engine_shop_visit value of 'yes' for AD 2025-19-13 is the operator's assertion. The event detail (separation of major mating flanges) appears to match paragraph (i)(2), but the qualification itself has not been verified against the directive definition.
- **Note:** The HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0005) is not listed in Table 1, so it is not affected under paragraph (g) on this record. Its listed status is confirmed from the record, not inferred from absence of data.
- **Note:** No ad_records or amoc_claims for AD 2025-19-13 were supplied, so no operator AD status or alternative method of compliance was assessed.
- **Note:** The 2025-10-29 engine cycle reading of 18000 is used as the cycle count at the effective date, so 100 flight cycles after the effective date is 18100.
- **Note:** The 2025-10-25 NPRM (2025-10764) was not relied on for the deadline; the final rule 2025-18469 governs this screen.
- **Note:** This is a screening aid. It does not determine compliance or return-to-service status of the engine or any part.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSS9840, removal cycle limit 3,900

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2530-A5 engine is within the in-force AD 2025-18469 applicability. Its HPT 1st-stage hub (P/N 2A5001, S/N PKLBSK9287) is listed in Table 1 with a 100-cycle removal limit, and the hub shows 90 cycles since new, so removal and replacement is required at the next engine shop visit or within 100 flight cycles of the effective date (engine cycle 25600), whichever is later.
- **Stated timing:** Remove the listed HPT 1st-stage hub and replace it with a part eligible for installation at the next engine shop visit before it exceeds 100 cycles since new, or within 100 flight cycles from the effective date of 2025-10-29 (engine cycle 25600), whichever occurs later. At the current pace the hub reaches 100 cycles near engine cycle 25540.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** The record gives 90 cycles since new as an undated top-level value and 60 as of 2025-10-29. The 90 value is taken as the current count as of the 2025-11-20 snapshot, which fits the 30-cycle engine increase over that period. A dated confirmation is needed because the remaining-cycle figure and the deadline depend on it.
- **Missing fact:** No engine shop visit history or upcoming shop visit date is recorded (events is empty). The shop-visit prong of the required action cannot be scheduled from the record.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0006) is not listed in Table 1 and is not matched. Its record is not evidence that it is unaffected, but the supplied data does not show it as a listed part.
- **Note:** The HPT 1st-stage hub was installed on 2025-09-30, before the effective date. The installation prohibition in (h) concerns later installations and does not by itself bear on this hub's removal timing.
- **Note:** Engine cycles were 25500 on the effective date and 25530 on the question date. The 100-flight-cycle prong therefore runs to engine cycle 25600.
- **Note:** This is a screening aid. It does not state whether the engine or part is compliant or noncompliant, airworthy, or approved for return to service.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSK9287, removal cycle limit 100

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine is within the directive's applicability, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed with a 4,800-cycle removal limit. At 4,300 cycles since new it has about 500 cycles left, so removal is required at the next engine shop visit before that limit is reached, or within 100 flight cycles of 2025-10-29 if that later date governs; the listed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005, 2,300 cycles since new against a 4,000 limit) is also subject to the same requirement.
- **Stated timing:** Remove the listed hubs at the next engine shop visit after 2025-10-29 and before the 1st-stage hub exceeds 4,800 cycles since new (about 500 cycles after the 2025-12-01 snapshot, roughly engine flight cycle 30,800), or within 100 flight cycles of 2025-10-29 (engine flight cycle 30,100), whichever occurs later.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** No engine shop visit events are recorded, so the date of the next shop visit and whether it will occur before the 1st-stage hub reaches 4,800 cycles since new are unknown. This determines the removal deadline.
- **Missing fact:** The current cycles-since-new value of 4,300 is undated; it should be confirmed as of 2025-12-01 for the remaining-cycle calculation.
- **Missing fact:** The current cycles-since-new value of 2,300 is undated; it should be confirmed as of 2025-12-01 for the remaining-cycle calculation.
- **Missing fact:** The projected engine flight cycle at which the 1st-stage hub reaches 4,800 cycles (about 30,800) assumes the hub accumulates cycles at the same rate as the engine. The record shows equal increases over the same interval, but this is a projection and not a confirmed fact.
- **Note:** The 2025-10764 NPRM was superseded by this final rule for the question date, so only 2025-18469 was relied on.
- **Note:** The 100-flight-cycle reference uses the engine flight-cycle reading of 30,000 on 2025-10-29 as the effective-date baseline, giving a 30,100 threshold.
- **Note:** The latest engine flight cycle of 30,800 is a projection from the 500 cycles remaining, assuming the hub accumulates cycles at the engine rate.
- **Note:** Installed-part removal is required only as stated in paragraph (g); the installation prohibition in paragraph (h) applies to any engine regardless of this engine's status.
- **Note:** This screen is not a compliance determination; the required action depends on the shop-visit schedule and on confirming the current hub cycle counts.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200 (limit 4,800) and HPT 2nd-stage hub row 2A4802 / PKLBST5005 (limit 4,000)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive applies to this V2528-D5 engine, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) is a listed part with a 6,200-cycle removal limit. The record shows 2,500 cycles since new, so the hub must be removed at the next engine shop visit before the engine reaches 54,200 flight cycles, and no shop visit is recorded yet.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds its 6,200 cycles-since-new removal limit, which the record puts at engine flight cycle 54,200. The 100-flight-cycle alternative in paragraph (g), counted from 2025-10-29, would fall at 50,100 cycles, which the engine has already passed at 50,500 cycles; see alternative_readings.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The serial number of the installed HPT 2nd-stage hub (P/N 2A4802) is unknown. Its serial number must be checked against the four listed 2A4802 serial numbers in table 1 to paragraph (g) before it can be screened for this directive.
- **Missing fact:** The cycles since new for the installed HPT 2nd-stage hub are unknown. If its serial number is listed, its removal limit (3,900 to 6,000 cycles depending on serial number) and remaining cycles cannot be computed without this value.
- **Missing fact:** No engine shop visit is recorded in the events list. Whether the next shop visit occurs before the 54,200-cycle limit is unknown, and that visit is the trigger for removal under paragraph (g).
- **Missing fact:** No ad_records entry for this directive was supplied, so the operator's recorded AD status and any claimed alternative method of compliance could not be checked. These are claims to verify, not evidence that settles the outcome.
- **Note:** This is a screening aid, not a compliance determination.
- **Note:** The installed 1st-stage hub's cycles_since_new of 2,500 has no date. It is consistent with the dated reading of 2,000 at 2025-10-29 plus 500 engine cycles to the 2026-03-10 snapshot (50,000 to 50,500), so 2,500 is treated as the current value.
- **Note:** Remaining cycles and the 54,200 engine flight-cycle figure assume the hub accrues one cycle per engine flight cycle from the snapshot onward.
- **Note:** If the 2nd-stage hub serial number matches a listed serial number in table 1, its own removal limit and cycles would need to be screened separately.
- **Note:** The 2025-10764 NPRM was superseded by the final rule 2025-18469 and was not relied on.
- **Unresolved locator:** 2025-18469 (g) Table 1 row: HPT 1st-stage hub, 2A5001, PKLBST7489, limit 6,200

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** Directive 2025-18469 is in force and covers the V2522-A5 model of this engine, so it applies on scope. The record lists no installed HPT 1st-stage or 2nd-stage hub entries and no events, so it cannot be determined whether any table 1 hub is installed and whether removal under paragraph (g) is due.
- **Stated timing:** For any installed hub listed in table 1 to paragraph (g), removal is due at the next engine shop visit after 2025-10-29, before exceeding the listed removal cycle limit, or within 100 flight cycles of 2025-10-29, whichever occurs later. No shop visit or hub installation is recorded, so the due point cannot be fixed from this record.
- **Missing fact:** No installed component record for an HPT 1st-stage hub is present. Whether a table 1 hub (P/N 2A5001 with a listed S/N) is installed decides whether paragraph (g) removal applies. An empty list is not evidence that no hub is installed.
- **Missing fact:** No installed component record for an HPT 2nd-stage hub is present. Whether a table 1 hub (P/N 2A4802 with a listed S/N) is installed decides whether paragraph (g) removal applies. An empty list is not evidence that no hub is installed.
- **Missing fact:** No engine flight-cycle counter is recorded. It is needed to compute the 100-flight-cycle limit measured from the 2025-10-29 effective date and any hub removal deadline.
- **Missing fact:** No engine shop visit events are recorded. Whether a shop visit has occurred since 2025-10-29 determines when paragraph (g) removal is triggered.
- **Note:** The record is synthetic and shows an empty installed_components list and an empty events list. These are absence of recorded data, not confirmation that no affected hub is installed.
- **Note:** The directive is the final rule 2025-18469, effective 2025-10-29. The earlier NPRM 2025-10764 is a proposal and was not relied on for any obligation.
- **Note:** The installation prohibition in paragraph (h) applies to all engines in scope, so it binds the operator whether or not an affected hub is currently installed.
- **Note:** This is a screening aid and does not establish compliance or noncompliance. The paragraph (g) deadline cannot be computed without the hub records, the engine cycle counter, and shop visit history.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model V2500-A1 is not among the V2500 models this screen supports, so no applicability determination is made against this directive. No action status is assigned.
- **Note:** The engine record lists model V2500-A1, which is outside the supported model list for this screen.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) appears in Table 1 of the directive, but this does not change the outcome because the model is out of scope.
- **Note:** The directive is in force, effective October 29, 2025, as of the question date. This output is a screening aid only and is not a compliance determination.
- **Unresolved locator:** 2025-18469 (c) Applicability paragraph listing IAE AG V2522-A5 through V2533-A5 models

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (Federal Register 2026-16954, as corrected by 2026-18423) is in force as of 2026-09-24 and covers V2527-A5 engines with a 3rd stage HPC rotor blade P/N 6A8353 or 6A8688 installed. The recorded 3rd stage HPC rotor blade set is P/N 6A8353, so the engine is within applicability; the required full-set replacement is triggered only at the next engine shop visit after 2026-09-24 where the 3rd stage HPC rotor blade is exposed, and no such event is recorded.
- **Stated timing:** Not yet due. Required at the next engine shop visit inducted after 2026-09-24 where the 3rd stage HPC rotor blade is exposed (any blade removed from the HPC stage 3 to 8 drum); no calendar or cycle deadline applies until that event occurs.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** The events list is empty, so it is not confirmed whether any engine shop visit has been inducted since 2026-09-24 or whether the 3rd stage HPC rotor blade was exposed at any such visit. Either would trigger the replacement requirement in paragraph (g).
- **Missing fact:** Serial number is not tracked at set level. Applicability here rests on the part number, but individual blade serial and part-number records would be needed to confirm that every blade in the set is P/N 6A8353 and not already a part eligible for installation (P/N 6C8368, 6C8403, a later approved P/N, or 6A8353-001 / 6A8688-001).
- **Note:** Screening aid only; this is not a compliance determination. The engine record is synthetic (SYN-ENG-011, SYN-V2500-0011).
- **Note:** The correction document 2026-18423 (published 2026-09-10) fixes only the omitted word 'blade' in paragraph (g); the effective date remains September 24, 2026.
- **Note:** The NPRM 2025-20088 is superseded by the final rule and was not relied on for the requirement, which differs from it (the NPRM required replacement at the next blade exposure, while the final rule requires it only at an engine shop visit after the effective date).
- **Note:** No ad_records or amoc_claims were supplied, so the operator's recorded AD status and any AMOC claim are not assessed.
- **Note:** Replacement with reworked blades or new blades (P/N 6C8368, 6C8403, or later approved P/N) would be the path to a part eligible for installation under paragraph (h)(1); the record does not show any such part.
- **Unresolved locator:** 2026-18423 (g) Correction of paragraph (g) wording: 'where the 3rd stage HPC rotor blade is exposed'

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** AD 2026-17-03 (FR 2026-16954) is in force since 2026-09-24 and applies to V2533-A5 engines with 3rd stage HPC rotor blade P/N 6A8353 or 6A8688 installed. The recorded 3rd stage HPC rotor blade set is P/N 6C8368, which the AD lists as a part eligible for installation, so this screen places the engine outside the applicability and no action is triggered on this record.
- **Missing fact:** The record gives one set-level part number (6C8368) and no per-blade part numbers. The screen relies on the set-level entry; confirmation that no blade in the set is P/N 6A8353 or 6A8688 would be needed to firm up the does-not-apply reading.
- **Note:** Authority: the final rule states an effective date of September 24, 2026, so it is in force on the 2026-10-05 question date.
- **Note:** The engine record lists no events, so no engine shop visit or blade exposure is recorded. If the engine is inducted into a shop visit where a 3rd stage HPC rotor blade is exposed and any blade is found to be P/N 6A8353 or 6A8688, the engine would need to be re-screened and the replacement requirement in paragraph (g) would be evaluated then.
- **Note:** The blade set serial number is not tracked at set level, so individual blade identity cannot be checked from this record.
- **Note:** This is a screening aid only and does not determine compliance, airworthiness, or return-to-service status.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The directive applies to this V2530-A5 engine because the installed 3rd stage HPC rotor blade set is recorded as P/N 6A8688, and it has been in force since 2026-09-24. The only recorded engine shop visit was inducted on 2026-09-14, before the effective date, so paragraph (g) is not triggered by this record; replacement would be due at the next engine shop visit inducted on or after 2026-09-24 where the blade is exposed.
- **Stated timing:** At the next engine shop visit inducted after the effective date of 2026-09-24 where the 3rd stage HPC rotor blade is exposed, replace the full set of 3rd stage HPC rotor blades with parts eligible for installation. The 2026-09-14 visit does not count as that shop visit under the preamble's stated intent.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** Blade serial numbers are not tracked at set level, so the record cannot confirm that every blade in the set is P/N 6A8688 rather than a mixed set; this matters for confirming the applicability match.
- **Missing fact:** The operator's assertion that the 2026-09-14 induction qualifies as an engine shop visit is a claim; the induction date is what determines whether paragraph (g) is triggered, so the induction date should be confirmed from source documents.
- **Missing fact:** The disposition of the 3rd stage blade removed on 2026-09-30 during the pre-effective-date visit (blade exposure after the effective date within a visit inducted before it) is not addressed by the record; a reviewer should confirm how the exposure is classified under paragraph (g) and (h)(2).
- **Note:** The operator's qualifies_as_engine_shop_visit 'yes' for AD 2026-17-03 is an operator assertion that the 2026-09-14 induction is an engine shop visit under (h)(3); the timing question turns on the induction date relative to the 2026-09-24 effective date, not on that flag.
- **Note:** The blade exposure on 2026-09-30 occurred after the effective date but within a visit inducted before it. A reading that treats this in-progress visit as the triggering shop visit would require replacing the full blade set at that visit, with no cycle-based deadline; this reading is contrary to the preamble's stated intent, so it is flagged for reviewer confirmation rather than listed as an alternative deadline.
- **Note:** No engine flight-cycle or blade cycle data was supplied, so no cycle-based deadline or remaining-cycles figure can be computed.
- **Note:** This screen is not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2026-17-03 applies to this V2524-A5 because a 3rd stage HPC rotor blade set with P/N 6A8353 is recorded as installed. The 2026-10-01 shop visit came after the 2026-09-24 effective date, but the record says no 3rd-stage blade was removed from the stage 3-8 drum, so the paragraph (h)(2) exposure that triggers full-set replacement is not shown; replacement is due at the next qualifying exposure.
- **Stated timing:** No fixed deadline. Full-set replacement is required at the next engine shop visit after 2026-09-24 at which a 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum. The 2026-10-01 visit, per the record, did not include such a removal.
- **Expected timing:** Replacement is not required at this visit under the corrected text. Whether it is required at a later visit depends on how "next engine shop visit ... where" is read.
- **Missing fact:** Confirmation that no 3rd stage HPC rotor blade was removed from the HPC stage 3 to 8 drum during the 2026-10-01 shop visit. The record states none was, but the 2026-10-02 entry is brief and operator-asserted. Paragraph (h)(2) defines exposure by removal from the drum, so this fact decides whether replacement was triggered.
- **Missing fact:** The blade set serial number is not tracked at set level. This does not change applicability, which turns on P/N, but it limits the ability to show which blades are installed when a future exposure occurs.
- **Note:** This is a screening aid, not a compliance determination. The record's qualifies_as_engine_shop_visit assertion and the 2026-10-02 exposure statement come from the operator record and were not verified.
- **Note:** The 2026-10-02 event says 'HPC rotor exposed for inspection' with no blade removed from the drum. Under (h)(2), exposure is defined by blade removal, so that wording is not treated as a trigger. If any blade was removed from the drum at any point during the visit, reassess; under that reading the replacement obligation would already have been triggered at the 2026-10-01 visit.
- **Note:** The record contains no engine flight-cycle counter and no component cycle data, and the directive is not cycle-based, so no cycle figures are computed.
- **Note:** Return to service on 2026-10-04 is recorded. The directive does not tie a deadline to return to service; the obligation attaches to the next qualifying exposure.
- **Note:** NPRM 2025-20088 was superseded by the final rule and is not relied on for the obligation. Its compliance language differs (it required the replacement at the next exposure, not at the next shop visit).
- **Unresolved locator:** 2026-16954 (c) Applicability paragraph listing V2524-A5 and P/N 6A8353 or 6A8688

Forbidden claims for this case:

- AD 2026-17-03 requires replacement at this visit because the HPC rotor was exposed.
- The AD no longer applies because this shop visit passed without blade exposure, presented as settled.
- Replacement is required at a later visit, presented as settled.
- The paragraph (g) text as published on 2026-08-20 controls.

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model is supported and its installed 3rd stage HPC rotor blade set is recorded as P/N 6A8353, which matches the proposed applicability. The document is an NPRM with no effective date, so it cannot require action on the question date, and the full-set replacement would be triggered only by a future 3rd stage HPC rotor blade exposure if the AD is adopted as proposed.
- **Stated timing:** No compliance time is in effect. If adopted as proposed, the full set of 3rd stage HPC rotor blades must be replaced at the next 3rd stage HPC rotor blade exposure after the AD's effective date, which has not been published.
- **Missing fact:** No final rule or effective date for Docket FAA-2025-2555 appears in the supplied material. The NPRM's comment period closed January 2, 2026, before the question date, so the status must be checked for a final rule before any required action can be determined.
- **Missing fact:** The record gives one set-level part number, 6A8353. The applicability paragraph refers to each installed 3rd stage HPC rotor blade, so the individual blade part numbers should be confirmed (6A8353 or 6A8688) if the AD is adopted.
- **Missing fact:** The events list is empty, so no 3rd stage HPC rotor blade exposure is recorded. Exposure history would be needed to determine whether the replacement would be triggered under the proposed wording.
- **Note:** This is a screening aid, not a compliance determination. The engine and part are not classified as compliant or noncompliant.
- **Note:** The directive is a proposed rule as of the question date, so it does not yet bind the operator. Re-screen if a final rule is published with an effective date.
- **Note:** The record states that the blade set serial number is not tracked at set level, so the installed serial number could not be matched to any listed serial number. The listed serial number is null because the directive lists part number only.

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 (Federal Register document 2025-17066) is in force, effective 2025-10-10, and covers the V2527-A5, which is a supported model. The operator reports it is an air carrier and that neither its approved maintenance program nor paragraph B.1 of the V2500-A5 TLM ALS yet incorporates table 1 to paragraph (g), so the required revisions are due by 2026-01-08.
- **Stated timing:** Within 90 days after the 2025-10-10 effective date, on or before 2026-01-08: revise paragraph B.1 of the Maintenance Scheduling section of the TLM ALS per paragraph (g)(1), and for air carrier operations revise the existing approved maintenance or inspection program per paragraph (g)(2), incorporating table 1 (HPT Stage 1 Hub P/N 2A5001, TASK 72-45-11-200-006; HPT Stage 2 Hub P/N 2A4802, TASK 72-45-31-200-009).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** No component record for the HPT Stage 1 hub (P/N 2A5001) is present. It is not needed for the 90-day ALS and program revision, but it is needed to know when the piece-part inspection under TASK 72-45-11-200-006 comes due.
- **Missing fact:** No component record for the HPT Stage 2 hub (P/N 2A4802) is present. It is not needed for the 90-day revision, but it is needed to know when the piece-part inspection under TASK 72-45-31-200-009 comes due.
- **Note:** Screening aid only; this is not a compliance determination. The operator's statement that the program and TLM ALS do not yet incorporate table 1 is an assertion from the record, not a finding.
- **Note:** Deadline is calendar-based: 90 days after 2025-10-10 is 2026-01-08. The snapshot date 2025-11-15 leaves 54 days.
- **Note:** The record has no engine flight-cycle counter, so no cycle-based deadline or remaining-cycle figure can be computed.
- **Note:** The record is synthetic and lists no installed components, so no HPT hub part or serial numbers are matched.
- **Note:** The 2024 NPRM (2024-26092) was not relied on for obligations; the final rule 2025-17066 governs. The final rule clarifies the TASK 72-45-31-200-009 reference and the TLM and program revision requirements.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** Engine model V2522-A5 is within the applicability of AD 2025-17-16 (Federal Register 2025-17066), which took effect October 10, 2025. The one-time revision of the airworthiness limitations Maintenance Scheduling paragraph B.1 is due by January 8, 2026, and the record contains no evidence on whether it has been done; the air carrier program revision in paragraph (g)(2) also depends on operator status that is unknown.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, that is by January 8, 2026, for the paragraph (g)(1) Time Limits Manual revision. The paragraph (g)(2) program revision has the same 90-day window and applies only to air carrier operations.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Whether the operator conducts air carrier operations is unknown. This decides whether the paragraph (g)(2) revision of the existing approved maintenance or inspection program applies.
- **Missing fact:** No operator record exists for whether the paragraph (g)(1) Time Limits Manual revision, or the (g)(2) program revision where applicable, has been done. Absence of a record is not evidence either way.
- **Missing fact:** No installed component record exists for the HPT Stage 1 Hub (listed P/N 2A5001). Its part number and serial number are needed to determine whether the piece-part exposure inspection in Table 1 applies to it.
- **Missing fact:** No installed component record exists for the HPT Stage 2 Hub (listed P/N 2A4802). Its part number and serial number are needed to determine whether the piece-part exposure inspection in Table 1 applies to it.
- **Note:** This is a screening aid and not a compliance determination. The engine record has no installed components, events, AD records, or operator facts, and missing records are not evidence that the revision has or has not been made.
- **Note:** The deadline is calendar-based, so no flight-cycle count applies. The 90-day window runs from the October 10, 2025 effective date stated in the final rule, not from the September 5, 2025 publication date.
- **Note:** The required Time Limits Manual revision is keyed to engine variant. For an A5 engine, the listed TLM is P/N 2A4408, TASK 05-10-00-990-000-B00. The reviewer should confirm the applicable TLM for this engine.
- **Note:** The FAA states that the piece-part inspection tasks are required by other regulations once the AD's required revision is made, so the AD itself mainly requires the revision.
- **Note:** The 2024 NPRM (2024-26092) is superseded by the final rule and was not used to set any deadline.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 is a listed model, and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is in Table 1 to paragraph (g). The directive is published with an effective date of 2025-10-29, so no required action is triggered on 2025-10-15, and the removal obligation applies at the next shop visit after that date or within 100 flight cycles of it, whichever is later.
- **Stated timing:** Not yet in force on 2025-10-15. From the effective date of 2025-10-29, remove the listed hub at the next engine shop visit before its 6000-cycle removal limit, or within 100 flight cycles of the effective date, whichever occurs later.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine flight-cycle counter is not recorded. It is needed to compute the deadline of 100 flight cycles after the 2025-10-29 effective date, and to know whether the hub's removal limit is reached first.
- **Missing fact:** No engine events are recorded, so it is not known whether a shop visit has occurred or will occur after 2025-10-29. Removal at the next shop visit depends on this. An empty event list is not evidence that no shop visit has occurred.
- **Note:** The directive is published with a 2025-10-29 effective date, so it is not in force on the question date and cannot require action yet. Its removal and installation obligations begin on that date.
- **Note:** The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed with a 6000-cycle removal limit. Its 990 cycles since new leave 5010 cycles to that limit.
- **Note:** The installed HPT 1st-stage hub P/N 2A5001 has S/N SYN-HUB1-0018, which is not in Table 1, so it is not matched as an affected part on this record.
- **Note:** The engine record has no ad_records or amoc_claims entries for this directive, and no engine flight-cycle counter.
- **Note:** This is a screening aid only and is not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub, 2A4802, PKLBSR2100, limit 6000

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine is within the directive's applicability. Its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in Table 1 with a 4,800-cycle removal limit, and the record shows 4,990 cycles since new, so the removal must be done by engine flight cycle 60100 (100 cycles after the 2025-10-29 effective date), because the shop-visit prong can no longer be met. This is a screening result, not a compliance determination.
- **Stated timing:** Remove the listed HPT 1st-stage hub and replace it with a part eligible for installation no later than 100 flight cycles after the 2025-10-29 effective date (engine flight cycle 60100). The at-next-shop-visit prong cannot be met because the hub already exceeds its 4,800-cycle limit.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** No AD status record for this AD was supplied, so it cannot be confirmed whether the listed hub has already been removed or replaced. This matters for whether the action is still outstanding.
- **Missing fact:** The events list is empty, so no engine shop visit or hub removal since the 2025-10-29 effective date is recorded. Any such event would need to be checked against the paragraph (g) removal obligation.
- **Missing fact:** The 4,990 cycles-since-new value is undated. The only dated reading is 4,950 at 2025-10-29. The current value is needed to confirm the component's position against its 4,800-cycle limit.
- **Note:** The record is synthetic. The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0019) is not in Table 1, whose listed S/Ns are PKLBST5005, PKLBSS9840, PKLBSS0301 and PKLBSR2100, so the record does not match it. Its 4,990 cycles do not trigger a removal limit under this AD.
- **Note:** The effective-date engine cycle count is taken as 60000 (reading dated 2025-10-29). The snapshot count is 60040, leaving 60 cycles before the 60100 deadline.
- **Note:** The 2025-10764 NPRM was not relied on, since the final rule 2025-18469 governs and is in force on the question date.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row with P/N 2A5001 and S/N PKLBSS9200, removal cycle limit 4,800

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 (FR 2021-11960) was in force on 2022-03-01 and covers V2533-A5 engines. The installed HPT 1st-stage disk (P/N 2A5001) and HPT 2nd-stage disk (P/N 2A4802) match the directive's part numbers, but their serial numbers cannot be checked against the Appendix A tables, and the record has no cycle counter or event history, so applicability and deadline cannot be settled. The superseding AD 2022-02-09 (FR 2022-02574) was published but is not effective until 2022-03-15, so it does not change the in-force status on the question date.
- **Stated timing:** If the disk serial numbers are listed in the Appendix A tables: the USI is due at the next engine shop visit after 2021-07-13 or before the HPT 1st-stage disk accumulates 3,200 flight cycles since 2021-07-13, whichever occurs first. The HPT 2nd-stage disk has the same timing under paragraph (g)(2).
- **Missing fact:** Whether HPT 1st-stage disk serial SYN-DISK1-0020 (P/N 2A5001) is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1. The NMSB is not in the supplied text, and the listing decides whether paragraph (g)(1) applies.
- **Missing fact:** Whether HPT 2nd-stage disk serial SYN-DISK2-0020 (P/N 2A4802) is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713 Rev 1. The listing decides whether paragraph (g)(2) applies.
- **Missing fact:** The engine flight-cycle counter is not in the record. It is needed to compute the 3,200-cycle deadline and the latest engine flight-cycle count for the action.
- **Missing fact:** Flight cycles the HPT 1st-stage disk has accumulated since the directive's effective date of 2021-07-13 are not recorded. They are needed to measure the 3,200-cycle limit.
- **Missing fact:** Flight cycles the HPT 2nd-stage disk has accumulated since 2021-07-13 are not recorded. They are needed to measure the 3,200-cycle limit.
- **Missing fact:** The event list is empty. The record does not show whether any engine shop visit has occurred since 2021-07-13, which would trigger the earlier (g)(1)/(g)(2) deadline. An empty list is not evidence that no shop visit occurred.
- **Missing fact:** The operator's recorded status for AD 2021-11-15 is not provided. It is needed to check the operator's claimed status against the directive.
- **Note:** On the question date, 2021-11960 is in force and 2022-02574 is published but not yet effective. The superseding AD changes the compliance times for disks that previously operated on high-thrust engines. That AD's Figure 1 is not in the supplied text, so its times cannot be computed here.
- **Note:** The record has no ad_records or amoc_claims entries, and no AMOC claim is in the record.
- **Note:** Engine flight cycles, disk cycles since 2021-07-13, and the Appendix A tables are needed before any deadline or applicability conclusion can be drawn.
- **Note:** This is a screening aid. It does not state that any engine or part is compliant or noncompliant, airworthy, or approved for return to service.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2022-02574 preamble Summary and DATES; The Amendment item 2.a and paragraph (b) of 2022-02-09

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (FR 2022-02574, superseding AD 2021-11-15) takes effect March 15, 2022, so it is not in force on the 2022-03-01 question date and cannot require action yet. The V2533-A5 model is in scope and both installed disk part numbers match, but applicability turns on serial-number lists in Appendix A that were not supplied, so the screen needs review.
- **Stated timing:** Not in force on 2022-03-01. Once effective on 2022-03-15, paragraphs (g)(1) and (g)(2) would require a USI of the HPT 1st-stage and HPT 2nd-stage disks at the next engine shop visit after that date, or within the Figure 1 compliance time or 10 flight cycles after the effective date, whichever occurs later, if the serial numbers are listed in Appendix A. Figure 1 was not supplied, so the deadline cannot be computed.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (serial numbers of listed HPT 1st-stage disks, P/N 2A5001) was not supplied. Needed to confirm whether installed S/N SYN-DISK1-0020 is within the directive's applicability.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (serial numbers of listed HPT 2nd-stage disks, P/N 2A4802) was not supplied. Needed to confirm whether installed S/N SYN-DISK2-0020 is within the directive's applicability.
- **Missing fact:** Figure 1 to paragraph (g)(1), which gives the compliance time for the USI, is an image not included in the supplied text. Needed to compute any deadline.
- **Missing fact:** No engine flight-cycle counter is in the record. Needed to measure cycles accumulated after the March 15, 2022 effective date and to compute any cycle-based deadline.
- **Missing fact:** The events list is empty. This does not show that no engine shop visit has occurred; a shop visit on or after March 15, 2022 is the trigger for paragraphs (g)(1) and (g)(2).
- **Missing fact:** The operator's recorded status for AD 2022-02-09 is not in the record. It is not evidence of compliance either way and was not relied on.
- **Note:** Screening aid only, not a compliance determination. The question date (2022-03-01) precedes the March 15, 2022 effective date, so no action is required on that date.
- **Note:** The engine model V2533-A5 is in the supported scope. The preamble classifies it as a high-thrust model, so paragraphs (g)(1) and (g)(2) apply rather than (g)(3) and (g)(4).
- **Note:** Installed HPT 1st-stage disk (P/N 2A5001, S/N SYN-DISK1-0020) and HPT 2nd-stage disk (P/N 2A4802, S/N SYN-DISK2-0020) match the directive's part numbers. Their serial numbers could not be checked against the Appendix A lists, so no matched_parts entries are recorded.
- **Note:** The superseded AD 2021-11-15 (FR 2021-11960) used a 3,200 FC limit from its effective date. That text was replaced by 2022-02574 and was not used to compute any deadline.
- **Note:** The engine record is synthetic. It has no ad_records, amoc_claims, flight-cycle counter, or shop-visit events, so none of these was treated as evidence that a part is absent or unaffected.

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The engine is a supported V2530-A5 and both installed disks carry the part numbers named in paragraph (c) (2A5001 and 2A4802), but applicability turns on whether serial numbers SYN-DISK1-0021 and SYN-DISK2-0021 appear in Appendix A, Tables 1 and 2, which were not supplied. The Figure 1 compliance time, which governs the required USI, is also not reproduced in the text provided, so the screen needs review.
- **Stated timing:** If the disk serial numbers are listed, the USI is due at the next engine shop visit or within 10 flight cycles after March 15, 2022, whichever occurs later, under the compliance time in Figure 1 to paragraph (g)(1), which was not supplied. No shop visit is recorded in the events list.
- **Missing fact:** Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713, Revision 1, is not supplied, so it cannot be confirmed whether HPT 1st-stage disk S/N SYN-DISK1-0021 (P/N 2A5001) is listed, which decides applicability under paragraph (c)(1) and the paragraph (g)(1) requirement.
- **Missing fact:** Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713, Revision 1, is not supplied, so it cannot be confirmed whether HPT 2nd-stage disk S/N SYN-DISK2-0021 (P/N 2A4802) is listed, which decides applicability under paragraph (c)(2) and the paragraph (g)(2) requirement.
- **Missing fact:** Figure 1 to paragraph (g)(1) (the compliance time table) is an image not included in the supplied text, so the flight-cycle or shop-visit limit for the USI cannot be determined.
- **Missing fact:** The engine flight-cycle counter is not in the record, so no flight-cycle deadline or remaining-cycle figure can be computed.
- **Missing fact:** The events list is empty. Whether any engine shop visit (separation of H-P major mating flanges) has occurred since the effective date, which would start the shop-visit trigger, is not confirmed.
- **Note:** This is a screening aid, not a compliance determination. Part numbers match the directive, but serial-number listing in Appendix A is unverified, so the disk-level applicability is open.
- **Note:** The superseding AD states the V2530-A5 is a high-thrust model, so paragraphs (g)(3) and (g)(4) for low-thrust models do not apply to this engine as a matter of model. Paragraph (g)(3)(ii) and (g)(4)(ii) are noted only as context and are not used to set the deadline.
- **Note:** The engine record contains no AD status or AMOC claims, and no engine flight-cycle count, so no deadline can be computed. Engine shop visit history since 2022-03-15 is not evidenced in the record (events is empty).
- **Note:** The Figure 1 compliance time is an image not included in the supplied text; the superseding AD does not restate the 3,200 flight-cycle figure from the original AD 2021-11-15, and this screen does not assume it.
- **Note:** Paragraph (i) credit for previous actions covers only paragraphs (g)(5) and (g)(6) (V2531-E5 NMSB V2500-E5-72-0015), so it does not apply to a V2530-A5 engine on this record.
- **Note:** The disk serial numbers (SYN-DISK1-0021, SYN-DISK2-0021) are synthetic; no listed_serial_number is recorded because the Appendix A tables were not supplied.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine has an installed HPT 1st-stage disk (P/N 2A5001, S/N PKLBSH1829) that is on the directive's paragraph (c)(1) serial list, so the ultrasonic inspection in paragraph (g)(1) is required within 10 flight cycles after the July 19, 2021 effective date, which is engine cycle 33010. The supplied record contains no inspection completion, and the engine read 33004 cycles on 2021-07-20.
- **Stated timing:** Within 10 flight cycles after the AD effective date of July 19, 2021: perform the USI of the HPT 1st-stage disk per IAE NMSB V2500-ENG-72-0713 paragraph 6. Engine cycle reading 33000 on 2019-07-19 (record date 2021-07-19) gives a due count of 33010; the 2021-07-20 reading of 33004 leaves 6 cycles.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** No AD status record or inspection completion record for AD 2021-11-51 is in the supplied engine record, so it cannot be confirmed whether the HPT 1st-stage disk USI was already performed within the compliance window.
- **Missing fact:** The text of Table 1 to paragraph (g)(1) and Table 2 to paragraph (g)(2) is an image not included in the supplied text; applicability was read from the serial numbers listed in paragraph (c) of the AD.
- **Note:** The engine record has no ad_records or amoc_claims entries for this AD, so no operator-asserted status was checked.
- **Note:** The events list is empty. No engine shop visit is recorded, and the AD's required action is not tied to a shop visit event.
- **Note:** The HPT 2nd-stage disk serial SYN-DISK2-0022 is not on the listed serials in paragraph (c)(2), so the 2nd-stage requirement does not match this engine's recorded part, subject to the record being accurate.
- **Note:** The 33000-cycle reading is dated 2021-07-19, the effective date. If the exact cycle count at the effective time differs, the due count could shift; the record gives no time of day.
- **Note:** This is a screening aid only and does not state whether the engine or any part is compliant or approved for return to service.
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
- **Summary:** AD 2021-11-15 is in force on the question date and V2533-A5 is a supported model, but applicability cannot be decided because the installed HPT 1st-stage disk (2A5001, S/N PKLBSH1829) and HPT 2nd-stage disk (2A4802, S/N SYN-DISK2-0022) must be checked against Appendix A serial lists that were not supplied. If both disks are listed, the USI is due at the next engine shop visit or before 3,200 FCs since July 13, 2021, whichever occurs first, but the engine's cycle count on July 13, 2021 is not in the record, so no flight-cycle deadline can be computed.
- **Stated timing:** For the V2533-A5, if the HPT 1st-stage disk (P/N 2A5001) and HPT 2nd-stage disk (P/N 2A4802) are listed in the Appendix A tables of IAE NMSB V2500-ENG-72-0713 Rev 1, each USI is due at the next engine shop visit after July 13, 2021 or before the disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first. No engine shop visit is recorded.
- **Missing fact:** Serial PKLBSH1829 must be checked against Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1, which the supplied Federal Register text does not reproduce. Applicability of paragraph (g)(1) depends on this.
- **Missing fact:** Serial SYN-DISK2-0022 must be checked against Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, which is not supplied. Applicability of paragraph (g)(2) depends on this.
- **Missing fact:** Engine flight cycles on the July 13, 2021 effective date are not in the record. The 3,200-FC limit runs from that date, so the latest cycle count for the action cannot be computed. Only 2021-07-19 (33000) and 2021-07-20 (33004) readings are present.
- **Missing fact:** The events list is empty. The record does not show whether any engine shop visit has occurred since July 13, 2021, which would trigger the USI before the cycle limit.
- **Missing fact:** Appendix A, Tables 1 and 2 of the NMSB are not included in the supplied document text. The serial lists are needed to decide whether each installed disk is within the directive's applicability.
- **Note:** Screening aid only, not a compliance determination. No ad_records or amoc_claims were supplied, so no operator AD status or AMOC is assessed.
- **Note:** The part numbers 2A5001 and 2A4802 match the directive's listed part numbers, but the directive ties applicability to serial numbers in Appendix A, which is not in the supplied text. No serial match is claimed.
- **Note:** The V2533-A5 is listed in paragraphs (g)(1) and (g)(2), not (g)(3) through (g)(6), which apply to other models or to V2531-E5.
- **Note:** The 3,200-FC limit runs from the July 13, 2021 effective date, so the engine's cycle count on that date is needed. The 33000 reading on 2021-07-19 is not a substitute.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive applies to this V2527M-A5 engine, and the installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 is listed in table 1 with a 6,000-cycle removal limit. The hub is recorded at 3,500 cycles since new, so it must be removed at the next engine shop visit before it exceeds that limit, and no shop visit is recorded yet.
- **Stated timing:** At the next engine shop visit after 2025-10-29 and before the hub exceeds 6,000 cycles since new (about engine flight cycle 25,000). No engine shop visit is recorded in the engine record.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).
- **Missing fact:** The current cycles-since-new value of 3,500 for hub PKLBSR2100 is undated. The dated reading of 1,000 on 2025-10-29 plus the 2,500 engine cycles recorded since then is consistent with 3,500, but the current value should be confirmed because it sets the 2,500 cycles remaining.
- **Missing fact:** Whether an engine shop visit (separation of major mating H-P flanges) has occurred since 2025-10-29 or is scheduled is not recorded. The timing of removal depends on the next shop visit, and the record shows none.
- **Note:** Screening aid only, not a compliance determination. The operator record shows a maintenance program revision on 2025-12-01 that refers to table 1 of AD 2025-17-16. That is a different AD number and is not analyzed here; it does not establish removal of hub PKLBSR2100 under this AD.
- **Note:** The HPT 1st-stage hub with P/N 2A5001 and S/N SYN-HUB1-0023 is not among the table 1 serial numbers and is not matched on this record. Its absence from the table is not evidence beyond the listed serials.
- **Note:** The 3rd stage HPC rotor blade set is outside this directive's table 1 and was not matched.
- **Note:** Engine flight cycles used: 20000 on 2025-10-29 (effective date) and 22500 on 2026-10-06 (snapshot). The hub's dated and current cycles-since-new readings differ by 2,500, matching the engine cycle increase, which supports treating hub and engine cycles as accruing together.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), row HPT 2nd-stage hub 2A4802 PKLBSR2100, removal cycle limit 6,000

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (FR 2026-16954, corrected by FR 2026-18423) applies because the installed 3rd stage HPC rotor blade set is P/N 6A8688, which the AD lists, and the directive is in force since its September 24, 2026 effective date. Replacement of the full blade set is required only at the next engine shop visit after that date where the 3rd stage HPC rotor blade is exposed; the record shows no such shop visit, so no deadline is computed.
- **Stated timing:** At the next engine shop visit after September 24, 2026 where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum), replace the full set of 3rd stage HPC rotor blades with parts eligible for installation. No calendar or cycle deadline applies otherwise.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record lists no engine shop visit after the 2026-09-24 effective date, and no event states whether the 3rd stage HPC rotor blade was exposed at any shop visit. Whether a qualifying shop visit with blade exposure occurs is what triggers the replacement action.
- **Missing fact:** The blade set serial number is recorded as not tracked at set level. This does not change applicability, which is based on part number, but the record does not show the individual blade identities needed to document blade removal and replacement.
- **Missing fact:** The record holds no ad_records entry for AD 2026-17-03, so the operator's recorded status for this directive is not supplied. Any operator status would be a claim to check, not evidence of compliance.
- **Note:** The record's maintenance_program_revision event (2025-12-01, Revision 48) cites AD 2025-17-16 table 1. That is a different AD, and 2026-16954 lists no affected ADs, so the revision neither satisfies nor triggers paragraph (g) of this directive.
- **Note:** The engine has 22500 cycles at the snapshot. No cycle-based deadline applies because the trigger is a shop visit with blade exposure, not a cycle count.
- **Note:** The HPT 1st-stage and 2nd-stage hub components are not listed by this directive and do not affect this screen.
- **Note:** This is a screening aid, not a compliance determination. The record does not establish compliance or noncompliance with AD 2026-17-03.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527M-A5 is a listed model under AD 2025-17-16, which took effect 2025-10-10, so the directive applies. The one-time airworthiness limitations and air carrier program revision was due by 2026-01-08, and the record shows a revision dated 2025-12-01, so no action is triggered on the record; the hub piece-part inspections remain continuing obligations that arise at piece-part exposure.
- **Stated timing:** The one-time revision of TLM paragraph B.1 and the air carrier maintenance program was due within 90 days after 2025-10-10, i.e. by 2026-01-08; the record shows a revision dated 2025-12-01. The HPT 1st-stage hub (TASK 72-45-11-200-006) and HPT 2nd-stage hub (TASK 72-45-31-200-009) inspections are performed at piece-part exposure under the revised TLM.
- **Missing fact:** The HPT 2nd-stage hub record shows cycles_since_new 3500 with no date and a dated reading of 1000 at 2025-10-29; the two values conflict and the current hub history is unclear. The AD itself sets no cycle limit, but the hub history matters for any piece-part exposure review.
- **Missing fact:** The install date and any dated cycle readings for the HPT 1st-stage hub (P/N 2A5001) are missing, so its service history cannot be confirmed.
- **Missing fact:** The revision to the approved program and V2500-A5 TLM is recorded only as an operator assertion. The record does not confirm that the applicable TLM (P/N 2A4408, TASK 05-10-00-990-000-B00) paragraph B.1 was revised to list both inspection tasks, or that the revision was accepted into the approved program.
- **Missing fact:** No piece-part exposure or engine shop visit history is recorded for this engine. Whether the hubs have been or will be exposed, which would trigger the on-event inspections, cannot be determined from the record.
- **Note:** This is a screening aid. The operator record's maintenance_program_revision entry is an operator assertion and was not independently verified against the TLM or the approved program.
- **Note:** The 90-day deadline runs from the 2025-10-10 effective date, giving 2026-01-08. The 2025-12-01 revision date falls within that window. Counting from the 2025-09-05 publication date would give 2025-12-04, and the 2025-12-01 date would still fall within it.
- **Note:** The AD sets no cycle limit for the hubs. The 20,000-cycle replacement threshold mentioned in the docket comments comes from the AMP, not the AD text, so no component cycle figure is computed here. The engine's 22500 cycles are therefore not used to derive an AD deadline.
- **Note:** The 3rd stage HPC rotor blade set (P/N 6A8688) is not listed in table 1 and was not matched.
- **Note:** No ad_records or amoc_claims entries were supplied for this AD. No AMOC is claimed.
- **Note:** The hub cycle readings conflict (3500 undated vs 1000 at 2025-10-29) and should be reconciled. This does not change the AD's required actions but affects the hub history.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 is a listed model and AD 2025-18469 has been in force since 2025-10-29, so the directive applies. Neither installed hub's part number and serial number pair appears in Table 1 to paragraph (g): the 1st-stage hub serial SYN-HUB1-0024 is not listed, and the 2nd-stage hub serial PKLBST5011 is listed only with P/N 2A5001, not 2A4802. No required removal is triggered on this record, but the installation prohibition in paragraph (h) continues to bind.
- **Note:** The 2nd-stage hub's serial number PKLBST5011 appears in Table 1, but only under 2A5001 (1st-stage hub, 5,500-cycle limit). Because the table pairs P/N and S/N, this does not match the installed 2A4802 hub. If the record's P/N were wrong, the hub would need checking; the screen does not resolve that.
- **Note:** The installed 1st-stage hub's serial SYN-HUB1-0024 is not in Table 1, so it is not an affected part on this record.
- **Note:** The record has no engine events, so no shop visit is on file. The required action is tied to the next shop visit only for a listed hub.
- **Note:** This is a screening aid based only on the supplied record. It does not determine compliance, airworthiness, or return-to-service status.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine record lists model CFM56-5B4/3, which is not among the IAE V2500 models this screen supports, so no applicability determination is made against Federal Register document 2025-17066. The directive was effective October 10, 2025, so it is in force on the question date.
- **Note:** The engine record shows model CFM56-5B4/3, which is a CFM International engine model and not an IAE V2500 model. The screen supports only the listed IAE V2500 models, so no applicability determination is made and no action status is assigned.
- **Note:** The record also shows no installed components and no events. These facts do not bear on the outside-scope result.
- **Note:** This screen is an aid only and does not state or imply compliance, airworthiness, or return-to-service status for the engine.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The engine is a supported V2530-A5 with installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489, which is listed in Table 1 to paragraph (g) with a 6,200-cycle removal limit. The hub is at 3,600 cycles since new, so removal is required at the next engine shop visit before it exceeds 6,200 cycles, about 23,200 engine flight cycles on the record's cycle rate.
- **Stated timing:** Remove the hub at the next engine shop visit after 2025-10-29 and before it exceeds 6,200 cycles since new (about 2,600 more cycles from 3,600). The alternative 100-flight-cycle window from 2025-10-29 ended at 20,100 engine cycles, which the engine passed by its 2026-03-01 reading of 20,600; read as the operative deadline, that window would already be exceeded. Paragraph (h) bars installing the listed hub in any engine after 2025-10-29.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Missing fact:** The current cycles_since_new value of 3,600 has no as-of date. The count of 2,600 remaining assumes it is current as of the 2026-03-01 snapshot. The dated reading of 3,000 at 2025-10-29 and the 600 engine cycles between the two readings suggest a 1:1 accumulation, but this should be confirmed.
- **Missing fact:** The record does not show whether an engine shop visit has occurred since 2025-10-29 or is scheduled. The 2024-06-10 blend repair is not recorded as an engine shop visit. The shop-visit removal trigger and the 23,200-cycle backstop depend on this.
- **Missing fact:** The record shows no removal of the listed hub within the 100-flight-cycle window that ended at 20,100 cycles. Whether that window controls the deadline affects whether the removal is already overdue.
- **Missing fact:** No operator AD status record for AD 2025-19-13 was supplied. This screen does not rely on any operator-asserted status, and the absence is not evidence either way.
- **Note:** Screening aid only, not a compliance determination. This result does not state whether the engine or hub is compliant, airworthy, or approved for return to service.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0026) is not matched: its P/N appears in table 1, but its S/N is not listed, and the directive requires both P/N and S/N to match.
- **Note:** The 2024-06-10 blend repair and the 2024-06-12 inspection of hub PKLBST7489 do not change the listed status. The directive lists the P/N and S/N regardless of repair history.
- **Note:** The 23,200-cycle figure assumes the hub accumulates cycles one-for-one with engine flight cycles, as the readings between 2025-10-29 and 2026-03-01 suggest (600 hub cycles over 600 engine cycles).
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), row HPT 1st-stage hub, P/N 2A5001, S/N PKLBST7489, removal cycle limit 6,200

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
- **Summary:** AD 2025-19-13 (FR 2025-18469, effective 2025-10-29) applies to V2527-A5 engine SYN-V2500-0027. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed with a 4,800 cycle removal limit and is at 4,750 cycles since new, about 50 cycles short of that limit, so removal is required at the next engine shop visit before the limit is exceeded. The operator's 5,300-cycle AMOC claim has no FAA approval on file and is not relied on.
- **Stated timing:** Remove the HPT 1st-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 4,800 cycles since new. On the current record that limit is reached at engine flight cycle 15,300. The 100-flight-cycle alternative in paragraph (g) ended at engine cycle 15,100, which is earlier, so under 'whichever occurs later' it does not set the deadline.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The current cycles-since-new value of 4,750 is undated. The only dated reading is 4,500 at 2025-10-29. The remaining-cycle figure depends on this value being the 2026-01-20 count, which the 250 engine cycles elapsed since 2025-10-29 would support but the record does not state.
- **Missing fact:** No FAA AMOC approval reference is recorded for the claimed 5,300-cycle limit. Without an approval, the claim cannot change the 4,800-cycle limit in table 1.
- **Missing fact:** The date or schedule of the next engine shop visit is not in the record, and the events list is empty. It is therefore unknown whether a shop visit has occurred since 2025-10-29 or when the next one is planned, which determines whether removal can be completed before the 4,800-cycle limit.
- **Note:** Screening aid only. This is not a compliance determination and does not state that the engine or any part is compliant, noncompliant, airworthy, or approved for return to service.
- **Note:** The engine record is synthetic (SYN- identifiers). Engine cycles were 15,000 at 2025-10-29 and 15,250 at 2026-01-20. The hub's dated CSN reading of 4,500 plus 250 cycles gives 4,750, which matches the undated current value.
- **Note:** The installed 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0027) does not match any S/N in table 1 for that P/N, so it is not a matched part on this record. Its S/N should be confirmed against table 1 if the record is updated.
- **Note:** The 1st-stage hub's removal deadline is about 50 cycles away. Because the shop visit is the trigger and no shop visit is recorded since the effective date, the operator should plan the shop visit before engine cycle 15,300.
- **Note:** The AD's removal limit is per part (CSN), and the record assumes this hub has accumulated its CSN on this engine since its 2020-09-14 installation. The record does not state that directly.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), row HPT 1st-stage hub, P/N 2A5001, S/N PKLBSS9200, removal cycle limit 4,800

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** Model V2524-A5 is in scope and AD 2025-19-13 (effective 2025-10-29) applies. The installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 is a listed hub with a 4,000-cycle removal limit and about 2,600 cycles remaining, so removal is required at the next engine shop visit before that limit or within 100 flight cycles of the effective date, whichever occurs later; the operator's recorded N/A status is not supported by this record.
- **Stated timing:** Remove the listed HPT 2nd-stage hub at the next engine shop visit after 2025-10-29 and before it exceeds 4,000 cycles since new, or within 100 flight cycles from 2025-10-29, whichever occurs later. On the record's cycle counts, the 4,000-cycle limit is reached at engine flight cycle 11,000; the 100-flight-cycle point (engine flight cycle 8,100) has already passed at the 8,400 reading of 2026-02-10.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The current cycles_since_new value of 1400 is undated, while the only dated reading is 1000 on 2025-10-29. The remaining-cycle figure and the deadline depend on the 1400 value being the count at the 2026-02-10 snapshot; the 400-cycle rise matches the 400-cycle rise in engine flight cycles over the same period, which supports that reading but should be confirmed.
- **Missing fact:** The recorded status is not_applicable with the note 'no affected hubs installed', but the record lists an HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 installed on the engine, which matches Table 1 to paragraph (g). The basis for the N/A status needs review.
- **Missing fact:** The date of the next engine shop visit is not known and the events list is empty. The removal must occur at that shop visit (or within the later deadline), so the expected visit date is needed to plan the removal.
- **Note:** The HPT 1st-stage hub record (P/N 2A5001, S/N SYN-HUB1-0028) has a listed P/N but its S/N is not in Table 1 to paragraph (g), so it is not matched on this record. This is a screening result only.
- **Note:** The deadline assumes the hub accumulates cycles one-for-one with engine flight cycles after the snapshot; the record does not give hub cycles by date beyond the 2025-10-29 reading.
- **Note:** Both cycle readings give the same 11,000 engine-flight-cycle deadline (1000 at 8,000 and 1400 at 8,400), so the dating question affects the record consistency more than the deadline.
- **Note:** No removal or replacement event is recorded for the listed hub. This screen does not state compliance or noncompliance and is not an AD status determination; the record is synthetic.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row P/N 2A4802 S/N PKLBST5005, removal cycle limit 4,000

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2025-19-13 (effective 2025-10-29) applies to V2525-D5 engines. The installed HPT 1st-stage hub's serial number (PKLBSK9287) matches a Table 1 entry, but its recorded part number is 2A5001-01 rather than the listed 2A5001, so applicability needs confirmation. If the part numbers are the same, the hub's 2400 cycles since new exceed its 100-cycle removal limit, and removal would be due at the later of the next engine shop visit or 100 flight cycles after 2025-10-29. The installed HPT 2nd-stage hub (S/N SYN-HUB2-0029) is not listed in Table 1.
- **Stated timing:** If the 1st-stage hub is the listed part, remove it at the next engine shop visit after 2025-10-29 or within 100 flight cycles after 2025-10-29, whichever occurs later. The 100-cycle removal limit is already exceeded, so no further cycles can be accrued on that hub under the table limit.
- **Missing fact:** The record gives P/N 2A5001-01, but Table 1 lists P/N 2A5001. Whether the suffix -01 is the same part number must be confirmed before the hub is treated as a listed part. The -01 reading drives both applicability and the removal requirement.
- **Missing fact:** The engine flight-cycle counter at 2025-10-29 (effective date) and at the snapshot is not in the record. It is needed to compute the 100-flight-cycle deadline, which runs from the effective date.
- **Missing fact:** The events list is empty, so no engine shop visit is recorded since the effective date. Any shop visit after 2025-10-29 would trigger removal, and the record must show whether one has occurred.
- **Missing fact:** No operator AD status record for AD 2025-19-13 is supplied. This does not change the directive's requirements but is needed for a full review.
- **Note:** This is a screening aid, not a compliance determination. Compliance status for the installed hub cannot be established from this record.
- **Note:** The P/N discrepancy (2A5001-01 versus 2A5001) is the controlling open question. If the suffix is not the same part number, the 1st-stage hub is not matched under Table 1, and this record shows no action for either hub under the directive, but the identity question must be resolved before that conclusion can be drawn.
- **Note:** The 2400 cycles-since-new figure is taken as the cycles-since-new value that Table 1 uses. The 100-cycle limit is exceeded by 2300 cycles on that reading.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0029) does not match any S/N in Table 1, so it is not a matched part on this record.
- **Note:** Because the 1st-stage hub's limit is already exceeded, the 'within 100 flight cycles' clause is the operative fixed deadline. Its computation needs the engine flight-cycle count at 2025-10-29, which is not in the record, so latest_engine_flight_cycles is null.
- **Note:** No alternative readings with an integer flight-cycle deadline can be computed from this record, so none are listed. The alternative reading for the P/N suffix is described here instead.
- **Note:** The NPRM (2025-10764) was superseded by the final rule and is not relied on for this screen.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row, P/N 2A5001, S/N PKLBSK9287, removal cycle limit 100

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.
