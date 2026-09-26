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

Transport content-coding is not part of the representation. Acquisition
requests `Accept-Encoding: identity`; if a server still applies gzip or a
similar transport coding, the retained bytes and hash are the entity body after
that coding is removed. This keeps a hash stable when a server toggles
compression, so a hash change signals a content change.
HTTP ETag and Last-Modified values are retained when present but never replace
the content hash.

## Logical Source Versions

A logical source version is one distinct content hash for one source identity
and representation role (plus graphic identifier for figures). A derived
version index is rebuilt from successful receipts on every run and is never a
source of truth. Each new success is classified as `new`, `unchanged`, or
`changed`; a `changed` result is preserved and surfaced for review, never
replaced.

Federal Register API JSON includes a `page_views` counter that changes without
any change to the document. For API JSON only, the version hash is computed
over a canonical form with `page_views` removed. The receipt still records the
SHA-256 of the exact retained bytes. Any other volatile field must be added
explicitly to `VOLATILE_API_JSON_FIELDS`, never ignored implicitly.

Each run retains its own copy of every artifact. Physical deduplication by hash
is deferred until corpus size shows a need.

## Validation Gate

Every retained artifact is validated immediately after retrieval, and each
check is recorded in a `validation-report` record (schema `1.0.0`) with a
bounded reason code on failure. The checks cover integrity (re-hashing the
retained bytes), media type from leading bytes, JSON/XML/PDF readability, text
decoding, document identity, GovInfo granule agreement with the served URL,
original-image size and MD5 against the API's `images_metadata`, and the
directive's stated incorporated-material paragraph.

XML is parsed with `defusedxml`, so entity-expansion and external-entity
payloads fail as malformed. Required API JSON fields are checked by presence
only, so additive upstream fields never fail acquisition.

A generation is eligible for normalization only when it is complete and every
finding passed. Receipts named in a failed finding never become logical source
versions.

Document identity in the official PDF requires the full `FR Doc. <number>`
line after normalizing typographic dashes. The GovInfo edition typesets
`2025–10764` with an en dash, and its pages can carry a neighbouring document's
`FR Doc.` line.

The incorporated-material paragraph is found by heading text, not letter: the
HPT pair uses `(l)` and `2021-14268` uses `(k)`. A stated `None.` becomes an
explicit `not_required` dependency; listed items become named `unavailable`
dependencies; an absent heading fails validation.

## Document Relationships

Relationships read `from → to`:

| Type | From | To | Evidence |
|---|---|---|---|
| `proposal_final` | proposed rule | original final rule | shared FAA docket; both API JSON receipts |
| `corrects` | correction | the final rule it corrects | shared AD number; both API JSON receipts |
| `supersedes` | replacing AD | replaced AD | "Affected ADs: This AD replaces AD …"; XML and API JSON receipts |

The Federal Register API types a correction as `Rule` and may leave
`correction_of` empty. For example, `2026-18423` corrects AD 2026-17-03 but
does not link to `2026-16954`. A correction is therefore recognized by its
action (`Final rule; correction.`) or title and is never treated as a second
final rule. Links are `identifier_join` unless the API asserts them directly.
Supersession is recorded only when both ADs are in the generation.

## Interrupted Runs

An artifact is published before its receipt is written. If the receipt write
fails, the run aborts with an error and writes no manifest. The artifact is
left orphaned: no receipt, manifest, or validation report refers to it, so it
never becomes a logical version or part of a generation. The next run
re-acquires it normally. Orphans are harmless but occupy space; a storage audit
that lists files without receipts is deferred until the corpus grows.

Each run rebuilds the version index by reading every receipt and validation
report. This full scan is deliberate at the current corpus size.

## Paths and Secrets

Artifact and receipt paths are relative and may not traverse above their
storage root. Receipts intentionally have no fields for credentials,
authorization headers, or cookies.

## Versioning

Both initial schemas use `1.0.0`. Additive or corrective schema evolution must
be explicit; existing receipts remain validated against the version they
declare. A schema migration must create a new derived record rather than
rewrite historical evidence silently.


The raw-generation manifest moved to `1.1.0` to add an optional
`source_graphic_identifier` on missing artifacts, so a missing figure is
identifiable even when no receipt exists. `1.0.0` manifests existed only as
local development output before the first frozen generation, so no `1.0.0`
manifest validator is retained.