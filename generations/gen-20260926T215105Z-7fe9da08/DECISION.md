# Raw Generation Decision: gen-20260926T215105Z-7fe9da08

**Decision: ACCEPTED for normalization and as the source snapshot for the
evaluation seed** — 2026-09-26.

Acceptance makes this generation the source for evaluation-seed cases. It does
not promote a retrieval index or release, and makes no evaluation or impact
claim.

## Identity

| Field | Value |
|---|---|
| Generation | `gen-20260926T215105Z-7fe9da08` |
| Corpus track | `frozen_evaluation` |
| Acquisition run | `run-20260926T215105Z-7fe9da08` |
| Manifest schema | `1.1.0` |
| Manifest SHA-256 | `118e21f6eda7b1a6b8110c8d88c4bde660d9714887bde23b6c200c4d489c50f3` |
| Validation report SHA-256 | `7cfe7075fe86d87244348e5f7c31351b0f554d35736f824c589dd1e1baa48999` |
| Creating process | `faa-directive-impact 0.1.0` at commit `d0b44c6` |
| Storage root | clean `data/seed-frozen/`, not committed |

## Scope

Ten Federal Register documents, all IAE V2500-family airworthiness directives:

| Thread | Documents | Role in the seed |
|---|---|---|
| HPT hub quality escape | `2025-10764` → `2025-18469` (AD 2025-19-13) | Part/serial match, cycle limits, shop-visit timing |
| HPC 3rd-stage blades | `2025-20088` → `2026-16954` (AD 2026-17-03), corrected by `2026-18423` | Exposure trigger, proposal-to-final change, correction |
| Airworthiness limitations | `2024-26092` → `2025-17066` (AD 2025-17-16) | Operator and maintenance-program state |
| HPT disk inspection | `2021-11960` (AD 2021-11-15), superseded by `2022-02574` (AD 2022-02-09) | Superseded authority, incorporated material |
| HPT disk inspection | `2021-14268` (AD 2021-11-51) | Incorporated material, image-only applicability tables |

This is 64 artifacts, including four original-size graphics.

## Review

| Criterion | Result |
|---|---|
| Hashes and receipts verify | 64 of 64 re-hashed with `shasum -a 256 -c`, independently of project code |
| Completeness | `complete`; no missing artifacts |
| Validation | `passed`; every check |
| Relationships | 3 `proposal_final`, `2026-18423 corrects 2026-16954`, `2022-02574 supersedes 2021-11960`; all `identifier_join` |
| Incorporated material | `not_required` for the seven recent records; named `unavailable` IAE service bulletins for `2021-11960`, `2022-02574`, and `2021-14268` |
| Idempotency | Rerun `gen-20260926T215115Z-3be03dcf` classified all 64 representations `unchanged` |
| Graphics | Reviewed and `permitted`; see `REDISTRIBUTION.md` |

## Rejected Candidate

`gen-20260926T215017Z-4171a454`, from the same ten documents at an earlier
commit, was **rejected** during review:

- it recorded `[Reserved]` placeholder items as unavailable incorporated
  material; and
- it recorded AD 2026-17-03's DRS dependency twice, once for the final rule and
  once for its correction.

Both defects were fixed in `d0b44c6` before this generation was acquired. The
rejected candidate remains in local storage and was never used.

## Known Limits

- **Volatile API fields untested over time.** The rerun came seconds later, so
  volatile API fields are still untested over days.
- **Supersession needs both ADs.** It is recorded only because both ADs are in
  the generation.
- **No DRS corroboration.** All DRS dependencies remain
  `deferred_access_verification`.
- **Image-only applicability.** `2021-14268`'s applicability tables exist only
  as images; transcription is decided in E3 (#14).
