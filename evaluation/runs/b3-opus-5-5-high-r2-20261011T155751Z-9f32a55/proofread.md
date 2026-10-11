# Proofread: B3 drafted rule records (b3-opus-5-5-high-r2-20261011T155751Z-9f32a55)

Start a timer. For each directive, read the drafted record below against the AD text and mark every field that is wrong or unsupported. Do not look at the reference records or the field scores first. Record the minutes per directive in `proofread.yaml`.

## 2025-18469 (documents given: 2025-10764, 2025-18469)

```json
{
  "ad_number": "AD 2025-19-13",
  "final_rule_document": "2025-18469",
  "governing_document": {
    "document": "2025-18469",
    "reason": "2025-18469 is the final rule (Amendment 39-23153, AD 2025-19-13). The thread has no correction document, so the final rule's regulatory text controls. The proposed rule 2025-10764 does not control."
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
      "description": "An HPT 1st-stage hub or HPT 2nd-stage hub whose P/N and S/N combination is not listed in table 1 to paragraph (g). The definition names no part numbers of its own.",
      "paragraph": "(i)(1)"
    }
  ],
  "required_actions": [
    {
      "paragraph": "(g)",
      "description": "For engines with an installed part whose P/N and S/N are identified in table 1 to paragraph (g): remove the affected part from service and replace it with a part eligible for installation. This is due at the next engine shop visit after the effective date, before exceeding the applicable removal cycle limit in table 1, or within 100 flight cycles from the effective date, whichever occurs later.",
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
      "description": "After the effective date of the AD, do not install in any engine an HPT 1st-stage hub or HPT 2nd-stage hub that has a P/N and S/N listed in table 1 to paragraph (g).",
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
      "description": "The compliance time names three elements: the next engine shop visit after the effective date, before exceeding the table 1 removal cycle limit, and within 100 flight cycles from the effective date. These are joined by a single 'whichever occurs later', with no punctuation showing which elements are being compared. This decides whether removal is forced without a shop visit and what the latest permissible removal point is.",
      "readings": [
        "Reading 1: The deadline is the later of (a) reaching the part's table 1 removal cycle limit (cycles since new) and (b) 100 flight cycles after the effective date. The part must be removed at the next engine shop visit after the effective date, or by that deadline if no shop visit happens first.",
        "Reading 2: 'Whichever occurs later' compares 'at the next engine shop visit after the effective date, before exceeding the removal cycle limit' with 'within 100 flight cycles from the effective date'. Removal is due at the later of those two points.",
        "Reading 3: Removal is required only at the next engine shop visit after the effective date. The cycle limit / 100 flight cycle clause only qualifies how late that shop visit may occur."
      ]
    },
    {
      "paragraph": "(i)(2)",
      "description": "The engine shop visit definition refers to 'separation of any major mating engine flanges, H-P'. This decides whether a given maintenance event is a shop visit, and so when paragraph (g) comes due.",
      "readings": [
        "Reading 1: 'H-P' means the range of major mating flanges from H through P inclusive.",
        "Reading 2: 'H-P' names only the two flanges H and P, or a single flange designated H-P."
      ]
    }
  ],
  "notes": [
    "No correction document is in the thread. The final rule's regulatory text matches the NPRM (2025-10764), except that paragraph (a) changed from Comments Due Date to Effective Date. The preamble states the AD was adopted as proposed except for minor editorial changes.",
    "The applicability paragraph (c) covers all listed engine models with no part condition. Paragraph (g) applies only to engines with an installed part whose P/N and S/N combination appears in table 1. Screening must match both P/N and S/N, not P/N alone.",
    "The installation prohibition in paragraph (h) applies to all engines within the applicability. The preamble response to comments confirms the applicability was deliberately kept to all listed models so that this prohibition reaches every engine.",
    "HPT 1st-stage hub S/N PKLBSK9287 has a removal cycle limit of only 100 cycles since new. The 100 flight cycles after the effective date limit in paragraph (g) may control for it, depending on how the compliance time is read.",
    "The table 1 title reads 'Affected HPT 1st Stage and HPT 2nd Stage Hubs'. The row component names are written 'HPT 1st-stage hub' and 'HPT 2nd-stage hub', and those are the names recorded here.",
    "The preamble estimates two U.S.-registered engines are affected, both needing HPT 1st-stage hub replacement and none needing HPT 2nd-stage hub replacement.",
    "No material is incorporated by reference (paragraph (l)). Paragraph (b) lists no affected ADs."
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
    "reason": "Document 2026-18423 is a correction to AD 2026-17-03 that republishes the entire regulatory text. It corrects a typographical error in paragraph (g). Its text controls wherever it differs from the final rule 2026-16954. The only difference is in paragraph (g)."
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
      "description": "A 3rd stage HPC rotor blade having P/N 6C8368, 6C8403, or later approved P/N. The 'later approved P/N' clause is open-ended and cannot be screened as a fixed list.",
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
      "description": "Paragraph (g) uses the phrase 'where the 3rd stage HPC rotor blade is exposed'. It does not use the defined term '3rd stage HPC rotor blade exposure' from (h)(2), and no paragraph of the governing text uses that defined term. It is therefore unclear whether (h)(2) sets the condition for (g). This affects which shop visits trigger the replacement.",
      "readings": [
        "The condition is met only when any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum, applying the (h)(2) definition to 'is exposed'.",
        "The condition is met whenever the 3rd stage HPC rotor blades are made accessible or visible during the shop visit (for example, by HPC case or module disassembly), even if no blade is removed from the drum, because 'is exposed' is not the defined term and takes its ordinary meaning."
      ]
    }
  ],
  "notes": [
    "The proposed rule (2025-20088) made the action due 'At the next 3rd stage HPC rotor blade exposure after the effective date'. In response to a United Airlines comment, the final rule changed this to the next engine shop visit after the effective date at which the blade is exposed, and added (h)(3).",
    "The preamble states the FAA does not intend to require compliance for engines inducted into a shop visit before the effective date. (h)(3) defines 'engine shop visit' as the induction of an engine into the shop for maintenance.",
    "Paragraph (g) states no flight-cycle or calendar backstop limit. The action is due only at a qualifying shop visit.",
    "Paragraph (g) requires replacing the full set of 3rd stage HPC rotor blades, not only the blades with P/N 6A8353 or 6A8688. applies_to is recorded as part_condition_parts because the action acts on the 3rd stage HPC rotor blade set named in the part condition.",
    "affected_parts is empty because no required action lists specific parts. The P/Ns 6A8353 and 6A8688 appear only in the applicability paragraph (c) and are recorded as the part condition.",
    "The preamble states that replacing the blades per IAE AG SB V2500-ENG-72-0716, dated October 4, 2024, demonstrates compliance. That service bulletin is not referenced in or incorporated into the regulatory text; paragraph (k) states no material is incorporated by reference.",
    "The preamble notes operators may request an AMOC under (i)(1) to extend the compliance time if parts are unavailable.",
    "Paragraph (f) states 'Comply with this AD within the compliance times specified, unless already done.'",
    "The final rule's Background says P/Ns 6A8353 'and' 6A8688, whereas the regulatory text (c) says 'P/N 6A8353 or P/N 6A8688'. The regulatory text controls.",
    "The correction 2026-18423 states the effective date remains September 24, 2026."
  ]
}
```
