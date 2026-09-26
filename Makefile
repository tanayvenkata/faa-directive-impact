.PHONY: sync test lint format check acquire-api-json

STORAGE_ROOT ?= data

sync:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

check: lint test


# Live network call. Example: make acquire-api-json DOC=2025-10764
acquire-api-json:
	uv run faa-directive-impact acquire-api-json $(DOC) --storage-root $(STORAGE_ROOT)
