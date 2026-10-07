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
- **Summary:** Engine model PW1133G-JM is not one of the supported IAE V2500 models, so this screen makes no applicability determination and reports no action under Federal Register document 2025-18469, which is in force as of the question date.
- **Note:** The record lists no installed components and no events; these empty lists are not evidence that any part is absent or unaffected and were not used to clear the engine.
- **Note:** No part matching, cycle computation, or Table 1 comparison was performed because the engine model is outside the supported scope.
- **Note:** The record is flagged synthetic and its serial and asset identifiers carry the SYN- prefix; this is a screening aid, not a compliance determination, and nothing here states the engine is compliant, noncompliant, safe, airworthy, or approved for return to service.
- **Note:** The proposed rule 2025-10764 is not relied on; the final rule 2025-18469 is the governing text.

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

- **No answer:** answer is not JSON: Expecting value: line 1 column 1 (char 0)

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
- **Summary:** The recorded engine model CFM56-5B4/3 is not one of the IAE V2500 models in this screen's supported scope, so no applicability determination is made against final rule 2025-17066 and no action is set. The rule was effective October 10, 2025, so it is in force on the question date, but that does not bring this engine within scope.
- **Note:** The engine record lists engine_model CFM56-5B4/3, which is not among the IAE AG V2500 models named in the directive or in this screen's supported scope, so no applicability determination is made and no AD status is stated for this engine.
- **Note:** Because no applicability determination is made, the paragraph (g)(1) and (g)(2) revisions (the Maintenance Scheduling paragraph B.1 of the ALS in the TLM and the air carrier maintenance or inspection program) were not assessed, and no deadline or cycle count is computed; installed_components and events are empty and were not needed for this outcome.
- **Note:** The air_carrier_operation flag does not change scope, since applicability turns on engine model.
- **Note:** If the engine_model entry is a recording error and the engine is actually one of the ten listed IAE AG models, the screen should be rerun on the corrected record; the 90-day window in paragraph (g) ran from October 10, 2025 and ended January 8, 2026, so the rerun would need operator records showing whether those revisions were made.
- **Note:** The proposed rule 2024-26092 was replaced by final rule 2025-17066 and was not relied on.
- **Note:** The record is flagged synthetic and its identifiers carry the SYN- prefix.
- **Unresolved locator:** 2025-17066 (c) Applicability paragraph listing IAE AG Model V2522-A5, V2524-A5, V2525-D5, V2527-A5, V2527E-A5, V2527M-A5, V2528-D5, V2530-A5, V2531-E5, and V2533-A5 engines

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
