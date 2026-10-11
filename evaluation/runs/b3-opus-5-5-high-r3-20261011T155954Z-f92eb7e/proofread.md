# Proofread: B3 drafted rule records (b3-opus-5-5-high-r3-20261011T155954Z-f92eb7e)

Start a timer. For each directive, read the drafted record below against the AD text and mark every field that is wrong or unsupported. Do not look at the reference records or the field scores first. Record the minutes per directive in `proofread.yaml`.

## 2025-18469 (documents given: 2025-10764, 2025-18469)

```json
{
  "ad_number": "AD 2025-19-13",
  "final_rule_document": "2025-18469",
  "governing_document": {
    "document": "2025-18469",
    "reason": "2025-18469 is the final rule (Amendment 39-23153, AD 2025-19-13). No correction was published in the thread, so its regulatory text controls over the proposed rule 2025-10764."
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
      "description": "A part eligible for installation is an HPT 1st-stage hub or HPT 2nd-stage hub having a P/N and S/N that is not listed in table 1 to paragraph (g). The definition names no eligible part numbers. It excludes only the specific P/N and S/N combinations in table 1.",
      "paragraph": "(i)(1)"
    }
  ],
  "required_actions": [
    {
      "paragraph": "(g)",
      "description": "For engines with an installed part (P/N and S/N) identified in table 1 to paragraph (g): at the next engine shop visit after the effective date, before exceeding the applicable removal cycle limit in table 1 or within 100 flight cycles from the effective date, whichever occurs later, remove the affected part from service and replace it with a part eligible for installation.",
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
      "description": "After the effective date, do not install in any engine an HPT 1st-stage hub or HPT 2nd-stage hub that has a P/N and S/N listed in table 1 to paragraph (g).",
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
      "description": "The sentence joins three timing elements: the next engine shop visit after the effective date, 'before exceeding the applicable removal cycle limit', and 'within 100 flight cycles from the effective date'. These are followed by 'whichever occurs later'. The text does not settle whether the shop visit is one of the alternatives being compared, or how the shop visit relates to the two cycle limits. This changes when removal is due.",
      "readings": [
        "Remove at the next engine shop visit after the effective date, but no later than the later of (a) reaching the table 1 removal cycle limit (cycles since new) and (b) 100 flight cycles after the effective date. Whichever comes first, the shop visit or that backstop, triggers removal.",
        "The deadline is the later of (a) reaching the table 1 removal cycle limit and (b) 100 flight cycles after the effective date. The shop visit only describes where the work is expected to be done, not an earlier trigger.",
        "Removal is required at the next engine shop visit only if that shop visit occurs before the part exceeds its table 1 removal cycle limit. Otherwise removal is due within 100 flight cycles after the effective date. 'Whichever occurs later' compares the shop-visit-before-limit timing with the 100 flight cycle timing."
      ]
    },
    {
      "paragraph": "(i)(2)",
      "description": "The engine shop visit definition refers to 'separation of any major mating engine flanges, H-P' without saying what 'H-P' means. This affects which maintenance events count as an engine shop visit, and so when paragraph (g) is triggered.",
      "readings": [
        "Separation of any major mating flange in the range of flange designations H through P.",
        "Separation of the flanges designated H and P only."
      ]
    }
  ],
  "notes": [
    "No correction documents are in the thread. The final rule's regulatory text matches the proposed rule (2025-10764) except that paragraph (a) changed from 'Comments Due Date' to 'Effective Date'. The final rule states it was adopted as proposed except for minor editorial changes.",
    "Applicability under paragraph (c) covers all listed engine models regardless of installed parts. The FAA declined a comment asking to limit applicability to engines with the affected hubs, so that the paragraph (h) installation prohibition applies to all listed models.",
    "Table 1 is titled 'Affected HPT 1st Stage and HPT 2nd Stage Hubs'. Its removal cycle limits are stated in cycles since new.",
    "HPT 1st-stage hub S/N PKLBSK9287 has a removal cycle limit of only 100 cycles since new. This hub may already be past its limit, which makes the 100 flight cycles from the effective date timing especially relevant to this part.",
    "Paragraph (g) acts on parts identified by both P/N and S/N. A screening program should match the P/N and S/N combination, not the P/N alone, since part numbers 2A5001 and 2A4802 are not affected by themselves.",
    "Paragraph (l) states that no material is incorporated by reference."
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
    "reason": "2026-18423 is a correction to AD 2026-17-03 that republishes the entire regulatory text. It changes paragraph (g) to restore the omitted word \"blade\". As the latest correction that republishes the regulatory text, it controls wherever it differs from the final rule 2026-16954. The only difference is paragraph (g)."
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
      "description": "A 3rd stage HPC rotor blade having P/N 6C8368, 6C8403, or later approved P/N. The \"later approved P/N\" clause is open-ended and is not enumerated in the text.",
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
      "description": "At the next engine shop visit after the effective date of this AD where the 3rd stage HPC rotor blade is exposed, replace the full set of 3rd stage HPC rotor blades with parts eligible for installation (as defined in (h)(1)).",
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
      "description": "Paragraph (g) is conditioned on the shop visit being one \"where the 3rd stage HPC rotor blade is exposed\". It does not use the defined term \"3rd stage HPC rotor blade exposure\" from (h)(2), and no other paragraph uses that defined term. It is therefore unclear whether \"is exposed\" carries the (h)(2) meaning. This decides whether a given shop visit triggers the replacement.",
      "readings": [
        "\"Is exposed\" means a 3rd stage HPC rotor blade exposure as defined in (h)(2): any 3rd stage HPC rotor blade is removed from the HPC stage 3 to 8 drum. A shop visit where the blades become accessible or visible but none is removed from the drum does not trigger the replacement.",
        "\"Is exposed\" has its ordinary meaning, because (g) does not invoke the defined term. Any shop visit where the 3rd stage HPC rotor blades become accessible or visible (for example, the HPC case is opened) triggers the replacement, even if no blade is removed from the drum."
      ]
    }
  ],
  "notes": [
    "2026-18423 republishes the full regulatory text. It differs from the final rule 2026-16954 only in paragraph (g), where \"rotor\" became \"rotor blade\". All other paragraphs are identical, including the effective date of September 24, 2026.",
    "The proposed rule (2025-20088) used a different trigger: \"At the next 3rd stage HPC rotor blade exposure after the effective date of this AD\". The final rule changed it to the shop-visit-based trigger after a comment, and added the (h)(3) definition of \"engine shop visit\" (\"the induction of an engine into the shop for maintenance\"). (h)(2) was carried over from the proposal unchanged.",
    "The final rule preamble states that the FAA does not intend to require compliance for engines inducted into a shop visit before the effective date. The (h)(3) definition ties the shop visit to induction, which is consistent with that statement.",
    "Paragraph (g) states no flight-cycle, calendar, or other backstop limit. The only compliance time is the conditional shop visit, so limits is empty. If the condition never occurs, the text sets no outer deadline.",
    "Paragraph (g) requires replacing the full set of 3rd stage HPC rotor blades, not only individual blades with P/N 6A8353 or 6A8688. The \"part_condition_parts\" classification refers to the stage 3 blades named in (c). The text has no separate list or table of affected parts, so affected_parts is empty.",
    "Screening caution: the applicability P/Ns are 6A8353 and 6A8688. The modified, eligible P/Ns 6A8353-001 and 6A8688-001 in (h)(1)(ii) share these prefixes. A program should not prefix-match 6A8353-001 or 6A8688-001 as applicable P/Ns, since the text treats them as eligible replacement parts.",
    "Eligible parts include \"or later approved P/N\" in (h)(1)(i). Any such later approved P/Ns are not listed in the text and cannot be screened from this record.",
    "The final rule preamble says that replacing the blades per IAE AG SB V2500-ENG-72-0716, dated October 4, 2024, demonstrates compliance because it changes the blades to eligible P/Ns. However, the regulatory text does not reference this SB, and paragraph (k) states that no material is incorporated by reference.",
    "There is no installation prohibition paragraph in the regulatory text. The final rule preamble background says P/Ns \"6A8353 and 6A8688\", while the regulatory text (c) says \"P/N 6A8353 or P/N 6A8688\". The regulatory wording controls.",
    "The preamble notes that an AMOC under (i)(1) may be requested to extend the compliance time if parts are not available in a timely manner."
  ]
}
```
