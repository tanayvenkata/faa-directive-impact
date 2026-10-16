"""Render the fleet view: one static HTML page over the recorded screens.

The page is built around one directive taking effect: AD 2025-19-13 on
2025-10-29, replayed as of the day before, the day itself, and the fleet
snapshot. Every queue, summary, timing, missing fact, citation, and cycle
count comes from a recorded file (``demo/fleet-screen.json``,
``demo/fleet-replay.json``, ``demo/fleet.json``); the browser only lays out,
counts, filters, and switches between recorded states. Sentences built from
data (the headline and the status line) are written here, at build time,
from the recorded counts.

The 20 evaluation-case engines are test fixtures. They are drawn in their own
band and never enter the fleet's tiles, counters, or lists.

Directives retrieved but not yet evaluated are shown in the sixteen-row
strip, hatched, and never set a queue (ROADMAP, "Directive Coverage State").

The page is a screening aid on a synthetic fleet. It carries no FAA logo or
branding.
"""

import json
from datetime import date
from html import escape
from pathlib import Path
from typing import Any

from faa_directive_impact.fleet.replay import REPLAY_DIRECTIVE, engine_as_of
from faa_directive_impact.fleet.slim import expand_fleet_screen

FLEET_PAGE_DIRECTORY = "fleet"
REPOSITORY_URL = "https://github.com/tanayvenkata/faa-directive-impact"
WRITEUP_02_URL = f"{REPOSITORY_URL}/blob/main/writeups/02-evaluated.md"
WRITEUP_03_URL = f"{REPOSITORY_URL}/blob/main/writeups/03-full-coverage.md"
# The freshness page sits one level up on the published site.
FRESHNESS_URL = "../"
# The first daily sync of the discovery corpus (DISCOVERY_SYNC.md).
DAILY_SYNC_BEGAN = "2026-10-11"
DISCLAIMER = (
    "Screening tool, not a compliance determination. The fleet is synthetic. "
    "Nothing here is an operator's AD status record or a maintenance, "
    "airworthiness, or return-to-service decision. Always work from the "
    "directive itself."
)
EYEBROW = (
    "Synthetic V2500 fleet &middot; Screening tool, not a compliance determination"
)
# Words the page must never use about an engine (tests/fleet/test_page.py).
FORBIDDEN_WORDS = (
    "compliant",
    "noncompliant",
    "airworthy",
    "safe",
    "approved for return to service",
    "overdue",
)
HUB_COMPONENTS = ("HPT 1st-stage hub", "HPT 2nd-stage hub")
POTENTIALLY_AFFECTED = "potentially_affected"
NEEDS_REVIEW = "needs_review"
NO_ACTION = "no_action_or_not_applicable"
QUEUE_KEYS = (POTENTIALLY_AFFECTED, NEEDS_REVIEW, NO_ACTION)
NUMBER_WORDS = (
    "no zero one two three four five six seven eight nine ten eleven twelve "
    "thirteen fourteen fifteen sixteen seventeen eighteen nineteen twenty"
).split()[1:]


def build_fleet_page(
    fleet_screen: dict[str, Any],
    site_root: Path,
    replay: dict[str, Any] | None = None,
    fleet: dict[str, Any] | None = None,
) -> Path:
    """Write ``<site_root>/fleet/index.html`` and return its path."""
    directory = site_root / FLEET_PAGE_DIRECTORY
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "index.html"
    path.write_text(render_fleet_page(fleet_screen, replay, fleet), encoding="utf-8")
    return path


def render_fleet_page(
    fleet_screen: dict[str, Any],
    replay: dict[str, Any] | None = None,
    fleet: dict[str, Any] | None = None,
) -> str:
    """The page as one HTML string.

    Without ``replay`` the banner, date control, fleet tiles, and movers are
    left out; without ``fleet`` the engines' records come from the screen.
    """
    fleet_screen = expand_fleet_screen(fleet_screen)  # the file is slim
    data = page_data(fleet_screen, replay, fleet)
    text = json.dumps(data, sort_keys=True, separators=(",", ":"))
    # Keep the embedded JSON from closing the script element early.
    text = text.replace("</", "<\\/")
    story = data["story"]
    return (
        TEMPLATE.replace("__STYLE__", STYLE)
        .replace("__SCRIPT__", SCRIPT)
        .replace("__DATA__", text)
        .replace("__EYEBROW__", EYEBROW)
        .replace("__HEADLINE__", escape(story["headline"]))
        .replace("__STATUS__", escape(story["status"]))
        .replace("__REPLAY_HIDDEN__", "" if replay else " hidden")
        .replace("__RULES__", escape(story["rules"]))
        .replace("__SYNC_BEGAN__", _day_label(DAILY_SYNC_BEGAN))
        .replace("__FRESHNESS__", FRESHNESS_URL)
        .replace("__DISCLAIMER__", escape(DISCLAIMER))
        .replace("__REPO__", REPOSITORY_URL)
        .replace("__WRITEUP02__", WRITEUP_02_URL)
        .replace("__WRITEUP03__", WRITEUP_03_URL)
        .replace("__FLEET_SHA__", fleet_screen["fleet_sha256"][:12])
    )


def page_data(
    fleet_screen: dict[str, Any],
    replay: dict[str, Any] | None,
    fleet: dict[str, Any] | None,
) -> dict[str, Any]:
    """Everything the page shows, shaped from the recorded files.

    Summaries, timings, and citations repeat across engines, so each distinct
    one is stored once and screens refer to it by index.
    """
    strings: dict[str, int] = {}
    cites: dict[str, int] = {}

    def string_index(value: str | None) -> int | None:
        return None if value is None else strings.setdefault(value, len(strings))

    def cite_index(citation: dict[str, Any]) -> int:
        return cites.setdefault(json.dumps(citation, sort_keys=True), len(cites))

    def pack(entry: dict[str, Any]) -> dict[str, Any]:
        computed = entry.get("computed") or {}
        return {
            "q": entry["queue"],
            "s": string_index(entry["summary"]),
            "t": string_index(entry["timing"]),
            "m": entry["missing_facts"],
            "c": [cite_index(c) for c in entry["citations"]],
            "r": computed.get("component_cycles_remaining"),
            "k": computed.get("latest_engine_flight_cycles"),
        }

    directives = fleet_screen["directives"]
    by_document = {d["document"]: d for d in directives}
    # The replayed directive; without a replay, the one the replay is of.
    document = replay["directive"] if replay else REPLAY_DIRECTIVE
    directive = by_document[document]
    screened = {e["asset"]["engine"]["asset_id"]: e for e in fleet_screen["engines"]}
    assets = (
        {e["engine"]["asset_id"]: e for e in fleet["engines"]}
        if fleet
        else {asset_id: e["asset"] for asset_id, e in screened.items()}
    )
    snapshot_day = _snapshot_day(fleet_screen, fleet)

    states: list[dict[str, Any]] = []
    engines: list[dict[str, Any]] = []
    movers: list[str] = []
    replayed: list[str] = []
    if replay:
        replayed = sorted(replay["states"][replay["dates"][0]]["engines"])
        for day in replay["dates"]:
            states.append(
                {
                    "key": day,
                    "label": _day_label(day),
                    "replay": True,
                    "in_force": day >= directive["effective_date"],
                    "counts": _counts(replay["states"][day]["counts"]),
                }
            )
        states.append(
            {
                "key": snapshot_day,
                "label": _day_label(snapshot_day),
                "replay": False,
                "in_force": True,
                "counts": _counts(
                    _tally(screened[a]["screens"][document]["queue"] for a in replayed)
                ),
            }
        )
        last = replay["states"][replay["dates"][-1]]["engines"]
        order = {POTENTIALLY_AFFECTED: 0, NEEDS_REVIEW: 1, NO_ACTION: 2}

        def mover_key(asset_id: str) -> tuple[int, float, str]:
            remaining = (last[asset_id].get("computed") or {}).get(
                "component_cycles_remaining"
            )
            return (
                order[last[asset_id]["queue"]],
                remaining if remaining is not None else float("inf"),
                asset_id,
            )

        movers = sorted(replay["moved"], key=mover_key)
        left_out = set(replay["left_out"])
        for asset_id, entry in screened.items():
            asset = assets[asset_id]
            if "evaluation_case" in asset:
                continue
            identity = asset["engine"]
            engine: dict[str, Any] = {
                "id": asset_id,
                "esn": identity["engine_serial_number"],
                "model": identity["engine_model"],
                "tail": identity.get("aircraft_tail_id"),
                "pos": identity.get("installation_position"),
                "out": asset_id in left_out,
            }
            if asset_id not in left_out:
                engine["st"] = {
                    day: pack(replay["states"][day]["engines"][asset_id])
                    for day in replay["dates"]
                }
                engine["st"][snapshot_day] = pack(entry["screens"][document])
                engine["hubs"] = {
                    day: _hubs(engine_as_of(asset, day)) for day in replay["dates"]
                }
                engine["hubs"][snapshot_day] = _hubs(asset)
            engines.append(engine)
        engines.sort(key=lambda e: (e["tail"] or "", e["pos"] or 0, e["id"]))

    fixtures = []
    for asset_id, entry in screened.items():
        asset = assets[asset_id]
        case = asset.get("evaluation_case")
        if not case:
            continue
        screen = entry["screens"].get(document)
        fixtures.append(
            {
                "id": asset_id,
                "esn": asset["engine"]["engine_serial_number"],
                "model": asset["engine"]["engine_model"],
                "case": case["case_id"],
                "title": case["title"],
                "as_of": entry["as_of"],
                "sc": pack(screen) if screen else None,
                "hubs": _hubs(asset),
            }
        )
    fixtures.sort(key=lambda f: f["id"])

    return {
        "directive": {
            "document": document,
            "ad": directive["ad_number"],
            "effective": directive["effective_date"],
            "provenance": directive.get("review_provenance"),
        },
        "ad_numbers": {d["document"]: d["ad_number"] for d in directives},
        "states": states,
        "default_state": 1 if len(states) > 1 else 0,
        "engines": engines,
        "movers": movers,
        "fixtures": fixtures,
        "left_out_reason": replay["left_out_reason"] if replay else None,
        "strip": [_strip_row(d, fleet_screen) for d in _strip_order(directives)],
        "screened_engines": len(fleet_screen["engines"]),
        "snapshot": _day_label(snapshot_day),
        "fixture_count": len(fixtures),
        "story": _story(directive, replay, fleet),
        "strings": list(strings),
        "cites": [json.loads(key) for key in cites],
    }


def _snapshot_day(fleet_screen: dict[str, Any], fleet: dict[str, Any] | None) -> str:
    if fleet:
        return fleet["snapshot_at"]
    generated = [
        e for e in fleet_screen["engines"] if "evaluation_case" not in e["asset"]
    ]
    return (generated or fleet_screen["engines"])[0]["as_of"]


def _tally(queues: Any) -> dict[str, int]:
    counts: dict[str, int] = {}
    for queue in queues:
        counts[queue] = counts.get(queue, 0) + 1
    return counts


def _counts(counts: dict[str, int]) -> dict[str, int]:
    return {key: counts.get(key, 0) for key in QUEUE_KEYS}


def _hubs(asset: dict[str, Any]) -> list[dict[str, Any]]:
    """The installed HPT hubs: name, P/N, S/N, cycles since new (or None)."""
    found = {c["component_name"]: c for c in asset.get("installed_components", [])}
    return [
        {
            "n": name,
            "pn": found[name].get("part_number"),
            "sn": found[name].get("serial_number"),
            "csn": found[name].get("cycles_since_new"),
        }
        if name in found
        else {"n": name, "pn": None, "sn": None, "csn": None, "absent": True}
        for name in HUB_COMPONENTS
    ]


def _day_label(day: str) -> str:
    value = date.fromisoformat(day)
    return f"{value.day} {value.strftime('%b %Y')}"


def _count_words(n: int) -> str:
    return NUMBER_WORDS[n] if 0 <= n < len(NUMBER_WORDS) else f"{n:,}"


def _story(
    directive: dict[str, Any],
    replay: dict[str, Any] | None,
    fleet: dict[str, Any] | None,
) -> dict[str, str]:
    """The headline and status line, written from the recorded counts."""
    ad = directive["ad_number"]
    if not replay:
        return {
            "headline": f"Which engines does {ad} touch, and why?",
            "status": "",
            "rules": "",
        }
    effective = replay["states"][replay["dates"][-1]]
    counts = _counts(effective["counts"])
    affected, review = counts[POTENTIALLY_AFFECTED], counts[NEEDS_REVIEW]
    headline = (
        f"{ad} took effect on {_day_label(directive['effective_date'])}. "
        f"{_count_words(affected).capitalize()} "
        f"{'engine' if affected == 1 else 'engines'} must lose a hub, "
        f"{_count_words(review)} {'needs' if review == 1 else 'need'} a person, "
        "and the screen says which paragraph and which missing fact."
    )
    status = ""
    if fleet:
        planted = {
            p["engine_asset_id"]
            for p in fleet["composition"].get("planted_listed_parts", [])
            if p["directive"] == ad
        }
        found = {
            asset_id
            for asset_id, screen in effective["engines"].items()
            if screen["queue"] == POTENTIALLY_AFFECTED
        }
        n = _count_words(len(planted))
        if planted and found == planted:
            status = (
                f"The {n} listed hubs were planted in the synthetic fleet on "
                f"purpose; the screen found all {n} and no others."
            )
        elif planted:
            status = (
                f"{n.capitalize()} listed hubs were planted in the synthetic fleet "
                f"on purpose; the screen flagged {len(found & planted)} of them "
                f"and {len(found - planted)} other engines."
            )
    return {"headline": headline, "status": status, "rules": replay["rules"]}


def _strip_order(directives: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Evaluated directives first, then the rest, newest first."""
    return sorted(
        directives,
        key=lambda d: (
            d["coverage_state"] != "evaluated",
            _negated(d["effective_date"]),
        ),
    )


def _negated(day: str) -> int:
    return -date.fromisoformat(day).toordinal()


def _strip_row(
    directive: dict[str, Any], fleet_screen: dict[str, Any]
) -> dict[str, Any]:
    document = directive["document"]
    superseded = None
    if directive["engines"] and directive["superseded"] == directive["engines"]:
        superseded = next(
            e["screens"][document]["summary"]
            for e in fleet_screen["engines"]
            if document in e["screens"]
            and e["screens"][document]["applicability"] == "superseded"
        )
    held = [
        {"document": b["document"], "engines": b["engines"]}
        for b in directive["blocking_documents"]
    ]
    facts = [] if held or superseded else directive["missing_facts"][:1]
    return {
        "document": document,
        "ad": directive["ad_number"],
        "effective": directive["effective_date"],
        "evaluated": directive["coverage_state"] == "evaluated",
        "engines": directive["engines"],
        "queues": _counts(directive["queues"]),
        "superseded": superseded,
        "held": held,
        "facts": [
            {"fact": f["fact"], "kind": f["kind"], "engines": f["engines"]}
            for f in facts
        ],
        "provenance": directive.get("review_provenance"),
    }


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>Fleet Directive Screen</title>
<meta name="description" content="An as-of replay of AD 2025-19-13 taking effect across a synthetic V2500 fleet, from recorded screening output.">
<style>__STYLE__</style>
</head>
<body>
<main>
  <p class="eyebrow">__EYEBROW__</p>
  <h1 id="headline">__HEADLINE__</h1>
  <p class="status-line" id="status-line">__STATUS__</p>

  <div class="replay-banner" role="note" id="banner"__REPLAY_HIDDEN__>
    <span class="tag">As-of replay, not live</span>
    <span>The system re-screened recorded fleet states; it did not watch this
    directive go live. The daily sync began on __SYNC_BEGAN__, after this
    directive took effect; what is live is the
    <a href="__FRESHNESS__">directive freshness page</a>. __RULES__</span>
  </div>

  <section class="replay" id="replay" aria-label="As-of replay"__REPLAY_HIDDEN__>
    <div class="controls">
      <div class="seg" role="radiogroup" aria-label="Screened as of" id="seg"></div>
      <button type="button" class="play" id="play">Replay 28 &rarr; 29 Oct</button>
      <span class="status" id="status" aria-live="polite"></span>
    </div>

    <div class="stats" id="stats" aria-live="polite"></div>

    <section class="fleet-wrap" aria-labelledby="fleet-h">
      <div class="fleet-head">
        <h2 id="fleet-h">The fleet, two engines per aircraft</h2>
        <span class="small muted" id="fleet-sub"></span>
      </div>
      <div class="groups" id="groups"></div>
      <p class="note" id="tile-note" aria-live="polite"></p>
      <div class="legend" id="legend">
        <span><i class="sw pa"></i>Potentially affected</span>
        <span><i class="sw nr"></i>Needs review</span>
        <span><i class="sw na"></i>No action or not applicable</span>
        <span><i class="sw ny"></i>Not yet in force</span>
        <span><i class="sw ny named"></i>Names a listed hub before it takes effect</span>
        <span><i class="sw out"></i>Not replayed</span>
      </div>
    </section>

    <section class="movers" aria-labelledby="movers-h">
      <h2 id="movers-h">The engines that move</h2>
      <p class="small muted" id="movers-sub"></p>
      <ol id="movers"></ol>
    </section>

    <section class="fixtures" aria-labelledby="fixtures-h">
      <h2 id="fixtures-h">Test fixtures, not part of the fleet</h2>
      <p class="small muted">These are test cases that reuse serial numbers listed
      in the directive, so a listed serial can appear on a fixture and a fleet
      engine. Each is screened as of its own case date and is never counted
      above.</p>
      <div class="ac-grid" id="fixtures"></div>
    </section>
  </section>

  <section class="strip" aria-labelledby="strip-h">
    <h2 id="strip-h">Sixteen directives retrieved for this fleet</h2>
    <p class="small muted">Solid rows are evaluated and set an engine's queue.
    Hatched rows are not yet evaluated: screened and shown, but they cannot set
    a queue. Counts are of all <span id="strip-n"></span> screened engines,
    <span id="strip-fixtures"></span> of them test fixtures, as of the
    <span id="strip-asof"></span> snapshot.</p>
    <div id="rows"></div>
  </section>

  <section class="colophon" aria-labelledby="who-h">
    <h2 id="who-h">Who checked what</h2>
    <div class="who">
      <div class="hcard"><b>AD 2025-19-13</b>Hand-written rules (S1). The
      hand-judged gates were judged by Claude only.</div>
      <div class="hcard"><b>AD 2020-07-51</b>A model draft, proofread by a
      Claude stand-in (<code>label_review: claude_stand_in</code>).</div>
      <div class="hcard"><b>Nobody else</b>No practitioner has reviewed any of
      it. Zero false clears on 95 scored units.</div>
    </div>
    <p class="whole">That is the whole product: the paragraph that applies, the
    part that triggers it, the counter it must be done by, and the fact a person
    still has to settle.</p>
    <p class="small"><a href="__WRITEUP02__">Write-up 02: Evaluated</a> &middot;
    <a href="__WRITEUP03__">Write-up 03: Full coverage</a> &middot;
    <a href="__REPO__">Repository</a> &middot;
    <a href="__FRESHNESS__">Directive freshness</a></p>
  </section>

  <footer>
    <p>__DISCLAIMER__</p>
    <p>Fleet <code>__FLEET_SHA__</code>.</p>
  </footer>
</main>

<aside class="drawer" id="drawer" aria-hidden="true" aria-labelledby="d-title" role="dialog">
  <div class="drawer-inner">
    <button type="button" class="close" id="close" aria-label="Close">&times;</button>
    <div id="detail"></div>
  </div>
</aside>
<div class="scrim" id="scrim" hidden></div>

<script id="fleet-data" type="application/json">__DATA__</script>
<script>__SCRIPT__</script>
</body>
</html>
"""

STYLE = """
:root {
  --bg:#f6f5f1; --panel:#ffffff; --fg:#17181a; --muted:#5c5f65; --line:#dcdad3; --line-2:#ecebe5;
  --affected:#c8431f; --affected-ink:#ffffff; --review:#c98a12; --review-ink:#1b1c1e;
  --clear:#d4d6cf; --notyet:#9fb0c8; --notyet-ink:#1b1c1e; --off:#f1f0eb; --off-line:#b9b8b1;
  --accent:#1d4ed8; --ok:#2f7a45; --warn-bg:#fff4d6; --warn-line:#e6c36a;
  --hatch:rgba(0,0,0,.14); --shadow:0 18px 50px rgba(20,20,20,.18);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg:#111214; --panel:#1a1c1f; --fg:#ecebe6; --muted:#a0a2a7; --line:#2d3035; --line-2:#23262a;
    --affected:#f26b47; --affected-ink:#1b1c1e; --review:#f0b43c; --review-ink:#1b1c1e;
    --clear:#3a3d42; --notyet:#5d7091; --notyet-ink:#ecebe6; --off:#16171a; --off-line:#4a4d53;
    --accent:#8fb0ff; --ok:#8fd19e; --warn-bg:#2a2410; --warn-line:#6b5a1e;
    --hatch:rgba(255,255,255,.16); --shadow:0 18px 50px rgba(0,0,0,.6);
  }
}
:root[data-theme="dark"] {
  --bg:#111214; --panel:#1a1c1f; --fg:#ecebe6; --muted:#a0a2a7; --line:#2d3035; --line-2:#23262a;
  --affected:#f26b47; --affected-ink:#1b1c1e; --review:#f0b43c; --review-ink:#1b1c1e;
  --clear:#3a3d42; --notyet:#5d7091; --notyet-ink:#ecebe6; --off:#16171a; --off-line:#4a4d53;
  --accent:#8fb0ff; --ok:#8fd19e; --warn-bg:#2a2410; --warn-line:#6b5a1e;
  --hatch:rgba(255,255,255,.16); --shadow:0 18px 50px rgba(0,0,0,.6);
}
* { box-sizing:border-box; }
html { -webkit-text-size-adjust:100%; }
body { margin:0; background:var(--bg); color:var(--fg);
  font:15px/1.5 ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif; }
main { max-width:1180px; margin:0 auto; padding:28px 16px 64px; }
[hidden] { display:none !important; }
a { color:var(--accent); }
code { font:12px/1.4 ui-monospace, SFMono-Regular, Menlo, monospace; overflow-wrap:anywhere; }
.mono { font-family:ui-monospace, SFMono-Regular, Menlo, monospace; font-variant-numeric:tabular-nums; }
.muted { color:var(--muted); }
.small { font-size:13px; }
.note { font-size:12.5px; color:var(--muted); margin:8px 0 0; min-height:1.4em; }
.eyebrow { margin:0 0 8px; font-size:12px; letter-spacing:.08em; text-transform:uppercase; color:var(--muted); }
h1 { font-size:clamp(26px, 4.2vw, 44px); line-height:1.08; margin:0 0 12px; letter-spacing:-.022em; max-width:26ch; }
.status-line { margin:0 0 18px; color:var(--muted); max-width:70ch; font-size:16px; }
h2 { font-size:16px; margin:0 0 4px; }

.replay-banner { position:sticky; top:0; z-index:5; display:flex; gap:12px; align-items:flex-start;
  background:var(--warn-bg); border:1px solid var(--warn-line); border-radius:12px; padding:10px 14px;
  margin:0 0 18px; font-size:13.5px; }
.replay-banner .tag { flex:none; font-size:11px; font-weight:700; letter-spacing:.06em; text-transform:uppercase;
  padding:3px 8px; border-radius:6px; background:var(--fg); color:var(--bg); margin-top:2px; }

.controls { display:flex; flex-wrap:wrap; gap:10px 14px; align-items:center; margin:0 0 14px; }
.seg { display:inline-flex; flex-wrap:wrap; background:var(--panel); border:1px solid var(--line);
  border-radius:12px; padding:3px; gap:2px; max-width:100%; }
.seg button { font:inherit; color:var(--muted); background:none; border:0; border-radius:9px; padding:8px 12px;
  cursor:pointer; display:flex; flex-direction:column; align-items:flex-start; line-height:1.2; }
.seg .k { font-size:11px; letter-spacing:.05em; text-transform:uppercase; }
.seg .v { font-weight:600; font-size:14px; color:var(--fg); margin-top:2px; }
.seg button[aria-checked="true"] { background:var(--fg); color:var(--bg); }
.seg button[aria-checked="true"] .v { color:var(--bg); }
.seg button:focus-visible, .play:focus-visible, .close:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.play { font:inherit; font-weight:600; border:1px solid var(--line); border-radius:999px; padding:9px 16px;
  background:var(--panel); color:var(--fg); cursor:pointer; }
.status { font-size:13px; color:var(--muted); }

.stats { display:grid; grid-template-columns:repeat(4, minmax(0,1fr)); gap:10px; margin:0 0 14px; }
.stat { background:var(--panel); border:1px solid var(--line); border-radius:12px; padding:12px 14px 12px 18px;
  position:relative; overflow:hidden; }
.stat i { position:absolute; left:0; top:0; bottom:0; width:5px; background:var(--clear); }
.stat.pa i { background:var(--affected); } .stat.nr i { background:var(--review); }
.stat.ny i { background:var(--notyet); } .stat.out i { background:var(--off-line); }
.stat b { display:block; font-size:clamp(26px, 4vw, 38px); line-height:1; font-variant-numeric:tabular-nums;
  letter-spacing:-.02em; }
.stat .lab { display:block; color:var(--muted); font-size:13px; margin-top:6px; }
.stat .delta { display:block; font-size:12.5px; font-weight:600; margin-top:4px; color:var(--fg);
  font-variant-numeric:tabular-nums; }
.stat .delta.zero { color:var(--muted); font-weight:500; }

.fleet-wrap, .movers, .fixtures, .strip, .colophon { background:var(--panel); border:1px solid var(--line);
  border-radius:16px; padding:14px 16px; margin-top:14px; }
.fleet-head { display:flex; justify-content:space-between; gap:6px 12px; flex-wrap:wrap; align-items:baseline;
  margin-bottom:10px; }
.groups { display:flex; flex-wrap:wrap; gap:14px 22px; }
.group h3 { margin:0 0 6px; font-size:12px; color:var(--muted); font-weight:500; letter-spacing:.04em;
  text-transform:uppercase; }
.ac-grid { display:flex; flex-wrap:wrap; gap:6px; }
.ac { display:flex; gap:2px; padding:2px; border-radius:6px; background:var(--line-2); }
.eng { width:16px; height:16px; border-radius:3px; border:0; padding:0; cursor:pointer; position:relative;
  background:var(--clear); transition:background-color .35s ease; }
.eng.pa { background:var(--affected); }
.eng.nr { background:var(--review); }
.eng.ny { background:var(--notyet); }
.eng.named { box-shadow:inset 0 0 0 2px var(--affected); }
.eng.out { background:var(--off); box-shadow:inset 0 0 0 1px var(--off-line);
  background-image:repeating-linear-gradient(135deg, var(--hatch) 0 1px, transparent 1px 4px); }
.eng.fx { background:transparent; box-shadow:inset 0 0 0 2px var(--fg); }
.eng:focus-visible { outline:2px solid var(--accent); outline-offset:2px; z-index:1; }
.eng.hit { animation:hit .9s ease-out 1; }
@keyframes hit { 0% { transform:scale(1.9); filter:brightness(1.4); } 100% { transform:none; filter:none; } }
.legend { display:flex; flex-wrap:wrap; gap:6px 16px; margin:10px 0 0; color:var(--muted); font-size:12.5px; }
.legend span { display:inline-flex; align-items:center; gap:6px; }
.sw { width:12px; height:12px; border-radius:3px; display:inline-block; background:var(--clear); }
.sw.pa { background:var(--affected); } .sw.nr { background:var(--review); } .sw.ny { background:var(--notyet); }
.sw.named { box-shadow:inset 0 0 0 2px var(--affected); }
.sw.out { background:var(--off); box-shadow:inset 0 0 0 1px var(--off-line);
  background-image:repeating-linear-gradient(135deg, var(--hatch) 0 1px, transparent 1px 4px); }

.movers ol { list-style:none; margin:8px 0 0; padding:0; }
.movers li { border-top:1px solid var(--line-2); }
.movers li:first-child { border-top:0; }
.mrow { all:unset; box-sizing:border-box; display:grid; grid-template-columns:12px minmax(0,1fr) minmax(0,14rem);
  gap:4px 12px; width:100%; padding:10px 2px; cursor:pointer; font-size:13.5px; }
.mrow:focus-visible { outline:2px solid var(--accent); outline-offset:-2px; border-radius:6px; }
.mrow:hover { background:var(--line-2); }
.dot { width:12px; height:12px; border-radius:3px; margin-top:4px; background:var(--clear); }
.dot.pa { background:var(--affected); } .dot.nr { background:var(--review); } .dot.ny { background:var(--notyet); }
.mrow .who { font-weight:600; }
.mrow .who .muted { font-weight:400; }
.mrow .sum { display:block; color:var(--fg); margin-top:2px; }
.mrow .tim { display:block; color:var(--muted); font-size:12.5px; margin-top:2px; }
.mrow .par { display:block; color:var(--muted); font-size:12.5px; margin-top:2px; }
.mrow .fig { text-align:right; font-size:13px; }
.mrow .fig b { display:block; font-size:18px; font-variant-numeric:tabular-nums; }
.mrow .fig > span, .mrow .fig code { display:block; }
.mrow .fig code { text-align:left; margin-top:2px; }
.mrow .fig b + span { margin-bottom:4px; }
.q { display:inline-block; font-size:11.5px; font-weight:600; padding:1px 7px; border-radius:6px;
  background:var(--clear); color:var(--fg); white-space:nowrap; }
.q.pa { background:var(--affected); color:var(--affected-ink); }
.q.nr { background:var(--review); color:var(--review-ink); }
.q.ny { background:var(--notyet); color:var(--notyet-ink); }

.fixtures .ac-grid { margin-top:8px; }

.row { border-top:1px solid var(--line-2); padding:10px 0; display:grid;
  grid-template-columns:minmax(0,11rem) minmax(0,1fr); gap:4px 14px; }
.row:first-child { border-top:0; }
.row .lab { font-size:13px; line-height:1.3; }
.row .lab b { display:block; font-size:14px; }
.row .lab .st { font-size:11.5px; color:var(--muted); }
.row .lab .st.ev { color:var(--ok); font-weight:600; }
.bar { display:flex; height:18px; border-radius:4px; overflow:hidden; background:var(--clear); }
.bar i { display:block; height:100%; }
.bar .pa { background:var(--affected); } .bar .nr { background:var(--review); } .bar .na { background:var(--clear); }
.row.nye .bar { height:12px; opacity:.85; }
.row.nye .bar i { background-image:repeating-linear-gradient(135deg, var(--hatch) 0 2px, transparent 2px 6px); }
.row.sup .bar i { opacity:.55; }
.row .counts { font-size:12px; color:var(--muted); margin-top:4px; font-variant-numeric:tabular-nums; }
.row .held { font-size:13px; margin-top:4px; }
.row .caveat { font-size:12px; color:var(--muted); margin-top:2px; }
.sep { margin:12px 0 0; padding-top:10px; border-top:1px dashed var(--line); font-size:11px; letter-spacing:.06em;
  text-transform:uppercase; color:var(--muted); }

.who { display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:10px; margin-top:8px; }
.hcard { border:1px solid var(--line); border-radius:12px; padding:12px 14px; font-size:13.5px; }
.hcard b { display:block; margin-bottom:4px; }
.whole { font-size:17px; line-height:1.45; max-width:62ch; margin:14px 0 8px; }
footer { margin-top:24px; color:var(--muted); font-size:13px; max-width:80ch; }

.scrim { position:fixed; inset:0; background:rgba(0,0,0,.32); z-index:29; }
.drawer { position:fixed; top:0; right:0; bottom:0; width:min(540px, 100%); background:var(--panel);
  border-left:1px solid var(--line); z-index:30; transform:translateX(100%); transition:transform .28s ease;
  box-shadow:var(--shadow); overflow-y:auto; visibility:hidden; }
.drawer.open { transform:none; visibility:visible; }
.drawer-inner { padding:22px 20px 48px; }
.close { position:absolute; top:10px; right:12px; font-size:28px; line-height:1; background:none; border:0;
  color:var(--muted); cursor:pointer; }
.drawer h2 { margin:0 0 2px; font-size:20px; letter-spacing:-.01em; padding-right:32px; }
.drawer h3 { font-size:12px; margin:18px 0 6px; text-transform:uppercase; letter-spacing:.06em; color:var(--muted);
  font-weight:600; }
.drawer p { margin:6px 0; font-size:14px; }
.drawer ul { margin:6px 0; padding-left:18px; font-size:13px; }
.kv { display:grid; grid-template-columns:max-content minmax(0,1fr); gap:3px 14px; font-size:13px; margin:8px 0; }
.kv dt { color:var(--muted); } .kv dd { margin:0; overflow-wrap:anywhere; }
.cite { display:grid; grid-template-columns:max-content minmax(0,1fr); gap:3px 10px; font-size:13px; margin:6px 0 0; }
.cite dt { font-family:ui-monospace, Menlo, monospace; color:var(--accent); }
.cite dd { margin:0; }
.hubs { width:100%; border-collapse:collapse; font-size:13px; }
.hubs th, .hubs td { text-align:left; padding:4px 6px; border-bottom:1px solid var(--line-2); vertical-align:top; }
.hubs th { color:var(--muted); font-weight:500; }
.tag-replay { display:inline-block; font-size:11px; font-weight:700; letter-spacing:.05em; text-transform:uppercase;
  padding:1px 6px; border-radius:5px; background:var(--warn-bg); border:1px solid var(--warn-line); }

@media (max-width: 820px) {
  .stats { grid-template-columns:repeat(2, minmax(0,1fr)); gap:8px; }
  .stat b { font-size:26px; }
  .who { grid-template-columns:1fr; }
  .eng { width:14px; height:14px; }
  .groups { gap:12px 16px; }
  .mrow { grid-template-columns:12px minmax(0,1fr); }
  .mrow .fig { grid-column:2; text-align:left; }
  .mrow .fig b { display:inline; margin-right:6px; }
  .row { grid-template-columns:minmax(0,1fr); }
  .replay-banner { position:static; flex-direction:column; gap:6px; }
  .seg button { padding:7px 9px; }
}
@media (prefers-reduced-motion: reduce) {
  .eng, .drawer { transition:none !important; animation:none !important; }
}
"""

SCRIPT = r"""
(() => {
  const DATA = JSON.parse(document.getElementById('fleet-data').textContent);
  const $ = id => document.getElementById(id);
  const esc = s => String(s ?? '').replace(/[&<>"']/g,
    c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const num = n => Number(n).toLocaleString('en-US');
  const REDUCED = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const Q = {potentially_affected:'Potentially affected', needs_review:'Needs review',
    no_action_or_not_applicable:'No action or not applicable'};
  const CLS = {potentially_affected:'pa', needs_review:'nr', no_action_or_not_applicable:'na'};
  const STR = i => i === null || i === undefined ? '' : DATA.strings[i];
  const STATES = DATA.states;
  const ENG = DATA.engines;
  const BY_ID = Object.fromEntries(ENG.map(e => [e.id, e]));
  const KIND = ['Day before', 'Effective date', 'Snapshot'];
  let state = DATA.default_state;
  const tiles = new Map();

  // A queue's tone in a state: before the directive is in force, no action
  // reads "not yet in force".
  const tone = (s, p) => !s.in_force && p.q === 'no_action_or_not_applicable' ? 'ny' : CLS[p.q];
  const toneLabel = (s, p) => tone(s, p) === 'ny' ? 'Not yet in force' : Q[p.q];

  // Date control ------------------------------------------------------------
  function renderSeg() {
    STATES.forEach((s, i) => {
      const b = document.createElement('button');
      b.type = 'button'; b.setAttribute('role', 'radio'); b.dataset.i = i;
      b.innerHTML = `<span class="k">${esc(KIND[i] || '')}</span><span class="v">${esc(s.label)}</span>`;
      b.addEventListener('click', () => go(i, true));
      b.addEventListener('keydown', ev => {
        const step = {ArrowRight:1, ArrowDown:1, ArrowLeft:-1, ArrowUp:-1}[ev.key];
        if (!step) return;
        ev.preventDefault();
        go(Math.max(0, Math.min(STATES.length - 1, state + step)), true);
        $('seg').children[state].focus();
      });
      $('seg').append(b);
    });
  }

  // Counters ----------------------------------------------------------------
  function renderStats() {
    const s = STATES[state], p = STATES[state - 1];
    const cell = (cls, n, before, label) => {
      let delta = '';
      if (p) {
        const d = n - before;
        delta = d === 0 ? `<span class="delta zero">no change since ${esc(p.label)}</span>`
          : `<span class="delta">${d > 0 ? '+' : '&minus;'}${num(Math.abs(d))} since ${esc(p.label)}</span>`;
      }
      return `<div class="stat ${cls}"><i></i><b>${num(n)}</b><span class="lab">${label}</span>${delta}</div>`;
    };
    const c = s.counts, b = p ? p.counts : {};
    const naCls = s.in_force ? 'na' : 'ny';
    const naLabel = s.in_force ? 'No action or not applicable' : 'No action: not yet in force';
    $('stats').innerHTML = cell('pa', c.potentially_affected, b.potentially_affected, 'Potentially affected')
      + cell('nr', c.needs_review, b.needs_review, 'Needs review')
      + cell(naCls, c.no_action_or_not_applicable, b.no_action_or_not_applicable, naLabel)
      + `<div class="stat out"><i></i><b>${num(ENG.filter(e => e.out).length)}</b><span class="lab">Not replayed</span></div>`;
  }

  // Fleet tiles -------------------------------------------------------------
  const family = t => (t || '').split('-')[1] || '';
  function tileLabel(e) {
    const s = STATES[state];
    const where = e.tail ? `${e.tail} position ${e.pos}` : '';
    if (e.out) return `${e.id}, ${e.model}, ${where}: not replayed`;
    return `${e.id}, ${e.model}, ${where}: ${toneLabel(s, e.st[s.key])} as of ${s.label}`;
  }
  function renderFleet() {
    const groups = new Map();
    for (const e of ENG) {
      const f = family(e.tail);
      if (!groups.has(f)) groups.set(f, new Map());
      const g = groups.get(f);
      if (!g.has(e.tail)) g.set(e.tail, []);
      g.get(e.tail).push(e);
    }
    for (const [f, aircraft] of groups) {
      const g = document.createElement('div'); g.className = 'group';
      g.innerHTML = `<h3>${esc(f)} &middot; ${aircraft.size} aircraft</h3><div class="ac-grid"></div>`;
      const grid = g.querySelector('.ac-grid');
      for (const [tail, engines] of aircraft) {
        const ac = document.createElement('div'); ac.className = 'ac'; ac.title = tail;
        for (const e of engines) {
          const b = document.createElement('button');
          b.type = 'button'; b.className = 'eng';
          if (e.out) {
            b.addEventListener('focus', () => showOut(e));
            b.addEventListener('mouseenter', () => showOut(e));
            b.addEventListener('click', () => showOut(e));
            b.addEventListener('blur', clearNote);
            b.addEventListener('mouseleave', clearNote);
          } else {
            b.addEventListener('click', () => openEngine(e));
          }
          tiles.set(e.id, b); ac.append(b);
        }
        grid.append(ac);
      }
      $('groups').append(g);
    }
  }
  function showOut(e) {
    $('tile-note').textContent = `${e.id} (${e.tail} position ${e.pos}) is not replayed. ${DATA.left_out_reason}`;
  }
  function clearNote() { $('tile-note').textContent = ''; }
  function paintTiles(animate) {
    const s = STATES[state];
    for (const e of ENG) {
      const b = tiles.get(e.id);
      if (e.out) { b.className = 'eng out'; b.setAttribute('aria-label', tileLabel(e)); continue; }
      const p = e.st[s.key];
      const named = !s.in_force && p.t !== null;
      b.className = 'eng ' + tone(s, p) + (named ? ' named' : '');
      b.setAttribute('aria-label', tileLabel(e));
      if (animate && !REDUCED && DATA.movers.includes(e.id)) {
        b.classList.remove('hit'); void b.offsetWidth; b.classList.add('hit');
      }
    }
    const replayed = ENG.filter(e => !e.out).length;
    $('fleet-sub').textContent = `${replayed} engines screened as of ${s.label}`
      + (s.replay ? ' (as-of replay)' : ' (fleet snapshot)')
      + `; ${ENG.length - replayed} not replayed`;
  }

  // Movers ------------------------------------------------------------------
  function paragraphs(p) {
    const seen = [];
    for (const i of p.c) { const par = DATA.cites[i].paragraph; if (!seen.includes(par)) seen.push(par); }
    return seen;
  }
  function renderMovers() {
    const s = STATES[state];
    const from = STATES[0], to = STATES[1];
    $('movers-sub').textContent = `${DATA.movers.length} engines change queue between ${from.label} and ${to.label}`
      + `; shown as screened on ${s.label}. Ordered by hub cycles remaining on ${to.label}, then needs review.`;
    const ol = $('movers'); ol.innerHTML = '';
    for (const id of DATA.movers) {
      const e = BY_ID[id], p = e.st[s.key];
      const t = tone(s, p);
      let fig = '';
      if (p.r !== null) fig += `<b>${num(p.r)}</b><span class="muted">hub cycles remain, as of ${esc(s.label)}</span>`;
      if (p.m.length) fig += `<span class="muted">Missing:</span>${p.m.map(m => `<code>${esc(m)}</code>`).join('')}`;
      const timing = p.r === null && p.t !== null ? `<span class="tim">${esc(STR(p.t))}</span>` : '';
      const li = document.createElement('li');
      li.innerHTML = `<button type="button" class="mrow"><span class="dot ${t}"></span>
        <span><span class="who"><span class="mono">${esc(e.id)}</span> <span class="muted">${esc(e.tail)} &middot; position ${e.pos}</span></span>
        <span class="q ${t}">${esc(toneLabel(s, p))}</span>
        <span class="sum">${esc(STR(p.s))}</span>${timing}
        <span class="par">Cites ${paragraphs(p).map(esc).join(' ')}</span></span>
        <span class="fig">${fig}</span></button>`;
      li.querySelector('button').addEventListener('click', () => openEngine(e));
      ol.append(li);
    }
  }

  // Fixtures ----------------------------------------------------------------
  function renderFixtures() {
    const grid = $('fixtures');
    for (const f of DATA.fixtures) {
      const b = document.createElement('button');
      b.type = 'button'; b.className = 'eng fx'; b.title = f.id;
      b.setAttribute('aria-label', `${f.id}, test fixture ${f.case}, screened as of ${f.as_of}`);
      b.addEventListener('click', () => openFixture(f));
      const ac = document.createElement('div'); ac.className = 'ac'; ac.append(b); grid.append(ac);
    }
  }

  // Sixteen-row strip ---------------------------------------------------------
  function renderStrip() {
    $('strip-n').textContent = DATA.screened_engines;
    $('strip-fixtures').textContent = DATA.fixture_count;
    $('strip-asof').textContent = DATA.snapshot;
    const box = $('rows');
    let sep = false;
    for (const d of DATA.strip) {
      if (!d.evaluated && !sep) {
        sep = true;
        const s = document.createElement('div'); s.className = 'sep';
        s.textContent = 'Not yet evaluated: screened and shown, cannot set a queue';
        box.append(s);
      }
      const q = d.queues, n = d.engines || 1;
      const seg = (cls, k) => q[k] ? `<i class="${cls}" style="width:${(q[k] / n * 100).toFixed(2)}%"></i>` : '';
      const status = d.evaluated ? '<span class="st ev">Evaluated: sets the queue</span>'
        : d.superseded ? '<span class="st">Superseded, not waiting</span>'
        : '<span class="st">Not yet evaluated</span>';
      let held = '';
      if (d.superseded) held = `<div class="held">${esc(d.superseded)}</div>`;
      else if (d.held.length) held = `<div class="held">Held by ${d.held.map(h =>
          `${esc(h.document)} (${num(h.engines)} engines)`).join(', ')}</div>
        <div class="caveat">These counts are mostly a product of the fleet's generation rules: generated
        engines carry the part numbers this directive names.</div>`;
      else if (d.facts.length) held = `<div class="held">Held by ${d.facts.map(f =>
          `${esc(f.kind)} <code>${esc(f.fact)}</code> (${num(f.engines)} engines)`).join(', ')}</div>`;
      const row = document.createElement('div');
      row.className = 'row' + (d.evaluated ? '' : ' nye') + (d.superseded ? ' sup' : '');
      row.innerHTML = `<div class="lab"><b>${esc(d.ad)}</b><span class="muted">Effective ${esc(d.effective)}</span><br>${status}</div>
        <div><div class="bar" role="img" aria-label="${esc(d.ad)}: ${q.potentially_affected} potentially affected, ${q.needs_review} needs review, ${q.no_action_or_not_applicable} no action or not applicable, of ${d.engines} engines">${
          seg('pa', 'potentially_affected')}${seg('nr', 'needs_review')}${seg('na', 'no_action_or_not_applicable')}</div>
        <div class="counts">${num(q.potentially_affected)} potentially affected &middot; ${num(q.needs_review)} needs review &middot; ${num(q.no_action_or_not_applicable)} no action or not applicable, of ${num(d.engines)} engines</div>
        ${held}</div>`;
      box.append(row);
    }
  }

  // Drawer ------------------------------------------------------------------
  const val = v => v === null || v === undefined ? '<span class="muted">not in the record</span>'
    : esc(typeof v === 'number' ? num(v) : v);
  function hubTable(hubs, asOf) {
    return `<table class="hubs"><thead><tr><th>Part</th><th>P/N</th><th>S/N</th><th>Cycles since new, as of ${esc(asOf)}</th></tr></thead><tbody>${
      hubs.map(h => `<tr><td>${esc(h.n)}</td><td class="mono">${val(h.pn)}</td><td class="mono">${val(h.sn)}</td><td class="mono">${val(h.csn)}</td></tr>`).join('')}</tbody></table>`;
  }
  function citeList(p) {
    return `<dl class="cite">${p.c.map(i => DATA.cites[i]).map(c => `<dt>${esc(DATA.ad_numbers[c.document] || c.document)} ${esc(c.paragraph)}</dt>
      <dd>${esc(c.supports)}${c.locator ? ` <span class="muted">(${esc(c.locator)})</span>` : ''}</dd>`).join('')}</dl>`;
  }
  function provenance() {
    const pv = DATA.directive.provenance;
    return pv ? `<dl class="kv">${Object.entries(pv).map(([k, v]) =>
      `<dt>${esc(k.replace(/_/g, ' '))}</dt><dd>${esc(v)}</dd>`).join('')}</dl>` : '';
  }
  function screenBlock(p, s) {
    const t = s ? tone(s, p) : CLS[p.q];
    const label = s ? toneLabel(s, p) : Q[p.q];
    return `<p><span class="q ${t}">${esc(label)}</span></p>
      <p>${esc(STR(p.s))}</p>
      ${p.t !== null ? `<h3>Timing</h3><p>${esc(STR(p.t))}</p>` : ''}
      ${p.m.length ? `<h3>Missing facts</h3><ul>${p.m.map(m => `<li><code>${esc(m)}</code></li>`).join('')}</ul>` : ''}
      <h3>Cited</h3>${citeList(p)}
      <h3>Review provenance, ${esc(DATA.directive.ad)}</h3>${provenance()}`;
  }
  let lastFocus = null;
  function openDrawer(html) {
    lastFocus = document.activeElement;
    $('detail').innerHTML = html;
    $('drawer').classList.add('open'); $('drawer').setAttribute('aria-hidden', 'false');
    $('scrim').hidden = false; $('close').focus();
  }
  function openEngine(e) {
    const s = STATES[state], p = e.st[s.key];
    openDrawer(`<p class="eyebrow">${esc(e.tail)} &middot; position ${e.pos}</p>
      <h2 id="d-title">${esc(e.id)} <span class="muted">${esc(e.model)}</span></h2>
      <dl class="kv"><dt>Engine S/N</dt><dd class="mono">${esc(e.esn)}</dd>
        <dt>Screened as of</dt><dd>${esc(s.label)} ${s.replay ? '<span class="tag-replay">As-of replay, not live</span>' : '(fleet snapshot)'}</dd>
        <dt>Directive</dt><dd>${esc(DATA.directive.ad)}, effective ${esc(DATA.directive.effective)}</dd></dl>
      <h3>Installed HPT hubs</h3>${hubTable(e.hubs[s.key], s.label)}
      <h3>${esc(DATA.directive.ad)}</h3>${screenBlock(p, s)}
      <p class="note">Screening tool, not a compliance determination.</p>`);
  }
  function openFixture(f) {
    openDrawer(`<p class="eyebrow">Test fixture &middot; ${esc(f.case)}</p>
      <h2 id="d-title">${esc(f.id)} <span class="muted">${esc(f.model)}</span></h2>
      <p class="muted">${esc(f.title)}</p>
      <dl class="kv"><dt>Engine S/N</dt><dd class="mono">${esc(f.esn)}</dd>
        <dt>Screened as of</dt><dd>${esc(f.as_of)} (its case date)</dd></dl>
      <h3>Installed HPT hubs</h3>${hubTable(f.hubs, f.as_of)}
      ${f.sc ? `<h3>${esc(DATA.directive.ad)}</h3>${screenBlock(f.sc, null)}` : ''}
      <p class="note">Screening tool, not a compliance determination.</p>`);
  }
  function closeDrawer() {
    if (!$('drawer').classList.contains('open')) return;
    $('drawer').classList.remove('open'); $('drawer').setAttribute('aria-hidden', 'true');
    $('scrim').hidden = true;
    if (lastFocus) lastFocus.focus();
  }
  $('close').addEventListener('click', closeDrawer);
  $('scrim').addEventListener('click', closeDrawer);
  document.addEventListener('keydown', ev => {
    if (!$('drawer').classList.contains('open')) return;
    if (ev.key === 'Escape') { closeDrawer(); return; }
    if (ev.key === 'Tab') {
      const items = [...$('drawer').querySelectorAll('button, a[href]')];
      const first = items[0], last = items[items.length - 1];
      if (ev.shiftKey && document.activeElement === first) { ev.preventDefault(); last.focus(); }
      else if (!ev.shiftKey && document.activeElement === last) { ev.preventDefault(); first.focus(); }
    }
  });

  // State -------------------------------------------------------------------
  function apply(animate) {
    const s = STATES[state];
    for (const b of $('seg').children) b.setAttribute('aria-checked', String(+b.dataset.i === state));
    $('status').textContent = `Screened as of ${s.label}` + (s.replay ? ', as-of replay' : ', fleet snapshot');
    renderStats(); paintTiles(animate); renderMovers();
  }
  function go(i, animate) { if (i === state) return; state = i; apply(animate); }
  let timer = null;
  $('play').addEventListener('click', () => {
    clearTimeout(timer);
    state = 0; apply(false);
    timer = setTimeout(() => { state = 1; apply(true); }, REDUCED ? 0 : 1400);
  });

  renderStrip();
  if (STATES.length) {
    renderSeg(); renderFleet(); renderFixtures(); apply(false);
  }
})();
"""
