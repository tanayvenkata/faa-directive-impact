"""The frozen B3 prompt: draft a directive's rule record from its text.

The model reads a directive thread (proposal, final rule, corrections) and
fills the shared rule-record schema, citing the paragraph behind each value.
The instructions describe the schema and the interpreter's fixed vocabulary
only. They never contain a seed case, a label, a reference rule record, an
ambiguity the project has found, or an adjudication. A change to the
instructions or the schema changes ``PROMPT_VERSION``, and a run records it.
"""

import hashlib
import json

from faa_directive_impact.directives.source_text import SourceDocument
from faa_directive_impact.evaluation.b2_prompt import render_documents
from faa_directive_impact.llm.client import ModelRequest
from faa_directive_impact.schema_validation import load_schema

RULE_SCHEMA = load_schema("b3-rule-record.schema.json")

INSTRUCTIONS = """\
You draft the rule record for one FAA airworthiness directive (AD) from its
Federal Register text. You are given every document in the directive's
thread: the proposed rule, the final rule, and any correction. A program
will screen engine records against your rule record without reading the
text, and a person will proofread it against the text before anyone relies
on it. Extract only what the text states. Do not add requirements, fill gaps
with assumptions, or resolve unclear wording silently: report it under
ambiguities.

## Which text controls

The final rule's regulatory text controls, not the proposal. If a correction
republishes the regulatory text, the correction's text controls wherever it
differs. governing_document is the document whose regulatory text controls
(the final rule, or the latest correction that republishes it), with the
reason. List under corrections each paragraph a correction changed, quoting
the original and corrected wording.

## Sources

Every source names the Federal Register document number only (for example
2025-18469) and the paragraph label exactly as written, such as "(c)", "(g)",
or "(h)(1)(i)". Cite paragraphs in governing_document. locator is a short
pointer within the paragraph, such as a table name, or null.

## Fields

- ad_number: as "AD yyyy-nn-nn". final_rule_document: the final rule's
  document number.
- effective_date: the date the AD takes effect, as YYYY-MM-DD.
- applicability.engine_models: every engine model the applicability
  paragraph lists, written exactly as the text writes it.
- applicability.part_condition: if the applicability paragraph covers only
  engines with certain parts installed, the component and those part
  numbers; otherwise null. A parts list that appears only in a required
  action, not in the applicability paragraph, is not a part condition.
- affected_parts: each row of a list or table of specific parts that a
  required action acts on, with its component name exactly as the text
  writes it, part number, serial number (null if the text lists the part
  number only), and removal limit in cycles since new (null if none).
- eligible_parts: each definition of a part eligible for installation that
  names part numbers, with those part numbers. If the definition names no
  part numbers, give an empty list and describe it.
- required_actions: each required action, one per paragraph.
  - applies_to: "listed_parts" if it acts on the parts in affected_parts;
    "part_condition_parts" if it acts on the parts named in the part
    condition; "engine" if it acts on the engine as a whole; otherwise
    "other".
  - trigger: "next_shop_visit_after_effective_date" if it is due at the next
    engine shop visit after the effective date;
    "next_shop_visit_after_effective_date_with_condition" if it is due at the
    next such shop visit at which a further stated condition occurs;
    "compliance_time_only" if it is due within stated compliance times with
    no shop visit trigger; otherwise "other".
  - shop_visit_definition_paragraph: the paragraph that defines an engine
    shop visit, or null.
  - condition: for a conditional trigger, the condition in words and the
    paragraph that defines it (or null if none does); otherwise null.
  - limits: each compliance limit. "listed_part_cycles_since_new" means the
    per-part limit given in affected_parts (value null);
    "flight_cycles_after_effective_date" and "days_after_effective_date"
    carry their number in value; anything else is "other".
  - combination: how the trigger and the limits combine: "single" if there
    is one; "whichever_occurs_later" or "whichever_occurs_first" as the text
    states; "unclear" if the text does not settle it.
- installation_prohibitions: each paragraph that prohibits installing
  parts, and which parts.
- definitions: each defined term and its paragraph.
- amoc_paragraph: the paragraph on alternative methods of compliance, or null.
- ambiguities: each place where the controlling text can reasonably be read
  more than one way in a way that could change whether or when an action is
  required. Give the paragraph, what is unclear, and each reading. Leave it
  empty if there is none; do not invent one.
- notes: anything a proofreader should know.
"""

PROMPT_VERSION = hashlib.sha256(
    (INSTRUCTIONS + json.dumps(RULE_SCHEMA, sort_keys=True)).encode("utf-8")
).hexdigest()[:12]


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
    max_tokens: int = 32000,
) -> ModelRequest:
    return ModelRequest(
        model=model,
        instructions=INSTRUCTIONS,
        document=render_documents(documents),
        question=question(directive),
        output_schema=RULE_SCHEMA,
        effort=effort,
        max_tokens=max_tokens,
    )
