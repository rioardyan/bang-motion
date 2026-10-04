/* Potret detik kunci dengan Playwright (alternatif snap.mjs bila puppeteer tidak ada).
   Pakai: ROUTES=projects/x/vendor node scripts/snap-pw.mjs <index.html> <folder-out> 1 3.5 8
   ROUTES = folder berisi gsap.min.js, fonts.css, *.woff2. Permintaan ke CDN (jsdelivr, google fonts)
   dijawab dari folder itu, jadi tetap jalan di lingkungan yang memblokir CDN. */
import { createRequire } from 'node:module';
import { pathToFileURL } from 'node:url';
import { mkdir, readFile } from 'node:fs/promises';
import path from 'node:path';
const require = createRequire('/opt/node-tools/node_modules/');
const { chromium } = require('playwright');
const [file, outDir, ...times] = process.argv.slice(2);
const ROUTES = process.env.ROUTES;
await mkdir(outDir, { recursive: true });
const browser = await chromium.launch({ executablePath: process.env.CHROME || '/opt/pw-browsers/chromium-1194/chrome-linux/chrome', args: ['--no-sandbox'] });
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.log('PAGEERROR', e.message));
page.on('console', m => { if (m.type() === 'error' || m.type() === 'assert') console.log('CONSOLE', m.text()); });
if (ROUTES) await page.route(/^https:\/\//, async route => {
  const u = new URL(route.request().url()); const base = path.basename(u.pathname);
  const map = base === 'gsap.min.js' ? 'gsap.min.js' : (u.hostname === 'fonts.googleapis.com' && !base.endsWith('.woff2')) ? 'fonts.css' : base;
  try { const body = await readFile(path.join(ROUTES, map));
    const type = map.endsWith('.js') ? 'text/javascript' : map.endsWith('.css') ? 'text/css' : 'font/woff2';
    await route.fulfill({ body, contentType: type, headers: { 'access-control-allow-origin': '*' } });
  } catch { await route.abort(); }
});
await page.goto(pathToFileURL(path.resolve(file)).href + '?clean=1', { waitUntil: 'load' });
await page.waitForFunction('window.OPENER && window.OPENER.ready', { timeout: 30000 });
const fonts = await page.evaluate(async () => {
  const r = {}; for (const f of ['900 100px "Big Shoulders Display"', '700 40px "Schibsted Grotesk"']) { await document.fonts.load(f, 'Aa'); r[f] = document.fonts.check(f); }
  r.loaded = [...document.fonts].filter(f => f.status === 'loaded').map(f => f.family + ' ' + f.weight); return r; });
console.log('fonts', JSON.stringify(fonts));
for (const ts of times) {
  const t = Number(ts);
  await page.evaluate(async time => { window.OPENER.seek(time); await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))); window.OPENER.seek(time); }, t);
  await page.screenshot({ path: `${outDir}/t${t.toFixed(2).replace('.', '_')}.png` });
  process.stdout.write(t + ' ');
}
await browser.close(); console.log('\nselesai');
