// ブログ記事のシェアボタン。<div class="share"></div> の中に描画する。
(function () {
  var box = document.querySelector('.share');
  if (!box) return;

  var url = (document.querySelector('meta[property="og:url"]') || {}).content || location.href;
  var title = document.title;
  var u = encodeURIComponent(url);
  var t = encodeURIComponent(title);

  var css = document.createElement('style');
  css.textContent =
    '.share { margin-top: 56px; text-align: center; }' +
    '.share .label { font-size: 12px; letter-spacing: .3em; color: var(--gold); font-weight: 700; margin: 0 0 14px; }' +
    '.share .btns { display: flex; flex-wrap: wrap; justify-content: center; gap: 10px; }' +
    '.share a, .share button { display: inline-flex; align-items: center; gap: 8px; height: 42px; padding: 0 18px; border: 1px solid var(--line); background: var(--paper); color: var(--ink); font: 500 13.5px var(--gothic); letter-spacing: .06em; text-decoration: none; cursor: pointer; border-radius: 999px; transition: background .15s, border-color .15s; }' +
    '.share a:hover, .share button:hover { background: var(--panel); border-color: var(--gold); }' +
    '.share svg { width: 17px; height: 17px; flex: none; }' +
    '.share .note { font-size: 12px; color: var(--faint); margin: 12px 0 0; min-height: 1.5em; }';
  document.head.appendChild(css);

  var icon = {
    ig: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.5" cy="6.5" r="1" fill="currentColor" stroke="none"/></svg>',
    x: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M18.9 2H22l-7.2 8.2L23 22h-6.6l-5.2-6.8L5.3 22H2.2l7.7-8.8L1.8 2h6.8l4.7 6.2L18.9 2zm-1.2 18h1.7L7.4 3.9H5.6L17.7 20z"/></svg>',
    fb: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M13.5 22v-8h2.7l.4-3.2h-3.1V8.8c0-.9.3-1.5 1.6-1.5h1.7V4.4c-.3 0-1.3-.1-2.4-.1-2.4 0-4.1 1.5-4.1 4.2v2.3H7.6V14h2.7v8h3.2z"/></svg>',
    line: '<svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 3C6.5 3 2 6.6 2 11.1c0 4 3.6 7.4 8.4 8 .3.1.8.2.9.5.1.3.1.7 0 1l-.1.9c0 .3-.2 1 .9.6 1.1-.5 6-3.5 8.1-6 1.5-1.6 2.2-3.3 2.2-5C22.4 6.6 17.9 3 12 3zM8.3 13.5H6.3c-.3 0-.5-.2-.5-.5V9c0-.3.2-.5.5-.5s.5.2.5.5v3.5h1.5c.3 0 .5.2.5.5s-.2.5-.5.5zm2.1-.5c0 .3-.2.5-.5.5s-.5-.2-.5-.5V9c0-.3.2-.5.5-.5s.5.2.5.5v4zm4.8 0c0 .2-.1.4-.3.5h-.2c-.2 0-.3-.1-.4-.2l-2-2.8V13c0 .3-.2.5-.5.5s-.5-.2-.5-.5V9c0-.2.1-.4.3-.5h.2c.2 0 .3.1.4.2l2 2.8V9c0-.3.2-.5.5-.5s.5.2.5.5v4zm3.2-2.5c.3 0 .5.2.5.5s-.2.5-.5.5h-1.5v1h1.5c.3 0 .5.2.5.5s-.2.5-.5.5h-2c-.3 0-.5-.2-.5-.5V9c0-.3.2-.5.5-.5h2c.3 0 .5.2.5.5s-.2.5-.5.5h-1.5v1h1.5z"/></svg>',
    link: '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><path d="M10 14a5 5 0 0 0 7 0l3-3a5 5 0 0 0-7-7l-1 1"/><path d="M14 10a5 5 0 0 0-7 0l-3 3a5 5 0 0 0 7 7l1-1"/></svg>'
  };

  box.innerHTML =
    '<p class="label">SHARE</p>' +
    '<div class="btns">' +
    '<button type="button" data-act="ig">' + icon.ig + 'Instagram</button>' +
    '<a href="https://twitter.com/intent/tweet?text=' + t + '&url=' + u + '" target="_blank" rel="noopener">' + icon.x + 'X</a>' +
    '<a href="https://www.facebook.com/sharer/sharer.php?u=' + u + '" target="_blank" rel="noopener">' + icon.fb + 'Facebook</a>' +
    '<a href="https://social-plugins.line.me/lineit/share?url=' + u + '" target="_blank" rel="noopener">' + icon.line + 'LINE</a>' +
    '<button type="button" data-act="copy">' + icon.link + 'リンクをコピー</button>' +
    '</div>' +
    '<p class="note" aria-live="polite"></p>';

  var note = box.querySelector('.note');

  function copy(msg) {
    var done = function () { note.textContent = msg; };
    if (navigator.clipboard && navigator.clipboard.writeText) {
      navigator.clipboard.writeText(url).then(done, fallback);
    } else {
      fallback();
    }
    function fallback() {
      var ta = document.createElement('textarea');
      ta.value = url;
      document.body.appendChild(ta);
      ta.select();
      try { document.execCommand('copy'); done(); } catch (e) { note.textContent = url; }
      ta.remove();
    }
  }

  box.addEventListener('click', function (e) {
    var b = e.target.closest('button');
    if (!b) return;
    if (b.dataset.act === 'copy') {
      copy('リンクをコピーしました');
    } else if (b.dataset.act === 'ig') {
      // Instagram にはWebから直接シェアする仕組みがないので、
      // スマホは共有メニュー（ここからInstagramを選べる）、PCはリンクコピーにする。
      if (navigator.share) {
        navigator.share({ title: title, url: url }).catch(function () {});
      } else {
        copy('リンクをコピーしました。Instagramのストーリーズやプロフィールに貼ってください');
      }
    }
  });
})();

// 記事の下に「前の記事・次の記事」を出す。
// 並び順はブログ一覧（/blog/）の <li> から読むので、一覧に記事を足すだけで自動でつながる。
(function () {
  var article = document.querySelector('article');
  if (!article || !window.fetch || !window.DOMParser) return;
  var here = location.pathname.replace(/index\.html$/, '');

  fetch('/blog/').then(function (r) { return r.text(); }).then(function (html) {
    var doc = new DOMParser().parseFromString(html, 'text/html');
    var items = Array.prototype.map.call(doc.querySelectorAll('.posts li'), function (li, i) {
      var a = li.querySelector('a'), t = li.querySelector('time'), h = li.querySelector('h2');
      return {
        href: a ? a.getAttribute('href') : '',
        title: h ? h.textContent.trim() : '',
        date: t ? t.getAttribute('datetime') : '',
        label: t ? t.textContent.trim() : '',
        nikki: li.classList.contains('is-nikki'),
        i: i
      };
    });
    // 一覧と同じ並び（新しい順・同じ日ならふつうの記事が先）
    items.sort(function (a, b) {
      return (a.date < b.date ? 1 : a.date > b.date ? -1 : 0) || (a.nikki - b.nikki) || (a.i - b.i);
    });
    var at = -1;
    items.forEach(function (it, i) { if (it.href === here) at = i; });
    if (at < 0) return;
    var older = items[at + 1], newer = items[at - 1];
    if (!older && !newer) return;

    var css = document.createElement('style');
    css.textContent =
      '.post-nav { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; margin: 48px 0 0; }' +
      '.post-nav a { display: block; padding: 14px 16px; border: 1px solid var(--line); background: var(--panel); color: var(--ink); text-decoration: none; transition: border-color .15s; }' +
      '.post-nav a:hover { border-color: var(--gold); }' +
      '.post-nav a.newer { grid-column: 2; text-align: right; }' +
      '.post-nav .dir { display: block; font-size: 11px; letter-spacing: .2em; color: var(--gold); font-weight: 700; }' +
      '.post-nav b { display: block; font-family: var(--mincho); font-size: 15px; line-height: 1.6; margin: 4px 0 2px; }' +
      '.post-nav time { font-size: 12px; color: var(--faint); }' +
      '@media (max-width: 560px) { .post-nav { grid-template-columns: 1fr; } .post-nav a.newer { grid-column: auto; text-align: left; } }';
    document.head.appendChild(css);

    function card(it, cls, dir) {
      return '<a class="' + cls + '" href="' + it.href + '"><span class="dir">' + dir + '</span>' +
        '<b>' + it.title.replace(/</g, '&lt;') + '</b><time>' + it.label + '</time></a>';
    }
    var nav = document.createElement('nav');
    nav.className = 'post-nav';
    nav.setAttribute('aria-label', '前の記事・次の記事');
    nav.innerHTML = (older ? card(older, 'older', '← 前の記事') : '') + (newer ? card(newer, 'newer', '次の記事 →') : '');
    article.after(nav);
  }).catch(function () {});
})();
