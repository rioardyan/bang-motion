/* =========================================================
   EXPORT MP4 HEMAT — Playwright + ffmpeg, satu kali jalan.

   Beda dengan export-frames.mjs (PNG ke folder, lalu ffmpeg terpisah):
   - frame JPEG dialirkan langsung ke ffmpeg (tanpa ribuan PNG di disk);
   - tiap frame dipotret dua kali dan yang dipakai potret KEDUA — di Chromium
     headless potret pertama setelah seek kadang tertinggal satu langkah
     (huruf hilang sesaat / frame berkedip);
   - encode langsung ke ukuran iklan: default ±3,5 Mbps, 30 fps, faststart.

   Prasyarat: Node + Playwright (Chromium) + ffmpeg ber-libx264.
   Halaman harus mengekspos window.OPENER = { W, H, DURATION, ready, seek(t) }.

   Pakai (dari folder proyek):
     node <path>/scripts/export-mp4.mjs index.html hasil.mp4
   Variabel opsional:
     FPS=30  RATE=3500k  FFMPEG=/path/ffmpeg  CHROMIUM=/path/chromium
     ROUTES=folder  → sajikan GSAP & font dari disk bila CDN diblokir:
       folder/gsap.min.js, folder/fonts.css (+ file .woff2 yang dirujuknya)
   Tips ukuran: hindari butiran/noise di seluruh frame — noise paling boros bitrate.
   ========================================================= */
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import { existsSync } from 'node:fs';
import { resolve, join } from 'node:path';

const [inFile = 'index.html', outFile = 'promo.mp4'] = process.argv.slice(2);
const FPS = Number(process.env.FPS || 30), RATE = process.env.RATE || '3500k';
const FF = process.env.FFMPEG || 'ffmpeg', R = process.env.ROUTES;

const browser = await chromium.launch(process.env.CHROMIUM ? { executablePath: process.env.CHROMIUM } : {});
const page = await browser.newPage();
page.on('pageerror', e => console.log('PAGEERROR', e.message));
if (R) {
  if (existsSync(join(R, 'gsap.min.js'))) await page.route('**/gsap.min.js', r => r.fulfill({ path: join(R, 'gsap.min.js') }));
  if (existsSync(join(R, 'fonts.css'))) {
    await page.route('**/css2*', r => r.fulfill({ path: join(R, 'fonts.css'), contentType: 'text/css' }));
    await page.route('**/*.woff2', r => r.fulfill({ path: join(R, r.request().url().split('/').pop()), contentType: 'font/woff2' }));
  }
}
await page.goto('file://' + resolve(inFile) + '?clean=1');
await page.waitForFunction('window.OPENER && window.OPENER.ready', null, { timeout: 60000 });
// pastikan semua @font-face benar-benar termuat (fonts.check saja bisa "lolos" bila CSS font gagal dimuat)
const fontsOk = await page.evaluate(async () => {
  await Promise.all([...document.fonts].map(f => f.load().catch(() => null)));
  const faces = [...document.fonts];
  return faces.length > 0 && faces.every(f => f.status === 'loaded');
});
if (!fontsOk) { console.log('FONT GAGAL DIMUAT — pakai ROUTES=folder berisi fonts.css + .woff2'); process.exit(1); }
const { W, H, D } = await page.evaluate(() => ({ W: OPENER.W || 1920, H: OPENER.H || 1080, D: OPENER.DURATION }));
await page.setViewportSize({ width: W, height: H });

const ff = spawn(FF, ['-y', '-loglevel', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  '-c:v', 'libx264', '-preset', 'medium', '-b:v', RATE, '-maxrate', RATE, '-bufsize', '7000k',
  '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-movflags', '+faststart', outFile], { stdio: ['pipe', 'inherit', 'inherit'] });

const n = Math.round(D * FPS), t0 = Date.now();
for (let i = 0; i < n; i++) {
  const t = i / FPS;
  await page.evaluate(async t => { OPENER.seek(t); await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); OPENER.seek(t); }, t);
  await page.screenshot({ type: 'jpeg', quality: 60 });            // potret pertama dibuang (bisa tertinggal satu langkah)
  const buf = await page.screenshot({ type: 'jpeg', quality: 93 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % 90 === 0) console.log(`frame ${i}/${n}  ${((Date.now() - t0) / 1000).toFixed(0)} dtk`);
}
ff.stdin.end();
await new Promise(r => ff.on('close', r));
await browser.close();
console.log(`selesai: ${outFile} · ${n} frame · ${((Date.now() - t0) / 1000).toFixed(0)} dtk`);
