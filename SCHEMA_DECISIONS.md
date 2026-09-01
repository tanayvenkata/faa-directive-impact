# Acquisition Schema Decisions

## Why JSON Schema

Receipts and manifests are durable evidence records, not Python-only objects.
JSON Schema Draft 2020-12 is the canonical contract so other languages,
validation tools, and future services can verify the same files. Python uses
the `jsonschema` library to enforce that contract.

## Two Record Levels

### Artifact receipt

One receipt represents one attempted retrieval of one representation. Success
and failure are both retained:

- success requires artifact path, byte length, media types, and SHA-256;
- failure requires a bounded reason code and safe diagnostic detail;
- failure cannot include an artifact as though acquisition succeeded; and
- an original graphic must identify its parent document and source graphic ID.

### Raw-generation manifest

One manifest describes the expected and observed acquisition set. It records:

- corpus track and acquisition runs;
- expected representations;
- receipt locations;
- typed document relationships;
- external dependencies and availability;
- missing artifacts; and
- completeness and normalization eligibility.

An incomplete manifest can never be eligible for normalization.

## Semantic Validation Boundary

The schemas enforce universal acquisition meaning, not only JSON types. For
example, Federal Register XML is a structured parsing input, GovInfo PDF is an
official edition, and DRS metadata is identity/status corroboration. Invalid
source, representation, and authority-role combinations are rejected.

Directive-domain semantics remain deferred to normalization. The acquisition
schemas do not assert what an engine model, part number, shop visit, or
maintenance obligation means.

## Identity Semantics

IDs have different meanings and must not be collapsed:

- source document identity belongs to the source authority;
- acquisition run identity groups one execution;
- retrieval identity distinguishes an individual attempt;
- receipt identity identifies the durable evidence record; and
- generation identity identifies an expected/observed raw corpus set.

The schema keeps these IDs opaque and constrained rather than embedding
mutable business meaning in them. Their concrete generation algorithm belongs
to the acquisition implementation.

## Hash Semantics

The receipt records lowercase hexadecimal SHA-256 of the exact retained bytes.
It is not a hash of parsed text, normalized JSON, or a decoded representation.
HTTP ETag and Last-Modified values are retained when present but never replace
the content hash.

## Paths and Secrets

Artifact and receipt paths are relative and may not traverse above their
storage root. Receipts intentionally have no fields for credentials,
authorization headers, or cookies.

## Versioning

Both initial schemas use `1.0.0`. Additive or corrective schema evolution must
be explicit; existing receipts remain validated against the version they
declare. A schema migration must create a new derived record rather than
rewrite historical evidence silently.
