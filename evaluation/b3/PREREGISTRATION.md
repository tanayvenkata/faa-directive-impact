# B3 Pre-Registration

Written 2026-10-11, after the three scored runs (Opus 5.5, high effort,
repeats 1–3, prompt `93fa052fe394`, interpreter v1) were started and before
any of their outputs or reports were opened.

## Fixed before reading results

1. **Model and repeats.** One model, `claude-opus-5-5` at high effort, three
   repeats through the Batches API. Rule drafting runs once per directive, so
   cost does not argue for a smaller model; the repeats measure how much the
   draft varies, not a model comparison. All three runs are kept. None is
   rerun to replace another. A run that crashes after its batch returns is
   re-scored from its recorded calls, never re-called.
2. **Interpreter.** Version 1 stays frozen for these runs. It is not changed
   after reading any output.
3. **`combination: "unclear"`.** AD 2025-19-13 (g) states "whichever occurs
   later", so `"unclear"` there is scored as a field error; the ambiguity the
   reference records belongs under `ambiguities`. End to end, the frozen gate
   results stand unchanged, but each failing unit is reported in one of two
   classes:
   - **Safe escalation:** the interpreter declined an action it does not
     support (its output carries the "is not evaluated" note) and the unit
     went to `needs_review`. Gate 1 (false clear) is never in this class.
   - **Substantive extraction error:** every other gate that fails with the
     draft but passes with the reference.
4. **Proofreading.** The owner proofreads repeat 1's drafts, with a timer,
   before seeing field scores or the reference records. The repeat was chosen
   here, not after seeing scores.
5. **What is headline.** Field accuracy is reported in two groups: data
   fields (dates, models, part numbers, serial numbers, limits, paragraphs)
   and vocabulary fields (`applies_to`, `trigger`, `combination`), because the
   vocabulary was designed from the two scored directives and partly supplies
   its own answers. End-to-end results are reported both as the delta from
   the reference record and as absolute gates against S1.

## Deviation recorded afterwards

- **2026-10-11: the proofreading is not blind.** Item 4 asks for the owner to
  proofread before seeing results. Claude's progress messages in the working
  session reported the headline results (every data field right; AD
  2025-19-13 (g) coded `"unclear"`) before the proofreading sheet existed.
  The sheet records whether the owner saw them, and the write-up discloses
  it. Nothing else above changed.
