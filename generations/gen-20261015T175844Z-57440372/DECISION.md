# Raw Generation Decision: gen-20261015T175844Z-57440372

**Decision: ACCEPTED as the retrieval corpus for ROADMAP step 7** —
2026-10-15. It makes no evaluation or impact claim by itself.

| Field | Value |
|---|---|
| Generation | `gen-20261015T175844Z-57440372` |
| Corpus track | `frozen_evaluation` |
| Acquisition run | `run-20261015T175844Z-57440372` |
| Completeness | `complete`, no missing artifacts; validation `passed` |
| Storage root | clean `data/retrieval-frozen/`, not committed |

## Scope

57 Federal Register documents, chosen by the rule in
[`evaluation/retrieval/PREREGISTRATION.md`](../../evaluation/retrieval/PREREGISTRATION.md)
before acquisition: the ten seed documents, the eight other in-scope V2500
final rules in the discovery corpus, and 39 near-neighbor distractors (IAE
outside the family, CFM International, Pratt & Whitney). The exact list is
[`evaluation/retrieval/corpus-selection.json`](../../evaluation/retrieval/corpus-selection.json).

Raw bytes stay local. Retrieval records normalized from this generation are
committed as [`evaluation/retrieval/corpus.json`](../../evaluation/retrieval/corpus.json)
(`make retrieval-corpus`); Federal Register text is a U.S. Government work
(`REDISTRIBUTION.md`). Graphics are not redistributed.
