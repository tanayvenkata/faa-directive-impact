"""Prompt v2: draft a directive's rule record in the v2 schema.

Used for full V2500 coverage (``evaluation/coverage/PREREGISTRATION.md``,
"Rules"). Like B3's prompt, it describes only the schema and how to read the
text. It never contains a coverage or seed case, a label, a reference rule
record, an ambiguity the project has found, or an adjudication, and the
schema's field descriptions were checked for case-specific wording before it
was frozen. A change to the instructions or the schema changes
``PROMPT_VERSION``, and a run records it.
"""

import hashlib
import json

from faa_directive_impact.directives.source_text import SourceDocument
from faa_directive_impact.evaluation.b2_prompt import render_documents
from faa_directive_impact.llm.client import ModelRequest
from faa_directive_impact.schema_validation import load_schema

RULE_SCHEMA = load_schema("rule-record-v2.schema.json")

INSTRUCTIONS = """\
You draft the rule record for one FAA airworthiness directive (AD) from its
Federal Register text. You are given every document in the directive's
thread: the proposed rule, the final rule, any correction, and any earlier
AD it replaces. A program will screen engine records against your rule
record without reading the text, and a person will proofread it against the
text before anyone relies on it.

Extract only what the text states. Do not add requirements, fill gaps with
assumptions, or settle unclear wording silently: report it under
ambiguities. A program that cannot tell sends the engine to a person, which
is safe; a record that guesses can clear an engine that needs action, which
is not.

## Which text controls

The final rule's regulatory text controls, not the proposal or the
discussion. If a correction republishes the regulatory text, the
correction's text controls wherever it differs; governing_document is the
document whose regulatory text controls, with the reason. List each
corrected paragraph under corrections. Use the preamble only where the
regulatory text relies on it, and say so under preamble_basis.

## Documents, paragraphs, and identifiers

- A document field holds the Federal Register document number only.
- A paragraph field holds the paragraph label exactly as written in the
  governing document, such as "(c)", "(g)(2)", or "(h)(1)(i)". Where a
  paragraph field does not apply, give an empty string.
- Copy every engine model, part number, and serial number exactly as the
  text prints it. Never write an identifier the text does not print: a
  program rejects any record that contains one.

## Material you do not have

When the text decides something by reference to material it does not
print (a serial-number list or compliance-time table in a service bulletin
or other incorporated document, or a table printed only as an image), do
not guess its contents. Record the material under dependencies, and point
the part groups, actions, and limits that need it at that dependency. A
procedure the text only tells the operator to follow is not a dependency
unless it decides whether or when an action applies.

## Facts no engine record holds

When an action turns on a fact that engine records do not hold (a part's
operating history, a condition only the operator knows), name it under the
action's unrecorded_conditions instead of assuming it either way.

## Answer format

Reply with one JSON object that validates against the JSON Schema below,
and nothing else. Follow each field's description in the schema; it says
what the field means and how the program reads it. Fill every required
field; use empty lists and empty strings where the directive has nothing for
a field.

## JSON Schema
"""

PROMPT = INSTRUCTIONS + json.dumps(RULE_SCHEMA, indent=1) + "\n"
PROMPT_VERSION = hashlib.sha256(PROMPT.encode("utf-8")).hexdigest()[:12]


def question(directive: str) -> str:
    return (
        "Draft the rule record for the airworthiness directive published as "
        f"Federal Register document {directive}."
    )


def build_request(
    model: str,
    effort: str,
    directive: str,
    documents: list[SourceDocument],
    max_tokens: int = 64000,
) -> ModelRequest:
    return ModelRequest(
        model=model,
        instructions=PROMPT,
        document=render_documents(documents),
        question=question(directive),
        output_schema=RULE_SCHEMA,
        effort=effort,
        max_tokens=max_tokens,
        constrained=False,
    )
