# Source Review: Remaining Protected Threads and Challenge Records

## Review Status

This review completes source reconnaissance for the six-document protected
core and spot-checks the two evidence-sufficiency challenge records. As with
the first review, temporary files are not immutable corpus acquisitions.

- Reviewed: 2026-09-01
- Compressor-blade thread: `2025-20088` → `2026-16954` / AD `2026-17-03`
- Airworthiness-limitations thread: `2024-26092` → `2025-17066` / AD `2025-17-16`
- Challenge records: `2022-02574` and `2021-14268`

## Representation Result

The source-role mixture selected after the HPT hub review holds for both
remaining protected threads:

- API JSON supplies discovery, identity, relationship metadata, canonical
  representation URLs, and referenced-image metadata;
- Federal Register XML preserves headings, paragraphs, page markers, and
  structured tables;
- Federal Register HTML adds evidence-addressing IDs and direct links to
  original-size graphics;
- GovInfo PDF remains the official-edition and visual verification source; and
- plain text remains useful for lexical search and diffs, but not authority or
  complete structure.

The challenge records add one qualification: XML can contain only a graphic
identifier where a compliance figure is image-only. Original-size Federal
Register images must therefore be captured as first-class raw artifacts.

## Thread 1: Compressor Rotor Blades

### Identity

| Field | Proposal | Final |
|---|---|---|
| Federal Register document | `2025-20088` | `2026-16954` |
| Docket | `FAA-2025-2555` | `FAA-2025-2555` |
| Project identifier | `AD-2025-00433-E` | `AD-2025-00433-E` |
| RIN | `2120-AA64` | `2120-AA64` |
| Publication date | 2025-11-18 | 2026-08-20 |
| Effective date | Not applicable | 2026-09-24 |
| AD / amendment | Not assigned | `AD 2026-17-03` / `39-23446` |

### Deterministic Predicates

The applicability predicate combines the ten supported V2500 variants with an
installed 3rd-stage HPC rotor blade having P/N `6A8353` or `6A8688`.

The final action is:

```text
at the next engine shop visit after the effective date
where the 3rd-stage HPC rotor is exposed
→ replace the full set of 3rd-stage HPC rotor blades
  with parts eligible for installation
```

An exposure occurs when any 3rd-stage HPC rotor blade is removed from the HPC
stage 3-to-8 drum. Eligible parts are either named later-standard P/Ns or the
two named modified P/Ns.

### Proposal-to-Final Change

The proposal triggered at the next blade exposure after the effective date.
The final rule changed the trigger to the next engine shop visit after the
effective date where the rotor is exposed and added an engine-shop-visit
definition. The FAA explained that it did not intend an engine inducted before
the effective date to become subject merely because exposure occurred later.

This is a meaningful temporal and event-semantics change, not editorial noise.
The normalized model must preserve both proposal and final predicates rather
than overwriting one with the other.

The final rule names manufacturer service information in its discussion but
does not incorporate it by reference because the directive itself supplies the
necessary compliance procedure. Paragraph (k) explicitly states that there is
no incorporated material.

### Modeling Consequences

- Blade exposure and engine shop visit are separate event facts.
- Shop-visit induction time relative to the effective date matters.
- A full-set replacement cannot be inferred from one component-row update
  unless the asset snapshot represents the installed set.
- Later-approved part numbers require controlled authority; the model must not
  invent or semantically extrapolate them.

## Thread 3: Airworthiness-Limitations Revision

### Identity

| Field | Proposal | Final |
|---|---|---|
| Federal Register document | `2024-26092` | `2025-17066` |
| Docket | `FAA-2024-2423` | `FAA-2024-2423` |
| Project identifier | `AD-2024-00320-E` | `AD-2024-00320-E` |
| RIN | `2120-AA64` | `2120-AA64` |
| Publication date | 2024-11-12 | 2025-09-05 |
| Effective date | Not applicable | 2025-10-10 |
| AD / amendment | Not assigned | `AD 2025-17-16` / `39-23126` |

### Deterministic Predicates

Within 90 days after the effective date, the final directive requires revision
of paragraph B.1 of the Maintenance Scheduling section in the ALS of the ICA
located in the applicable existing Time Limits Manual. It names distinct TLM
part/task references for A5, D5, and E5 families.

For air-carrier operations, it separately requires revision of the existing
approved maintenance or inspection program within the same 90-day period. The
added inspections cover HPT stage 1 hub P/N `2A5001` and HPT stage 2 hub P/N
`2A4802` with named task references.

### Proposal-to-Final Changes

The final rule makes several substantive corrections and clarifications:

- corrects the HPT stage 2 reference from nonexistent Task
  `72-45-11-200-009` to `72-45-31-200-009`;
- replaces the proposal's generic EMM/ICA wording with family-specific TLM
  references;
- separates the universally applicable ICA/TLM revision from the additional
  air-carrier maintenance-program revision; and
- clarifies that the named inspection tasks are scheduled at piece-part
  exposure rather than directly performed within 90 days by this AD.

These changes prove that proposal-to-final comparison must operate at predicate
and reference level. A textual similarity score alone would miss a safety-
relevant task-number correction.

### Modeling Consequences

- The asset/operator scenario needs an explicit air-carrier-operation state.
- Manual/program revisions are versioned organizational state, not installed
  component state.
- A completed program revision and a completed inspection are different facts.
- Family-specific TLM identity and revision provenance must be preserved.
- Missing operator/program state must result in `needs_review`.

## Evidence-Sufficiency Challenge Records

### Federal Register document 2022-02574

AD `2022-02-09` supersedes AD `2021-11-15`. Its applicability depends on serial
lists in two named IAE non-modification service bulletins. Its required actions
also depend on manufacturer accomplishment instructions and pass/fail criteria.
Two compliance schedules appear as image-only Federal Register figures.

The directive establishes the model, component P/Ns, dependency identities,
general action, and some timing logic. Without authorized bulletin access and
verified figure transcription, the system cannot independently establish the
complete affected population or executable inspection procedure.

### Federal Register document 2021-14268

AD `2021-11-51` includes explicit affected P/N/S/N lists in paragraph (c), so
public text can establish candidate applicability. The inspection method and
pass/fail criteria still depend on incorporated IAE service bulletins. Its two
required-action tables are image-only graphics, although the paragraph text
provides the urgent ten-flight-cycle timing.

The correct outcome is therefore finer-grained than a global “document
unavailable” label:

- public directive evidence may be sufficient for candidate applicability;
- public evidence is insufficient for the complete inspection/action packet;
  and
- the missing dependency and exact version must be reported.

## Cross-Thread Findings

The six protected records now demonstrate:

- structured tables and image-only figures;
- proposal/final relationship and authority-state changes;
- substantive predicate and task-reference corrections;
- component P/N/S/N matching and component-cycle state;
- event qualification and effective-date ordering;
- family-specific document/program obligations;
- operator-state branching;
- incorporated-material dependencies; and
- safe partial-evidence behavior.

The selected corpus is sufficiently varied for a first acquisition,
normalization, retrieval, and deterministic-label feasibility slice. It is not
sufficient for a general FAA compliance system, and no such claim should be
made.

