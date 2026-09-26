from pathlib import Path

import pytest

from faa_directive_impact.acquisition.storage import (
    STAGING_DIRECTORY,
    ArtifactExistsError,
    RawStorage,
    StoragePathError,
)


@pytest.mark.parametrize(
    "relative_path", ["../escape.json", "/etc/passwd", "raw/../../escape", ""]
)
def test_storage_rejects_paths_outside_root(tmp_path: Path, relative_path: str) -> None:
    with pytest.raises(StoragePathError):
        RawStorage(tmp_path).resolve(relative_path)


def test_publish_refuses_to_overwrite(tmp_path: Path) -> None:
    storage = RawStorage(tmp_path)
    storage.write_json("receipts/a.json", {"n": 1})

    with pytest.raises(ArtifactExistsError):
        storage.write_json("receipts/a.json", {"n": 2})

    assert (tmp_path / "receipts/a.json").read_text() == '{\n  "n": 1\n}\n'
    assert list((tmp_path / STAGING_DIRECTORY).iterdir()) == []


def test_exception_while_staging_leaves_nothing(tmp_path: Path) -> None:
    storage = RawStorage(tmp_path)

    with pytest.raises(RuntimeError):
        with storage.stage() as writer:
            writer.write(b"partial")
            raise RuntimeError("interrupted")

    assert list((tmp_path / STAGING_DIRECTORY).iterdir()) == []
