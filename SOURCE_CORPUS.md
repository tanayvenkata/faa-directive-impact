# Initial FAA Source Corpus

## Purpose

This is the reading guide for the FAA feasibility slice. The six documents below form the first protected evaluation core: three real proposed-to-final rule threads concerning International Aero Engines V2500-family engines.

They are not the complete FAA discovery corpus. Their purpose is to establish the source structure, authority and time states, directive predicates, required fleet fields, and proposed-to-final relationships before implementation begins.

Corpus selection was verified on **2026-08-23**. The HPT hub thread's live
representations were rechecked on **2026-09-01**. See
[`SOURCE_REVIEW_HPT_HUB.md`](SOURCE_REVIEW_HPT_HUB.md). Recheck each remaining
record when it is reviewed or acquired.

## Source Hierarchy

Use each source for a distinct role:

1. **Federal Register API JSON** — discovery metadata, identifiers, dates, docket metadata, and canonical representation URLs. The API is public and does not require a key.
2. **Federal Register XML** — preferred initial parsing representation because it preserves headings, paragraphs, printed-page markers, and table structure.
3. **Federal Register HTML** — evidence-addressing projection because it adds paragraph and heading IDs plus printed-page metadata. It must be checked against the XML and official edition rather than treated as an independent authority.
4. **GovInfo official PDF** — official published edition retained for authority and visual verification. Follow the PDF link exposed by each Federal Register record.
5. **FAA Dynamic Regulatory System (DRS)** — FAA document identity, current/historical status, related versions, and FAA-specific metadata. Reproducible API acquisition appears to require a DRS API key and remains to be verified.
6. **Incorporated material** — record the exact named artifact and version. If it is not legally and reproducibly available, mark it unavailable; do not reconstruct it.

Starting points:

- [Federal Register API documentation](https://www.federalregister.gov/developers/documentation/api/v1)
- [FAA Dynamic Regulatory System](https://drs.faa.gov/)
- [FAA Airworthiness Directives](https://www.faa.gov/regulations_policies/airworthiness_directives)

## Six-Document Protected Core

### Thread 1: Compressor rotor blades

- [Proposed rule — Federal Register document 2025-20088](https://www.federalregister.gov/documents/2025/11/18/2025-20088/airworthiness-directives-international-aero-engines-ag-engines)
- [Final rule — AD 2026-17-03, Federal Register document 2026-16954](https://www.federalregister.gov/documents/2026/08/20/2026-16954/airworthiness-directives-international-aero-engines-ag-engines)

Read for:

- differences between proposed and final authority;
- engine-model and installed blade part-number predicates;
- the effective date;
- the next-shop-visit condition;
- what it means for the compressor rotor to be exposed;
- replacement-part eligibility;
- comments or changes between proposal and final rule.

Status: live representation review complete. The final rule made the trigger
more precise by requiring the next engine shop visit after the effective date
where the rotor is exposed and added a definition of engine shop visit. See
[`SOURCE_REVIEW_REMAINING_THREADS.md`](SOURCE_REVIEW_REMAINING_THREADS.md).

### Thread 2: HPT hub quality escape

- [Proposed rule — Federal Register document 2025-10764](https://www.federalregister.gov/documents/2025/06/13/2025-10764/airworthiness-directives-international-aero-engines-ag-engines)
- [Final rule — AD 2025-19-13, Federal Register document 2025-18469](https://www.federalregister.gov/documents/2025/09/24/2025-18469/airworthiness-directives-international-aero-engines-ag-engines)

Read for:

- engine-model applicability;
- installed HPT hub part and serial numbers;
- cycles-since-new predicates and tables;
- shop-visit, removal, and compliance timing;
- how an affected serial list is represented;
- changes between proposal and final rule.

Status: first live representation review complete. The review found structured
tables in both XML and HTML, a stable docket/project relationship, unchanged
codified applicability and action predicates, and a separate continuing
installation prohibition. See
[`SOURCE_REVIEW_HPT_HUB.md`](SOURCE_REVIEW_HPT_HUB.md).

### Thread 3: Airworthiness-limitations revision

- [Proposed rule — Federal Register document 2024-26092](https://www.federalregister.gov/documents/2024/11/12/2024-26092/airworthiness-directives-international-aero-engines-ag-engines)
- [Final rule — AD 2025-17-16, Federal Register document 2025-17066](https://www.federalregister.gov/documents/2025/09/05/2025-17066/airworthiness-directives-international-aero-engines-ag-engines)

Read for:

- model-family-specific applicability;
- the required airworthiness-limitations/manual task;
- the 90-day program-revision requirement;
- air-carrier maintenance-program state;
- publication date versus effective date;
- changes between proposal and final rule.

Status: live representation review complete. The final rule corrected a
nonexistent task reference and separated the ICA/TLM revision from the
additional air-carrier maintenance-program obligation. See
[`SOURCE_REVIEW_REMAINING_THREADS.md`](SOURCE_REVIEW_REMAINING_THREADS.md).

## Evidence-Sufficiency Challenge Records

These are not part of the six-document core, but they should enter the later curated retrieval corpus because the correct behavior depends on recognizing incomplete public evidence.

- [Federal Register document 2022-02574](https://www.federalregister.gov/documents/2022/02/08/2022-02574/airworthiness-directives-international-aero-engines-ag-turbofan-engines) — depends on named IAE non-modification service bulletins for affected serial lists and inspection instructions.
- [Federal Register document 2021-14268](https://www.federalregister.gov/documents/2021/07/02/2021-14268/airworthiness-directives-international-aero-engines-ag-turbofan-engines) — includes affected serials in the directive but still requires incorporated service instructions to perform the inspection.

The safe public behavior is to state what the directive itself establishes, identify the required external artifact and version, and mark the action evidence incomplete pending authorized access.

Status: challenge-record spot check complete. The public directives identify
the incorporated materials and some affected-part facts, but required serial
lists, inspection procedures, and compliance figures cross into manufacturer
materials or image-only Federal Register graphics. See
[`SOURCE_REVIEW_REMAINING_THREADS.md`](SOURCE_REVIEW_REMAINING_THREADS.md).

## Reading Checklist

For each of the six documents, record:

- Federal Register document number;
- rule type and authority state;
- AD, docket, amendment, RIN, and project identifiers;
- publication and effective dates;
- affected or superseded directives;
- applicable engine models;
- component, part-number, and serial-number predicates;
- date, cycle, inspection, shop-visit, or program-state predicates;
- required actions and conditional timing;
- tables and exact paragraph regions supporting each predicate;
- incorporated materials and their exact versions;
- proposal-to-final changes;
- questions or interpretations that cannot be labeled confidently without a practitioner.

## Boundary While Reading

- Supported applicability remains IAE V2500-A5/D5/E5 variants.
- PW1100G and PW1400G are out of scope except as retrieval negatives.
- Do not infer family membership that the selected authoritative sources do not establish.
- Do not interpret the system as determining compliance, maintenance adequacy, an alternative method of compliance, or return to service.
- Do not begin implementation or choose a stack merely to match a presumed source shape. Inspect the actual API responses, XML/HTML, PDFs, tables, and identifiers first.

## After Reading

The protected-core source review is complete. The resulting feasibility
decision is recorded in [`FEASIBILITY_RECOMMENDATION.md`](FEASIBILITY_RECOMMENDATION.md).
Before implementation, the remaining work is to:

1. perform the first immutable acquisition under the raw-manifest contract;
2. write the feasibility-seed cases and numerical evaluation gates;
3. decide how image-only figures are transcribed and reviewed;
4. verify FAA DRS external API access and identity fields; and
5. discuss the smallest credible acquisition and parsing stack.
