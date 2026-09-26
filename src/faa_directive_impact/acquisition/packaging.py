"""Package an accepted generation's raw bytes as a deterministic archive."""

import gzip
import io
import json
import tarfile
from pathlib import Path

ARCHIVE_MODE = 0o444


def package_generation(storage_root: Path, generation_id: str, output: Path) -> Path:
    """Write ``<generation>-raw.tar.gz`` containing every retained artifact.

    The archive holds ``SHA256SUMS`` (matching the receipts) and the artifacts
    at their storage-relative paths. Entries are sorted and metadata is fixed,
    so the same generation always yields byte-identical archives.
    """
    manifest_path = storage_root / "manifests" / f"raw-generation-{generation_id}.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    receipts = [
        json.loads((storage_root / ref["receipt_relative_path"]).read_text("utf-8"))
        for ref in manifest["receipt_references"]
    ]
    artifacts = sorted(
        (receipt["artifact"]["relative_path"], receipt["artifact"]["sha256"])
        for receipt in receipts
        if receipt["acquisition_status"] == "succeeded"
    )
    sums = "".join(f"{digest}  {path}\n" for path, digest in artifacts).encode()

    buffer = io.BytesIO()
    with tarfile.open(fileobj=buffer, mode="w", format=tarfile.PAX_FORMAT) as tar:
        _add(tar, f"{generation_id}/SHA256SUMS", sums)
        for path, _ in artifacts:
            _add(tar, f"{generation_id}/{path}", (storage_root / path).read_bytes())

    output.mkdir(parents=True, exist_ok=True)
    archive = output / f"{generation_id}-raw.tar.gz"
    with archive.open("wb") as handle:
        with gzip.GzipFile(fileobj=handle, mode="wb", mtime=0, filename="") as gz:
            gz.write(buffer.getvalue())
    return archive


def _add(tar: tarfile.TarFile, name: str, data: bytes) -> None:
    info = tarfile.TarInfo(name)
    info.size = len(data)
    info.mtime = 0
    info.mode = ARCHIVE_MODE
    info.uid = info.gid = 0
    info.uname = info.gname = ""
    tar.addfile(info, io.BytesIO(data))
