import re

import httpx
from discovery_fakes import Harness, seed_corpus

from faa_directive_impact import cli
from faa_directive_impact.acquisition.retrieval import build_client
from faa_directive_impact.discovery.site import build_site, latest_s1_queues
from faa_directive_impact.discovery.sync import run_sync


def failed_first_sync(harness: Harness) -> None:
    handler = lambda request: httpx.Response(503)  # noqa: E731
    with build_client(transport=httpx.MockTransport(handler)) as client:
        run_sync(harness.root, client, clock=harness.clock)


def test_page_embeds_last_success_and_a_browser_staleness_check(tmp_path):
    harness = Harness(tmp_path / "discovery")
    attempt = harness.sync(seed_corpus())

    page = build_site(harness.root, tmp_path / "site").read_text()

    stamp = attempt["finished_at_utc"]
    assert f'<time id="last-success" datetime="{stamp}">' in page
    assert re.search(r'<div id="stale-banner"[^>]*hidden', page)
    assert "hours > 48" in page and "STALE" in page
    # The script runs after the elements it reads have been parsed.
    assert page.index("<script>") > page.index('id="last-success"')
    assert "As of <time" in page
    assert attempt["generation_id"] in page
    assert "Screening tool, not a compliance determination" in page
    assert "Not yet evaluated: unverified candidate" in page
    assert "IAE NMSB V2500-ENG-72-0000" in page
    assert "not redistributed" in page
    assert "published on or after 2025-01-01" in page
    assert "Directives published earlier are not in this corpus" in page
    assert 'name="viewport"' in page
    assert "<img" not in page and "logo" not in page.lower()


def test_page_renders_a_failed_first_sync(tmp_path):
    harness = Harness(tmp_path / "discovery")
    failed_first_sync(harness)

    page = build_site(harness.root, tmp_path / "site").read_text()

    assert "No sync has succeeded yet" in page
    assert "did not succeed: rejected" in page
    assert "Failures in the last attempt" in page
    assert "search page 1 failed" in page


def test_page_shows_a_failure_after_a_success(tmp_path):
    harness = Harness(tmp_path / "discovery")
    first = harness.sync(seed_corpus())
    failed_first_sync(harness)

    page = build_site(harness.root, tmp_path / "site").read_text()

    assert "did not succeed: rejected" in page
    assert first["generation_id"] in page
    assert 'id="last-success"' in page


def test_page_renders_with_no_state_at_all(tmp_path):
    page = build_site(tmp_path / "empty", tmp_path / "site").read_text()

    assert "No sync has succeeded yet" in page


def test_s1_queues_are_linked_only_when_present(tmp_path):
    runs = tmp_path / "runs"
    assert latest_s1_queues(runs) is None
    (runs / "s1-20261006T000000Z-abc").mkdir(parents=True)
    (runs / "s1-20261006T000000Z-abc" / "queues.html").write_text("<p>queues</p>")

    site = tmp_path / "site"
    page = build_site(tmp_path / "empty", site, latest_s1_queues(runs)).read_text()

    assert 'href="s1-queues.html"' in page
    assert (site / "s1-queues.html").read_text() == "<p>queues</p>"


def test_cli_writes_the_site(tmp_path, capsys):
    code = cli.main(
        [
            "discovery-site",
            "--storage-root",
            str(tmp_path / "discovery"),
            "--output",
            str(tmp_path / "site"),
            "--runs-root",
            str(tmp_path / "runs"),
        ]
    )

    assert code == 0
    assert (tmp_path / "site" / "index.html").is_file()


def test_cli_refuses_a_frozen_storage_root(tmp_path, capsys):
    (tmp_path / "data" / "seed-frozen").mkdir(parents=True)

    code = cli.main(["discovery-rollback", "--storage-root", str(tmp_path / "data")])

    assert code == 1
    assert "refusing" in capsys.readouterr().out
