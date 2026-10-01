// 受付係（Google Apps Script）のウェブアプリURL。
// 公開手順は gas/README.md。空のままだと画面の確認用のデモ表示になり、予約は届かない。
window.WORKSHOP_API = 'https://script.google.com/macros/s/AKfycbzWtuuNEUqNYTwg-E7d_EMYvLa10DCcHQV4elprUfrWkS034Fs3aFrlJZkGOs7F02fDdA/exec';

// ?demo を付けて開くと、本物の受付係につながず見本データで動く（紹介ページから試してもらう用）。
// ページ内のリンクにも ?demo を引き継いで、デモの中だけで行き来できるようにする。
window.WORKSHOP_DEMO = /[?&]demo(=|&|$)/.test(location.search);
if (window.WORKSHOP_DEMO) {
  window.WORKSHOP_API = '';
  document.addEventListener('DOMContentLoaded', function () {
    document.querySelectorAll('a[href]').forEach(function (a) {
      var h = a.getAttribute('href');
      if (/^(\.\/|cancel\.html)/.test(h) && h.indexOf('demo') < 0) a.setAttribute('href', h + (h.indexOf('?') < 0 ? '?' : '&') + 'demo');
    });
  });
}

// 受付係とのやりとり。POST は text/plain で送ると事前確認なしで Apps Script に届く。
// 返事がJSONでないとき（ログイン画面・Googleのエラー画面など）は、原因が分かる文にして投げる
function workshopJson(r) {
  return r.text().then(function (t) {
    try { return JSON.parse(t); } catch (e) {
      var m = t.match(/<title>([^<]*)<\/title>/i) || t.match(/class="errorMessage"[^>]*>([^<]*)</i);
      throw new Error('受付係から予期しない返事がありました（' + r.status + (m ? '：' + m[1].trim() : '') + '）');
    }
  });
}

// 通信そのものが断られたとき（公開設定が「全員」でない・URL違いなど）の言い換え
function workshopNetErr(e) {
  throw new Error(e instanceof TypeError ? '受付係につながりませんでした（公開設定が「全員」になっているか、URLが正しいかをご確認ください）' : e.message);
}

window.workshopApi = {
  get: function (params) {
    if (!window.WORKSHOP_API) return Promise.resolve(workshopDemo.get(params));
    var q = new URLSearchParams(params || {}).toString();
    return fetch(window.WORKSHOP_API + (q ? '?' + q : ''), { cache: 'no-store' }).then(workshopJson, workshopNetErr);
  },
  post: function (body) {
    if (!window.WORKSHOP_API) return Promise.resolve(workshopDemo.post(body));
    return fetch(window.WORKSHOP_API, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(body),
    }).then(workshopJson, workshopNetErr);
  },
};

// デモ表示用の見本データ（WORKSHOP_API が空のときだけ使う）
var workshopDemo = {
  config: {
    ok: true,
    title: '第2回JCSAアートフェス ワークショップ',
    products: ['アートバック', 'アートタンブラー'],
    ages: ['大人', '中学生', '小学6年', '小学5年', '小学4年', '小学3年', '小学2年', '小学1年', '年長', '年中', '年少', 'その他'],
    sources: ['Instagram', 'チラシ・ポスター', 'ホームページ', '知人の紹介', 'その他'],
    cancelDeadlineHours: 24,
    slots: [
      { label: '7月18日14時30分〜', remaining: 3, open: true },
      { label: '7月18日16時30分〜', remaining: 0, open: true },
      { label: '7月19日11時30分〜', remaining: 6, open: true },
    ],
  },
  get: function (p) {
    if (p && p.action === 'lookup') {
      return { ok: true, reservation: { id: p.id || 'DEMO23', status: '予約中', name: '見本 花子', product: 'アートバック', slot: '7月19日11時30分〜', age: '大人', cancelable: true } };
    }
    return this.config;
  },
  post: function (b) {
    if (b.action === 'reserve') return { ok: true, id: 'DEMO23', key: 'demo', slot: b.slot, product: b.product, name: b.name };
    if (b.action === 'cancel') return { ok: true, reservation: { id: b.id, status: 'キャンセル', name: '見本 花子', product: 'アートバック', slot: '7月19日11時30分〜' } };
    return { ok: false, error: 'demo' };
  },
};
