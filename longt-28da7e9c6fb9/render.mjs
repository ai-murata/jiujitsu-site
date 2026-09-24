// SVG → 入稿用 透過PNG(300dpi) を書き出す。 使い方: NODE_PATH=$(npm root -g) node render.mjs
import { createRequire } from 'node:module';
import { readFileSync } from 'node:fs';
import { execFileSync } from 'node:child_process';

const { chromium } = createRequire(import.meta.url)('playwright');

const DPI = 300;
const FONTS = 'https://fonts.googleapis.com/css2?family=Anton&family=Oswald:wght@600&family=Noto+Sans+JP:wght@900&display=block';
const jobs = [
  // ガイド付き（レイアウト確認用）と、ガイドを消した文字のみ（入稿用）の2枚
  { svg: 'front.svg', png: 'front_layout_300dpi.png', mm: [280, 350] },
  { svg: 'front.svg', png: 'front_print_300dpi.png', mm: [280, 350], hideGuides: true },
  { svg: 'sleeve.svg', png: 'sleeve_300dpi.png', mm: [80, 420] },
];

// Chromium からは Google Fonts に直接届かない環境があるため、curl で取得して data URL で埋め込む
const curl = (url, enc) => execFileSync('curl', ['-sSfL', url], { encoding: enc, maxBuffer: 64 << 20 });
const fontCss = curl(FONTS, 'utf8').replace(/url\((https:[^)]+)\)/g,
  (_, u) => `url(data:font/ttf;base64,${curl(u, 'buffer').toString('base64')})`);

const browser = await chromium.launch();
for (const { svg, png, mm, hideGuides } of jobs) {
  const [w, h] = mm.map((v) => Math.round((v / 25.4) * DPI));
  const page = await browser.newPage({ viewport: { width: w, height: h } });
  const src = readFileSync(new URL(svg, import.meta.url), 'utf8')
    .replace(/width="[^"]+mm" height="[^"]+mm"/, 'width="100%" height="100%"');
  await page.setContent(`<style>${fontCss}</style><style>html,body{margin:0;background:transparent}svg{display:block}${hideGuides ? '.guide{display:none}' : ''}</style>${src}`);
  await page.evaluate(() => Promise.all(
    ['100px Anton', '600 100px Oswald', '900 100px "Noto Sans JP"'].map((f) => document.fonts.load(f, 'Aあ')),
  ));
  const loaded = await page.evaluate(() => [...document.fonts].filter((f) => f.status === 'loaded').map((f) => f.family));
  for (const fam of ['Anton', 'Oswald', 'Noto Sans JP']) {
    if (!loaded.some((l) => l.replace(/"/g, '') === fam)) throw new Error(`フォント未ロード: ${fam}`);
  }
  // 各テキストの左右端(mm)を表示し、版面外へのはみ出しを警告
  const rows = await page.evaluate(([wmm, hmm]) => {
    const box = document.querySelector('svg').getBoundingClientRect();
    const k = wmm / box.width;
    return [...document.querySelectorAll('text')].map((t) => {
      const r = t.getBoundingClientRect();
      return { text: t.textContent, x0: +((r.left - box.left) * k).toFixed(1), x1: +((r.right - box.left) * k).toFixed(1),
        y0: +((r.top - box.top) * k).toFixed(1), y1: +((r.bottom - box.top) * k).toFixed(1),
        out: r.left < box.left || r.right > box.right || r.top < box.top || r.bottom > box.bottom };
    });
  }, mm);
  for (const r of rows) console.log(`  ${r.out ? '⚠ はみ出し' : '  '} x ${r.x0}–${r.x1}mm  y ${r.y0}–${r.y1}mm  ${r.text}`);
  await page.screenshot({ path: new URL(png, import.meta.url).pathname, omitBackground: true });
  console.log(`${png}: ${w}×${h}px`);
  await page.close();
}
await browser.close();
