# Gate Research, 2026-10-06

Three research passes ran before gates version 1 was frozen. Each looked for
evidence that would add, remove, or justify a gate:

1. FAA and EASA rules on AD applicability and records.
2. Documented real-world failures in AD applicability and compliance.
3. Commercial AD-tracking software, published research, and precedents from
   other safety-critical screening fields.

Each finding below lists its source. **[P]** means the primary text was read,
**[S]** means a secondary source was read, and **[snip]** means only a search
summary was seen. Statements marked "Inference" are the project's reading, not
the source's.

## Rules

- **[P] 14 CFR 39.15.** "an airworthiness directive applies to each product
  identified in the airworthiness directive, even if an individual product has
  been changed by modifying, altering, or repairing it in the area addressed by
  the airworthiness directive."
  → Gate 1 note; seed-026.
- **[P] 14 CFR 39.17.** A change that affects the required actions needs an
  approved AMOC.
- **[P] 14 CFR 39.19.** An AMOC may be used "only if the manager approves it",
  and it may change the compliance time.
  → seed-027.
- **[P] 14 CFR 39.27.** An incorporated service document becomes part of the
  AD, and the AD prevails where the two conflict.
  → Supports routing missing incorporated material to review (gate 3).
- **[P] AC 39-7D.**
  - ¶9: if no serial numbers are listed, all are affected.
  - ¶9c: "In no case does the presence of any alteration, modification, or
    repair remove any product from the applicability of this AD."
  - ¶11b: cycle definition.
  - ¶15a: the "revision date" is the effective date of the latest amendment.
  - ¶7b: a final rule with a request for comments is immediately adopted.
  - ¶7c: an emergency AD binds on actual notice.
  → Gate 7 now checks both directions; the uncovered cases are listed as
  known gaps.
- **[P] FAA AD Manual FAA-IR-M-8040.1C, chapter 8.**
  - "within X" includes X; "before … accumulates X" excludes it.
  - "calendar months" run to month end.
  - Engine cycles follow the AD's definition, or else the service document's.
  - Credit for "unless already done" work is limited to what the AD states.
  - AMOCs carry over to a revised or superseding AD only if that AD includes
    them.
  → Gate 8 note; the "already done" rule in the gate 1 note.
- **[P] AC 39-9.**
  - Rotable spares must be checked so that noncompliant spares are not
    installed.
  - AD status is not the same as the record of accomplishment.
  → Standing forbidden claims.
- **[P] 14 CFR 91.417(a)(2)(v), 121.380(a)(2)(vi).** AD records hold status,
  method of compliance, AD number and revision date, and the next due time for
  recurring actions.
  → Known gap: recurring and terminating actions.
- **[P] EASA AMC M.A.305(c)1(b).** An AD that is generally applicable but does
  not apply to a particular product "should be identified with the reason why
  it is not applicable".
  → Gate 10: every clear must cite its reason.
- **Not read.** FAA Order 8900.1 Vol 3 Ch 59 (inspector guidance), because
  FSIMS did not resolve.

## Documented Failures

- **[S] Hawaiian Airlines, 2014 proposed civil penalty ($547,500).** Records
  "erroneously showed" a 767 thrust-reverser AD did not apply, from 2004 to
  2012.
  → seed-028.
- **[P] DOT OIG AV2020019 (Southwest used 737s, 2020).** It found 44 AMOCs
  "previously unknown". FAA designees relied on summary data supplied by the
  air carrier.
  → seed-027.
- **[P] FAA AD Compliance Review Team reports (2009).**
  - Carriers did SB work before the AD was issued and did not re-check it
    against the final AD.
  - Carriers were often unaware of global AMOCs.
  - Normal maintenance sometimes undid AD compliance.
  - Literal readings grounded aircraft over trivial deviations.
  → Gate 12 rationale. Proposal-era work is a known gap; for AD 2025-19-13 the
  proposal and final rule are identical, which was checked in the frozen
  generation.
- **[S] Southwest AD 2004-18-06 (2008), SkyWest (DOT OIG AV2025038), Eastern
  (GAO/RCED-90-94).** Recurring inspections or parts of an AD's scope were
  dropped from tracking.
  → Known gap: recurring actions.
- **[P] NTSB WPR19FA091; [S] ATSB AO-2022-025.** Life-limit cycles were
  miscounted or never compared to the limit.
  → Gate 8.
- **[P] NTSB A-06-60.** An HPT disk ruptured while still inside its AD window.
  → The standing ban on "safe" and "airworthy".
- **[P] IATA LLP traceability guidance (2020).** Calculation errors and
  doubtful provenance occur, and part cycles diverge from engine cycles after
  parts are swapped.
  → Gate 8 note; known gap: a part moved between engines.
- **[P] AD 2018-09-10 (CFM56).** It says what to do when a blade's cycles
  since new are unknown.
  → Gate 12 note; known gap.
- **No documented failure was found for:**
  - a misread serial-number range;
  - confusion between cycles and hours;
  - a missing link to a superseding AD;
  - a wrong compliance-time anchor.
- **No audit gives a base rate of AD-status record errors.**

## Software, Research, and Precedents

- **[P/S] Vendors (Traxxall, CAMP, Ramco, Veryon, GE Aerospace, Bluetail).**
  - Human analysts decide applicability.
  - Newer AI features produce drafts for an engineer to approve.
  - No vendor publishes accuracy for its applicability decisions.
- **[P] Drop (2026), TU Wien thesis.** LLM extraction of A320 AD applicability
  scored 93.8% under a schema-guided approach, on 15 hand-labeled ADs.
  - Active-vs-superseded status was the weakest automatically scored field.
  - Affected parts was the weakest field overall: 3.75/5 for the model and 23%
    for non-expert humans.
  - The author concludes human verification is required.
  → Gate 9; seed-029.
- **[P] IDx-DR pivotal trial (Abràmoff et al. 2018).**
  - Endpoints were fixed before enrollment, partly from regulatory
    requirements.
  - The "insufficient quality" rate was reported separately.
  → Budgets are declared as policy.
- **[S] Plesner et al., Radiology 2023.** Near-zero misses on abnormal chest
  X-rays came at the cost of clearing only 28% of normal studies
  autonomously.
  → The gate 12 tension is stated.
- **[P] GraphCompliance (arXiv 2510.26309).** A compliance evaluation weighted
  recall over precision (F2).
  → Supports weighting misses over false alarms.
- **[P] Cormack & Grossman, SIGIR 2024.** Recall estimates are meaningful only
  if the labels are independent of the process being evaluated.
  → The statement on what the sample can show; practitioner review.

## Not Adopted

- **Thrust-rating proration of life-limited parts.** No documented turbofan
  failure was found.
- **Same part number with a different cap by engine model (AD 2009-22-06).**
  That AD is not in the frozen generation. It is a candidate when the
  evaluated slice widens.
- **Vendor accuracy claims** such as ">98% field-level". They measure generic
  document extraction, not applicability.
