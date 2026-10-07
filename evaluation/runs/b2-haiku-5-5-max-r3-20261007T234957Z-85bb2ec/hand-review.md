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

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-003: Listed hub part number but the serial number is unknown

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-004: Geared-turbofan engine outside the supported V2500 family

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** Engine model PW1133G-JM is not one of the supported IAE V2500 models, so this screen makes no applicability determination and assigns no action status for AD 2025-19-13 (Federal Register 2025-18469). The final rule is effective October 29, 2025, so it is in force on the question date, but that does not change the scope limit.
- **Note:** Engine record SYN-ENG-004 (serial SYN-PW1100-0004, model PW1133G-JM, snapshot 2026-09-26) is synthetic; its installed_components and events lists are empty and were not evaluated because the model is outside the supported scope.
- **Note:** An empty installed_components list is not evidence that no affected HPT 1st-stage or 2nd-stage hub is installed; no part-level screen was performed.
- **Note:** If the model designation was entered in error, correct the engine record and rescreen against the actual model.
- **Note:** The proposed rule 2025-10764 was not relied on; final rule 2025-18469 is the document under question.
- **Note:** This is a screening aid only and makes no determination about the engine's status or return to service.

Forbidden claims for this case:

- The engine is not affected by any airworthiness directive.
- The engine is compliant.

## seed-005: Qualifying shop visit inducted 40 FC after the effective date

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-006: Hub with a 100 CSN limit, where the 100-FC window sets the outer deadline

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-007: Both HPT hubs are listed, with different removal limits

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-008: One listed hub matches while the other hub's serial number is unknown

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-009: Engine record has no HPT hub component records

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-010: V2500-A1, a V2500 engine outside the supported variants

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The engine model V2500-A1 in the record is not one of the ten IAE V2500 models this screen supports for Federal Register document 2025-18469, so no applicability determination is made and action_status is none. The final rule took effect October 29, 2025, so it is in force on the question date of 2026-09-26.
- **Note:** Screen scope: this screen supports only IAE V2500 models V2522-A5, V2524-A5, V2525-D5, V2527-A5, V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2531-E5 and V2533-A5. The record lists engine model V2500-A1, which is not on that list, so no applicability determination or cycle computation was made.
- **Note:** The installed HPT 1st-stage hub record (P/N 2A5001, S/N PKLBST5011) carries identifiers that appear in Table 1 to paragraph (g) of 2025-18469; that appearance does not establish applicability for this engine and was not evaluated for action status, timing, or remaining cycles.
- **Note:** The screen does not infer that V2500-A1 is a mis-recorded listed model. If the engine model field is corrected, rerun the screen against the directive's applicability paragraph and Table 1 using the corrected record.
- **Note:** The events list is empty. That means no event is recorded, not that no engine shop visit occurred, and a missing record is not evidence that a part is absent.
- **Note:** Authority: 2025-18469 is the final rule for AD 2025-19-13, effective October 29, 2025, so it is in force on 2026-09-26. The NPRM 2025-10764 (published 2025-06-13) is the proposal stage and was not relied on for this outcome; no correction or later superseding document was supplied.
- **Note:** The record is flagged synthetic and its engine identifiers begin with SYN-. This output is a screening aid and makes no status determination for the engine or any part.
- **Unresolved locator:** 2025-18469 (g) Table 1 to Paragraph (g), HPT 1st-stage hub row with P/N 2A5001 and S/N PKLBST5011

Forbidden claims for this case:

- The engine is potentially affected because it is a V2500.
- The engine is potentially affected because a listed hub is recorded.
- The engine is not affected by any airworthiness directive.

## seed-011: Affected 3rd-stage HPC blades installed, no shop visit since the AD took effect

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-012: Later-standard 3rd-stage HPC blades installed

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-013: Blades exposed after the effective date during a visit inducted before it

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-014: HPC rotor exposed after the effective date but no 3rd-stage blade removed

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-015: Asked while only the proposed rule existed

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-016: Air carrier with an A5 engine whose program is not yet revised

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-017: A5 engine where air-carrier status is unknown

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-018: Listed hub, asked after publication but before the effective date

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-019: Hub already past its removal limit on the effective date

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-020/2021-11960: Asked between the replacing AD's publication and its effective date

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-020/2022-02574: Asked between the replacing AD's publication and its effective date

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-021: Disk applicability lives in an unavailable service bulletin

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-022/2021-14268: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-022/2021-11960: Listed disk installed, but the inspection procedure is in an unavailable bulletin

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-023/2025-18469: One engine under three directives at once

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-023/2026-16954: One engine under three directives at once

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-023/2025-17066: One engine under three directives at once

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-024: Listed serial number on the wrong part number

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

## seed-025: CFM56 engine from a mixed A320-family fleet

- **Fields:** applicability `outside_supported_scope`, action_status `None`, authority `in_force`
- **Expected:** applicability `outside_supported_scope`, action_status `None`
- **Summary:** The recorded engine model CFM56-5B4/3 is outside the supported IAE V2500 model scope of this screen, so no applicability determination is made under final rule 2025-17066. The rule is in force on the question date, but no action, deadline, or compliance status is stated for this engine.
- **Note:** Screening aid only: this output is not a compliance determination, a return-to-service statement, or an operator AD status record.
- **Note:** The engine record is marked synthetic and engine_model reads CFM56-5B4/3, which is not on the supported list (IAE V2522-A5, V2524-A5, V2525-D5, V2527-A5, V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2531-E5, V2533-A5).
- **Note:** installed_components and events are both empty; they were not evaluated because the model is outside scope, and empty lists are not evidence that any part is absent or unaffected.
- **Note:** operator.air_carrier_operation reads 'yes'; it would bear on paragraph (g)(2) only for an in-scope engine and does not change the scope result here.
- **Note:** Document 2024-26092 is a notice of proposed rulemaking only; the operative text on the question date is final rule 2025-17066, effective October 10, 2025.
- **Note:** No cycle count, deadline, or component cycles remaining is computed, since no applicability determination is made for this engine.
- **Note:** If the engine_model entry is a recording error, the record would need correction to a supported model before this screen could be rerun; this screen does not assume a different model.

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

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)
