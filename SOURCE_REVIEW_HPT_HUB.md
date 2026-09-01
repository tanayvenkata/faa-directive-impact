# Source Review: HPT Hub Quality Escape

## Review Status

This is a source-structure and feasibility review of the first protected
proposed-to-final thread. It is not an immutable corpus acquisition. The files
used during reconnaissance were temporary and are not release artifacts.

- Reviewed: 2026-09-01
- Proposed rule: Federal Register document `2025-10764`
- Final rule: Federal Register document `2025-18469`, AD `2025-19-13`
- Scope: live Federal Register API JSON, XML, HTML, plain text, GovInfo PDF,
  and the public FAA DRS access surface

## Identity and Relationship

| Field | Proposed rule | Final rule |
|---|---|---|
| Federal Register document | `2025-10764` | `2025-18469` |
| Authority state | NPRM | Final rule / AD |
| Docket | `FAA-2025-0926` | `FAA-2025-0926` |
| Project identifier | `AD-2025-00200-E` | `AD-2025-00200-E` |
| RIN | `2120-AA64` | `2120-AA64` |
| Regulations.gov document | `FAA-2025-0926-0001` | `FAA-2025-0926-0004` |
| AD / amendment | Not assigned | `AD 2025-19-13` / `39-23153` |
| Publication date | 2025-06-13 | 2025-09-24 |
| Effective date | Not applicable | 2025-10-29 |
| Federal Register citation | 90 FR 25002–25004 | 90 FR 45907–45909 |

The stable docket, project identifier, and RIN establish the thread. The final
record adds the AD and amendment identifiers. Proposal/final identity must not
be inferred from title similarity alone.

## Representation Findings

### API JSON

Useful for discovery and identity. It exposes publication/effective dates,
document type, citation and page range, docket identifiers, CFR references,
Regulations.gov metadata, and canonical URLs for XML, HTML, text, PDF, MODS,
and JSON representations.

It does not contain the complete directive body or predicate tables, so it is
not sufficient as the parsing source.

### Federal Register XML

Preferred first parsing representation. The reviewed records preserve:

- semantic preamble and regulatory-text sections;
- heading levels;
- paragraph boundaries;
- printed-page markers;
- structured tables with row and cell elements; and
- proposal/final root distinctions.

The affected-hub table is represented as rows with four cells: component,
part number, serial number, and cycles-since-new removal limit.

### Federal Register HTML

Preferred evidence-addressing projection. It preserves the same table as HTML
rows and cells and adds generated heading/paragraph IDs and `data-page`
attributes. For example, the final required-action paragraph and its table are
on printed page 45909.

Generated HTML IDs are representation-local locators, not permanent legal
identifiers. A citation should therefore carry the source document/version,
representation hash, printed page, regulatory paragraph, and local element ID
when available.

### Plain text

Useful for lexical search, diffs, debugging, and human inspection. It retains
readable tables but introduces line wrapping and does not provide stable
element addressing. It is a derived retrieval aid, not the parsing or
authority source.

### GovInfo PDF

The official-edition PDF preserves the visual publication and table layout.
Use it to verify authority, pagination, and parser output. Do not make PDF text
extraction the primary parser while the structured XML is adequate.

### FAA DRS

The public DRS application is reachable and offers guest search. Its current
application also exposes an API-key workflow for document metadata, with keys
described as expiring after one year. A stable public, unauthenticated record
endpoint was not established during this review.

Before automated DRS acquisition, verify the official API contract, key terms,
identity fields, rate limits, and whether public records can be retrieved
without session-bound UI calls. Until then, DRS review is manual and its
automation status is `deferred_access_verification`.

## Deterministic Directive Predicates

The final directive applies to the ten named V2500 variants already listed in
the project boundary. For an engine with an installed hub whose component,
part number, and serial number match one of eight table rows, paragraph (g)
requires removal and replacement:

```text
at the next qualifying engine shop visit after the effective date
before exceeding the row's cycles-since-new removal limit
OR within 100 flight cycles after the effective date,
whichever occurs later
```

The eight affected rows use:

- HPT 1st-stage hub P/N `2A5001` with four named serial numbers; and
- HPT 2nd-stage hub P/N `2A4802` with four named serial numbers.

Paragraph (h) independently prohibits installation of any listed P/N and S/N
combination after the effective date. Paragraph (i) defines both an eligible
replacement part and a qualifying engine shop visit.

## Modeling Consequences

- Engine model alone is insufficient; the installed component, P/N, and S/N
  must be known.
- `cycles_since_new` is component state, not merely engine state.
- A shop visit cannot be represented only as an arbitrary timestamp. The event
  must either be pre-qualified or retain facts about major mating-flange
  separation and the directive's two exclusions.
- Removing all currently affected hubs does not end the directive's relevance,
  because the installation prohibition continues.
- Unknown component identity, cycle state, or event qualification must produce
  `needs_review`, not `not affected`.

## Proposed-to-Final Result

Two commenters participated. One supported the proposal without change. The
other requested narrower engine applicability, an explicit terminating action,
and later supersession or rescission. The FAA rejected those requests because
narrowing applicability or ending the AD would weaken the continuing
installation prohibition.

The final rule states that it adopted the proposal except for minor editorial
changes. The reviewed codified applicability, eight affected-hub rows, removal
timing, shop-visit definition, and installation prohibition are substantively
unchanged.

## Open Questions

1. Does XML-first parsing remain adequate for the compressor-blade and
   airworthiness-limitations threads?
2. Are Federal Register HTML IDs stable across an unexpected regenerated
   representation with the same document identity?
3. What exact FAA DRS API identity and version fields are available to an
   external API-key holder?
4. Should shop-visit qualification be an input assertion with provenance, a
   deterministic event classifier, or both?
5. Which practitioner interpretations must be preserved around the timing
   phrase containing the shop-visit, cycle-limit, and 100-flight-cycle clauses?

## Official URLs

- Proposed API JSON: https://www.federalregister.gov/api/v1/documents/2025-10764.json
- Proposed XML: https://www.federalregister.gov/documents/full_text/xml/2025/06/13/2025-10764.xml
- Proposed HTML: https://www.federalregister.gov/documents/full_text/html/2025/06/13/2025-10764.html
- Proposed official PDF: https://www.govinfo.gov/content/pkg/FR-2025-06-13/pdf/2025-10764.pdf
- Final API JSON: https://www.federalregister.gov/api/v1/documents/2025-18469.json
- Final XML: https://www.federalregister.gov/documents/full_text/xml/2025/09/24/2025-18469.xml
- Final HTML: https://www.federalregister.gov/documents/full_text/html/2025/09/24/2025-18469.html
- Final official PDF: https://www.govinfo.gov/content/pkg/FR-2025-09-24/pdf/2025-18469.pdf
- FAA DRS: https://drs.faa.gov/

