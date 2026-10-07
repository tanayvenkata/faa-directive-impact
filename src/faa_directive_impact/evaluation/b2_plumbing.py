"""Plumbing check for B2: two calls on a synthetic engine that is in no case.

It confirms the API accepts the answer schema, the answer parses and
validates, and the second call reads the shared document from the prompt
cache. It checks format only; nothing here is scored, and the engine is
invented so no seed case is seen before the prompt is frozen.
"""

from datetime import date
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator

from faa_directive_impact.directives.source_text import documents_for, load_generation
from faa_directive_impact.evaluation.b2_prompt import ANSWER_SCHEMA, build_request
from faa_directive_impact.evaluation.s1_run import GENERATION_ID
from faa_directive_impact.llm.client import LiveModel, record

DIRECTIVE = "2025-18469"
AS_OF = date(2026, 6, 1)


def synthetic_engine(serial: str) -> dict[str, Any]:
    return {
        "synthetic": True,
        "engine": {
            "asset_id": f"SYN-PLUMB-{serial}",
            "engine_serial_number": f"SYN-PLUMB-{serial}",
            "engine_model": "V2524-A5",
            "snapshot_at": AS_OF.isoformat(),
        },
        "installed_components": [
            {
                "component_name": "HPT 1st-stage hub",
                "part_number": "2A5001",
                "serial_number": f"SYN-PLUMB-HUB1-{serial}",
                "cycles_since_new": 1200,
            },
            {
                "component_name": "HPT 2nd-stage hub",
                "part_number": "2A4802",
                "serial_number": f"SYN-PLUMB-HUB2-{serial}",
                "cycles_since_new": 1200,
            },
        ],
        "events": [],
    }


def run_plumbing(
    repo: Path, storage_root: Path, directory: Path, model: str, effort: str
) -> list[dict[str, Any]]:
    documents, relationships = load_generation(
        repo / "generations" / GENERATION_ID, storage_root
    )
    given = documents_for(DIRECTIVE, AS_OF, documents, relationships)
    live = LiveModel()
    validator = Draft202012Validator(ANSWER_SCHEMA)
    results = []
    for serial in ("A", "B"):
        request = build_request(
            model, effort, DIRECTIVE, AS_OF, synthetic_engine(serial), given
        )
        response = live.call(request)
        record(directory / "calls", request, response)
        schema_errors = (
            [error.message for error in validator.iter_errors(response.answer)]
            if response.answer is not None
            else ["no answer"]
        )
        results.append(
            {
                "engine": serial,
                "error": response.error,
                "schema_errors": schema_errors,
                "applicability": (response.answer or {}).get("applicability"),
                "action_status": (response.answer or {}).get("action_status"),
                "usage": response.usage,
                "cost_usd": response.cost_usd,
            }
        )
    return results
