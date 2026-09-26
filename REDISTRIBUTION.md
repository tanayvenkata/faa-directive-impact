# Raw Artifact Retention and Redistribution

Decided 2026-09-26 for the Reproducible checkpoint.

## Decision

| Representation | Status | Basis |
|---|---|---|
| Federal Register API JSON, XML, HTML, plain text | `permitted` | U.S. Government work |
| GovInfo official PDF and MODS | `permitted` | U.S. Government work |
| Document graphics (original-size images) | `review_required` | May reproduce third-party material |
| Incorporated manufacturer material | not acquired | Proprietary; recorded only as an unavailable dependency |

Text published by the FAA in the Federal Register is a work of the U.S.
Government, which has no copyright protection under 17 U.S.C. §105. GovInfo's
[policy](https://www.govinfo.gov/about/policies) states that government
publications "can generally be reprinted without legal restriction", with
customary credit to the preparing agency. It also warns that a government
publication "may contain copyrighted material which was used with permission"
and that such inclusion authorizes no further use. A directive's figures can
reproduce manufacturer drawings, so graphics are reviewed per document before
redistribution.

Redistributed artifacts credit the Federal Aviation Administration, U.S.
Department of Transportation, as the issuing agency. They are published through
the Office of the Federal Register and GovInfo.

## Where Artifacts Live

- **Git:** receipts, manifests, validation reports, and decisions. These are
  small, reviewable evidence records.
- **GitHub release assets:** each accepted frozen generation's raw bytes, as a
  deterministic `tar.gz` with a `SHA256SUMS` file matching the receipts. This
  keeps binary PDFs out of Git history while preserving exact bytes if the
  upstream representation later changes.
- **Local `data/`:** working acquisitions; ignored by Git.

## Receipts Recorded Before This Decision

Receipts are immutable. Receipts written before this decision, including the
accepted generation `gen-20260926T213233Z-000f808f`, record
`review_required`. This document supersedes that status for the text
representations they describe. Receipts written afterwards record the decided
status directly.
