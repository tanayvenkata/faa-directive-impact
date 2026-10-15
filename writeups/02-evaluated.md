# Evaluated: Rules, a Model, and a Model Writing Rules

*Written 2026-10-11; finalized 2026-10-15. Every hand-checked result below
is a review by Claude, which also wrote the system being checked. The project
owner chose not to re-check them (2026-10-15), so no person has confirmed
them; see "Who checked what" at the end. This post makes
one claim: on a disclosed suite of cases for one directive, AD 2025-19-13
(IAE V2500-A5/D5/E5 engines), it measures how plain rules, a model reading
the directive, and a model drafting the rules each perform. It makes no claim
about any other directive or engine family.*

## The question

[*Reproducible*](01-reproducible.md) showed the project can get the same
official bytes twice. This rung asks whether it reads them correctly: given
a synthetic engine's records, does it say whether AD 2025-19-13 applies,
what must be done, by when, and which paragraph says so?

Three approaches were scored on the same cases under the same gates:

- **S1, rules.** Hand-written code for this one directive.
- **B2, ask a model.** Give a model the directive text and the engine record.
- **B3, a model drafts the rules.** A model writes the directive's rules as
  data once, and a fixed interpreter applies them to each engine.

## Cases and gates, frozen first

The seed has 33 scoring units across 29 cases; 18 units are AD 2025-19-13
([`GATES.md`](../evaluation/GATES.md), "Scoring Unit"). They are edge cases:
a serial number listed under a different part number, a shop visit inside
the 100-cycle grace window, a directive not yet in force.

The gates were frozen on 2026-10-06, before any run
([`GATES.md`](../evaluation/GATES.md)). Nine are protected: one failing unit
fails the system. They include no false clear, no scope leak, no settled
answer without the fact behind it, no made-up citation, exact cycle
arithmetic, and exact part identity. Four are aggregate, each with a small
budget. Two gates, forbidden claims (5) and timing wording (11), are judged
by hand.

## Results on the 18 AD 2025-19-13 units

| Approach | Protected gate failures per run (unit × gate) | False clears | Cost |
|---|---|---|---|
| S1 rules | 0 | 0 | ~$0 |
| B2, Sonnet 5.5 high (best setting) | 2.0 | 0 | $0.565 per 33-unit run |
| B2, other six settings | 1.0–9.7 on units answered | up to 1.0 per run, all 33 units | $0.024–$0.443 per run |
| B3, Opus 5.5 high, drafted rules | 10 (all gate 8, one per unit) | 0 | $0.35 for three runs |

Sources: S1 [`verdict.md`](../evaluation/runs/s1-20261006T223638Z-6a301b1/verdict.md);
B2 [`B2_FULL_CONTEXT.md`](../evaluation/B2_FULL_CONTEXT.md) "Results" and
[`b2-summary.md`](../evaluation/b2-summary.md); B3
[`B3_RULE_EXTRACTION.md`](../evaluation/B3_RULE_EXTRACTION.md) and
[`b3-summary.md`](../evaluation/b3-summary.md). B2 ran each setting three
times, B3 three times; B2's Haiku-at-max count covers only the units it
answered.

**S1 passes every gate.** The decision under the frozen verdict rules is
*go* ([`S1_BASELINE.md`](../evaluation/S1_BASELINE.md)). Its hand-checked
gates 5 and 11 were judged by Claude only.

**B2 matched the rules at no setting.** The best setting still failed seed-005
(a deadline that depends on an informal FAA answer not in the text) and
seed-029 (part identity) in every run. At low and medium effort Sonnet read
paragraph (g) as "no shop visit, no deadline", a confident misreading under
which a listed hub could fly past its limit. On AD 2026-17-03's seed-013, outside
the 18 units, every setting that answered it except Sonnet high cleared an
engine that needs action. Haiku
changed its answer on 6–11 of 33 units between identical runs; Sonnet on
1–3. B2's hand-checked gates were judged by Claude only.

**B3 drafted every data field right and left one clause open.** In all three
repeats Opus transcribed 17/17 data fields for AD 2025-19-13, including all
eight serial numbers and limits. It coded paragraph (g)'s timing as
`"unclear"` and listed it as ambiguous. The interpreter does not guess, so 10
of 18 units went to review without a deadline. That is a safe failure: no
engine was cleared. It is still a failure under gate 8. Changing that one
field reproduces the hand-written reference on all 23 units B3 scored
(a test asserts it). The clause it flagged is the one the project had to
ask the FAA about. Proofreading time, the third B3 measure, was not
measured: no person proofread the drafts. Whether each flagged ambiguity is
real was judged by Claude only.

A second directive, AD 2026-17-03, was scored for B3 only, as evidence that
the approach transfers: 18/18 fields and every unit matching its reference.
Its labels are Claude drafts that no person has confirmed, so these results
are weaker evidence, and they do not widen the evaluated claim. S1's parser, run unchanged on it, stops at
its first check: nothing in S1 transfers.

## What the numbers can bear

- **Small and exact, not rates.** With zero failures in 18 units, the true
  failure rate could still be about 17%; on gate 1's ten units, about 30%
  ([`GATES.md`](../evaluation/GATES.md), "What the Sample Can Show").
- **One author.** The same reader wrote the labels, gates, rules, reference
  records, and prompts. A pass shows agreement with one reading of the
  directive, not that the reading is right. A shared misreading would pass
  every gate. Practitioner review is the independent check, and it has not
  happened.
- **Settings chosen on the test set.** B2's effort sweep ran on the scored
  units. Every setting is reported, not only the best.
- **Interpreter tuned against S1.** B3's interpreter was corrected on three
  seed units before the freeze, so the reference passing through it is not
  independent evidence ([`B3_RULE_EXTRACTION.md`](../evaluation/B3_RULE_EXTRACTION.md),
  "Deviations").
- **S1 leans on two outside inputs.** It encodes an informal FAA reply on
  a shop visit inside the 100-cycle window (T2), and it assumes a hub gains
  cycles one-for-one with its engine from the effective date (T3)
  ([`S1_BASELINE.md`](../evaluation/S1_BASELINE.md), "Failure Taxonomy").
- **Hand-checked gates were judged by Claude only**, and the B2 hand review
  covers only Sonnet repeat 1 at medium and high.

## Failures and gaps, in one place

| What | Where |
|---|---|
| seed-005 needs an informal FAA answer no text supplies. Only S1 passes it, because S1 encodes that answer (taxonomy T2); B2 and B3's own hand-written reference both fail it | B2, B3 |
| Paragraph (g) misread at Sonnet low/medium; left open by B3 | B2, B3 |
| False clear on seed-013 (AD 2026-17-03, outside the evaluated claim) at every B2 setting that answered it, except Sonnet high | B2 |
| Haiku at max effort ran out of tokens on about 30% of units | B2 |
| Structured outputs refused B3's schema as too large; JSON is validated afterwards | B3 |
| S1's rules are hand-written for one directive (taxonomy T4) | S1 |
| Image-only tables in two seed directives stay `needs_review` until a person reads them | [`E3_IMAGE_FIGURES.md`](../evaluation/E3_IMAGE_FIGURES.md) |
| Not exercised: retrieval (gate 14), recurring actions, counting boundaries | [`GATES.md`](../evaluation/GATES.md) "Known Gaps" |

## What it suggests

The final call should come from rules a person has reviewed. A model is
useful for drafting those rules once per directive, where a person catches a
mistake once rather than once per engine. Re-screening a 300-engine fleet
against about 20 directives would cost up to about $100 with Sonnet at high effort
(an upper estimate), and about $0 with rules ([`B2_FULL_CONTEXT.md`](../evaluation/B2_FULL_CONTEXT.md),
"What It Would Cost at Fleet Scale").

## Who checked what

On 2026-10-15 the project owner waived the planned sign-offs in
[`OWNER_PACKET.md`](../evaluation/review/OWNER_PACKET.md): the B3 proofread
and ambiguity judging, the AD 2026-17-03 labels, and the S1 and B2 hand
reviews. The mechanical gates are computed by code from kept runs. The hand
gates, the AD 2026-17-03 labels, and the B3 ambiguity judgments are Claude's
alone. A practitioner review (issue #9) is the next rung,
*Practitioner-reviewed*; it is deferred, and this post does not claim it.

Every run is kept under [`evaluation/runs/`](../evaluation/runs/) and
re-scores offline (`make b3-replay RUN=...`, `make s1-conclude RUN=...`).
The daily sync that keeps the wider directive corpus current is live at
<https://tanayvenkata.github.io/faa-directive-impact/>.
