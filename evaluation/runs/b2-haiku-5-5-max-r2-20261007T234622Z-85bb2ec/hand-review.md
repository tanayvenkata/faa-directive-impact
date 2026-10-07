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
- **Summary:** The engine model in the record, PW1133G-JM, is not one of the IAE V2500 models that this screen supports or that the directive's applicability paragraph names, so no applicability determination is made and no action is triggered under Federal Register document 2025-18469.
- **Note:** The record is flagged synthetic and gives engine_model PW1133G-JM with serial number SYN-PW1100-0004; because the model is outside the supported IAE V2500 list, the screen makes no applicability determination and does not assess any hub part or serial number.
- **Note:** The installed_components and events lists are both empty; that emptiness is not treated as evidence that any hub is absent or unaffected, and it does not affect the outcome because the engine is outside scope.
- **Note:** The June 2025 notice of proposed rulemaking (Federal Register document 2025-10764) was a proposal; the final rule 2025-18469 is the operative text for this question and is the only document relied on.
- **Note:** If the model designation is a data-entry error and the engine is actually an IAE V2500 model, rerun the screen with the installed HPT 1st-stage and HPT 2nd-stage hub part and serial numbers, their cycles since new, and the engine shop-visit history, none of which appear in this record.
- **Note:** This output is a screening aid only; it is not a compliance determination and does not state whether the engine is airworthy or approved for return to service.

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
- **Summary:** The engine model V2500-A1 is not one of the IAE V2500 models this screen supports, so no applicability determination is made and the action status is none. Final rule 2025-18469 took effect October 29, 2025, so it is in force as of the 2026-09-26 question date.
- **Note:** Screening aid only: this is not a compliance determination, and no applicability finding is made for engine SYN-V2500-0010 (asset SYN-ENG-010).
- **Note:** The engine record is marked synthetic and carries SYN- identifiers; the engine_model field reads V2500-A1, which is not among the supported models.
- **Note:** No cycle calculation, shop-visit analysis, part-level comparison, or continuing obligation is reported because the engine is outside scope. If the model designation is corrected to a supported model, rerun the screen: it would need to compare the installed HPT 1st-stage hub (P/N 2A5001, S/N PKLBST5011, 2000 cycles since new) with Table 1 to paragraph (g) and review the events list, which is currently empty.
- **Note:** Federal Register document 2025-10764 is the June 13, 2025 NPRM; it was replaced for this question date by final rule 2025-18469 and was not relied on.
- **Note:** No correction or later superseding document was supplied with the question.

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
- **Summary:** The engine model CFM56-5B4/3 is outside the supported IAE V2500 model scope, so no applicability determination is made against AD 2025-17066, which is in force as of the question date. Action status is none under the supported-scope rule.
- **Note:** The record lists engine_model CFM56-5B4/3, which is not in the supported IAE V2500 model list for this screen, so no applicability determination is made.
- **Note:** installed_components and events are empty; no component-cycle, part-match, or shop-visit analysis was performed, and the empty lists are not evidence that any part is absent or unaffected.
- **Note:** The operator air_carrier_operation flag does not change the scope outcome.
- **Note:** The operative text is final rule 2025-17066 (effective October 10, 2025); proposed rule 2024-26092 was not relied on.
- **Note:** The record is marked synthetic; this output is a screening aid only and is not a compliance, airworthiness, or return-to-service determination.

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
