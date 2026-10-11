# Review: B3, Opus 5.5 high, repeat 1

About 40–60 minutes, in two parts. Do part 1 **before** opening
`evaluation/B3_RULE_EXTRACTION.md`, `evaluation/b3-summary.md`, the run's
`report.md`, or `evaluation/b3/reference/`. Repeat 1 was chosen for this in
advance (`evaluation/b3/PREREGISTRATION.md`).

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

Now read `evaluation/B3_RULE_EXTRACTION.md`. In `proofread.yaml`, for each
ambiguity the draft listed, say whether it is a real ambiguity in the text
(`real`, `not_real`, `unsure`) and whether it is the same as the reference's
(where one exists). Claude's first-pass views are filled in; agree or
disagree.

Then tell Claude it is done. Nothing here changes `evaluation/GATES.md` or a
seed case; a disagreement with a label goes through "Disputed Labels".
