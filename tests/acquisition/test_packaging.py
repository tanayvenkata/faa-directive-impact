import hashlib
import json
import tarfile
from pathlib import Path

import httpx
import pytest
from source_fakes import document_pages, serve

from faa_directive_impact import cli
from faa_directive_impact.acquisition import retrieval
from faa_directive_impact.acquisition.packaging import package_generation


def run_acquisition(
    root: Path, capsys: pytest.CaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> str:
    pages = document_pages("2021-14268", images=("ER02JY21.000",))
    monkeypatch.setattr(
        cli,
        "build_client",
        lambda timeout: retrieval.build_client(
            timeout, transport=httpx.MockTransport(serve(pages))
        ),
    )
    cli.main(
        [
            "acquire",
            "2021-14268",
            "--storage-root",
            str(root),
            "--corpus-track",
            "frozen_evaluation",
        ]
    )
    manifest = json.loads(capsys.readouterr().out)["manifest"]
    return Path(manifest).stem.removeprefix("raw-generation-")


def test_archive_is_deterministic_and_matches_receipts(
    tmp_path: Path, capsys: pytest.CaptureFixture, monkeypatch: pytest.MonkeyPatch
) -> None:
    root = tmp_path / "store"
    generation = run_acquisition(root, capsys, monkeypatch)

    first = package_generation(root.resolve(), generation, tmp_path / "a")
    second = package_generation(root.resolve(), generation, tmp_path / "b")

    assert first.read_bytes() == second.read_bytes()
    with tarfile.open(first) as tar:
        names = tar.getnames()
        sums = tar.extractfile(f"{generation}/SHA256SUMS").read().decode()
        for line in sums.splitlines():
            digest, path = line.split("  ", 1)
            member = tar.extractfile(f"{generation}/{path}")
            assert hashlib.sha256(member.read()).hexdigest() == digest
    assert len(sums.splitlines()) == 7
    assert any(name.endswith("_original.png") for name in names)
