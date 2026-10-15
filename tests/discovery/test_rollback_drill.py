"""The rollback drill, offline: roll back, check the page, restore, check again.

This mirrors operations/drills/rollback_drill.sh, which runs the same steps
on a local copy of the live discovery state.
"""

from discovery_fakes import Harness, seed_corpus

from faa_directive_impact.discovery.site import build_site
from faa_directive_impact.discovery.state import read_active, read_decisions
from faa_directive_impact.discovery.sync import rollback


def active_row(html: str) -> str:
    start = html.index("<dt>Active generation</dt>")
    return html[start : html.index("</dd>", start)]


def test_rollback_then_restore_by_id_returns_the_page_and_the_next_sync(tmp_path):
    harness = Harness(tmp_path / "discovery")
    corpus = seed_corpus()
    first = harness.sync(corpus)
    corpus.add("2026-18800", "2026-09-15", ad_number="2026-19-01")
    second = harness.sync(corpus)
    assert second["outcome"] == "promoted", second["failures"]
    before = build_site(harness.root, tmp_path / "before").read_text()
    assert second["generation_id"] in active_row(before)

    rolled = rollback(harness.root, clock=harness.clock)

    assert rolled["generation_id"] == first["generation_id"]
    assert rolled["checkpoint"] == "2026-09-12"
    page = build_site(harness.root, tmp_path / "rolled").read_text()
    assert first["generation_id"] in active_row(page)
    assert "<dt>Activated by</dt><dd>rollback at" in page
    assert "New in the active generation (5)" in page

    restored = rollback(
        harness.root, to_generation=second["generation_id"], clock=harness.clock
    )

    assert restored["generation_id"] == second["generation_id"]
    assert restored["previous_generation_id"] == first["generation_id"]
    assert read_active(harness.root)["checkpoint"] == "2026-09-15"
    page = build_site(harness.root, tmp_path / "restored").read_text()
    assert second["generation_id"] in active_row(page)
    assert "New in the active generation (1)" in page
    kinds = [d["receipt_type"] for d in read_decisions(harness.root)]
    assert kinds == ["promotion", "promotion", "rollback", "rollback"]

    # The restored generation is a working base: the same responses change
    # nothing.
    again = harness.sync(corpus)

    assert again["outcome"] == "no_change", again["failures"]
    assert read_active(harness.root)["generation_id"] == second["generation_id"]


def test_the_page_says_which_receipt_activated_the_generation(tmp_path):
    harness = Harness(tmp_path / "discovery")
    attempt = harness.sync(seed_corpus())

    page = build_site(harness.root, tmp_path / "site").read_text()

    assert "<dt>Activated by</dt><dd>promotion at" in page
    assert attempt["decision_receipt_id"] in page
