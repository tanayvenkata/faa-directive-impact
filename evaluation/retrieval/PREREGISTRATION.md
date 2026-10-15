# Retrieval Pre-Registration (ROADMAP step 7)

Committed 2026-10-15, before the retrieval corpus was acquired and before any
retrieval run. Changes after the first run are recorded under "Deviations"
below, never edited into the sections above it. `GATES.md` is not edited.

## Task

Given one engine record (`asset_snapshot` in the seed-case schema) and an
as-of date, return the candidate directives a screener must consider. This
is **relevance only**: a candidate is a directive the engine might fall
under. Whether the evidence is sufficient to decide is the screener's job
(S1 rules, or the rule interpreter on a rule record); a candidate with no
rule record goes to `needs_review` as `not_yet_evaluated`. Retrieval never
clears an engine.

## Corpus

A new `frozen_evaluation` generation, acquired with the existing `acquire`
command, holding:

| Group | Documents | Rule |
|---|---|---|
| Seed threads | 10 | The seed generation `gen-20260926T215105Z-7fe9da08` (proposals, finals, correction) |
| In-scope finals not in the seed | 8 | Discovery generation `gen-20261014T171827Z-398619f9`: coverage `evaluated` or `not_yet_evaluated` |
| IAE out of scope (distractors) | 22 | Same generation: title names International Aero Engines, `outside_supported_scope` read from paragraph (c), published 2012-01-01 or later |
| CFM International (distractors) | 9 | Title names CFM International, published 2025-01-01 or later |
| Pratt & Whitney (distractors) | 8 | Title begins "Airworthiness Directives; Pratt & Whitney", not Canada, published 2023-01-01 or later |

The exact lists are in [`corpus-selection.json`](corpus-selection.json),
computed from the discovery records by the rule above. The distractors are
near neighbors: same airframe family (A320, MD-90, C-390) or same
manufacturer, so a retriever that matches on "engine" or "turbine" words
would surface them.

Raw bytes stay under git-ignored `data/`; the generation's manifest,
receipts, and validation are committed under `generations/`. Normalized
retrieval records (document identity, kind, dates, relationships, the models
paragraph, and every part-number token with its paragraph) are committed, so
tests and CI run without raw bytes. The index is rebuilt from them and is
never the source of truth.

## Baseline R0 (frozen)

An identifier-match lexical retriever: an inverted index over two token
types, chosen because directive applicability is decided by identifiers,
not by topic words.

- **Engine model.** The engine's `engine_model`, uppercased with spaces
  removed, matched against the model designations listed in the directive's
  applicability paragraph (c).
- **Part number.** Every installed component `part_number` other than
  `unknown`, matched as a whole token anywhere in the directive's regulatory
  text (paragraphs (a) onward, including tables).
- **Time.** Only documents published on or before the as-of date.
- **Threads.** A retrieved final rule brings its corrections published by
  the as-of date. Proposals are indexed like finals.

A document is a candidate if either token type matches. Candidates are
ordered: part-number match first, then model-only, then newest first. There
is no score cutoff and no top-k: the whole candidate set goes to screening.

## Measures

| # | Measure | Kind |
|---|---|---|
| Gate 14 | Candidate recall, exactly as `GATES.md` v1 defines it: for each case, the share of its `directive_candidates` surfaced. A missed candidate whose expected outcome is `action_required*` or `needs_review` is a protected failure (false clear by omission) | Protected gate |
| M1 | Distractor inclusion: candidates from the CFM, Pratt & Whitney, or out-of-scope IAE groups surfaced for an in-family (V2500-A5/D5/E5) engine | Report only |
| M2 | Part-number-only candidates: surfaced by a part number while paragraph (c) does not list the engine model | Report only |
| M3 | Candidate-set size per case: median and maximum | Report only |

Counts are exact; with 29 cases no rate is claimed. Cases whose expected
outcome is `outside_supported_scope` (engines outside the family) may show a
missed candidate without a protected failure; they are reported separately.

## Decision rule

- R0 passes if gate 14 has no protected failure.
- If R0 fails, diagnose the stage (corpus coverage, parsing, tokenization,
  time filter, thread expansion) and change only that stage. The change is
  run as R1 on every case, reported paired with R0, and recorded below as a
  deviation. M1 to M3 are never tuned.
- A technique beyond R0 (BM25 over prose, embeddings, query rewriting) is
  added only for an observed miss that R0's identifiers cannot reach.

## Deviations

None yet.
