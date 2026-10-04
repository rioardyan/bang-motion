/* =========================================================
   Render halaman motion jadi MP4 SEKALI jalan.
   Frame dipotret satu per satu (waktu timeline disetel, bukan direkam), JPEG-nya langsung
   dialirkan ke ffmpeg lewat pipe — tanpa menulis ribuan PNG ke disk.
   Tiap frame dipotret DUA kali dan yang kedua dipakai: potret pertama kadang menangkap
   frame sebelum gaya terbaru tergambar (kedip).

   Pakai (Playwright dari /opt/node-tools; ROUTES = folder gsap.min.js + fonts.css + *.woff2,
   dipakai bila CDN diblokir):
     ROUTES=projects/x/vendor node scripts/export-mp4.mjs projects/x/index.html projects/x/hasil.mp4
   Opsi lewat env: FPS=30  BITRATE=3500k  QUALITY=92  CHROME=/path/chrome
   Halaman harus mengekspos window.OPENER = { W, H, DURATION, seek(t), ready }.
   ========================================================= */
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';
import { readFile } from 'node:fs/promises';
import { spawn } from 'node:child_process';
import path from 'node:path';

const require = createRequire(process.env.PW_ROOT || '/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const [file, out] = process.argv.slice(2);
if (!file || !out) { console.log('pakai: node export-mp4.mjs <index.html> <hasil.mp4>'); process.exit(1); }
const FPS = Number(process.env.FPS || 30), BITRATE = process.env.BITRATE || '3500k', QUALITY = Number(process.env.QUALITY || 92);
const ROUTES = process.env.ROUTES;

const browser = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.log('PAGEERROR', e.message));
if (ROUTES) await page.route(/^https:\/\//, async route => {
  const u = new URL(route.request().url()); const base = path.basename(u.pathname);
  const map = base === 'gsap.min.js' ? 'gsap.min.js' : (u.hostname === 'fonts.googleapis.com' && !base.endsWith('.woff2')) ? 'fonts.css' : base;
  try { await route.fulfill({ body: await readFile(path.join(ROUTES, map)), contentType: map.endsWith('.js') ? 'text/javascript' : map.endsWith('.css') ? 'text/css' : 'font/woff2' }); }
  catch { await route.abort(); }
});
await page.goto(pathToFileURL(path.resolve(file)).href + '?clean=1', { waitUntil: 'load' });
await page.waitForFunction('window.OPENER && window.OPENER.ready', null, { timeout: 60000 });
const { W, H, DURATION } = await page.evaluate(() => ({ W: window.OPENER.W, H: window.OPENER.H, DURATION: window.OPENER.DURATION }));
await page.setViewportSize({ width: W, height: H });
const fonts = await page.evaluate(() => [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight));
console.log('font termuat:', fonts.join(', '));

const total = Math.round(DURATION * FPS);
console.log(`${total} frame @ ${FPS} fps (${DURATION}s), ${W}x${H}, ${BITRATE} -> ${out}`);
const ff = spawn('ffmpeg', ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-c:v', 'libx264', '-preset', 'medium', '-b:v', BITRATE, '-maxrate', '4500k', '-bufsize', '7000k', '-pix_fmt', 'yuv420p',
  '-r', String(FPS), '-movflags', '+faststart', out], { stdio: ['pipe', 'inherit', 'inherit'] });
const ffDone = new Promise(res => ff.on('close', res));

const t0 = Date.now();
for (let i = 0; i < total; i++) {
  const t = i / FPS;
  await page.evaluate(async time => {
    window.OPENER.seek(time);
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    window.OPENER.seek(time);
  }, t);
  await page.screenshot({ type: 'jpeg', quality: QUALITY });                      // potret pertama dibuang
  const buf = await page.screenshot({ type: 'jpeg', quality: QUALITY });          // potret kedua dipakai
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % FPS === 0) console.log(`${i}/${total}  ${t.toFixed(1)}s  (${((Date.now() - t0) / 1000).toFixed(0)} dtk berjalan)`);
}
ff.stdin.end();
await ffDone;
await browser.close();
console.log(`selesai dalam ${((Date.now() - t0) / 1000).toFixed(0)} dtk -> ${out}`);
