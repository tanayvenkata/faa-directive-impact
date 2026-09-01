# Initial Raw Manifest Contract

## Status and Purpose

This contract defines the first immutable acquisition receipt for the protected
FAA feasibility corpus. It records what must be captured; it does not select a
language, storage product, scheduler, or database.

The first real acquisition should cover the HPT hub proposed/final pair and
should not be promoted as a corpus generation until every required capture is
present or has an explicit failure record.

## Proposed Capture Layout

The logical layout below separates immutable bytes from acquisition receipts.
The eventual physical storage may differ if it preserves the same contract.

```text
raw/
  federal-register/
    2025-10764/
      <retrieval-id>/
        api.json
        full-text.xml
        full-text.html
        full-text.txt
        govinfo-official.pdf
        govinfo-mods.xml
        acquisition.json
    2025-18469/
      <retrieval-id>/
        ...
  faa-drs/
    <drs-document-identity>/
      <retrieval-id>/
        metadata.<source-format>
        acquisition.json
manifests/
  raw-generation-<generation-id>.json
```

`retrieval-id` must be unique for an acquisition attempt and sortable by UTC
time. It is not the source document identity or content version.

## Artifact Receipt

Each requested representation receives one receipt, including failures. A
receipt must record:

- `receipt_schema_version`
- `acquisition_run_id`
- `retrieval_id`
- `retrieved_at_utc`
- `source_system`
- `source_document_identity`
- `representation_role`
- `requested_url`
- `resolved_url`
- `request_method`
- `response_status`
- selected response metadata, including media type, content length, ETag,
  Last-Modified, and Content-Disposition when present
- `acquisition_status`
- `failure_reason_code` and safe diagnostic detail when unsuccessful
- artifact relative path when successful
- byte length
- SHA-256 of the exact retained bytes
- detected media type and declared media type
- authority role
- redistribution status and basis
- source terms or access note when relevant

Do not store credentials, authorization headers, session cookies, or other
secrets in a receipt.

## Identity Snapshot

The run manifest should snapshot identifiers observed in source metadata
without treating all of them as the same identity:

- Federal Register document number
- Federal Register citation, volume, and page range
- document type and authority state
- publication, comment-close, signing, and effective dates when present
- AD number and amendment number when assigned
- FAA docket and project identifiers
- RIN
- Regulations.gov docket and document identifiers
- DRS document identity and status when available
- correction-of, corrected-by, supersedes, superseded-by, proposal/final, and
  other typed relationships

Relationships must record their evidence source and confidence class. A shared
title alone is not sufficient to establish a relationship.

## Representation Roles

Use explicit roles rather than a single `canonical` flag:

| Representation | Initial role |
|---|---|
| Federal Register API JSON | Discovery and identity metadata |
| Federal Register XML | Preferred structured parsing input |
| Federal Register HTML | Evidence addressing and web presentation |
| Federal Register plain text | Lexical/debug projection |
| GovInfo official PDF | Official-edition authority and visual verification |
| GovInfo MODS XML | Official-edition bibliographic metadata |
| FAA DRS metadata/record | FAA identity, status, and relationship corroboration |

A parser may choose one preferred input, but the manifest must preserve all
successfully acquired representations independently.

## Generation Manifest

The raw-generation manifest must record:

- manifest schema version and generation ID;
- creation timestamp and creating process/version when implementation exists;
- acquisition run IDs included;
- frozen-evaluation or refreshable-discovery track;
- expected document identities and representations;
- artifact receipts and hashes;
- typed relationships;
- missing, failed, quarantined, or intentionally unavailable artifacts;
- incorporated-material dependencies and exact named versions;
- redistribution decisions;
- completeness result; and
- whether the generation is eligible to enter normalization.

The manifest does not promote itself. Later candidate validation and a separate
promotion receipt decide which normalized/index generation becomes active.

## Idempotency and Change Rules

- The tuple of source system, source document identity, representation role,
  resolved URL, and exact content hash identifies an already-seen capture.
- Repeating an acquisition may create a new attempt receipt, but must not create
  duplicate authoritative artifact bytes in the logical corpus.
- A new hash for an existing identity and representation is preserved as a new
  observed version and flagged for comparison; it is never overwritten.
- HTTP cache validators help explain observations but do not replace hashing.
- A failed representation must remain visible in the run manifest.
- A partial run cannot silently qualify as a complete raw generation.

## Initial Completeness Gate

For each of the two HPT hub Federal Register documents, require:

1. API JSON;
2. full-text XML;
3. full-text HTML;
4. plain text;
5. GovInfo official PDF; and
6. GovInfo MODS XML.

DRS is required as either a successful capture or an explicit
`deferred_access_verification` record until its external API contract is
confirmed. There is no incorporated material for this thread, and that
negative fact must be recorded from paragraph (l), not inferred from a missing
download.

The generation may enter normalization only when hashes verify, required media
types are plausible, Federal Register identifiers agree across the pair, PDFs
are readable, XML and HTML contain the codified section and affected-hub table,
and every missing artifact has an approved reason code.

## Decisions Still Deferred

- whether raw bytes are committed to Git or retained in external object storage;
- exact serialization schema and validation technology;
- storage deduplication mechanism;
- DRS authentication and key handling;
- retention period for repeated unchanged observations; and
- scheduler, queue, database, index, hosting, and orchestration products.

