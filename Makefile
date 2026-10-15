.PHONY: sync test lint format check acquire s1 s1-conclude llm-check b2 b3-plumbing b3 coverage-drafts \
	b3-replay b3-summary discovery-sync discovery-rollback discovery-drill discovery-site \
	fleet-build fleet-site retrieval-corpus retrieval-run

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

# Live model calls (batch, half price). Example: make b2 MODEL=claude-haiku-5-5 REPEAT=1
MODEL ?= claude-haiku-5-5
EFFORT ?= medium
REPEAT ?= 1
MAX_TOKENS ?= 16000
b2:
	uv run faa-directive-impact b2-run --model $(MODEL) --effort $(EFFORT) --repeat $(REPEAT) --max-tokens $(MAX_TOKENS)

# Live model call, one format-only rule draft on an unscored directive.
b3-plumbing:
	uv run faa-directive-impact b3-plumbing --model $(MODEL) --effort $(EFFORT)

# Live model calls (batch). Example: make b3 MODEL=claude-sonnet-5-5 EFFORT=high REPEAT=1
b3:
	uv run faa-directive-impact b3-run --model $(MODEL) --effort $(EFFORT) --repeat $(REPEAT)

# Offline. Example: make b3-replay RUN=evaluation/runs/b3-...
b3-replay:
	uv run faa-directive-impact b3-replay $(RUN)

# Offline. Writes evaluation/b3-summary.md and .json.
b3-summary:
	uv run faa-directive-impact b3-summary

# Live model calls (batch): the one coverage drafting run (prompt v2).
# Collect an interrupted run instead of redrafting it:
# make coverage-drafts BATCH=msgbatch_... STAMP=20261015T195012Z
coverage-drafts:
	uv run faa-directive-impact coverage-drafts drafts-opus-5-5-high $(if $(BATCH),--batch-id $(BATCH)) $(if $(STAMP),--stamp $(STAMP))

# Discovery corpus (ROADMAP step 6). Never writes to data/seed-frozen,
# data/frozen-evaluation, or generations/.
DISCOVERY_ROOT ?= data/discovery

# Live network call. Example: make discovery-sync (START_DATE applies only
# before the first promotion).
# 1994 is where the Federal Register API's documents begin.
START_DATE ?= 1994-01-01
discovery-sync:
	uv run faa-directive-impact discovery-sync --storage-root $(DISCOVERY_ROOT) --start-date $(START_DATE)

# Offline. Example: make discovery-rollback  (or TO=gen-... for a specific one)
discovery-rollback:
	uv run faa-directive-impact discovery-rollback --storage-root $(DISCOVERY_ROOT) $(if $(TO),--to $(TO),)

# Fetches discovery-state (read only), then offline: rollback drill on a copy
# under data/drill/; never pushes. STATE=<commit> drills an older state.
discovery-drill:
	operations/drills/rollback_drill.sh "$(STATE)" data/drill

# Offline. Writes site/index.html from the discovery state.
discovery-site:
	uv run faa-directive-impact discovery-site --storage-root $(DISCOVERY_ROOT) --output site

# Offline. Regenerates demo/fleet.json and demo/fleet-screen.json.
fleet-build:
	uv run faa-directive-impact fleet-build

# Offline. Writes site/fleet/index.html from demo/fleet-screen.json.
fleet-site:
	uv run faa-directive-impact fleet-site --output site

# Offline, needs the raw corpus under data/retrieval-frozen. Rebuilds
# evaluation/retrieval/corpus.json from the frozen retrieval generation.
RETRIEVAL_GENERATION ?= gen-20261015T175844Z-57440372
retrieval-corpus:
	uv run faa-directive-impact retrieval-corpus generations/$(RETRIEVAL_GENERATION) --storage-root data/retrieval-frozen

# Offline. Scores the retriever on the seed cases into evaluation/runs/.
retrieval-run:
	uv run faa-directive-impact retrieval-run
