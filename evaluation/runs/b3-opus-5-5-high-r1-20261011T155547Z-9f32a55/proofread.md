# Proofread: B3 drafted rule records (b3-opus-5-5-high-r1-20261011T155547Z-9f32a55)

Start a timer. For each directive, read the drafted record below against the AD text and mark every field that is wrong or unsupported. Do not look at the reference records or the field scores first. Record the minutes per directive in `proofread.yaml`.

## 2025-18469 (documents given: 2025-10764, 2025-18469)

```json
{
  "ad_number": "AD 2025-19-13",
  "final_rule_document": "2025-18469",
  "governing_document": {
    "document": "2025-18469",
    "reason": "2025-18469 is the final rule (Amendment 39-23153, AD 2025-19-13). The thread contains no correction document, so the final rule's regulatory text controls over the proposed rule (2025-10764)."
  },
  "corrections": [],
  "effective_date": {
    "date": "2025-10-29",
    "paragraph": "(a)"
  },
  "applicability": {
    "engine_models": [
      "V2522-A5",
      "V2524-A5",
      "V2525-D5",
      "V2527-A5",
      "V2527E-A5",
      "V2527M-A5",
      "V2528-D5",
      "V2530-A5",
      "V2531-E5",
      "V2533-A5"
    ],
    "models_paragraph": "(c)",
    "part_condition": {
      "component": "",
      "part_numbers": [],
      "paragraph": "(c)"
    }
  },
  "affected_parts": [
    {
      "component": "HPT 1st-stage hub",
      "part_number": "2A5001",
      "serial_number": "PKLBSK9287",
      "removal_limit_cycles_since_new": 100,
      "paragraph": "(g)"
    },
    {
      "component": "HPT 1st-stage hub",
      "part_number": "2A5001",
      "serial_number": "PKLBSS9200",
      "removal_limit_cycles_since_new": 4800,
      "paragraph": "(g)"
    },
    {
      "component": "HPT 1st-stage hub",
      "part_number": "2A5001",
      "serial_number": "PKLBST5011",
      "removal_limit_cycles_since_new": 5500,
      "paragraph": "(g)"
    },
    {
      "component": "HPT 1st-stage hub",
      "part_number": "2A5001",
      "serial_number": "PKLBST7489",
      "removal_limit_cycles_since_new": 6200,
      "paragraph": "(g)"
    },
    {
      "component": "HPT 2nd-stage hub",
      "part_number": "2A4802",
      "serial_number": "PKLBST5005",
      "removal_limit_cycles_since_new": 4000,
      "paragraph": "(g)"
    },
    {
      "component": "HPT 2nd-stage hub",
      "part_number": "2A4802",
      "serial_number": "PKLBSS9840",
      "removal_limit_cycles_since_new": 3900,
      "paragraph": "(g)"
    },
    {
      "component": "HPT 2nd-stage hub",
      "part_number": "2A4802",
      "serial_number": "PKLBSS0301",
      "removal_limit_cycles_since_new": 5000,
      "paragraph": "(g)"
    },
    {
      "component": "HPT 2nd-stage hub",
      "part_number": "2A4802",
      "serial_number": "PKLBSR2100",
      "removal_limit_cycles_since_new": 6000,
      "paragraph": "(g)"
    }
  ],
  "eligible_parts": [
    {
      "component": "HPT 1st-stage hub or HPT 2nd-stage hub",
      "part_numbers": [],
      "description": "A \"part eligible for installation\" is an HPT 1st-stage hub or HPT 2nd-stage hub having a P/N and S/N that is not listed in table 1 to paragraph (g) of this AD. The definition names no part numbers of its own. It works by excluding the P/N and S/N combinations in table 1.",
      "paragraph": "(i)(1)"
    }
  ],
  "required_actions": [
    {
      "paragraph": "(g)",
      "description": "For engines with an installed part (P/N and S/N) identified in table 1 to paragraph (g), remove the affected part from service and replace it with a part eligible for installation. The action is due at the next engine shop visit after the effective date, before exceeding the applicable removal cycle limit in table 1 or within 100 flight cycles from the effective date, whichever occurs later.",
      "applies_to": "listed_parts",
      "trigger": "next_shop_visit_after_effective_date",
      "shop_visit_definition_paragraph": "(i)(2)",
      "condition_description": "",
      "condition_definition_paragraph": "",
      "limits": [
        {
          "kind": "listed_part_cycles_since_new",
          "value": null
        },
        {
          "kind": "flight_cycles_after_effective_date",
          "value": 100
        }
      ],
      "combination": "unclear"
    }
  ],
  "installation_prohibitions": [
    {
      "paragraph": "(h)",
      "description": "After the effective date of this AD, do not install in any engine an HPT 1st-stage hub or HPT 2nd-stage hub that has a P/N and S/N listed in table 1 to paragraph (g).",
      "applies_to": "listed_parts"
    }
  ],
  "definitions": [
    {
      "term": "part eligible for installation",
      "paragraph": "(i)(1)"
    },
    {
      "term": "engine shop visit",
      "paragraph": "(i)(2)"
    }
  ],
  "amoc_paragraph": "(j)",
  "ambiguities": [
    {
      "paragraph": "(g)",
      "description": "Paragraph (g) states three timing elements in one clause: the next engine shop visit after the effective date, the table 1 removal cycle limit (cycles since new), and 100 flight cycles from the effective date. It then says \"whichever occurs later\". It is unclear whether \"whichever occurs later\" compares only the two numeric limits or all three elements, and how the shop visit relates to the limits.",
      "readings": [
        "Reading 1: Remove the part at the next engine shop visit after the effective date. In any event, remove it no later than the later of (a) reaching its table 1 cycles-since-new limit and (b) 100 flight cycles after the effective date. Under this reading the shop visit applies if it comes first, and the later of the two limits is the backstop.",
        "Reading 2: \"Whichever occurs later\" compares all three elements. Removal is due at the latest of the next shop visit, the table 1 cycles-since-new limit, and 100 flight cycles after the effective date.",
        "Reading 3: The shop visit only names where the removal is done, not a separate deadline. Removal is due at the later of the table 1 cycles-since-new limit and 100 flight cycles after the effective date, and it must be done at a shop visit that occurs before that point."
      ]
    },
    {
      "paragraph": "(i)(2)",
      "description": "The engine shop visit definition says \"separation of any major mating engine flanges, H-P\". The meaning of \"H-P\" is not explained. This affects which maintenance inductions count as a shop visit and so when the paragraph (g) action becomes due.",
      "readings": [
        "Reading 1: Only separation of major mating flanges designated H through P counts as an engine shop visit.",
        "Reading 2: \"H-P\" refers to high-pressure section flanges, so only separation of high-pressure major mating flanges counts.",
        "Reading 3: \"H-P\" is a descriptive or editorial label, and separation of any major mating engine flange counts."
      ]
    }
  ],
  "notes": [
    "No correction document is in the thread. The final rule's regulatory text (paragraphs (a) through (l)) matches the proposed rule 2025-10764 in substance. The only difference is that paragraph (a) changed from the comments due date to the effective date. The preamble states the AD was adopted as proposed except for minor editorial changes.",
    "Applicability under paragraph (c) covers all engines of the listed models, with no part condition. The table 1 parts list appears only in required action (g) and installation prohibition (h). The preamble confirms the FAA declined to limit applicability so that the installation prohibition applies to all listed models.",
    "Model names are given as written after the \"IAE AG Model\" prefix in paragraph (c). The full text reads \"International Aero Engines AG (IAE AG) Model V2522-A5, ...\".",
    "Removal cycle limits in table 1 are written with thousands separators (for example \"4,800\"). They are recorded here as integers.",
    "HPT 1st-stage hub S/N PKLBSK9287 has a removal cycle limit of only 100 cycles since new. The proofreader should confirm this value against the source table, since the part may already exceed it, which would make the 100-flight-cycle grace period controlling.",
    "Paragraph (g) does not state whether \"100 flight cycles from the effective date\" is counted on the engine or on the affected part.",
    "Paragraph (l) states no material is incorporated by reference."
  ]
}
```

## 2026-16954 (documents given: 2025-20088, 2026-16954, 2026-18423)

```json
{
  "ad_number": "AD 2026-17-03",
  "final_rule_document": "2026-16954",
  "governing_document": {
    "document": "2026-18423",
    "reason": "2026-18423 is a correction to AD 2026-17-03 that republishes the entire regulatory text. It changes paragraph (g) by restoring the omitted word \"blade\". As the latest correction that republishes the regulatory text, its text controls wherever it differs from final rule 2026-16954. All other paragraphs are identical to the final rule."
  },
  "corrections": [
    {
      "document": "2026-18423",
      "paragraph": "(g)",
      "original_text": "At the next engine shop visit after the effective date of this AD where the 3rd stage HPC rotor is exposed, replace the full set of 3rd stage HPC rotor blades with parts eligible for installation.",
      "corrected_text": "At the next engine shop visit after the effective date of this AD where the 3rd stage HPC rotor blade is exposed, replace the full set of 3rd stage HPC rotor blades with parts eligible for installation."
    }
  ],
  "effective_date": {
    "date": "2026-09-24",
    "paragraph": "(a)"
  },
  "applicability": {
    "engine_models": [
      "V2522-A5",
      "V2524-A5",
      "V2525-D5",
      "V2527-A5",
      "V2527E-A5",
      "V2527M-A5",
      "V2528-D5",
      "V2530-A5",
      "V2531-E5",
      "V2533-A5"
    ],
    "models_paragraph": "(c)",
    "part_condition": {
      "component": "3rd stage high-pressure compressor (HPC) rotor blade",
      "part_numbers": [
        "6A8353",
        "6A8688"
      ],
      "paragraph": "(c)"
    }
  },
  "affected_parts": [],
  "eligible_parts": [
    {
      "component": "3rd stage HPC rotor blade",
      "part_numbers": [
        "6C8368",
        "6C8403"
      ],
      "description": "A 3rd stage HPC rotor blade having P/N 6C8368, 6C8403, or later approved P/N. The definition is open-ended: any later approved P/N also qualifies.",
      "paragraph": "(h)(1)(i)"
    },
    {
      "component": "3rd stage HPC rotor blade",
      "part_numbers": [
        "6A8353-001",
        "6A8688-001"
      ],
      "description": "A 3rd stage HPC rotor blade modified to P/N 6A8353-001 or P/N 6A8688-001.",
      "paragraph": "(h)(1)(ii)"
    }
  ],
  "required_actions": [
    {
      "paragraph": "(g)",
      "description": "At the next engine shop visit after the effective date of this AD where the 3rd stage HPC rotor blade is exposed, replace the full set of 3rd stage HPC rotor blades with parts eligible for installation.",
      "applies_to": "part_condition_parts",
      "trigger": "next_shop_visit_after_effective_date_with_condition",
      "shop_visit_definition_paragraph": "(h)(3)",
      "condition_description": "The 3rd stage HPC rotor blade is exposed at that engine shop visit.",
      "condition_definition_paragraph": "(h)(2)",
      "limits": [],
      "combination": "single"
    }
  ],
  "installation_prohibitions": [],
  "definitions": [
    {
      "term": "part eligible for installation",
      "paragraph": "(h)(1)"
    },
    {
      "term": "3rd stage HPC rotor blade exposure",
      "paragraph": "(h)(2)"
    },
    {
      "term": "engine shop visit",
      "paragraph": "(h)(3)"
    }
  ],
  "amoc_paragraph": "(i)",
  "ambiguities": [
    {
      "paragraph": "(g)",
      "description": "Paragraph (g) conditions the action on a shop visit \"where the 3rd stage HPC rotor blade is exposed.\" That phrase is not the term defined in (h)(2), \"3rd stage HPC rotor blade exposure,\" which means removal of any 3rd stage HPC rotor blade from the HPC stage 3 to 8 drum. The text does not say whether the (h)(2) definition governs \"is exposed\" in (g). This determines which shop visits trigger the replacement.",
      "readings": [
        "The (h)(2) definition applies: the replacement is due at the first engine shop visit, inducted after the effective date, at which any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum.",
        "\"Exposed\" carries its ordinary meaning, which is broader than removal from the drum (for example, the blades become accessible or visible when the HPC is opened). Under this reading the replacement could be due at a shop visit where no blade is removed from the drum."
      ]
    }
  ],
  "notes": [
    "affected_parts is empty. No required action contains a list or table of specific parts. The P/Ns 6A8353 and 6A8688 appear only in the applicability paragraph (c), so they are recorded as the part condition.",
    "Paragraph (g) requires replacing the full set of 3rd stage HPC rotor blades, not only the individual blades having P/N 6A8353 or 6A8688. applies_to is coded part_condition_parts because the action targets the 3rd stage HPC rotor blades named in the part condition. The proofreader should confirm that this coding captures the full-set scope.",
    "No flight-cycle, calendar or other hard compliance limit is stated. The only compliance time is the conditional shop-visit trigger in (g). Paragraph (f) states \"Comply with this AD within the compliance times specified, unless already done.\"",
    "An \"engine shop visit\" is defined in (h)(3) as the induction of an engine into the shop for maintenance. The final-rule preamble states it is not the FAA's intent to require engines inducted into a shop visit before the effective date to comply.",
    "The proposed rule (2025-20088) used a different trigger: \"At the next 3rd stage HPC rotor blade exposure after the effective date of this AD.\" The final rule changed (g) to a shop-visit trigger and added (h)(3) in response to a United Airlines comment. The (h)(2) definition was retained even though (g) no longer uses that exact term.",
    "The final-rule preamble states that replacing the blades per IAE AG SB V2500-ENG-72-0716, dated October 4, 2024, demonstrates compliance. That SB is not referenced in the regulatory text. Paragraph (k) states no material is incorporated by reference.",
    "The eligible-part definition in (h)(1)(i) includes \"or later approved P/N\". A screening program cannot resolve this from the listed P/Ns alone.",
    "No paragraph of the AD prohibits installation of parts.",
    "The only change made by correction 2026-18423 is in (g); the effective date remains September 24, 2026.",
    "The final-rule preamble estimates 1,462 affected U.S.-registry engines; the NPRM estimated 1,496."
  ]
}
```
