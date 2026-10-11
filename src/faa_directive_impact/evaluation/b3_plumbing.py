"""Plumbing check for B3: draft one rule record for a directive B3 does not score.

AD 2025-17-16 (Federal Register 2025-17066) has no B3 unit, so drafting it
shows nothing about the scored directives before the prompt is frozen. The
check confirms the API accepts the rule schema, the record parses and
validates, sources name document numbers only, and the interpreter accepts
the record on an invented engine. It checks format only; nothing is scored.
"""

import re
from datetime import date
from pathlib import Path
from typing import Any

from faa_directive_impact.directives.source_text import documents_for, load_generation
from faa_directive_impact.evaluation.b3_prompt import build_request
from faa_directive_impact.evaluation.b3_run import valid_draft
from faa_directive_impact.evaluation.s1_run import GENERATION_ID
from faa_directive_impact.llm.client import LiveModel, record
from faa_directive_impact.rules.interpreter import screen_rules

DIRECTIVE = "2025-17066"
AS_OF = date(2026, 10, 6)
DOCUMENT_NUMBER = re.compile(r"^\d{4}-\d{5}$")
ENGINE = {
    "synthetic": True,
    "engine": {
        "asset_id": "SYN-PLUMB-B3",
        "engine_serial_number": "SYN-PLUMB-B3",
        "engine_model": "V2527-A5",
        "snapshot_at": AS_OF.isoformat(),
    },
    "installed_components": [],
    "events": [],
}


def run_plumbing(
    repo: Path, storage_root: Path, directory: Path, model: str, effort: str
) -> dict[str, Any]:
    documents, relationships = load_generation(
        repo / "generations" / GENERATION_ID, storage_root
    )
    given = documents_for(DIRECTIVE, AS_OF, documents, relationships)
    request = build_request(model, effort, DIRECTIVE, given)
    response = LiveModel().call(request)
    record(directory, request, response)

    draft = valid_draft(response)
    problems = []
    if draft is None:
        problems.append(f"no valid record (stop reason {response.stop_reason})")
    else:
        sources = _sources(draft)
        bad = sorted({s for s in sources if not DOCUMENT_NUMBER.match(s)})
        if bad:
            problems.append(f"source documents not in number form: {bad}")
        try:
            screen_rules(draft, ENGINE, AS_OF)
        except (KeyError, TypeError, ValueError) as error:
            problems.append(f"interpreter rejected the record: {error!r}")
    return {
        "directive": DIRECTIVE,
        "documents": [d.number for d in given],
        "stop_reason": response.stop_reason,
        "cost_usd": response.cost_usd,
        "problems": problems,
    }


def _sources(value: Any) -> list[str]:
    found = []
    if isinstance(value, dict):
        if set(value) >= {"document", "paragraph"}:
            found.append(value["document"])
        for item in value.values():
            found.extend(_sources(item))
    elif isinstance(value, list):
        for item in value:
            found.extend(_sources(item))
    return found
