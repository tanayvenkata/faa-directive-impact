# Feasibility Seed

Twenty-five manually inspectable cases that establish the first failure
taxonomy. They are a feasibility seed, not a corpus limit or a release
threshold. Each case is one synthetic engine, one accepted source generation,
and the expected directive-impact outcome.

Cases live in `cases/seed-NNN.yaml` and are validated by the packaged
`seed-case.schema.json`. `make test` also checks every case against its source
generation.

## Outcome Fields

Each expected outcome separates whether a directive applies from whether it
requires action now. The FAA's own comment responses for AD 2025-19-13 show
why: its installation prohibition binds every listed engine model, so removing
or never having an affected hub "does not make the AD no longer applicable."

| `applicability` | Meaning |
|---|---|
| `applies` | The engine is within the directive's applicability |
| `does_not_apply` | Supplied facts place the engine outside the directive |
| `unknown` | A fact needed to decide applicability is missing |
| `outside_supported_scope` | Not a supported V2500 variant; no determination is made |

| `action_status` (when the directive applies or applicability is unknown) | Meaning |
|---|---|
| `action_required` | Supplied facts trigger a required action; `action_timing` says when |
| `action_required_on_event` | Action is required only when a future event occurs (for example a shop visit that exposes a part); no deadline otherwise |
| `no_action_triggered` | No required action is triggered now; `continuing_obligations` still bind |
| `needs_review` | A required fact or interpretation is missing; the missing item is named |

Review queues are derived: `action_required` → potentially affected;
`action_required_on_event` → potentially affected (conditional);
`needs_review` → needs review; `no_action_triggered` → no action currently
required; `does_not_apply` → not applicable; `outside_supported_scope` →
outside supported scope. The system never claims compliance, noncompliance,
maintenance adequacy, or return-to-service authority.

An omitted `authority_state` means `in_force`. `action_required` may still list
`required_missing_facts` when part of the obligation is established and another
part depends on a missing fact (seed-008, seed-017).

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

Critiques that fed changes are kept in `critique/` with a verification verdict
for each item.

Adjudications that settle an interpretation are recorded in `adjudication/`.
Each records its source, its date, and its informal or official status. A case
it settles carries `status: adjudicated` and the adjudication's `id`.
