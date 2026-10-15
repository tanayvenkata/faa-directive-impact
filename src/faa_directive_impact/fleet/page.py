"""Render the fleet view: one static HTML page over the fleet screen.

Every engine is a tile in one of three queues, set by evaluated directives
only. Directives retrieved for an engine but not yet evaluated are shown
beside the queues and in each engine's detail, never inside a queue (ROADMAP,
"Directive Coverage State"). Nothing on the page is computed in the browser
beyond counting and layout; each queue, candidate, summary, timing, missing
fact, and citation comes from the recorded screen.

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
                "queue": engine["evaluated_queue"],
                "nye": engine["not_yet_evaluated"],
            }
        )
    return {
        "directives": fleet_screen["directives"],
        "evaluated": fleet_screen["evaluated_directive"],
        "counts": fleet_screen["evaluated_counts"],
        "corpus": fleet_screen["corpus_generation"],
        "engines": engines,
    }


TEMPLATE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Fleet Directive Screen</title>
<meta name="description" content="A synthetic V2500 fleet: each engine's airworthiness directives retrieved and screened.">
<style>__STYLE__</style>
</head>
<body>
<main>
  <p class="eyebrow">Synthetic V2500 fleet &middot; screening tool</p>
  <h1 id="headline">Which engines does a new directive touch?</h1>
  <p class="lede" id="lede"></p>

  <section class="stats" id="stats" aria-live="polite"></section>

  <section class="lanes" id="lanes"></section>

  <section class="legend" aria-label="Legend">
    <span><i class="sw q-potentially_affected"></i>Potentially affected</span>
    <span><i class="sw q-needs_review"></i>Needs review</span>
    <span><i class="sw q-no_action_or_not_applicable"></i>No action or not applicable</span>
    <span><i class="sw q-no_action_or_not_applicable nye"></i>A rule record not yet evaluated also flags it</span>
    <span><i class="sw q-no_action_or_not_applicable case"></i>Evaluation case</span>
  </section>

  <section aria-labelledby="dir-title">
    <h2 class="section" id="dir-title">Directives retrieved for this fleet</h2>
    <p class="muted small">Retrieval finds each engine's candidates by its model
    and installed part numbers. Only the evaluated directive sets the queues
    above; the rest are shown here for a person to act on.</p>
    <div class="table-wrap"><table class="dtable" id="directives"></table></div>
  </section>

  <footer>
    <p>__DISCLAIMER__</p>
    <p>Each tile is a recorded screen, not a browser calculation. Candidates come
    from the step 7 retriever over a frozen corpus (<code id="corpus"></code>);
    AD 2025-19-13 is screened by the evaluated rules baseline, AD 2026-17-03 by
    the rule interpreter on a reference rule record no person has confirmed.
    Evaluation-case engines are edge cases from the test suite, embedded as
    they are. Fleet <code>__FLEET_SHA__</code>.
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
.badge { display:inline-block; white-space:nowrap; font-size:11px; font-weight:600; letter-spacing:.04em;
  text-transform:uppercase; padding:2px 8px; border-radius:999px;
  border:1px solid currentColor; }
.badge.evaluated { color:var(--ok); }
.badge.not_yet_evaluated { color:var(--review); }

h2.section { font-size:18px; margin:8px 0 4px; }
.small { font-size:13px; }
.table-wrap { overflow-x:auto; background:var(--panel); border:1px solid var(--line);
  border-radius:14px; }
.dtable { width:100%; border-collapse:collapse; font-size:13px; }
.dtable th, .dtable td { text-align:left; padding:8px 10px; border-bottom:1px solid var(--line);
  vertical-align:top; }
.dtable th { color:var(--muted); font-weight:500; white-space:nowrap; }
.dtable td.num { font-variant-numeric:tabular-nums; white-space:nowrap; }
.dtable tr:last-child td { border-bottom:0; }
.nye-list { margin:6px 0; padding-left:18px; font-size:13px; }
.nye-list li { margin:4px 0; }
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
     'An evaluated directive applies and an action is due or waits on an event.'],
    ['needs_review', 'Needs review',
     'A fact the evaluated directive turns on is missing or unclear. A person decides.'],
    ['no_action_or_not_applicable', 'No action or not applicable',
     'Checked: no listed part, or the evaluated directive does not apply.'],
  ];
  const LABEL = Object.fromEntries(QUEUES.map(([k, l]) => [k, l]));
  const DIRECTIVES = Object.fromEntries(DATA.directives.map(d => [d.document, d]));
  const ENGINES = DATA.engines;
  const EVALUATED = DIRECTIVES[DATA.evaluated];
  const $ = id => document.getElementById(id);
  const esc = s => String(s ?? '').replace(/[&<>"']/g,
    c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const fmtDate = iso => iso ? new Date(iso + 'T00:00:00Z').toLocaleDateString('en-GB',
    {day:'numeric', month:'short', year:'numeric', timeZone:'UTC'}) : '';
  const name = d => d.ad_number || ('FR ' + d.document);
  const frLink = doc => `https://www.federalregister.gov/d/${encodeURIComponent(doc)}`;

  // A rule record that is not yet evaluated also flags the engine.
  const ruleFlag = e => e.nye.some(doc => e.screens[doc].screener === 'rules');

  function renderLanes() {
    const sorted = [...ENGINES].sort((a, b) => {
      const ka = (a.case ? '1' : '0') + (a.tail || '') + (a.position || '') + a.id;
      const kb = (b.case ? '1' : '0') + (b.tail || '') + (b.position || '') + b.id;
      return ka < kb ? -1 : 1;
    });
    for (const [key, label, blurb] of QUEUES) {
      const lane = document.createElement('div');
      lane.className = 'lane';
      lane.innerHTML = `<h2><span>${label}</span><span class="n">${DATA.counts[key]}</span></h2>
        <p>${blurb}</p><div class="tiles"></div>`;
      const box = lane.querySelector('.tiles');
      for (const engine of sorted.filter(e => e.queue === key)) {
        const t = document.createElement('button');
        t.type = 'button';
        t.className = 'tile q-' + key + (ruleFlag(engine) ? ' nye' : '')
          + (engine.case ? ' case' : '');
        t.setAttribute('aria-label', `${engine.id}, ${engine.model}, ${label}`);
        t.addEventListener('click', () => openDetail(engine, t));
        t.addEventListener('mouseenter', e => showTip(e, engine));
        t.addEventListener('mousemove', moveTip);
        t.addEventListener('mouseleave', hideTip);
        box.append(t);
      }
      $('lanes').append(lane);
    }
  }

  function renderStats() {
    const cell = (cls, n, label) =>
      `<div class="stat ${cls}"><b>${n}</b><span>${label}</span></div>`;
    $('stats').innerHTML = cell('', ENGINES.length, 'Engines in fleet')
      + QUEUES.map(([k, l]) => cell(k, DATA.counts[k], l)).join('');
  }

  function renderStory() {
    const touched = DATA.counts.potentially_affected + DATA.counts.needs_review;
    const nearest = ENGINES.filter(e => !e.case && e.screens[DATA.evaluated])
      .map(e => [e, e.screens[DATA.evaluated].computed.component_cycles_remaining])
      .filter(([, n]) => typeof n === 'number')
      .sort((a, b) => a[1] - b[1])[0];
    const others = DATA.directives.filter(d => d.coverage_state !== 'evaluated'
      && d.queues.needs_review + d.queues.potentially_affected > 0).length;
    $('headline').textContent = `${name(EVALUATED)} touches ${touched} of ${ENGINES.length} engines.`;
    const parts = [`It took effect on ${fmtDate(EVALUATED.effective_date)}:`
      + ` <b>${DATA.counts.potentially_affected}</b> engines are potentially affected and`
      + ` <b>${DATA.counts.needs_review}</b> need review.`];
    if (nearest) parts.push(`The nearest listed hub, on ${esc(nearest[0].id)}, is`
      + ` <b>${nearest[1].toLocaleString('en-US')} cycles</b> from its table 1 removal limit.`);
    parts.push(`Retrieval also found <b>${others}</b> other directives for this fleet`
      + ' that are not yet evaluated; they are listed below, outside the queues.');
    $('lede').innerHTML = parts.join(' ');
    $('corpus').textContent = DATA.corpus;
  }

  function renderDirectives() {
    const head = `<thead><tr><th>Directive</th><th>Coverage</th><th>Screened by</th>
      <th>Engines retrieved</th><th>By part number</th><th>Potentially affected</th>
      <th>Needs review</th><th>Superseded</th></tr></thead>`;
    const rows = DATA.directives.map(d => `<tr>
      <td><a href="${frLink(d.document)}">${esc(name(d))}</a><br>
        <span class="muted">Effective ${fmtDate(d.effective_date)}</span></td>
      <td><span class="badge ${d.coverage_state}">${d.coverage_state.replace(/_/g, ' ')}</span></td>
      <td>${esc(d.screener)}</td>
      <td class="num">${d.engines}</td><td class="num">${d.by_part_number}</td>
      <td class="num">${d.queues.potentially_affected}</td>
      <td class="num">${d.queues.needs_review}</td><td class="num">${d.superseded}</td></tr>`).join('');
    $('directives').innerHTML = head + '<tbody>' + rows + '</tbody>';
  }

  // Tooltip -------------------------------------------------------------
  function showTip(e, engine) {
    const tip = $('tip');
    tip.innerHTML = `<b>${esc(engine.id)}</b> &middot; ${esc(engine.model)}<br>`
      + (engine.tail ? `${esc(engine.tail)}, position ${engine.position}<br>` : '')
      + (engine.case ? `Evaluation case ${esc(engine.case.case_id)}<br>` : '')
      + `${LABEL[engine.queue]}; ${engine.nye.length} not yet evaluated`;
    tip.hidden = false;
    moveTip(e);
  }
  function moveTip(e) {
    const tip = $('tip');
    tip.style.left = Math.min(e.clientX + 14, innerWidth - tip.offsetWidth - 8) + 'px';
    tip.style.top = (e.clientY + 16) + 'px';
  }
  function hideTip() { $('tip').hidden = true; }

  // Detail drawer -------------------------------------------------------
  function value(v) {
    if (v === undefined || v === null) return '<span class="muted">&mdash;</span>';
    if (v === 'unknown') return '<span class="unknown">unknown</span>';
    return esc(typeof v === 'number' ? v.toLocaleString('en-US') : v);
  }
  function screenCard(doc, s) {
    const d = DIRECTIVES[doc];
    const cites = s.citations.map(c => `<li><a href="${frLink(c.document)}">${esc(c.document)}</a>
      paragraph ${esc(c.paragraph)}${c.locator ? ', ' + esc(c.locator) : ''}
      <span class="muted">(${esc(c.supports)})</span></li>`).join('');
    const missing = s.missing_facts.length ? `<p class="muted">Missing:</p><ul>${
      s.missing_facts.map(f => `<li><code>${esc(f)}</code></li>`).join('')}</ul>` : '';
    const notes = s.notes.length ? `<ul>${s.notes.map(n => `<li>${esc(n)}</li>`).join('')}</ul>` : '';
    return `<section class="sc"><header><b>${esc(name(d))}</b>
      <span class="badge ${d.coverage_state}">${d.coverage_state.replace(/_/g, ' ')}</span>
      <span class="q ${s.queue}">${LABEL[s.queue]}</span></header>
      <p>${esc(s.summary)}</p>${s.timing ? `<p>${esc(s.timing)}</p>` : ''}
      ${missing}${notes}${cites ? `<p class="muted">Cited:</p><ul>${cites}</ul>` : ''}</section>`;
  }
  let lastTile = null;
  function openDetail(engine, tile) {
    hideTip();
    lastTile = tile;
    const comps = engine.components.map(c => `<tr><td>${esc(c.component_name)}</td>
      <td>${value(c.part_number)}</td><td>${value(c.serial_number)}</td>
      <td>${value(c.cycles_since_new)}</td></tr>`).join('');
    const events = engine.events.map(ev => `<li>${esc(ev.event_type.replace(/_/g, ' '))}
      on ${esc(ev.at)}${ev.detail ? ': ' + esc(ev.detail) : ''}</li>`).join('');
    const evaluated = engine.screens[DATA.evaluated]
      ? screenCard(DATA.evaluated, engine.screens[DATA.evaluated])
      : `<p class="muted">${esc(name(EVALUATED))} was not retrieved for this engine.</p>`;
    const rules = engine.nye.filter(doc => engine.screens[doc].screener === 'rules');
    const unread = engine.nye.filter(doc => engine.screens[doc].screener !== 'rules');
    const superseded = Object.entries(engine.screens)
      .filter(([, s]) => s.applicability === 'superseded');
    const unreadList = unread.length ? `<p class="muted">No rule record yet; a person reads each:</p>
      <ul class="nye-list">${unread.map(doc => `<li><a href="${frLink(doc)}">${
        esc(name(DIRECTIVES[doc]))}</a>: ${esc(engine.screens[doc].summary)}</li>`).join('')}</ul>` : '';
    const supList = superseded.length ? `<p class="muted">Superseded: ${superseded.map(([doc, s]) =>
      `${esc(name(DIRECTIVES[doc]))} (${esc(s.summary)})`).join('; ')}</p>` : '';
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
      <h3>Evaluated</h3>${evaluated}
      <h3>Not yet evaluated (${engine.nye.length})</h3>
      ${rules.map(doc => screenCard(doc, engine.screens[doc])).join('')}
      ${unreadList}${supList}`;
    $('drawer').classList.add('open');
    $('drawer').setAttribute('aria-hidden', 'false');
    $('scrim').hidden = false;
    $('close').focus();
  }
  function closeDetail() {
    $('drawer').classList.remove('open');
    $('drawer').setAttribute('aria-hidden', 'true');
    $('scrim').hidden = true;
    if (lastTile) lastTile.focus();
  }
  $('close').addEventListener('click', closeDetail);
  $('scrim').addEventListener('click', closeDetail);
  addEventListener('keydown', e => { if (e.key === 'Escape') closeDetail(); });

  renderStory();
  renderStats();
  renderLanes();
  renderDirectives();
})();
"""
