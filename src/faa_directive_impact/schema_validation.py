"""Validate durable acquisition records against the canonical JSON Schemas."""

import json
from importlib.resources import files
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

SCHEMA_PACKAGE = "faa_directive_impact.schemas"


def load_schema(schema_name: str) -> dict[str, Any]:
    """Load a packaged acquisition schema by filename."""
    schema_path = files(SCHEMA_PACKAGE).joinpath(schema_name)
    return json.loads(schema_path.read_text(encoding="utf-8"))


def validate_artifact_receipt(receipt: dict[str, Any]) -> None:
    """Raise ValidationError when an artifact receipt violates its contract."""
    _validator("artifact-receipt.schema.json").validate(receipt)


def validate_raw_generation_manifest(manifest: dict[str, Any]) -> None:
    """Raise ValidationError when a raw-generation manifest is invalid."""
    _validator("raw-generation-manifest.schema.json").validate(manifest)


def validate_validation_report(report: dict[str, Any]) -> None:
    """Raise ValidationError when a generation validation report is invalid."""
    _validator("validation-report.schema.json").validate(report)


def _validator(schema_name: str) -> Draft202012Validator:
    schema = load_schema(schema_name)
    Draft202012Validator.check_schema(schema)
    return Draft202012Validator(schema, format_checker=FormatChecker())
