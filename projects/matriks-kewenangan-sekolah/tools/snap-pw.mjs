/* Potret detik kunci dengan Playwright (Chromium bawaan), tanpa server.
   Pakai (dari folder proyek): node tools/snap-pw.mjs <folder-keluaran> <detik> [<detik> ...]
   Halaman harus mengekspos window.OPENER = { W, H, ready, seek(t) }. */
import { createRequire } from 'node:module';
const { chromium } = createRequire(import.meta.url)('playwright');   // playwright global: NODE_PATH=$(npm root -g)
import { pathToFileURL } from 'node:url';
import { mkdir } from 'node:fs/promises';
import path from 'node:path';

const [outDir, ...times] = process.argv.slice(2);
if (!outDir || !times.length) { console.log('pakai: node tools/snap-pw.mjs <folder-keluaran> <detik> [...]'); process.exit(1); }
const url = process.env.URL || pathToFileURL(path.resolve('index.html')).href + '?clean=1';
await mkdir(outDir, { recursive: true });
const browser = await chromium.launch();
const page = await browser.newPage({ viewport: { width: 1080, height: 1350 }, deviceScaleFactor: 1 });
page.on('pageerror', e => console.log('PAGEERROR', e.message));
page.on('console', m => { if (m.type() === 'error') console.log('CONSOLE', m.text()); });
await page.goto(url, { waitUntil: 'load' });
await page.waitForFunction('window.OPENER && window.OPENER.ready', { timeout: 60000 });
const fonts = await page.evaluate(() => [...document.fonts].map(f => `${f.family} ${f.weight} ${f.status}`));
console.log('fonts:', fonts.join(' | '));
for (const ts of times) {
  const t = Number(ts);
  await page.evaluate(async (time) => {
    window.OPENER.seek(time);
    await new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r)));
    window.OPENER.seek(time);
  }, t);
  await page.screenshot({ path: `${outDir}/t${t.toFixed(2).replace('.', '_')}.png` });
  process.stdout.write(`${t} `);
}
await browser.close(); console.log('\nselesai');
