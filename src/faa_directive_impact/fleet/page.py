"""Render the fleet view: one static HTML page over the fleet screen.

Every engine is a tile in one of three queues. The page replays the two
releases recorded by ``fleet.screen``: first AD 2025-19-13 alone, then with AD
2026-17-03 added, and the tiles move to their new queues. Nothing on the page is
computed in the browser beyond counting and layout; each queue, summary,
timing, missing fact, and citation comes from the recorded screen.

The page is a screening aid on a synthetic fleet. It carries no FAA logo or
branding.
"""

import json
from html import escape
from pathlib import Path
from typing import Any

FLEET_PAGE_DIRECTORY = "fleet"
REPOSITORY_URL = "https://github.com/tanayvenkata/faa-directive-impact"
WRITEUP_URL = f"{REPOSITORY_URL}/blob/main/writeups/02-evaluated.md"
DISCLAIMER = (
    "Screening tool, not a compliance determination. The fleet is synthetic. "
    "Nothing here is an operator's AD status record or a maintenance, "
    "airworthiness, or return-to-service decision. Always work from the "
    "directive itself."
)


def build_fleet_page(fleet_screen: dict[str, Any], site_root: Path) -> Path:
    """Write ``<site_root>/fleet/index.html`` and return its path."""
    directory = site_root / FLEET_PAGE_DIRECTORY
    directory.mkdir(parents=True, exist_ok=True)
    path = directory / "index.html"
    path.write_text(render_fleet_page(fleet_screen), encoding="utf-8")
    return path


def render_fleet_page(fleet_screen: dict[str, Any]) -> str:
    data = json.dumps(_page_data(fleet_screen), sort_keys=True, separators=(",", ":"))
    # Keep the embedded JSON from closing the script element early.
    data = data.replace("</", "<\\/")
    return (
        TEMPLATE.replace("__STYLE__", STYLE)
        .replace("__SCRIPT__", SCRIPT)
        .replace("__DATA__", data)
        .replace("__DISCLAIMER__", escape(DISCLAIMER))
        .replace("__REPO__", REPOSITORY_URL)
        .replace("__WRITEUP__", WRITEUP_URL)
        .replace("__FLEET_SHA__", fleet_screen["fleet_sha256"][:12])
    )


def _page_data(fleet_screen: dict[str, Any]) -> dict[str, Any]:
    engines = []
    for engine in fleet_screen["engines"]:
        asset = engine["asset"]
        identity = asset["engine"]
        engines.append(
            {
                "id": identity["asset_id"],
                "esn": identity["engine_serial_number"],
                "model": identity["engine_model"],
                "tail": identity.get("aircraft_tail_id"),
                "position": identity.get("installation_position"),
                "as_of": engine["as_of"],
                "case": asset.get("evaluation_case"),
                "components": asset["installed_components"],
                "events": asset.get("events", []),
                "screens": engine["screens"],
            }
        )
    return {
        "directives": fleet_screen["directives"],
        "releases": fleet_screen["releases"],
        "engines": engines,
    }


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; script-src 'unsafe-inline'; style-src 'unsafe-inline'; base-uri 'none'; form-action 'none'">
<title>Fleet Directive Screen</title>
<meta name="description" content="A synthetic V2500 fleet screened against two airworthiness directives, replayed release by release.">
<style>__STYLE__</style>
</head>
<body>
<main>
  <p class="eyebrow">Synthetic V2500 fleet &middot; screening tool</p>
  <h1 id="headline">Which engines does a new directive touch?</h1>
  <p class="lede" id="lede"></p>

  <section class="controls" aria-label="Release">
    <div class="steps" role="tablist">
      <button type="button" role="tab" data-release="r1" id="tab-r1">
        <span class="step-n">Release 1</span>
        <span class="step-l">AD 2025-19-13</span>
      </button>
      <span class="arrow" aria-hidden="true">&rarr;</span>
      <button type="button" role="tab" data-release="r2" id="tab-r2">
        <span class="step-n">Release 2</span>
        <span class="step-l">+ AD 2026-17-03</span>
      </button>
    </div>
    <button type="button" class="replay" id="replay">&#9654; Replay</button>
  </section>

  <section class="stats" id="stats" aria-live="polite"></section>

  <section class="lanes" id="lanes"></section>

  <section class="legend" aria-label="Legend">
    <span><i class="sw q-potentially_affected"></i>Potentially affected</span>
    <span><i class="sw q-needs_review"></i>Needs review</span>
    <span><i class="sw q-no_action_or_not_applicable"></i>No action or not applicable</span>
    <span><i class="sw q-potentially_affected nye"></i>Placed by a directive not yet evaluated</span>
    <span><i class="sw q-no_action_or_not_applicable case"></i>Evaluation case</span>
  </section>

  <section class="directives" id="directives"></section>

  <footer>
    <p>__DISCLAIMER__</p>
    <p>Each tile is a recorded screen, not a browser calculation: AD 2025-19-13
    by the evaluated rules baseline, AD 2026-17-03 by the rule interpreter on a
    reference rule record that no person has confirmed. Evaluation-case
    engines are edge cases from the test suite, embedded as they are. Fleet
    <code>__FLEET_SHA__</code>.
    <a href="../">Directive freshness</a> &middot;
    <a href="__WRITEUP__">How it was evaluated</a> &middot;
    <a href="__REPO__">Source</a></p>
  </footer>
</main>

<div class="tip" id="tip" role="tooltip" hidden></div>
<aside class="drawer" id="drawer" aria-hidden="true" aria-labelledby="d-title">
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
  --bg:#f7f6f2; --panel:#ffffff; --fg:#1b1c1e; --muted:#62656b; --line:#dcdad3;
  --affected:#d2492a; --review:#d99a1e; --clear:#c9ccc4; --clear-ink:#7c8077;
  --accent:#1f4fd1; --ok:#2f7a45; --ring:#1b1c1e; --shadow:0 12px 40px rgba(20,20,20,.18);
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg:#121315; --panel:#1b1d20; --fg:#ecebe6; --muted:#9a9ca1; --line:#2e3135;
    --affected:#f06a48; --review:#f0b43c; --clear:#3a3d41; --clear-ink:#8d9096;
    --accent:#8fb0ff; --ok:#8fd19e; --ring:#ecebe6; --shadow:0 12px 40px rgba(0,0,0,.5);
  }
}
:root[data-theme="dark"] {
  --bg:#121315; --panel:#1b1d20; --fg:#ecebe6; --muted:#9a9ca1; --line:#2e3135;
  --affected:#f06a48; --review:#f0b43c; --clear:#3a3d41; --clear-ink:#8d9096;
  --accent:#8fb0ff; --ok:#8fd19e; --ring:#ecebe6; --shadow:0 12px 40px rgba(0,0,0,.5);
}
* { box-sizing: border-box; }
html { -webkit-text-size-adjust: 100%; }
body { margin:0; background:var(--bg); color:var(--fg);
  font:15px/1.5 ui-sans-serif, system-ui, -apple-system, "Segoe UI", sans-serif; }
main { max-width:1180px; margin:0 auto; padding:32px 16px 56px; }
a { color:var(--accent); }
code { font:12px/1.4 ui-monospace, SFMono-Regular, Menlo, monospace; }
.muted { color:var(--muted); }
.eyebrow { margin:0; font-size:12px; letter-spacing:.08em; text-transform:uppercase;
  color:var(--muted); }
h1 { font-size:clamp(26px, 4.2vw, 42px); line-height:1.1; margin:8px 0 10px;
  letter-spacing:-.02em; max-width:22ch; }
.lede { margin:0 0 24px; color:var(--muted); max-width:62ch; font-size:16px; }
.lede b { color:var(--fg); }

.controls { display:flex; flex-wrap:wrap; gap:12px; align-items:center;
  justify-content:space-between; margin-bottom:18px; }
.steps { display:flex; align-items:center; gap:8px; flex-wrap:wrap; }
.steps button { font:inherit; color:inherit; background:var(--panel);
  border:1px solid var(--line); border-radius:10px; padding:8px 14px; cursor:pointer;
  text-align:left; display:flex; flex-direction:column; min-width:150px; }
.steps button[aria-selected="true"] { border-color:var(--fg);
  box-shadow:inset 0 0 0 1px var(--fg); }
.step-n { font-size:11px; text-transform:uppercase; letter-spacing:.06em;
  color:var(--muted); }
.step-l { font-weight:600; }
.arrow { color:var(--muted); }
.replay { font:inherit; font-weight:600; border:0; border-radius:999px;
  padding:9px 18px; background:var(--fg); color:var(--bg); cursor:pointer; }

.stats { display:grid; grid-template-columns:repeat(4, minmax(0,1fr)); gap:10px;
  margin-bottom:18px; }
.stat { background:var(--panel); border:1px solid var(--line); border-radius:12px;
  padding:12px 14px; }
.stat b { display:block; font-size:clamp(22px, 3.4vw, 32px); line-height:1.1;
  font-variant-numeric:tabular-nums; }
.stat span { color:var(--muted); font-size:13px; }
.stat .delta { font-size:13px; font-weight:600; margin-left:6px; }
.stat.potentially_affected b { color:var(--affected); }
.stat.needs_review b { color:var(--review); }

.lanes { display:grid; grid-template-columns:repeat(3, minmax(0,1fr)); gap:12px; }
.lane { background:var(--panel); border:1px solid var(--line); border-radius:14px;
  padding:14px; min-height:220px; }
.lane h2 { margin:0 0 2px; font-size:15px; display:flex; justify-content:space-between;
  gap:8px; }
.lane h2 .n { font-variant-numeric:tabular-nums; color:var(--muted); font-weight:500; }
.lane p { margin:0 0 12px; color:var(--muted); font-size:13px; }
.tiles { display:flex; flex-wrap:wrap; gap:4px; align-content:flex-start; }
.tile { width:18px; height:18px; border-radius:4px; border:0; padding:0;
  cursor:pointer; position:relative; will-change:transform; }
.tile:focus-visible { outline:2px solid var(--accent); outline-offset:2px; }
.q-potentially_affected { background:var(--affected); }
.q-needs_review { background:var(--review); }
.q-no_action_or_not_applicable { background:var(--clear); }
.nye { background-image:repeating-linear-gradient(135deg,
  rgba(255,255,255,.55) 0 2px, transparent 2px 5px); }
.case { box-shadow:0 0 0 2px var(--bg), 0 0 0 3.5px var(--ring); }
.tile.moved { animation:pulse 1.4s ease-out 1; }
@keyframes pulse { 0% { filter:brightness(1.6); } 100% { filter:none; } }

.legend { display:flex; flex-wrap:wrap; gap:8px 18px; margin:14px 2px 28px;
  color:var(--muted); font-size:13px; }
.legend span { display:inline-flex; align-items:center; gap:7px; }
.sw { width:14px; height:14px; border-radius:3px; display:inline-block; }

.directives { display:grid; grid-template-columns:repeat(2, minmax(0,1fr)); gap:12px; }
.dcard { background:var(--panel); border:1px solid var(--line); border-radius:14px;
  padding:14px 16px; }
.dcard h3 { margin:0 0 4px; font-size:16px; }
.dcard p { margin:4px 0; font-size:14px; color:var(--muted); }
.badge { display:inline-block; font-size:11px; font-weight:600; letter-spacing:.04em;
  text-transform:uppercase; padding:2px 8px; border-radius:999px;
  border:1px solid currentColor; }
.badge.evaluated { color:var(--ok); }
.badge.not_yet_evaluated { color:var(--review); }

footer { margin-top:36px; color:var(--muted); font-size:13px; max-width:80ch; }

.tip { position:fixed; z-index:20; pointer-events:none; background:var(--fg);
  color:var(--bg); font-size:12px; padding:6px 9px; border-radius:6px;
  max-width:260px; }

.scrim { position:fixed; inset:0; background:rgba(0,0,0,.28); z-index:29; }
.drawer { position:fixed; top:0; right:0; bottom:0; width:min(520px, 100%);
  background:var(--panel); border-left:1px solid var(--line); z-index:30;
  transform:translateX(100%); transition:transform .28s ease; box-shadow:var(--shadow);
  overflow-y:auto; }
.drawer.open { transform:none; }
.drawer-inner { padding:22px 20px 40px; }
.close { position:absolute; top:10px; right:12px; font-size:26px; line-height:1;
  background:none; border:0; color:var(--muted); cursor:pointer; }
.drawer h2 { margin:0 0 2px; font-size:20px; }
.drawer h3 { font-size:14px; margin:20px 0 6px; }
.kv { display:grid; grid-template-columns:max-content 1fr; gap:2px 14px; font-size:13px;
  margin:8px 0; }
.kv dt { color:var(--muted); } .kv dd { margin:0; overflow-wrap:anywhere; }
.comp { width:100%; border-collapse:collapse; font-size:13px; }
.comp th, .comp td { text-align:left; padding:5px 6px; border-bottom:1px solid var(--line);
  vertical-align:top; }
.comp th { color:var(--muted); font-weight:500; }
.unknown { color:var(--review); font-weight:600; }
.sc { border:1px solid var(--line); border-radius:12px; padding:12px 14px; margin:10px 0; }
.sc header { display:flex; justify-content:space-between; gap:8px; align-items:center;
  flex-wrap:wrap; }
.sc .q { font-size:12px; font-weight:600; padding:2px 8px; border-radius:6px; }
.sc .q.potentially_affected { background:var(--affected); color:#fff; }
.sc .q.needs_review { background:var(--review); color:#1b1c1e; }
.sc .q.no_action_or_not_applicable { background:var(--clear); color:var(--fg); }
.sc p { margin:8px 0; font-size:14px; }
.sc ul { margin:6px 0; padding-left:18px; font-size:13px; }
.sc .muted { color:var(--muted); font-size:13px; }

@media (max-width: 760px) {
  .stats { grid-template-columns:repeat(2, minmax(0,1fr)); }
  .lanes, .directives { grid-template-columns:1fr; }
  .steps button { min-width:0; }
}
@media (prefers-reduced-motion: reduce) {
  .tile, .drawer { transition:none !important; animation:none !important; }
}
"""

SCRIPT = r"""
(() => {
  const DATA = JSON.parse(document.getElementById('fleet-data').textContent);
  const QUEUES = [
    ['potentially_affected', 'Potentially affected',
     'A directive applies and an action is due or waits on an event.'],
    ['needs_review', 'Needs review',
     'A fact the directive turns on is missing or unclear. A person decides.'],
    ['no_action_or_not_applicable', 'No action or not applicable',
     'Checked: no listed part, or outside the directive.'],
  ];
  const LABEL = Object.fromEntries(QUEUES.map(([k, l]) => [k, l]));
  const ORDER = QUEUES.map(([k]) => k);
  const DIRECTIVES = Object.fromEntries(DATA.directives.map(d => [d.document, d]));
  const RELEASES = Object.fromEntries(DATA.releases.map(r => [r.release_id, r]));
  const ENGINES = DATA.engines;
  const reduce = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const $ = id => document.getElementById(id);
  const esc = s => String(s ?? '').replace(/[&<>"']/g,
    c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const fmtDate = iso => new Date(iso + 'T00:00:00Z').toLocaleDateString('en-GB',
    {day:'numeric', month:'short', year:'numeric', timeZone:'UTC'});

  let current = null;

  // Lanes and tiles are built once; switching releases moves the same nodes.
  const lanes = {};
  for (const [key, label, blurb] of QUEUES) {
    const lane = document.createElement('div');
    lane.className = 'lane';
    lane.innerHTML = `<h2><span>${label}</span><span class="n"></span></h2>
      <p>${blurb}</p><div class="tiles"></div>`;
    $('lanes').append(lane);
    lanes[key] = {count: lane.querySelector('.n'), tiles: lane.querySelector('.tiles')};
  }
  const tiles = {};
  for (const engine of ENGINES) {
    const t = document.createElement('button');
    t.type = 'button';
    t.className = 'tile';
    t.dataset.id = engine.id;
    t.setAttribute('aria-label', `${engine.id}, ${engine.model}`);
    t.addEventListener('click', () => openDetail(engine));
    t.addEventListener('mouseenter', e => showTip(e, engine));
    t.addEventListener('mousemove', moveTip);
    t.addEventListener('mouseleave', hideTip);
    tiles[engine.id] = t;
  }

  // Which directive put the engine in its queue under a release.
  function driver(engine, release) {
    const q = release.queues[engine.id];
    return release.directives.find(d => engine.screens[d].queue === q);
  }

  function sortKey(engine) {
    return (engine.case ? '1' : '0') + (engine.tail || '') + (engine.position || '')
      + engine.id;
  }

  function render(releaseId, animate) {
    const release = RELEASES[releaseId];
    const previous = current && RELEASES[current];
    const first = {};
    if (animate) for (const [id, t] of Object.entries(tiles))
      first[id] = t.getBoundingClientRect();

    const ordered = [...ENGINES].sort((a, b) => sortKey(a) < sortKey(b) ? -1 : 1);
    for (const key of ORDER) lanes[key].tiles.replaceChildren();
    for (const engine of ordered) {
      const q = release.queues[engine.id];
      const t = tiles[engine.id];
      const by = DIRECTIVES[driver(engine, release)];
      t.className = 'tile q-' + q
        + (by && by.coverage_state !== 'evaluated' && q !== 'no_action_or_not_applicable'
           ? ' nye' : '')
        + (engine.case ? ' case' : '');
      lanes[q].tiles.append(t);
    }
    for (const key of ORDER) lanes[key].count.textContent = release.counts[key];

    if (animate && !reduce) {
      let i = 0;
      for (const engine of ordered) {
        const t = tiles[engine.id], a = first[engine.id], b = t.getBoundingClientRect();
        const dx = a.left - b.left, dy = a.top - b.top;
        const moved = previous && previous.queues[engine.id] !== release.queues[engine.id];
        if (!dx && !dy) continue;
        t.animate([{transform: `translate(${dx}px, ${dy}px)`}, {transform: 'none'}],
          {duration: moved ? 1100 : 600, delay: moved ? 120 + (i++ % 60) * 14 : 0,
           easing: 'cubic-bezier(.2,.7,.2,1)', fill: 'backwards'});
        if (moved) { t.classList.remove('moved'); void t.offsetWidth; t.classList.add('moved'); }
      }
    }
    current = releaseId;
    for (const id of ['r1', 'r2'])
      $('tab-' + id).setAttribute('aria-selected', String(id === releaseId));
    renderStats(release, previous);
    renderStory(release, previous);
  }

  function renderStats(release, previous) {
    const total = ENGINES.length;
    const cell = (cls, n, label, prev) => {
      const d = prev == null ? 0 : n - prev;
      const delta = d ? `<span class="delta">${d > 0 ? '+' : ''}${d}</span>` : '';
      return `<div class="stat ${cls}"><b>${n}${delta}</b><span>${label}</span></div>`;
    };
    const p = previous ? previous.counts : {};
    $('stats').innerHTML = cell('', total, 'Engines in fleet')
      + ORDER.map(k => cell(k, release.counts[k], LABEL[k], previous ? p[k] : null)).join('');
  }

  function renderStory(release, previous) {
    const added = release.directives.filter(d => !(previous || {directives: []})
      .directives.includes(d));
    const last = DIRECTIVES[release.directives[release.directives.length - 1]];
    const touched = ENGINES.filter(e => e.screens[last.document].queue
      !== 'no_action_or_not_applicable').length;
    const moved = previous ? ENGINES.filter(e =>
      previous.queues[e.id] !== release.queues[e.id]).length : null;
    $('headline').textContent = `${last.ad_number} took effect on ${fmtDate(last.effective_date)}.`;
    const parts = [`It touches <b>${touched}</b> of ${ENGINES.length} engines`
      + ` in this synthetic fleet: potentially affected or needing review.`];
    if (moved != null && added.length)
      parts.push(`Adding it moved <b>${moved}</b> engines to a new queue.`);
    if (last.coverage_state !== 'evaluated') {
      parts.push('Its action waits on the next shop visit that exposes a blade.');
      parts.push('This directive is <b>not yet evaluated</b>: its tiles are striped.');
    } else {
      const nearest = ENGINES.filter(e => !e.case)
        .map(e => [e, e.screens[last.document].computed.component_cycles_remaining])
        .filter(([, n]) => typeof n === 'number')
        .sort((a, b) => a[1] - b[1])[0];
      if (nearest) parts.push(`The nearest listed hub, on ${esc(nearest[0].id)}, is`
        + ` <b>${nearest[1].toLocaleString('en-US')} cycles</b> from its table 1 removal limit.`);
      parts.push('Its rules passed every frozen gate on 18 evaluation units;'
        + ' the two hand-checked gates were judged by Claude only.');
    }
    $('lede').innerHTML = parts.join(' ');
  }

  function renderDirectives() {
    $('directives').innerHTML = DATA.directives.map(d => `
      <article class="dcard">
        <span class="badge ${d.coverage_state}">${d.coverage_state.replace(/_/g, ' ')}</span>
        <h3>${esc(d.ad_number)}</h3>
        <p>Effective ${fmtDate(d.effective_date)} &middot; Federal Register
          <a href="https://www.federalregister.gov/d/${esc(d.document)}">${esc(d.document)}</a></p>
        <p>Screened by ${esc(d.screener)}.</p>
      </article>`).join('');
  }

  // Tooltip -------------------------------------------------------------
  function showTip(e, engine) {
    const tip = $('tip');
    const q = RELEASES[current].queues[engine.id];
    tip.innerHTML = `<b>${esc(engine.id)}</b> &middot; ${esc(engine.model)}<br>`
      + (engine.tail ? `${esc(engine.tail)}, position ${engine.position}<br>` : '')
      + (engine.case ? `Evaluation case ${esc(engine.case.case_id)}<br>` : '')
      + LABEL[q];
    tip.hidden = false;
    moveTip(e);
  }
  function moveTip(e) {
    const tip = $('tip');
    const x = Math.min(e.clientX + 14, innerWidth - tip.offsetWidth - 8);
    tip.style.left = x + 'px';
    tip.style.top = (e.clientY + 16) + 'px';
  }
  function hideTip() { $('tip').hidden = true; }

  // Detail drawer -------------------------------------------------------
  function value(v) {
    if (v === undefined || v === null) return '<span class="muted">&mdash;</span>';
    if (v === 'unknown') return '<span class="unknown">unknown</span>';
    return esc(typeof v === 'number' ? v.toLocaleString('en-US') : v);
  }
  function openDetail(engine) {
    hideTip();
    const release = RELEASES[current];
    const comps = engine.components.map(c => `<tr><td>${esc(c.component_name)}</td>
      <td>${value(c.part_number)}</td><td>${value(c.serial_number)}</td>
      <td>${value(c.cycles_since_new)}</td></tr>`).join('');
    const events = engine.events.map(ev => `<li>${esc(ev.event_type.replace(/_/g, ' '))}
      on ${esc(ev.at)}${ev.detail ? ': ' + esc(ev.detail) : ''}</li>`).join('');
    const screens = release.directives.map(doc => {
      const s = engine.screens[doc], d = DIRECTIVES[doc];
      const cites = s.citations.map(c => `<li><a href="https://www.federalregister.gov/d/${esc(c.document)}">${esc(c.document)}</a>
        paragraph ${esc(c.paragraph)}${c.locator ? ', ' + esc(c.locator) : ''}
        <span class="muted">(${esc(c.supports)})</span></li>`).join('');
      const missing = s.missing_facts.length ? `<p class="muted">Missing:</p><ul>${
        s.missing_facts.map(f => `<li><code>${esc(f)}</code></li>`).join('')}</ul>` : '';
      const notes = s.notes.length ? `<ul>${s.notes.map(n => `<li>${esc(n)}</li>`).join('')}</ul>` : '';
      return `<section class="sc"><header><b>${esc(d.ad_number)}</b>
        <span class="badge ${d.coverage_state}">${d.coverage_state.replace(/_/g, ' ')}</span>
        <span class="q ${s.queue}">${LABEL[s.queue]}</span></header>
        <p>${esc(s.summary)}</p>${s.timing ? `<p>${esc(s.timing)}</p>` : ''}
        ${missing}${notes}<p class="muted">Cited:</p><ul>${cites}</ul></section>`;
    }).join('');
    $('detail').innerHTML = `
      <p class="eyebrow">${engine.case ? 'Evaluation case ' + esc(engine.case.case_id) : 'Synthetic engine'}</p>
      <h2 id="d-title">${esc(engine.id)}</h2>
      ${engine.case ? `<p class="muted">${esc(engine.case.title)}</p>` : ''}
      <dl class="kv"><dt>Model</dt><dd>${esc(engine.model)}</dd>
        <dt>Engine S/N</dt><dd>${esc(engine.esn)}</dd>
        ${engine.tail ? `<dt>Aircraft</dt><dd>${esc(engine.tail)}, position ${engine.position}</dd>` : ''}
        <dt>Screened as of</dt><dd>${esc(engine.as_of)}</dd></dl>
      <h3>Installed components</h3>
      <table class="comp"><thead><tr><th>Component</th><th>P/N</th><th>S/N</th>
        <th>Cycles since new</th></tr></thead><tbody>${comps}</tbody></table>
      ${events ? `<h3>Recent events</h3><ul>${events}</ul>` : ''}
      <h3>Screens in ${esc(release.label)}</h3>${screens}`;
    $('drawer').classList.add('open');
    $('drawer').setAttribute('aria-hidden', 'false');
    $('scrim').hidden = false;
    $('close').focus();
    lastTile = tiles[engine.id];
  }
  let lastTile = null;
  function closeDetail() {
    $('drawer').classList.remove('open');
    $('drawer').setAttribute('aria-hidden', 'true');
    $('scrim').hidden = true;
    if (lastTile) lastTile.focus();
  }
  $('close').addEventListener('click', closeDetail);
  $('scrim').addEventListener('click', closeDetail);
  addEventListener('keydown', e => { if (e.key === 'Escape') closeDetail(); });

  // Controls ------------------------------------------------------------
  for (const id of ['r1', 'r2'])
    $('tab-' + id).addEventListener('click', () => {
      if (current !== id) render(id, true);
      history.replaceState(null, '', '#' + id);
    });
  let timer = null;
  function replay() {
    clearTimeout(timer);
    render('r1', current !== 'r1');
    timer = setTimeout(() => render('r2', true), 1800);
  }
  $('replay').addEventListener('click', replay);

  renderDirectives();
  // Play the release change once on arrival, unless a release is linked
  // directly or motion is reduced. ?autoplay holds release 1 longer (video).
  const hold = new URLSearchParams(location.search).has('autoplay') ? 2500 : 1200;
  if (location.hash === '#r1' || location.hash === '#r2' || reduce) {
    render(location.hash === '#r1' ? 'r1' : 'r2', false);
  } else {
    render('r1', false);
    timer = setTimeout(() => render('r2', true), hold);
  }
})();
"""
