---
name: site-capture
description: Screenshot, check, and record this project's static pages (the freshness page, the fleet view under site/fleet/, any page built into site/). Captures light, dark, and phone screenshots, reports console errors and horizontal overflow, and records a cropped 1280x720 MP4 clip for demos. Use this whenever you change a page generator (discovery/site.py, fleet/page.py), before opening a PR that touches the site, or when the user wants a screenshot, demo clip, launch video footage, or a visual for a write-up, resume, or website, even if they don't say "screenshot".
---

# Site Capture

Pages in this repo are static HTML built offline, so a change can pass every
test and still look broken. Look at it before calling the work done.

## Build the page

Build into the scratchpad, not `site/`, so the working tree stays clean:

```bash
uv run faa-directive-impact fleet-site --output <scratch>/site      # fleet view
uv run faa-directive-impact discovery-site --output <scratch>/site  # freshness (needs data/discovery)
```

## Capture

```bash
node .claude/skills/site-capture/scripts/capture.js <scratch>/site/fleet/index.html <scratch>/shots
```

It prints JSON per viewport: the screenshot path, console `errors`, and
`horizontalOverflow`. Treat any error or overflow as a bug to fix. Then read
the PNGs; the tool output only proves the page loaded, not that it reads well.
Check dark mode contrast in particular, since tokens get missed there.

For a demo clip, add `--video SECONDS`, optionally `--query autoplay` (the
fleet view holds release 1 longer for video) and `--click SELECTOR` to open
something near the end (e.g. `'.tile.q-potentially_affected.nye'` opens an
engine). Output is `clip.mp4` at 1280x720. Pull a frame to check it:
`ffmpeg -ss 4 -i clip.mp4 -frames:v 1 frame.png`.

## Why the script exists

- It reuses the Playwright and Chromium already installed by the
  playwright plugin, so nothing downloads. If it can't find them, set
  `PLAYWRIGHT_MODULE` and `CHROMIUM_PATH`.
- Recorded frames from Chrome for Testing leave a gray band at the bottom;
  the script records at 1280x810 and crops, which is why clips are 720 high.

## Claims on screen

What a page says is a public claim. Keep the wording consistent with
`writeups/02-evaluated.md` and `writeups/03-full-coverage.md`: two directives
are evaluated (AD 2025-19-13 on hand-written rules, AD 2020-07-51 on a model
draft with a Claude stand-in review), hand-checked gates were judged by
Claude only, any replay is an as-of replay and not a live event, and the page
is a screening tool, not a compliance determination. Send finished clips or screenshots to
the user with SendUserFile.
