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
- **Summary:** The engine is a V2527-A5, a model within the directive's applicability, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) is listed in Table 1 of AD 2025-19-13 (Federal Register 2025-18469, in force since 2025-10-29), so removal at the next engine shop visit before the hub exceeds its 5,500-cycle limit is required (engine flight cycle 45,050 on the record's readings). The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0001) is not an affected part on this record because its S/N is not listed in Table 1.
- **Stated timing:** At the next engine shop visit after 2025-10-29 that occurs before the hub exceeds its 5,500 cycles-since-new limit; on the record's 2026-09-26 readings that limit is reached at engine flight cycle 45,050, 2,400 cycles after the snapshot. The 100-flight-cycle clause (engine flight cycle 41,300) is the earlier date, had already passed at the snapshot, and does not set the deadline under the directive's 'whichever occurs later' wording.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.
- **Missing fact:** The 3,100 cycles-since-new value for the HPT 1st-stage hub has no date. It is read as current at the 2026-09-26 snapshot because it is 1,450 above the dated 1,650 reading at 2025-10-29, the same 1,450 increase as engine flight cycles, but the record should confirm the date because the 2,400 remaining cycles and the 45,050 engine-cycle point depend on it.
- **Note:** Screening aid only; this is not a compliance determination.
- **Note:** Directive relied on: AD 2025-19-13, Federal Register 2025-18469 (final rule, effective 2025-10-29). The NPRM 2025-10764 was not relied on for any requirement.
- **Note:** Cycle arithmetic: the 100-flight-cycle point is the engine counter on 2025-10-29 (41,200) plus 100, which is 41,300. The limit point is the 2026-09-26 engine counter (42,650) plus the 2,400 remaining hub cycles (5,500 minus 3,100), which is 45,050. This assumes the hub accrues one cycle per engine flight cycle while installed; the record's two readings support this because both rose by 1,450 between 2025-10-29 and 2026-09-26.
- **Note:** The dated 1,650 hub reading at 2025-10-29 is superseded by the later 3,100 value; using it as the current count would overstate remaining cycles at 3,850, although the engine-cycle point would still be 45,050 if the two readings are consistent.
- **Note:** No engine shop visit is recorded (events is empty), so the next shop visit is treated as still ahead. Whether a future event is an engine shop visit depends on paragraph (i)(2): transport-only flange separation and engine removal for field maintenance at a facility in lieu of on-wing work are excluded. If a shop visit occurred that the record does not show, the reviewer should check whether the hub was removed at that visit.
- **Note:** The installed 1st-stage hub was installed 2023-04-18, before the effective date, so the installation prohibition in paragraph (h) was not triggered by that installation; reinstalling this listed hub in any engine after 2025-10-29 would be prohibited.
- **Note:** The installed 2nd-stage hub has a listed P/N but an S/N not in Table 1; on this record it is not an affected part, and its undated cycles_since_new value does not change the result.
- **Note:** No ad_records or amoc_claims were supplied, so no operator AD status entry or AMOC claim was checked; neither is needed to reach this screen. If an AMOC is used, paragraph (j)(2) requires notice to the principal inspector before use.
- **Note:** Any replacement hub must be a part eligible for installation, meaning its P/N and S/N are not listed in Table 1 (paragraph (i)(1)).
- **Unresolved locator:** 2025-18469 (g) Required Actions text and Table 1 to Paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBST5011 / 5,500
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 2nd-stage hub rows for P/N 2A4802

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-19-13 (Federal Register 2025-18469, effective 2025-10-29) is in force on the question date and covers V2533-A5 engines, so this engine is within its applicability. Neither recorded installed hub's P/N and S/N pair appears in Table 1 to paragraph (g) (the 1st-stage hub's S/N PKLBST5012 is not the listed PKLBST5011, and the 2nd-stage hub's S/N SYN-HUB2-0002 is not listed), so no removal is triggered on this record.
- **Note:** Only Federal Register document 2025-18469 (final rule, AD 2025-19-13, effective 2025-10-29) was relied on; it was in force on 2026-09-26. The NPRM 2025-10764 is a proposal and was not relied on.
- **Note:** Table 1 entries match on P/N and S/N together. Both recorded hubs carry a P/N that appears in Table 1 (2A5001 for the 1st-stage hub, 2A4802 for the 2nd-stage hub), but neither recorded S/N is listed with that P/N, so matched_parts is empty.
- **Note:** The 1st-stage hub's recorded S/N PKLBST5012 differs from listed PKLBST5011 only in its last character. This screen uses the record as given; if the hub's identification confirms PKLBST5011, the hub would be a Table 1 part with a 5,500-cycle removal limit (1,300 cycles remaining at 4,200 cycles since new) and this result would need to be redone.
- **Note:** Do not apply Table 1 cycle limits by P/N alone. The 2A4802 limits attach to specific S/Ns; a P/N-only comparison at 4,200 cycles would wrongly show the 2nd-stage hub past its 3,900- and 4,000-cycle limits and the 1st-stage hub past its 100-cycle limit.
- **Note:** Applicability follows the engine model list in paragraph (c), not hub serial numbers, so the V2533-A5 engine is within the AD even though no Table 1 hub is recorded.
- **Note:** The events list is empty, so no engine shop visit is recorded. The paragraph (g) shop-visit trigger matters only if a Table 1 hub is installed; none is recorded, so the empty list does not change this result.
- **Note:** The record has no ad_records or amoc_claims entries, so no operator AD status or alternative method was evaluated; neither is needed for this Table 1 screen.
- **Note:** This is a screening aid only; it does not settle the status of either hub, so verify the installed P/N and S/N against the hub identification before relying on this result.
- **Note:** Engine serial SYN-V2500-0002 and hub serial SYN-HUB2-0002 are synthetic identifiers.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g): HPT 1st-stage hub rows for P/N 2A5001 and HPT 2nd-stage hub rows for P/N 2A4802

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2025-19-13 (Federal Register document 2025-18469, effective 2025-10-29) applies to this V2524-A5 engine and is in force on the question date, but the record cannot settle whether the installed HPT 1st-stage hub (P/N 2A5001, with unknown serial number and unknown cycles since new) is one of the table 1 listed hubs. The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003) does not match any table 1 P/N and S/N pair in the record, so no table 1 removal trigger is identified for it.
- **Stated timing:** Only if the installed HPT 1st-stage hub is a table 1 listed hub: remove and replace it at the next engine shop visit after 2025-10-29 before exceeding its removal cycle limit (100, 4,800, 5,500 or 6,200 cycles since new, depending on its serial number), or within 100 flight cycles of 2025-10-29, whichever occurs later; the record does not allow a date or engine flight-cycle count to be computed.
- **Missing fact:** Serial number is unknown for the installed HPT 1st-stage hub, which has P/N 2A5001 (listed in table 1). Only a P/N and S/N pair identifies a listed hub, and the serial number sets both whether removal is required and which removal cycle limit applies (PKLBSK9287 = 100, PKLBSS9200 = 4,800, PKLBST5011 = 5,500, PKLBST7489 = 6,200 cycles since new). An unknown serial number is not evidence in either direction.
- **Missing fact:** Cycles since new are unknown for the installed HPT 1st-stage hub, so cycles remaining before its removal cycle limit, and whether a limit has already been exceeded, cannot be computed.
- **Missing fact:** The engine record has no engine flight-cycle counter. The count at the snapshot date is needed to convert a hub's remaining cycles into the engine flight-cycle count by which removal must be done.
- **Missing fact:** The engine flight-cycle count on the effective date is needed to compute the 100-flight-cycle window that runs from 2025-10-29, one of the two removal triggers in paragraph (g).
- **Missing fact:** The events list is empty, so the record does not show whether an engine shop visit has occurred since 2025-10-29 or whether such an event meets the engine shop visit definition in paragraph (i)(2). The next-engine-shop-visit trigger in paragraph (g) depends on this.
- **Note:** Synthetic record. The question date 2026-09-26 is after the 2025-10-29 effective date of final rule 2025-18469, so the rule is in force; NPRM 2025-10764 preceded the final rule and is not relied on.
- **Note:** Table 1 entries for P/N 2A5001 (HPT 1st-stage hub): PKLBSK9287 (100 cycles), PKLBSS9200 (4,800), PKLBST5011 (5,500), PKLBST7489 (6,200). Entries for P/N 2A4802 (HPT 2nd-stage hub): PKLBST5005 (4,000), PKLBSS9840 (3,900), PKLBSS0301 (5,000), PKLBSR2100 (6,000).
- **Note:** The installed HPT 2nd-stage hub (S/N SYN-HUB2-0003, 5,100 cycles since new) is not compared with any limit because its S/N is not among the table 1 entries for P/N 2A4802.
- **Note:** Timing reading used: removal is due at the later of the next engine shop visit and 100 flight cycles after 2025-10-29, and in all cases before the hub exceeds its removal cycle limit. If the cycle limit would be reached first, the cap appears to control; confirm this reading before relying on it.
- **Note:** Installation history after 2025-10-29 is not in the record, so the paragraph (h) installation prohibition cannot be checked against it.
- **Note:** The record has no ad_records or amoc_claims entries, so no operator-asserted AD status or AMOC claim was checked.
- **Note:** Per the FAA response to comments in the preamble, removing affected hubs does not end the AD's applicability because of the installation prohibition in paragraph (h).
- **Note:** Screening aid only; this is not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Required Actions; Table 1 to Paragraph (g), HPT 1st-stage hub P/N 2A5001 rows and HPT 2nd-stage hub P/N 2A4802 rows

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model PW1133G-JM is not an IAE V2500 model supported by this screen, so no applicability determination or action status is given for AD 2025-19-13 (Federal Register document 2025-18469). The directive is in force on the question date because it became effective October 29, 2025, but no screening of this engine against its requirements was performed.
- **Note:** Recorded engine model PW1133G-JM is outside the supported scope of this screen, which covers only the listed IAE V2500 models; no determination of applicability, AD status, or return-to-service status is made.
- **Note:** The record has no ad_records or amoc_claims entries for this AD, and installed_components and events are both empty; these empty values are not evidence that any HPT 1st-stage or 2nd-stage hub is absent or unaffected, and no Table 1 part-number or serial-number screening was performed.
- **Note:** If the model designation is a record error, re-screen against the corrected engine model and the installed hub records before relying on any outcome.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive applies to this V2527E-A5 engine and is in force on 2025-11-12. The installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSS9840) is a listed part that must be removed and replaced by engine flight cycle 18100, the later of the 2025-11-12 shop visit and 100 flight cycles after 2025-10-29; the record still lists it as installed at 18040 cycles, and the HPT 1st-stage hub (S/N SYN-HUB1-0005) is not a listed serial number.
- **Stated timing:** Remove and replace the listed HPT 2nd-stage hub at the next engine shop visit after 2025-10-29 (before it exceeds 3,900 cycles since new) or within 100 flight cycles of 2025-10-29, whichever is later; the 2025-11-12 induction at 18040 cycles is recorded as qualifying, so the later prong sets the due point at engine flight cycle 18100, 60 cycles after the 2025-11-12 reading.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** Shop-visit work records for the 2025-11-12 induction showing whether serial PKLBSS9840 was removed and replaced, with the date and engine flight cycle. The engine record still lists the hub as installed and has no removal or replacement event, so whether the action is already done before 18100 cannot be shown from the record.
- **Missing fact:** The yes for AD 2025-19-13 is the operator's assertion. The event detail (inducted for maintenance separating major mating flanges) is consistent with the shop-visit definition but does not say which flanges were separated or rule out an excepted situation. The 18100 due point assumes this induction is the next engine shop visit; if it is not, the due point moves to a later qualifying shop visit that the record does not show.
- **Missing fact:** The 1040 cycles-since-new value has no date; the only dated reading is 1000 at 2025-10-29. The 40-cycle rise matches the 40 engine cycles recorded between the two dated engine readings, so 1040 is used as the 2025-11-12 value. A dated reading would confirm the 2,860 cycles remaining.
- **Note:** Screening aid only: this is not a compliance determination, not an operator AD status record, and not a return-to-service decision.
- **Note:** Model V2527E-A5 is within the supported scope. Final rule 2025-18469 (AD 2025-19-13) is effective 2025-10-29 and is in force on 2025-11-12. The June 2025 NPRM (2025-10764) is a proposal and was not relied on.
- **Note:** Due point: engine flight cycles were 18000 on 2025-10-29, so 100 flight cycles later is 18100. The later of that and the 2025-11-12 shop visit at 18040 is 18100, leaving 60 flight cycles after the 18040 reading. The 100-cycle prong is read on the engine flight-cycle counter.
- **Note:** Remaining cycles: 3,900 minus 1,040 gives 2,860 on the listed HPT 2nd-stage hub, the only affected part on this record.
- **Note:** HPT 1st-stage hub P/N 2A5001 S/N SYN-HUB1-0005 does not match any of the four serial numbers listed for P/N 2A5001 in table 1, so it is not treated as affected and is not in matched_parts.
- **Note:** The listed hub was installed 2022-08-02, before the effective date, so no post-effective-date installation of a listed hub is recorded.
- **Note:** If the 2025-11-12 induction were not a qualifying engine shop visit, the due point would move to the next qualifying shop visit, which the record does not show; that visit would have to occur before the hub exceeds 3,900 cycles since new, about engine flight cycle 20,900 if the hub tracks engine cycles. That bound cannot be fixed from this record.
- **Note:** The engine record has no ad_records or amoc_claims entries for this AD, so no AMOC is claimed or assessed.
- **Note:** The qualifies flag and the shop-visit event are operator assertions checked against the definition; neither shows that removal has occurred, and the record still lists the hub as installed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row, P/N 2A4802, S/N PKLBSS9840, removal cycle limit 3,900
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub rows, P/N 2A5001

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (Federal Register 2025-18469, in force since its 2025-10-29 effective date) applies to this V2531-E5 engine, and both installed hubs match Table 1: the 1st-stage hub PKLBSS9200 has 500 cycles left to its 4,800-cycle limit and the 2nd-stage hub PKLBST5005 has 1,700 left to its 4,000-cycle limit. Removal is required at the next engine shop visit, which must occur no later than engine flight cycle 30800; the 100-flight-cycle time (cycle 30100) has passed, but under the whichever-occurs-later wording the shop visit controls, and no shop visit is recorded since the effective date.
- **Stated timing:** Due at the next engine shop visit after 2025-10-29, and that visit must occur no later than the point at which hub PKLBSS9200 would exceed 4,800 cycles since new (engine flight cycle 30800, about 500 cycles after the 2025-12-01 snapshot at cycle 30300). The 100-flight-cycle time (cycle 30100) already passed and, because the AD applies whichever occurs later, does not set an earlier date. Hub PKLBST5005's own limit (about cycle 32000) is later and falls under the same shop-visit trigger.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** No engine shop visit is recorded after the 2025-10-29 effective date (events is empty), and no future shop visit is recorded. The record cannot show whether a shop visit has already occurred, which would have triggered removal at that visit, or whether a future induction would meet the (i)(2) definition (separation of major mating H-P engine flanges; transport-only separation and off-wing field maintenance removal are excluded). This decides whether the removal trigger has been reached and when the next one falls.
- **Missing fact:** The current 4,300 cycles-since-new value is undated; the only dated reading is 4,000 on 2025-10-29. The 500-cycle figure and cycle 30800 assume 4,300 is the count at the 2025-12-01 snapshot and that the hub accrues one cycle per engine flight cycle, as the matching 300-cycle change since 2025-10-29 suggests. A dated reading would confirm both.
- **Missing fact:** The current 2,300 cycles-since-new value is undated; the only dated reading is 2,000 on 2025-10-29. It drives the 1,700-cycle figure for hub PKLBST5005, which does not set the engine's controlling date but should be confirmed.
- **Note:** Screening aid only: this is not a compliance determination, a return-to-service decision, or an operator AD status record.
- **Note:** Engine model V2531-E5 is on the supported list and in the AD's applicability paragraph (c), so no scope question arises.
- **Note:** Figures are as of the 2025-12-01 snapshot (engine cycle 30300). Hub PKLBSS9200 is at 4,300 of 4,800 cycles since new (500 left); hub PKLBST5005 is at 2,300 of 4,000 (1,700 left). The 2025-10-29 readings (engine 30000; hubs 4,000 and 2,000) treat the engine count as of the effective date and show 300 cycles added to both the engine and each hub, which supports one-for-one accrual over that interval.
- **Note:** Cycle 30800 is the engine flight-cycle count at which hub PKLBSS9200 would reach 4,800 cycles since new under one-for-one accrual; the cycle number is fixed while the remaining count falls as the engine flies.
- **Note:** The reading used here treats 'before exceeding the applicable removal cycle limit' as a bound on the shop visit. If the shop-visit trigger were instead read as having no fixed bound, the status would be action_required_on_event with no computed deadline; the screen does not adopt that because the AD's wording ties the shop visit to the limit.
- **Note:** Both listed hubs were installed before the 2025-10-29 effective date, so the record shows no post-effective-date installation. The installation prohibition in paragraph (h) still governs any future installation of these two hubs in any engine.
- **Note:** The record has no ad_records or amoc_claims entries: no AMOC is claimed and no operator-recorded AD status is supplied. Neither is needed to reach this screen result.
- **Note:** The installed_components list shows one HPT 1st-stage hub and one HPT 2nd-stage hub; the screen assumes no other hub covered by Table 1 is installed. The events list is empty, so no event carries a qualifies_as_engine_shop_visit flag.
- **Note:** Federal Register 2025-10764 is the June 2025 NPRM and is superseded background here; the requirements above come from 2025-18469.
- **Note:** Per the preamble discussion in 2025-18469, complying with paragraph (g) provides a terminating action for that portion of the AD, but the installation prohibition keeps the AD applicable to this engine model after the hubs are removed.

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive applies to this V2528-D5 engine and is in force on 2026-03-10. The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) is a table 1 hub at 2,500 of its 6,200-cycle removal limit, so it must be removed and replaced at the next engine shop visit and before engine flight cycle 54,200; the later-of wording makes that shop visit govern over the 100-cycle date (50,100). Whether the HPT 2nd-stage hub is a table 1 hub cannot be determined because its serial number is unknown.
- **Stated timing:** Remove and replace the HPT 1st-stage hub at the next engine shop visit after 2025-10-29, and in any case before the hub exceeds 6,200 cycles since new, which is engine flight cycle 54,200 on the recorded accrual. The 100-flight-cycle date (engine flight cycle 50,100) is earlier than the 50,500 recorded on 2026-03-10, but under 'whichever occurs later' the shop-visit clause controls on this record, so the removal is not due at that earlier date, and no engine shop visit after 2025-10-29 is recorded.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub (P/N 2A4802) has an unknown serial number, so it cannot be matched to the four table 1 serial numbers for that P/N (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100). An unknown value is not evidence that the hub is unaffected, so its status under paragraphs (g) and (h) stays open.
- **Missing fact:** Cycles since new are unknown. If the serial number proves to be a table 1 serial number, the removal limit (3,900 to 6,000 cycles depending on serial number) and the remaining-cycle count cannot be computed from this record.
- **Missing fact:** The install date is not recorded. Paragraph (h) bars installing a table 1 hub in any engine after 2025-10-29, so an install date after that date would matter if the serial number proves to be listed.
- **Missing fact:** The engine record's events list is empty. Confirm that no engine shop visit meeting paragraph (i)(2) occurred after 2025-10-29; an unrecorded shop visit would have required removal of the hub at that visit, which could make the action already overdue and would change the timing.
- **Note:** Screening aid only; this is not a compliance determination and does not state the engine's status under the directive.
- **Note:** Model V2528-D5 is within the supported scope and the applicability paragraph, and the final rule effective 2025-10-29 is in force on 2026-03-10.
- **Note:** Cycle arithmetic: from 2025-10-29 to 2026-03-10 the 1st-stage hub's cycles since new rose from 2,000 to 2,500 while engine flight cycles rose from 50,000 to 50,500, so on this record the hub accrues one cycle per engine flight cycle. The 6,200 limit is reached at engine flight cycle 54,200 and 3,700 cycles remain; this assumes the hub stays installed on this engine at that rate.
- **Note:** Timing reading: paragraph (g) makes the later of the shop-visit clause and the 100-cycle clause control. No engine shop visit after the effective date is recorded, so the shop visit is the later event and governs, subject to the removal cycle limit. The earlier-date reading in alternative_readings is not the text as written.
- **Note:** The events list is empty, which does not prove that no shop visit occurred; confirm the shop visit history before relying on the timing above.
- **Note:** The HPT 2nd-stage hub has P/N 2A4802, which appears in table 1, but its serial number is unknown, so it is not a matched part and no removal limit or remaining-cycle count is given for it. component_cycles_remaining reflects only the 1st-stage hub.
- **Note:** The 1st-stage hub was installed on 2024-06-03, before the effective date, so that installation is not itself a paragraph (h) event; paragraph (h) bars installing P/N 2A5001 S/N PKLBST7489 in any engine after 2025-10-29.
- **Note:** The record has no ad_records or amoc_claims entries, so no operator AD status or alternative method of compliance is evaluated here. The final rule states that removing all affected hubs does not make the AD inapplicable, so the installation prohibition continues after removal.
- **Note:** NPRM 2025-10764 was superseded by the final rule 2025-18469, which controls.
- **Unresolved locator:** 2025-18469 (g) Required Actions; Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBST7489 (removal cycle limit 6,200) and HPT 2nd-stage hub rows for P/N 2A4802

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2025-19-13 (final rule 2025-18469) is in force and applies to this V2522-A5 engine by model, but the record has empty installed-component and event lists and no flight-cycle counter, so it cannot be determined whether a Table 1 HPT 1st-stage or 2nd-stage hub is installed or when any removal falls due. Status is needs review until those facts are supplied.
- **Stated timing:** Due only if a Table 1 hub is installed: remove the hub and replace it with a part eligible for installation at the next engine shop visit after 2025-10-29, before exceeding that hub's listed removal cycle limit, or within 100 flight cycles after 2025-10-29, whichever occurs later. No calendar or cycle date can be fixed from this record.
- **Missing fact:** installed_components is an empty list, so the record does not show whether an HPT 1st-stage hub is installed; an empty list is not evidence that none is installed or that the hub is unaffected. If one is installed, its P/N and S/N must be checked against Table 1 (P/N 2A5001 with S/N PKLBSK9287, PKLBSS9200, PKLBST5011 or PKLBST7489; listed limits 100, 4,800, 5,500 or 6,200 cycles since new) and its cycles since new must be known to find the remaining cycles.
- **Missing fact:** Same gap for HPT 2nd-stage hubs. Table 1 lists P/N 2A4802 with S/N PKLBST5005, PKLBSS9840, PKLBSS0301 or PKLBSR2100 (listed limits 4,000, 3,900, 5,000 or 6,000 cycles since new).
- **Missing fact:** events is empty, so no engine shop visit since the 2025-10-29 effective date is recorded, and no event is marked as qualifying or not qualifying as an engine shop visit under paragraph (i)(2). The next qualifying shop visit is the trigger for the paragraph (g) removal, so the event history is needed to know whether that trigger has occurred.
- **Missing fact:** The engine record has no flight-cycle counter. The flight-cycle count on the 2025-10-29 effective date is needed to fix the 100-flight-cycle point in paragraph (g).
- **Missing fact:** The current flight-cycle count at the 2026-09-26 snapshot is needed to tell whether the 100-flight-cycle point has passed and to convert any removal cycle limit into a flight-cycle deadline.
- **Note:** Authority: 2025-18469 is the final rule for AD 2025-19-13, published 2025-09-24 with an effective date of 2025-10-29, so it is in force on the 2026-09-26 question date. The NPRM 2025-10764 is the proposal that the final rule adopted with only minor editorial changes; it was not relied on for any requirement.
- **Note:** Model V2522-A5 is on the supported scope list and is named in paragraph (c), so no scope exclusion applies.
- **Note:** The record has no installed components, no events, no flight-cycle counter, and no ad_records or amoc_claims entries. These gaps are not evidence that Table 1 hubs are absent or that the required action has been taken, and no operator-asserted status or AMOC claim was considered.
- **Note:** If a Table 1 hub is found installed, the paragraph (g) removal is due at the later of the next engine shop visit after 2025-10-29 (before exceeding that hub's listed removal cycle limit) and 100 flight cycles after 2025-10-29. The record has neither the 2025-10-29 cycle count nor the shop-visit history, so neither the deadline nor whether it has already passed can be established here; a reviewer should pull the cycle and shop-visit history from 2025-10-29 forward.
- **Note:** Paragraph (g) pairs a shop-visit trigger bounded by the listed cycle limit with a 100-flight-cycle point, joined by 'whichever occurs later'. The wording admits more than one reading, but the record lacks the cycle counts and shop-visit history needed to turn either reading into a flight-cycle number, so no alternative reading with a numeric deadline is given.
- **Note:** latest_engine_flight_cycles and component_cycles_remaining are null because neither the engine flight-cycle counter nor the cycles since new of any installed hub is in the record.
- **Note:** Paragraph (h) binds this engine whether or not a Table 1 hub is found installed, and the preamble states the AD does not stop applying when affected hubs are removed; a removal finding would therefore not end the continuing installation prohibition.
- **Note:** This screen is an aid for review only, based solely on the supplied directive text and engine record, and makes no finding about the engine or any part.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The recorded engine model V2500-A1 is not one of the ten IAE V2500 models this screen supports or that the applicability paragraph of AD 2025-19-13 (Federal Register document 2025-18469) lists, so no applicability determination is made and no action is set. The final rule is in force on 2026-09-26 (effective October 29, 2025), but that does not bring this engine model within its applicability.
- **Note:** Scope gate stopped the screen: engine_model V2500-A1 is not one of the ten listed IAE V2500 models, so no applicability determination, deadline, cycles-remaining figure, or continuing-obligation status is given.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) corresponds to a row of table 1 to paragraph (g); because the engine is outside scope, that hub is not evaluated against the row's removal cycle limit and is not listed in matched_parts.
- **Note:** Paragraph (h) says 'in any engine'. The preamble indicates the installation prohibition applies to models listed in the Applicability paragraph, so this screen does not read (h) to reach V2500-A1. Even on a broader reading, (h) bars future installation rather than requiring removal, and no installation event is recorded, so no deadline would arise; confirm this reading before any listed hub is installed in a non-listed model.
- **Note:** The record lists only one installed component (HPT 1st-stage hub). The absence of an HPT 2nd-stage hub entry is not evidence that none is installed; the gap matters only if the engine is re-screened under a listed model.
- **Note:** If engine_model is a recording error and the engine is one of the listed models, re-run the screen with the confirmed model; the screen would then need the hub's recorded cycles since new (2000) against its table 1 limit, an HPT 2nd-stage hub record, and the events history, which is empty and does not establish that no engine shop visit occurred.
- **Note:** Authority is taken from final rule 2025-18469, effective 2025-10-29; the earlier NPRM 2025-10764 is a proposal and is not relied on.
- **Note:** The record is marked synthetic (SYN- identifiers) and is used as supplied.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row with P/N 2A5001 and S/N PKLBST5011

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (FR 2026-16954, as corrected by FR 2026-18423) applies to this V2527-A5 because the recorded 3rd stage HPC rotor blade set is P/N 6A8353, a listed P/N, and the directive has been in force since 2026-09-24. Replacement of the full blade set with parts eligible for installation is required only at the next engine shop visit after that date where a blade is exposed, and the record shows no events, so no action is due now and no fixed deadline applies.
- **Stated timing:** No calendar or cycle deadline. Due at the next engine shop visit (induction of the engine into the shop for maintenance) after 2026-09-24 at which any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum; the full set must then be replaced with parts eligible for installation.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** The record has no events, so no engine shop visit (induction of the engine into the shop for maintenance) on or after 2026-09-24 is recorded. Whether such an induction has occurred, and whether any 3rd stage HPC rotor blade was removed from the HPC stage 3 to 8 drum during it, is not confirmed. That induction is the only trigger for paragraph (g), so it decides whether replacement is already due or remains a future event.
- **Note:** Screening aid only; this is not a compliance determination for this engine or any part.
- **Note:** The record is marked synthetic (SYN- identifiers). The question date 2026-10-05 is after the 2026-09-24 effective date, so authority_state is in_force.
- **Note:** The governing text is the final rule FR 2026-16954 as corrected by FR 2026-18423, which restored 'blade' in paragraph (g); the corrected wording is used here. Both wordings tie the requirement to the next engine shop visit after the effective date, so the deadline does not change and alternative_readings is empty.
- **Note:** The November 2025 NPRM (FR 2025-20088) proposed a blade-exposure trigger; the final rule replaced that trigger and the NPRM was not relied on.
- **Note:** Trigger test: replacement is required only when an engine shop visit after 2026-09-24 (induction into the shop for maintenance) includes a blade removed from the HPC stage 3 to 8 drum. On the text, an induction with no blade removal does not trigger paragraph (g).
- **Note:** The events list is empty and is read here as no recorded shop visit. If an induction after 2026-09-24 with blade removal exists but is not in the record, replacement would be due at that visit and this screen must be rerun on the full event history.
- **Note:** Preamble: the FAA does not intend to require engines inducted into a shop visit before the effective date to comply. The record holds no induction dates, so this cannot be checked here.
- **Note:** The set is recorded at base P/N 6A8353 with no -001 suffix. Confirm the set's P/N at any exposure, because blades modified to 6A8353-001 are eligible parts under (h)(1).
- **Note:** The set serial number is not tracked. Applicability is keyed to P/N, so this does not change the screen.
- **Note:** Preamble: the FAA states that replacing blades under IAE AG SB V2500-ENG-72-0716 (dated October 4, 2024) changes the P/Ns to eligible parts. The SB is not incorporated by reference and is not in the record; its content was not verified.
- **Note:** No ad_records or amoc_claims were supplied for AD 2026-17-03, and no AMOC is evaluated here.
- **Note:** The AD sets no blade cycle limit and no blade cycle data is recorded, so component_cycles_remaining and latest_engine_flight_cycles are null.

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** AD 2026-17-03 (final rule 2026-16954, paragraph (g) corrected by 2026-18423) is in force on 2026-10-05 but applies only to V2533-A5 engines with 3rd stage HPC rotor blade P/N 6A8353 or 6A8688 installed. The only installed component entry is a 3rd stage HPC rotor blade set recorded as P/N 6C8368, which the AD lists as a part eligible for installation rather than an affected part, so the engine falls outside the applicability on the supplied record and no action is triggered.
- **Note:** Screening aid only: this is not a compliance determination and not an operator AD status record. No ad_records or amoc_claims were supplied, so the result rests only on the installed-component entry and the events list.
- **Note:** Authority: final rule 2026-16954 (published 2026-08-20) takes effect 2026-09-24, so it is in force on the 2026-10-05 question date. The NPRM 2025-20088 is a superseded proposal and was not relied on; its trigger was the next 3rd stage blade exposure, while the final rule uses the next engine shop visit where the blade is exposed.
- **Note:** Correction 2026-18423 (published 2026-09-10) fixes paragraph (g) by restoring the omitted word blade; the corrected wording is used here and the correction does not affect applicability.
- **Note:** Applicability turns on an installed 3rd stage HPC rotor blade with P/N 6A8353 or 6A8688. The record has one component entry, a 3rd stage HPC rotor blade set recorded as P/N 6C8368; this screen takes that set-level P/N as the P/N of the installed blades. Serial numbers are not tracked at set level, but the AD keys on P/N and lists no serial numbers, so the untracked serial does not by itself change the result.
- **Note:** No engine shop visit is recorded (events is empty), so the paragraph (g) trigger has not occurred on this record; that fact does not drive the result because the directive does not attach to this installed configuration.
- **Note:** Conditional only: if blade-level records showed any 6A8353 or 6A8688 blade installed, the engine would fall within paragraph (c). The required action would then be full-set replacement with parts eligible for installation at the next engine shop visit after 2026-09-24 where the blade is exposed; that is event-triggered with no fixed flight-cycle or calendar deadline, and the screen would need to be rerun on that record.
- **Note:** No continuing obligations are listed because the directive does not apply on this record. matched_parts is empty because 6C8368 is not a listed affected P/N, although it is a listed eligible P/N under paragraph (h)(1)(i).
- **Note:** Engine model V2533-A5 is on the supported scope list, so an applicability determination was made.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** Applies: the installed 3rd stage HPC rotor blade set is P/N 6A8688 on a listed V2530-A5 engine, and the directive has been in force since 24 September 2026. No action is triggered now because the engine shop visit (induction 14 September 2026) predates the effective date, so the 30 September 2026 blade removal during that visit does not trigger paragraph (g); full-set replacement is due only at the next engine shop visit inducted after 24 September 2026 in which a 3rd stage HPC rotor blade is exposed.
- **Stated timing:** No calendar or flight-cycle deadline. Full-set replacement is due at the next engine shop visit inducted after 24 September 2026 in which a 3rd stage HPC rotor blade is exposed (removed from the stage 3 to 8 drum); the 14 September 2026 visit does not count.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The operator-asserted induction date of 14 September 2026 decides whether this visit began before the 24 September 2026 effective date. Confirm it against the shop induction record; if the induction was on or after 24 September 2026, the 30 September 2026 blade removal would trigger paragraph (g) and full-set replacement would be due during that visit.
- **Note:** Screening aid only: this is not a compliance determination and not an AD status record. The record holds no ad_records or amoc_claims entries, so no operator status or alternative method was evaluated.
- **Note:** Applicability turns on the installed part number: the blade set is recorded as P/N 6A8688, which paragraph (c) lists. The set-level serial number is not tracked, which does not affect applicability because the directive lists part numbers only.
- **Note:** The operator's qualification of the 14 September 2026 induction as an engine shop visit is consistent with paragraph (h)(3), which defines an engine shop visit as the induction of an engine into the shop for maintenance. The qualification does not address the effective-date limit in paragraph (g), and that limit decides this case.
- **Note:** Timing: the induction (14 September 2026) precedes the 24 September 2026 effective date. The 30 September 2026 blade removal meets the paragraph (h)(2) exposure definition but occurred during a visit inducted before the effective date. The preamble of 2026-16954 states the FAA does not intend to require engines inducted before the effective date to comply, so this visit does not trigger paragraph (g).
- **Note:** Alternative reading not adopted: that the 30 September 2026 exposure is itself the post-effective event, which would require full-set replacement during the current visit before the engine leaves that visit. That reading conflicts with paragraph (h)(3) and the preamble. Its deadline cannot be stated as a flight-cycle integer from this record, so it is described here rather than in alternative_readings.
- **Note:** The record does not say whether the blade removed on 30 September 2026 was reinstalled or replaced during the visit. The outcome does not depend on it because paragraph (g) is not triggered by this visit.
- **Note:** Correction 2026-18423 (published 10 September 2026) changes paragraph (g) from rotor is exposed to rotor blade is exposed and states the effective date remains 24 September 2026. The corrected wording does not change this timing analysis.
- **Note:** The record has no engine flight-cycle counter, and the trigger is a shop-visit event rather than a cycle count, so latest_engine_flight_cycles and component_cycles_remaining are null.
- **Note:** Verify the induction date against shop induction documentation before relying on this result. If the induction was on or after 24 September 2026, the 30 September 2026 blade removal would trigger paragraph (g), and full-set replacement with parts eligible under paragraph (h)(1) would be due during that visit.
- **Note:** Clarify any reading that departs from the preamble with the FAA contact named in paragraph (j) before relying on it.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model V2527E-A5 is a listed model, and the recorded 3rd stage HPC rotor blade set with P/N 6A8353 falls within the proposed applicability text, but Federal Register document 2025-20088 is a notice of proposed rulemaking with no effective date and cannot yet require action as of 2026-01-15. If adopted as proposed, full-set replacement would be due at the next 3rd stage HPC rotor blade exposure after the effective date.
- **Stated timing:** Not due now: the document is a proposal with no effective date, so no required action exists. If adopted as proposed, action would be due at the next 3rd stage HPC rotor blade exposure after the effective date, with no fixed calendar or cycle deadline.
- **Missing fact:** The effective date is not stated (the Federal Register record shows none) and no final rule is in the packet; a final rule with its text and effective date would be needed before any action could be required or any deadline set.
- **Missing fact:** Blade-level serial numbers are not tracked at set level, so individual blade part numbers and any -001 modification cannot be confirmed; the applicability reading here relies on the set-level P/N 6A8353 being the P/N of the installed blades.
- **Missing fact:** The record shows base P/N 6A8353 only; no modification to P/N 6A8353-001 and no eligible P/N (6C8368, 6C8403, or later approved P/N) is recorded, so eligibility under paragraph (h)(1) cannot be determined from the record for the replacement step.
- **Missing fact:** The engine events list is empty, so whether any 3rd stage HPC rotor blade has been removed from the HPC stage 3 to 8 drum (the paragraph (h)(2) exposure) is unknown; an empty list is not evidence that no exposure occurred, and exposure timing relative to a future effective date is needed.
- **Note:** Screening aid only; this output is not an AD status determination and makes no statement about the status of the engine or any part.
- **Note:** Authority: 2025-20088 is a notice of proposed rulemaking published 2025-11-18 with effective date none. The packet contains no final rule, correction, or superseding document, so the proposal is treated as not in force as of 2026-01-15. The comment period in paragraph (a) closed January 2, 2026, before the question date.
- **Note:** Applicability: V2527E-A5 is a supported model and is named in paragraph (c). The record lists a 3rd stage HPC rotor blade set with P/N 6A8353, which matches a listed P/N. The set-level P/N is treated as the blade P/N; blade-level confirmation would close that gap but does not change the applicability reading on the current record.
- **Note:** Action now: none is triggered. Once in force, paragraph (g) would require replacing the full set of 3rd stage HPC rotor blades with eligible parts at the next blade exposure after the effective date. That obligation would be event-triggered with no calendar or cycle deadline, so latest_engine_flight_cycles and component_cycles_remaining are null.
- **Note:** continuing_obligations is empty because no obligation binds while the document is a proposal; the proposed paragraphs (f) through (i) would matter only if adopted in final form.
- **Note:** The record has no ad_records or amoc_claims entries, so no operator-asserted AD status or AMOC claim is assessed here.
- **Note:** The engine record is marked synthetic (SYN- identifiers); the snapshot date 2026-01-15 matches the question date.
- **Unresolved locator:** 2025-20088 preamble Federal Register header 'Effective date: none'; DATES section

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 (Federal Register document 2025-17066, effective 2025-10-10, in force on the 2025-11-15 question date) applies to this IAE V2527-A5 engine, so the operator must incorporate table 1 to paragraph (g) into paragraph B.1 of the V2500-A5 TLM ALS and, as an air carrier, into its approved maintenance program within 90 days. The operator's record states that neither is yet revised, so the required action remains to be done by 2026-01-08, a deadline that had not passed on 2025-11-15.
- **Stated timing:** Within 90 days after the 2025-10-10 effective date, i.e. on or before 2026-01-08 (a calendar deadline; 54 calendar days remained on 2025-11-15).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** No HPT Stage 1 Hub component record (listed P/N 2A5001) is in the engine record; installed_components and events are both empty. Whether this hub is installed, its serial number, and whether it has had piece-part exposure are unknown. An empty list is not evidence that the hub is absent or unaffected. This does not change the revision deadline but decides whether and when TASK 72-45-11-200-006 falls due.
- **Missing fact:** No HPT Stage 2 Hub component record (listed P/N 2A4802) is in the engine record, for the same reasons. This decides whether and when TASK 72-45-31-200-009 falls due.
- **Missing fact:** The statement that neither the approved maintenance program nor TLM paragraph B.1 yet incorporates table 1 is the operator's own assertion. No program or TLM document was supplied to verify it, and its accuracy decides whether the required action is still open.
- **Missing fact:** The directive gives no inspection interval for TASK 72-45-11-200-006 or TASK 72-45-31-200-009. The tasks are located in paragraph B.1 of the Maintenance Scheduling section of the revised TLM, which was not supplied; any threshold would be found there, so no next-due cycle or date can be computed from the supplied text.
- **Note:** Synthetic record (synthetic true; SYN- identifiers) used as supplied. This is a screening aid only and makes no AD status or airworthiness determination.
- **Note:** Authority: AD 2025-17-16 (Amendment 39-23126) is the final rule published 2025-09-05 as Federal Register document 2025-17066, effective 2025-10-10. No correction or later superseding document was supplied, so it is in force on 2025-11-15.
- **Note:** The NPRM (Federal Register document 2024-26092, published 2024-11-12, no effective date, comments due 2024-12-27) is a superseded proposal and was not relied on. Its paragraph (g) differed: it named the engine maintenance manual rather than the TLM, had no air carrier split, and cited TASK 72-45-11-200-009 for the stage 2 hub, which the final rule corrects to TASK 72-45-31-200-009.
- **Note:** Deadline: 90 calendar days after 2025-10-10 is 2026-01-08. The trigger is the effective date, not the 2025-09-05 publication date. If a reviewer counts the effective date as day one, the result is 2026-01-07; the earlier date is the safer internal target.
- **Note:** The overall action_status is action_required because the documentation revision is a calendar obligation; the hub inspections themselves are event-driven (piece-part exposure) and carry no date in the supplied text.
- **Note:** latest_engine_flight_cycles and component_cycles_remaining are null: the revision deadline is calendar-based, the engine record has no flight-cycle counter, and no component record exists from which a remaining-cycle figure could be computed.
- **Note:** installed_components is empty, so no part matches are made and no hub is treated as absent or unaffected. events is empty, so no piece-part exposure of either hub is recorded; that absence of a record is not evidence that no exposure occurred.
- **Note:** Of the TLM entries in (g)(1)(i) through (iii), only (g)(1)(i) (V2500-A5, P/N 2A4408) appears to apply, since the record refers only to the V2500-A5 TLM.
- **Note:** The operator's statement that Revision 47 (2025-06-01) and TLM paragraph B.1 do not yet incorporate table 1 is an assertion to check against the program and TLM documents, which were not supplied.
- **Note:** Per the FAA's comment responses, incorporation into the TLM alone satisfies the AD only for operators without an existing approved program; this air carrier must also change its approved maintenance or inspection program under (g)(2).
- **Note:** The preamble records a commenter's reference to replacement before 20,000 flight cycles in the operator's AMP. The directive sets no such limit and that figure is not used in this screen.
- **Note:** No ad_records or amoc_claims were supplied and no AMOC is claimed; paragraph (i) matters only if an AMOC is later proposed.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** Model V2522-A5 is within the applicability of AD 2025-17-16 (final rule 2025-17066), which has been in force since its October 10, 2025 effective date, so the paragraph (g)(1) revision of paragraph B.1 of the Maintenance Scheduling section of the airworthiness limitations section is required by January 8, 2026. Whether the separate paragraph (g)(2) program revision also applies cannot be settled because operator air-carrier status is unknown, and the record supplies no ad_records entry and no hub component records.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, so on or before January 8, 2026 (54 days after the 2025-11-15 question date); the paragraph (g)(2) program revision has the same 90-day window if the operator conducts air carrier operations.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Value is unknown. Paragraph (g)(2) requires revising the existing approved maintenance or inspection program within the same 90-day window only for air carrier operations, so this value decides whether (g)(2) applies in addition to (g)(1). An unknown value does not exclude air carrier operations.
- **Missing fact:** No ad_records entry for AD 2025-17-16 is supplied, so the record does not show whether the paragraph (g)(1) TLM revision, or the paragraph (g)(2) program revision if applicable, has been recorded. The screen does not infer completion or non-completion from the absence of an entry.
- **Missing fact:** No component record is supplied for the HPT Stage 1 Hub (P/N 2A5001, inspection TASK 72-45-11-200-006) and installed_components is empty. Whether this hub is installed, its serial number, and its cycles since new are unknown, so its piece-part inspection cannot be tied to a part and no cycle margin can be computed. An empty list is not evidence that the hub is absent.
- **Missing fact:** No component record is supplied for the HPT Stage 2 Hub (P/N 2A4802, inspection TASK 72-45-31-200-009) and installed_components is empty. Whether this hub is installed, its serial number, and its cycles since new are unknown, so its piece-part inspection cannot be tied to a part and no cycle margin can be computed. An empty list is not evidence that the hub is absent.
- **Note:** Record is marked synthetic (synthetic: true; SYN- identifiers). The screen uses the supplied record and the final rule only.
- **Note:** Operative text is Federal Register document 2025-17066 (final rule, AD 2025-17-16, Amendment 39-23126), effective October 10, 2025. The NPRM 2024-26092 is a proposal and is not relied on; its Table 1 listed TASK 72-45-11-200-009 for the stage 2 hub, which the final rule corrects to TASK 72-45-31-200-009.
- **Note:** Deadline arithmetic: 90 days from October 10, 2025 is January 8, 2026. The deadline is calendar-based and the record has no flight-cycle counter, so the cycle fields are null.
- **Note:** Model series: paragraph (g)(1)(i) names the V2500-A5 TLM; this screen takes that entry as the TLM for the V2522-A5 by model series. The record does not name the TLM or ICA revision the operator uses, or whether it already carries the paragraph B.1 entries.
- **Note:** installed_components and events are both empty. Neither is evidence that the hubs are absent or that no piece-part exposure has occurred; the paragraph B.1 hub tasks are performed at piece-part exposure, so a piece-part exposure would make them relevant.
- **Note:** No amoc_claims are supplied, so no alternative method is evaluated. Unknown air-carrier status is not evidence that the operator is not an air carrier.
- **Note:** Paragraph (f) lets an operator skip work already done. With no ad_records entry, this screen cannot account for any earlier work.
- **Note:** A commenter (SIAEC) cited a 20,000-flight-cycle hub replacement limit in another maintenance document (AMP section 18). That figure is not in the directive text and is not used here.
- **Note:** Screening aid only: this output identifies the required action and open facts. It does not determine compliance status or describe the operator's AD status record.
- **Unresolved locator:** 2025-17066 (g)(1)(i) TLM list item (i): P/N 2A4408, TASK 05-10-00-990-000-B00 (V2500-A5)
- **Unresolved locator:** 2025-17066 (g) Table 1 to Paragraph (g), rows HPT Stage 1 Hub (2A5001) and HPT Stage 2 Hub (2A4802)

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The V2525-D5 engine is within the directive's applicability, and its installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) is listed in table 1 with a 6,000-cycle removal limit and 5,010 cycles remaining on the record. The final rule is not effective until 2025-10-29, so nothing is due on 2025-10-15; removal is required at the next engine shop visit after that date (before the hub exceeds its limit) or within 100 flight cycles after it, whichever is later, and no such visit is recorded.
- **Stated timing:** Nothing is due on 2025-10-15 because the directive is not effective until 2025-10-29. From 2025-10-29, remove HPT 2nd-stage hub P/N 2A4802, S/N PKLBSR2100 at the next engine shop visit after 2025-10-29 before it exceeds 6,000 cycles since new, or within 100 flight cycles after 2025-10-29, whichever occurs later.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** Engine flight-cycle counter at the snapshot and at the 2025-10-29 effective date. Needed to place the 100-flight-cycle point and any engine-cycle deadline on the engine's own count; the record gives only the hub's cycles since new (990), which is not an engine count.
- **Missing fact:** Planned date or flight-cycle count of the next engine shop visit after 2025-10-29. Removal falls due at that visit (if it occurs before the hub exceeds 6,000 cycles since new) or 100 flight cycles after 2025-10-29, whichever is later. No such visit is recorded and the events list is empty.
- **Note:** This is a screening aid only, not a determination on the engine. The record is marked synthetic; identifiers beginning SYN- are synthetic.
- **Note:** Applicability is by engine model under paragraph (c); the engine serial number does not affect applicability.
- **Note:** The engine record has no engine flight-cycle counter. The Table 1 limit is in hub cycles since new, so latest_engine_flight_cycles is null and component_cycles_remaining (6,000 minus 990 = 5,010) is the only computed figure.
- **Note:** The HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0018, 2,000 cycles since new) does not match any S/N that Table 1 lists for that P/N (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489), so its cycles were not compared with any listed limit. This does not address any other directive.
- **Note:** 'Whichever occurs later' is applied literally: removal is due at the later of (a) the next engine shop visit after 2025-10-29 that occurs before the hub exceeds 6,000 cycles since new and (b) 100 flight cycles after 2025-10-29. If a shop visit occurs before the 100-cycle point, the 100-cycle point governs; if the next shop visit comes later, that visit governs. Alternative_readings is empty because the readings cannot be stated as engine flight-cycle figures without the engine counter.
- **Note:** The events list is empty, so no engine shop visit after 2025-10-29 is recorded. Any future event's qualifies_as_engine_shop_visit flag is the operator's assertion and must be checked against paragraph (i)(2).
- **Note:** No ad_records or amoc_claims entries for this AD appear in the record, so no operator-asserted status or AMOC was relied on.
- **Note:** The NPRM 2025-10764 (published 2025-06-13) was superseded by final rule 2025-18469; the screen relies on the final rule only.
- **Unresolved locator:** 2025-18469 preamble Document header (published 2025-09-24; effective 2025-10-29) and DATES
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row P/N 2A4802, S/N PKLBSR2100, removal cycle limit 6,000
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub rows P/N 2A5001

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2531-E5 engine is within the applicability of Federal Register document 2025-18469 (AD 2025-19-13), and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is listed in table 1 with a 4,800-cycle removal limit but shows 4,990 cycles since new, so the hub must be removed and replaced within 100 flight cycles after the October 29, 2025 effective date, by engine flight cycle 60,100. The installed HPT 2nd-stage hub (S/N SYN-HUB2-0019) is not listed in table 1 and does not trigger the required action.
- **Stated timing:** Remove the HPT 1st-stage hub from service and replace it with a part eligible for installation within 100 flight cycles after the October 29, 2025 effective date, i.e. by engine flight cycle 60,100 (60 flight cycles remain from the 60,040 engine count on 2025-11-05); the at-next-shop-visit option cannot be met because the hub already exceeds its 4,800-cycle removal limit.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Note:** Screening aid only, not a compliance determination. Identifiers beginning SYN- are synthetic.
- **Note:** Authority: 2025-18469 is a final rule effective 2025-10-29 and was in force on the 2025-11-05 question date. The June 2025 NPRM 2025-10764 is only a proposal and was not relied on. The compliance clock runs from the 2025-10-29 effective date, not the 2025-09-24 publication date.
- **Note:** Compliance window: paragraph (g) takes the later of (a) the next engine shop visit before the table limit is exceeded and (b) 100 flight cycles after the effective date. The hub showed 4,950 cycles since new on 2025-10-29 and 4,990 on the snapshot, both above 4,800, so option (a) cannot be met and option (b) governs. The baseline is the engine counter reading of 60,000 dated 2025-10-29, which gives 60,100; flight cycles are counted on the engine counter, the only flight-cycle counter in the record. The reviewer should confirm that the 2025-10-29 reading is the count at the effective date.
- **Note:** Readings not carried as alternatives: (1) treating option (a) as an open-ended deferral to the next shop visit, which conflicts with the before-exceeding-the-limit qualifier for a part already past its limit and gives no fixed cycle count; (2) reading whichever occurs later as an earlier-of rule, which contradicts the text and would place the deadline at or before 60,000.
- **Note:** Component cycles remaining uses the snapshot value of 4,990 (-190). On the 2025-10-29 reading of 4,950 the figure is -150. The 40-cycle rise from 4,950 to 4,990 matches the engine rise from 60,000 to 60,040. At the 2025-11-05 engine count of 60,040, 60 flight cycles remain before 60,100.
- **Note:** HPT 2nd-stage hub S/N SYN-HUB2-0019 (P/N 2A4802) does not match any S/N listed for that P/N in table 1 (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100), so the table limits do not apply to it. Its record lacks an installation date and readings, which the match does not need.
- **Note:** The engine events list is empty, so no engine shop visit is recorded since the effective date. The deadline does not depend on a shop visit, and a shop visit before cycle 60,100 would not move it.
- **Note:** The engine record has no ad_records or amoc_claims entries, so there is no operator-recorded AD status or AMOC claim to check against this screen.
- **Note:** A replacement must be a hub whose P/N and S/N are not in table 1 (paragraph (i)(1)); installing any listed P/N and S/N combination is prohibited regardless of cycle count (paragraph (h)).
- **Unresolved locator:** 2025-18469 (g) Required actions paragraph and table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 PKLBSS9200 limit 4,800

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** Applicability is unknown: this V2533-A5 engine's HPT 1st-stage disk (P/N 2A5001) and HPT 2nd-stage disk (P/N 2A4802) match the directive's part numbers, but the directive reaches each disk only if its serial number is listed in an NMSB Appendix A table that was not supplied. If listed, each disk's ultrasonic inspection is due at the next engine shop visit after July 13, 2021 or before 3,200 flight cycles since that date, whichever occurs first, but the record has no cycle counts, so no engine flight-cycle deadline can be computed.
- **Stated timing:** Only if each disk's serial number is confirmed in the NMSB Appendix A tables: the USI of that disk is due at the next engine shop visit after July 13, 2021, or before the disk accumulates 3,200 flight cycles since July 13, 2021, whichever occurs first. The record shows no events and no cycle counts, so no calendar date or engine flight-cycle number can be fixed.
- **Missing fact:** Whether HPT 1st-stage disk S/N SYN-DISK1-0020 is listed in Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713, Revision 1, the NMSB that paragraphs (g)(1) and (g)(2) cite for this engine model; the appendix is not in the supplied text. Paragraph (c)(1) reaches the disk only if it is listed, so this decides whether paragraph (g)(1) applies.
- **Missing fact:** Whether HPT 2nd-stage disk S/N SYN-DISK2-0020 is listed in Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713, Revision 1; the appendix is not in the supplied text. Paragraph (c)(2) reaches the disk only if it is listed, so this decides whether paragraph (g)(2) applies.
- **Missing fact:** No flight-cycle count for this disk on any date is recorded. The 3,200-cycle limit runs from July 13, 2021, so the disk's cycles at that date and at the snapshot are needed to compute cycles remaining and the latest engine flight-cycle number.
- **Missing fact:** No flight-cycle count for this disk on any date is recorded. The 3,200-cycle limit runs from July 13, 2021, so the disk's cycles at that date and at the snapshot are needed to compute cycles remaining and the latest engine flight-cycle number.
- **Missing fact:** The engine record has no engine flight-cycle counter, so the deadline cannot be expressed as an engine flight-cycle number.
- **Missing fact:** The events list is empty. The record does not establish whether an engine shop visit (induction for H-P major flange separation, per paragraph (h)(1)) has occurred since July 13, 2021, which would trigger the USI of any listed disk at that visit, or whether either disk has already been inspected under this AD. An empty list is not evidence that no such event occurred.
- **Note:** Screening aid only, not a compliance determination. Applicability turns on whether the two installed disk serial numbers (SYN- identifiers, so synthetic) appear in Appendix A, Table 1 and Table 2 of IAE NMSB V2500-ENG-72-0713, Revision 1; those tables were not supplied, so no serial match is confirmed.
- **Note:** For V2533-A5 engines, paragraphs (g)(1) and (g)(2) cite only NMSB V2500-ENG-72-0713, Revision 1; the NMSB V2500-E5-72-0015 route in paragraphs (g)(5) and (g)(6) is for V2531-E5 engines and does not govern this engine.
- **Note:** The 3,200-cycle limit counts only cycles accumulated since the July 13, 2021 effective date; cycles before that date do not count, and the installation date does not set the baseline.
- **Note:** The record has no engine flight-cycle counter, disk cycle counts, piece-part history, ad_records entry or amoc_claims entry. The empty events list is not evidence that no shop visit or USI has occurred, and no ad_records or amoc_claims content was used as evidence.
- **Note:** Superseding AD 2022-02-09 (FR doc 2022-02574; published 2022-02-08; effective 2022-03-15) replaces AD 2021-11-15. On 2022-03-01 that superseding AD is published but not yet effective, while 2021-11960 is in force, so this answer addresses 2021-11960 only. Once effective, its paragraphs (g)(1) and (g)(2) set the V2533-A5 compliance time by Figure 1 to paragraph (g)(1), an image not in the supplied text, or within 10 FCs after March 15, 2022, whichever is later; re-screen against it then, because its deadlines can differ.
- **Note:** alternative_readings is empty: the original and superseding readings give different deadlines, but neither reduces to an engine flight-cycle integer from this record, so no number was invented.
- **Note:** matched_parts are matched on part number only; listed_serial_number is null because the NMSB Appendix A serial lists were not supplied.
- **Note:** Piece-part note: under Note 1 to paragraph (g)(1), the ALS piece-part inspections are not required by this AD unless a disk has more than 100 FCs since its last piece-part opportunity inspection, is damaged, or is the cause for engine removal; engine removal for this AD is not cause. No piece-part history is in the record, so this was not assessed.
- **Note:** Only the two installed disks in the record were screened; no other components or operator details were supplied.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2022-02574 (g)(1) Figure 1 to paragraph (g)(1) (image not included in supplied text)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** Applicability is unknown: V2530-A5 is a supported high-thrust model and both installed disks match the directive's listed part numbers (2A5001 and 2A4802), but applicability turns on whether their serial numbers appear in Appendix A tables that are not in the supplied text. The USI due date also depends on Figure 1 and the engine's flight-cycle history, both missing, so this screen needs review rather than a determination.
- **Stated timing:** For high-thrust V2530-A5 engines with listed disks, paragraphs (g)(1) and (g)(2) require each disk's USI by the Figure 1 to paragraph (g)(1) compliance time or within 10 flight cycles after March 15, 2022, whichever is later; Figure 1 is not in the supplied text, so no date or cycle count can be computed, and whether that point has already passed cannot be determined from the record.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (dated January 26, 2021), which lists HPT 1st-stage disk serial numbers for P/N 2A5001, is not in the supplied text. Needed to confirm whether installed S/N SYN-DISK1-0021 falls within paragraph (c)(1); the part-number match alone does not decide applicability.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1, which lists HPT 2nd-stage disk serial numbers for P/N 2A4802, is not in the supplied text. Needed to confirm whether installed S/N SYN-DISK2-0021 falls within paragraph (c)(2).
- **Missing fact:** Figure 1 to paragraph (g)(1), which sets the USI compliance time for high-thrust engines, is shown only as an image placeholder and is not in the supplied text. Needed to state any USI due date for either disk.
- **Missing fact:** Engine flight-cycle count on the directive effective date. Needed to apply the 10-flight-cycle floor after March 15, 2022, which sets the due date whenever it is later than the Figure 1 time. The engine record has no cycle counter.
- **Missing fact:** Engine flight-cycle count at the snapshot date. Needed to test the due dates against the engine's cycle history.
- **Missing fact:** HPT 1st-stage disk flight cycles since new and any operating history on other engine models. The component record has neither field; since Figure 1 is not in the text, its dependence on disk cycle history cannot be ruled out.
- **Missing fact:** HPT 2nd-stage disk flight cycles since new and any operating history on other engine models. The component record has neither field; same reason as the 1st-stage disk.
- **Missing fact:** The events list is empty. Missing: any engine shop visit on or after March 15, 2022 (H-P flange separation under paragraph (h)(1)), which Figure 1 may use to set a compliance time, and any USI of either disk under the NMSB with its date, cycle count, and pass or fail result. An empty list is not evidence that no shop visit or USI occurred.
- **Missing fact:** No operator AD status record for AD 2022-02-09 is in the record, so no USI, part replacement, or other disposition is asserted for either disk. Any such claim would need its disk serial numbers, dates, and cycle counts checked.
- **Note:** Screening aid only: this output does not determine compliance, airworthiness, or return-to-service status for the engine or either disk.
- **Note:** Scope: V2530-A5 is on the supported model list, so the screen was run. The record has no cycle counter, operator section, ad_records, or amoc_claims, and its events list is empty.
- **Note:** Model class: per the preamble of 2022-02574, V2530-A5 is a high-thrust model, so paragraphs (g)(1) and (g)(2) govern. Paragraphs (g)(3) and (g)(4) cover low-thrust models and (g)(5) and (g)(6) cover V2531-E5, so they do not apply to this engine.
- **Note:** Listing reference: paragraph (c) names Appendix A of either NMSB V2500-ENG-72-0713 Rev 1 or V2500-E5-72-0015 Rev 1, while (g)(1) and (g)(2) point to the V2500-ENG Rev 1 tables for this engine. Neither set of tables is in the supplied text, so the reviewer should confirm which listing controls the serial check.
- **Note:** matched_parts records part-number matches only. listed_serial_number is null because the supplied text does not give the listed serial numbers, not because the directive lists part numbers alone.
- **Note:** Figure 1 is referenced but not included, so no compliance time or due date has been assumed.
- **Note:** Absent records and an empty events list are not evidence that a part is unaffected or that a shop visit or USI did not occur; the status stays unresolved until those records are supplied.
- **Note:** Shop visit (paragraph (h)(1)): induction for maintenance involving separation of pairs of major mating H-P flanges. Flange separation solely for transportation, and engine removal for field maintenance at a maintenance facility in lieu of on-wing work, do not count.
- **Note:** Prior work: paragraph (i) credits only earlier (g)(5) and (g)(6) actions on V2531-E5 engines under NMSB V2500-E5-72-0015 original issue. The supplied text gives no credit for an earlier USI or replacement on a V2530-A5 disk, so whether any earlier work counts toward (g)(1) or (g)(2) needs review.
- **Note:** Superseded AD: AD 2021-11-15 (FR 2021-11960) is replaced by this AD under paragraph (b). Its 3,200-flight-cycle and next-engine-shop-visit terms are not used here. No integer deadline can be computed under either reading, so alternative_readings is empty.
- **Note:** Note 1 to paragraph (g)(1): the USI requires disk removal, which allows piece-part opportunity inspections. Per the ICA Airworthiness Limitations Section, additional piece-part inspections are not required unless the part has more than 100 FCs since its last piece-part opportunity inspection, is damaged, or is the cause of engine removal; engine removal to comply with this AD is not cause.
- **Note:** No AMOC claim is recorded. Any alternative method must be approved under 14 CFR 39.19 (paragraph (j)(1)), and the principal inspector notified before use (paragraph (j)(2)).
- **Note:** No later superseding or correcting document was supplied; this screen treats 2022-02574 as in force on 2026-10-06 on that basis.
- **Note:** Paragraphs (g)(1) and (g)(2) are separate requirements, one per disk; each disk's outcome depends on its own serial number check.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2022-02574 preamble Background, high-thrust and low-thrust categorization
- **Unresolved locator:** 2022-02574 (g)(1) Figure 1 to paragraph (g)(1), not included in supplied text
- **Unresolved locator:** 2022-02574 (g)(2) Figure 1 to paragraph (g)(1), not included in supplied text
- **Unresolved locator:** 2021-11960 (g)(1) Superseded; see 2022-02574 paragraph (b)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** The V2533-A5 engine has HPT 1st-stage disk P/N 2A5001, S/N PKLBSH1829 installed, and that serial is listed in paragraph (c)(1), so the AD applies and requires an ultrasonic inspection (USI) of that disk within 10 flight cycles after the July 19, 2021 effective date, that is by engine flight cycle 33010. The HPT 2nd-stage disk S/N SYN-DISK2-0022 is not on the paragraph (c)(2) serial list, and no USI completion is recorded in the supplied engine record.
- **Stated timing:** Within 10 flight cycles after the July 19, 2021 effective date, that is by engine flight cycle 33010; the 2021-07-20 reading of 33004 leaves 6 flight cycles before cycle 33010 is reached.
- **Expected timing:** Ultrasonic inspection within 10 FC after the effective date that applies to this operator: the date of actual notice of the emergency AD, or 2021-07-19 (engine counter 33,010) without actual notice.
- **Missing fact:** No AD status entry for AD 2021-11-51 is in the engine record, so it is not shown whether the USI of HPT 1st-stage disk S/N PKLBSH1829 was already completed. Paragraph (f) says to comply within the compliance times unless already done; if a completed USI is recorded, its date and engine cycle count would need to be checked against the paragraph (g)(1) window.
- **Missing fact:** Table 1 to paragraph (g)(1) is an image that is not included in the supplied text. Paragraph (g)(1) applies the USI to engines with an HPT 1st-stage disk listed in that table; this screen matched the disk using the paragraph (c)(1) serial list, which includes PKLBSH1829, and did not verify the table content.
- **Missing fact:** Table 2 to paragraph (g)(2) is an image that is not included in the supplied text. The HPT 2nd-stage disk S/N SYN-DISK2-0022 is not on the paragraph (c)(2) serial list, so the text gives no 2nd-stage match, but the table content could not be checked.
- **Note:** Screening aid only; this is not a determination of any engine's or part's status, airworthiness, or return to service.
- **Note:** Model V2533-A5 is in the AD's model list. Applicability rests on the HPT 1st-stage disk match to the paragraph (c)(1) serial list; the HPT 2nd-stage disk P/N 2A4802 matches the listed part number, but S/N SYN-DISK2-0022 is not listed, so it is not treated as a matched part.
- **Note:** The engine record has no ad_records or amoc_claims entries and an empty events list. These do not show whether the USI was performed, and no AMOC is claimed; the absence of a record is not treated as evidence that the USI was or was not done.
- **Note:** Deadline arithmetic: the 2021-07-19 reading of 33000 is taken as the engine cycle count on the effective date, and 33000 plus 10 flight cycles gives 33010. The 2021-07-20 reading of 33004 leaves 6 cycles in that window; confirm the count at the start of July 19, 2021 if an exact figure is needed.
- **Note:** component_cycles_remaining is null because the directive lists no part life limit in cycles; the 10-cycle window is a compliance time and is carried in latest_engine_flight_cycles.
- **Note:** Emergency AD 2021-11-51 (issued May 21, 2021, effective with actual notice) is described in the final rule as containing the same requirements. Its text and any earlier actual-notice compliance date are not in the supplied document, so this screen uses the July 19, 2021 effective date stated in the final rule; a reviewer should check any earlier emergency AD date.
- **Note:** The preamble also mentions earlier Emergency AD 2020-07-51, which removed the highest-risk HPT 1st-stage disks; its text is not supplied and this screen does not evaluate it.
- **Note:** The document is a final rule with request for comments; comments are due by August 16, 2021 per the preamble, and the July 19, 2021 effective date places the rule in force on the 2021-07-20 question date. The open comment period does not change that.
- **Note:** The engine record is marked synthetic; this screen uses only the values supplied.
- **Expected missing fact (judge on meaning):** operator date of actual notice of Emergency AD 2021-11-51
- **Expected missing fact (judge on meaning):** table 1 to paragraph (g)(1) content (image-only; transcription decided in E3)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 accomplishment instructions (unavailable incorporated material)
- **Unresolved locator:** 2021-14268 (g)(1) Table 1 to paragraph (g)(1) is an image not included in the supplied text
- **Unresolved locator:** 2021-14268 (g)(2) Table 2 to paragraph (g)(2) is an image not included in the supplied text

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-022/2021-11960: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** Applicability is unknown because the Appendix A serial-number tables that decide it are not in the supplied text, although V2533-A5 is a supported model and both installed disks match the directive's part numbers (2A5001 and 2A4802). If both serial numbers are listed, each disk would need an ultrasonic inspection (USI) at the next engine shop visit after July 13, 2021 or before 3,200 flight cycles since that date, whichever occurs first.
- **Stated timing:** Conditional on the Appendix A serial check: each disk's USI is due at the next engine shop visit after July 13, 2021 or before the disk accumulates 3,200 FCs since July 13, 2021, whichever occurs first; the record's events list is empty, so no shop visit is recorded.
- **Missing fact:** Whether HPT 1st-stage disk S/N PKLBSH1829 (P/N 2A5001) is listed in Appendix A, Table 1, of IAE NMSB V2500-ENG-72-0713 Rev 1 (or Table 1 of NMSB V2500-E5-72-0015, which paragraph (c)(1) also cites). Needed for applicability under (c)(1) and to decide whether (g)(1) is triggered; the NMSB tables are not in the supplied text or the engine record.
- **Missing fact:** Whether HPT 2nd-stage disk S/N SYN-DISK2-0022 (P/N 2A4802) is listed in Appendix A, Table 2, of IAE NMSB V2500-ENG-72-0713 Rev 1 (or Table 2 of NMSB V2500-E5-72-0015). Needed for applicability under (c)(2) and to decide whether (g)(2) is triggered.
- **Missing fact:** Engine flight-cycle count on the effective date, July 13, 2021. The 3,200-FC limit runs from that date, but the earliest reading in the record is 33,000 on July 19, 2021, so the exact engine-counter deadline cannot be computed.
- **Missing fact:** Each disk's accumulated flight cycles since July 13, 2021, and whether either disk was installed on other engines in that period. The record has no component cycle fields, so the disk-level 3,200-FC limit and the cycles remaining cannot be computed.
- **Note:** Screening aid only, not a compliance or airworthiness determination; nothing here states that either disk is compliant, noncompliant, safe, or approved for return to service.
- **Note:** Authority: the only document supplied is the final rule (AD 2021-11-15, Docket FAA-2021-0129), effective July 13, 2021, which is before the July 20, 2021 question date; no proposal, correction, or superseding document was supplied.
- **Note:** Model scope: V2533-A5 is on the supported list. Paragraphs (g)(3) and (g)(4) (6,700 FCs) cover only V2522-A5, V2524-A5, V2525-D5 and V2527-A5, and (g)(5) and (g)(6) cover only V2531-E5, so the V2533-A5 timing comes from (g)(1) and (g)(2).
- **Note:** Serial check: matched_parts is on part number only; the serial numbers must be checked against Appendix A Table 1 and Table 2 of NMSB V2500-ENG-72-0713 Revision 1, which are not in the supplied text. Paragraphs (c)(1) and (c)(2) also name NMSB V2500-E5-72-0015 as a source of listed serials, but the V2533-A5 action paragraphs cite only the Revision 1 tables; a serial listed only in the E5 table would need interpretation review.
- **Note:** Cycle counting: the 3,200-FC limit runs from July 13, 2021, not from the July 20 snapshot, so adding 3,200 to the 33,004 snapshot count (giving 36,204) would be wrong. The counter read 33,000 on July 19 and does not run backward, so if a disk had been on this engine since July 13, the engine counter at its 3,200-FC point would be at or below 36,200; the exact value needs the July 13 reading and the disk's own cycle history.
- **Note:** Shop-visit trigger: the events list is empty, so no engine shop visit is recorded since July 13, 2021. A future shop visit that meets the (h)(1) definition would set the USI deadline for each listed disk if it comes before the 3,200-FC point; an unrecorded visit would not appear in this screen.
- **Note:** Piece-part note: Note 1 to paragraph (g)(1) says additional ALS inspections are not required unless a part has more than 100 FCs since its last piece-part opportunity inspection, is damaged, or is the cause for engine removal; engine removal for this AD is not cause. The NMSB accomplishment paragraphs 6, 7 and 8 are not in the supplied text.
- **Note:** No ad_records or amoc_claims entries are in the record, so the screen relies only on the directive text and the installed-component and cycle fields; no operator AD status is treated as evidence.
- **Note:** Identifiers: the record is flagged synthetic, and disk serial SYN-DISK2-0022 carries the SYN- prefix; the screen takes the identifiers as given and does not infer NMSB table listing from the prefix.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)
- **Unresolved locator:** 2021-11960 (g)(3) V2522-A5, V2524-A5, V2525-D5, V2527-A5 only
- **Unresolved locator:** 2021-11960 (g)(4) V2522-A5, V2524-A5, V2525-D5, V2527-A5 only
- **Unresolved locator:** 2021-11960 (g)(5) V2531-E5 only; NMSB V2500-E5-72-0015
- **Unresolved locator:** 2021-11960 (g)(6) V2531-E5 only; NMSB V2500-E5-72-0015

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** AD 2026-17-03 (Federal Register 2026-16954, effective 2026-09-24 and so in force on the 2026-10-06 question date) applies to this V2527M-A5 because a 3rd stage HPC rotor blade set with P/N 6A8688 is recorded as installed. Its full-set blade replacement is required only at the next engine shop visit after 2026-09-24 where a 3rd stage HPC rotor blade is exposed, and the record shows no such visit, so no action is triggered yet.
- **Stated timing:** Required only at the next engine shop visit after 2026-09-24 at which a 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); no fixed calendar date or flight-cycle limit applies.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record lists no engine shop visit (induction of the engine into the shop for maintenance) on or after the 2026-09-24 effective date; the only recorded event is a 2025-12-01 maintenance program revision. Whether any such induction has occurred since 2026-09-24 is unconfirmed, and that induction is the trigger for paragraph (g), so it decides whether any action is due now.
- **Missing fact:** If an engine shop visit has occurred since 2026-09-24, the record does not show whether any 3rd stage HPC rotor blade was removed from the HPC stage 3 to 8 drum (blade exposure under paragraph (h)(2)). Exposure, not the visit alone, triggers the full-set replacement.
- **Missing fact:** Serial number is not tracked at set level, so individual blade part numbers and serials are unconfirmed. Blade-level records would show whether each blade carries P/N 6A8688 or a modified 6A8688-001 suffix, which bears on blade-level applicability, and would be needed to verify any later full-set replacement under paragraph (h)(1).
- **Note:** Screening aid only; this is not a compliance determination, an airworthiness finding, or a return-to-service statement.
- **Note:** V2527M-A5 is a supported model. The directive under question is FAA AD 2026-17-03 (Federal Register 2026-16954), in force since its 2026-09-24 effective date; no later superseding document was supplied.
- **Note:** Correction 2026-18423 (published 2026-09-10) changes paragraph (g) from 'where the 3rd stage HPC rotor is exposed' to 'where the 3rd stage HPC rotor blade is exposed'; the corrected wording is used. Both readings are shop-visit triggers with no cycle or calendar deadline, so no alternative reading with a different deadline is listed.
- **Note:** The NPRM 2025-20088 is a proposal superseded by the final rule and was not relied on.
- **Note:** The only recorded event is a 2025-12-01 maintenance program revision (Revision 48) incorporating table 1 of AD 2025-17-16. It is not an engine shop visit under AD 2026-17-03 and is not a record of blade replacement under it. AD 2025-17-16 was not supplied and was not evaluated.
- **Note:** Engine cycle readings (20000 on 2025-10-29; 22500 on 2026-10-06) and the HPT 1st- and 2nd-stage hub entries are not inputs to this AD. No cycle limit for the 3rd stage blades appears in the directive or the record, so no cycle deadline or remaining-cycle figure was computed.
- **Note:** If the record showed an engine shop visit after 2026-09-24 at which a 3rd stage HPC rotor blade was exposed and the blade set was not replaced at that visit, paragraph (g) would make replacement due at that visit and this screen would change to action_required. The record shows no such visit.
- **Note:** The recorded set P/N 6A8688 (no -001 suffix) matches the applicability list but is not a part eligible for installation under paragraph (h)(1); any replacement set must meet (h)(1).
- **Note:** No ad_records or amoc_claims entries for AD 2026-17-03 were supplied, so no operator AD status claim or AMOC claim was assessed.
- **Note:** No pre-effective-date engine shop visit is recorded, so the preamble's statement that engines inducted before 2026-09-24 are not intended to be covered does not affect this screen.
- **Note:** Per the preamble, parts availability concerns are addressed through an AMOC request under paragraph (i)(1) to extend the compliance time; repetitive inspections are not offered as an alternative.
- **Unresolved locator:** 2026-16954 (g) Required Actions, as corrected by 2026-18423

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-19-13 (Federal Register document 2025-18469) is in force and covers V2528-D5 engines, but on the record as supplied neither installed HPT hub matches a P/N and S/N pair in table 1, so no paragraph (g) removal is triggered now. The HPT 2nd-stage hub's S/N PKLBST5011 is listed in table 1 only with P/N 2A5001, so its S/N alone does not identify it, and the paragraph (h) installation prohibition still binds.
- **Missing fact:** Confirm the recorded P/N 2A4802 against the hub's identification. The no-match result rests on it: S/N PKLBST5011 is listed in table 1 only with P/N 2A5001 (HPT 1st-stage hub, 5,500-cycle limit), so a corrected P/N or S/N would need to be re-screened against table 1.
- **Missing fact:** The engine flight-cycle counter is not in the supplied record. It is needed to state any paragraph (g) deadline as an engine flight-cycle count if a table 1 P/N and S/N pair is later confirmed on an installed hub.
- **Missing fact:** The events list is empty, so no engine shop visit and no part installation after October 29, 2025 is recorded. Whether a shop visit has occurred or a table 1 hub has been installed since the effective date cannot be checked from this record, and an empty list is not evidence that neither occurred.
- **Note:** The final rule 2025-18469 is the operative text; the June 2025 NPRM 2025-10764 was not relied on. The question date is after the stated effective date of October 29, 2025.
- **Note:** Table 1 requires the installed part's P/N and S/N to match the same row. The HPT 2nd-stage hub's S/N PKLBST5011 appears only in the HPT 1st-stage hub row for P/N 2A5001 (5,500 cycles since new), and the recorded P/N 2A4802 is not paired with it. A serial-number-only reading would give 2,500 cycles remaining (5,500 less 3,000), but paragraph (g) does not support that reading, so no cycle count is reported.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0024) has a serial number that does not appear in table 1.
- **Note:** Applicability rests on the engine model V2528-D5, which is in the directive's applicability paragraph and in the supported scope list.
- **Note:** Because the recorded P/N and S/N of the HPT 2nd-stage hub do not form a table 1 pair, a reviewer may wish to confirm both against the hub's identification; if either is wrong, the hub must be re-screened.
- **Note:** If a table 1 P/N and S/N pair is confirmed on an installed hub, paragraph (g) would apply: removal would be due at the next engine shop visit after October 29, 2025 before exceeding the listed limit or within 100 flight cycles of October 29, 2025, whichever occurs later. The engine flight-cycle counter is not in the record, so that deadline cannot be stated as an engine flight-cycle count from this record.
- **Note:** No ad_records or amoc_claims were supplied; none were relied on, and no AMOC is claimed.
- **Note:** This is a screening result from the supplied record and the directive text. It is not a compliance determination and does not address return to service.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The recorded engine model CFM56-5B4/3 is not one of the IAE V2500 models this screen supports, so no applicability determination is made under AD 2025-17066 and action_status is none. The directive has been in force since its October 10, 2025 effective date, but that does not change the model-scope result for this engine.
- **Note:** Engine model CFM56-5B4/3 (engine_serial_number SYN-CFM56-0025) is outside the supported IAE V2500 model list, so this screen makes no applicability determination and assigns action_status none.
- **Note:** If engine.engine_model is a recording error, the field would need correction and the screen re-run; no supported model is inferred from the serial or asset identifiers.
- **Note:** The record has no installed_components and no events, so no part or event was evaluated against the directive.
- **Note:** The 2024 NPRM (2024-26092) was a proposal only; the final rule 2025-17066 text was used for this screen.
- **Note:** The record is marked synthetic and identifiers beginning with SYN- are synthetic; the operator field air_carrier_operation does not change the model-scope result.
- **Note:** This is a screening aid only and does not establish airworthiness or return-to-service status for any engine or part.

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-027: Listed hub near its limit, with an unverified AMOC claimed to extend it

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **No answer:** answer is not JSON: Unterminated string starting at: line 1 column 98 (char 97)
