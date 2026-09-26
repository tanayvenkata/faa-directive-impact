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

Numbering matches the GitHub issues. Build a thin end-to-end slice first, then
widen it: one representation of one document goes all the way to a validated
receipt before the full representation matrix is attempted. Tests for each
behavior land with the issue that introduces it.

- **A1. Tooling foundation** (done) — Python, uv, Ruff, pytest, Makefile.
- **A2. Acquisition contract** (done) — receipt and raw-generation JSON
  Schemas, identity semantics, and reason codes (`SCHEMA_DECISIONS.md`).
- **A3. Thin slice** — fetch API JSON for `2025-10764`, stream to a temporary
  file, publish it atomically to local raw storage, hash it, and write a
  schema-valid receipt, including failure receipts.
- **A4. Widen representations and idempotency** — resolve and retrieve XML,
  HTML, text, GovInfo PDF, MODS, and original-size images; unchanged reruns
  deduplicate; changed bytes are preserved and flagged.
- **A5. Pair and manifest** — add `2025-18469`, the expected-versus-observed
  matrix, proposal/final relationship evidence, dependencies, and completeness.
- **A6. Validation gate** — identity agreement, media plausibility, XML/PDF
  integrity, paragraph-(l) status, upstream-change signals, and whether
  Federal Register HTML element IDs are stable across a regenerated
  representation.
- **A7. Offline lifecycle suite** — one end-to-end offline suite exercising
  the full rerun, change, and partial-failure lifecycle across both documents.
- **A8. First frozen raw generation** — execute live, review the manifest, and
  record accept-for-normalization or reject with reasons.
- **A9. Public "Reproducible" checkpoint** — short write-up and repository
  state that meet the series' Reproducible claim level.

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

## After This Milestone

Publishing at the Reproducible level is a checkpoint, not a finish line. The
next milestone writes the feasibility seed cases, freezes numerical gates, and
decides image-figure transcription before normalization. Retrieval, agent, UI,
hosting, and long-term storage choices remain deferred.
