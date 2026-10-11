# Review: B3, Opus 5.5 high, repeat 1

About 55–70 minutes, in three parts. Do part 1 **before** opening
`judgments.yaml` (in this directory), `writeups/02-evaluated.md`,
`evaluation/B3_RULE_EXTRACTION.md`, `evaluation/b3-summary.md`, or
`evaluation/b3/reference/`. In the run directory, open only `proofread.md`
and `extractions/`; its other files are results. Repeat 1 was chosen for
this in advance (`evaluation/b3/PREREGISTRATION.md`).

## Part 1: proofread the drafted rules, with a timer (the B3 measure)

For each directive:

1. Open the AD text on federalregister.gov: document 2025-18469 for AD
   2025-19-13; documents 2026-16954 and its correction 2026-18423 for AD
   2026-17-03.
2. Start a timer. Open the drafted record:
   `evaluation/runs/b3-opus-5-5-high-r1-20261011T155547Z-9f32a55/extractions/<document>.json`
   (`proofread.md` in the same run shows both).
3. Check every field against the text. Note each field you would change and
   what you would change it to. Stop the timer when you would sign the
   record off as corrected.
4. Fill in `proofread.yaml`: minutes, and each correction.

You are proofreading as the person who approves rules before they screen a
fleet. Judge against the AD text, not against anything the project wrote.

## Part 2: judge the drafted ambiguities (after part 1)

Now read `evaluation/B3_RULE_EXTRACTION.md` and open `judgments.yaml`. For each
ambiguity the draft listed, say whether it is a real ambiguity in the text
(`real`, `not_real`, `unsure`) and whether it is the same as the reference's
(where one exists). Claude's first-pass views are filled in; agree or
disagree.

## Part 3: the AD 2026-17-03 labels and reference record (after part 2)

These are Claude drafts (`labeled_by: claude-draft`). Read
`evaluation/seed/cases/seed-011.yaml` to `seed-014.yaml`, the 2026-16954
outcome in `seed-023.yaml`, and `evaluation/b3/reference/2026-16954.json`
against AD 2026-17-03 and its correction. In `judgments.yaml` set
`labels_2026_17_03_confirmed` and `reference_2026_16954_confirmed` to `true`
if they are a fair reading, or `false` with what you would change in
`part_3_note`.
About 15 minutes.

Then commit both sheets and ask Claude, in a new session, to fold them in.
Nothing here changes `evaluation/GATES.md` or a seed case; a disagreement
with a label goes through "Disputed Labels".
