import re
from datetime import date
from pathlib import Path

import pytest

from faa_directive_impact.directives.hpt_hub_record import build_record
from faa_directive_impact.evaluation.seed import load_seed_cases
from faa_directive_impact.impact.hpt_hub_rules import screen
from faa_directive_impact.impact.queue_page import DISCLAIMER, render_page

REPO = Path(__file__).resolve().parents[2]
XML = REPO / "tests/fixtures/federal-register/2025-18469/full-text.xml"
GENERATION = REPO / "generations/gen-20260926T215105Z-7fe9da08"
FORBIDDEN_WORDS = re.compile(
    r"compliant|compliance|\bsafe\b|safety|airworth|return.to.service", re.I
)


@pytest.fixture(scope="module")
def page_and_items():
    record = build_record(XML.read_bytes(), GENERATION)
    items = []
    for case in load_seed_cases(REPO / "evaluation/seed/cases"):
        if not any(o["directive"] == "2025-18469" for o in case.record["expected"]):
            continue
        as_of = case.record["source_snapshot"]["as_of"]
        result = screen(
            record, case.record["asset_snapshot"], date.fromisoformat(as_of)
        )
        items.append(
            {
                "case": case.record["case_id"],
                "as_of": as_of,
                "engine": case.record["asset_snapshot"]["engine"],
                "screen": result.to_dict(),
            }
        )
    meta = {"run_id": "s1-test", "gate_version": 1, "commit": "abc1234"}
    return render_page(items, record, meta), items


def test_page_never_uses_compliance_or_safety_wording(page_and_items) -> None:
    page, _ = page_and_items
    without_disclaimer = page.replace(DISCLAIMER.replace("'", "&#x27;"), "")

    assert FORBIDDEN_WORDS.findall(without_disclaimer) == []


def test_page_states_it_is_a_screening_aid(page_and_items) -> None:
    page, _ = page_and_items

    assert "screening aid" in page
    assert "<title>Directive Screening Queues</title>" in page


def test_every_engine_appears_in_its_queue_section(page_and_items) -> None:
    page, items = page_and_items
    for item in items:
        queue = item["screen"]["queue"]
        section = re.search(
            rf'<section class="{queue}">(.*?)</section>', page, re.DOTALL
        )
        assert section is not None
        assert item["engine"]["engine_serial_number"] in section.group(1)


def test_page_is_self_contained(page_and_items) -> None:
    page, _ = page_and_items

    assert "<script" not in page
    assert not re.search(r'(src|href)="https?://', page)
