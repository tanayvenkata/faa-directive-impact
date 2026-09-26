# Checkpoint: Reproducible

**Status:** Reproducible, the second rung of the series claim ladder — 2026-09-26.

**Claim:** built a reproducible source-to-evidence acquisition path for one FAA
airworthiness-directive thread. Nothing more: no evaluation, retrieval,
applicability, or fleet-impact claim is made at this rung.

## What Was Acquired

The HPT hub quality-escape thread for IAE V2500 engines:

| Document | Role | Published |
|---|---|---|
| `2025-10764` | Proposed rule | 2025-06-13 |
| `2025-18469` | Final rule, AD 2025-19-13 | 2025-09-24; effective 2025-10-29 |

For each document, acquisition resolves six official representations from the
Federal Register API record and retrieves them without transforming their
bytes: API JSON, full-text XML, HTML, plain text, the GovInfo official PDF, and
GovInfo MODS. Every attempt, successful or not, produces a schema-validated
receipt with the SHA-256 of the exact retained bytes. Each run produces a
raw-generation manifest (expected versus observed matrix, relationships,
dependencies, completeness) and a validation report. A generation is eligible
for normalization only when it is complete and every check passes.

The accepted generation is
[`gen-20260926T213233Z-000f808f`](generations/gen-20260926T213233Z-000f808f/DECISION.md):

- 12 of 12 artifacts, independently re-hashed;
- 54 of 54 validation checks passed;
- proposal → final relationship joined on docket `FAA-2025-0926`;
- an unchanged rerun reported all 12 representations unchanged.

## Reproduce It

Either re-acquire from the official sources and compare hashes:

```bash
make sync
make acquire DOCS="2025-10764 2025-18469" STORAGE_ROOT=data/reproduce
```

Or download the exact frozen bytes from the release
[`raw-gen-20260926T213233Z-000f808f`](https://github.com/tanayvenkata/faa-directive-impact/releases/tag/raw-gen-20260926T213233Z-000f808f)
and verify them:

```bash
tar -xzf gen-20260926T213233Z-000f808f-raw.tar.gz
cd gen-20260926T213233Z-000f808f && shasum -a 256 -c SHA256SUMS
```

The `SHA256SUMS` entries equal the hashes in the committed receipts. The test
suite (`make check`, 92 tests) runs fully offline; a fixture fails any test
that reaches a real network transport.

## What Surprised Us

Each of these was found against live sources, not anticipated in design:

1. **The official PDF typesets identifiers with an en dash.** The first
   validated run failed its own identity gate: GovInfo prints
   `2025–10764`, not `2025-10764`. The fix normalizes typographic dashes but
   requires the full `FR Doc. <number>` line.
2. **Official PDF pages carry neighbouring documents.** The same page includes
   another document's `FR Doc.` line, so a bare number match would have
   accepted the wrong evidence.
3. **The API record changes when the document doesn't.** API JSON includes a
   `page_views` counter. A raw-hash comparison would flag it as a new version on
   every run, so logical versions ignore that one explicitly named field while
   the exact bytes are still retained.
4. **HTML element IDs are positional.** `p-1`…`p-46` would renumber if a
   paragraph were inserted, so they cannot be durable evidence anchors.
5. **The incorporation paragraph moves.** It is `(l)` in this thread and `(k)`
   in `2021-14268`, so it is found by heading text, not letter.
6. **The API does not link a proposal to its final rule.** The relationship
   is an identifier join on the shared docket, labelled `identifier_join`
   rather than a source assertion.

## Known Limits

- **One thread only.** Two documents, one supported engine family, no images,
  and no incorporated material. The image path and listed-material path are
  tested offline and exercised live on `2021-14268`, outside the accepted
  generation.
- **Volatile fields untested over time.** The `page_views` exclusion has been
  tested over minutes, not days.
- **No FAA DRS corroboration.** It is recorded as
  `deferred_access_verification`.
- **Snapshot, not monitoring.** Acquisition is run on demand; there is no
  scheduled synchronization, promotion, or rollback of derived indexes yet.
- **No practitioner review.** No aviation-maintenance practitioner has reviewed
  anything yet.

## Next

The next milestone writes the feasibility-seed evaluation cases, freezes the
numerical gates before tuning, and decides how image-only figures are
transcribed. Normalization is then built against those fixed targets.
