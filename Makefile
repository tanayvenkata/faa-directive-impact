.PHONY: sync test lint format check acquire

STORAGE_ROOT ?= data
CORPUS_TRACK ?= frozen_evaluation

sync:
	uv sync

test:
	uv run pytest

lint:
	uv run ruff check .

format:
	uv run ruff format .

check: lint test


# Live network call. Example: make acquire DOCS="2025-10764 2025-18469"
acquire:
	uv run faa-directive-impact acquire $(DOCS) --storage-root $(STORAGE_ROOT) --corpus-track $(CORPUS_TRACK)
