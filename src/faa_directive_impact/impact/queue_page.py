"""Render screened engines as one static HTML page with three review queues.

The page is a screening aid. It never states that an engine is compliant,
safe, or airworthy, and it carries no FAA branding.
"""

from html import escape
from typing import Any

QUEUE_ORDER = (
    (
        "potentially_affected",
        "Potentially affected",
        "Supplied records match the directive's required action.",
    ),
    (
        "needs_review",
        "Needs review",
        "A required fact is missing or unconfirmed. A person must supply it.",
    ),
    (
        "no_action_or_not_applicable",
        "No action currently required, or not applicable",
        "No required action is triggered by the supplied records, the engine "
        "model is not listed, or the engine is outside the supported scope.",
    ),
)
TAGS = {
    "action_required": "action required",
    "action_required_on_event": "action required on event",
    "needs_review": "needs review",
    "no_action_triggered": "no action triggered",
    "does_not_apply": "not applicable",
    "outside_supported_scope": "outside supported scope: no determination made",
}
DISCLAIMER = (
    "This page is a screening aid built from synthetic test engines. It is not "
    "a compliance determination, not an operator's AD status record, and not "
    "a maintenance or return-to-service decision. A qualified person must "
    "verify every result against the directive and the engine's records."
)

STYLE = """
:root { --fg:#1d1d1f; --muted:#5f6368; --bg:#ffffff; --card:#f6f7f9;
  --line:#d9dce1; --act:#b3261e; --rev:#8a5a00; --ok:#2f6f3e; }
@media (prefers-color-scheme: dark) {
  :root { --fg:#e8eaed; --muted:#a0a4aa; --bg:#16181b; --card:#202328;
    --line:#3a3e44; --act:#f2b8b5; --rev:#f5c26b; --ok:#8fd19e; } }
* { box-sizing: border-box; }
body { margin:0; padding:24px 16px 48px; background:var(--bg); color:var(--fg);
  font:15px/1.5 system-ui, -apple-system, "Segoe UI", sans-serif; }
main { max-width: 960px; margin: 0 auto; }
h1 { font-size: 1.5rem; margin: 0 0 4px; }
h2 { font-size: 1.15rem; margin: 32px 0 4px; }
.lede, .muted { color: var(--muted); }
.banner { border:1px solid var(--line); border-radius:8px; padding:12px 14px;
  margin:16px 0; background:var(--card); }
.counts { display:flex; gap:12px; flex-wrap:wrap; margin:16px 0; }
.count { border:1px solid var(--line); border-radius:8px; padding:8px 12px; }
.count b { font-size:1.3rem; display:block; }
details { border:1px solid var(--line); border-radius:8px; margin:10px 0;
  background:var(--card); }
summary { cursor:pointer; padding:10px 14px; list-style-position: outside; }
.body { padding:0 14px 12px; }
.tag { display:inline-block; font-size:.8rem; padding:1px 8px; border-radius:999px;
  border:1px solid currentColor; margin-left:6px; }
.potentially_affected .tag { color: var(--act); }
.needs_review .tag { color: var(--rev); }
.no_action_or_not_applicable .tag { color: var(--ok); }
ul { margin: 4px 0 8px; padding-left: 20px; }
code { font-size: .9em; overflow-wrap: anywhere; }
table { border-collapse: collapse; width: 100%; font-size: .9rem; }
th, td { text-align:left; padding:4px 6px; border-bottom:1px solid var(--line);
  vertical-align: top; }
.wrap { overflow-x: auto; }
footer { margin-top:40px; font-size:.85rem; color:var(--muted); }
"""


def render_page(
    screened: list[dict[str, Any]], record: dict[str, Any], meta: dict[str, Any]
) -> str:
    """Return the page. Each ``screened`` item has ``case``, ``engine``, ``screen``."""
    queues: dict[str, list[dict[str, Any]]] = {key: [] for key, _, _ in QUEUE_ORDER}
    for item in screened:
        queues[item["screen"]["queue"]].append(item)

    counts = "".join(
        f'<div class="count"><b>{len(queues[key])}</b>{escape(title)}</div>'
        for key, title, _ in QUEUE_ORDER
    )
    sections = []
    for key, title, explanation in QUEUE_ORDER:
        cards = "".join(_card(item) for item in queues[key]) or (
            '<p class="muted">None.</p>'
        )
        sections.append(
            f'<section class="{key}"><h2>{escape(title)} ({len(queues[key])})</h2>'
            f'<p class="muted">{escape(explanation)}</p>{cards}</section>'
        )
    source = record["source"]
    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Directive Screening Queues</title>
<style>{STYLE}</style>
</head>
<body>
<main>
<h1>{escape(record["ad_number"])} screening queues</h1>
<p class="lede">HPT 1st- and 2nd-stage hub removal (Federal Register document
{escape(record["document"])}), effective {escape(record["effective_date"])}.
Rules baseline S1: plain rules, no retrieval and no language model.</p>
<div class="banner">{escape(DISCLAIMER)}</div>
<div class="counts">{counts}</div>
{"".join(sections)}
<footer>
<p>Run <code>{escape(meta["run_id"])}</code> · gate version
{escape(str(meta["gate_version"]))} · commit <code>{escape(meta["commit"])}</code>
· source generation <code>{escape(source["generation_id"])}</code> · source
SHA-256 <code>{escape(source["sha256"])}</code> · normalized record
<code>{escape(record["record_sha256"][:16])}</code>.</p>
<p>Engines are synthetic evaluation cases, not a real fleet. Paragraph
references are to the directive's regulatory text.</p>
</footer>
</main>
</body>
</html>
"""


def _card(item: dict[str, Any]) -> str:
    screen = item["screen"]
    engine = item["engine"]
    status = screen["action_status"] or screen["applicability"]
    if screen["authority_state"] != "in_force":
        status_note = " · directive not yet effective on the question date"
    else:
        status_note = ""
    parts = [f"<p>{escape(screen['summary'])}</p>"]
    findings = [hub["statement"] for hub in screen["hubs"]]
    if findings:
        parts.append(_list("Hub findings", findings))
    if screen["timing"]:
        parts.append(f"<p><b>Timing.</b> {escape(screen['timing'])}</p>")
    if screen["missing_facts"]:
        parts.append(
            _list(
                "Missing or unconfirmed facts",
                screen["missing_facts"],
                code=True,
            )
        )
    obligations = [
        f"{o['paragraph']}: {o['text']}" for o in screen["continuing_obligations"]
    ]
    if obligations:
        parts.append(_list("Continuing obligations", obligations))
    if screen["notes"]:
        parts.append(_list("Notes", screen["notes"]))
    rows = "".join(
        f"<tr><td>{escape(c['document'])}</td><td>{escape(c['paragraph'])}</td>"
        f"<td>{escape(c['locator'] or '')}</td><td>{escape(c['supports'])}</td></tr>"
        for c in screen["citations"]
    )
    parts.append(
        '<p><b>Cited paragraphs</b></p><div class="wrap"><table><thead><tr>'
        "<th>Document</th><th>Paragraph</th><th>Locator</th><th>Supports</th>"
        f"</tr></thead><tbody>{rows}</tbody></table></div>"
    )
    return (
        f"<details><summary><b>{escape(engine['engine_serial_number'])}</b> · "
        f"{escape(engine['engine_model'])} · question date "
        f'{escape(item["as_of"])}<span class="tag">{escape(TAGS[status])}</span>'
        f'<span class="muted">{escape(status_note)} · case '
        f"{escape(item['case'])}</span></summary>"
        f'<div class="body">{"".join(parts)}</div></details>'
    )


def _list(title: str, items: list[str], code: bool = False) -> str:
    wrap = (lambda s: f"<code>{escape(s)}</code>") if code else escape
    return (
        f"<p><b>{escape(title)}</b></p><ul>"
        + "".join(f"<li>{wrap(item)}</li>" for item in items)
        + "</ul>"
    )
