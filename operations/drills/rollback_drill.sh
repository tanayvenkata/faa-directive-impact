#!/usr/bin/env bash
# Rollback drill on a LOCAL copy of the live discovery state (ROADMAP step 9).
#
# Copies the `discovery` folder of one discovery-state commit into a scratch
# directory with `git archive` (no branch, no worktree, nothing pushable),
# rolls the active generation back to its predecessor, checks that the
# freshness page renders the rolled-back generation, restores the original
# generation by id, and checks the page again. It never pushes and never
# touches data/discovery/.
#
# Usage (from the repository root):
#   operations/drills/rollback_drill.sh [STATE_COMMIT] [WORK_DIR]
# STATE_COMMIT defaults to the current origin discovery-state head; WORK_DIR
# defaults to data/drill (git-ignored). Prints a log; exit 0 means it passed.
set -euo pipefail

work="${2:-data/drill}"
if [ -n "${1:-}" ]; then
  state="$1"
else
  git fetch --quiet origin discovery-state
  state="$(git rev-parse FETCH_HEAD)"
fi
root="$work/discovery"

now() { date -u +%Y-%m-%dT%H:%M:%SZ; }
active() {
  python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["generation_id"])' \
    "$root/active.json"
}
render() {
  # Build the page from the drill copy and confirm it names $2 as active.
  uv run faa-directive-impact discovery-site --storage-root "$root" \
    --output "$work/site-$1" >/dev/null
  if grep -q "<dt>Active generation</dt><dd><code>$2</code>" "$work/site-$1/index.html"; then
    echo "$(now) page site-$1/index.html shows active generation $2"
  else
    echo "$(now) FAIL: page site-$1/index.html does not show $2" >&2
    exit 1
  fi
}

echo "$(now) drill start; state commit $state; work dir $work"
rm -rf "$work"
mkdir -p "$work"
git archive --output="$work/state.tar" "$state" discovery
tar -xf "$work/state.tar" -C "$work"
rm "$work/state.tar"

original="$(active)"
predecessor="$(python3 -c 'import json,sys; print(json.load(open(sys.argv[1]))["previous_generation_id"] or "")' "$root/active.json")"
promotions="$(grep -l '"receipt_type": "promotion"' "$root"/decisions/*.json | wc -l | tr -d ' ')"
echo "$(now) before: active $original; predecessor ${predecessor:-none}; $promotions promotion receipt(s)"
if [ -z "$predecessor" ]; then
  echo "$(now) FAIL: the active generation has no predecessor to roll back to" >&2
  exit 1
fi
render before "$original"

echo "$(now) \$ faa-directive-impact discovery-rollback --storage-root $root"
uv run faa-directive-impact discovery-rollback --storage-root "$root"
rolled="$(active)"
echo "$(now) after rollback: active $rolled"
[ "$rolled" = "$predecessor" ] || { echo "FAIL: expected $predecessor" >&2; exit 1; }
render rolled-back "$rolled"

echo "$(now) \$ faa-directive-impact discovery-rollback --storage-root $root --to $original"
uv run faa-directive-impact discovery-rollback --storage-root "$root" --to "$original"
restored="$(active)"
echo "$(now) after restore: active $restored"
[ "$restored" = "$original" ] || { echo "FAIL: expected $original" >&2; exit 1; }
render restored "$restored"

echo "$(now) rollback receipts written by the drill:"
grep -l '"receipt_type": "rollback"' "$root"/decisions/*.json | while read -r receipt; do
  python3 -c 'import json,sys; d=json.load(open(sys.argv[1])); print("  ", d["receipt_id"], d["decided_at_utc"], d["previous_generation_id"], "->", d["generation_id"])' "$receipt"
done
echo "$(now) drill passed"
