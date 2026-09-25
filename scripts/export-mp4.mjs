/* =========================================================
   EXPORT MP4 SEKALI JALAN — frame JPEG langsung dialirkan ke ffmpeg.

   Tidak ada ribuan PNG di disk: tiap frame dipotret (dua kali — potret
   pertama dibuang supaya tidak ada frame berkedip karena gaya belum
   tergambar), lalu ditulis ke stdin ffmpeg (image2pipe → libx264).

   Pakai:
     ROUTES=projects/nama-proyek node scripts/export-mp4.mjs out.mp4
   Variabel opsional:
     FPS=30  BITRATE=3500k  W=1080 H=1350  FFMPEG=/path/ke/ffmpeg
     QUALITY=92   (kualitas JPEG antara, bukan kualitas akhir)
   ROUTES = folder proyek yang disajikan lewat server http lokal
   (font & aset lokal termuat seperti di browser biasa).
   Halaman harus mengekspos window.OPENER = { DURATION, ready, seek(t) }.
   ========================================================= */
import puppeteer from 'puppeteer';
import { spawn } from 'node:child_process';
import http from 'node:http';
import { readFile } from 'node:fs/promises';
import path from 'node:path';

const out = process.argv[2] || 'out.mp4';
const ROOT = path.resolve(process.env.ROUTES || '.');
const FPS = Number(process.env.FPS || 30), W = Number(process.env.W || 1080), H = Number(process.env.H || 1350);
const BITRATE = process.env.BITRATE || '3500k', QUALITY = Number(process.env.QUALITY || 92);
const FFMPEG = process.env.FFMPEG || 'ffmpeg';

const TYPES = { '.html':'text/html', '.js':'text/javascript', '.css':'text/css', '.woff2':'font/woff2', '.json':'application/json',
  '.png':'image/png', '.jpg':'image/jpeg', '.svg':'image/svg+xml', '.mp4':'video/mp4', '.webm':'video/webm' };
const server = http.createServer(async (req, res) => {
  try { const p = path.join(ROOT, decodeURIComponent(new URL(req.url, 'http://x').pathname));
    if (!p.startsWith(ROOT)) throw 0;
    const body = await readFile(p.endsWith('/') ? p + 'index.html' : p);
    res.writeHead(200, { 'Content-Type': TYPES[path.extname(p)] || 'application/octet-stream', 'Cache-Control': 'no-store' }); res.end(body);
  } catch { res.writeHead(404); res.end(); }
});
await new Promise(r => server.listen(0, '127.0.0.1', r));
const url = `http://127.0.0.1:${server.address().port}/index.html?clean=1`;

const browser = await puppeteer.launch({ headless: 'new', executablePath: process.env.PUPPETEER_EXECUTABLE_PATH,
  args: ['--no-sandbox', '--hide-scrollbars', '--force-color-profile=srgb'] });
const page = await browser.newPage();
page.on('pageerror', e => console.log('PAGEERROR', e.message));
await page.setViewport({ width: W, height: H, deviceScaleFactor: 1 });
await page.goto(url, { waitUntil: 'networkidle0' });
await page.waitForFunction('window.OPENER && window.OPENER.ready', { timeout: 60000 });
/* document.fonts.check bisa "lolos" palsu — pastikan setiap font benar-benar berstatus loaded */
const fonts = await page.evaluate(() => [...document.fonts].map(f => `${f.family} ${f.weight}:${f.status}`));
const notLoaded = fonts.filter(f => !f.endsWith(':loaded'));
console.log('font:', fonts.join(' | '));
if (notLoaded.length) { console.error('FONT BELUM TERMUAT:', notLoaded.join(', ')); process.exit(1); }

const DURATION = await page.evaluate(() => window.OPENER.DURATION);
const total = Math.round(DURATION * FPS);
const ff = spawn(FFMPEG, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-c:v', 'libx264', '-preset', 'medium', '-b:v', BITRATE, '-maxrate', BITRATE, '-bufsize', '7000k',
  '-pix_fmt', 'yuv420p', '-movflags', '+faststart', '-r', String(FPS), out], { stdio: ['pipe', 'inherit', 'inherit'] });
const done = new Promise((res, rej) => ff.on('close', c => c === 0 ? res() : rej(new Error('ffmpeg keluar ' + c))));

const t0 = Date.now();
for (let i = 0; i < total; i++) {
  await page.evaluate(t => { window.OPENER.seek(t); return new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); }, i / FPS);
  await page.screenshot({ type: 'jpeg', quality: QUALITY, clip: { x: 0, y: 0, width: W, height: H } });           // dibuang
  const buf = await page.screenshot({ type: 'jpeg', quality: QUALITY, clip: { x: 0, y: 0, width: W, height: H } });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % FPS === 0) process.stdout.write(`\r${i}/${total} frame (${((Date.now() - t0) / 1000).toFixed(0)} dtk)`);
}
ff.stdin.end(); await done;
console.log(`\nselesai: ${out} — ${total} frame @ ${FPS} fps`);
await browser.close(); server.close();
