# Milestone 1: Immutable Official-Source Acquisition

## Outcome

Acquire the HPT hub proposal/final pair reproducibly and prove that rerunning
the acquisition is safe, complete, and explainable.

The milestone is complete when two Federal Register documents—`2025-10764`
and `2025-18469`—have immutable raw artifacts, artifact receipts, a raw
generation manifest, validation results, and a demonstrably idempotent rerun.

## Acquisition Comes Before Parsing

```text
source query and URL resolution
→ HTTP retrieval
→ exact-byte preservation
→ response metadata and SHA-256
→ artifact receipts
→ raw-generation completeness gate
──────────────────────────────────── raw/normalized boundary
→ parsing and normalization
→ evidence regions and predicates
```

Acquisition may perform only the minimum inspection needed to validate a
download—for example, media type, readable PDF, well-formed XML, expected
document identity, and presence of the codified section. It must not convert
the directive into normalized applicability logic.

## In Scope

- Explicit, reproducible Federal Register API requests for the two document
  identities.
- Retrieval of API JSON, full-text XML, full-text HTML, plain text, GovInfo
  official PDF, GovInfo MODS XML, and every referenced original-size image.
- Exact retained bytes, SHA-256, byte count, requested/resolved URL, retrieval
  timestamp, response status, selected HTTP metadata, media type, authority
  role, and redistribution status.
- One artifact receipt per expected representation, including failures.
- One raw-generation manifest covering the expected document/representation
  matrix and proposal/final relationship evidence.
- Validation of identity agreement, hashes, media plausibility, XML
  well-formedness, PDF readability, required representation presence, and
  explicit paragraph-(l) incorporated-material status.
- Idempotent rerun behavior and detection of an unexpected hash change.
- A failed/partial acquisition that remains inactive and visible.
- Automated tests using small local fixtures; live network calls are excluded
  from the default test suite.

## Deferred

- Directive predicate extraction and normalized schemas.
- Chunking, embeddings, vector or graph indexes, reranking, and generation.
- Synthetic fleet ingestion and impact classification.
- Scheduler, hosting, database, and object-storage products.
- Incremental reprocessing beyond safe reruns of the first bounded pair.
- FAA DRS automation until its external API contract is verified.
- Production promotion of a normalized or retrieval generation.

## Work Packages

### A1. Freeze the executable acquisition contract

- Convert the approved raw-manifest fields into a machine-validated schema.
- Define stable source-document, acquisition-run, retrieval, representation,
  artifact, and raw-generation identities.
- Define approved status and failure reason codes.
- Decide the initial local raw-artifact location without claiming it is the
  final production storage architecture.

### A2. Implement official-source retrieval

- Resolve representation URLs from Federal Register API metadata.
- Download each expected representation without transforming its bytes.
- Stream downloads safely, capture response metadata, hash retained bytes,
  and avoid partial-file publication.
- Discover and retrieve original-size document graphics.

### A3. Produce receipts and the generation manifest

- Write one receipt for every success or failure.
- Build the expected-versus-observed representation matrix.
- Record identity snapshots, typed relationship evidence, authority roles,
  unavailable dependencies, and completeness status.

### A4. Validate and test failure behavior

- Verify exact hashes and basic format integrity.
- Test reruns, interrupted downloads, malformed content, missing
  representations, redirects, HTTP failures, and changed bytes.
- Ensure a partial run cannot qualify for downstream normalization.

### A5. Create the first frozen raw generation

- Execute acquisition for the HPT hub pair.
- Review the manifest and validation report.
- Record the raw generation as accepted for normalization or rejected with
  explicit reasons.
- Preserve the receipt; acceptance does not make a retrieval release active.

## Exit Criteria

- Every expected artifact is present or has an approved explicit failure.
- Every retained artifact independently verifies against its recorded SHA-256.
- Source identifiers agree with the requested documents.
- XML is well formed, PDFs are readable, and referenced graphics are retained.
- A second unchanged run creates no duplicate logical source version.
- A simulated changed representation is preserved and surfaced for review.
- A simulated partial run fails the completeness gate.
- The raw generation can be reproduced from documented commands.
- The next normalization milestone can consume artifacts without network
  access.

## First Implementation Decision

The next discussion should choose the smallest stack capable of this milestone
only. It should not select retrieval, agent, UI, hosting, or long-term storage
technology on their behalf.
