# B2: Asking a Model Directly, Compared With the Rules

- **ROADMAP step:** 4 (full-context LLM comparison)
- **Question:** if a model reads the directive text and an engine's record,
  with no hand-written rules, how close does it get to the rules (S1)?
- **Scored under:** frozen gates v1, the same 33 units as S1, prompt version
  `e0a54c1578a5`
- **Status:** mechanical results final; the hand review of gates 5 and 11 is
  a first pass by Claude, awaiting the owner
  (`evaluation/review/b2-sonnet-r1/`)

## The Short Version

No model setting matched the rules. On the 18 AD 2025-19-13 units, where
the rules fail nothing, the best setting (Claude Sonnet 5.5 at high effort)
still failed about 2 protected checks per run. Cheaper settings failed 3–10.

Three things stand out:

1. **A plausible misreading, stated with confidence.** At low and medium
   effort, Sonnet read paragraph (g) as "remove the hub at the next shop
   visit, so with no shop visit there is no deadline." Under that reading a
   listed hub could keep flying past its removal limit. The FAA engineer's
   informal answer and the labels rule it out. At high effort the misreading
   mostly disappeared.
2. **More effort helped one model and not the other.** Sonnet's deadline
   errors fell from about 8 per run to 1 between medium and high. Haiku was
   flat from low to high, and at max it reasoned past 64,000 tokens without
   answering on about 30% of units.
3. **One false clear recurs.** Every setting except Sonnet at high cleared
   seed-013, an engine whose blades must be replaced at its next qualifying
   shop visit.

This supports the architecture in `APPROACH.md`: the final call should come
from rules a person has reviewed. The model's place is drafting those rules
(B3), where a mistake is caught once per directive instead of once per engine.

## Results

Each setting ran 3 times through the Batch API. "No answer" means the model
returned nothing usable; those units are counted separately from wrong
answers here. The gate reports count a no-answer as failing every gate it
covers.

| Setting | Cost per run (33 units) | Cost per engine check | No answer per run | Protected failures per run, 18 S1 units (answered) | Deadline errors (gate 8) | False clears, all 33 units |
|---|---|---|---|---|---|---|
| **S1 rules** | ~$0 | ~$0 | 0 | **0** | 0 | 0 |
| Haiku 5.5, low | $0.024 | $0.0007 | 0 | 3.3 | 1.3 | 0.7 |
| Haiku 5.5, medium | $0.033 | $0.0010 | 0 | 4.0 | 1.7 | 0.7 |
| Haiku 5.5, high | $0.048 | $0.0015 | 0 | 4.0 | 1.7 | 1.0 |
| Haiku 5.5, max (64K cap) | $0.443 | $0.0134 | 9.3 | 1.0 | 1.0 | 0 |
| Sonnet 5.5, low | $0.431 | $0.0131 | 0 | 9.7 | 8.7 | 1.0 |
| Sonnet 5.5, medium | $0.434 | $0.0132 | 0 | 9.3 | 8.3 | 1.0 |
| **Sonnet 5.5, high** | $0.565 | $0.0171 | 0 | **2.0** | 1.0 | **0** |

Haiku at max with the default 16,000-token cap is left out of the table:
about 30 of 33 units per run hit the cap during reasoning and returned no
answer. Those runs are kept as a configuration failure. Haiku at max with a
64,000-token cap still ran out on 9–10 units per run; its low failure count
on answered units covers only the units it finished.

Per-unit detail for every setting, with failures shown as runs out of 3, is
in [`b2-summary.md`](b2-summary.md).

### What fails, and why

| Unit | What happened | Settings | Kind |
|---|---|---|---|
| seed-005 | Removal stated at the current shop visit, or within 100 FC. The expected answer follows the FAA engineer's informal reply, which is not in the text. | All | Needs knowledge outside the text; written down before the first run |
| seed-006, 007, 008, 023, 026, 027, 028 | "No deadline unless a shop visit occurs"; the latest removal point left blank | Sonnet low and medium | Confident misreading of paragraph (g) |
| seed-013 | Cleared (`no_action_triggered`) instead of action at the next qualifying shop visit. The written timing states the future requirement correctly; the status field contradicts it. | All except Sonnet high | Protected false clear |
| seed-029 | The listed S/N under a dash-number P/N was put in `matched_parts` while the status said needs review | All | Part identity (gate 9); see the note below |
| seed-014 | A settled answer on an unadjudicated expert question | All | False confidence (gate 3) |
| seed-022/2021-14268 | The 10-FC deadline anchored on the effective date, ignoring actual notice of an emergency AD | All | False confidence (gate 3) and a missing fact |
| AD 2026-17-03 units | The correction document 2026-18423 not cited although the labels require it | Most | Required evidence (gate 10, aggregate) |

**Note on seed-029.** The answer schema had no way to say "possible match,
unconfirmed," so a model that listed the candidate in `matched_parts` while
answering needs review is scored as an inexact match. That is strict but
follows the gate text.

### Stability

Haiku changed its answer on 6–11 of 33 units between identical runs.
Sonnet changed on 1–3. A screen that gives different answers to the same
input needs a reviewer behind every answer, which removes most of the saving.

## What It Would Cost at Fleet Scale

For a fleet of 300 engines and about 20 in-scope directives, one full
re-screen is about 6,000 engine checks. With prompt caching and the Batch API:

| Approach | One full re-screen |
|---|---|
| S1 rules | about $0, the same answer every time |
| Sonnet 5.5 at high effort | about $100, with 1–3 answers per 33 changing between runs |
| Haiku 5.5 at low effort | about $4, with up to a third of answers changing between runs |

A rules design pays a model once per directive, to draft its rules (B3).
A model-only design pays per engine, per directive, every time records change.

## Method

- **Input.** Each unit gets its directive and the related documents
  (proposal, correction, supersession) published by its question date,
  rendered from the Federal Register XML. The Federal Register's own plain
  text silently drops image-only tables, so the rendering marks each image
  with a placeholder instead.
- **Prompt.** The outcome vocabulary and record conventions from
  `seed/README.md`, the supported models, the missing-fact path format, and
  the answer format. Never a case's title, label, rationale, forbidden
  claims, or the FAA adjudication; a test enforces this.
- **Answer.** Structured JSON in a fixed schema, converted to the shape the S1
  rules produce so the same scorer applies.
- **Settings.** Every run is identical except effort (and the output cap for
  Haiku max). Three repeats per setting. Prompt caching on the shared
  document; the Batch API at half price. Latency is not reported because a
  batch's wall-clock time measures the queue, not the model.
- **Spend.** $6.89 for every scored run in this report, including version 1
  and the failed Haiku max runs, plus under a cent for the plumbing checks.

## Deviations From the Plan, in Order

Each was recorded in the run directories and commits when it happened.

1. **Prompt version 1 → 2, format only.** Version 1's first scored runs wrote
   citation document numbers with extra text ("Federal Register 2025-18469 (AD
   2025-19-13)") and mixed record paths with prose. Version 2 constrains the
   format with the schema and changes nothing about content. The version 1
   runs are kept as scored, each with a note.
2. **Scorer fixes after the first runs.** A described missing fact starting
   with "operator" was misread as a record path. Locators are now checked
   against each document's full text. Both are applied to every version 2
   run from its recorded calls. The second fix only reduced hand review; it
   cannot turn a failure into a pass.
3. **Output cap.** Haiku at max effort needed more than the default 16,000
   tokens. The cap became a recorded run setting, and Haiku max was re-run
   at 64,000.

## What This Can and Cannot Show

- **Same author.** The labels, the gates, the rules, and this prompt come from
  one reading of the directives. Agreement with the labels is agreement with
  that reading. Practitioner review (issue #9) is the independent check.
- **Settings chosen on the test set.** The effort sweep ran on the scored
  units, so the best setting looks better than it would on new cases. Every
  setting is reported, not only the best.
- **Small sample.** 18 units for the paired comparison, 3 repeats per
  setting. These are exact counts, not rates.
- **Public cases.** The seed cases are on GitHub, so later models may have
  seen them in training. This does not affect the models run here.
- **Hand-checked gates are pending.** Gates 5 (forbidden claims) and 11
  (timing wording) have a first pass on Sonnet medium repeat 1 only, and the
  owner has not confirmed it. That first pass marks the shop-visit
  misreading as a timing contradiction on 8 units.

## Next

B3: a model drafts the rule record for a directive from its text,
deterministic checks verify every value against the text, and the S1 rules
apply the result. Sonnet 5.5 at high effort is the starting candidate, with
Haiku as the cost comparison.
