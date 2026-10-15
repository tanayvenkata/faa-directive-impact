# Step 7: Candidate Retrieval

- **ROADMAP step:** 7 (normalize and retrieve)
- **Question:** given an engine record and a date, does the system surface
  every directive the engine might fall under, without a person naming the
  directive first?
- **Pre-registered:** [`retrieval/PREREGISTRATION.md`](retrieval/PREREGISTRATION.md),
  committed before the corpus was acquired
- **Corpus:** frozen generation `gen-20261015T175844Z-57440372`, 57 documents
  ([decision](../generations/gen-20261015T175844Z-57440372/DECISION.md))
- **Run:** [`evaluation/runs/retrieval-r0-20261015T180258Z`](../evaluation/runs/retrieval-r0-20261015T180258Z/report.md)
- **Status:** gate 14 passes. No model calls; nothing judged by hand.

## The Short Version

A plain identifier match finds every directive the seed cases expect: 35 of
37 expected candidates, and both misses are engines outside the V2500-A5/D5/E5
family (a PW1133G-JM and a CFM56-5B4/3), whose expected outcome is "outside
supported scope", so neither is a false clear. Each in-family engine gets
8 to 20 candidates, and no CFM or Pratt & Whitney distractor reached one.

Building the corpus found a bug in the daily sync: two directives that apply
to V2500-A5/D5 engines were filed outside scope without review. It is fixed.

## Approach

S1 and the model comparisons were handed their directive. Retrieval removes
that: it starts from the engine.

- **Relevance, not sufficiency.** A candidate is a directive the engine
  might fall under. Deciding is left to the screener (S1 rules, or the rule
  interpreter on a rule record). A candidate with no rule record is shown
  as `not_yet_evaluated` and goes to review. Retrieval never clears an engine.
- **Identifiers, not topic words.** Applicability turns on engine model
  designations and part numbers, so the baseline is an inverted index over
  those two token types: the model in paragraph (c), and each installed part
  number anywhere in the regulatory text, tables included. Only documents
  published by the as-of date count, and a retrieved final brings its
  published corrections.
- **No cutoff.** Every candidate goes to screening; there is no top-k or
  score threshold to calibrate, so there is no threshold to get wrong.

The pre-registration allowed a second technique (BM25 over prose,
embeddings, query rewriting) only for a miss identifiers could not reach.
There was none, so none was added.

## Results (R0)

| Measure | Result |
|---|---|
| Gate 14, candidate recall (protected) | **pass**: 35/37 surfaced; no protected miss |
| Unprotected misses | seed-004 (PW1133G-JM) and seed-025 (CFM56-5B4/3): out-of-family engines, expected `outside_supported_scope` |
| M1 distractors for in-family engines | 48, all from two mislabeled documents (below); 0 from any true distractor |
| M2 part-number-only candidates | 21 |
| M3 candidates per case | median 16, max 20 |

Exact counts over 29 cases; no rate is claimed. With zero protected misses in
the 27 in-family cases, the true miss rate could still be about 11% (rule of
three).

## The Sync Bug It Found

AD 2012-09-09 (`2012-12329`) and AD 2015-10-04 (`2015-12068`) state
applicability as "This AD applies to:" followed by a list that includes
V2500-A1 and V2522-A5 through V2533-A5. The sync's scope reader took only the
lead-in, found no V2500 model, and filed both `outside_supported_scope`.
Under its own rules a mixed A1/A5 list goes to a person. The reader now
follows a lead-in into its list (`discovery/scope.py`, with a regression
test). The two records already in the discovery corpus still carry the old
classification until they are re-read; that follow-up is tracked in
`ROADMAP.md` step 7. Retrieval reads the full paragraph (c) and was never
affected.

## What This Can and Cannot Show

- **Small, author-built cases.** 29 seed cases written by the same reader
  as the rules. The distractors are real directives, chosen by a rule
  written before acquisition.
- **Frozen corpus.** The fleet view retrieves from this generation. A new
  in-scope directive found by the daily sync appears on the freshness page
  as `not_yet_evaluated`; it reaches fleet retrieval when a new frozen
  generation is acquired and accepted.
- **Serials in images.** AD 2021-11-51 lists serials in image-only tables
  (`E3_IMAGE_FIGURES.md`). Retrieval matches its part numbers and models,
  so the directive is still surfaced; the serial decision stays with review.
