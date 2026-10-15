# Stand-In Proofread: Changed Fields

One line per changed field, written by the proofreading agents under
[`PROOFREAD_BRIEF.md`](PROOFREAD_BRIEF.md) (`PREREGISTRATION.md`,
deviation 7). Four Claude Opus 5.5 agents, four directives each, worked
from each draft and its recorded request only. Every reviewed record
validated against the schema and the serial guard, and a leaf-by-leaf
diff against its draft (`coverage-drafts-opus-5-5-high-20261015T195012Z`)
matches these lines. One agent also ran a read-only listing of its
three input folders before starting, outside the brief's
validate-only rule; it opened nothing outside them.

**Total: 23 changed fields across 8 of 16 directives.**

## 2012-12329 (0 changed)

No changes.

## 2013-08448 (0 changed)

No changes.

## 2015-12068 (1 changed)

- notes[7]: "The preamble names drum P/Ns 6A8316 and 6B1404. The regulatory text prints no drum part number, so the drum part group has no P/Ns." → "The preamble of the superseded AD 2012-09-09 (FR Doc 2012-12329) names drum P/Ns 6A8316 and 6B1404; the 2015-12068 preamble does not. The regulatory text prints no drum part number, so the drum part group has no P/Ns." Reason: the citation pointed at the wrong document. P/Ns 6A8316 and 6B1404 appear only in the 2012-12329 preamble ("Request To Include All HPC Stage 3 to 8 Drum P/N Possibilities"); the 2015-12068 preamble and regulatory text print neither.

## 2016-21061 (8 changed)

- required_actions[0].dependencies: [] → ["nmsb_0661_r2_table1"]. Reason: 2016-21061 paragraph (c)(1) limits the HPT stage 1 hub, P/N 2A5001, to S/Ns listed in Table 1, Appendix A, of IAE NMSB V2500-ENG-72-0661, Revision 2, which the text does not print; that list decides whether the (e)(1)(i) inspection applies to a hub (brief item 6).
- required_actions[1].dependencies: [] → ["nmsb_0661_r2_table1"]. Reason: 2016-21061 paragraph (c)(1); the Table 1 serial list decides whether the (e)(1)(ii) inspection applies to a stage 1 hub.
- required_actions[2].dependencies: [] → ["nmsb_0661_r2_table1"]. Reason: 2016-21061 paragraph (c)(1); the Table 1 serial list decides whether the (e)(1)(iii) inspection applies to a stage 1 hub.
- required_actions[3].dependencies: [] → ["nmsb_0661_r2_table1"]. Reason: 2016-21061 paragraph (c)(1); the Table 1 serial list decides whether the (e)(1)(iv) inspection applies to a stage 1 hub.
- required_actions[4].dependencies: [] → ["nmsb_0661_r2_table2"]. Reason: 2016-21061 paragraph (c)(2) limits the HPT stage 2 hub, P/N 2A4802, to S/Ns listed in Table 2, Appendix A, of IAE NMSB V2500-ENG-72-0661, Revision 2, which the text does not print; that list decides whether the (e)(1)(i) inspection applies to a hub.
- required_actions[5].dependencies: [] → ["nmsb_0661_r2_table2"]. Reason: 2016-21061 paragraph (c)(2); the Table 2 serial list decides whether the (e)(1)(ii) inspection applies to a stage 2 hub.
- required_actions[6].dependencies: [] → ["nmsb_0661_r2_table2"]. Reason: 2016-21061 paragraph (c)(2); the Table 2 serial list decides whether the (e)(1)(iii) inspection applies to a stage 2 hub.
- required_actions[7].dependencies: [] → ["nmsb_0661_r2_table2"]. Reason: 2016-21061 paragraph (c)(2); the Table 2 serial list decides whether the (e)(1)(iv) inspection applies to a stage 2 hub.

## 2017-14706 (0 changed)

No changes.

## 2019-17403 (0 changed)

No changes.

## 2019-19412 (0 changed)

No changes.

## 2020-07627 (1 changed)

- ambiguities[2]: listed ambiguity "Paragraph (g)(2) identifies the disks by serial number only and prints no part number ..." (paragraph (g)(2)) → removed. Reason: the text settles this. 2020-07627 (g)(2) applies only to "affected IAE model turbofan engines" and requires removal of "the affected HPT 1st-stage disk", and (c) defines the affected disk as P/N 2A5001 with the listed serial numbers. The record's use of P/N 2A5001 for the (g)(2) group follows the text, not a chosen reading.

## 2021-11960 (0 changed)

No changes.

## 2021-14268 (6 changed)

- ambiguities[0] (paragraph (c)(2), missing comma between PKLBR88708 and PKLBR89452): entry → removed. Reason: 2021-14268 (c)(2) prints two well-formed serial numbers, both recorded; the text settles the list, and "a typo hiding another listing" is not a reading of the printed text.
- ambiguities[3] (paragraph (g)(3), "before further flight"): entry → removed. Reason: 2021-14268 (g)(3) is plain and the entry gives only one reading; the wording is settled.
- ambiguities[4] (paragraph (h)(1), eligibility tables): entry → removed. Reason: 2021-14268 (h)(1) and (h)(2) state the two eligibility prongs plainly; the entry's "readings" restate those prongs rather than competing readings of one wording.
- ambiguities[5] (paragraph (a), emergency AD actual notice): entry → removed. Reason: 2021-14268 (a) settles it (requirements effective on actual notice under Emergency AD 2021-11-51, otherwise July 19, 2021); both "readings" are true at once for different operators, and effective_date.emergency_ad already records it.
- eligible_parts[0] (part_group hpt1_disk_table1, part_numbers []): entry → removed. Reason: 2021-14268 (h) defines a part eligible for installation by NMSB Appendix A listing and USI result and prints no part number; an entry with an empty part-number list could be read as clearing every P/N of the group targeted by the (g)(1) USI.
- eligible_parts[1] (part_group hpt2_disk_table2, part_numbers []): entry → removed. Reason: same, 2021-14268 (h), for the (g)(2) group.

## 2021-15486 (1 changed)

- required_actions[5].limits: [] → [{kind: flight_cycles_after_prior_action, value: 0, role: alternative, paragraph: "(g)(6)", dependency: "", date: null, anchor_offset_days: 0}]. Reason: 2021-15486 paragraph (g)(6) says a disk that does not pass the USI must be removed "before further flight"; the draft recorded no limit for that stated compliance time.

## 2022-02574 (1 changed)

- ambiguities[2]: ambiguity at "(g)(5)" on whether a disk's prior operating history in another model changes the (g)(1), (g)(2), (g)(5), (g)(6) compliance time → removed. Reason: 2022-02574 paragraphs (g)(1), (g)(2), (g)(5) and (g)(6) set the compliance time by the engine model the disk is installed on ("For IAE ... model turbofan engines with an HPT ... disk ... within the compliance time specified in Figure 1 to paragraph (g)(1)"), with no history condition. Only (g)(3) and (g)(4) make operating history decide it, so the text settles this wording (brief item 9). The actions still route to review through the image-only Figure 1 dependency.

## 2024-12594 (0 changed)

No changes.

## 2025-17066 (0 changed)

No changes.

## 2025-18469 (4 changed)

- required_actions[0].combination: whichever_occurs_later → unclear. Reason: 2025-18469 (g) words the compliance time as "at the next engine shop visit after the effective date of this AD before exceeding the applicable removal cycle limit listed in table 1 ... or within 100 flight cycles from the effective date of this AD, whichever occurs later"; the draft itself lists this grouping as an unresolved ambiguity at (g), so encoding one reading (the less conservative one, under which a shop visit inside the first 100 flight cycles does not require removal) settles it silently.
- required_actions[1].combination: whichever_occurs_later → unclear. Reason: same wording, 2025-18469 (g), for the HPT 2nd-stage hub.
- ambiguities[0].description: "... The record encodes the literal grammatical grouping (reading 1). ..." → that sentence removed. Reason: with combination unclear the record no longer encodes reading 1; the (g) wording stays unresolved.
- ambiguities[0].readings[0]: "Reading 1 (encoded): ..." → "Reading 1: ...". Reason: same as above, 2025-18469 (g).

## 2026-16954 (1 changed)

- ambiguities[2]: listed ambiguity "Applicability names P/N 6A8353 and P/N 6A8688 ... a program matching part numbers by prefix would wrongly treat the modified -001 blades as affected" (paragraph (c)) → removed. Reason: the text settles this. 2026-18423 (c) prints P/N 6A8353 and P/N 6A8688 as the affected blades, and (h)(1)(ii) separately names the modified blades P/N 6A8353-001 and P/N 6A8688-001 as parts eligible for installation; the record already carries both exactly as printed. How records format a part number is not ambiguous wording in the directive.
