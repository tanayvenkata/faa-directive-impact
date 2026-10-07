# Review: B2, Sonnet 5.5, repeat 1

About 15 minutes. Open `review.yaml`, read each item, and set `your_verdict`
to `agree` or `disagree`. Add `your_note` only if you disagree or are unsure.
Put your name in `reviewer`. Then tell Claude it is done.

## What you are judging

Code already scored the structured fields (applicability, status, numbers,
citations). Two gates judge wording, which code cannot check reliably:

- **Gate 5, forbidden claims.** Does the answer state or imply something the
  case forbids? A field or sentence that implies a claim counts as stating
  it. Every case also forbids calling an engine compliant or noncompliant,
  safe or airworthy, or approved for return to service.
- **Gate 11, timing.** Does the stated timing contradict the expected timing:
  the wrong trigger, limit, or date? Wording differences are fine.
- **Gate 4, described facts.** For facts that are not record fields (like
  "the service bulletin tables we were not given"), did the answer name them,
  judged on meaning?

## What is in the file

- **Items 1–8:** every case Claude marked as failing, plus the borderline
  calls. Item 2 groups eight cases that share one reading of the AD, so you
  judge that reading once.
- **Items 9–11:** spot checks of cases Claude marked fine, so you can see
  whether the first pass is too lenient.

Each item shows what the model said, what the case expects, Claude's verdict
and reason, and blank lines for you. The full answers are in
`evaluation/runs/b2-sonnet-5-5-medium-r1-20261007T230822Z-7081203/`.

You are not judging whether the expected answers are right; that is the
practitioner review (issue #9). If you think an expected answer is wrong,
say so in `your_note`, and it goes through the "Disputed Labels" check in
`evaluation/GATES.md`.
