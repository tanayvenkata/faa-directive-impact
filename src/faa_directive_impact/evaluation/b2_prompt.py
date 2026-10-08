"""The frozen B2 prompt: screen one engine against one directive from its text.

The instructions state the task contract only: the outcome vocabulary and
record conventions from ``evaluation/seed/README.md``, the supported scope,
and the answer format. They never contain a case's label, rationale, title,
forbidden claims, or an adjudication. A change to the instructions or the
answer schema changes ``PROMPT_VERSION``, and a run records it.
"""

import hashlib
import json
from datetime import date
from typing import Any

import yaml

from faa_directive_impact.directives.source_text import SourceDocument
from faa_directive_impact.impact.hpt_hub_rules import SUPPORTED_ENGINE_MODELS
from faa_directive_impact.llm.client import ModelRequest
from faa_directive_impact.schema_validation import load_schema

ANSWER_SCHEMA = load_schema("b2-screen-answer.schema.json")
# Version 1 (b73f8e333bee) took missing facts as plain strings and had no
# format rule for citation document numbers. Its runs are kept and are
# re-scored under the schema they were given.
ANSWER_SCHEMAS = {
    "b73f8e333bee": load_schema("b2-screen-answer-v1.schema.json"),
}

INSTRUCTIONS = f"""\
You screen one aircraft engine against one FAA airworthiness directive (AD).
You are given the directive's Federal Register text (with any related
proposal, correction, or superseding document published by the question
date) and the engine's maintenance record. Answer from the text and the record
only.

This is a screening aid, not a compliance determination. Never state or imply
that an engine or part is compliant or noncompliant, safe or airworthy, or
approved for return to service, and never word an answer as the operator's AD
status record.

## Supported scope

This screen supports only these IAE V2500 engine models:
{", ".join(sorted(SUPPORTED_ENGINE_MODELS))}.
For any other engine model, answer applicability "outside_supported_scope"
with action_status "none", and make no applicability determination.

## Outcome fields

applicability:
- "applies": the engine is within the directive's applicability.
- "does_not_apply": supplied facts place the engine outside the directive.
- "unknown": a fact needed to decide applicability is missing.
- "outside_supported_scope": not a supported model; no determination.

action_status (when the directive applies or applicability is unknown;
otherwise "none"):
- "action_required": supplied facts trigger a required action; say when.
- "action_required_on_event": action is required only when a future event
  occurs (for example a shop visit that exposes a part); no deadline otherwise.
- "no_action_triggered": no required action is triggered now; continuing
  obligations still bind.
- "needs_review": a required fact or interpretation is missing; name it.

"action_required" may still list missing facts when part of the obligation is
established and another part depends on a missing fact.

authority_state, on the question date: "proposed" (a proposed rule),
"published_not_yet_effective" (a final rule before its effective date), or
"in_force". Only an in-force directive can require action.

## Engine record conventions

- "unknown" means the value is not known. A missing or unknown record is
  never evidence that a part is absent or unaffected.
- ad_records and amoc_claims hold what the operator asserts: its recorded AD
  status and any alternative method of compliance it claims. They are claims
  to check, never evidence that settles an outcome.
- An event's qualifies_as_engine_shop_visit states, per AD, whether the
  operator's record says that event meets that AD's definition of an engine
  shop visit.
- Identifiers starting with "SYN-" are synthetic.

## Answer fields

- summary: one or two sentences stating the outcome and why.
- timing: when the required action is due, in words, or null.
- latest_engine_flight_cycles: the engine flight-cycle counter by which the
  required action must be done, when it can be computed; otherwise null.
- component_cycles_remaining: cycles remaining before the affected part
  reaches its listed limit (negative if already past), when it can be
  computed; otherwise null. With several affected parts, give the smallest.
- alternative_readings: if the text can be read more than one way and the
  readings give different deadlines, list each reading; otherwise empty.
- missing_facts: each fact needed but missing or unconfirmed, as an object.
  record_path is the path of the engine-record field that would settle it,
  exactly in one of the forms below and with no other text, or null when the
  fact is not part of the engine record. description says in words what is
  missing and why it matters. Path forms: <section>.<field> (sections are engine, operator,
  and so on), <section>.<field>[<date>] for a dated reading,
  installed_components[<component_name>] for a missing component record,
  installed_components[<component_name>].<field>,
  installed_components[<component_name>].<field>[<date>], and
  <list>[<AD number>] for an item in a record list that relates to a
  directive. A fact that is not part of the engine record (for example the
  content of a document or image you were not given) has record_path null.
- continuing_obligations: obligations that keep binding while the directive
  applies, each with its paragraph.
- matched_parts: each installed part you matched to a part the directive
  lists, with both the installed and the listed identifiers.
  listed_serial_number is null when the directive lists the part number only.
- citations: every document and paragraph your answer relies on, including
  for answers that clear an engine. document is the Federal Register
  document number only, exactly as shown after "Federal Register document"
  (for example 2025-18469), with no AD number or other text. paragraph is the
  paragraph label as written, such as "(c)", "(g)", or "(i)(2)"; use
  "preamble" for text before the regulatory paragraphs. Give a locator, such
  as a table row, when it helps; otherwise null.
- notes: anything a reviewer should know.
"""

PROMPT_VERSION = hashlib.sha256(
    (INSTRUCTIONS + json.dumps(ANSWER_SCHEMA, sort_keys=True)).encode("utf-8")
).hexdigest()[:12]
ANSWER_SCHEMAS[PROMPT_VERSION] = ANSWER_SCHEMA


def render_documents(documents: list[SourceDocument]) -> str:
    """The shared source text: each document with its identity and dates."""
    parts = []
    for document in documents:
        effective = (
            document.effective_date.isoformat() if document.effective_date else "none"
        )
        parts.append(
            f"===== Federal Register document {document.number} =====\n"
            f"Type: {document.document_type}\n"
            f"Published: {document.publication_date.isoformat()}\n"
            f"Effective date (from the Federal Register record): {effective}\n\n"
            f"{document.text}"
        )
    return "\n".join(parts)


def question(directive: str, as_of: date, asset: dict[str, Any]) -> str:
    record = yaml.safe_dump(asset, sort_keys=False, allow_unicode=True)
    return (
        f"Question date: {as_of.isoformat()}\n"
        f"Directive under question: Federal Register document {directive}\n\n"
        f"Engine record:\n{record}"
    )


def build_request(
    model: str,
    effort: str,
    directive: str,
    as_of: date,
    asset: dict[str, Any],
    documents: list[SourceDocument],
    max_tokens: int = 16000,
) -> ModelRequest:
    return ModelRequest(
        model=model,
        instructions=INSTRUCTIONS,
        document=render_documents(documents),
        question=question(directive, as_of, asset),
        output_schema=ANSWER_SCHEMA,
        effort=effort,
        max_tokens=max_tokens,
    )
