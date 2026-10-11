"""Search the Federal Register for FAA airworthiness directives since a date.

The query and its parameter names come from the Federal Register API's
OpenAPI description (``data/open_api_v3.yml`` in
usnationalarchives/federalregister-api-core, the source of
https://www.federalregister.gov/developers/documentation/api/v1):

- ``conditions[agencies][]=federal-aviation-administration``
- ``conditions[type][]=RULE`` (final rules; corrections are also typed Rule)
- ``conditions[cfr][title]=14`` and ``conditions[cfr][part]=39``: documents
  affecting 14 CFR part 39, the airworthiness-directive part
- ``conditions[publication_date][gte]``: published on or after a date
- ``order=oldest``: publication date, then document number, ascending
- ``per_page`` (1000 maximum) and ``page``
- ``fields[]``: the document attributes to return

The search code behind the API resets to page 1 when ``page * per_page``
exceeds 10,000, caps ``total_pages`` at 50, and reports at most 10,000 for
``count``. Pages are therefore requested by number, never by following the
response's ``next_page_url``, and a search fails loudly when it could be
truncated or when the collected documents disagree with ``count``.

Each page's exact bytes are kept with a receipt like any other acquisition.
"""

import json
import math
import re
from dataclasses import dataclass, field
from datetime import date
from typing import Any
from urllib.parse import urlencode

from faa_directive_impact.acquisition.federal_register import (
    API_BASE_URL,
    TEXT_REDISTRIBUTION,
)
from faa_directive_impact.acquisition.retrieval import (
    SEARCH_RESULTS_ROLE,
    AcquisitionContext,
    RepresentationRequest,
    retrieve,
)

SEARCH_NAMESPACE = "federal_register_search_query"
# Besides numbers like 2025-18469, the search returns documents the Federal
# Register itself corrected or republished, numbered like C1-2025-03880 and
# R1-2025-04334; their ``correction_of`` names the original document.
DISCOVERED_DOCUMENT_NUMBER = re.compile(r"^(?:[A-Z]\d+-)?\d{4}-\d{5}$")
PER_PAGE = 1000
RESULT_WINDOW = 10_000
# The attributes each search result carries. Every name was checked against a
# live response; an unknown name makes the API answer HTTP 400.
SEARCH_FIELDS = (
    "document_number",
    "title",
    "type",
    "action",
    "publication_date",
    "effective_on",
    "docket_ids",
    "correction_of",
    "corrections",
    "citation",
    "html_url",
)


@dataclass
class SearchOutcome:
    """Every result collected, the receipts that hold them, and any problems."""

    since: date
    entries: list[dict[str, Any]] = field(default_factory=list)
    entry_receipts: dict[str, str] = field(default_factory=dict)
    receipts: list[dict[str, Any]] = field(default_factory=list)
    count: int | None = None
    problems: list[str] = field(default_factory=list)

    @property
    def complete(self) -> bool:
        return not self.problems


def search_url(since: date, page: int, per_page: int = PER_PAGE) -> str:
    """Return the search URL for one page; parameter order is fixed."""
    parameters: list[tuple[str, str | int]] = [
        ("conditions[agencies][]", "federal-aviation-administration"),
        ("conditions[type][]", "RULE"),
        ("conditions[cfr][title]", 14),
        ("conditions[cfr][part]", 39),
        ("conditions[publication_date][gte]", since.isoformat()),
        ("order", "oldest"),
        ("per_page", per_page),
        ("page", page),
    ]
    parameters.extend(("fields[]", name) for name in SEARCH_FIELDS)
    return f"{API_BASE_URL}/documents.json?{urlencode(parameters)}"


def search_request(
    since: date, page: int, run_id: str, per_page: int = PER_PAGE
) -> RepresentationRequest:
    """Request one search page, kept under ``raw/federal-register-search/``."""
    return RepresentationRequest(
        source_system="federal_register",
        identity_namespace=SEARCH_NAMESPACE,
        identity_value=f"faa-14cfr39-rules-since-{since.isoformat()}-page-{page}",
        representation_role=SEARCH_RESULTS_ROLE,
        authority_role="discovery_metadata",
        url=search_url(since, page, per_page),
        relative_path=f"raw/federal-register-search/{run_id}/page-{page:04d}.json",
        redistribution_status=TEXT_REDISTRIBUTION[0],
        redistribution_basis=TEXT_REDISTRIBUTION[1],
    )


def search_directives(
    context: AcquisitionContext, since: date, per_page: int = PER_PAGE
) -> SearchOutcome:
    """Fetch every page of the search and collect each document once.

    The checkpoint date is inclusive, so documents published on it are
    returned again; the caller deduplicates them against its corpus. Within
    one search a repeated document number means the pages overlapped, which
    is reported as a problem rather than silently dropped.
    """
    outcome = SearchOutcome(since)
    seen: set[str] = set()
    page = 1
    expected_pages = 1
    while page <= expected_pages:
        if page * per_page > RESULT_WINDOW:
            outcome.problems.append(
                f"page {page} lies beyond the API's {RESULT_WINDOW}-result window"
            )
            break
        request = search_request(since, page, context.run_id, per_page)
        receipt = retrieve(context, request)
        outcome.receipts.append(receipt)
        if receipt["acquisition_status"] != "succeeded":
            failure = receipt["failure"]
            outcome.problems.append(
                f"search page {page} failed: {failure['reason_code']} "
                f"({failure['detail']})"
            )
            break
        body = _read_page(context, receipt, outcome, page)
        if body is None:
            break
        count = body["count"]
        if outcome.count is None:
            outcome.count = count
            if count >= RESULT_WINDOW:
                outcome.problems.append(
                    f"search matched {count} documents, at or above the API's "
                    f"{RESULT_WINDOW}-result cap; move the checkpoint forward"
                )
                break
            expected_pages = max(1, math.ceil(count / per_page))
        elif count != outcome.count:
            outcome.problems.append(
                f"count changed during paging: {outcome.count} then {count}"
            )
            break
        for entry in body.get("results") or []:
            number = entry.get("document_number") if isinstance(entry, dict) else None
            if not isinstance(number, str) or not DISCOVERED_DOCUMENT_NUMBER.fullmatch(
                number
            ):
                outcome.problems.append(
                    f"search page {page} has a result without a valid document "
                    f"number: {str(entry)[:200]}"
                )
                continue
            if number in seen:
                outcome.problems.append(
                    f"{number} appeared twice in one search; pages overlapped"
                )
                continue
            seen.add(number)
            outcome.entries.append(entry)
            outcome.entry_receipts[number] = receipt["receipt_id"]
        page += 1

    if not outcome.problems and outcome.count is not None:
        if len(outcome.entries) != outcome.count:
            outcome.problems.append(
                f"collected {len(outcome.entries)} documents but the search "
                f"reported {outcome.count}"
            )
    return outcome


def _read_page(
    context: AcquisitionContext,
    receipt: dict[str, Any],
    outcome: SearchOutcome,
    page: int,
) -> dict[str, Any] | None:
    path = context.storage.root / receipt["artifact"]["relative_path"]
    try:
        body = json.loads(path.read_bytes())
    except (OSError, ValueError) as error:
        outcome.problems.append(f"search page {page} is not readable JSON: {error}")
        return None
    if (
        not isinstance(body, dict)
        or not isinstance(body.get("count"), int)
        or not isinstance(body.get("results", []), list)
    ):
        outcome.problems.append(
            f"search page {page} lacks an integer count or a results list"
        )
        return None
    return body
