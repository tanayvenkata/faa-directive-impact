# Stand-In Proofread Brief

Frozen before the proofread starts (`PREREGISTRATION.md`, deviation 7). The
same brief goes to the proofreader for every directive. It is written from
the drafting prompt (prompt v2, `226de36424d1`) and the general gate list in
`evaluation/GATES.md`; it names no case, unit, score, or directive-specific
finding.

## Role

You proofread a rule record that a model drafted from one FAA airworthiness
directive. You stand in for the project owner, who would otherwise check the
draft against the text before anyone relies on it. A program screens engine
records against the reviewed record without reading the text, so a wrong
field can clear an engine that needs action.

## What you may read

For each directive, only:

- `draft.json`: the model's draft.
- `request.json`: the recorded request. Its instructions are the frozen
  drafting prompt, including the JSON Schema with each field's description;
  its document is the full text of every document in the directive's thread.
- `schema.json`: the same rule schema, on its own.

Do not open anything else in the repository. In particular, never read
`evaluation/coverage/cases/`, `evaluation/seed/`, `evaluation/runs/`,
`evaluation/coverage/reference/`, `evaluation/coverage/critique/`, the
write-ups, or `src/faa_directive_impact/rules/`. Do not run the screening
interpreter or any scorer. If you are unsure whether a file is allowed, it
is not.

## What to check, field by field, against the text

1. **Controlling text.** The final rule's regulatory text controls, and a
   correction's republished text controls where it differs. The preamble
   counts only where the regulatory text relies on it.
2. **Every identifier.** Each engine model, part number, and serial number
   is printed in the controlling text exactly as recorded. Nothing the text
   does not print.
3. **Applicability.** Models, part and serial groups, and exclusions match
   paragraph (c) and any applicability limits elsewhere in the regulatory
   text.
4. **Every citation.** Each document number is a document in the request,
   and each paragraph label exists in that document exactly as written. A
   citation to a paragraph that does not exist is an error, not a style
   point.
5. **Actions and timing.** Each action's trigger, threshold, limit, grace
   period, reference date, and unit (cycles, hours, days, calendar date)
   matches the text exactly. Arithmetic the record implies must come out
   exactly as the text states it.
6. **Material you do not have.** Where the text decides something by
   reference to material it does not print (a list in a service bulletin, a
   table printed only as an image), it is a dependency, and the groups,
   actions, and limits that need it point at it. A procedure the text only
   tells the operator to follow is not a dependency.
7. **Facts no engine record holds.** Conditions only the operator knows are
   named under the action's unrecorded conditions, not assumed either way.
8. **Credit, termination, and the thread.** Credit for earlier actions,
   terminating actions, and the replaced directive match the text.
9. **Ambiguities.** A real ambiguity stays listed and unresolved. Do not
   settle unclear wording by choosing a reading; do not list wording that
   the text actually settles.
10. **Completeness.** Nothing the regulatory text requires of an engine is
    missing.

Change a field only when the text shows the draft is wrong or incomplete.
Do not restyle, reorder, or rephrase fields that are correct. Do not add
requirements the text does not state. When in doubt, prefer the form that
sends an engine to a person over the form that clears it.

## What to write

For each directive:

- `reviewed.json`: the corrected record. It must still validate against the
  schema, and every identifier must be printed in the text. Run
  `validate.py` on it (it checks only the schema and the identifiers).
- `changes.md`: one line per changed field, in the form
  `- <JSON path>: <old> → <new>. Reason: <what the text says, with document
  and paragraph>.` If nothing changed, write `No changes.`

Each changed field counts once in `CHANGES.md`. The count of changed fields
stands in for proofreading time, which cannot be measured here.
