// Render hero-v3-lens frames with headless Chrome (deterministic: window.renderAt(t)).
//   node tools/render-hero-v3.mjs stills <url> <outdir> t1,t2,...
//   node tools/render-hero-v3.mjs video  <url> <out.mp4|out.webm|frames-dir> [fps] [seconds]
// <url> must carry ?render=1 (plus w/h/finger as needed); serve the folder over http first.
import { chromium } from '/home/vadim_prod/.npm/_npx/9833c18b2d85bc59/node_modules/playwright/index.mjs';
import { spawn } from 'node:child_process';
import { mkdirSync } from 'node:fs';
const [, , mode, url, out, a4, a5] = process.argv;
const u = new URL(url), W = +u.searchParams.get('w') || 1440, H = +u.searchParams.get('h') || 1200;
const browser = await chromium.launch({ executablePath: '/usr/bin/google-chrome', args: ['--use-angle=swiftshader', '--enable-unsafe-swiftshader', '--ignore-gpu-blocklist', '--font-render-hinting=none'] });
const page = await browser.newPage({ viewport: { width: W, height: H }, deviceScaleFactor: 1 });
page.on('console', m => { if (m.type() === 'error' || m.type() === 'warning') console.log('console:', m.text()); });
page.on('pageerror', e => console.log('pageerror:', e.message));
await page.goto(url);
await page.waitForFunction(() => window.heroReady === true, null, { timeout: 120000 });
if (mode === 'stills') {
  mkdirSync(out, { recursive: true });
  for (const t of a4.split(',').map(Number)) {
    await page.evaluate(t => window.renderAt(t), t);
    await page.screenshot({ path: `${out}/t${String(t).replace('.', '_')}.png` });
    console.log('still', t);
  }
} else {
  const fps = +a4 || 30, secs = +a5 || 16, n = Math.round(fps * secs);
  const args = ['-loglevel', 'error', '-y', '-f', 'image2pipe', '-framerate', String(fps), '-c:v', 'png', '-i', '-'];
  const enc = out.endsWith('.webm')
    ? ['-c:v', 'libvpx-vp9', '-b:v', '0', '-crf', '34', '-row-mt', '1', '-pix_fmt', 'yuv420p', out]
    : ['-c:v', 'libx264', '-preset', 'slow', '-crf', '18', '-pix_fmt', 'yuv420p', '-movflags', '+faststart', out];
  const ff = spawn('ffmpeg', [...args, ...enc], { stdio: ['pipe', 'inherit', 'inherit'] });
  const t0 = Date.now();
  for (let i = 0; i < n; i++) {
    await page.evaluate(t => window.renderAt(t), i / fps);
    const buf = await page.screenshot({ type: 'png' });
    if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
    if (i % 30 === 0) console.log(`frame ${i}/${n} ${((Date.now() - t0) / 1000).toFixed(0)}s`);
  }
  ff.stdin.end(); await new Promise(r => ff.on('close', r));
}
await browser.close();
