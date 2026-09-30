// 受付係（Google Apps Script）のウェブアプリURL。
// 公開手順は gas/README.md。空のままだと画面の確認用のデモ表示になり、予約は届かない。
window.WORKSHOP_API = 'https://script.google.com/a/macros/jiujitsu.co.jp/s/AKfycbyVIWoYKZn-b8DGUELiX3i-rDX1iahenFMkrVxNLChMI9kD2Ic4S7Igf1p-ERPhwA16/exec';

// 受付係とのやりとり。POST は text/plain で送ると事前確認なしで Apps Script に届く。
window.workshopApi = {
  get: function (params) {
    if (!window.WORKSHOP_API) return Promise.resolve(workshopDemo.get(params));
    var q = new URLSearchParams(params || {}).toString();
    return fetch(window.WORKSHOP_API + (q ? '?' + q : ''), { cache: 'no-store' }).then(function (r) { return r.json(); });
  },
  post: function (body) {
    if (!window.WORKSHOP_API) return Promise.resolve(workshopDemo.post(body));
    return fetch(window.WORKSHOP_API, {
      method: 'POST',
      headers: { 'Content-Type': 'text/plain;charset=utf-8' },
      body: JSON.stringify(body),
    }).then(function (r) { return r.json(); });
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
