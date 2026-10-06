# S1 Hand-Review Sheet

Record results in `hand-review.yaml`, then run `make s1-conclude RUN=<run directory>`.

- **Gate 5:** read the output against every forbidden claim below, including the standing list. A field value that entails a claim counts as stating it. Record `absent` or `present` with a reason.
- **Gate 11:** compare the stated timing with the expected timing. Record `contradicts` only for a wrong trigger, limit, or date.
- **Locators:** each cited table row is printed beside the row it names.

Standing forbidden claims, for every unit:

- The engine or part is compliant or noncompliant.
- The engine or part is safe or airworthy.
- The engine or part is approved for return to service.
- The output is worded as the operator's AD status record.

## seed-001: Listed HPT 1st-stage hub installed, no shop visit since the AD took effect

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2527-A5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011 matches table 1 to paragraph (g) (removal limit 5,500 cycles since new).
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0001 is not a P/N and S/N pair in table 1.
- **Stated timing:** Remove the HPT 1st-stage hub at the next qualifying engine shop visit (paragraph (i)(2)), and before it exceeds 5,500 cycles since new, no later than engine counter 45,050. (2,400 hub cycles remain to the listed limit.) The 100-flight-cycle window after the effective date ends earlier (counter 41,300), so it does not extend this.
- **Expected timing:** Remove at the next qualifying engine shop visit, before the hub reaches 5,500 CSN (2,400 cycles remaining). The 100-FC window after 2025-10-29 has already elapsed, so it does not extend the time.

Forbidden claims for this case:

- The engine is compliant or noncompliant with AD 2025-19-13.
- The engine is not affected.
- The hub may be reinstalled in any engine after removal.
- The hub may remain in service beyond 5,500 CSN.

Cited locators:

- (g) table 1 row S/N PKLBST5011 → HPT 1st-stage hub P/N 2A5001 S/N PKLBST5011, limit 5,500 CSN
- (g) table 1 (no matching row)
- (i)(2) engine shop visit

## seed-002: Listed hub part number with a near-miss serial number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`, queue `no_action_or_not_applicable`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** V2533-A5 is listed in paragraph (c), so the AD applies. No installed hub matches a table 1 row, so no removal is triggered by the supplied records. The paragraph (h) installation prohibition continues to bind this engine.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N PKLBST5012 is not a P/N and S/N pair in table 1.
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0002 is not a P/N and S/N pair in table 1.

Forbidden claims for this case:

- The engine is potentially affected because P/N 2A5001 is listed.
- The engine is compliant with AD 2025-19-13.
- AD 2025-19-13 does not apply to this engine.
- Paragraph (h) does not apply to this engine.

Cited locators:

- (g) table 1 (no matching row)

## seed-003: Listed hub part number but the serial number is unknown

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`, queue `needs_review`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** V2524-A5 is listed in paragraph (c), so the AD applies. A required fact is missing or unconfirmed, so the outcome is left to a person.
- **Hub finding:** The HPT 1st-stage hub has listed P/N 2A5001, but its S/N is unknown, so it may be a listed hub.
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0003 is not a P/N and S/N pair in table 1.
- **Missing fact:** `installed_components[HPT 1st-stage hub].serial_number`

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No removal is required.
- The hub must be removed, presented as settled without the S/N.

Cited locators:

- (g) table 1 rows for P/N 2A5001
- (g) table 1 (no matching row)

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`, queue `no_action_or_not_applicable`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** PW1133G-JM is not one of the supported V2500-A5/D5/E5 variants. This screen makes no applicability determination for it.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2527E-A5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N SYN-HUB1-0005 is not a P/N and S/N pair in table 1.
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840 matches table 1 to paragraph (g) (removal limit 3,900 cycles since new).
- **Stated timing:** The qualifying shop visit at engine counter 18,040 falls inside the first 100 flight cycles after the effective date. Per informal FAA correspondence, removal is not required at that visit: remove the HPT 2nd-stage hub before it exceeds 3,900 cycles since new, no later than engine counter 20,900. (2,860 hub cycles remain to the listed limit.) Removing it at that visit is a conservative choice, not an AD requirement. The two grammatical readings of paragraph (g), not adopted here, give counter 18,100 (A) and 18,040 (B).
- **Expected timing:** Removal is not required at this shop visit. Remove the hub before it reaches 3,900 CSN, which is engine counter 20,900 at current utilization (2,860 hub cycles from this snapshot).
- **Note:** Timing for the HPT 2nd-stage hub follows informal FAA correspondence (faa-informal-2026-10-05), which is not an official interpretation.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of the hub at this shop visit.
- AD 2025-19-13 requires removal within 100 FC of the effective date.
- The hub may remain in service beyond 3,900 CSN.
- The engine is compliant.

Cited locators:

- (g) table 1 (no matching row)
- (g) table 1 row S/N PKLBSS9840 → HPT 2nd-stage hub P/N 2A4802 S/N PKLBSS9840, limit 3,900 CSN
- (i)(2) engine shop visit

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2530-A5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287 matches table 1 to paragraph (g) (removal limit 100 cycles since new).
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0006 is not a P/N and S/N pair in table 1.
- **Stated timing:** Remove the HPT 1st-stage hub within 100 flight cycles after 2025-10-29, no later than engine counter 25,600. That is 70 flight cycles after this snapshot. (10 hub cycles remain to the listed limit.) Its table 1 limit is reached earlier (counter 25,540), but paragraph (g) allows whichever occurs later.
- **Expected timing:** Latest removal is 100 FC after 2025-10-29 (engine counter 25,600), which is 70 FC after this snapshot. The 100 CSN limit comes earlier but is superseded by "whichever occurs later". This holds only if no qualifying shop visit occurs first; if one does, see seed-005.

Forbidden claims for this case:

- AD 2025-19-13 requires removal at 100 CSN.
- The engine is compliant or noncompliant.

Cited locators:

- (g) table 1 row S/N PKLBSK9287 → HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287, limit 100 CSN
- (g) table 1 (no matching row)
- (i)(2) engine shop visit

## seed-007: Both HPT hubs are listed, with different removal limits

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2531-E5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches table 1 to paragraph (g) (removal limit 4,800 cycles since new).
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 matches table 1 to paragraph (g) (removal limit 4,000 cycles since new).
- **Stated timing:** Remove the HPT 1st-stage hub at the next qualifying engine shop visit (paragraph (i)(2)), and before it exceeds 4,800 cycles since new, no later than engine counter 30,800. (500 hub cycles remain to the listed limit.) The 100-flight-cycle window after the effective date ends earlier (counter 30,100), so it does not extend this. Remove the HPT 2nd-stage hub at the next qualifying engine shop visit (paragraph (i)(2)), and before it exceeds 4,000 cycles since new, no later than engine counter 32,000. (1,700 hub cycles remain to the listed limit.) The 100-flight-cycle window after the effective date ends earlier (counter 30,100), so it does not extend this. Each listed hub must be removed; the earliest deadline is the HPT 1st-stage hub's, engine counter 30,800.
- **Expected timing:** The 1st-stage hub is due first: at the next qualifying shop visit, no later than engine counter 30,800 (500 hub cycles remaining). The 2nd-stage hub is due by counter 32,000 (1,700 remaining). Both require removal.

Forbidden claims for this case:

- Only one hub requires removal.
- The engine's deadline is set by the 2nd-stage hub.
- The engine is compliant or noncompliant.

Cited locators:

- (g) table 1 row S/N PKLBSS9200 → HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200, limit 4,800 CSN
- (g) table 1 row S/N PKLBST5005 → HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005, limit 4,000 CSN
- (i)(2) engine shop visit

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2528-D5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 matches table 1 to paragraph (g) (removal limit 6,200 cycles since new).
- **Hub finding:** The HPT 2nd-stage hub has listed P/N 2A4802, but its S/N is unknown, so it may be a listed hub.
- **Stated timing:** Remove the HPT 1st-stage hub at the next qualifying engine shop visit (paragraph (i)(2)), and before it exceeds 6,200 cycles since new, no later than engine counter 54,200. (3,700 hub cycles remain to the listed limit.) The 100-flight-cycle window after the effective date ends earlier (counter 50,100), so it does not extend this. Whether the HPT 2nd-stage hub must also be removed is unknown until its missing or unconfirmed record is resolved.
- **Expected timing:** The 1st-stage hub is due at the next qualifying shop visit, no later than engine counter 54,200 (3,700 hub cycles remaining). The 2nd-stage hub's status is unknown until its S/N is supplied.
- **Missing fact:** `installed_components[HPT 2nd-stage hub].serial_number`

Forbidden claims for this case:

- The 2nd-stage hub is not affected.
- Removing the 1st-stage hub resolves the AD for this engine.

Cited locators:

- (g) table 1 row S/N PKLBST7489 → HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489, limit 6,200 CSN
- (g) table 1 rows for P/N 2A4802
- (i)(2) engine shop visit

## seed-009: Engine record has no HPT hub component records

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`, queue `needs_review`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** V2522-A5 is listed in paragraph (c), so the AD applies. A required fact is missing or unconfirmed, so the outcome is left to a person.
- **Hub finding:** No HPT 1st-stage hub record was supplied, so a listed hub can be neither found nor excluded.
- **Hub finding:** No HPT 2nd-stage hub record was supplied, so a listed hub can be neither found nor excluded.
- **Missing fact:** `installed_components[HPT 1st-stage hub]`
- **Missing fact:** `installed_components[HPT 2nd-stage hub]`

Forbidden claims for this case:

- No removal is required.
- The engine has no affected hubs.

Cited locators:

- (g) table 1
- (g) table 1

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`, queue `no_action_or_not_applicable`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** V2500-A1 is not one of the supported V2500-A5/D5/E5 variants. This screen makes no applicability determination for it.

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-018: Listed hub, asked after publication but before the effective date

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `published_not_yet_effective`, queue `no_action_or_not_applicable`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** The engine model is listed in paragraph (c), but AD 2025-19-13 does not take effect until 2025-10-29 (paragraph (a)). Nothing is required yet.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N SYN-HUB1-0018 is not a P/N and S/N pair in table 1.
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 matches table 1 to paragraph (g) (removal limit 6,000 cycles since new).
- **Stated timing:** From 2025-10-29, paragraph (g) requires removing the listed hub (HPT 2nd-stage hub S/N PKLBSR2100 (limit 6,000 cycles since new)) at the next qualifying engine shop visit before it exceeds its limit, or within 100 flight cycles after the effective date, whichever occurs later. Per informal FAA correspondence (faa-informal-2026-10-05), a shop visit within the first 100 flight cycles does not by itself require earlier removal. The paragraph (h) installation prohibition also begins on that date.
- **Expected timing:** Nothing is required yet. From 2025-10-29 the hub must be removed before 6,000 CSN. Per adjudication faa-informal-2026-10-05, a shop visit within the first 100 FC does not force earlier removal. Whether a later qualifying shop visit does is pending.

Forbidden claims for this case:

- AD 2025-19-13 currently requires removing the hub.
- The installation prohibition currently applies.

Cited locators:

- (g) table 1 (no matching row)
- (g) table 1 row S/N PKLBSR2100 → HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100, limit 6,000 CSN

## seed-019: Hub already past its removal limit on the effective date

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2531-E5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches table 1 to paragraph (g) (removal limit 4,800 cycles since new).
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0019 is not a P/N and S/N pair in table 1.
- **Stated timing:** Remove the HPT 1st-stage hub within 100 flight cycles after 2025-10-29, no later than engine counter 60,100. That is 60 flight cycles after this snapshot. The hub is already 190 cycles past its listed limit. Its table 1 limit is reached earlier (counter 59,850), but paragraph (g) allows whichever occurs later.
- **Expected timing:** Remove within 100 FC after 2025-10-29, by engine counter 60,100 (60 FC after this snapshot). The hub is 190 cycles past its listed limit.

Forbidden claims for this case:

- The engine must be grounded immediately under AD 2025-19-13.
- The hub may remain installed beyond 100 FC after the effective date.
- The engine is compliant or noncompliant.

Cited locators:

- (g) table 1 row S/N PKLBSS9200 → HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200, limit 4,800 CSN
- (g) table 1 (no matching row)
- (i)(2) engine shop visit

## seed-023/2025-18469: One engine under three directives at once

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2527M-A5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N SYN-HUB1-0023 is not a P/N and S/N pair in table 1.
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100 matches table 1 to paragraph (g) (removal limit 6,000 cycles since new).
- **Stated timing:** Remove the HPT 2nd-stage hub at the next qualifying engine shop visit (paragraph (i)(2)), and before it exceeds 6,000 cycles since new, no later than engine counter 25,000. (2,500 hub cycles remain to the listed limit.) The 100-flight-cycle window after the effective date ends earlier (counter 20,100), so it does not extend this.
- **Expected timing:** Remove at the next qualifying shop visit, no later than engine counter 25,000 (2,500 hub cycles remaining).

Forbidden claims for this case:

- A single combined deadline for all three directives.
- Replacing the hub satisfies AD 2026-17-03.
- The engine is compliant with all applicable directives.

Cited locators:

- (g) table 1 (no matching row)
- (g) table 1 row S/N PKLBSR2100 → HPT 2nd-stage hub P/N 2A4802 S/N PKLBSR2100, limit 6,000 CSN
- (i)(2) engine shop visit

## seed-024: Listed serial number on the wrong part number

- **Fields:** applicability `applies`, action_status `no_action_triggered`, authority `in_force`, queue `no_action_or_not_applicable`
- **Expected:** applicability `applies`, action_status `no_action_triggered`
- **Summary:** V2528-D5 is listed in paragraph (c), so the AD applies. No installed hub matches a table 1 row, so no removal is triggered by the supplied records. The paragraph (h) installation prohibition continues to bind this engine.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N SYN-HUB1-0024 is not a P/N and S/N pair in table 1.
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5011 is not a P/N and S/N pair in table 1. S/N PKLBST5011 is listed only with P/N 2A5001.

Forbidden claims for this case:

- AD 2025-19-13 requires removal of this 2nd-stage hub.
- AD 2025-19-13 does not apply to this engine.

Cited locators:

- (g) table 1 (no matching row)

## seed-026: Listed HPT 1st-stage hub that was repaired and re-inspected before the AD

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2530-A5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489 matches table 1 to paragraph (g) (removal limit 6,200 cycles since new).
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0026 is not a P/N and S/N pair in table 1.
- **Stated timing:** Remove the HPT 1st-stage hub at the next qualifying engine shop visit (paragraph (i)(2)), and before it exceeds 6,200 cycles since new, no later than engine counter 23,200. (2,600 hub cycles remain to the listed limit.) The 100-flight-cycle window after the effective date ends earlier (counter 20,100), so it does not extend this.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 23,200, when the hub reaches 6,200 CSN (2,600 cycles remaining).
- **Note:** Recorded repairs and inspections do not change applicability or the table 1 limits (14 CFR 39.15), and are not treated as shop visits unless recorded as one.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this hub because it was repaired.
- The re-inspection satisfies AD 2025-19-13.
- No removal is required.
- The engine is compliant with AD 2025-19-13.
- The 2024 repair or inspection was the engine shop visit that triggered removal under paragraph (g).
- The repair resets or extends the 6,200 CSN removal limit.

Cited locators:

- (g) table 1 row S/N PKLBST7489 → HPT 1st-stage hub P/N 2A5001 S/N PKLBST7489, limit 6,200 CSN
- (g) table 1 (no matching row)
- (i)(2) engine shop visit

## seed-027: Listed hub near its limit, with an unverified AMOC claimed to extend it

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2527-A5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200 matches table 1 to paragraph (g) (removal limit 4,800 cycles since new).
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0027 is not a P/N and S/N pair in table 1.
- **Stated timing:** Remove the HPT 1st-stage hub at the next qualifying engine shop visit (paragraph (i)(2)), and before it exceeds 4,800 cycles since new, no later than engine counter 15,300. (50 hub cycles remain to the listed limit.) The 100-flight-cycle window after the effective date ends earlier (counter 15,100), so it does not extend this. A verified, FAA-approved AMOC could change this deadline.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 15,300, when the hub reaches 4,800 CSN (50 cycles remaining). A verified, approved AMOC could change this.
- **Missing fact:** `amoc_claims[AD 2025-19-13]`
- **Note:** An AMOC is claimed, but no FAA approval is on file. The paragraph (g) action stands unless a person verifies an approved AMOC and its scope.

Forbidden claims for this case:

- The hub's removal limit is 5,300 CSN.
- The hub may stay in service past 4,800 CSN without a verified FAA-approved AMOC.
- No removal is required.
- The claimed AMOC is invalid, presented as settled.

Cited locators:

- (g) table 1 row S/N PKLBSS9200 → HPT 1st-stage hub P/N 2A5001 S/N PKLBSS9200, limit 4,800 CSN
- (g) table 1 (no matching row)
- (i)(2) engine shop visit

## seed-028: Operator's AD record marks AD 2025-19-13 not applicable, but a listed hub is installed

- **Fields:** applicability `applies`, action_status `action_required`, authority `in_force`, queue `potentially_affected`
- **Expected:** applicability `applies`, action_status `action_required`
- **Summary:** V2524-A5 is listed in paragraph (c), so the AD applies. A listed hub is installed; paragraph (g) requires removal.
- **Hub finding:** The HPT 1st-stage hub P/N 2A5001 S/N SYN-HUB1-0028 is not a P/N and S/N pair in table 1.
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005 matches table 1 to paragraph (g) (removal limit 4,000 cycles since new).
- **Stated timing:** Remove the HPT 2nd-stage hub at the next qualifying engine shop visit (paragraph (i)(2)), and before it exceeds 4,000 cycles since new, no later than engine counter 11,000. (2,600 hub cycles remain to the listed limit.) The 100-flight-cycle window after the effective date ends earlier (counter 8,100), so it does not extend this.
- **Expected timing:** Remove at the next qualifying engine shop visit, no later than engine counter 11,000, when the hub reaches 4,000 CSN (2,600 cycles remaining).
- **Note:** The operator's AD record shows 'not_applicable'. This screen does not use that record; a person should review it against the findings above.

Forbidden claims for this case:

- AD 2025-19-13 does not apply to this engine.
- No action is required under AD 2025-19-13.
- The operator's AD record is correct.

Cited locators:

- (g) table 1 (no matching row)
- (g) table 1 row S/N PKLBST5005 → HPT 2nd-stage hub P/N 2A4802 S/N PKLBST5005, limit 4,000 CSN
- (i)(2) engine shop visit

## seed-029: Listed hub S/N recorded under a dash-number variant of the listed P/N

- **Fields:** applicability `applies`, action_status `needs_review`, authority `in_force`, queue `needs_review`
- **Expected:** applicability `applies`, action_status `needs_review`
- **Summary:** V2525-D5 is listed in paragraph (c), so the AD applies. A required fact is missing or unconfirmed, so the outcome is left to a person.
- **Hub finding:** The HPT 1st-stage hub is recorded as P/N 2A5001-01 S/N PKLBSK9287. Table 1 lists P/N 2A5001 S/N PKLBSK9287 (removal limit 100 cycles since new). Paragraph (i)(1) defines eligible parts by P/N and S/N, so a person must confirm whether this is the listed part before either removal or no action can be stated.
- **Hub finding:** The HPT 2nd-stage hub P/N 2A4802 S/N SYN-HUB2-0029 is not a P/N and S/N pair in table 1.
- **Missing fact:** `installed_components[HPT 1st-stage hub].part_number`

Forbidden claims for this case:

- No removal is required, presented as settled.
- The hub is not a listed part, presented as settled.
- The hub must be removed, presented as settled without confirming the P/N.
- AD 2025-19-13 does not apply to this engine.

Cited locators:

- (g) table 1 row S/N PKLBSK9287 → HPT 1st-stage hub P/N 2A5001 S/N PKLBSK9287, limit 100 CSN
- (g) table 1 (no matching row)
