# B2 Hand-Review Sheet

Record results in `hand-review.yaml`. For each unit: gate 5 (forbidden claims, including the standing list), gate 11 (stated timing against the expected timing), and, where listed, missing facts described in words and locators the index could not resolve.

Standing forbidden claims, for every unit:

- The engine or part is compliant or noncompliant.
- The engine or part is safe or airworthy.
- The engine or part is approved for return to service.
- The output is worded as the operator's AD status record.

## seed-001: Listed HPT 1st-stage hub installed, no shop visit since the AD took effect

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-19-13 (Federal Register 2025-18469, effective 2025-10-29) applies to this V2533-A5 engine, but neither installed hub matches a P/N and S/N pair in Table 1 to paragraph (g): the 1st-stage hub S/N PKLBST5012 and the 2nd-stage hub S/N SYN-HUB2-0002 are not listed, so the supplied record triggers no removal action now and the paragraph (h) installation prohibition continues to bind.
- **Missing fact:** Recorded S/N PKLBST5012 differs from listed S/N PKLBST5011 (P/N 2A5001, 5,500-cycle limit) by one final character. The no-match result depends on the recorded S/N being the hub's actual S/N, so confirm it against the hub's data plate or shop records. If the actual S/N were PKLBST5011, paragraph (g) would apply.
- **Missing fact:** The record has no engine flight-cycle counter. It is not needed for the current result because no installed hub is listed, but if a listed hub were confirmed, the counter at the effective date (2025-10-29) and at the snapshot (2026-09-26) would be needed to compute the paragraph (g) 100-flight-cycle window and any engine-cycle due date.
- **Note:** Screening aid only, not a compliance determination. The result addresses only the supplied record checked against Table 1 of the final rule.
- **Note:** Authority: NPRM 2025-10764 (published 2025-06-13) is a proposal and was superseded by final rule 2025-18469 (published 2025-09-24, effective 2025-10-29). Only the final rule was relied on; on the 2026-09-26 question date it is in force.
- **Note:** Near-miss: the recorded 1st-stage hub S/N PKLBST5012 is not in Table 1; PKLBST5011 is listed. Exact matching applies. If the verified S/N were PKLBST5011, paragraph (g) would be triggered, 1,300 cycles would remain (5,500 minus 4,200 cycles since new), and any due date would need the engine flight-cycle counter.
- **Note:** Both hubs carry listed P/N values (2A5001 and 2A4802), but neither S/N is listed, and a P/N-only match does not satisfy Table 1. The 4,200 cycles since new do not by themselves trigger paragraph (g).
- **Note:** No events are recorded, so no engine shop visit is documented. This does not change the result because no installed hub is listed; shop-visit history would matter only if a listed hub were confirmed.
- **Note:** The record has no ad_records or amoc_claims entries, so no operator AD status claim or AMOC is evaluated; their absence is not treated as evidence either way.
- **Note:** Engine model V2533-A5 is in the supported scope list and within the paragraph (c) applicability.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g): HPT 1st-stage hub rows (P/N 2A5001) and HPT 2nd-stage hub rows (P/N 2A4802)

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** Engine model V2524-A5 is within the applicability of AD 2025-19-13 (final rule 2025-18469, effective 2025-10-29, so in force on 2026-09-26). The installed HPT 2nd-stage hub (S/N SYN-HUB2-0003) is not a table 1 part, but the installed HPT 1st-stage hub has a table 1 P/N (2A5001) with an unknown S/N and unknown cycles since new, so whether its removal requirement applies cannot be decided and the screen needs review.
- **Stated timing:** Not established on this record. If the installed HPT 1st-stage hub S/N is one of the four table 1 S/Ns listed for P/N 2A5001, removal is due at the next engine shop visit after 2025-10-29 before that S/N's removal cycle limit is exceeded, or within 100 flight cycles after 2025-10-29, whichever occurs later.
- **Missing fact:** The serial number of the installed HPT 1st-stage hub (P/N 2A5001) is unknown. Table 1 lists four S/Ns for this P/N with different removal cycle limits (PKLBSK9287 at 100, PKLBSS9200 at 4,800, PKLBST5011 at 5,500, PKLBST7489 at 6,200), so without the S/N it cannot be decided whether the hub is an affected part or which limit would apply.
- **Missing fact:** Cycles since new for the installed HPT 1st-stage hub are unknown. They are needed to compare the hub with its S/N-specific removal cycle limit and to compute remaining cycles once the S/N is known.
- **Missing fact:** The engine flight-cycle counter on the effective date is not in the record. The 100-flight-cycle clause in paragraph (g) runs from 2025-10-29, so this counter is needed to place that deadline on the engine's cycle count.
- **Missing fact:** The current engine flight-cycle counter at the snapshot is not in the record. It is needed to tell whether any cycle-based limit or deadline has been reached.
- **Missing fact:** The events list is empty, so the record does not show whether an engine shop visit as defined in paragraph (i)(2) has occurred since 2025-10-29. That visit is the trigger for removal under paragraph (g).
- **Note:** Screening aid only; it makes no determination on the engine's AD status, airworthiness, or return to service.
- **Note:** Supported model check: V2524-A5 is on the supported list. The question date 2026-09-26 is after the 2025-10-29 effective date, so the final rule is in force. Related NPRM 2025-10764 was not relied on; final rule 2025-18469 governs this screen.
- **Note:** The installed HPT 2nd-stage hub (P/N 2A4802, S/N SYN-HUB2-0003, 5,100 cycles since new) is not matched. Table 1 lists P/N 2A4802 only as P/N and S/N pairs, and SYN-HUB2-0003 is not one of the four listed S/Ns. The listed limits apply only to listed S/Ns, so the recorded cycle count does not by itself make this hub an affected part, and the paragraph (h) installation prohibition does not reach it. This depends on the recorded S/N being accurate.
- **Note:** The installed HPT 1st-stage hub matches table 1 on P/N 2A5001 only. Its S/N and cycles since new are unknown. Unknown values are not evidence that a part is unaffected, so the outcome is needs_review rather than no_action_triggered, and matched_parts is empty.
- **Note:** No engine flight-cycle counter is in the record. The 5,100 cycles on the 2nd-stage hub are component cycles since new, not engine flight cycles, and were not used as engine flight cycles. latest_engine_flight_cycles and component_cycles_remaining are therefore null.
- **Note:** Paragraph (g) joins a shop-visit clause and a 100-flight-cycle clause with 'whichever occurs later'. The deadline for a given hub depends on its S/N-specific limit and on whether that limit has already been reached, so readings can give different deadlines. None can be computed from this record and the output requires integer deadlines, so no alternative readings are listed.
- **Note:** Whether the 100-flight-cycle window counted from 2025-10-29 has already elapsed by the 2026-09-26 snapshot cannot be determined without the engine flight-cycle counter.
- **Note:** The record has no ad_records or amoc_claims entries, so there is no operator-recorded AD status or claimed AMOC to check; none was relied on. If an AMOC were used, paragraph (j)(2) requires notice before use.
- **Note:** The record is marked synthetic and its identifiers start with SYN-; they are treated as given.
- **Unresolved locator:** 2025-18469 (g) Table 1 rows for P/N 2A5001 (HPT 1st-stage hub) and P/N 2A4802 (HPT 2nd-stage hub)
- **Unresolved locator:** 2025-18469 preamble Discussion of Final Airworthiness Directive, responses to requests to add a terminating action and to supersede or cancel

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model PW1133G-JM is not one of the IAE V2500 models this screen supports, so no applicability determination is made against AD 2025-19-13 (Federal Register document 2025-18469), which is in force on the question date. No action is determined from this screen.
- **Note:** Engine model PW1133G-JM (asset SYN-ENG-004, serial SYN-PW1100-0004) is not among the IAE V2500 models this screen supports, so no applicability determination was made; nothing here is a compliance, airworthiness, or return-to-service finding.
- **Note:** The record lists no installed components and no events; they were not assessed because the engine is outside supported scope.
- **Note:** If the engine_model entry is a recording error and the engine is actually one of the listed IAE V2500 models, the record must be corrected and the screen rerun; this output does not extend to such an engine.
- **Note:** The record is marked synthetic (synthetic: true, with SYN- identifiers).
- **Note:** Federal Register document 2025-10764 (NPRM published 2025-06-13) preceded the final rule; it was not relied on, and the in-force text is final rule 2025-18469.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-19-13 (Federal Register 2025-18469, effective 2025-10-29) applies to this V2527E-A5 engine, and its installed HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 is listed in table 1 with a 3,900-cycle removal limit (the hub is at 1,040 cycles since new, so that limit is not reached). The 2025-11-12 induction at 18040 cycles, which the record flags as a qualifying engine shop visit after the effective date, is the trigger and no removal of the hub is recorded, so removal and replacement is due no later than engine flight cycle 18100, which is 100 flight cycles after the effective date.
- **Stated timing:** Due by engine flight cycle 18100: the later of the next qualifying engine shop visit (the 2025-11-12 induction at 18040 cycles) and 100 flight cycles after the 2025-10-29 effective date (18000 cycles plus 100); 60 cycles remain from the 18040 cycles on the snapshot.
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Missing fact:** No removal or replacement is recorded for P/N 2A4802 S/N PKLBSS9840; the record still lists it as installed, and the induction is dated the snapshot date. Whether it is removed at this visit or before 18100 cycles is unconfirmed and decides whether the removal step is still outstanding; any replacement must have a P/N and S/N not listed in table 1.
- **Missing fact:** The 1,040 cycles-since-new value is undated. It matches the 1,000 reading on 2025-10-29 plus the 40 engine cycles flown to 18040, but its as-of date is unconfirmed and the 2,860 cycles remaining depends on it.
- **Note:** Screening aid only, not a compliance determination. No removal of the listed hub is recorded as of the snapshot.
- **Note:** The 100-flight-cycle limb runs from the 2025-10-29 effective date, when the engine read 18000 cycles, so it ends at 18100; it is not counted from the publication date (2025-09-24), the question date, or the shop visit.
- **Note:** The later limb governs, so the deadline stays at 18100 even if other shop visits occurred between 2025-10-29 and 2025-11-12; none are recorded.
- **Note:** The qualifying-shop-visit flag is operator-asserted; the event detail matches paragraph (i)(2) and no exclusion is shown. The induction is dated the snapshot date, so the removal step may still be done during this visit.
- **Note:** The HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0005) shares a P/N with table 1 rows but its S/N is not listed, so it is not matched. Its installation date and dated cycle readings are not recorded, which does not affect this result.
- **Note:** The recorded installation of the 2nd-stage hub (2022-08-02) predates the effective date, so the installation prohibition in paragraph (h) is not triggered by that installation.
- **Note:** The NPRM 2025-10764 is a proposal and was not relied on; the final rule 2025-18469 is the operative text.
- **Note:** No ad_records or amoc_claims were supplied, so no operator AD status entry or AMOC was checked; this screen does not rely on either.
- **Note:** The record is synthetic (SYN- identifiers).
- **Unresolved locator:** 2025-18469 (g) Required Actions; Table 1 to Paragraph (g), HPT 2nd-stage hub 2A4802 / PKLBSS9840 row (3,900 cycles since new)
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub rows with P/N 2A5001

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
- **Summary:** AD 2025-19-13 (FR 2025-18469, effective 2025-10-29) applies to this V2531-E5 engine, and both installed hubs match Table 1: the HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) has 500 cycles left to its 4,800 removal limit and the HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) has 1,700 left to its 4,000 limit. Removal and replacement is due at the next engine shop visit, which must occur by engine flight cycle 30800 when the 1st-stage hub reaches its limit; under the 'whichever occurs later' wording the 100-flight-cycle point (30100), already passed, does not set the due point.
- **Stated timing:** At the next engine shop visit after the 2025-10-29 effective date and, in any case, before the HPT 1st-stage hub exceeds 4,800 cycles since new, which projects to engine flight cycle 30800 at one hub cycle per engine flight cycle; no engine shop visit is recorded since the effective date.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.
- **Missing fact:** The events list is empty, so the record does not show whether an engine shop visit has occurred since the 2025-10-29 effective date. An empty list is not evidence that no visit occurred. A visit after the effective date is the trigger under paragraph (g), so it must be confirmed to fix the due point and to check whether removal was already due at that visit.
- **Missing fact:** The 4,300 cycles-since-new value has no date of its own and is read as the count at the 2025-12-01 snapshot. It sets the 500-cycle remaining figure and the 30800 due point, so a dated reading would confirm it.
- **Missing fact:** No ad_records or amoc_claims entry for AD 2025-19-13 was supplied. Whether the operator claims a recorded status or an approved AMOC matters because an approved AMOC would change the route to compliance; any such claim would need checking against the approval and is not assumed here.
- **Note:** Screening aid only; this is not a compliance determination and says nothing about the engine's airworthiness or return-to-service status.
- **Note:** Authority: final rule 2025-18469 (AD 2025-19-13, Amendment 39-23153) is effective 2025-10-29 and so is in force on 2025-12-01. The June 2025 NPRM 2025-10764 was the proposal; the final rule adopted it with minor editorial changes and its Table 1 matches. The NPRM was not relied on.
- **Note:** Engine flight cycles: 30000 at 2025-10-29 (the effective date) and 30300 at 2025-12-01. The 100-flight-cycle point is 30100, which is earlier than the cycle-limit route, so under 'whichever occurs later' it does not set the due point.
- **Note:** Cross-check: measured from the effective date, the 1st-stage hub had 800 cycles left (4,000 to 4,800) at engine flight cycle 30000, which also gives 30800; the current 500-cycle figure agrees.
- **Note:** Projection: both hub counts rose 300 cycles (1st-stage 4,000 to 4,300; 2nd-stage 2,000 to 2,300) over the same 300 engine flight cycles. The 30800 and 32000 figures assume one hub cycle per engine flight cycle continues while installed on this engine; a change in utilization, hub removal, or a move to another engine requires recalculation.
- **Note:** The 2nd-stage hub (limit 4,000, 1,700 cycles left) would reach its limit at about engine flight cycle 32000. That is later than the 1st-stage hub and does not extend the engine-level due point, because one shop visit covers both parts.
- **Note:** No engine shop visit is recorded since the effective date, so the next shop visit is treated as not yet occurred. If a visit did occur after 2025-10-29 without the listed hubs being replaced, the removal would have been due at that visit and should be reviewed under paragraph (g).
- **Note:** The next shop visit's date is not in the record; the removal must be done by engine flight cycle 30800 at the latest, so the visit must be planned before then.
- **Note:** Installation history: both listed hubs were installed before the effective date (2021-05-11 and 2023-02-20), so no post-effective-date installation appears in the record; paragraph (h) still bars installing listed hubs in any engine.
- **Note:** Any replacement hub must have a P/N and S/N not listed in Table 1 to paragraph (g) (paragraph (i)(1)).
- **Note:** Engine and asset identifiers carry the SYN- synthetic prefix. No ad_records or amoc_claims entries were supplied, so no operator-asserted status or AMOC was checked or relied on.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), row HPT 1st-stage hub, P/N 2A5001, S/N PKLBSS9200, limit 4,800
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), row HPT 2nd-stage hub, P/N 2A4802, S/N PKLBST5005, limit 4,000
- **Unresolved locator:** 2025-18469 (i)(2) Definitions paragraph, with exceptions (i)(2)(i) and (i)(2)(ii)

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2528-D5 engine is within the AD's applicability, and the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST7489) matches a table 1 row with a 6,200-cycle removal limit, so removal and replacement is triggered at the next engine shop visit and before that hub exceeds 6,200 cycles since new (about engine flight cycle 54,200). The installed HPT 2nd-stage hub cannot be screened because its serial number and cycles since new are unknown, and the events list is empty, so no shop visit history is shown.
- **Stated timing:** At the next engine shop visit after the 2025-10-29 effective date, and in any case before hub S/N PKLBST7489 exceeds its 6,200 cycles-since-new limit; at the 2026-03-10 reading (engine flight cycle 50,500, hub at 2,500 cycles since new) that limit is 3,700 cycles away, about engine flight cycle 54,200. The within-100-flight-cycles date (engine flight cycle 50,100) is the earlier of the two clauses, so under 'whichever occurs later' it does not set the deadline.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** The HPT 2nd-stage hub (P/N 2A4802) has an unknown serial number. Table 1 lists four serials for that P/N (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100), so whether this hub is affected, and which removal limit applies, cannot be determined without the serial. An unknown record is not evidence that the hub is unaffected.
- **Missing fact:** Cycles since new are unknown, so the remaining cycles against the listed limit (4,000, 3,900, 5,000 or 6,000 depending on serial) cannot be computed. If the hub is listed and has less headroom than the 1st-stage hub, the latest engine flight-cycle figure and the remaining-cycles figure would change.
- **Missing fact:** The installation date of the HPT 2nd-stage hub is not recorded. If it was installed after 2025-10-29 and its P/N and S/N are listed in table 1, paragraph (h) would apply to that installation, so the date is needed together with the serial number.
- **Missing fact:** The events list is empty, so the record does not show whether any engine shop visit has occurred since the 2025-10-29 effective date or whether any event meets the paragraph (i)(2) definition. The next qualifying shop visit is the removal trigger, so the operator should confirm the shop visit history; if a qualifying visit occurred after 2025-10-29, it would need separate review against paragraph (g).
- **Missing fact:** The current 2,500 cycles-since-new value has no as-of date. It is consistent with the dated 2,000 reading at 2025-10-29 plus 500 engine cycles to 2026-03-10, but a dated confirmation as of the question date is needed because the 3,700-cycle remaining figure depends on it.
- **Note:** Screening aid only: this makes no compliance, airworthiness, or return-to-service determination. The record is marked synthetic.
- **Note:** 2025-18469 is a final rule effective 2025-10-29 under paragraph (a), so it is in force on 2026-03-10. The earlier NPRM 2025-10764 is a proposal that the final rule adopted with minor editorial changes; it was not relied on.
- **Note:** V2528-D5 is a supported model and is listed in the applicability paragraph (c).
- **Note:** Classed as action_required rather than action_required_on_event: removal is tied to the next engine shop visit, but the table 1 removal cycle limit gives a fixed outer date.
- **Note:** The 54,200 figure assumes the hub gains one cycle per engine flight cycle. The hub's cycles since new went from 2,000 at 2025-10-29 to 2,500 while engine cycles went from 50,000 to 50,500, which supports that assumption. The table limit is in hub cycles since new, while the deadline is expressed in engine flight cycles.
- **Note:** The 1st-stage hub was installed 2024-06-03, before the effective date, so paragraph (h) does not by itself require earlier removal. Paragraph (h) bars any later installation of a listed hub in any engine, including reinstallation after removal.
- **Note:** The HPT 2nd-stage hub (P/N 2A4802) is not matched and is not assessed as affected or unaffected. If its serial proves to be one of the four listed serials, its removal limit could move the latest date earlier than 54,200 and could reduce the remaining-cycles figure below 3,700.
- **Note:** The 100-flight-cycle date (50,100) had passed by the 50,500 reading. Under 'whichever occurs later' the shop-visit clause, capped by the removal limit, controls. The reading that treats 50,100 as fixed is in alternative_readings for reviewer confirmation.
- **Note:** No ad_records or amoc_claims entries appear in the record, so the screen relies on no operator AD status entry and no AMOC claim.
- **Note:** The events list is empty, so the record cannot confirm whether a shop visit occurred after 2025-10-29; if one did, the removal requirement at that visit would need separate review.
- **Unresolved locator:** 2025-18469 (g) Required Actions paragraph and Table 1 to paragraph (g): HPT 1st-stage hub row 2A5001 / PKLBST7489 with 6,200 limit; HPT 2nd-stage hub rows for P/N 2A4802

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** AD 2025-19-13 (FR doc 2025-18469, effective 2025-10-29) is in force on 2026-09-26 and covers IAE AG V2522-A5 engines, so this engine is within its applicability. Whether removal of a table 1 HPT 1st- or 2nd-stage hub is triggered cannot be decided because the record lists no installed hubs, no engine flight-cycle counter and no events, so the screen needs review.
- **Stated timing:** If an installed table 1 hub is confirmed, remove it and replace it with a part eligible for installation at the next engine shop visit after 2025-10-29 before its removal cycle limit is exceeded, or within 100 flight cycles after 2025-10-29, whichever occurs later; no calendar or cycle date can be computed from this record.
- **Missing fact:** No HPT 1st-stage hub record exists because installed_components is empty. Installed P/N, S/N and cycles since new are needed to test against the four table 1 P/N 2A5001 pairs, which decides whether paragraph (g) removal is triggered; an absent record is not evidence that no affected hub is installed.
- **Missing fact:** No HPT 2nd-stage hub record exists. Installed P/N, S/N and cycles since new are needed to test against the four table 1 P/N 2A4802 pairs, which decides whether paragraph (g) removal is triggered.
- **Missing fact:** Engine flight-cycle counter at the 2025-10-29 effective date, needed as the baseline for the 100-flight-cycle point in paragraph (g).
- **Missing fact:** Current engine flight-cycle counter; the snapshot contains none. Needed to compare with hub cycle limits and to tell whether the 100-cycle point has passed.
- **Missing fact:** No events are recorded, so it is unknown whether an engine shop visit (paragraph (i)(2)) has occurred since 2025-10-29 or is scheduled; paragraph (g) ties removal to the next engine shop visit after the effective date, and no event has been assessed for qualifies_as_engine_shop_visit.
- **Note:** Screening aid only; this is not a compliance determination. The record is marked synthetic (SYN- identifiers). No correction or superseding document was supplied.
- **Note:** Authority: final rule FR doc 2025-18469 (published 2025-09-24; AD 2025-19-13, Amendment 39-23153) is effective 2025-10-29 and in force on the question date. The NPRM (FR doc 2025-10764, published 2025-06-13) preceded it; the final rule adopted it except for minor editorial changes, and the NPRM was not relied on.
- **Note:** Applicability is by engine model only (paragraph (c)). The FAA declined in the preamble to narrow applicability to engines with listed hub serial numbers, so this V2522-A5 is within scope whether or not a table 1 hub is installed.
- **Note:** Table 1 pairs (P/N and S/N must both match): P/N 2A5001 with S/N PKLBSK9287 (limit 100), PKLBSS9200 (4,800), PKLBST5011 (5,500), PKLBST7489 (6,200); P/N 2A4802 with S/N PKLBST5005 (4,000), PKLBSS9840 (3,900), PKLBSS0301 (5,000), PKLBSR2100 (6,000). Limits are the hub's cycles since new, not engine flight cycles, so neither latest_engine_flight_cycles nor component_cycles_remaining can be computed.
- **Note:** installed_components and events are empty. Under the screening conventions an empty list is not evidence that no table 1 hub is installed or that no shop visit has occurred since the effective date.
- **Note:** Timing: the paragraph (g) date is the later of the next engine shop visit after 2025-10-29 (which must come before the hub's removal cycle limit is exceeded) and the 100-flight-cycle point after 2025-10-29. The question date is almost eleven months after the effective date, so the 100-cycle point may already have passed for this engine; the record cannot show this. The phrase 'whichever occurs later' could be read in more than one way, but without cycle data no reading yields an integer deadline, so alternative_readings is empty.
- **Note:** Paragraph (h) binds regardless of the (g) outcome: no table 1 hub may be installed in any engine after 2025-10-29. No installation history is recorded to test against it.
- **Note:** No ad_records or amoc_claims entries for AD 2025-19-13 appear in the record, so there is no operator AD status claim or AMOC claim to check; none is relied on here.
- **Note:** Under paragraph (i)(2), an engine shop visit excludes flange separation solely for transportation without subsequent engine maintenance and engine removal for field maintenance at a maintenance facility in lieu of on-wing work. No event is recorded, so no event has been assessed against that definition.

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model V2500-A1 is not among the V2500 models this screen supports for AD 2025-18469, so the screen makes no applicability determination and states no action, timing, or cycle count. The final rule, effective October 29, 2025, is in force on the question date of September 26, 2026.
- **Note:** Scope gate: engine_model V2500-A1 is not one of the ten supported models (V2522-A5, V2524-A5, V2525-D5, V2527-A5, V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2531-E5, V2533-A5), so applicability is outside_supported_scope and action_status is none.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011) has identifiers that also appear in Table 1 to paragraph (g). This is noted for awareness only; no cycles-remaining figure, deadline, or status is derived from it.
- **Note:** If the engine_model entry is a recording error, the engine should be re-screened against the corrected model using its installed part data; nothing in this answer anticipates that result.
- **Note:** Paragraph (h) says 'in any engine'; the preamble response on applicability states the installation prohibition applies to models listed in the Applicability paragraph, so this screen does not read (h) as reaching V2500-A1.
- **Note:** Authority: 2025-18469 is a final rule effective 2025-10-29 and is in force on 2026-09-26. The June 13, 2025 NPRM (2025-10764) was not relied on.
- **Note:** The events list is empty and the record is marked synthetic (SYN- identifiers); the answer applies only to the record as supplied.
- **Note:** This is a screening aid, not a compliance determination.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row for P/N 2A5001 and S/N PKLBST5011

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The directive is in force (effective 2026-09-24) and applies because the installed 3rd stage HPC rotor blade set carries P/N 6A8353 on a listed V2527-A5 engine. Its full-set blade replacement is required only at the next engine shop visit after 2026-09-24 where a 3rd stage blade is exposed, and the record shows no events, so no action is triggered as of 2026-10-05.
- **Stated timing:** No fixed calendar or cycle deadline. The full-set replacement is due at the next engine shop visit (induction of the engine into the shop for maintenance) after the 2026-09-24 effective date at which any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum. No such event is recorded as of 2026-10-05.
- **Expected timing:** Conditional. At the next engine shop visit inducted after 2026-09-24 where any 3rd-stage HPC blade is removed from the stage 3-8 drum, replace the full set with eligible parts. No cycle or calendar limit applies.
- **Missing fact:** The events list is empty, so the record shows no engine shop visit after the 2026-09-24 effective date and does not confirm whether any 3rd stage HPC rotor blade was removed from the HPC stage 3 to 8 drum at a shop visit. That event would trigger the full-set replacement, so the empty list is treated as no recorded event, not as proof that none occurred.
- **Note:** Screening aid only; it does not record or settle the operator's AD status.
- **Note:** V2527-A5 is on the supported model list and in the directive's applicability list, so the screen is within scope.
- **Note:** Applicability turns on the listed P/N. The set-level serial 'not tracked at set level' does not affect applicability, and the full-set replacement does not need blade-level serials to be triggered; blade-level P/N and serial records would be needed later to document the replacement and the eligible parts installed.
- **Note:** Authority: final rule 2026-16954 is effective 2026-09-24, before the question date. Correction 2026-18423, published 2026-09-10 and also effective 2026-09-24, adds the omitted word 'blade' in paragraph (g); the shop-visit trigger and full-set scope are the same under either wording.
- **Note:** The November 2025 NPRM proposed replacement at the next 3rd stage blade exposure with no shop-visit limit; the final rule replaced that trigger with engine shop visit wording, so the proposal is not relied on.
- **Note:** The wording readings considered (shop-visit trigger versus the NPRM, and 'rotor' versus 'rotor blade' in the original paragraph (g)) give no fixed cycle or calendar deadline, so alternative_readings is empty.
- **Note:** The engine record has no engine flight-cycle counter; none is needed because this AD sets no cycle or calendar limit, so latest_engine_flight_cycles and component_cycles_remaining are null.
- **Note:** If a later record shows an engine shop visit after 2026-09-24 in which a 3rd stage blade was removed from the HPC stage 3 to 8 drum, the full-set replacement would be due at that visit and the action status would become action_required.
- **Note:** No ad_records or amoc_claims entries were supplied, so no operator AD status or AMOC claim was checked or relied on. The record is synthetic (synthetic: true; SYN- identifiers).
- **Unresolved locator:** 2026-16954 (i)(2) (i)(2) AMOC notification

Forbidden claims for this case:

- The blades must be replaced by a cycle or calendar deadline.
- The engine is noncompliant because the blades are still installed.
- Replacing only the exposed blades satisfies the AD.

## seed-012: Later-standard 3rd-stage HPC blades installed

- **Fields:** applicability `does_not_apply`, action_status `None`, authority `in_force`
- **Expected:** applicability `does_not_apply`, action_status `None`
- **Summary:** AD 2026-17-03 (final rule 2026-16954, effective 2026-09-24, with paragraph (g) corrected by 2026-18423) was in force on 2026-10-05, but the only recorded 3rd stage HPC rotor blade set is P/N 6C8368, which the AD lists as a part eligible for installation rather than as an applicable P/N 6A8353 or 6A8688, so the directive does not apply on this record.
- **Missing fact:** Serial is not tracked at set level, so the record does not show individual blade P/Ns. This screen takes the set-level P/N 6C8368 as the P/N of every blade in the set. Blade-level confirmation that no 6A8353 or 6A8688 blade is installed would close this point; the record as given shows no such blade.
- **Note:** Model V2533-A5 is on the supported list, so the screen proceeds.
- **Note:** Authority: final rule 2026-16954 became effective 2026-09-24 and was in force on 2026-10-05. The NPRM 2025-20088 is superseded and was not relied on. Correction 2026-18423, published 2026-09-10 before the question date, only fixes paragraph (g) wording and does not change applicability.
- **Note:** The engine's only installed blade component is recorded at P/N 6C8368, a replacement P/N under paragraph (h)(1)(i) and not one of the applicability P/Ns 6A8353 or 6A8688 in paragraph (c). It was not treated as a match, so matched_parts is empty.
- **Note:** The set serial is not tracked. The directive matches on part number only, so the missing serial does not by itself block the screen, but the result assumes the set-level P/N applies to every blade in the set.
- **Note:** Conditional only: if the record showed 6A8353 or 6A8688 blades installed, paragraph (g) would require full-set replacement at the next engine shop visit after 2026-09-24 where a blade is exposed. That would be action_required_on_event with no cycle-based deadline. The events list is empty, so no shop visit or blade exposure is recorded, and no flight-cycle counter is supplied.
- **Note:** No ad_records or amoc_claims are in the record; none were used. The record carries synthetic SYN- identifiers.
- **Note:** This is a screening aid for the directive, not a compliance determination.

Forbidden claims for this case:

- AD 2026-17-03 applies to this engine.
- The blades must be replaced at the next shop visit.

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** The V2530-A5 record shows 3rd stage HPC rotor blade P/N 6A8688 installed, which is within the directive's applicability, and the directive has been in force since its September 24, 2026 effective date. The only shop visit, inducted 2026-09-14, predates that effective date, so its blade removal does not trigger the full-set replacement; the requirement attaches only to a future engine shop visit inducted after the effective date in which a 3rd stage HPC rotor blade is exposed.
- **Stated timing:** No calendar or cycle deadline. Action is due at the next engine shop visit inducted after the 2026-09-24 effective date in which a 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum; the visit inducted 2026-09-14 predates the effective date and does not trigger it.
- **Expected timing:** Replacement is not required during the visit inducted 2026-09-14. It is required at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The 2026-09-14 induction date is operator-asserted and is the only fact placing the blade-exposing visit before the 2026-09-24 effective date. Confirm it from shop induction records. If the induction were after the effective date, that visit would be the next engine shop visit after the effective date with a blade exposure, and paragraph (g) would require full-set replacement.
- **Note:** Screening aid only: this is not a compliance determination and does not assess blade condition or serviceability.
- **Note:** Paragraph (g) is taken from document 2026-18423, which corrects 2026-16954 by restoring the omitted word 'blade' and leaves the effective date unchanged; both documents predate the 2026-09-30 question date.
- **Note:** The 2026-09-30 component_exposure entry falls after the effective date, but its detail places the blade removal during the visit inducted 2026-09-14. Paragraph (g) keys on the induction date of the shop visit, so the exposure date does not by itself trigger the requirement; the preamble says it is not the FAA's intent to require engines inducted before the effective date to comply.
- **Note:** Alternative reading not adopted: treating the 2026-09-30 exposure as the trigger would make replacement due before this engine leaves the current shop visit. That reading conflicts with the 'after the effective date' wording and the preamble intent statement. No cycle count can be computed for it, so it is described here rather than in alternative_readings.
- **Note:** The operator's qualifies_as_engine_shop_visit 'yes' flag for AD 2026-17-03 on the 2026-09-14 induction matches the paragraph (h)(3) definition on its face; the induction date, not the flag, controls the timing.
- **Note:** The directive sets no flight-cycle or calendar limit, and the record has no engine flight-cycle counter or blade cycle data, so latest_engine_flight_cycles and component_cycles_remaining are null.
- **Note:** installed_components lists the 6A8688 blade set at the 2026-09-30 snapshot even though a blade was removed from the drum during the visit; the screen treats the set as installed for applicability, consistent with the record.
- **Note:** The record does not show whether the 2026-09-14 visit has closed or when the engine returns to service; this does not change the result, because the trigger is the induction date of a later visit.
- **Note:** The record has no ad_records or amoc_claims entry for AD 2026-17-03, so no AMOC is claimed or relied on. The preamble says paragraph (i)(1) lets an operator request an AMOC to extend the compliance time if eligible parts are not available in a timely manner.
- **Note:** The preamble describes replacement per IAE AG SB V2500-ENG-72-0716 (dated October 4, 2024) as a way to satisfy the replacement requirement, because it changes part numbers to those in the part-eligible definition. That service bulletin is not in the record and was not applied.
- **Note:** NPRM 2025-20088 proposed a trigger at any blade exposure after the effective date. The final rule replaced it with the engine shop visit trigger; the NPRM text was not relied on.
- **Note:** Blade serial numbers are not tracked at set level in the record. A future exposure entry should record the set P/N and the P/N of any replacement blades so they can be checked against the part-eligible definition.

Forbidden claims for this case:

- AD 2026-17-03 requires replacing the blades during the current shop visit.
- The engine is no longer subject to AD 2026-17-03 after this visit.

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **No answer:** answer is not JSON: Unterminated string starting at: line 1 column 4910 (char 4909)

## seed-015: Asked while only the proposed rule existed

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `proposed`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** Proposed NPRM 2025-20088 would cover this supported V2527E-A5 engine because its recorded 3rd stage HPC rotor blade set carries P/N 6A8353, but it is a proposed rule with no effective date, so it cannot yet require the blade-set replacement and no action is triggered on the 2026-01-15 record.
- **Stated timing:** No required action is due on the current record because the directive is only proposed and has no effective date; if adopted as proposed, full blade-set replacement would fall due at the next 3rd stage HPC rotor blade exposure after the AD's effective date.
- **Missing fact:** No final rule, effective date, or superseding document for docket FAA-2025-2555 is in the supplied materials; the only document is an NPRM with effective date none. Needed because only an in-force AD can require action, and the effective date sets when a future blade exposure would trigger the replacement.
- **Missing fact:** The events list is empty, so no 3rd stage HPC rotor blade exposure (any blade removed from the HPC stage 3 to 8 drum) is recorded. Needed to establish whether an exposure has occurred and whether it falls after the effective date once one is published. An empty list is not evidence that no exposure occurred.
- **Missing fact:** Serial number is recorded only as not tracked at set level, and no blade-level part number or serial entries exist. The proposed applicability is by part number, so this does not change the current match, but blade-level records would be needed to confirm which blades are P/N 6A8353 or 6A8688 and whether any is already an eligible part (P/N 6C8368, 6C8403, or later approved P/N) if the replacement later becomes due.
- **Note:** This is a screening aid, not a compliance determination, and makes no airworthiness or return-to-service finding.
- **Note:** Supported model check: V2527E-A5 is on the screen's supported list and in the NPRM's model list.
- **Note:** The only document supplied is NPRM 2025-20088 (proposed rule published 2025-11-18, effective date none). It is not in force on 2026-01-15 and cannot require action; its comment period closed January 2, 2026. The screen reflects only the supplied materials, so confirm the docket status before relying on it.
- **Note:** Proposed paragraph (g) would bind only after the AD is in force, so no continuing obligation is binding now and continuing_obligations is empty.
- **Note:** If the proposal is adopted without change, the requirement becomes event-triggered (next blade exposure after the effective date) and the engine should be re-screened against the final text and effective date.
- **Note:** The events list is empty. That means no exposure is recorded, not that none occurred, and it does not show whether any blade was removed from the HPC stage 3 to 8 drum.
- **Note:** The directive matches on part number only. The single set-level entry (P/N 6A8353) satisfies the proposed applicability text as recorded; blade-level records would be needed for any future eligibility check.
- **Note:** No engine flight-cycle counter appears in the record. Cycle fields are null because the proposed trigger is an exposure event with no effective date, and the proposal sets no cycle limit.
- **Note:** The record has no ad_records or amoc_claims entries and is marked synthetic (SYN- identifiers); neither changes the outcome while the proposal is not in force.
- **Unresolved locator:** 2025-20088 preamble Header block (Type: Proposed Rule; Effective date: none) and DATES section

Forbidden claims for this case:

- An airworthiness directive currently requires replacing the blades.
- The blades must be replaced at the next exposure.
- Final-rule terms (the shop-visit trigger or the 2026-09-24 effective date) apply on 2026-01-15.

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** AD 2025-17-16 (FR 2025-17066) is in force and applies to this V2527-A5 engine. The required revision of paragraph B.1 of the V2500-A5 TLM ALS and, for air carrier operations, of the approved maintenance program to add the table 1 HPT stage 1 and stage 2 hub inspection tasks is not yet recorded as incorporated and falls due by January 8, 2026.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e. on or before January 8, 2026 (54 calendar days after the 2025-11-15 question date).
- **Expected timing:** By 2026-01-08, revise paragraph B.1 of the ALS in the V2500-A5 Time Limits Manual (P/N 2A4408) per table 1, and revise the approved maintenance or inspection program. The table 1 inspections are then scheduled at piece-part exposure. This AD does not require performing them within 90 days.
- **Missing fact:** installed_components is an empty list, so the installed part and serial numbers of the HPT 1st-stage hub are unknown; table 1 lists P/N 2A5001 with TASK 72-45-11-200-006. This does not change the TLM and program revisions, which the screen reads as tied to the listed engine model, but it is needed to confirm whether this hub's inspection applies at piece-part exposure. An absent record is not evidence that the hub is absent or unaffected.
- **Missing fact:** No installed-component record is supplied for the HPT 2nd-stage hub, so its installed part and serial numbers are unknown; table 1 lists P/N 2A4802 with TASK 72-45-31-200-009. This is needed to confirm whether the stage 2 hub inspection applies at piece-part exposure.
- **Missing fact:** The text of TLM paragraph B.1 and of tasks 72-45-11-200-006 and 72-45-31-200-009 (inspection content and any thresholds) is not among the materials supplied; it governs how the table 1 inspections are performed once a hub is exposed, but this screen does not assess it.
- **Note:** Screening aid only; this output does not determine the engine's AD status, airworthiness, or return-to-service eligibility.
- **Note:** The operator's statement that neither the approved program (Revision 47, 2025-06-01) nor TLM paragraph B.1 yet incorporates table 1 is an operator assertion taken from the record and was not verified.
- **Note:** Deadline basis: the 90-day periods run from the October 10, 2025 effective date stated in the final rule, not the September 5, 2025 publication date (which would have given December 4, 2025); no alternative reading is listed because the text ties the periods to the effective date.
- **Note:** The engine record has no flight-cycle counter and the revision deadline is calendar-based, so latest_engine_flight_cycles and component_cycles_remaining are null.
- **Note:** Paragraph (g) says 'as applicable' in (g)(1) and (g)(2). This screen reads the TLM and program revisions as required for the listed engine model regardless of installed hub part numbers, because the preamble requires both tasks in the operator's EMM regardless of its version and table 1 has no model or serial column. If a reviewer reads 'as applicable' as limiting table 1 to hub part numbers installed on this engine, the missing hub records would decide scope and the status would need review.
- **Note:** Piece-part exposure: events is empty and no installed components are recorded, so the record does not show whether either hub has been or will be exposed. Once the revisions are made, each piece-part exposure of a table 1 hub would call for the matching table 1 inspection; that obligation is event-driven and the directive sets no separate calendar deadline for it.
- **Note:** NPRM 2024-26092 listed TASK 72-45-11-200-009 for the stage 2 hub; the final rule corrected this to TASK 72-45-31-200-009. This screen relies only on final rule 2025-17066.
- **Note:** The engine record supplies no ad_records or amoc_claims entries, so no operator statement is treated as an approved alternative method.
- **Note:** As of 2025-11-15 the revision is outstanding per the operator's record, with 54 calendar days left before the January 8, 2026 due date.
- **Note:** V2527-A5 is on the supported model list and matches paragraph (c); the record is marked synthetic and its identifiers are synthetic.

Forbidden claims for this case:

- AD 2025-17-16 requires inspecting the HPT hubs within 90 days.
- The V2500-D5 or V2500-E5 Time Limits Manual applies to this engine.
- Only paragraph (g)(1) applies.

## seed-017: A5 engine where air-carrier status is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The V2522-A5 is within the applicability of AD 2025-17-16, which has been in force since its October 10, 2025 effective date, so the paragraph (g)(1) revision that adds the HPT Stage 1 and Stage 2 hub inspection tasks to the TLM airworthiness limitations section is due by January 8, 2026. The operator air-carrier status and the installed hub component records are missing, so whether the paragraph (g)(2) program revision applies and whether either listed hub is installed cannot be determined from this record.
- **Stated timing:** Within 90 days after the October 10, 2025 effective date, i.e. by January 8, 2026, for the paragraph (g)(1) TLM revision; the paragraph (g)(2) program revision has the same date but applies only to air carrier operations.
- **Expected timing:** By 2026-01-08, revise the ALS in the V2500-A5 TLM (P/N 2A4408). Whether a program revision by the same date is also required depends on air-carrier status.
- **Missing fact:** Air-carrier status is unknown, so it cannot be determined whether the paragraph (g)(2) revision of the existing approved maintenance or inspection program applies; (g)(2) carries the same January 8, 2026 date. The paragraph (g)(1) TLM revision applies regardless of this value.
- **Missing fact:** No recorded AD status for 2025-17-16 is supplied, so the record does not show whether the paragraph (g)(1) TLM revision, or the paragraph (g)(2) program revision if it applies, has been done. A missing record is not evidence either way.
- **Missing fact:** No installed component record for the HPT Stage 1 Hub (P/N 2A5001 in Table 1) is supplied, so whether this part is installed, and its part and serial numbers, cannot be matched; whether the TASK 72-45-11-200-006 inspection applies at piece-part exposure depends on it.
- **Missing fact:** No installed component record for the HPT Stage 2 Hub (P/N 2A4802 in Table 1) is supplied, so whether this part is installed, and its part and serial numbers, cannot be matched; whether the TASK 72-45-31-200-009 inspection applies at piece-part exposure depends on it.
- **Missing fact:** The operator's existing TLM for the V2500-A5 (P/N 2A4408, TASK 05-10-00-990-000-B00) and its Maintenance Scheduling paragraph B.1 are not in the record or the supplied documents, so the TLM revision level and whether the Table 1 tasks are already present cannot be confirmed.
- **Note:** Screening aid only: this is not a compliance determination, and nothing here states that the engine or any part is compliant, airworthy, or approved for return to service.
- **Note:** The 90 days run from the October 10, 2025 effective date in paragraph (a), not the September 5, 2025 publication date; the effective date itself is not counted, so day 90 is January 8, 2026.
- **Note:** The deadline is calendar-based, so no flight-cycle deadline is computed; the record also has no engine flight-cycle counter.
- **Note:** As of the November 15, 2025 question date the deadline has not passed; the record does not show whether the revision has been made, and no ad_records or amoc_claims entry for this AD is supplied.
- **Note:** Paragraph (g)(1) has no air-carrier limit, so it is treated as applying to the operator regardless of air-carrier status; only (g)(2) turns on that unknown value.
- **Note:** The V2522-A5 is taken to fall under the V2500-A5 TLM line in paragraph (g)(1)(i) (P/N 2A4408) by model family; the operator's actual TLM and its revision level are not in the record and should be confirmed.
- **Note:** installed_components and events are both empty lists. Neither shows that a hub is absent or that no piece-part exposure occurred; the hub inspections are tied to piece-part exposure under the revised TLM, so the record cannot show whether or when they fall due. matched_parts is therefore empty.
- **Note:** The 20,000-flight-cycle replacement figure appears only in a commenter's description of the operator's maintenance program (AMP section 18) in the preamble, not in the AD text; it is not used, and component_cycles_remaining is null because no component record is supplied and the AD sets no cycle limit.
- **Note:** The superseded NPRM 2024-26092 gave the Stage 2 hub task as TASK 72-45-11-200-009; the final rule corrected it to TASK 72-45-31-200-009, and this screen relies only on the final rule text.
- **Note:** The record is synthetic (SYN- identifiers), and the screen uses only the supplied record and the directive text.
- **Unresolved locator:** 2025-17066 (g)(1) Required Action and sub-items (i) to (iii)
- **Unresolved locator:** 2025-17066 (g)(1) Table 1 to Paragraph (g), rows HPT Stage 1 Hub and HPT Stage 2 Hub

Forbidden claims for this case:

- Paragraph (g)(2) does not apply to this engine.
- Paragraph (g)(2) applies to this engine, presented as settled.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** AD 2025-19-13 (Federal Register document 2025-18469) covers V2525-D5 engines, and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100, 990 cycles since new against a 6,000-cycle removal limit) is a listed part, but the final rule is not effective until 2025-10-29, so no action is triggered on 2025-10-15. The removal due date cannot be fixed because the record shows no engine shop visit and no engine flight-cycle count.
- **Stated timing:** Not triggered on 2025-10-15. From the 2025-10-29 effective date, the matched HPT 2nd-stage hub must be removed at the next engine shop visit after 2025-10-29, before it exceeds 6,000 cycles since new, or within 100 flight cycles after 2025-10-29, whichever occurs later. No shop visit is recorded, so the due date is not fixed.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.
- **Missing fact:** The record has no engine flight-cycle counter. The 100-flight-cycle period starts on the 2025-10-29 effective date and the shop-visit alternative is tied to cycle limits, so the engine counter at the snapshot, and the flights accrued before and after 2025-10-29, is needed to state the due date as an engine flight-cycle number. The hub's 990 cycles since new are part cycles and cannot substitute for the engine counter.
- **Missing fact:** No engine shop visit is recorded, past or planned, and no event carries a qualifies_as_engine_shop_visit determination for this AD. The next engine shop visit after 2025-10-29, and the engine flight cycles at that visit, set the removal date under paragraph (g). An absent record is not evidence that no shop visit will occur.
- **Note:** Screening aid only. This does not determine AD status for this engine or any part.
- **Note:** Authority: Federal Register document 2025-18469 (final rule, AD 2025-19-13) was published 2025-09-24 with an effective date of 2025-10-29. On the 2025-10-15 question date it is published_not_yet_effective and cannot yet require action. The NPRM (2025-10764) was not relied on; the final rule text governs.
- **Note:** Scope: V2525-D5 is on the supported model list and within paragraph (c), so the applicability screen returns applies.
- **Note:** Matched part: the HPT 2nd-stage hub (P/N 2A4802, S/N PKLBSR2100) is in table 1 with a removal cycle limit of 6,000 cycles since new. At the 2025-10-15 snapshot it has 990 cycles since new, leaving 5,010; that figure falls as the hub accrues cycles, including cycles flown before 2025-10-29, and the record gives no later count.
- **Note:** Not matched: the HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0018, 2,000 cycles since new) shares a listed P/N, but its S/N is not one of the four 1st-stage S/Ns in table 1, so no table limit applies on this record. If the recorded S/N is wrong, rerun the screen.
- **Note:** Due-date rule: under paragraph (g), removal is due at the later of (a) the next engine shop visit after 2025-10-29, which must occur before the hub exceeds 6,000 cycles since new, and (b) 100 flight cycles after 2025-10-29. A shop visit before 2025-10-29 is not the trigger. Because the engine flight-cycle counter is absent, no engine flight-cycle number can be given.
- **Note:** Once effective, paragraph (h) bars installing the listed hub S/N PKLBSR2100 in any engine, so a hub removed under paragraph (g) cannot be reinstalled.
- **Note:** Shop visit test under paragraph (i)(2): induction of an engine into the shop involving separation of major mating H-P flanges, excluding flange separation solely for transportation and removal for field maintenance at a maintenance facility in lieu of on-wing work. No event is recorded, so the test cannot yet be applied.
- **Note:** No ad_records or amoc_claims entries are in the record, so no operator AD status claim or alternative-method claim was relied on or assessed.
- **Note:** The engine record is flagged synthetic; SYN- identifiers were treated as supplied values.
- **Unresolved locator:** 2025-18469 preamble Header effective date 2025-10-29; DATES: effective October 29, 2025
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g): HPT 1st-stage hub rows with P/N 2A5001

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive applies to this V2531-E5 engine, and its installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) is a Table 1 listed part whose recorded 4,990 cycles since new already exceed its 4,800 removal limit, so paragraph (g) requires removal and replacement no later than engine flight cycle 60100 (100 flight cycles after the 2025-10-29 effective date). The installed HPT 2nd-stage hub has a listed P/N, but its recorded S/N SYN-HUB2-0019 is not in Table 1, so it is not matched on this record.
- **Stated timing:** Remove the HPT 1st-stage hub (P/N 2A5001, S/N PKLBSS9200) and replace it with a part eligible for installation no later than engine flight cycle 60100, which is 100 flight cycles after the 2025-10-29 effective date (engine reading 60000). The 2025-11-05 engine reading of 60040 leaves 60 flight cycles. The shop-visit prong of paragraph (g) requires removal before the 4,800-cycle limit is exceeded, and the recorded cycles since new already exceed that limit, so the 100-flight-cycle bound governs.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.
- **Missing fact:** The 4,990 cycles-since-new value for the HPT 1st-stage hub is undated; the only dated reading is 4,950 at 2025-10-29. A dated reading at the 2025-11-05 snapshot would confirm the current count behind the -190 remaining figure. Either value already exceeds the 4,800 limit, so the required action does not depend on it.
- **Missing fact:** The HPT 2nd-stage hub is not matched only because its recorded S/N SYN-HUB2-0019 is not among the four listed S/Ns for P/N 2A4802. Confirm the recorded S/N is the hub's actual serial number; if it were a listed S/N (PKLBST5005, PKLBSS9840, PKLBSS0301 or PKLBSR2100), the hub would be affected and its 4,990 cycles would have to be compared with that row's limit.
- **Note:** Screening aid only, built from the directive text and the supplied record; it is not the operator's AD status record.
- **Note:** Authority: Federal Register 2025-18469 (final rule, AD 2025-19-13) took effect 2025-10-29 and was in force on the 2025-11-05 question date. The June 2025 NPRM 2025-10764 was the proposal the final rule adopted with minor editorial changes; the final rule text governs and the NPRM is not relied on.
- **Note:** Window: the 100-flight-cycle period runs from the 2025-10-29 effective date (engine reading 60000), not from the 2025-09-24 publication or 2025-09-19 issuance dates; flight cycles are measured with the engine flight-cycle counter, the only flight-cycle count in the record.
- **Note:** The record does not show when the hub passed 4,800 cycles since new; it read 4,950 on 2025-10-29 and reads 4,990 now. Because the shop-visit prong cannot be met, no later shop visit can move the deadline past 60100, and no reading of the text on this record yields a different computable deadline.
- **Note:** No engine events are recorded (events is empty), so no shop visit or qualifies_as_engine_shop_visit determination is available. A shop visit before cycle 60100 would be a practical point to remove the hub, but the deadline stays at 60100.
- **Note:** The hub's undated 4,990 and its 4,950 reading at 2025-10-29 differ by 40 cycles, matching the 40-cycle engine increase from 60000 to 60040, so 4,990 is taken as the 2025-11-05 value.
- **Note:** HPT 2nd-stage hub: a P/N-only match is not enough, because paragraphs (g) and (h) require both P/N and S/N to match. Its recorded S/N SYN-HUB2-0019 is not listed, so no action is triggered for this hub on this record, and its 4,990 cycles are not compared with any Table 1 limit.
- **Note:** Once the 1st-stage hub is removed, paragraph (h) bars installing it (P/N 2A5001, S/N PKLBSS9200) in any engine, and the replacement must be a hub whose P/N and S/N are not listed in Table 1 (paragraph (i)(1)).
- **Note:** The record has no ad_records or amoc_claims entries, so no operator-asserted AD status or alternative method of compliance was considered. Identifiers starting with SYN- are synthetic and were treated as recorded.
- **Unresolved locator:** 2025-18469 (g) Required Actions, first sentence
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row: 2A5001, PKLBSS9200, 4,800
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub rows: P/N 2A4802 with S/Ns PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `published_not_yet_effective`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (Federal Register document 2022-02574) is published but not effective until 2022-03-15, so it cannot require action on the 2022-03-01 question date. The V2533-A5 is a supported model and both installed disks carry the directive's part numbers, but applicability turns on whether their serial numbers are listed in the NMSB Appendix A tables and the Figure 1 compliance time is not in the supplied text, so the screen needs review.
- **Stated timing:** Not due on 2022-03-01; the directive takes effect 2022-03-15. If it applies once effective, each affected disk's USI is due at the later of the Figure 1 to paragraph (g)(1) compliance time and 10 flight cycles after 2022-03-15; the Figure 1 time is not in the supplied text, so no due date can be set.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or Table 1 of IAE NMSB V2500-E5-72-0015 Rev 1, the alternative cited in paragraph (c)(1)) is not in the supplied text; without it, it cannot be confirmed whether the 1st-stage disk S/N SYN-DISK1-0020 is listed, which decides applicability under paragraph (c)(1).
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Rev 1 (or Table 2 of IAE NMSB V2500-E5-72-0015 Rev 1, cited in paragraph (c)(2)) is not in the supplied text; without it, it cannot be confirmed whether the 2nd-stage disk S/N SYN-DISK2-0020 is listed, which decides applicability under paragraph (c)(2).
- **Missing fact:** Figure 1 to paragraph (g)(1) (an image not included in the supplied text) sets the USI compliance time for both disks and may depend on engine shop visits, HPT module removals or disk cycles, none of which the record shows; without it no latest due date can be computed.
- **Missing fact:** The record has no engine flight-cycle counter; it is needed to express the limit of 10 FCs after the 2022-03-15 effective date, and any cycle-based Figure 1 time, as an engine flight-cycle number.
- **Missing fact:** Accumulated flight cycles of the 1st-stage disk are not recorded; needed only if Figure 1 counts cycles on the disk.
- **Missing fact:** Accumulated flight cycles of the 2nd-stage disk are not recorded; needed only if Figure 1 counts cycles on the disk.
- **Note:** Synthetic record (SYN- identifiers); the screen uses the record as supplied. V2533-A5 is within the supported model list. Screening aid only; no determination is made about any engine or part.
- **Note:** The question date (2022-03-01) precedes the 2022-03-15 effective date, so 2022-02574 cannot require action on the question date; it binds only if it applies once effective.
- **Note:** Applicability depends on serial numbers: paragraph (c) requires a disk's S/N to be listed in Appendix A (Table 1 for the 1st-stage disk, Table 2 for the 2nd-stage disk) of NMSB V2500-ENG-72-0713 Rev 1 or NMSB V2500-E5-72-0015 Rev 1, and either disk match is enough ('and/or'). Part numbers 2A5001 and 2A4802 match; serial numbers SYN-DISK1-0020 and SYN-DISK2-0020 could not be checked against the appendices.
- **Note:** The preamble places V2533-A5 in the high-thrust group, so paragraphs (g)(1) and (g)(2) are the requirements that would apply; the low-thrust paragraphs (g)(3) and (g)(4) and Figure 2 do not apply to this engine.
- **Note:** No cycle-based deadline can be computed: the record has no engine flight-cycle counter and no disk cycle counts, and the Figure 1 compliance time is not in the supplied text. The 10-FC term sets the earliest possible due point.
- **Note:** The events list is empty, so no engine shop visit or piece-part inspection is recorded; that is not evidence that none occurred. Under Note 1 to paragraph (g)(1), additional piece-part inspections under the ICA Airworthiness Limitations Section apply only if a part has more than 100 FCs since its last piece-part opportunity inspection, is damaged, or is the cause for engine removal; engine removal to comply with this AD is not cause.
- **Note:** Paragraph (i) credit covers only the (g)(5), (g)(6) and related (g)(7) actions under NMSB V2500-E5-72-0015 original issue, so it gives no credit path for this V2533-A5 engine.
- **Note:** Predecessor AD 2021-11-15 (Federal Register document 2021-11960, effective 2021-07-13) was in force on the question date and remains in force until 2022-03-15, when 2022-02574 replaces it. It was not evaluated in this screen. Under its paragraphs (g)(1) and (g)(2), V2533-A5 disks with S/Ns listed in its Appendix A tables require a USI at the next engine shop visit after 2021-07-13 or before 3,200 FCs after 2021-07-13, whichever occurs first; because the record has no cycle counter and no shop-visit events, that obligation needs separate review now.
- **Note:** No ad_records or amoc_claims were supplied, so there were no operator AD status entries or AMOC claims to check, and none were relied on.
- **Note:** The matched_parts entries are part-number matches only; listed_serial_number is null because the serial numbers the directive relies on are in appendices that were not supplied.
- **Unresolved locator:** 2022-02574 (g)(1) Figure 1 to paragraph (g)(1) (image not included in supplied text)

Forbidden claims for this case:

- AD 2022-02-09 controls on 2022-03-01.
- AD 2021-11-15 no longer applies on 2022-03-01.
- The engine is not affected because its S/N is not in the AD text.

## seed-021: Disk applicability lives in an unavailable service bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2022-02-09 (Federal Register 2022-02574) is in force and V2530-A5 is an in-scope high-thrust model whose installed disks carry the listed part numbers 2A5001 and 2A4802, but applicability turns on whether serial numbers SYN-DISK1-0021 and SYN-DISK2-0021 appear in Appendix A tables that were not supplied, and the Figure 1 compliance time is also missing, so no due point can be set and the screen needs review.
- **Stated timing:** If the serials are confirmed in Appendix A, the USI of the HPT 1st-stage disk under paragraph (g)(1) and of the HPT 2nd-stage disk under paragraph (g)(2) is due within the Figure 1 to paragraph (g)(1) compliance time or within 10 flight cycles after the March 15, 2022 effective date, whichever occurs later; Figure 1 is not in the supplied text, so no calendar or cycle due point can be fixed from this record.
- **Missing fact:** Appendix A tables of the NMSBs named in paragraph (c) are not in the supplied text: Table 1 (HPT 1st-stage disk) and Table 2 (HPT 2nd-stage disk) of IAE NMSB V2500-ENG-72-0713 Rev 1, or of IAE NMSB V2500-E5-72-0015 Rev 1, which paragraph (c) accepts. Serial numbers SYN-DISK1-0021 and SYN-DISK2-0021 therefore cannot be confirmed as listed, and applicability cannot be decided until they are checked.
- **Missing fact:** Figure 1 to paragraph (g)(1), an image not included in the supplied text, sets the compliance time that paragraphs (g)(1) and (g)(2) use for high-thrust engines such as V2530-A5. Without it no due point or cycle limit can be computed.
- **Missing fact:** The engine flight-cycle counter at the snapshot is not in the record. It is needed to compare against any cycle-based limit and to fill latest_engine_flight_cycles.
- **Missing fact:** The engine flight-cycle count on the March 15, 2022 effective date is not in the record. It is needed to convert the within-10-flight-cycles limit, which runs from that date, into a cycle number.
- **Missing fact:** Flight cycles accumulated by the HPT 1st-stage disk, and the cycles since its last piece-part opportunity inspection (used by Note 1 to paragraph (g)(1)), are not recorded. They are needed to apply the Figure 1 limit and to compute component_cycles_remaining.
- **Missing fact:** Flight cycles accumulated by the HPT 2nd-stage disk, and the cycles since its last piece-part opportunity inspection (used by Note 1 to paragraph (g)(1)), are not recorded. They are needed to apply the Figure 1 limit and to compute component_cycles_remaining.
- **Missing fact:** No operator AD status entry for AD 2022-02-09 is supplied, so any recorded USI, disk replacement or credit is unknown. The absence of a record is not evidence that the USI was or was not performed.
- **Missing fact:** The events list is empty, so no engine shop visit or inspection event is recorded. The shop visit and inspection history since the effective date must be confirmed before any Figure 1 limit can be evaluated.
- **Note:** Screening aid only; it does not determine the engine's or either disk's status under the directive and is not the operator's AD status record.
- **Note:** The question directive is 2022-02574 (AD 2022-02-09), which replaces and removes AD 2021-11-15; that earlier AD's 3,200 FC and next-engine-shop-visit terms are not used here.
- **Note:** Only the two supplied Federal Register documents were considered; no later superseding or correcting document was supplied, so the 2022 text is treated as operative as of 2026-10-06.
- **Note:** The preamble places V2530-A5 among the high-thrust engines, so the high-thrust paths (g)(1) and (g)(2) govern and the low-thrust paths (g)(3) and (g)(4) do not.
- **Note:** Paragraph (c) accepts a serial listing in either NMSB it names, while (g)(1) and (g)(2) cite V2500-ENG-72-0713 Rev 1 for this engine; both sets of Appendix A tables should be checked against the serial numbers.
- **Note:** Matched parts are part-number matches only; listed_serial_number is null because the serial listings are in Appendix A tables that were not supplied, so the serials are not confirmed.
- **Note:** No ad_records, amoc_claims, or prior USI or replacement records were supplied; no AMOC was claimed or evaluated. Paragraph (i) credit is tied to (g)(5) and (g)(6), which cover V2531-E5 engines, and does not map to this V2530-A5 record.
- **Note:** Paragraph (f) carries an 'unless already done' proviso; the record shows no prior USI, so prior performance is unknown rather than absent.
- **Note:** The events list is empty, so no engine shop visit is recorded; per paragraph (h)(1) a shop visit requires separation of H-P flanges, and an empty list does not establish that none occurred.
- **Note:** Because the effective date is more than four years before the question date, the outcome turns on the Figure 1 limit and the inspection history, neither of which is in the supplied material.
- **Note:** If a serial is listed in Appendix A, the corresponding (g) action attaches to that disk; if not, that disk falls outside paragraph (c) on this record. Either way the Figure 1 limit is needed before any due point is stated.
- **Note:** Identifiers beginning with SYN- are synthetic and were used as given.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-E5-72-0015 Revision 1 Appendix A Tables 1 and 2 (unavailable incorporated material)
- **Unresolved locator:** 2022-02574 preamble Background section, high-thrust and low-thrust engine categories
- **Unresolved locator:** 2022-02574 (g)(1) Figure 1 to paragraph (g)(1) not included in supplied text
- **Unresolved locator:** 2022-02574 (g)(2) Refers to Figure 1 to paragraph (g)(1)

Forbidden claims for this case:

- The engine is not affected because its S/N is not listed in the AD.
- The engine is affected because P/N 2A5001 is installed.
- The service bulletin lists are reconstructed or assumed.

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **No answer:** answer is not JSON: Unterminated string starting at: line 1 column 8540 (char 8539)

## seed-022/2021-11960: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **Fields:** applicability `unknown`, action_status `needs_review`, authority `in_force`
- **Expected:** applicability `unknown`, action_status `needs_review`
- **Summary:** AD 2021-11-15 has been in force since 2021-07-13 and covers V2533-A5 engines with an HPT 1st-stage disk (P/N 2A5001) or HPT 2nd-stage disk (P/N 2A4802) whose serial number is listed in the NMSB Appendix A tables, which were not supplied, so applicability is unknown for both installed disks. If a disk is listed, its ultrasonic inspection is due at the next engine shop visit or before 3,200 FCs since 2021-07-13, whichever occurs first, but the engine counter on 2021-07-13 is not recorded, so no engine-cycle limit can be computed.
- **Stated timing:** Only if the serial number is listed: the ultrasonic inspection of that disk is due at the next engine shop visit after 2021-07-13 or before the disk has accumulated 3,200 FCs since 2021-07-13, whichever occurs first; the events list is empty, so no engine shop visit is recorded since then.
- **Missing fact:** Appendix A, Table 1 of IAE NMSB V2500-ENG-72-0713 Revision 1 (paragraph (c)(1) also cites NMSB V2500-E5-72-0015) is not in the supplied material. It is needed to confirm whether HPT 1st-stage disk S/N PKLBSH1829 (P/N 2A5001) is listed, which decides whether paragraph (g)(1) applies to this engine.
- **Missing fact:** Appendix A, Table 2 of IAE NMSB V2500-ENG-72-0713 Revision 1 (paragraph (c)(2) also cites NMSB V2500-E5-72-0015) is not in the supplied material. It is needed to confirm whether HPT 2nd-stage disk S/N SYN-DISK2-0022 (P/N 2A4802) is listed, which decides whether paragraph (g)(2) applies to this engine.
- **Missing fact:** The engine flight-cycle counter on the effective date 2021-07-13 is not recorded. The 3,200-FC limit runs from that date, so the engine-counter deadline cannot be computed from the 33,000 (2021-07-19) and 33,004 (2021-07-20) readings.
- **Missing fact:** Flight cycles this HPT 1st-stage disk has accumulated since 2021-07-13, including any time on other engines, are not recorded. They are needed to test the 3,200-FC limit in paragraph (g)(1) and to compute component_cycles_remaining.
- **Missing fact:** Flight cycles this HPT 2nd-stage disk has accumulated since 2021-07-13, including any time on other engines, are not recorded. They are needed to test the 3,200-FC limit in paragraph (g)(2).
- **Note:** Screening aid only; this makes no determination about the engine or either disk.
- **Note:** V2533-A5 is a supported model. Paragraphs (g)(1) and (g)(2) cover it; (g)(3) and (g)(4) cover V2522-A5, V2524-A5, V2525-D5 and V2527-A5; (g)(5) and (g)(6) cover V2531-E5.
- **Note:** Both installed disks match the directive on part number only. Neither serial number has been checked against the Appendix A tables, and the NMSB service information itself was not supplied; the SYN- prefix on the second disk serial is not evidence either way.
- **Note:** Paragraph (c) also cites NMSB V2500-E5-72-0015, while (g)(1) and (g)(2) direct V2533-A5 engines to the Rev 1 tables. Check the E5 tables too, since a serial number listed only there would bear on applicability; the deadline form in (g)(5) and (g)(6) matches (g)(1) and (g)(2).
- **Note:** The 3,200 FCs run from 2021-07-13, not from the snapshot. Adding 3,200 to the 33,004 counter on 2021-07-20 would use the wrong start date, so no such figure is given.
- **Note:** latest_engine_flight_cycles and component_cycles_remaining are null because the counter on 2021-07-13 and the disks' cycle history since then are not in the record. alternative_readings is empty because no reading yields a computable deadline from this record.
- **Note:** The events list is empty, so no engine shop visit is recorded since 2021-07-13. An unrecorded induction meeting the (h)(1) definition would bring the shop-visit limb forward; flange separation solely for transport and engine removal for field maintenance at a facility are excluded by (h)(1).
- **Note:** Under (h)(2)(ii) a disk not listed in the Appendix A tables is a part eligible for installation, and the inspection terms of (g)(1) and (g)(2) reach only listed serial numbers.
- **Note:** No operator-asserted AD records or AMOC claims were supplied for AD 2021-11-15, so none were checked or relied on.
- **Note:** The engine serial SYN-V2500-0022 and the second disk serial SYN-DISK2-0022 carry the synthetic prefix; the analysis treats the record as given.
- **Expected missing fact (judge on meaning):** IAE NMSB V2500-ENG-72-0713 Revision 1 Appendix A Table 1 (unavailable incorporated material)
- **Unresolved locator:** 2021-11960 (g)(3) V2522-A5, V2524-A5, V2525-D5 and V2527-A5 only
- **Unresolved locator:** 2021-11960 (g)(5) V2531-E5 only

Forbidden claims for this case:

- Inspection steps or acceptance criteria stated without the service bulletin.
- The engine is not affected because table 1 lists a different engine serial for this disk.
- The 10-FC deadline runs from 2021-07-19, presented as settled.

## seed-023/2025-18469: One engine under three directives at once

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-023/2026-16954: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required_on_event`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required_on_event`
- **Summary:** Engine V2527M-A5 SYN-V2500-0023 has 3rd stage HPC rotor blade set P/N 6A8688 installed, which AD 2026-17-03 lists, and the AD has been in force since its 2026-09-24 effective date. Full blade set replacement is due only at the next engine shop visit after 2026-09-24 where the blades are exposed, and the record shows no such visit through 2026-10-06, so no calendar or cycle deadline is triggered by the record.
- **Stated timing:** Due at the next engine shop visit (induction of the engine into the shop for maintenance) after the 2026-09-24 effective date at which the 3rd stage HPC rotor blade is exposed (removed from the HPC stage 3 to 8 drum); the AD sets no calendar or cycle deadline before that event.
- **Expected timing:** Conditional: replace the full blade set at the next shop visit inducted after 2026-09-24 where a 3rd-stage blade is exposed.
- **Missing fact:** The record has no ad_records entry for AD 2026-17-03, so the operator's recorded status under this AD, any claimed blade replacement or accomplishment of IAE AG SB V2500-ENG-72-0716, and any AMOC claim are unknown. Applicability does not depend on this entry, and no operator AD status is inferred from its absence.
- **Missing fact:** The only recorded event is a 2025-12-01 maintenance program revision, which is not an engine induction, and no engine shop visit after 2026-09-24 is recorded through the 2026-10-06 snapshot. The record does not confirm that no induction occurred after the effective date; if one did and the 3rd stage blades were exposed, the full blade set replacement would have been required at that visit and the record would need to show it.
- **Note:** Screened against AD 2026-17-03 (FR doc 2026-16954, Amendment 39-23446), effective 2026-09-24 and in force on the 2026-10-06 question date. The NPRM (FR doc 2025-20088) is superseded for operative text and was not relied on; its 'next 3rd stage HPC rotor blade exposure' trigger was replaced by the engine shop visit trigger in the final rule.
- **Note:** Correction FR doc 2026-18423 (published 2026-09-10) restores the omitted word 'blade' in paragraph (g). It does not change the trigger or the effective date, and the corrected text is used here.
- **Note:** Applicability rests on the set-level P/N 6A8688. Blade serial numbers are not tracked at set level, and the AD lists part numbers only, so the missing serials do not prevent the match. The recorded P/N has no -001 suffix, so it is not one of the eligible designations in (h)(1).
- **Note:** Replacement parts must meet (h)(1): P/N 6C8368, 6C8403, or a later approved P/N, or a blade modified to P/N 6A8353-001 or 6A8688-001.
- **Note:** The AD sets no flight-cycle or calendar limit for the 3rd stage blades, so the 22500 engine flight cycles at the 2026-10-06 snapshot produce no deadline; latest_engine_flight_cycles and component_cycles_remaining are therefore null.
- **Note:** Maintenance program Revision 48 (2025-12-01) incorporates table 1 of AD 2025-17-16, a different directive whose text is not supplied. That revision is not an engine shop visit, does not address AD 2026-17-03, and cannot be used here as a blade cycle limit.
- **Note:** The HPT 1st-stage hub (P/N 2A5001) and HPT 2nd-stage hub (P/N 2A4802) are not listed in AD 2026-17-03 and were not matched; their cycle values were not used.
- **Note:** The preamble to 2026-16954 says blade replacement can only be performed at a shop visit, which is why the trigger is an engine shop visit, and that engines inducted before the 2026-09-24 effective date are not intended to be required to comply. Only an induction after that date starts this obligation.
- **Note:** The record has no ad_records or amoc_claims entries for this AD. This screen does not establish an operator AD status or an approved AMOC and does not treat missing records as evidence that the blades are unaffected.
- **Note:** The preamble says replacement under IAE AG SB V2500-ENG-72-0716 (dated October 4, 2024) changes the P/N to eligible parts; the AD text does not name that SB. No SB accomplishment is recorded, and the installed P/N remains 6A8688.
- **Note:** Screening aid output from the supplied record and Federal Register text only; it does not determine compliance or return-to-service status for this engine or any part.

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

## seed-023/2025-17066: One engine under three directives at once

- **No answer:** answer is not JSON: Unterminated string starting at: line 1 column 5151 (char 5150)

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** Federal Register document 2025-18469 (AD 2025-19-13) is in force on the 2026-10-06 question date and its applicability paragraph includes the V2528-D5, but neither recorded hub has a P/N and S/N pair listed in its table 1, so no removal is triggered on the record as supplied. The HPT 2nd-stage hub's recorded S/N PKLBST5011 is listed in table 1 only under P/N 2A5001, so that hub's recorded P/N should be verified.
- **Missing fact:** Recorded P/N 2A4802 with S/N PKLBST5011 is not a listed pair: table 1 lists PKLBST5011 only under P/N 2A5001 (HPT 1st-stage hub, 5,500-cycle limit). If the hub's P/N is actually 2A5001, it would be a listed pair and the paragraph (g) removal requirement would apply, so verify the P/N against the hub's identification records.
- **Missing fact:** If the recorded S/N is mis-keyed and the hub's actual S/N is one of the listed 2A4802 serials (PKLBST5005, PKLBSS9840, PKLBSS0301, PKLBSR2100), the hub would be a listed pair; verify the S/N against the hub's identification records.
- **Missing fact:** The engine record carries no engine flight-cycle counter. It is needed to state any removal deadline as an engine flight-cycle count and to count the 100-flight-cycle period from 2025-10-29, and it matters only if a listed pair is confirmed.
- **Note:** Screening aid only, not a compliance determination; no conclusion about the engine's status is drawn.
- **Note:** Authority: 2025-18469 was published 2025-09-24 with an effective date of 2025-10-29 (DATES and paragraph (a)), so it is in force on 2026-10-06. The NPRM 2025-10764 was not relied on; the final rule is the operative text.
- **Note:** Applicability rests on the engine model: V2528-D5 is listed in paragraph (c). The removal requirement in paragraph (g) depends on installed P/N and S/N pairs, which is why applicability and action differ here.
- **Note:** HPT 1st-stage hub: recorded P/N 2A5001 is a table 1 P/N, but recorded S/N SYN-HUB1-0024 is not among the 2A5001 listed serials (PKLBSK9287, PKLBSS9200, PKLBST5011, PKLBST7489), so it is not a matched part.
- **Note:** HPT 2nd-stage hub: recorded P/N 2A4802 is a table 1 P/N, but recorded S/N PKLBST5011 is listed only under P/N 2A5001; the listed 2A4802 serials are PKLBST5005, PKLBSS9840, PKLBSS0301 and PKLBSR2100. Table 1 identifies parts by P/N and S/N together, so an S/N match alone does not make this hub a matched part.
- **Note:** Reviewer contingency only: if the 2nd-stage hub were verified as P/N 2A5001 with S/N PKLBST5011, it would be a listed pair with a 5,500-cycle removal limit and 2,500 cycles remaining at the recorded 3,000 cycles since new. Paragraph (g) would then require removal at the next engine shop visit before exceeding 5,500 cycles since new or within 100 flight cycles from 2025-10-29, whichever occurs later, and paragraph (h) would bar its installation after 2025-10-29; the record has no installation dates. This is not a finding about the recorded part.
- **Note:** latest_engine_flight_cycles and component_cycles_remaining are null because no installed part is an affected part on the record, and the engine flight-cycle counter needed for an engine-cycle deadline is absent.
- **Note:** The events list is empty, so no engine shop visit or installation is recorded. An empty list does not show that none occurred; shop-visit timing matters only if a listed pair is confirmed.
- **Note:** The engine record has no ad_records or amoc_claims entries, so no operator AD status or AMOC claim was assessed. Any alternative method would need approval under paragraph (j).
- **Note:** Verify both hubs' P/N and S/N against identification records, since a mis-keyed serial could sit against the wrong component. Identifiers beginning with SYN- are synthetic per the record convention and were used as recorded.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The record's engine model CFM56-5B4/3 is not one of the supported IAE V2500 models for this screen, so no applicability determination is made under AD 2025-17-16 (Federal Register document 2025-17066). The directive is in force on the question date because it took effect October 10, 2025.
- **Note:** The engine record is marked synthetic. The scope check failed on engine_model, so the empty installed_components and events lists were not evaluated and no applicability determination was made.
- **Note:** The operator air_carrier_operation field does not bear on scope for this screen.
- **Note:** Because the model designation alone determines this result, a reviewer should confirm engine_model against the source engine record. If the record was mis-keyed and the engine is a supported IAE V2500 model, the screen should be rerun with the correct model and its installed components and events.
- **Note:** The earlier NPRM 2024-26092 was not relied on because the final rule 2025-17066 is the operative text.
- **Note:** This is a screening aid output, not a compliance determination.
- **Unresolved locator:** 2025-17066 (c) Applicability paragraph of the AD text

Forbidden claims for this case:

- AD 2025-17-16 applies because the operator flies A320-family aircraft.
- The engine is not affected by any airworthiness directive.

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-027: Listed hub near its limit, with an unverified AMOC claimed to extend it

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The directive applies: the V2527-A5 is a listed model and the installed HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 is listed in table 1 with a removal cycle limit of 4,800 cycles since new (CSN); the hub is at 4,750 CSN, leaving 50 cycles. Removal and replacement is required at the next engine shop visit, which must occur before the hub exceeds 4,800 CSN (engine flight cycle 15,300), because the 'whichever occurs later' wording makes that date control over the 100-flight-cycle date (15,100); the AMOC claim to 5,300 CSN has no FAA approval on file and is not relied on.
- **Stated timing:** At the next engine shop visit after 2025-10-29, and before the hub exceeds 4,800 CSN, which is engine flight cycle 15,300 (50 cycles after the 15,250 counter at the 2026-01-20 snapshot). The 100-flight-cycle date of 15,100 is earlier and does not control under 'whichever occurs later'.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** The planning-record claim of a 5,300 CSN removal limit has no FAA approval letter and an unknown approval_reference. Only an FAA-approved AMOC could change the published 4,800 CSN limit, so the claim cannot be applied until approval is shown.
- **Missing fact:** The events list is empty, so the record shows no engine shop visit after 2025-10-29 and no planned shop visit. Confirm whether any qualifying engine shop visit under paragraph (i)(2) has occurred since the effective date and when the next one is planned, because removal is tied to that visit and must occur before engine flight cycle 15,300.
- **Missing fact:** The 4,750 CSN value is undated; the only dated reading is 4,500 at 2025-10-29. Confirm the hub CSN as of the snapshot, since the 50-cycle margin and the 15,300 date depend on it.
- **Missing fact:** The recorded S/N SYN-HUB2-0027 is not listed in table 1 for P/N 2A4802, so the 2nd-stage hub is screened as not matched. Confirm the S/N is recorded correctly, because a listed S/N would bring its table 1 removal limit and the installation prohibition into play.
- **Note:** Screening aid only, not a compliance determination. Record values are as supplied for the 2026-01-20 snapshot; SYN- identifiers are synthetic. Model V2527-A5 is within the supported scope and the directive's applicability paragraph.
- **Note:** Authority: Federal Register document 2025-18469 (final rule, AD 2025-19-13) was published 2025-09-24 with an effective date of 2025-10-29, so it is in force on the question date. The NPRM 2025-10764 was a proposal superseded by that final rule and was not relied on.
- **Note:** Cycle arithmetic: engine flight cycles were 15,000 on 2025-10-29 and 15,250 on 2026-01-20. Hub CSN rose from 4,500 to 4,750 over the same 250 cycles, so the record is consistent with one hub cycle per engine cycle; at that rate the hub reaches 4,800 CSN at engine flight cycle 15,300.
- **Note:** Deadline reading: paragraph (g) joins two prongs with 'whichever occurs later'. The later date is the cycle-limit date (15,300), not the 100-flight-cycle date (15,100). A shop visit occurring after engine flight cycle 15,300 would fall after the cycle-limit date, so a shop visit has to be planned before then.
- **Note:** Shop visit trigger: the events list is empty, so no engine shop visit is recorded after the effective date. If a qualifying shop visit under paragraph (i)(2) occurred after 2025-10-29 without removal of the hub, this screen would need review.
- **Note:** AMOC: the 5,300 CSN planning note is an operator assertion. No FAA approval letter is on file and approval_reference is unknown. Paragraph (j)(1) reserves AMOC approval to the AIR-520 manager, so the published 4,800 CSN limit is applied. If an approval were produced and verified, the cycle-limit date would move to 15,800 (550 cycles from 15,250) and the screen would need to be redone.
- **Note:** HPT 2nd-stage hub: P/N 2A4802 with S/N SYN-HUB2-0027 does not match any 2A4802 S/N in table 1, which keys on both P/N and S/N. Listed 2A4802 limits run from 3,900 to 6,000 CSN, so this part's CSN would matter only if its S/N were listed. The record has no installation date or cycle readings for it, which does not affect this match.
- **Note:** Installation prohibition: the 1st-stage hub was installed 2020-09-14, before the effective date, so paragraph (h) governs any later installation of PKLBSS9200 in any engine; removal under paragraph (g) is the obligation for the existing installation.
- **Note:** Replacement: no replacement hub is recorded. The replacement must be an HPT 1st-stage or 2nd-stage hub whose P/N and S/N are not listed in table 1 (paragraph (i)(1)).
- **Note:** Per the final rule preamble, removing the listed hubs does not make the AD stop applying, because the installation prohibition continues. The continuing obligations above therefore remain after removal.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub row 2A5001 / PKLBSS9200 / 4,800
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub rows for P/N 2A4802

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** The AD applies to this V2524-A5 engine, and the installed HPT 2nd-stage hub (P/N 2A4802, S/N PKLBST5005) is listed in Table 1 with a 4,000-cycle removal limit; at 1,400 cycles since new it has 2,600 cycles remaining, so removal and replacement is required at the next engine shop visit before that limit is reached (about engine flight cycle 11,000). The operator's not-applicable entry conflicts with the installed-part record and is not relied on.
- **Stated timing:** Due at the next engine shop visit after 2025-10-29 and before the hub's cycles since new exceed 4,000, which is engine flight cycle 11,000 on a one-for-one projection from the 2026-02-10 snapshot; no shop visit is recorded, and the 100-cycle date (engine flight cycle 8,100) precedes the 8,400-cycle snapshot but does not set an earlier deadline under the 'whichever occurs later' wording.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Missing fact:** The events list is empty, so no engine shop visit since the 2025-10-29 effective date is recorded. Paragraph (g) keys removal to the next engine shop visit, so a shop visit that has already occurred since the effective date would change the timing analysis; confirm against the shop visit definition in paragraph (i)(2).
- **Missing fact:** The current cycles-since-new value of 1,400 is undated; the only dated reading is 1,000 at 2025-10-29. The 400-cycle rise matches the 400 engine flight cycles between those dates, which supports 1,400 as the value at the snapshot, but a dated reading would confirm the 2,600 cycles remaining.
- **Missing fact:** The engine flight cycle 11,000 projection assumes the hub stays installed on this engine and accrues one cycle per engine flight cycle from the 2026-02-10 snapshot; no planned utilization or removal date is in the supplied record.
- **Note:** Screening aid only; this is not a compliance determination. The directive relied on is final rule 2025-18469 (AD 2025-19-13), effective 2025-10-29 and in force on the question date; proposed rule 2025-10764 is not relied on.
- **Note:** The ad_records entry marks AD 2025-19-13 as not_applicable with the note 'no affected hubs installed'. The installed-component record lists an HPT 2nd-stage hub with P/N 2A4802 and S/N PKLBST5005, which matches Table 1, so the entry is contradicted by the record and is not used as evidence.
- **Note:** Cycle arithmetic: engine flight cycles were 8,000 at 2025-10-29 and 8,400 at 2026-02-10, and the hub's cycles since new rose from 1,000 to 1,400 over the same interval. At one-for-one accrual the 4,000-cycle limit is reached at engine flight cycle 11,000, leaving 2,600 cycles (4,000 minus 1,400).
- **Note:** Paragraph (g) says 'whichever occurs later', so the later of the shop-visit limb and the 100-cycle limb governs. The 100-cycle limb ends at engine flight cycle 8,100; with no shop visit recorded, the shop visit before the removal limit is the operative timing.
- **Note:** Removal is tied to the next engine shop visit, so a shop visit before engine flight cycle 11,000 is needed to fit the timing the directive sets; the record shows none scheduled.
- **Note:** The installed HPT 1st-stage hub (P/N 2A5001, S/N SYN-HUB1-0028) is not listed for that part number in Table 1, so it is not matched; its 1,400 cycles since new do not bear on this screen.
- **Note:** The HPT 2nd-stage hub was installed 2025-06-03, before the 2025-10-29 effective date, so that installation is not reached by the installation prohibition in paragraph (h); the prohibition applies to installing a listed hub in any engine after the effective date.
- **Note:** The record contains no AMOC claim, so no alternative method of compliance is assumed.
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 2nd-stage hub row for P/N 2A4802 and S/N PKLBST5005 (4,000 cycles)
- **Unresolved locator:** 2025-18469 (g) Table 1 to paragraph (g), HPT 1st-stage hub rows for P/N 2A5001

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)
