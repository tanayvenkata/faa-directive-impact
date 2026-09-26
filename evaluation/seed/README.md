# Feasibility Seed

Twenty-five manually inspectable cases that establish the first failure
taxonomy. They are a feasibility seed, not a corpus limit or a release
threshold. Each case is one synthetic engine, one accepted source generation,
and the expected directive-impact outcome.

Cases live in `cases/seed-NNN.yaml` and are validated by the packaged
`seed-case.schema.json`. `make test` also checks every case against its source
generation.

## Labels

| Classification | Meaning |
|---|---|
| `potentially_affected` | Applicability predicates are met by supplied facts |
| `not_affected_for_directive` | Supplied facts establish the directive does not apply |
| `needs_review` | A required fact or interpretation is missing; the missing item is named |
| `outside_supported_scope` | The engine is outside the supported V2500 family; no determination is made |

The system never claims compliance, noncompliance, maintenance adequacy, or
return-to-service authority.

## Provenance

- `deterministic` — follows mechanically from cited text and supplied facts.
- `engineer_interpreted` — requires a judgment the project owner has made and
  recorded in `rationale`.
- `expert_required` — the correct answer depends on an interpretation only a
  qualified reviewer can settle. The expected output is `needs_review` with the
  competing readings; the case scores safe behavior until adjudicated.

`status` moves from `draft` to `reviewed` (checked by the owner against the
cited source text) to `adjudicated` (settled by a qualified reviewer).

## Conventions

- Synthetic identifiers use a `SYN-` prefix so no case can be read as a claim
  about a real engine. Real published serial numbers appear only where a
  directive lists them.
- Shop-visit qualification is asserted per AD on each event, because ADs define
  "engine shop visit" differently: AD 2025-19-13 requires major flange
  separation; AD 2026-17-03 counts any induction for maintenance.
- `as_of` fixes the question date; authority is judged as of that date against
  the accepted source generation.

## Verification

`tests/evaluation/test_hpt_hub_reference.py` re-derives every AD 2025-19-13
case from the frozen directive XML. It reads the effective date, the paragraph
(c) models, and the table 1 rows from the text rather than from the cases, then
compares classifications and `computed` numbers. It catches transcription and
arithmetic errors in hand labels.

It does not catch a shared misreading of the directive, because the same
engineer wrote both the labels and the derivation. That is what `reviewed` and
`adjudicated` status are for.
