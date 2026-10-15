#!/usr/bin/env node
// Capture a static page: screenshots (light, dark, phone) with a console and
// overflow check, and optionally a cropped MP4 clip.
//
// Usage:
//   node capture.js <url-or-file> <outdir> [--video SECONDS] [--click SELECTOR]
//                   [--query STRING]
//
// Finds Playwright and a Chromium build already on this machine, so nothing
// is downloaded. Override with PLAYWRIGHT_MODULE and CHROMIUM_PATH.
const fs = require('fs');
const os = require('os');
const path = require('path');
const { execFileSync } = require('child_process');

function findPlaywright() {
  if (process.env.PLAYWRIGHT_MODULE) return process.env.PLAYWRIGHT_MODULE;
  const roots = [path.join(os.homedir(), '.claude/plugins/cache')];
  for (const root of roots) {
    const stack = [[root, 0]];
    while (stack.length) {
      const [dir, depth] = stack.pop();
      const candidate = path.join(dir, 'node_modules/playwright');
      if (fs.existsSync(path.join(candidate, 'package.json'))) return candidate;
      if (depth > 6) continue;
      let entries = [];
      try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { continue; }
      for (const e of entries)
        if (e.isDirectory() && e.name !== 'node_modules' && !e.name.startsWith('.'))
          stack.push([path.join(dir, e.name), depth + 1]);
    }
  }
  try { return require.resolve('playwright'); } catch {}
  throw new Error('Playwright not found; set PLAYWRIGHT_MODULE.');
}

function findChromium() {
  if (process.env.CHROMIUM_PATH) return process.env.CHROMIUM_PATH;
  const cache = path.join(os.homedir(), 'Library/Caches/ms-playwright');
  const builds = fs.existsSync(cache)
    ? fs.readdirSync(cache).filter(n => /^chromium-\d+$/.test(n)).sort().reverse() : [];
  for (const b of builds) {
    const exe = path.join(cache, b,
      'chrome-mac-arm64/Google Chrome for Testing.app/Contents/MacOS/Google Chrome for Testing');
    if (fs.existsSync(exe)) return exe;
  }
  return undefined; // Let Playwright use its own default.
}

const args = process.argv.slice(2);
const opt = name => { const i = args.indexOf(name); return i >= 0 ? args[i + 1] : undefined; };
const [target, outdir] = args.filter((a, i) => !a.startsWith('--')
  && !(i > 0 && args[i - 1].startsWith('--')));
if (!target || !outdir) {
  console.error('usage: capture.js <url-or-file> <outdir> [--video S] [--click SEL] [--query Q]');
  process.exit(2);
}
const url = /^[a-z]+:/.test(target) ? target : 'file://' + path.resolve(target);
const query = opt('--query');
const withQuery = query ? url + (url.includes('?') ? '&' : '?') + query : url;
fs.mkdirSync(outdir, { recursive: true });

(async () => {
  const { chromium } = require(findPlaywright());
  const browser = await chromium.launch({ executablePath: findChromium() });
  const report = {};
  for (const [name, width, height, scheme] of [
    ['desktop-light', 1280, 900, 'light'],
    ['desktop-dark', 1280, 900, 'dark'],
    ['phone', 390, 844, 'light'],
  ]) {
    const page = await browser.newPage({ viewport: { width, height }, colorScheme: scheme });
    const errors = [];
    page.on('pageerror', e => errors.push(e.message));
    page.on('console', m => { if (m.type() === 'error') errors.push(m.text()); });
    await page.goto(url);
    await page.waitForTimeout(2500); // Let on-load animation settle.
    const file = path.join(outdir, name + '.png');
    await page.screenshot({ path: file, fullPage: true });
    const scrollWidth = await page.evaluate(() => document.documentElement.scrollWidth);
    report[name] = { file, errors, horizontalOverflow: scrollWidth > width };
    await page.close();
  }

  const seconds = Number(opt('--video') || 0);
  if (seconds) {
    // Headful Chrome for Testing leaves an unpainted band at the bottom of
    // recorded frames, so record taller than needed and crop to 1280x720.
    const raw = path.join(outdir, 'video-raw');
    const context = await browser.newContext({
      viewport: { width: 1280, height: 810 },
      recordVideo: { dir: raw, size: { width: 1280, height: 810 } },
    });
    const page = await context.newPage();
    await page.goto(withQuery);
    const click = opt('--click');
    if (click) {
      await page.waitForTimeout(Math.max(0, seconds * 1000 - 4000));
      const el = await page.$(click);
      if (el) {
        const box = await el.boundingBox();
        await page.mouse.move(box.x + box.width / 2, box.y + box.height / 2, { steps: 20 });
        await page.waitForTimeout(600);
        await el.click();
      }
      await page.waitForTimeout(3400);
    } else {
      await page.waitForTimeout(seconds * 1000);
    }
    await context.close();
    const webm = fs.readdirSync(raw).find(f => f.endsWith('.webm'));
    const mp4 = path.join(outdir, 'clip.mp4');
    execFileSync('ffmpeg', ['-loglevel', 'error', '-y', '-i', path.join(raw, webm),
      '-vf', 'crop=1280:720:0:0', '-c:v', 'libx264', '-pix_fmt', 'yuv420p', '-crf', '20', mp4]);
    fs.rmSync(raw, { recursive: true, force: true });
    report.video = mp4;
  }
  await browser.close();
  console.log(JSON.stringify(report, null, 2));
})().catch(e => { console.error(e); process.exit(1); });
