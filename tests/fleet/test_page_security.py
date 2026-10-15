"""The fleet view's Content-Security-Policy (ROADMAP step 9)."""

import json
import re
from pathlib import Path

from faa_directive_impact.fleet.page import render_fleet_page

REPO = Path(__file__).resolve().parents[2]


def test_fleet_page_refuses_everything_but_its_own_inline_code():
    html = render_fleet_page(json.loads((REPO / "demo/fleet-screen.json").read_text()))

    [policy] = re.findall(
        r'<meta http-equiv="Content-Security-Policy" content="([^"]+)">', html
    )
    directives = dict(
        (part.split()[0], part.split()[1:]) for part in policy.split("; ")
    )
    assert directives["default-src"] == ["'none'"]
    # Inline code only: the page's script and style are allowed inline (see
    # operations/HARDENING.md for why not by hash); no other source is.
    assert directives["script-src"] == ["'unsafe-inline'"]
    assert directives["style-src"] == ["'unsafe-inline'"]
    assert directives["base-uri"] == ["'none'"]
    assert directives["form-action"] == ["'none'"]
    assert html.index("Content-Security-Policy") < html.index("<style>")
    # Nothing is loaded from elsewhere, so nothing else needs allowing.
    assert not re.search(r"<script[^>]+src=|<link[^>]+stylesheet|<img|@import", html)
