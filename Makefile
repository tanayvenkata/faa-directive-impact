.PHONY: sync test lint format check acquire s1 s1-conclude llm-check

# Local settings and secrets (ANTHROPIC_API_KEY); optional and never committed.
-include .env
export

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

# Offline. Runs the S1 rules baseline and writes evaluation/runs/<run-id>/.
s1:
	uv run faa-directive-impact s1-run

# Offline. Example: make s1-conclude RUN=evaluation/runs/s1-...
s1-conclude:
	uv run faa-directive-impact s1-conclude $(RUN)

# Live model call, costs < $0.01. Confirms ANTHROPIC_API_KEY in .env works.
llm-check:
	uv run faa-directive-impact llm-check
