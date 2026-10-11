from datetime import UTC, date, datetime, timedelta
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

import httpx
import pytest
from source_fakes import search_entry, serve_search

from faa_directive_impact.acquisition.federal_register import (
    airworthiness_directive_numbers,
)
from faa_directive_impact.acquisition.retrieval import (
    AcquisitionContext,
    build_client,
    random_id,
)
from faa_directive_impact.acquisition.storage import RawStorage
from faa_directive_impact.discovery.search import (
    DISCOVERED_DOCUMENT_NUMBER,
    RESULT_WINDOW,
    SEARCH_FIELDS,
    search_directives,
    search_url,
)
from faa_directive_impact.schema_validation import validate_artifact_receipt


def context(root: Path, handler) -> AcquisitionContext:
    start = datetime(2026, 10, 1, tzinfo=UTC)
    ticks = iter(range(10_000))
    return AcquisitionContext(
        run_id="run-20261001T000000Z-00000000",
        storage=RawStorage(root),
        client=build_client(transport=httpx.MockTransport(handler)),
        clock=lambda: start + timedelta(seconds=next(ticks)),
        new_id=random_id,
    )


ENTRIES = [
    search_entry(f"2026-1000{i}", f"2026-09-0{i}", ad_number=f"2026-18-0{i}")
    for i in range(1, 6)
]


def test_search_url_uses_the_documented_parameters():
    query = dict(parse_qsl(urlsplit(search_url(date(2026, 9, 1), 2)).query))
    pairs = parse_qsl(urlsplit(search_url(date(2026, 9, 1), 2)).query)

    assert query["conditions[agencies][]"] == "federal-aviation-administration"
    assert query["conditions[type][]"] == "RULE"
    assert query["conditions[cfr][title]"] == "14"
    assert query["conditions[cfr][part]"] == "39"
    assert query["conditions[publication_date][gte]"] == "2026-09-01"
    assert query["order"] == "oldest"
    assert query["per_page"] == "1000" and query["page"] == "2"
    assert [v for k, v in pairs if k == "fields[]"] == list(SEARCH_FIELDS)


def test_pages_are_fetched_by_number_and_kept_with_receipts(tmp_path):
    outcome = search_directives(
        context(tmp_path, serve_search(ENTRIES)), date(2026, 9, 2), per_page=2
    )

    assert outcome.complete
    assert [e["document_number"] for e in outcome.entries] == [
        "2026-10002",
        "2026-10003",
        "2026-10004",
        "2026-10005",
    ]
    assert len(outcome.receipts) == 2
    for receipt in outcome.receipts:
        validate_artifact_receipt(receipt)
        assert receipt["schema_version"] == "1.1.0"
        assert receipt["representation_role"] == "search_results"
        assert (tmp_path / receipt["artifact"]["relative_path"]).is_file()
    assert outcome.entry_receipts["2026-10005"] == outcome.receipts[1]["receipt_id"]


def test_checkpoint_date_is_inclusive(tmp_path):
    outcome = search_directives(
        context(tmp_path, serve_search(ENTRIES)), date(2026, 9, 5)
    )

    assert [e["document_number"] for e in outcome.entries] == ["2026-10005"]


def test_empty_search_is_complete(tmp_path):
    outcome = search_directives(
        context(tmp_path, serve_search(ENTRIES)), date(2026, 10, 1)
    )

    assert outcome.complete and outcome.entries == [] and outcome.count == 0


def test_a_repeated_page_is_a_problem_not_a_silent_dedupe(tmp_path):
    def always_page_one(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"count": 4, "results": ENTRIES[:2]})

    outcome = search_directives(
        context(tmp_path, always_page_one), date(2026, 9, 1), per_page=2
    )

    assert not outcome.complete
    assert any("appeared twice" in problem for problem in outcome.problems)


def test_count_at_the_result_cap_fails_loudly(tmp_path):
    def capped(request: httpx.Request) -> httpx.Response:
        return httpx.Response(200, json={"count": RESULT_WINDOW, "results": ENTRIES})

    outcome = search_directives(context(tmp_path, capped), date(2020, 1, 1))

    assert not outcome.complete
    assert "cap" in outcome.problems[0]


def test_failed_page_is_a_problem(tmp_path):
    outcome = search_directives(
        context(tmp_path, lambda request: httpx.Response(503)), date(2026, 9, 1)
    )

    assert not outcome.complete
    assert outcome.receipts[0]["acquisition_status"] == "failed"


@pytest.mark.parametrize("body", [{"results": []}, [], {"count": "3"}])
def test_malformed_page_is_a_problem(tmp_path, body):
    outcome = search_directives(
        context(tmp_path, lambda request: httpx.Response(200, json=body)),
        date(2026, 9, 1),
    )

    assert not outcome.complete


@pytest.mark.parametrize(
    "number",
    [
        "2025-18469",
        "93-31908",
        "94-21",
        "00-6",
        "E6-11333",
        "E7-39",
        "2010-103",
        "2011-51",
        "C1-2010-14979",
        "R1-2025-04334",
    ],
)
def test_every_historical_document_number_form_is_accepted(number):
    assert DISCOVERED_DOCUMENT_NUMBER.fullmatch(number)


@pytest.mark.parametrize("number", ["2025-1846x", "2025", "AD-2025-19-13"])
def test_malformed_document_numbers_are_rejected(number):
    assert not DISCOVERED_DOCUMENT_NUMBER.fullmatch(number)


def test_two_digit_year_ad_numbers_are_read():
    entry = {"docket_ids": ["AD 93-25-17", "Docket No. 93-NM-68-AD"]}
    assert airworthiness_directive_numbers(entry) == {"93-25-17"}
