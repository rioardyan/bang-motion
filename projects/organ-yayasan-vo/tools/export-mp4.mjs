/* Render index.html jadi MP4, SEKALI JALAN: tiap frame di-seek ke waktunya, dipotret (JPEG),
   lalu dialirkan langsung ke ffmpeg. Frame dipotret setelah seek kedua supaya tidak ada frame berkedip.
   Pakai (dari folder proyek): NODE_PATH=$(npm root -g) node tools/export-mp4.mjs <keluaran.mp4> [fps=30]
   Aset (GSAP, font) dimuat dari folder lokal lewat file://, jadi tidak butuh jaringan. */
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');
import { spawn } from 'node:child_process';
import { pathToFileURL } from 'node:url';
import path from 'node:path';
import { mkdir } from 'node:fs/promises';

const out = process.argv[2] || 'out/video.mp4';
const FPS = Number(process.argv[3] || 30);
const AUDIO = process.argv[4] || '';   // opsional: berkas audio yang di-mux (aac), dipadatkan diam sampai durasi video
await mkdir(path.dirname(out), { recursive: true });
const browser = await chromium.launch({ args: ['--force-color-profile=srgb'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.log('PAGEERROR', e.message));
await page.goto(pathToFileURL(path.resolve('index.html')).href + '?clean=1', { waitUntil: 'load' });
await page.waitForFunction('window.OPENER && window.OPENER.ready', { timeout: 60000 });
const DUR = await page.evaluate(() => window.OPENER.DURATION);
const N = Math.round(DUR * FPS);
// JPEG = YCbCr penuh BT.601; ubah ke rentang TV BT.709 dan beri tanda warna yang benar
const ff = spawn('ffmpeg', ['-y', '-v', 'error', '-f', 'image2pipe', '-framerate', String(FPS), '-c:v', 'mjpeg', '-i', '-',
  ...(AUDIO ? ['-i', AUDIO, '-map', '0:v', '-map', '1:a', '-c:a', 'aac', '-b:a', '160k', '-ar', '48000', '-ac', '2', '-af', `apad=whole_dur=${DUR}`, '-t', String(DUR)] : []),
  '-vf', 'scale=in_range=pc:in_color_matrix=bt601:out_range=tv:out_color_matrix=bt709,format=yuv420p',
  '-c:v', 'libx264', '-preset', 'medium', '-b:v', '3500k', '-maxrate', '5000k', '-bufsize', '7000k',
  '-colorspace', 'bt709', '-color_primaries', 'bt709', '-color_trc', 'bt709', '-color_range', 'tv',
  '-r', String(FPS), '-movflags', '+faststart', ...(AUDIO ? [] : ['-an']), out], { stdio: ['pipe', 'inherit', 'inherit'] });
const done = new Promise((res, rej) => { ff.on('close', c => c === 0 ? res() : rej(new Error('ffmpeg keluar ' + c))); });
const t0 = Date.now();
for (let i = 0; i < N; i++) {
  const t = i / FPS;
  await page.evaluate(async (time) => {
    window.OPENER.seek(time);
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    window.OPENER.seek(time);                       // potret kedua: state sudah settle
  }, t);
  const buf = await page.screenshot({ type: 'jpeg', quality: 92 });
  if (!ff.stdin.write(buf)) await new Promise(r => ff.stdin.once('drain', r));
  if (i % 60 === 0) console.log(`frame ${i}/${N}  t=${t.toFixed(2)}s  ${((Date.now() - t0) / 1000).toFixed(0)}s`);
}
ff.stdin.end(); await done; await browser.close();
console.log(`selesai: ${out} (${N} frame, ${((Date.now() - t0) / 1000).toFixed(0)} dtk)`);
