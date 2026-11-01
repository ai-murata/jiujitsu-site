// ページの一番上に言語の切り替えボタンを出す。
// 行き先はページの <link rel="alternate" hreflang="..."> から読むので、言語版のあるページにだけ出る。
(function () {
  var names = { ja: ['🇯🇵', '日本語'], en: ['🇺🇸', 'English'], ko: ['🇰🇷', '한국어'], 'pt-BR': ['🇧🇷', 'Português'] };
  var order = ['ja', 'ko', 'en', 'pt-BR'];
  var here = document.documentElement.lang;
  var links = {};
  document.querySelectorAll('link[rel="alternate"][hreflang]').forEach(function (l) { links[l.hreflang] = l.getAttribute('href'); });
  if (!links.en) return;

  var css = document.createElement('style');
  css.textContent =
    '.langbar { display: flex; justify-content: flex-end; flex-wrap: wrap; gap: 2px; max-width: 1080px; margin: 0 auto; padding: 8px 12px 0; position: relative; z-index: 20; font-family: system-ui, -apple-system, "Hiragino Sans", "Apple SD Gothic Neo", sans-serif; }' +
    '.langbar a { display: inline-flex; align-items: center; gap: 5px; min-height: 36px; padding: 0 10px; border: 1px solid transparent; border-radius: 999px; color: #6f665a; font-size: 13px; font-weight: 500; letter-spacing: 0; text-decoration: none; }' +
    '.langbar a:hover { color: #17140d; }' +
    '.langbar a[aria-current] { color: #17140d; font-weight: 700; background: #fffaf0; border-color: #c9a227; }' +
    '@media (max-width: 480px) { .langbar { justify-content: space-between; padding: 6px 8px 0; } .langbar a { padding: 0 7px; font-size: 12px; gap: 3px; } }';
  document.head.appendChild(css);

  var bar = document.createElement('nav');
  bar.className = 'langbar';
  bar.setAttribute('aria-label', 'Language');
  order.forEach(function (code) {
    if (!links[code]) return;
    var a = document.createElement('a');
    a.href = links[code].replace(/^https:\/\/jiujitsu\.co\.jp/, '') + location.hash;
    a.lang = code;
    a.textContent = names[code][0] + ' ' + names[code][1];
    if (code === here) a.setAttribute('aria-current', 'true');
    bar.appendChild(a);
  });
  document.body.insertBefore(bar, document.body.firstChild);
})();
