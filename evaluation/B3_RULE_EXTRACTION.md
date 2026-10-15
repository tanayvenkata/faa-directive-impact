# B3: A Model Drafts the Rules, Compared With Hand-Written Rules

- **ROADMAP step:** 5 (rule extraction for new directives)
- **Question:** if a model reads a directive and drafts its rules (models,
  part conditions, listed parts and limits, triggers, the paragraph behind
  each), and a fixed interpreter screens engines from that draft, how close
  does it get to rules written by hand? Does it flag ambiguity instead of
  guessing?
- **Scored under:** frozen gates v1; prompt `93fa052fe394`; interpreter v1;
  the 18 AD 2025-19-13 units S1 is scored on, plus the 5 AD 2026-17-03 units,
  reported separately
- **Model:** Claude Opus 5.5 at high effort, 3 repeats (Batches API)
- **Pre-registered:** [`b3/PREREGISTRATION.md`](b3/PREREGISTRATION.md),
  committed before any run was read
- **Status:** mechanical results final. On 2026-10-15 the owner waived the
  proofread, the ambiguity meaning check, and confirming the AD 2026-17-03
  labels and reference record ([`review/b3-opus-r1/`](review/b3-opus-r1/)).
  Proofreading time is not measured; the other two are Claude's judgment only

## The Short Version

Opus drafted every data field right in all three repeats: effective dates,
the ten engine models, the AD 2026-17-03 part condition, all eight AD
2025-19-13 table rows with their serial numbers and limits, eligible parts,
and the scored paragraph labels (effective date, models, part condition,
actions, definitions, AMOC): 17/17 and 18/18 per repeat. It never cleared an
engine that needs action, and it made no substantive extraction error (the
pre-registered class).

It did not reproduce the hand-written rules end to end. In every repeat it
coded AD 2025-19-13 paragraph (g)'s timing as `"unclear"` rather than
"whichever occurs later", and listed the clause as ambiguous. The
interpreter does not guess at an unclear rule, so it sent 10 of the 18 units
to review without a deadline where the hand-written rules give one. That is
a safe failure, not a wrong answer, but it is a failure: those engines get no
deadline until a person settles the clause. Correcting that one field in each
draft reproduces the hand-written reference's outcomes and deadlines on all
23 units.

The clause it flagged is the one the project had to ask the FAA about. One of
its readings in each repeat is "the later of the hub's limit and the
100-cycle window". That matches the FAA engineer's informal answer for a
shop visit inside the window; the FAA's view of a visit after the window is
still pending, and the drafts' reading goes further than the answer does. Under the
pre-registered rule this still counts as a field error, because the text
does say "whichever occurs later"; the open question is what that phrase
compares, not whether it is there.

On AD 2026-17-03 the drafts were right on every field, and every unit came
out as it does with the hand-written reference. The drafts flagged an
ambiguity in (g), but a different one from the reference: whether "is
exposed" carries the (h)(2) definition (a blade removed from the drum) or
its ordinary meaning. They never raised the reference's question (does the
requirement carry forward past a visit with no exposure, or lapse). The
drafts' question is real. Seed-014 settles it by reading (g) through (h)(2),
and the reference record should have listed it.

Three runs cost $0.35 in total.

## Results

Fractions are correct/total per repeat. "Safe escalation" and "substantive"
are the classes registered in advance: a unit is a safe escalation when the
interpreter declined an action it does not support and sent the unit to
review (gate 1 never counts); every other gate that fails with the draft but
passes with the reference is substantive.

| Directive | Data fields | Vocabulary fields | Units: safe escalation | Units: substantive | False clears |
|---|---|---|---|---|---|
| AD 2025-19-13 (2025-18469), each repeat | 17/17 | 2/3 | 10/18 | 0/18 | 0 |
| AD 2026-17-03 (2026-16954 + correction 2026-18423), each repeat | 18/18 | 3/3 | 0/5 | 0/5 | 0 |

All three repeats gave the same field results and the same unit outcomes.
Per-run detail: [`b3-summary.md`](b3-summary.md); each run's `report.md`
under `runs/b3-opus-5-5-high-r*`.

**Against S1 (absolute).** S1 passes every protected gate on the 18 AD
2025-19-13 units. With the drafted rules, 10 units fail gate 8 (exact
arithmetic; protected), 8 of them also gate 12 (needless escalation), all
from the declined (g) timing. One of the 10 is seed-005, which fails with the
reference rules too: its shop visit falls inside the 100-cycle window, the
readings diverge, and only the FAA's informal answer settles it. No
extraction can supply that answer.

**Against the reference, through the same interpreter.** The reference rules
fail only seed-005 (gates 8 and 12) on AD 2025-19-13, and gate 10 (required
evidence; not protected) on seed-013 and seed-014, because the interpreter
does not cite the preamble. The drafts add the declined timing and nothing
else.

**Ambiguity.**

| Directive | Reference ambiguity | Registered score (same paragraph) | First-pass meaning check (Claude) |
|---|---|---|---|
| AD 2025-19-13 | (g): what "whichever occurs later" compares | 3/3 | Same ambiguity, 3/3 |
| AD 2026-17-03 | (g): carry forward or lapse after a visit without exposure | 3/3 | Different ambiguity, 0/3 |

The drafts also raised one ambiguity the reference does not list, in every
repeat: AD 2025-19-13 (i)(2), what "major mating engine flanges, H-P" means
(flanges H through P, or something else). It decides which maintenance
counts as a shop visit. The owner's proofreading decides whether it is real.

## The Baseline: S1's Parser on a Second Directive

ROADMAP step 5 asks for the S1 parser run unchanged on a second directive.
Run as written on AD 2026-17-03, it stops at its first check: it verifies
the XML against the receipt for 2025-18469, the only document it knows.
Pointed at the right receipt, it reads the effective date and the ten models
from (c), then fails. It finds no (g) grace window and no table, and it
never sees the part-number condition in (c). Nothing in S1 transfers to a
second directive: every predicate it reads is hand-written for AD 2025-19-13.
That is the cost B3 is meant to remove.

## Method

1. **One schema for every directive.**
   [`schemas/b3-rule-record.schema.json`](../src/faa_directive_impact/schemas/b3-rule-record.schema.json)
   states a directive's predicates: the governing document (the final rule,
   or a correction that republishes its text), corrections, effective date,
   models, an optional part condition, listed parts with limits, eligible
   parts, required actions (target, trigger, condition, limits, how they
   combine), installation prohibitions, definitions, the AMOC paragraph,
   ambiguities, and notes. Each value names its paragraph.
2. **One interpreter.**
   [`rules/interpreter.py`](../src/faa_directive_impact/rules/interpreter.py)
   screens an engine from any rule record and returns the output shape the
   frozen scorer reads. Its vocabulary is small and fixed; an action outside
   it, or one marked `"unclear"`, goes to review with a note rather than a
   guess. It applies no adjudication.
3. **Hand-written reference records** for both directives
   ([`b3/reference/`](b3/reference/)). Through the interpreter, the AD
   2025-19-13 record reproduces S1 on every unit except seed-005 (a test
   asserts this).
4. **Prompt.** [`b3_prompt.py`](../src/faa_directive_impact/evaluation/b3_prompt.py)
   gives the directive's whole thread (proposal, final rule, correction) and
   describes the schema and vocabulary only: no case, label, reference
   value, known ambiguity, or adjudication (a test checks the labels and
   reference ambiguities are absent). A format-only plumbing call on AD
   2025-17-16, which B3 does not score, parsed and validated; then the prompt
   was frozen.
5. **Runs.** One call per directive per repeat; every request and response is
   recorded under each run's `calls/`. `make b3-replay RUN=...` re-scores a
   run offline.
6. **Scoring.** Field accuracy compares each drafted field with the
   reference exactly. End to end, every unit is screened from the draft and
   from the reference and scored under the frozen gates.

## Deviations From the Plan, in Order

1. **No structured outputs.** The rule schema was too large for the API's
   structured-output grammar ("The compiled grammar is too large"). Probing
   with tiny calls showed the size came from the schema as a whole, not one
   section; removing union types and nesting was not enough. The model
   therefore writes the record as plain JSON, the schema is stated in the
   prompt, and every answer is validated afterwards. An invalid answer is no
   answer, as in B2. All six scored answers validated.
2. **Schema reshaped before the freeze.** To try to fit the grammar,
   per-value sources became paragraph labels within the governing document.
   This happened before any scored call.
3. **One model, not a sweep.** The plan named Sonnet 5.5 and Haiku 5.5. The
   owner chose to use the strongest suitable model without a bake-off: rules
   are drafted once per directive, so cost does not argue for a smaller
   model. The repeats measure variation, not a model comparison.
4. **Interpreter corrected against S1 before the freeze.** While porting S1's
   logic, three differences found by comparing with S1 on seed units were
   fixed (seed-008 and seed-027: a timed action stands while another fact is
   missing; seed-029: cite the eligible-part definition). So the reference
   passing through the interpreter is not independent evidence; the
   draft-against-reference comparison is unaffected.
5. **Repeat 3 ran at a later commit** (`f92eb7e`), which changed only how a
   run records an interpreter crash. Prompt and interpreter were unchanged,
   and no crash occurred.

## What This Can and Cannot Show

- **It shows the model can transcribe a directive's predicates.** Every data
  field, including eight serial numbers and limits, was right three times
  out of three on two directives. The Drop thesis (2026) reported 93.8%
  field accuracy on 15 A320 directives, with affected parts the weakest
  field; two directives here cannot support a comparable rate.
- **It does not show the drafts can replace a reviewer.** The one clause that
  decides when most hubs come off was left open. That is the right behavior
  for a draft a person must approve, and it is exactly why the person is
  needed.
- **The vocabulary was designed from these two directives.** `applies_to`,
  `trigger`, and `combination` partly supply their own answers, so they are
  reported apart from data fields. A third directive will need vocabulary
  the interpreter lacks; until then, its actions go to review.
- **The references and labels share an author with the interpreter (Claude).**
  Agreement shows consistency with one reading, as S1's does. AD 2026-17-03's
  labels and reference are Claude drafts no person confirmed, and its results do not
  widen the evaluated claim beyond AD 2025-19-13.
- **Proofreading time is not measured.** It is the third B3 measure in
  `APPROACH.md` and needs a person with a timer; the owner waived it on
  2026-10-15. Any later proofread would not be blind: the owner has seen the
  headline results.
- **Not every paragraph label is scored.** Listed-part and eligible-part rows
  are compared on their identifiers and limits, not their paragraph labels.

## Next

- If time allows later: a person proofreads repeat 1 with a timer and
  checks the ambiguity readings ([`review/b3-opus-r1/`](review/b3-opus-r1/)).
- One proofreading correction closes the gap. Changing only the (g)
  combination from `"unclear"` to "whichever occurs later" in each repeat's
  draft reproduces the reference's applicability, status, and computed
  deadlines on all 23 units (a test asserts this), and so S1's on every AD
  2025-19-13 unit but seed-005. Gate results were also compared locally,
  where the source documents are available, and matched. That is the intended workflow: the model drafts, a person
  settles what it flagged. Whether the owner makes that correction is the
  owner's call, not this write-up's.
- Add the AD 2026-17-03 "is exposed" ambiguity to its reference record if the
  owner agrees it is real (through the "Disputed Labels" path in
  `GATES.md`, not by editing to match a run).
