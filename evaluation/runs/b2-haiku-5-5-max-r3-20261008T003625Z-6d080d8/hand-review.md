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
- **Summary:** The directive applies to this V2527-A5 engine and is in force, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) is a Table 1 part with a 5,500-cycle removal limit, so removal and replacement is required at the next engine shop visit and before the hub exceeds that limit (engine flight cycle 45050; 2,400 cycles remaining at the snapshot). The HPT 2nd-stage hub serial number SYN-HUB2-0001 is not listed in Table 1, and no engine shop visit is recorded since the 2025-10-29 effective date.
- **Stated timing:** At the next engine shop visit after the 2025-10-29 effective date, and in no case after the hub reaches 5,500 cycles since new (engine flight cycle 45050). The 100-flight-cycle clause ends at engine flight cycle 41300, which is before the 2026-09-26 snapshot count of 42650; under the 'whichever occurs later' wording it does not set an earlier deadline, so the next engine shop visit controls.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** The events list is empty, so the record does not show whether any engine shop visit (paragraph (i)(2)) has occurred since the 2025-10-29 effective date. A shop visit that already occurred after that date would place the removal requirement at that visit and change the timing analysis; confirm before relying on the timing.
- **Missing fact:** The date or engine flight-cycle count of the next engine shop visit is not in the record. The removal must be done at that visit, so its timing sets when the action falls due, bounded by engine flight cycle 45050.
- **Note:** Screening aid only; this is not a compliance determination and does not state the engine's compliance, airworthiness, or return-to-service status.
- **Note:** The June 2025 NPRM was not relied on; the final rule governs this screen.
- **Note:** Remaining cycles use the current hub CSN of 3100 from the record, not the 1650 reading at 2025-10-29 (which would leave 3850 at that date); the 1450 change in hub CSN matches the 1450 engine flight cycles between 41200 and 42650.
- **Note:** The latest engine flight cycle 45050 equals 42650 plus 2400 and assumes one hub cycle per engine flight cycle while installed, which both dated readings support.
- **Note:** The 100-flight-cycle clause ends at 41300; under 'whichever occurs later' the next engine shop visit controls, but it must occur before the hub exceeds 5,500 cycles since new. The record shows no shop visit and no planned visit date, so the actual due point depends on that future event.
- **Note:** HPT 2nd-stage hub P/N 2A4802 is a listed part number, but S/N SYN-HUB2-0001 is not among the four listed 2nd-stage S/Ns, so it is not recorded as matched; its installed_at date and dated cycle readings are absent but do not affect this match.
- **Note:** Installation prohibition (h) continues to restrict future installation of listed hubs; the removal requirement for the installed hub is in (g).
- **Note:** No ad_records or amoc_claims entries were supplied, so no operator AD status or AMOC claim was considered.
- **Note:** A replacement must be a part eligible for installation under (i)(1); no replacement hub is recorded.
- **Note:** Identifiers beginning with SYN- are synthetic.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row P/N 2A5001 S/N PKLBST5011 limit 5,500
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub rows

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2533-A5 engine is within the applicability of AD 2025-19-13 (Federal Register document 2025-18469, effective October 29, 2025, and in force on the question date). Neither recorded hub matches a P/N and S/N row in table 1, so no paragraph (g) removal is triggered on this record, but the paragraph (h) installation prohibition still binds.
- **Note:** 1st-stage hub: P/N 2A5001 is listed, but serial PKLBST5012 is not one of the table 1 serials for that P/N (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489). It differs from PKLBST5011 by one character and is not treated as a match.
- **Note:** 2nd-stage hub: P/N 2A4802 is listed, but serial SYN-HUB2-0002 is not one of its table 1 serials (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100). Table 1 requires both P/N and S/N, so the P/N match alone does not place the hub in table 1. The SYN- prefix marks this identifier as synthetic, and the record itself is flagged synthetic.
- **Note:** Verification item: confirm both recorded hub serials against the parts' identification before relying on this result. The 1st-stage serial is one character from listed serial PKLBST5011, whose limit of 5,500 cycles would leave 1,300 cycles at the recorded 4,200; if either serial were a table 1 serial, paragraph (g) would apply, and the 100-flight-cycle deadline would need the engine's flight-cycle count as of October 29, 2025, which this record does not contain, so the screen would have to be redone.
- **Note:** Both hubs are recorded at 4,200 cycles since new, but neither has a table 1 limit, so no remaining-cycle figure or deadline is computed here; latest_engine_flight_cycles and component_cycles_remaining are therefore null.
- **Note:** The record has no events, no engine flight-cycle counter, and no hub installation or removal history. None of this changes the result, because no table 1 hub is recorded as installed, but the screen speaks only to the hubs currently recorded and cannot show whether a table 1 hub was installed or removed earlier.
- **Note:** NPRM 2025-10764 (published June 13, 2025) has the same applicability and table 1 but is a proposal and is not relied on. Final rule 2025-18469 is the operative text and was in force on 2026-09-26.
- **Note:** The record has no ad_records or amoc_claims entries, so no operator-asserted AD status or alternative means claim was present to check.
- **Note:** This output is a screening aid for applicability and action timing only; it does not establish the status of this engine or of either hub.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2524-A5 engine is within this directive's applicability, and the directive (effective 2025-10-29) is in force on 2026-09-26. The recorded HPT 2nd-stage hub serial number is not a table 1 pairing, but the installed HPT 1st-stage hub has a table 1 part number with an unknown serial number and unknown cycles, so whether the paragraph (g) removal requirement applies cannot be determined from the record.
- **Stated timing:** Cannot be fixed from the record. If the installed HPT 1st-stage hub is one of the four table 1 serial numbers for P/N 2A5001, removal is due at the next engine shop visit after 2025-10-29 before exceeding that serial number's removal cycle limit, or within 100 flight cycles after 2025-10-29, whichever occurs later. No engine shop visit after 2025-10-29 is recorded, and no engine flight-cycle count is recorded.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub (P/N 2A5001) is unknown. Table 1 lists four serial numbers for this P/N (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489), and the hub is affected only if both its P/N and S/N match a listed pair. Until the serial number is confirmed, applicability and the applicable removal limit cannot be decided, and the unknown value is not evidence that the hub is absent from table 1.
- **Missing fact:** Cycles since new for the HPT 1st-stage hub are unknown. They are needed to compare against the removal cycle limit for the confirmed serial number (100, 4,800, 5,500 or 6,200 cycles) and to compute cycles remaining.
- **Missing fact:** No engine flight-cycle count is recorded as of the directive's effective date. It is needed to evaluate the within-100-flight-cycles limb of paragraph (g) and to state any engine flight-cycle deadline.
- **Missing fact:** No current engine flight-cycle count is recorded at the 2026-09-26 snapshot. It is needed to tell whether the 100-flight-cycle window has already run and how many cycles remain before any deadline.
- **Note:** Screening aid only: this is not a compliance determination, an airworthiness finding, or a return-to-service decision.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003, 5,100 cycles since new) is not among the table 1 serial numbers for 2A4802 (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100), so on this record it is not matched under paragraph (g). Because 5,100 cycles is above the listed removal limits for PKLBST5005 (4,000), PKLBSS9840 (3,900) and PKLBSS0301 (5,000), the serial number record should be verified before relying on the no-match reading.
- **Note:** The HPT 1st-stage hub (P/N 2A5001) is a table 1 part number, but its serial number and cycles are unknown, so it is not recorded as a matched part. Its listed removal limits range from 100 to 6,200 cycles depending on serial number.
- **Note:** Paragraph (g) is read as requiring removal by the later of (a) the next engine shop visit before the applicable cycle limit is exceeded and (b) 100 flight cycles after 2025-10-29. Whether limb (b) has already run by 2026-09-26 depends on engine cycles flown since then, which the record does not supply. No numeric alternative readings are listed because no engine flight-cycle count is available to give them deadlines.
- **Note:** The events list is empty, so no engine shop visit after 2025-10-29 is recorded. If an unrecorded shop visit occurred, the timing analysis would change.
- **Note:** The record does not show installation dates for the hubs. If the HPT 1st-stage hub serial number turns out to be a listed one, its installation date would bear on the paragraph (h) installation prohibition.
- **Note:** The record contains no ad_records or amoc_claims entries for this AD, so there is no operator AD status claim or AMOC claim to check.
- **Note:** The screen relies on the final rule 2025-18469 (effective 2025-10-29). The earlier NPRM 2025-10764 was not relied on.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub rows (P/N 2A5001) and HPT 2nd-stage hub rows (P/N 2A4802)

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The recorded engine model PW1133G-JM is not one of the IAE V2500 models supported by this screen, so no applicability determination is made for AD 2025-19-13 (Federal Register document 2025-18469), which has been in force since its October 29, 2025 effective date. No required action is evaluated and no deadline is computed for this engine.
- **Note:** This screen stops at scope: the engine model is outside the supported IAE V2500 list, so no applicability or compliance determination is made and the (g) removal limits and (h) installation prohibition are not evaluated for this engine.
- **Note:** installed_components and events are empty in the record and were not evaluated because the engine is outside the supported scope.
- **Note:** Identifiers beginning with SYN- (asset_id SYN-ENG-004 and engine_serial_number SYN-PW1100-0004) are synthetic.
- **Note:** The 2025-10764 NPRM is a proposed rule and was not relied on; the final rule 2025-18469 is the document under question.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (Federal Register 2025-18469, in force since 2025-10-29) applies to this V2527E-A5 engine, and its HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is a Table 1 part still recorded as installed. Removal and replacement with a part eligible for installation is required by the later of the 2025-11-12 engine shop visit (18040 cycles) and 100 flight cycles after the effective date (18100 cycles), so by engine flight cycle 18100; the HPT 1st-stage hub S/N SYN-HUB1-0005 is not a Table 1 serial number.
- **Stated timing:** Remove the HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSS9840) and replace it with a part eligible for installation by the later of (a) the next engine shop visit after the 2025-10-29 effective date, which the record places at the 2025-11-12 induction at 18040 engine flight cycles, and (b) 100 flight cycles after the effective date, counted from the 18000-cycle reading on 2025-10-29, which is engine flight cycle 18100. The later date is 18100, 60 cycles after the 18040 snapshot. The 3,900-cycle removal limit is not reached at 1,040 cycles since new.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** The snapshot still lists the HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSS9840) as installed, with no removal or replacement recorded, although the engine was inducted on 2025-11-12. Whether the hub was removed at that induction, and the P/N and S/N of any replacement hub so it can be checked as a part eligible for installation under paragraph (i)(1), are needed to know whether the required action is still outstanding.
- **Note:** Screening aid only, not a compliance determination. The record does not show whether the HPT 2nd-stage hub was removed at the 2025-11-12 induction, so this screen cannot say the required action is done.
- **Note:** Proposed rule 2025-10764 (NPRM, 2025-06-13) is not relied on; final rule 2025-18469, effective 2025-10-29, is the directive under question and was in force on 2025-11-12.
- **Note:** Engine cycle readings: 18000 on 2025-10-29 (effective date) and 18040 on 2025-11-12 (snapshot and induction). The 100-cycle limit is counted from the effective-date reading, giving 18100; 60 cycles remain as of the snapshot.
- **Note:** The shop visit flag (AD 2025-19-13: yes) is the operator's assertion; its source_note says it is asserted by the synthetic operator record. Its detail matches the paragraph (i)(2) definition, and the record indicates neither the transport-only nor the field-maintenance exclusion.
- **Note:** HPT 2nd-stage hub cycles_since_new 1040 is undated; it matches the 1000 reading on 2025-10-29 plus the 40 engine cycles since, so it is used as the current value. Cycles remaining to the 3,900 limit: 2,860.
- **Note:** HPT 1st-stage hub: P/N 2A5001 is a listed P/N, but S/N SYN-HUB1-0005 is not among the Table 1 serial numbers (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489). The serial number is recorded, so the non-match rests on the record; the hub is not matched and is not counted toward component_cycles_remaining.
- **Note:** The record supplies no ad_records or amoc_claims, so no operator AD status claim or AMOC is under review.
- **Note:** Record is synthetic (SYN- identifiers); the answer rests only on the supplied directive text and engine record. If the hub is removed and replaced, check the replacement's P/N and S/N against Table 1 and paragraph (i)(1), and re-screen on updated records.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBSS9840, removal cycle limit 3,900
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub rows for P/N 2A5001
- **Unresolved locator:** 2025-18469 preamble Discussion of Final Airworthiness Directive: responses on terminating action and on superseding or cancelling the AD

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** Model V2530-A5 is within AD 2025-19-13 (Federal Register 2025-18469), which has been in force since its 2025-10-29 effective date. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSK9287) is a listed part with 90 cycles since new against its 100-cycle removal limit, so removal and replacement is required by engine flight cycle 25600 under the 'whichever occurs later' wording.
- **Stated timing:** Remove and replace the HPT 1st-stage hub (P/N 2A5001, S/N PKLBSK9287) with a part eligible for installation at the next engine shop visit after 2025-10-29 and before it exceeds 100 cycles since new, or within 100 flight cycles after the 2025-10-29 effective date, whichever occurs later; on this record the later of these is engine flight cycle 25600.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.
- **Missing fact:** The 90 cycles-since-new value for the installed HPT 1st-stage hub is undated; the only dated reading is 60 on 2025-10-29. The 90 is treated as the value at the 2025-11-20 snapshot because it equals 60 plus the 30 engine flight cycles from 25500 to 25530. A dated reading would confirm the 10 cycles remaining, which set the cycle-limit date.
- **Missing fact:** No engine shop visit after the 2025-10-29 effective date is recorded (events is empty), so the date of the next engine shop visit is unknown. The shop-visit timing matters for the cycle-limit-only alternative reading, under which removal would have to occur at a shop visit before the hub passes 100 cycles since new; any shop visit should be recorded with its qualifies_as_engine_shop_visit status.
- **Note:** Screening aid only; this does not determine compliance with the AD.
- **Note:** Deadline: 100 flight cycles after the 25500 engine reading dated 2025-10-29 is engine flight cycle 25600. The hub reaches its 100-cycle limit at 25540, but under the 'whichever occurs later' wording the 25600 date is the later of the two timing prongs, so it is the latest date. As of the 25530 reading on 2025-11-20, 70 engine flight cycles remain to 25600.
- **Note:** Cycle arithmetic: 100 minus 90 cycles since new leaves 10 cycles. The hub count rose by 30 between engine cycles 25500 and 25530, matching the engine's 30 flight cycles, so it is taken to accumulate one cycle per engine flight cycle, giving engine cycle 25540 for the 100-cycle point.
- **Note:** Under the literal later-of wording, a shop visit before 25600 does not move the latest date earlier; shop-visit timing matters mainly for the cycle-limit-only alternative reading.
- **Note:** The hub was recorded as installed on 2025-09-30, before the 2025-10-29 effective date, so that installation is not a paragraph (h) prohibited installation on this record; any later installation of a listed hub in any engine would be prohibited.
- **Note:** The HPT 2nd-stage hub has listed P/N 2A4802, but its S/N SYN-HUB2-0006 is not among the table 1 serial numbers for that P/N (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100), so it is not matched on this record; its missing installed_at date does not change this screen.
- **Note:** The record has no ad_records or amoc_claims entries, so there are no operator claims to check and no AMOC is assumed.
- **Note:** NPRM 2025-10764 (proposed rule, published 2025-06-13) was not relied on; final rule 2025-18469 governs. The record does not identify a replacement part; any replacement must meet paragraph (i)(1).
- **Unresolved locator:** 2025-18469 (g) Required Actions; Table 1 to Paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSK9287 (limit 100 cycles since new)
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub rows (P/N 2A4802)

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

## seed-007: Both HPT hubs are listed, with different removal limits

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (final rule 2025-18469, in force since 2025-10-29) applies to this V2528-D5 engine, and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 is a listed part with a 6,200 cycles-since-new removal limit and 3,700 cycles remaining at 2,500 cycles since new, so removal and replacement is required at the next engine shop visit and before that limit is exceeded. The HPT 2nd-stage hub's serial number and cycles since new are unknown, so the record cannot show whether it is an affected part.
- **Stated timing:** Removal and replacement is due at the next engine shop visit after 2025-10-29 and, in any case, before the HPT 1st-stage hub exceeds 6,200 cycles since new, which falls at engine flight cycle 54,200 if the hub keeps accumulating cycles one for one with the engine (3,700 cycles after the 50,500 snapshot). The 100-flight-cycle alternative (engine flight cycle 50,100) has already passed but, under the 'whichever occurs later' wording, does not set the deadline.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** Serial number is recorded as unknown. Part number 2A4802 matches the Table 1 HPT 2nd-stage hub part number, so the hub is an affected part only if its serial number is PKLBST5005, PKLBSS9840, PKLBSS0301 or PKLBSR2100. The record neither confirms nor clears it, so it is not treated as affected or unaffected.
- **Missing fact:** Cycles since new are recorded as unknown. If the serial number matches a Table 1 row, the removal limit is 3,900 to 6,000 cycles since new depending on the serial number, and the remaining cycles and deadline cannot be computed without this value.
- **Missing fact:** The current value of 2,500 is undated. It is taken as the 2026-03-10 value, consistent with the dated 2,000 reading at 2025-10-29 and the same 500-cycle increase as the engine counter. Confirm it, since the 3,700 remaining cycles and the 54,200 engine-cycle deadline depend on it.
- **Missing fact:** The events list is empty, so no engine shop visit since the 2025-10-29 effective date is on record. Confirm that none has occurred under the paragraph (i)(2) definition. A shop visit that has occurred would have made removal due at that visit, which would change the timing above.
- **Note:** Screening aid only; this is not a compliance determination and does not state any engine's or part's AD status.
- **Note:** The operative text is final rule 2025-18469 (AD 2025-19-13), effective 2025-10-29; no later correction or superseding document appears in the supplied material. NPRM 2025-10764 is a proposal that cannot require action; its Table 1 matches the final rule.
- **Note:** V2528-D5 is a supported model, so this screen makes an applicability determination.
- **Note:** Cycle arithmetic: the record gives 50,000 engine flight cycles at 2025-10-29 and 50,500 at 2026-03-10, and the 1st-stage hub reads 2,000 cycles since new at 2025-10-29 and 2,500 in the current record. The hub is taken to accumulate cycles one for one with the engine counter, which the dated readings support, so its 6,200 limit falls at engine flight cycle 54,200 (50,500 + 3,700).
- **Note:** Grace period: 50,000 + 100 = 50,100. That alternative is past at the 50,500 snapshot, but the 'whichever occurs later' wording makes the shop-visit and cycle-limit alternative controlling. The record shows no engine shop visit since 2025-10-29, so the shop-visit trigger has not occurred on this record.
- **Note:** component_cycles_remaining reports only the confirmed 1st-stage hub. If the 2nd-stage hub's serial number matches Table 1, its limit (3,900 to 6,000 cycles since new depending on serial number) and the same trigger would apply, and the smallest affected-part figure could then be lower than 3,700.
- **Note:** Paragraph (h) addresses installations after the effective date. The 1st-stage hub was installed on 2024-06-03, before the effective date, so its existing installation is governed by paragraph (g).
- **Note:** Removal under paragraph (g) does not end applicability. The final rule's response to comments explains that the installation prohibition in paragraph (h) keeps the AD applicable after affected hubs are removed.
- **Note:** Replacement hubs must have a P/N and S/N not listed in Table 1 (paragraph (i)(1)). The ad_records and amoc_claims entries are absent from the record, so there are no operator AD-status entries or AMOC claims to check; their absence is not evidence either way.
- **Note:** The record is synthetic (SYN- identifiers).
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row: P/N 2A5001, S/N PKLBST7489, removal cycle limit 6,200
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub rows: P/N 2A4802 with S/Ns PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100
- **Unresolved locator:** 2025-10764 preamble NPRM published 2025-06-13, Docket FAA-2025-0926

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** Model V2522-A5 is within the applicability of this in-force AD (effective 2025-10-29). The record lists no installed components and no events, so whether a table 1 HPT 1st- or 2nd-stage hub is installed, and whether a shop visit occurred after the effective date, cannot be determined and the screen needs review.
- **Stated timing:** Only if a table 1 hub is installed: at the next engine shop visit after 2025-10-29 that occurs before the hub exceeds its table 1 removal cycle limit, or within 100 flight cycles after 2025-10-29, whichever occurs later. The record gives no cycle counts or shop visit date, so no calendar or cycle date can be fixed.
- **Missing fact:** No HPT 1st-stage hub record is supplied because installed_components is empty. Needed: installed P/N and S/N and cycles since new, to test against table 1 (P/N 2A5001 with an S/N listed in table 1) and its removal cycle limit. An empty list does not show that the hub is absent or unaffected.
- **Missing fact:** No HPT 2nd-stage hub record is supplied. Needed: installed P/N and S/N and cycles since new, to test against table 1 (P/N 2A4802 with an S/N listed in table 1) and its removal cycle limit. An empty list does not show that the hub is absent or unaffected.
- **Missing fact:** The engine flight-cycle count on the effective date is not recorded. It is needed to convert the 100-flight-cycle clause into a cycle number.
- **Missing fact:** The current engine flight-cycle count at the snapshot date is not recorded. It is needed to show whether any table 1 cycle limit or the 100-cycle point has already passed for an installed hub.
- **Missing fact:** The events list is empty. Needed: any engine shop visit after 2025-10-29 and the operator's qualifies_as_engine_shop_visit determination for it, because that visit starts the removal window; and any installation of a table 1 hub after 2025-10-29, which paragraph (h) prohibits.
- **Note:** Screening aid only, not a determination about this engine or any part. The record is marked synthetic; its SYN- identifiers and values are taken as supplied.
- **Note:** Applicability rests on the engine model: V2522-A5 is on the supported model list and in paragraph (c). The preamble rejects a request to limit applicability to serial numbers known to have affected hubs, so the engine serial number does not change the applicability answer.
- **Note:** installed_components and events are both empty. An empty list is not evidence that a table 1 hub is absent or unaffected, so no table 1 P/N and S/N match was made and matched_parts is empty.
- **Note:** If the records later confirm that no table 1 hub is installed, the paragraph (g) removal would not be triggered, but the paragraph (h) installation prohibition would continue to bind.
- **Note:** Engine shop visit under (i)(2) excludes flange separation solely for transport without later engine maintenance, and engine removal for field maintenance at a maintenance facility in lieu of on-wing work. No event carries an operator qualifies_as_engine_shop_visit determination, so none can be applied.
- **Note:** Deadline wording: where a hub's table 1 cycle limit falls before the 100-flight-cycle date and no shop visit intervenes, the literal 'whichever occurs later' wording points to the 100-cycle date, while a reading that the cycle limit caps removal points to the earlier limit date (already passed if the limit preceded the effective date). These readings give different deadlines, but neither can be dated from this record, so alternative_readings is left empty.
- **Note:** The question date is nearly eleven months after the effective date, so any deadline tied to a shop visit or cycle count may already have passed for an installed hub; the record cannot show whether it has.
- **Note:** The final rule is in force on the question date. The NPRM 2025-10764 was superseded by the final rule and was not relied on.
- **Note:** No ad_records or amoc_claims are present, so no operator assertion about this AD or any AMOC was considered; such assertions would not settle the outcome in any case.
- **Note:** The engine.flight_cycles paths in missing_facts are proposed names; the record has no engine cycle counter.
- **Note:** Table 1 pairs (cycle limits are cycles since new): P/N 2A5001 HPT 1st-stage hub with S/N PKLBSK9287 (100), PKLBSS9200 (4,800), PKLBST5011 (5,500), PKLBST7489 (6,200); P/N 2A4802 HPT 2nd-stage hub with S/N PKLBST5005 (4,000), PKLBSS9840 (3,900), PKLBSS0301 (5,000), PKLBSR2100 (6,000).
- **Unresolved locator:** 2025-18469 (i)(2) Definitions, engine shop visit and exclusions (i)(2)(i) and (i)(2)(ii)
- **Unresolved locator:** 2025-18469 preamble Discussion of comments: requests to add terminating action and to supersede or cancel

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not among the ten IAE AG models listed in the applicability paragraph of Federal Register document 2025-18469 (AD 2025-19-13), so this screen gives no applicability determination, action status, or cycle figure. The directive took effect October 29, 2025 and is in force on the question date of 2026-09-26.
- **Note:** Recorded model V2500-A1 is not a supported model for this screen, so no applicability determination, timing, or cycle figure is given.
- **Note:** If the model value is a recording error, rerun the screen on the verified model designation before drawing any applicability conclusion.
- **Note:** Table 1 to paragraph (g) was not applied to the installed HPT 1st-stage hub because paragraph (c) does not reach this engine model; no matched part or cycle figure is reported.
- **Note:** No continuing obligations are listed because they bind only while the directive applies to an engine within paragraph (c).
- **Note:** Paragraph (h) says 'in any engine', but the final rule preamble says the installation prohibition applies to models listed in the Applicability paragraph; no installation-prohibition conclusion is drawn for this model.
- **Note:** The 2025 NPRM (2025-10764) lists the same models and was not relied on; the final rule 2025-18469 is the directive under question.
- **Note:** No later superseding document was provided, so authority_state rests only on the documents supplied.
- **Note:** The engine events list is empty, so no shop visit history is available for a rerun.
- **Note:** The record is marked synthetic and uses SYN- identifiers.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** On this screen, the V2527-A5 engine's recorded 3rd stage HPC rotor blade set (P/N 6A8353) falls within AD 2026-17-03, which has been in force since its 2026-09-24 effective date. Replacement of the full blade set is triggered only by the next engine shop visit after that date where a 3rd stage HPC rotor blade is exposed, and no such visit is recorded, so no replacement is triggered on this record.
- **Stated timing:** Event-driven, with no fixed calendar or flight-cycle deadline: replace the full 3rd stage HPC rotor blade set at the next engine shop visit (induction of the engine into the shop for maintenance) after the 2026-09-24 effective date at which any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum; no such visit is recorded.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Note:** Screening aid only: this is not a compliance determination and does not address return to service for the engine or any part.
- **Note:** Model check: V2527-A5 is on the supported list and is named in paragraph (c) of 2026-16954.
- **Note:** Part match: the recorded 3rd stage HPC rotor blade set is P/N 6A8353, which matches a listed P/N exactly. The directive lists part numbers only, so the 'not tracked at set level' serial entry does not block the match. The record shows no suffixed 6A8353-001 blade, which paragraph (h)(1)(ii) would treat as an eligible modified part rather than the base listed part.
- **Note:** Authority: 2026-16954 is effective 2026-09-24 and so is in force on 2026-10-05. The correction 2026-18423 (published 2026-09-10) changed paragraph (g) from 'rotor is exposed' to 'rotor blade is exposed' and left the effective date unchanged; the corrected wording is applied here. The NPRM 2025-20088 proposed an exposure-based trigger that the final rule did not adopt, so it is not applied.
- **Note:** Trigger: the action is event-driven. The events list is empty, so no engine shop visit after the effective date is recorded and no replacement is triggered on this record; an empty list only means no event is recorded. If the engine is inducted for maintenance and any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum, the full set must be replaced at that visit. Confirm the event log is complete, because an unrecorded post-effective-date shop visit with blade exposure would make replacement due at that visit.
- **Note:** Interpretation: the phrase 'after the effective date' in paragraph (g) attaches to the engine shop visit (induction). The preamble says the FAA does not intend to reach engines inducted before the effective date. Readings of the trigger remain event-based with no computable cycle deadline, so no alternative deadline is listed.
- **Note:** Service bulletin: the final rule preamble says replacing the blades per IAE AG SB V2500-ENG-72-0716 (dated October 4, 2024) changes the part numbers to eligible P/Ns and would meet the replacement requirement. The AD does not incorporate that SB, and the SB is not in the supplied record.
- **Note:** Deadlines: the record has no engine flight-cycle counter or install date. The AD sets no calendar or cycle limit, so latest_engine_flight_cycles and component_cycles_remaining are null. The record has no ad_records or amoc_claims, so no AMOC claim is relied on.
- **Unresolved locator:** 2026-16954 (g) text as corrected by 2026-18423

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** AD 2026-17-03 (FR 2026-16954, paragraph (g) as corrected by FR 2026-18423) is in force as of 2026-10-05 but applies only to listed IAE AG models, including the V2533-A5, that have 3rd stage HPC rotor blade P/N 6A8353 or 6A8688 installed. The recorded blade set is P/N 6C8368, which the AD lists as a part eligible for installation rather than an affected P/N, so on the supplied facts the engine falls outside the stated applicability and no required action is triggered.
- **Note:** Screening aid only; this is not a compliance determination, airworthiness finding, or return-to-service decision.
- **Note:** Authority: FR 2026-16954 is a final rule effective 2026-09-24 under its paragraph (a), so it is in force on the 2026-10-05 question date. The NPRM FR 2025-20088 (published 2025-11-18) is a proposal superseded by the final text and was not relied on; its proposed trigger (next 3rd stage HPC rotor blade exposure after the effective date, with no shop visit limit) differs from the final rule.
- **Note:** The correction FR 2026-18423 (published 2026-09-10, effective 2026-09-24) changes only paragraph (g), inserting the word blade so that it reads where the 3rd stage HPC rotor blade is exposed. The corrected wording is used here; it does not change applicability.
- **Note:** Paragraph (c) turns only on installed blade P/N 6A8353 or 6A8688 and has no serial number criterion, so the untracked set-level serial number does not change the result. Paragraph (h)(1)(i) lists P/N 6C8368 as a part eligible for installation.
- **Note:** The record tracks the blade set only at set level, so this screen takes the recorded set P/N 6C8368 as the P/N of every blade in the set. A reviewer should confirm that no blade in the set is P/N 6A8353 or 6A8688, because one such blade would meet paragraph (c) and change this result.
- **Note:** The events list is empty, so no engine shop visit is recorded. An empty list is not evidence that no shop visit occurred, but it does not change the result while applicability is not met. If an affected blade were found, paragraph (g) as corrected would require full-set replacement with parts eligible for installation at the next engine shop visit after 2026-09-24 in which the 3rd stage HPC rotor blade is exposed, with no flight-cycle deadline.
- **Note:** No ad_records or amoc_claims were supplied, so no operator-asserted AD record or alternative method of compliance was relied on.
- **Note:** The record has no engine flight-cycle counter and the AD sets no blade cycle limit, so no cycle-based figures are given.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2527E-A5 record shows a 3rd stage HPC rotor blade set with P/N 6A8353, which falls within the proposed applicability of this NPRM. The document is a proposed rule with no effective date, so it is not in force and no action is triggered as of 2026-01-15; the proposed full-set replacement would be due only at the next 3rd stage HPC rotor blade exposure after a future effective date.
- **Stated timing:** Nothing is due now because the proposal has no effective date and is not in force; if a final rule is adopted as proposed, the full-set replacement would be due at the next 3rd stage HPC rotor blade exposure after its effective date, with no fixed flight-cycle or calendar limit.
- **Missing fact:** No final rule, correction, or effective date for this AD was supplied; the only document is the NPRM (Type Proposed Rule, Effective date none). Confirm whether the FAA has published a final rule with an effective date on or before 2026-01-15, because only an in-force AD can require action and any trigger depends on that effective date.
- **Missing fact:** The events list is empty, so no removal of a 3rd stage HPC rotor blade from the HPC stage 3 to 8 drum is recorded. An empty list is not evidence that no exposure occurred; the exposure history since any effective date is needed to apply the proposed trigger in paragraph (g) if a final rule takes effect.
- **Missing fact:** Only a set-level P/N of 6A8353 is recorded; blade-level part numbers are not given. The set-level entry meets the applicability test as written, but the blade-level part numbers in the set should be confirmed because the directive tests P/N per blade.
- **Missing fact:** Serial numbers are not tracked at set level. The proposal tests part numbers rather than serial numbers, so this does not change applicability, but individual blade identification would be needed to document the blades removed at any future exposure and the eligible replacement parts installed.
- **Note:** Screening aid only: this is not an AD status determination, an airworthiness finding, or an approval for return to service, and no finding is made on the engine or any part.
- **Note:** The document is a proposed rule (NPRM, Docket FAA-2025-2555, Project Identifier AD-2025-00433-E) published 2025-11-18 with comments due January 2, 2026; the comment period closing before the question date does not make the proposal effective, and no final rule was supplied.
- **Note:** Engine model V2527E-A5 is on the supported scope list, so this screen applies.
- **Note:** If the proposal is adopted as written, the recorded set-level P/N 6A8353 would place the engine within paragraph (c), and the proposed action would be triggered only by the next 3rd stage HPC rotor blade exposure after the effective date.
- **Note:** The directive's trigger is a blade exposure as defined in paragraph (h)(2), not an engine shop visit, so the qualifies_as_engine_shop_visit convention does not apply to this screen.
- **Note:** The engine record has no engine flight-cycle counter. None is needed here because the proposal sets no cycle-based deadline, so latest_engine_flight_cycles and component_cycles_remaining are null.
- **Note:** The record contains no ad_records or amoc_claims entries. Nothing in the record is treated as an AD status or as an alternative method (AMOC) claim, and no AMOC evaluation is needed for a proposal that is not in force.
- **Note:** Re-screen if a final rule is published: check its effective date, whether the applicability and trigger text changed from this NPRM, and the exposure history since that effective date.
- **Unresolved locator:** 2025-20088 preamble Document header (Type: Proposed Rule; Effective date: none) and DATES (comments due January 2, 2026)

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 (final rule 2025-17066, effective October 10, 2025) is in force on 2025-11-15 and applies to this V2527-A5 engine. The operator record states that neither its approved maintenance program nor TLM paragraph B.1 yet incorporates table 1, so the paragraph (g)(1) and (g)(2) revisions are due on or before January 8, 2026, 54 days after the question date.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e. on or before January 8, 2026, for the paragraph (g)(1) TLM ALS revision and, because this is an air carrier operation, the paragraph (g)(2) approved maintenance program revision. The deadline is calendar-based, so no flight-cycle deadline applies.
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** No component record is supplied for the HPT Stage 1 Hub (table 1 P/N 2A5001). installed_components is empty, so whether such a hub is installed, and its serial number and history, cannot be confirmed; an empty list is not evidence that the hub is absent or unaffected. This does not change the revision requirement, which applies to the engine model, but it is needed to determine whether and when TASK 72-45-11-200-006 applies to this hub at piece-part exposure.
- **Missing fact:** No component record is supplied for the HPT Stage 2 Hub (table 1 P/N 2A4802) for the same reason. This does not change the revision requirement, but it is needed to determine whether and when TASK 72-45-31-200-009 applies to this hub at piece-part exposure.
- **Missing fact:** The record names the V2500-A5 TLM without its part number and identifies the approved program only by revision number. Confirm the TLM part number (paragraph (g)(1)(i) lists P/N 2A4408 for V2500-A5) and the name and revision of the approved maintenance or inspection program that paragraph (g)(2) requires revising, so the correct documents are revised.
- **Note:** Screening aid only, not a compliance determination. The record is synthetic (SYN- identifiers) and is used as supplied; the operator's statement that table 1 is not yet incorporated is taken as recorded and is not verified here.
- **Note:** Operative text: final rule 2025-17066 (AD 2025-17-16, Amendment 39-23126). No correction or later superseding document was supplied. NPRM 2024-26092 is a proposal and was not relied on; the final rule changed its wording, including the stage 2 hub task (now TASK 72-45-31-200-009) and the reference from the EMM to the TLM.
- **Note:** Trigger date: the 90-day periods run from the October 10, 2025 effective date in paragraph (a) and the DATES section, not from the September 5, 2025 publication date or the August 28, 2025 issuance date. Counting from publication would wrongly give December 4, 2025.
- **Note:** As of 2025-11-15, 54 days remain and the deadline has not passed. The engine record has no flight-cycle counter and no component cycle data, so latest_engine_flight_cycles and component_cycles_remaining are null.
- **Note:** installed_components is empty. That is not evidence that either table 1 hub is absent or unaffected. The revision requirement applies to the engine model and does not depend on which hubs are installed, so the action status stands; only hub-level inspection planning depends on the missing component records.
- **Note:** Table 1 ties the hub inspections to piece-part exposure in paragraph B.1 rather than to a flight-cycle interval, and the AD text states no cycle limit for either hub. A commenter (SIAEC) cited a 20,000-cycle replacement threshold in another manual; that figure is not in the AD and was not used.
- **Note:** The events list is empty, so no shop visit or piece-part exposure is recorded. Once paragraph B.1 is revised, a later piece-part exposure would bring the table 1 tasks into play; this screen does not evaluate any such event.
- **Note:** The record has no ad_records or amoc_claims entries, so no AMOC is claimed and no operator-recorded AD status is relied on. Any alternative method must be approved under paragraph (i).
- **Note:** Per the preamble, the FAA disagreed that the EMM revision is solely the OEM's responsibility: the operator must include the table 1 tasks regardless of the EMM version it is required to hold.
- **Note:** Paragraph (b) lists no affected ADs. The FAA declined to make this AD a supersedure of AD 2004-12-08, so that AD's requirements are separate and are not assessed here.
- **Note:** V2527-A5 is on the supported model list.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** Model V2522-A5 is listed in paragraph (c) of the directive, which has been in force since its October 10, 2025 effective date, so the paragraph (g)(1) revision of the airworthiness limitations section in the applicable V2500-A5 Time Limits Manual is required by January 8, 2026; the paragraph (g)(2) program revision has the same deadline but applies only to air carrier operations, which the record leaves unknown. The record has no operator AD entry, no installed components and no events, so it cannot show whether either revision has been made or whether either hub is installed.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, that is on or before January 8, 2026, for the paragraph (g)(1) revision; the paragraph (g)(2) revision has the same deadline and applies only to air carrier operations. The directive sets no separate date for the hub inspections, which are tied to piece-part exposure once incorporated. As of the November 15, 2025 question date, 54 days remain before the deadline.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** The record says the operator's air carrier status is unknown. That decides whether the paragraph (g)(2) revision of the existing approved maintenance or inspection program applies. It does not affect the paragraph (g)(1) revision, which has no air carrier condition.
- **Missing fact:** The record has no operator AD entry for this directive, so the screen cannot see whether the paragraph (g)(1) revision, or the paragraph (g)(2) program revision where it applies, is already recorded as done. A missing entry is not evidence that either revision was or was not made.
- **Missing fact:** The record lists no installed components, so it is unknown whether an HPT Stage 1 hub, P/N 2A5001, is installed. This matters for the table 1 hub inspection (TASK 72-45-11-200-006) at a future piece-part exposure; an empty list is not evidence that the hub is absent.
- **Missing fact:** The record lists no installed components, so it is unknown whether an HPT Stage 2 hub, P/N 2A4802, is installed. This matters for the table 1 hub inspection (TASK 72-45-31-200-009) at a future piece-part exposure; an empty list is not evidence that the hub is absent.
- **Missing fact:** The operator's Time Limits Manual edition and ICA for this engine, including the V2500-A5 TLM named in paragraph (g)(1)(i) (P/N 2A4408, TASK 05-10-00-990-000-B00), and whether its paragraph B.1 already contains the table 1 tasks, are not in the engine record. The content of that document is needed to confirm the revision outside this screen.
- **Note:** Screening aid only, not a compliance determination. The record is synthetic (identifiers starting with SYN- are synthetic); this screen uses only the supplied engine record and the final rule text.
- **Note:** The 90-day period runs from the stated effective date of October 10, 2025, not from the September 5, 2025 Federal Register publication date or the November 2024 proposal.
- **Note:** Proposed rule 2024-26092 was not relied on. Its table listed TASK 72-45-11-200-009 for the HPT Stage 2 hub; the final rule changed that reference to TASK 72-45-31-200-009, which is the text applied here.
- **Note:** Paragraph (g)(1) has no air carrier condition; only paragraph (g)(2) does. Confirm the operator's air carrier status before finalizing the (g)(2) item.
- **Note:** Paragraph (g)(1)(i) names the V2500-A5 TLM (P/N 2A4408, TASK 05-10-00-990-000-B00), which appears to be the applicable reference for a V2522-A5; the record does not show which TLM edition or ICA the operator holds.
- **Note:** Applicability in paragraph (c) is by engine model only. The record has no airframe or registry data, which does not change the model-based result.
- **Note:** The ICA revision is dated, but the hub inspections themselves are done at piece-part exposure per the preamble. Events is empty and no hub components are listed, so no piece-part exposure is shown and the hub inspections cannot be assessed from this record; empty lists are not evidence of absence.
- **Note:** Neither latest_engine_flight_cycles nor component_cycles_remaining can be computed: the deadline is calendar-based and the directive lists no cycle limit for the hubs. The 20,000 flight-cycle figure in the preamble is a commenter description of an existing AMP section 18 replacement limit, not a limit in this AD.
- **Note:** The record has no ad_records or amoc_claims entries, so no alternative method of compliance and no operator-recorded AD status for this directive appears in the record.

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 engine is within the directive's applicability, and its installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) matches Table 1 with 5,010 cycles remaining to its 6,000-cycle removal limit as of the 15 October 2025 snapshot. Because final rule 2025-18469 does not take effect until 29 October 2025, no action is triggered on the question date; from that date the hub must be removed and replaced at the next engine shop visit before the limit is exceeded or within 100 flight cycles, whichever occurs later.
- **Stated timing:** Not yet triggered: the AD takes effect 29 October 2025. From that date, remove the HPT 2nd-stage hub (S/N PKLBSR2100) from service and replace it with a part eligible for installation at the next engine shop visit after 29 October 2025, before the hub exceeds 6,000 cycles since new, or within 100 flight cycles after 29 October 2025, whichever occurs later.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The engine record has no engine flight-cycle counter, so the engine's flight-cycle count on the 29 October 2025 effective date is unknown. Without it the 100-flight-cycle alternative cannot be turned into an engine flight-cycle deadline, which is why latest_engine_flight_cycles is null.
- **Missing fact:** The events list is empty, so no engine shop visit is recorded and the date of the next engine shop visit after 29 October 2025 is unknown. Whether that visit occurs before the 6,000-cycle limit is reached, and whether the operator's record states that it meets the paragraph (i)(2) engine shop visit definition, determines when removal falls.
- **Note:** Screened against Federal Register document 2025-18469 (final rule, AD 2025-19-13, published 24 September 2025, effective 29 October 2025). The NPRM 2025-10764 (published 13 June 2025) is only a proposal with no legal effect and was not relied on, although its Table 1 lists the same hub entries.
- **Note:** The question date (15 October 2025) precedes the effective date, so the paragraph (g) removal duty and the paragraph (h) installation prohibition cannot be required on this date and take effect on 29 October 2025.
- **Note:** The 6,000-cycle limit counts the hub's cycles since new, not engine flight cycles. The 5,010 remaining figure is as of the 15 October 2025 snapshot and reduces as the hub accrues cycles; it could be read as an engine flight-cycle count only if the hub has flown all its cycles on this engine, which the record does not state.
- **Note:** Read as written, 'whichever occurs later' sets the due point at the later of (a) the next engine shop visit after 29 October 2025, with removal before the 6,000-cycle limit is exceeded, and (b) 100 flight cycles after 29 October 2025. Neither point can be stated as an engine flight-cycle number from this record, so no alternative-reading counts are given; confirm this reading before relying on any date.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0018, 2,000 cycles since new) is not listed in Table 1 for that part number, so it is not matched and no remaining-cycle figure is given for it. Identifiers beginning SYN- are synthetic and were matched as ordinary identifiers.
- **Note:** No ad_records or amoc_claims were supplied, so no operator AD-status assertion or AMOC claim was relied on or checked.
- **Note:** This is a screening aid, not a compliance determination; nothing here states that the engine or any part is compliant, noncompliant, airworthy, or approved for return to service.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row: P/N 2A4802, S/N PKLBSR2100, limit 6,000
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub rows: P/N 2A5001

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (Federal Register document 2025-18469, in force since its 2025-10-29 effective date) applies to this V2531-E5 engine, and its installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is listed in Table 1 and is already past its 4,800-cycle removal limit at 4,990 cycles since new. Removal and replacement is required at the next engine shop visit and no later than 100 flight cycles after the effective date, which is engine flight cycle 60100 (60 cycles remain at the 60040 reading on 2025-11-05).
- **Stated timing:** Remove and replace the HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) at the next engine shop visit after the 2025-10-29 effective date and no later than 100 flight cycles after that date, which is engine flight cycle 60100. The hub's 4,800-cycle limit has already passed, so under the whichever-occurs-later clause the 100-flight-cycle date controls; 60 cycles remained at the 60040 reading on 2025-11-05.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The events list is empty, so the record does not show whether any engine shop visit has occurred or is scheduled since the 2025-10-29 effective date. Removal is tied to the next engine shop visit, and a qualifying visit since the effective date would bring the removal requirement into play at that visit. An empty list is not evidence that no visit occurred, so the shop-visit history should be checked against the definition in paragraph (i)(2).
- **Note:** Screening aid only; this is not a compliance determination. The operative document is final rule 2025-18469 (AD 2025-19-13), effective 2025-10-29 and in force on 2025-11-05. NPRM 2025-10764 is a superseded proposal and was not relied on.
- **Note:** V2531-E5 is a supported model listed in paragraph (c). The engine record is marked synthetic.
- **Note:** Matching uses both P/N and S/N against Table 1. The HPT 1st-stage hub matches the 2A5001 / PKLBSS9200 row (4,800-cycle limit). Its recorded count is 4,990 cycles since new (undated field) and 4,950 on 2025-10-29; the 40-cycle change equals the 40 engine cycles from 60000 to 60040, so the undated value is read as the 2025-11-05 count. The hub is 190 cycles past its limit on that count and was 150 cycles past on 2025-10-29.
- **Note:** Deadline: the hub was already past 4,800 cycles at the effective date, so the before-exceeding date in the whichever-occurs-later clause cannot be met and the 100-flight-cycle date controls. That date is engine flight cycle 60100, counted from the 60000 reading dated 2025-10-29. The reading has no time of day, so the figure assumes it is the count at the effective date. The 100-cycle period runs from the effective date, not from the 2025-11-05 snapshot (60040).
- **Note:** A reading that treats the 100-cycle clause only as a floor, leaving removal open-ended until the next shop visit, would give no flight-cycle date. It is not used because, with the 4,800-cycle branch already unavailable, the whichever-occurs-later clause leaves the 100-flight-cycle date as the operative limit.
- **Note:** HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0019 is not matched. Its P/N appears in Table 1, but its recorded S/N is not one of the four listed for that P/N, and the table limits attach only to listed P/N and S/N pairs. This is a match result on the recorded identifiers, not a finding about the hub's condition.
- **Note:** The events list is empty. No engine shop visit is recorded since the effective date, and an empty list does not show that no visit occurred.
- **Note:** No ad_records or amoc_claims entries for AD 2025-19-13 are in the record. No operator-asserted AD status or AMOC was considered or relied on.
- **Note:** The replacement hub must be an HPT 1st-stage hub whose P/N and S/N are not listed in Table 1 (paragraph (i)(1)). Under the preamble response to comments, the AD continues to apply after removal because of the installation prohibition.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row: P/N 2A5001, S/N PKLBSS9200, removal cycle limit 4,800
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub rows for P/N 2A4802

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **No answer:** answer is not JSON: Unterminated string starting at: line 1 column 7023 (char 7022)

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (FR doc 2022-02574) does not take effect until 2022-03-15, after the 2022-03-01 question date, so it cannot require action now. The V2533-A5 engine's installed HPT 1st-stage and HPT 2nd-stage disk part numbers match the directive, but the Appendix A serial-number listings and the Figure 1 compliance times are not in the supplied text, so applicability and any due date cannot be settled.
- **Stated timing:** Not before the directive's effective date of 2022-03-15. Once effective, the HPT 1st-stage disk ultrasonic inspection under paragraph (g)(1) and the HPT 2nd-stage disk inspection under paragraph (g)(2) are due within the Figure 1 to paragraph (g)(1) compliance time or within 10 flight cycles after 2022-03-15, whichever occurs later; Figure 1 is not in the supplied text, so no due date can be computed.
- **Missing fact:** Appendix A serial-number listings are not in the supplied text: Table 1 (HPT 1st-stage disk) and Table 2 (HPT 2nd-stage disk) of IAE NMSB V2500-ENG-72-0713 Rev 1 or NMSB V2500-E5-72-0015 Rev 1. Whether S/N SYN-DISK1-0020 and S/N SYN-DISK2-0020 are listed decides whether the engine falls within paragraph (c)(1) and/or (c)(2); matching part numbers alone do not.
- **Missing fact:** Figure 1 to paragraph (g)(1), which sets the compliance time for the (g)(1) and (g)(2) inspections, is an image not included in the supplied text. Without it no due date or cycle-based deadline can be computed.
- **Missing fact:** The engine flight-cycle count is not recorded. It is needed to apply the 10-flight-cycle limit that runs from 2022-03-15 and to convert any Figure 1 time into an engine flight-cycle number.
- **Missing fact:** Accumulated flight cycles of the HPT 1st-stage disk are not recorded. They are needed to test any Figure 1 limit that counts disk cycles and to compute cycles remaining.
- **Missing fact:** Accumulated flight cycles of the HPT 2nd-stage disk are not recorded, for the same reasons as the 1st-stage disk.
- **Missing fact:** The events list is empty, so no engine shop visit is recorded. If the Figure 1 time is keyed to the next engine shop visit, as the superseded AD 2021-11-15 time was, timing cannot be assessed; an empty list does not show that no shop visit has occurred.
- **Note:** Screened against FR doc 2022-02574 (AD 2022-02-09, Amendment 39-21906), which supersedes AD 2021-11-15 (FR doc 2021-11960). The question date precedes the 2022-03-15 effective date, so no action can be required on the question date; the timing above applies from the effective date.
- **Note:** V2533-A5 is in the supported scope and is a high-thrust model per the preamble, so paragraphs (g)(1) and (g)(2) govern; the low-thrust timing in (g)(3) and (g)(4) does not apply to this engine.
- **Note:** Both installed disk part numbers match the directive's listed part numbers (2A5001 and 2A4802). Serial-number eligibility could not be checked because the Appendix A tables are not supplied, so the listed serial number fields are null and the installed serial numbers are unverified.
- **Note:** The due point is the later of the Figure 1 time and 10 flight cycles after 2022-03-15. Without Figure 1 and the current engine flight-cycle count, latest_engine_flight_cycles and component_cycles_remaining are null.
- **Note:** The 3,200-flight-cycle limit in superseded AD 2021-11-15 is not the limit in 2022-02574 and was not used for any deadline here.
- **Note:** AD 2021-11-15 (FR doc 2021-11960) remains in force on the question date until 2022-02574 takes effect. Its requirements for this engine were not screened and need separate review; its inputs (engine flight-cycle count, shop visit history, serial-number listings) are absent from this record.
- **Note:** The record has no ad_records or amoc_claims entries, so no operator-recorded AD status or AMOC claim was supplied or relied upon. The events list is empty, which does not show that no engine shop visit occurred.
- **Note:** The NMSB procedures (paragraphs 6 to 8) and the Appendix A tables were not supplied; this screen relies only on the directive text and the engine record.
- **Note:** The record is synthetic (SYN- identifiers). This is a screening aid only, not a determination of AD status, airworthiness, or return-to-service approval for the engine or either disk.
- **Unresolved locator:** 2022-02574 preamble The Amendment, item 2.a
- **Unresolved locator:** 2022-02574 (g)(1) Figure 1 to paragraph (g)(1), image not included in supplied text

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** The directive is in force and V2530-A5 is a supported model with P/N 2A5001 and P/N 2A4802 disks installed, but applicability turns on whether serials SYN-DISK1-0021 and SYN-DISK2-0021 appear in Appendix A of the referenced NMSBs, which were not supplied, and the Figure 1 compliance times are not reproduced, so the screen needs review rather than a determination.
- **Stated timing:** If either serial is listed in Appendix A, the USI of that disk is due at the Figure 1 to paragraph (g)(1) compliance time or within 10 flight cycles after the 2022-03-15 effective date, whichever occurs later; Figure 1 is not in the supplied text, so no due date or cycle limit can be computed.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (listed HPT 1st-stage disk serial numbers) is not in the supplied text. Whether serial SYN-DISK1-0021 is listed decides whether the 1st-stage disk falls within paragraph (c)(1) and the paragraph (g)(1) USI.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (listed HPT 2nd-stage disk serial numbers) is not in the supplied text. Whether serial SYN-DISK2-0021 is listed decides whether the 2nd-stage disk falls within paragraph (c)(2) and the paragraph (g)(2) USI.
- **Missing fact:** Appendix A tables of IAE NMSB V2500-E5-72-0015 Rev 1, which paragraph (c) also cites as a source of listed serial numbers, are not in the supplied text; they are needed to confirm whether either serial appears there.
- **Missing fact:** Figure 1 to paragraph (g)(1), which gives the compliance times for V2527E-A5, V2527M-A5, V2528-D5, V2530-A5 and V2533-A5 engines, is an image not reproduced in the supplied text. Without it no due date or cycle limit can be set under paragraph (g)(1) or (g)(2).
- **Missing fact:** No flight-cycle accumulation is recorded for the 1st-stage disk. The count on the basis Figure 1 uses is needed for any disk-based cycle limit and for component_cycles_remaining.
- **Missing fact:** No flight-cycle accumulation is recorded for the 2nd-stage disk. The count on the basis Figure 1 uses is needed for any disk-based cycle limit and for component_cycles_remaining.
- **Missing fact:** The engine flight-cycle counter at the question date is not recorded. It is needed to test the Figure 1 limit and to state latest_engine_flight_cycles.
- **Missing fact:** The engine flight-cycle counter at the 2022-03-15 effective date is not recorded. It is needed to convert the 10-cycles-after-effective-date alternative into a cycle count.
- **Missing fact:** The events list is empty. The record does not show whether an engine shop visit under paragraph (h)(1) or a USI of either disk has occurred since 2022-03-15; absence from the record is not evidence that none occurred.
- **Missing fact:** No operator AD status entry for AD 2022-02-09 is in the record, so the operator's recorded status, any claimed USI, and any credit claim are unknown.
- **Note:** Screening aid only. This is not a compliance determination and does not state that either disk or the engine is compliant, noncompliant, safe, airworthy, or approved for return to service.
- **Note:** Both installed disks match a listed part number (2A5001 for the 1st-stage disk, 2A4802 for the 2nd-stage disk). That is a part-number match only: paragraph (c) requires the serial to be listed in an NMSB Appendix A table, and those tables are not in the supplied text. Under the and/or wording of (c), a listing of either serial brings the engine within the directive, so both serials must be checked. The serials carry the SYN- synthetic prefix and are treated as given.
- **Note:** V2530-A5 is a supported model that the preamble categorizes as high-thrust, so paragraphs (g)(1) and (g)(2) with Figure 1 timing are the operative requirements; paragraphs (g)(3) and (g)(4) cover low-thrust models only. Disk thrust-rating history therefore does not change this engine's analysis.
- **Note:** Figure 1 to paragraph (g)(1) and the NMSB Accomplishment Instructions (paragraphs 6 to 8, including the pass criteria) are not in the supplied text. The record has no engine or disk flight-cycle counts, so latest_engine_flight_cycles and component_cycles_remaining are null. The directive has been in force since 2022-03-15, so once Figure 1 and the counts are supplied the reviewer should check whether the Figure 1 limit has already been reached for any listed disk.
- **Note:** The record has events as an empty list and no ad_records or amoc_claims entries. These absences do not show that no engine shop visit or USI has occurred since the effective date, and they do not show that a USI is outstanding. Operator shop-visit and USI history is needed before any timing conclusion.
- **Note:** Superseded thresholds: AD 2021-11-15 (document 2021-11960) required, for high-thrust engines, the USI at the next engine shop visit after 2021-07-13 or before 3,200 FCs from that date, whichever occurred first. AD 2022-02-09 replaces AD 2021-11-15 under its paragraph (b), so those thresholds are not used in this screen.
- **Note:** Credit: paragraph (i) grants credit only for USIs under paragraphs (g)(5) and (g)(6) and for (g)(7) replacements, when done before 2022-03-15 under IAE NMSB V2500-E5-72-0015 original issue. No credit paragraph covers an earlier V2530-A5 disk USI performed under AD 2021-11-15 or NMSB V2500-ENG-72-0713, so any earlier USI needs reviewer judgment.
- **Note:** Paragraph (c) accepts a listed serial from either NMSB V2500-ENG-72-0713 Rev 1 or V2500-E5-72-0015 Rev 1, but the V2530-A5 requirements in (g)(1) and (g)(2) refer only to the ENG-72-0713 Rev 1 tables, while the E5 NMSB is tied to V2531-E5 engines in (g)(5) and (g)(6). If a disk serial appears only in the E5 tables, the reviewer must resolve how that applies to V2530-A5.
- **Note:** No later amending or superseding document for AD 2022-02-09 was supplied, so authority_state is in_force based on the supplied documents and the 2022-03-15 effective date.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2022-02574 preamble Background: high-thrust and low-thrust model categorization
- **Unresolved locator:** 2022-02574 (g)(1) Figure 1 to paragraph (g)(1), not reproduced; Note 1 to paragraph (g)(1)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2021-11-51 (Federal Register 2021-14268) is in force and applies to this V2533-A5 engine because its installed HPT 1st-stage disk (P/N 2A5001, S/N PKLBSH1829) is a listed disk. The record shows no ultrasonic inspection (USI) of that disk, so the USI is due within 10 flight cycles after the July 19, 2021 effective date, which is engine flight cycle 33010 (6 cycles remain at the 33004 reading on 2021-07-20).
- **Stated timing:** Within 10 flight cycles after the July 19, 2021 effective date; on the record's counts that is engine flight cycle 33010 (33000 on 2021-07-19 plus 10), with 6 cycles left at the 33004 reading on 2021-07-20.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** Table 1 to paragraph (g)(1) is an image that is not included in the supplied text. The (g)(1) USI duty covers installed 1st-stage disks listed there. The (c)(1) applicability text includes S/N PKLBSH1829, so the duty is treated as established on the text, but the table should be checked to confirm this disk is listed.
- **Missing fact:** Table 2 to paragraph (g)(2) is an image that is not included in the supplied text. It is needed to confirm that the installed HPT 2nd-stage disk (P/N 2A4802, S/N SYN-DISK2-0022) is not listed there. The recorded S/N is not among the (c)(2) serial numbers, so no (g)(2) duty is shown on this record.
- **Missing fact:** No ad_records entry for AD 2021-11-51 is in the record, so the operator's recorded status for this AD and any claim that the USI was already accomplished, including under emergency AD 2021-11-51, are unknown. Any such claim would need checking. The absence is not evidence that the USI was or was not done.
- **Missing fact:** The events list is empty, so no USI event for HPT 1st-stage disk S/N PKLBSH1829 is recorded. If a USI was performed, its date, engine flight-cycle count, and pass or fail result are needed to decide whether the (g)(1) duty is already met and whether (g)(3) removal applies.
- **Missing fact:** Emergency AD 2021-11-51 (issued May 21, 2021, effective with actual notice, and stated to contain this amendment's requirements) was not supplied. Its terms, including any earlier USI deadline, cannot be checked from the supplied materials and are not reflected in the deadline computed here.
- **Missing fact:** The reading is dated but not timed. It is used as the engine flight-cycle count at the July 19, 2021 effective date, and the 10-cycle deadline is counted from it. The time-of-day and counter basis should be confirmed.
- **Note:** Screening aid only, not a compliance determination. Synthetic (SYN-) identifiers are used as recorded.
- **Note:** Applicability rests on the 1st-stage disk alone: P/N 2A5001 with S/N PKLBSH1829 is listed in (c)(1), and V2533-A5 is a listed model in (c).
- **Note:** The installed HPT 2nd-stage disk (P/N 2A4802, S/N SYN-DISK2-0022) carries a listed part number, but its recorded serial number is not among the (c)(2) serial numbers, so it is not a matched part on this record.
- **Note:** Deadline arithmetic: the AD counts 10 flight cycles from the July 19, 2021 effective date. The 2021-07-19 reading of 33000 is the baseline, giving 33010. The 2021-07-20 reading of 33004 is the snapshot, not the baseline; 4 cycles were logged after the 33000 reading and 6 remain. Counting from the snapshot would overstate the deadline as 33014.
- **Note:** The AD text says flight cycles; this screen uses the engine flight-cycle counter in the record. Confirm that this counter is the right basis.
- **Note:** The record has no events, no ad_records entries, and no amoc_claims. Nothing in it shows the USI as performed, and no AMOC is asserted.
- **Note:** The AD is interim action and says the root cause was still under investigation, so further rulemaking may follow. Comments were due August 16, 2021. No correction, proposal, or superseding document appears in the supplied materials as of 2021-07-20.
- **Note:** The USI result is unknown. If the 1st-stage disk does not pass, paragraph (g)(3) requires removal before further flight and replacement with a part eligible for installation under (h); the NMSB Appendix A tables that define eligibility were not supplied.
- **Note:** component_cycles_remaining is null because the AD sets no cycle life limit for either disk; the cycle figure that governs is the USI deadline in latest_engine_flight_cycles. The AD also sets no recurring inspection interval in the supplied text.
- **Note:** The NMSB service bulletins and the image-only Tables 1 and 2 were not supplied, so the USI procedure itself was not reviewed.
- **Expected missing fact (judge on meaning):** operator date of actual notice of Emergency AD 2021-11-51
- **Expected missing fact (judge on meaning):** table 1 to paragraph (g)(1) content (image-only; transcription decided in E3)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 accomplishment instructions (unavailable incorporated material)
- **Unresolved locator:** 2021-14268 (g)(1) Table 1 to paragraph (g)(1) (image not included in supplied text)
- **Unresolved locator:** 2021-14268 (g)(2) Table 2 to paragraph (g)(2) (image not included in supplied text)

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-022/2021-11960: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-023/2025-18469: One engine under three directives at once

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2527M-A5 engine is within the directive's applicability because its recorded 3rd stage HPC rotor blade set carries P/N 6A8688, and the directive has been in force since its 2026-09-24 effective date. Full-set replacement with parts eligible for installation is due at the next engine shop visit after that date where the blade is exposed; the record lists no engine shop visit, so nothing is triggered on the current record and the requirement awaits that future event.
- **Stated timing:** Due at the next engine shop visit (induction of the engine into the shop for maintenance) after the 2026-09-24 effective date where the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no fixed calendar date or flight-cycle limit applies, and no such visit is recorded as of 2026-10-06.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The events list has no engine shop visit entry at any date, so the record cannot confirm whether the engine was inducted into the shop for maintenance on or after 2026-09-24 or whether any 3rd stage HPC rotor blade was removed from the HPC stage 3 to 8 drum at such a visit. If a post-effective-date visit with blade exposure occurred, full-set replacement would already be due and this status would change to action required.
- **Missing fact:** The blade set has no installation date, so the record cannot show whether the set was fitted at a shop visit on or after 2026-09-24, which bears on whether a qualifying shop visit has already occurred.
- **Note:** Screening aid only; this is not a compliance determination and says nothing about airworthiness or return to service.
- **Note:** V2527M-A5 is on the supported model list. The record is marked synthetic; identifiers are used as given.
- **Note:** Authority: the final rule (FR 2026-16954, AD 2026-17-03) is effective 2026-09-24, and the correction (FR 2026-18423, published 2026-09-10) leaves that date unchanged, so the directive is in force on 2026-10-06.
- **Note:** The correction restores the word 'blade' in paragraph (g); the original text read 'rotor is exposed'. The trigger is exposure of the 3rd stage HPC rotor blade under either wording.
- **Note:** Applicability rests on the set-level P/N 6A8688. The directive matches by blade P/N only and the set serial is not tracked; individual blade P/N and serial records were not supplied. They are not needed to find applicability here but would be needed to document a full-set replacement at a future exposure event.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802) and HPT 1st-stage hub (P/N 2A5001) are not listed in this directive and were not used.
- **Note:** Cycle counter: 20000 cycles on 2025-10-29 and 22500 on 2026-10-06. The directive has no cycle limit, so latest_engine_flight_cycles and component_cycles_remaining are null; record the engine cycle count at any qualifying shop visit.
- **Note:** The 2025-12-01 maintenance program revision (Revision 48, incorporating table 1 of AD 2025-17-16) is not an induction into the shop under paragraph (h)(3) and concerns another AD that was not supplied, so it does not trigger this directive's requirement.
- **Note:** No ad_records or amoc_claims were supplied, so no operator AD status or AMOC claim was checked or relied on. The absence of any shop-visit entry is not evidence that the blade set is unaffected; it only means no triggering event is recorded.
- **Note:** Reading check: the natural reading attaches the obligation to the first engine shop visit after the effective date where the blade is exposed. A reading that ties it to the first visit of any kind would leave the obligation unattached if that visit had no exposure. Neither reading gives an integer cycle deadline, so alternative_readings is empty.
- **Note:** The November 2025 NPRM (FR 2025-20088) proposed a trigger at any blade exposure after the effective date. The final rule replaced that with an engine shop visit trigger, and this screen follows the final rule as corrected.
- **Note:** The preamble says replacement under the IAE AG service bulletin demonstrates compliance, but the AD does not reference that bulletin and its text was not supplied, so this screen does not evaluate it.
- **Note:** If the engine is inducted on or after 2026-09-24 and any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum, re-screen at that event; the directive then requires full-set replacement with parts eligible for installation at that visit.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2528-D5 engine is within the applicability of in-force AD 2025-19-13 (Federal Register 2025-18469, effective 2025-10-29), but neither recorded hub's P/N and S/N pair is listed in Table 1 to paragraph (g), so the supplied record triggers no required removal. The 2nd-stage hub's serial number PKLBST5011 appears in Table 1 only under HPT 1st-stage hub P/N 2A5001, so that hub's recorded P/N should be verified.
- **Missing fact:** The recorded S/N PKLBST5011 appears in Table 1 only under P/N 2A5001 (HPT 1st-stage hub, removal limit 5,500 cycles since new), not under the 2A4802 rows. The pair as recorded is not listed, so no removal is triggered on this record; but if the recorded P/N or S/N is wrong and the hub is P/N 2A5001 with this S/N, it would be a listed part and the result would change, so the pair should be confirmed from the hub's documentation.
- **Note:** Screening aid only; not a compliance determination and not a return-to-service decision.
- **Note:** Pairing rule: paragraph (g) Table 1 and definition (i)(1) identify each hub by P/N and S/N together. The 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0024) has a listed P/N, but its S/N is not among the four 2A5001 rows, so it is not a listed part on this record.
- **Note:** The 2nd-stage hub (P/N 2A4802, S/N PKLBST5011) has a listed P/N, but its S/N is not among the four 2A4802 rows; PKLBST5011 is listed only under P/N 2A5001. Matching on S/N alone does not follow the table's P/N and S/N columns, so it is not treated as a match.
- **Note:** Verification: if the hub's recorded P/N is wrong and the hub is P/N 2A5001 with this S/N, it would be a listed part with a 5,500-cycle removal limit and 2,500 cycles remaining at 3,000 cycles since new. Removal would then be due at the next engine shop visit after 2025-10-29 before exceeding 5,500 cycles, or within 100 flight cycles of 2025-10-29, whichever occurs later. No integer engine-cycle deadline can be computed from the record, and component_cycles_remaining and latest_engine_flight_cycles are null because no listed limit applies on the record as entered.
- **Note:** The record has no engine flight-cycle counter, no events (so no shop visit or hub installation dates), and no ad_records or amoc_claims. These do not change the no-action result on the recorded pairs, but the flight-cycle counter and installation history would be needed to date any removal or assess paragraph (h) if a listed hub is confirmed.
- **Note:** The NPRM 2025-10764 (published 2025-06-13) has the same applicability and Table 1, but it is a proposed rule and is not relied on; final rule 2025-18469 is the operative text.
- **Note:** Identifiers beginning with SYN- are synthetic per the record conventions, and the record is flagged synthetic.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub rows (P/N 2A5001) and HPT 2nd-stage hub rows (P/N 2A4802)

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model recorded as CFM56-5B4/3 is not one of the IAE V2500 models this screen supports, so no applicability determination is made against AD 2025-17-16 (Federal Register document 2025-17066). The final rule took effect October 10, 2025 and is in force on the 2026-10-06 question date, but it is not screened against this engine.
- **Note:** The record is marked synthetic (synthetic: true) and its identifiers use the SYN- prefix; the outcome rests only on the engine_model field, and no installed components or events are recorded.
- **Note:** No compliance status is stated or implied. No applicability determination is made for this engine under this AD because the model is outside the supported scope.
- **Note:** If the engine_model entry is a data-entry error and the engine is in fact one of the listed IAE V2500 models, the screen should be rerun with the corrected model; this answer does not assume that.
- **Note:** NPRM 2024-26092 is the proposal that became final rule 2025-17066 and was not relied on. The operator's air_carrier_operation entry does not change the scope outcome.
- **Note:** The directive's 90-day action window after its October 10, 2025 effective date is not computed for this engine, so the timing and cycle fields are null.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-027: Listed hub near its limit, with an unverified AMOC claimed to extend it

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2524-A5 is within the AD, and its installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 is listed in table 1, so the paragraph (g) removal applies at the next engine shop visit and before that hub exceeds 4,000 cycles since new (about engine flight cycle 11,000). The operator's N/A entry rests on 'no affected hubs installed', which the installed-component record contradicts, so it does not settle the screen.
- **Stated timing:** Due at the next engine shop visit after 2025-10-29 and before the hub exceeds 4,000 cycles since new, which is engine flight cycle 11,000 if the hub accrues cycles one-for-one with the engine as the readings show; the 100-flight-cycle point (engine flight cycle 8,100) has already passed but, under the 'whichever occurs later' wording, it is a floor and sets no earlier deadline.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The operator's N/A entry rests on 'no affected hubs installed', which the installed-component record contradicts because the HPT 2nd-stage hub matches a listed P/N and S/N; the basis must be reviewed and the entry cannot be relied on as evidence.
- **Missing fact:** The 1,400 cycles-since-new value is undated; it is taken as current at the 2026-02-10 snapshot (consistent with 1,000 on 2025-10-29 plus 400 engine cycles) and sets the 2,600 cycles remaining, so a dated reading should confirm it.
- **Missing fact:** No engine shop visit after 2025-10-29 is recorded and the events list is empty, which does not show that none occurred. Confirm whether any induction meeting the paragraph (i)(2) definition has occurred since 2025-10-29 and, if so, whether the hub was removed at it.
- **Missing fact:** The planned date and engine flight cycles of the next engine shop visit are not in the record. Removal must occur at that visit and before engine flight cycle 11,000, so the planned induction timing is needed to confirm the removal can be done in time.
- **Missing fact:** The identity (P/N and S/N) of the replacement HPT 2nd-stage hub is not in the record. The replacement must be a part eligible for installation, meaning a hub whose P/N and S/N are not listed in table 1 (paragraph (i)(1)).
- **Note:** Screening aid only, not a compliance determination. The final rule (FR document 2025-18469, AD 2025-19-13) controls; the NPRM 2025-10764 is the proposal and was not relied on.
- **Note:** Model V2524-A5 is on the supported scope list and within the paragraph (c) applicability; the rule was effective 2025-10-29 and so is in force on the 2026-02-10 question date.
- **Note:** Timing: the engine read 8,000 flight cycles on 2025-10-29, so the 100-flight-cycle point is 8,100; the engine read 8,400 on 2026-02-10, after that point. Because the AD says whichever occurs later, the next-shop-visit prong governs, bounded by the hub reaching 4,000 cycles since new.
- **Note:** Arithmetic: 4,000 minus 1,400 gives 2,600 cycles remaining; 8,400 plus 2,600 gives engine flight cycle 11,000, assuming one-for-one accrual, which the readings support (hub 1,000 to 1,400 versus engine 8,000 to 8,400).
- **Note:** Using the 2025-10-29 hub reading (1,000 at 8,000 engine cycles) gives the same outer bound of 11,000 engine flight cycles (3,000 remaining at that date), so the result does not depend on which reading is used.
- **Note:** 'Before exceeding' is read as the hub's cycles since new not going above 4,000; the last engine flight cycle at which it is still at 4,000 or below is 11,000.
- **Note:** The installed HPT 1st-stage hub, P/N 2A5001 S/N SYN-HUB1-0028, is not matched: table 1 lists four S/Ns for that P/N and this S/N is not among them. This is a table-match result only, not a finding on that hub.
- **Note:** No amoc_claims are recorded for this AD.
- **Note:** The 2nd-stage hub was installed 2025-06-03, before the effective date, so that installation is outside the paragraph (h) period; paragraph (h) still bars any later installation of a listed hub in any engine.
- **Note:** Per the FAA preamble, removing affected hubs does not end the AD's applicability because of the installation prohibition, and the FAA declined to add a terminating action; treat the AD as continuing to apply to this engine after removal.
- **Note:** Reviewer: confirm the next shop visit plan, whether any unrecorded shop visit has occurred since 2025-10-29, the dated hub cycles-since-new reading, and the replacement hub's P/N and S/N.
- **Unresolved locator:** 2025-18469 (g) Required Actions, first paragraph
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub row 2A4802 / PKLBST5005 / 4,000
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub rows for P/N 2A5001

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)
