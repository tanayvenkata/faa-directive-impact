"""Render the discovery corpus's freshness page as one static HTML file.

The page is built from the sync log, the decision receipts, and the active
generation, so it renders after a failed sync and before any success.
Staleness is computed in the viewer's browser: the page embeds the time of
the last successful sync, and a small inline script shows a STALE banner when
that is more than 48 hours before the viewer's clock. Without JavaScript the
page says plainly what date it is current as of.

The page is a screening aid. It carries no FAA logo or branding.
"""

import base64
import hashlib
import shutil
from html import escape
from pathlib import Path
from typing import Any

from faa_directive_impact.discovery.scope import (
    EVALUATED,
    NOT_YET_EVALUATED,
    OUTSIDE_SUPPORTED_SCOPE,
)
from faa_directive_impact.discovery.state import (
    read_active,
    read_attempts,
    read_decisions,
    read_generation,
)
from faa_directive_impact.discovery.sync import SUCCESSFUL_OUTCOMES

STALE_AFTER_HOURS = 48
MAX_LISTED = 100
S1_QUEUES_FILE = "s1-queues.html"
COVERAGE_LABELS = {
    EVALUATED: "Evaluated",
    NOT_YET_EVALUATED: "Not yet evaluated: unverified candidate",
    OUTSIDE_SUPPORTED_SCOPE: "Outside supported scope",
}
DISCLAIMER = (
    "Screening tool, not a compliance determination. This page lists Federal "
    "Register airworthiness directives found by an automated daily search. It "
    "is not an operator's AD status record and not a maintenance or "
    "return-to-service decision. Always work from the directive itself."
)
REDISTRIBUTION_NOTE = (
    "Receipts, manifests, decisions, and the sync log are published with this "
    "project. Raw source bytes of discovery generations are not redistributed: "
    "the scheduled sync keeps them only for the length of its run, and no "
    "release assets are made for them. Each receipt records the source URL "
    "and the SHA-256 of the bytes it saw."
)

STYLE = """
:root { --fg:#1d1d1f; --muted:#5f6368; --bg:#ffffff; --card:#f6f7f9;
  --line:#d9dce1; --bad:#b3261e; --warn:#8a5a00; --ok:#2f6f3e; --link:#0b57d0; }
@media (prefers-color-scheme: dark) {
  :root { --fg:#e8eaed; --muted:#a0a4aa; --bg:#16181b; --card:#202328;
    --line:#3a3e44; --bad:#f2b8b5; --warn:#f5c26b; --ok:#8fd19e;
    --link:#8ab4f8; } }
a { color: var(--link); }
* { box-sizing: border-box; }
body { margin:0; padding:24px 16px 48px; background:var(--bg); color:var(--fg);
  font:15px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; }
main { max-width: 960px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin: 0 0 4px; }
h2 { font-size: 1.15rem; margin: 32px 0 6px; }
.muted { color: var(--muted); }
.banner { border:1px solid var(--line); border-radius:8px; padding:12px 14px;
  margin:16px 0; background:var(--card); }
.alert { border:2px solid var(--bad); color:var(--bad); font-weight:600;
  border-radius:8px; padding:12px 14px; margin:16px 0; }
.alert[hidden] { display:none; }
.ok { color: var(--ok); } .bad { color: var(--bad); } .warn { color: var(--warn); }
dl { display:grid; grid-template-columns: minmax(8rem, max-content) 1fr;
  gap:4px 16px; margin:8px 0; }
dt { color: var(--muted); } dd { margin:0; overflow-wrap:anywhere; }
.counts { display:flex; gap:12px; flex-wrap:wrap; margin:12px 0; }
.count { border:1px solid var(--line); border-radius:8px; padding:8px 12px; }
.count b { font-size:1.3rem; display:block; }
.wrap { overflow-x:auto; }
table { border-collapse: collapse; width:100%; font-size:.9rem; }
th, td { text-align:left; padding:4px 6px; border-bottom:1px solid var(--line);
  vertical-align: top; }
.tag { display:inline-block; font-size:.8rem; padding:1px 8px; border-radius:999px;
  border:1px solid currentColor; white-space:nowrap; }
.not_yet_evaluated .tag { color: var(--warn); }
.evaluated .tag { color: var(--ok); }
ul { margin:4px 0 8px; padding-left:20px; }
code { font-size:.9em; overflow-wrap:anywhere; }
footer { margin-top:40px; font-size:.85rem; color:var(--muted); }
"""

STALENESS_SCRIPT = """
(function () {
  var node = document.getElementById("last-success");
  var banner = document.getElementById("stale-banner");
  if (!node || !banner) { return; }
  var when = Date.parse(node.getAttribute("datetime"));
  if (isNaN(when)) { return; }
  var hours = (Date.now() - when) / 3600000;
  if (hours > STALE_HOURS) {
    banner.textContent = "STALE: the last successful sync was " +
      Math.floor(hours) + " hours ago. Newer directives may be missing.";
    banner.hidden = false;
  }
}());
""".replace("STALE_HOURS", str(STALE_AFTER_HOURS))


def _csp_hash(text: str) -> str:
    digest = hashlib.sha256(text.encode("utf-8")).digest()
    return f"'sha256-{base64.b64encode(digest).decode()}'"


# The page needs only its own inline style and staleness script, allowed by
# hash; everything else (other scripts, frames, plugins, fetches, form posts,
# a <base> override) is refused. A meta-tag policy cannot set frame-ancestors.
CONTENT_SECURITY_POLICY = (
    "default-src 'none'; "
    f"style-src {_csp_hash(STYLE)}; "
    f"script-src {_csp_hash(STALENESS_SCRIPT)}; "
    "base-uri 'none'; form-action 'none'"
)
# Directive links are rendered only to the Federal Register; any other value
# in a search entry's html_url (a javascript: URL, another host) is shown as
# text, because escaping alone does not stop a javascript: link.
SAFE_LINK_PREFIX = "https://www.federalregister.gov/"


def load_state(root: Path) -> dict[str, Any]:
    """Collect what the page shows from a discovery storage root."""
    attempts = read_attempts(root) if (root / "attempts").is_dir() else []
    decisions = read_decisions(root) if (root / "decisions").is_dir() else []
    active = read_active(root)
    generation = read_generation(root, active["generation_id"]) if active else None
    return {
        "attempts": attempts,
        "decisions": decisions,
        "active": active,
        "generation": generation,
    }


def build_site(root: Path, output: Path, s1_queues: Path | None = None) -> Path:
    """Write ``index.html`` (and a copy of the S1 queues page, if given)."""
    output.mkdir(parents=True, exist_ok=True)
    linked = None
    if s1_queues is not None and s1_queues.is_file():
        shutil.copyfile(s1_queues, output / S1_QUEUES_FILE)
        linked = S1_QUEUES_FILE
    page = output / "index.html"
    page.write_text(render_page(load_state(root), linked), encoding="utf-8")
    return page


def latest_s1_queues(runs_root: Path) -> Path | None:
    """The newest committed S1 run's queue page, if there is one."""
    pages = sorted(runs_root.glob("s1-*/queues.html"))
    return pages[-1] if pages else None


def render_page(state: dict[str, Any], s1_queues_href: str | None = None) -> str:
    attempts = state["attempts"]
    generation = state["generation"]
    active = state["active"]
    last = attempts[-1] if attempts else None
    successes = [a for a in attempts if a.get("outcome") in SUCCESSFUL_OUTCOMES]
    last_success = successes[-1] if successes else None

    if last_success is None:
        freshness = (
            '<div class="alert" role="alert">No sync has succeeded yet. The '
            "corpus below is empty or incomplete.</div>"
        )
        as_of = '<p class="muted">No successful sync yet.</p>'
        script = ""
    else:
        stamp = last_success["finished_at_utc"]
        freshness = '<div id="stale-banner" class="alert" role="alert" hidden></div>'
        # After the elements it reads, so they exist when it runs.
        script = f"<script>{STALENESS_SCRIPT}</script>"
        as_of = (
            f'<p>As of <time id="last-success" datetime="{escape(stamp)}">'
            f"{escape(stamp[:10])}</time> (last successful sync, "
            f"{escape(stamp)} UTC). This page is regenerated by each sync; "
            f"it is stale if that date is more than {STALE_AFTER_HOURS} hours "
            "ago.</p>"
        )
    failed_now = last is not None and last.get("outcome") not in SUCCESSFUL_OUTCOMES
    failure_banner = (
        '<div class="alert" role="alert">The last sync attempt '
        f"({escape(last['started_at_utc'])}) did not succeed: "
        f"{escape(last.get('outcome', 'unknown'))}. The active generation "
        "below is unchanged from the last success.</div>"
        if failed_now
        else ""
    )

    s1_link = (
        f'<p>Evaluated screening queues for AD 2025-19-13: <a href="'
        f'{escape(s1_queues_href)}">S1 rules-baseline queues</a> (synthetic test '
        "engines).</p>"
        if s1_queues_href
        else ""
    )
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="{CONTENT_SECURITY_POLICY}">
<title>Directive Sync Freshness</title>
<style>{STYLE}</style>
</head>
<body>
<main>
<h1>FAA airworthiness directive sync</h1>
<p class="muted">Daily discovery of airworthiness directives published in the
Federal Register. Correctness claims cover only the IAE V2500-A5/D5/E5
boundary, and only AD 2025-19-13 is evaluated.</p>
<div class="banner">{escape(DISCLAIMER)}</div>
<p><a href="fleet/">Fleet view</a>: a synthetic 200-engine fleet screened
against AD 2025-19-13 (evaluated) and AD 2026-17-03 (not yet evaluated).</p>
{freshness}
{failure_banner}
{as_of}
<h2>Sync status</h2>
{_status(last, last_success, active, generation, state["decisions"])}
{s1_link}
{_failures(last)}
{_in_boundary(generation)}
{_new_directives(generation)}
{_review(generation)}
{_relationships(generation)}
{_dependencies(generation)}
<h2>Raw bytes and redistribution</h2>
<p>{escape(REDISTRIBUTION_NOTE)}</p>
<footer>
<p>Source: the Federal Register (Office of the Federal Register and GovInfo);
the directives are issued by the Federal Aviation Administration, U.S.
Department of Transportation. This project is independent and not affiliated
with the FAA.</p>
</footer>
</main>
{script}
</body>
</html>
"""


def _status(
    last: dict[str, Any] | None,
    last_success: dict[str, Any] | None,
    active: dict[str, Any] | None,
    generation: dict[str, Any] | None,
    decisions: list[dict[str, Any]] | None = None,
) -> str:
    def when(attempt: dict[str, Any] | None) -> str:
        if attempt is None:
            return "never"
        # The page header uses the finish time; show both so they agree.
        finished = attempt.get("finished_at_utc")
        span = f"started {attempt['started_at_utc']}" + (
            f", finished {finished}" if finished else ""
        )
        return f"{span} ({attempt.get('outcome', 'unknown')})"

    outcome_class = (
        "ok" if last and last.get("outcome") in SUCCESSFUL_OUTCOMES else "bad"
    )
    rows = [
        (
            "Last attempted sync",
            f'<span class="{outcome_class}">{escape(when(last))}</span>',
        ),
        ("Last successful sync", escape(when(last_success))),
        (
            "Checkpoint",
            f"{escape(active['checkpoint'])}: the latest publication date read. "
            "The Federal Register lists documents a few days before they "
            "publish, so this can be later than today. The next sync starts "
            "here."
            if active
            else "none yet",
        ),
        (
            "Coverage",
            "FAA airworthiness directives published on or after "
            f"{escape(generation['coverage_start'])}. Directives published "
            "earlier are not in this corpus."
            if generation and generation.get("coverage_start")
            else "coverage start not recorded",
        ),
        (
            "Active generation",
            f"<code>{escape(active['generation_id'])}</code>" if active else "none",
        ),
    ]
    activated_by = next(
        (
            d
            for d in decisions or []
            if active and d.get("receipt_id") == active.get("decision_receipt_id")
        ),
        None,
    )
    if activated_by is not None:
        # A rollback is shown as plainly as a promotion.
        kind = str(activated_by.get("receipt_type", "unknown"))
        rows.append(
            (
                "Activated by",
                f"{escape(kind)} at {escape(str(activated_by['decided_at_utc']))} "
                f"(<code>{escape(str(activated_by['receipt_id']))}</code>)",
            )
        )
    if active and active.get("previous_generation_id"):
        rows.append(
            (
                "Previous generation (rollback target)",
                f"<code>{escape(active['previous_generation_id'])}</code>",
            )
        )
    body = "".join(f"<dt>{label}</dt><dd>{value}</dd>" for label, value in rows)
    counts = ""
    if last is not None:
        attempt_counts = last.get("counts", {})
        items = [
            ("new", "New"),
            ("changed", "Changed"),
            ("failed", "Failed"),
            ("quarantined", "Quarantined for review"),
        ]
        counts = "".join(
            f'<div class="count"><b>{attempt_counts.get(key, 0)}</b>{label}</div>'
            for key, label in items
        )
        counts = f'<p class="muted">Last attempt:</p><div class="counts">{counts}</div>'
    totals = ""
    if generation is not None:
        by_state = generation["counts"].get("by_coverage_state", {})
        totals = "".join(
            f'<div class="count"><b>{by_state.get(state, 0)}</b>{escape(label)}</div>'
            for state, label in COVERAGE_LABELS.items()
        )
        totals = (
            '<p class="muted">Active generation, directives by coverage:</p>'
            f'<div class="counts">{totals}</div>'
        )
    return f"<dl>{body}</dl>{counts}{totals}"


def _failures(last: dict[str, Any] | None) -> str:
    if last is None:
        return ""
    if not last.get("failures"):
        return '<p class="ok">No failures in the last attempt.</p>'
    items = "".join(f"<li>{escape(f)}</li>" for f in last["failures"][:MAX_LISTED])
    return f'<h2 class="bad">Failures in the last attempt</h2><ul>{items}</ul>'


def _table(records: list[dict[str, Any]]) -> str:
    rows = []
    for record in records[:MAX_LISTED]:
        state = record["coverage_state"]
        title = escape(record["title"])
        url = record.get("html_url")
        if isinstance(url, str) and url.startswith(SAFE_LINK_PREFIX):
            title = f'<a href="{escape(url)}">{title}</a>'
        ads = ", ".join(record["ad_numbers"]) or "none"
        rows.append(
            f'<tr class="{escape(state)}"><td>{escape(ads)}</td>'
            f"<td>{escape(record['document_number'])}</td>"
            f"<td>{escape(record['publication_date'])}</td><td>{title}</td>"
            f'<td><span class="tag">{escape(COVERAGE_LABELS.get(state, state))}'
            "</span></td></tr>"
        )
    more = (
        f'<p class="muted">Showing {MAX_LISTED} of {len(records)}.</p>'
        if len(records) > MAX_LISTED
        else ""
    )
    return (
        '<div class="wrap"><table><thead><tr><th>AD</th><th>FR document</th>'
        "<th>Published</th><th>Title</th><th>Coverage</th></tr></thead><tbody>"
        + "".join(rows)
        + f"</tbody></table></div>{more}"
    )


def _in_boundary(generation: dict[str, Any] | None) -> str:
    if generation is None:
        return ""
    records = [
        r
        for r in generation["records"]
        if r["coverage_state"] in (EVALUATED, NOT_YET_EVALUATED)
    ]
    records.sort(key=lambda r: r["publication_date"], reverse=True)
    body = _table(records) if records else '<p class="muted">None.</p>'
    return (
        "<h2>Within the V2500-A5/D5/E5 boundary</h2>"
        '<p class="muted">Classified from each directive\'s paragraph (c) model '
        "list. A not-yet-evaluated directive is an unverified candidate: it has "
        "no verified rules or passing cases, and its results never enter the "
        "evaluated screening queues.</p>" + body
    )


def _new_directives(generation: dict[str, Any] | None) -> str:
    if generation is None:
        return ""
    new = set(generation.get("new_documents", []))
    records = [r for r in generation["records"] if r["document_number"] in new]
    records.sort(
        key=lambda r: (r["publication_date"], r["document_number"]), reverse=True
    )
    body = _table(records) if records else '<p class="muted">None.</p>'
    return (
        f"<h2>New in the active generation ({len(records)})</h2>"
        f'<p class="muted">Added by generation <code>'
        f"{escape(generation['generation_id'])}</code>, newest first.</p>" + body
    )


def _review(generation: dict[str, Any] | None) -> str:
    if generation is None or not generation.get("review"):
        return ""
    items = "".join(
        f"<li><b>{escape(r['document_number'])}</b> "
        f"({escape(', '.join(r['ad_numbers']) or 'no AD number')}): "
        f"{escape(r['title'])}. {escape(r['review_reason'])}</li>"
        for r in generation["review"][:MAX_LISTED]
    )
    return (
        f'<h2 class="warn">Needs a person to review ({len(generation["review"])})'
        '</h2><p class="muted">Held out of scope until reviewed; never '
        f"silently in scope.</p><ul>{items}</ul>"
    )


def _relationships(generation: dict[str, Any] | None) -> str:
    if generation is None:
        return ""
    unresolved = generation.get("unresolved_relationships", [])
    items = "".join(
        f"<li>{escape(u['relationship_type'])} from "
        f"{escape(u['from_document'])}: {escape(u['reason'])}</li>"
        for u in unresolved[:MAX_LISTED]
    )
    notes = "".join(f"<li>{escape(n)}</li>" for n in generation.get("notes", []))
    return (
        "<h2>Relationships</h2>"
        f"<p>{len(generation.get('relationships', []))} correction or "
        f"supersession link(s) derived; {len(unresolved)} left unresolved.</p>"
        + (f"<ul>{items}</ul>" if items else "")
        + f'<ul class="muted">{notes}</ul>'
    )


def _dependencies(generation: dict[str, Any] | None) -> str:
    if generation is None:
        return ""
    items = "".join(
        f"<li>{escape(d['name'])}"
        + (
            f" (named by {escape(d['document_number'])})"
            if d.get("document_number")
            else ""
        )
        + f": {escape(d['availability_status'].replace('_', ' '))}</li>"
        for d in generation.get("dependencies", [])
    )
    return (
        "<h2>Known unavailable dependencies</h2>"
        '<p class="muted">Manufacturer service information incorporated by '
        "reference is proprietary and never acquired; it is listed, not "
        f"summarized.</p><ul>{items}</ul>"
    )
