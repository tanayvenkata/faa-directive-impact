# E3: Image-Only Figures — Proposed Decision

- **Issue:** #14
- **Status:** proposed by Claude 2026-10-11; **the owner decides** (labeling
  and transcription policy are the owner's calls). Nothing below is built yet.

## The question

Some directives print a compliance table as an image instead of text. The
Federal Register's plain text drops it without a trace, and the XML has only
an image reference. How does such a table become data the rules can use,
with a verification status and a citation to the retained image, without
being treated as authoritative?

## What the corpus shows

Counted in the frozen seed corpus (`data/seed-frozen`, ten documents):

| Document | Directive | Text tables | Image-only figures |
|---|---|---|---|
| 2021-14268 | AD 2021-11-51 | 2 | 2 (`ER02JY21.000`, `.001`): engine serials paired with HPT 1st-stage disk serials |
| 2022-02574 | AD 2022-02-09 | 2 | 2 (`ER08FE22.048`, `.049`): compliance-time tables |
| the other eight | including AD 2025-19-13, AD 2026-17-03 and its correction, AD 2025-17-16 | 1–4 each | none |

- **XML-first parsing is adequate for the compressor-blade (AD 2026-17-03)
  and ALS (AD 2025-17-16) threads** (issue #14, open question 1): every
  table in them is XML text, and B3 drafted AD 2026-17-03's rules from that
  text with every data field right.
- The four images are small, clean typeset tables (about 7 rows × 2 columns
  each), retained at original size with SHA-256 receipts, and already
  reviewed as redistributable U.S. Government text (`REDISTRIBUTION.md`).

## Options

| Option | Effort per figure | Risk | Fit |
|---|---|---|---|
| A. Manual transcription by a person | Minutes | A single typist's slip goes unseen | Fine at this scale; no second check |
| **B. Model drafts, a person verifies (recommended)** | Minutes | Low: two independent reads must agree | Same pattern as B3: the model drafts, a person approves |
| C. Exclude image-only figures | None | Every engine those tables cover goes to `needs_review` forever | Safe but leaves AD 2021-11-51 and AD 2022-02-09 unusable |

## Recommendation: B, as a double read

1. **Two independent reads.** A model (Opus 5.5, from the retained original
   image) and a person each transcribe the table without seeing the other's.
2. **Compare cell by cell** in code. Every disagreement goes to the person,
   who settles it against the image; agreements are still spot-checked.
3. **Store as derived data**, never in place of the source: each cell keeps
   the image's receipt ID and SHA-256, the reader(s), and a
   `verification_status` of `unverified`, `double_read_agreed`, or
   `person_resolved`. The rules use only verified tables.
4. **Fail closed.** An unverified or partly verified table makes the engine
   `needs_review` with the image named as the missing fact. That is what the
   seed cases for these directives already expect.
5. **Re-verify on change.** A new image hash invalidates its transcription.

Why B over A: the cost is the same at this size, and the second read catches
the transposed digit a single typist would miss. Serial numbers decide
applicability, so that miss would be a wrong answer, not a cosmetic one.

## What the owner decides

- A, B, or C (or a variant). If B: whether the person's read can be the
  owner's own, and whether a spot check of agreed cells is required.
- Once decided, this file becomes the decision record and issue #14 closes.
