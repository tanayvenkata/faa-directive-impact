"""Hostile Federal Register responses and hostile text on the freshness page.

Each bad search response must reject the candidate with a receipt, keep the
previous generation and checkpoint, log the failure, and show it on the page.
"""

import base64
import hashlib
import json
import re

import httpx
import pytest
from discovery_fakes import Harness, seed_corpus
from source_fakes import SEARCH_PATH, serve_search

from faa_directive_impact.acquisition.retrieval import build_client
from faa_directive_impact.discovery import search as search_module
from faa_directive_impact.discovery.site import (
    STALENESS_SCRIPT,
    STYLE,
    build_site,
)
from faa_directive_impact.discovery.state import (
    read_active,
    read_attempts,
    read_decisions,
)
from faa_directive_impact.discovery.sync import run_sync


def entry(**overrides):
    base = {
        "document_number": "2026-18800",
        "title": "Airworthiness Directives; Airbus SAS Airplanes",
        "type": "Rule",
        "action": "Final rule.",
        "publication_date": "2026-09-15",
        "effective_on": None,
        "docket_ids": ["Docket No. FAA-2026-0001", "AD 2026-19-01"],
        "correction_of": None,
        "corrections": [],
        "citation": "91 FR 1",
        "html_url": "https://www.federalregister.gov/documents/2026-18800",
    }
    base.update(overrides)
    return base


def page(results, count=None):
    return json.dumps(
        {"count": len(results) if count is None else count, "results": results}
    ).encode()


HOSTILE_SEARCH_BODIES = {
    "not_json": b"<html><body>Service Unavailable</body></html>",
    "truncated_json": page([entry()])[:-40],
    "empty_body": b"",
    "array_not_object": b"[]",
    "count_is_string": json.dumps({"count": "1", "results": [entry()]}).encode(),
    "count_is_boolean": json.dumps({"count": True, "results": [entry()]}).encode(),
    "count_is_negative": page([], count=-1),
    "count_disagrees": page([entry()], count=2),
    "results_not_a_list": json.dumps({"count": 1, "results": {"a": 1}}).encode(),
    "result_not_an_object": page(["2026-18800"]),
    "document_number_is_number": page([entry(document_number=202618800)]),
    "title_is_number": page([entry(title=7)]),
    "docket_ids_hold_numbers": page([entry(docket_ids=[39, 2026])]),
    "corrections_hold_objects": page([entry(corrections=[{"x": 1}])]),
    "publication_date_malformed": page([entry(publication_date="15/09/2026")]),
    "unknown_type": page([entry(type="Proposed Rule")]),
}


def sync_with_search_body(harness: Harness, body: bytes) -> dict:
    corpus = seed_corpus()
    serve = serve_search(corpus.entries, corpus.pages)

    def handler(request: httpx.Request) -> httpx.Response:
        if request.url.path == SEARCH_PATH:
            return httpx.Response(
                200, content=body, headers={"content-type": "application/json"}
            )
        return serve(request)

    with build_client(transport=httpx.MockTransport(handler)) as client:
        return run_sync(harness.root, client, clock=harness.clock)


def assert_rejected_and_kept(harness, first, attempt, tmp_path):
    assert attempt["outcome"] == "rejected", attempt
    assert attempt["failures"]
    active = read_active(harness.root)
    assert active["generation_id"] == first["generation_id"]
    assert active["checkpoint"] == "2026-09-12"
    decision = read_decisions(harness.root)[-1]
    assert decision["receipt_type"] == "rejection"
    assert decision["reasons"]
    assert read_attempts(harness.root)[-1]["outcome"] == "rejected"
    html = build_site(harness.root, tmp_path / "site").read_text()
    assert "did not succeed: rejected" in html
    assert "Failures in the last attempt" in html


@pytest.mark.parametrize("name", sorted(HOSTILE_SEARCH_BODIES))
def test_hostile_search_response_rejects_and_keeps_the_previous_generation(
    tmp_path, name
):
    harness = Harness(tmp_path / "discovery")
    first = harness.sync(seed_corpus())
    assert first["outcome"] == "promoted"

    attempt = sync_with_search_body(harness, HOSTILE_SEARCH_BODIES[name])

    assert_rejected_and_kept(harness, first, attempt, tmp_path)


def test_oversized_search_page_is_refused_while_it_downloads(tmp_path, monkeypatch):
    harness = Harness(tmp_path / "discovery")
    first = harness.sync(seed_corpus())
    monkeypatch.setattr(search_module, "MAX_PAGE_BYTES", 4096)
    huge = page([entry(title="Airworthiness Directives; " + "A" * 10_000)])

    attempt = sync_with_search_body(harness, huge)

    assert_rejected_and_kept(harness, first, attempt, tmp_path)
    assert any("exceeded 4096 bytes" in f for f in attempt["failures"])
    # The refused bytes are not kept.
    run_pages = harness.root / "raw" / "federal-register-search"
    run_pages = run_pages / attempt["acquisition_run_id"]
    assert not [path for path in run_pages.rglob("*") if path.is_file()]
    assert not [p for p in (harness.root / ".staging").rglob("*") if p.is_file()]


def test_the_live_search_page_cap_is_far_above_the_largest_page_seen():
    # Largest live page, from the discovery-state receipts (2026-10-15).
    assert search_module.MAX_PAGE_BYTES > 40 * 382_095


HOSTILE_TITLE = '<script>alert("x")</script><img src=x onerror=alert(1)>'


def test_html_in_directive_titles_is_escaped_and_bad_links_are_not_linked(
    tmp_path,
):
    harness = Harness(tmp_path / "discovery")
    corpus = seed_corpus()
    added = corpus.add(
        "2026-18800",
        "2026-09-15",
        f"Airworthiness Directives; {HOSTILE_TITLE}",
        ad_number="2026-19-01",
    )
    added["html_url"] = "javascript:alert(document.domain)"
    attempt = harness.sync(corpus)
    assert attempt["outcome"] == "promoted", attempt["failures"]

    html = build_site(harness.root, tmp_path / "site").read_text()

    assert HOSTILE_TITLE not in html
    assert "&lt;script&gt;alert(&quot;x&quot;)&lt;/script&gt;" in html
    assert "javascript:" not in html
    assert "<img" not in html
    # Only the page's own staleness script is present.
    assert len(re.findall(r"<script\b", html)) == 1
    # Federal Register links are still links.
    assert 'href="https://www.federalregister.gov/documents/2026-16954"' in html


def test_html_in_a_failure_message_is_escaped(tmp_path):
    harness = Harness(tmp_path / "discovery")
    harness.sync(seed_corpus())
    body = page([entry(document_number="<b>x</b>")])

    attempt = sync_with_search_body(harness, body)

    assert attempt["outcome"] == "rejected"
    html = build_site(harness.root, tmp_path / "site").read_text()
    assert "<b>x</b>" not in html
    assert "&lt;b&gt;x&lt;/b&gt;" in html


def csp_hash(text: str) -> str:
    digest = hashlib.sha256(text.encode()).digest()
    return f"'sha256-{base64.b64encode(digest).decode()}'"


def test_page_carries_a_content_security_policy_allowing_only_its_own_code(
    tmp_path,
):
    harness = Harness(tmp_path / "discovery")
    harness.sync(seed_corpus())

    html = build_site(harness.root, tmp_path / "site").read_text()

    [policy] = re.findall(
        r'<meta http-equiv="Content-Security-Policy" content="([^"]+)">', html
    )
    assert "default-src 'none'" in policy
    assert f"script-src {csp_hash(STALENESS_SCRIPT)}" in policy
    assert f"style-src {csp_hash(STYLE)}" in policy
    assert "unsafe-inline" not in policy
    # The hashes cover the exact text inside the page's elements.
    [script] = re.findall(r"<script>(.*?)</script>", html, re.S)
    [style] = re.findall(r"<style>(.*?)</style>", html, re.S)
    assert csp_hash(script) in policy and csp_hash(style) in policy
    assert html.index("Content-Security-Policy") < html.index("<style>")
