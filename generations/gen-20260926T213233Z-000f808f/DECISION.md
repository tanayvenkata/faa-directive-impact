# Raw Generation Decision: gen-20260926T213233Z-000f808f

**Decision: ACCEPTED for normalization** — 2026-09-26.

This accepts the raw generation as the input to the normalization milestone.
It does not promote any retrieval index or release, and makes no evaluation or
impact claim.

## Identity

| Field | Value |
|---|---|
| Generation | `gen-20260926T213233Z-000f808f` |
| Corpus track | `frozen_evaluation` |
| Acquisition run | `run-20260926T213233Z-000f808f` |
| Manifest schema | `1.1.0` |
| Manifest SHA-256 | `9802a87039807d7d6eb02dffc74a8ecdb25a7627d3870e95eb4588431bc1b24a` |
| Validation report SHA-256 | `5ce45475ba2ea35bc35df0b7c3d88f4511921f504720b37d0e4401540ed9fcf6` |
| Creating process | `faa-directive-impact 0.1.0` at commit `3ef4bf6`, which produced these bytes. The release tag points at the later `a325939`, which changed only docs and the redistribution status of future receipts |
| Storage root | clean `data/frozen-evaluation/`, not committed |

## Scope

The HPT hub quality-escape thread for IAE V2500 engines:

- `2025-10764`: proposed rule, published 2025-06-13;
- `2025-18469`: final rule (AD 2025-19-13), published 2025-09-24, effective
  2025-10-29.

Each document has six expected representations: API JSON, full-text XML,
full-text HTML, and plain text from the Federal Register, plus the official
PDF and MODS from GovInfo. Neither document references any images.

## Review

| Criterion | Result |
|---|---|
| Hashes and receipts verify | 12 of 12 artifacts re-hashed with `shasum -a 256 -c`, independently of project code; all read-only |
| Expected identities agree | API JSON, XML `FRDOC`, HTML, text, PDF `FR Doc.` line, and MODS all name their document; GovInfo granules match the served URLs |
| Proposal/final relationship | `2025-10764 → 2025-18469`, `identifier_join` on docket `FAA-2025-0926`, backed by both API JSON receipts |
| Completeness | `complete`; 12 of 12 expected artifacts present; no missing artifacts |
| Validation | `passed`; 54 of 54 checks |
| Idempotency | Rerun `gen-20260926T213235Z-c078a2bf` classified all 12 representations `unchanged`; all 12 were byte-identical to this generation |
| Raw artifacts outside Git | Yes; only receipts, manifests, and validation reports are committed here |

## Recorded Dependencies

- **Incorporated material, both documents:** paragraph (l) states `None.`,
  recorded as `not_required`.
- **FAA DRS record for AD 2025-19-13:** `deferred_access_verification`. DRS
  corroboration of identity and status is not part of this generation; see
  issue #10.

## Known Limits

- **Volatile API fields untested over time.** The rerun came seconds later, so
  it does not test the `page_views` exclusion or the nested `dockets` counters
  over days. A later rerun must inspect any `changed` API JSON diff before
  adding a volatile field.
- **Redistribution undecided.** Every receipt records `review_required`. The
  decision belongs to the Reproducible checkpoint (A9).
- **Relationship by identifier join.** The proposal/final link is a docket
  join; the API does not assert it directly.
- **No DRS corroboration.** FAA identity and status have not been corroborated
  against DRS.

## Evidence in This Directory

```text
manifests/raw-generation-gen-20260926T213233Z-000f808f.json
validation/gen-20260926T213233Z-000f808f.json
receipts/run-20260926T213233Z-000f808f/*.json      12 receipts
rerun/                                              idempotency rerun records
```

Receipt paths in the manifest resolve relative to this directory. To reproduce
the generation, re-acquire into a clean storage root and compare the SHA-256
values in these receipts:

```bash
make acquire DOCS="2025-10764 2025-18469" STORAGE_ROOT=data/reproduce
```
