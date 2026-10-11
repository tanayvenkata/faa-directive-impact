"""A fake discovery corpus and a harness that syncs it offline."""

from datetime import UTC, date, datetime, timedelta
from pathlib import Path

import httpx
from source_fakes import document_pages, search_entry, serve_search

from faa_directive_impact.acquisition.retrieval import build_client
from faa_directive_impact.discovery.state import read_generation
from faa_directive_impact.discovery.sync import run_sync

IAE = "Airworthiness Directives; International Aero Engines AG Engines"
IAE_LLC = "Airworthiness Directives; International Aero Engines, LLC Engines"
FAMILY = (
    "This AD applies to International Aero Engines AG (IAE AG) Model V2522-A5, "
    "V2524-A5, V2525-D5, V2527-A5, and V2533-A5 engines."
)
LLC = "This AD applies to IAE LLC Model PW1127G-JM and PW1133G-JM engines."


class Corpus:
    """Search entries plus the full representations of the IAE directives."""

    def __init__(self) -> None:
        self.entries: list[dict] = []
        self.pages: dict[str, bytes | None] = {}

    def add(
        self,
        number: str,
        published: str,
        title: str = "Airworthiness Directives; Airbus SAS Airplanes",
        ad_number: str | None = None,
        applicability: str | None = None,
        action: str = "Final rule.",
        docket: str = "Docket No. FAA-2026-0001",
        incorporated: tuple[str, ...] = (),
    ) -> dict:
        entry = search_entry(number, published, title, ad_number, action, docket)
        self.entries.append(entry)
        if "International Aero Engines" in title:
            self.pages.update(
                document_pages(
                    number,
                    publication_date=published,
                    docket_ids=tuple(entry["docket_ids"]),
                    action=action,
                    title=title,
                    applicability=applicability,
                    incorporated=incorporated,
                )
            )
        return entry


class Harness:
    def __init__(self, root: Path) -> None:
        self.root = root
        self.start = datetime(2026, 10, 1, tzinfo=UTC)
        self.ticks = 0

    def clock(self) -> datetime:
        self.ticks += 1
        return self.start + timedelta(seconds=self.ticks)

    def sync(self, corpus: Corpus, **options) -> dict:
        handler = serve_search(corpus.entries, corpus.pages)
        with build_client(transport=httpx.MockTransport(handler)) as client:
            return run_sync(
                self.root,
                client,
                start_date=date(2025, 1, 1),
                clock=self.clock,
                **options,
            )

    def generation(self, attempt: dict) -> dict:
        return read_generation(self.root, attempt["generation_id"])

    def records(self, generation: dict) -> dict[str, dict]:
        return {r["document_number"]: r for r in generation["records"]}


def seed_corpus() -> Corpus:
    corpus = Corpus()
    corpus.add(
        "2025-18469",
        "2025-09-24",
        IAE,
        "2025-19-13",
        FAMILY,
        docket="Docket No. FAA-2025-0926",
        incorporated=("IAE NMSB V2500-ENG-72-0000, dated 2025.",),
    )
    corpus.add(
        "2026-16954",
        "2026-08-20",
        IAE,
        "2026-17-03",
        FAMILY,
        docket="Docket No. FAA-2025-2555",
    )
    corpus.add(
        "2026-18423",
        "2026-09-10",
        f"{IAE}; Correction",
        "2026-17-03",
        FAMILY,
        action="Final rule; correction.",
        docket="Docket No. FAA-2025-2555",
    )
    corpus.add("2026-18500", "2026-09-10", IAE_LLC, "2026-18-10", LLC)
    corpus.add("2026-18600", "2026-09-12", ad_number="2026-18-20")
    return corpus
