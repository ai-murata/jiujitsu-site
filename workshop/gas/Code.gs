/**
 * ワークショップ予約の受付係（Google Apps Script）
 *
 * SHEET_ID のスプレッドシートに予約を書き込む（空なら、貼り付けたスプレッドシート自身）。
 * 最初に一度だけ setup を実行すると「予約」「枠」シートができる。
 * 日時・定員は「枠」シートで、制作物や年齢の選択肢は下の CONFIG で変える。
 * くわしい手順は同じフォルダの README.md を参照。
 */

// 予約を書き込むスプレッドシートのID（URLの /d/ と /edit の間）。
// 空ならこのプログラムが付いているスプレッドシートを使う。
const SHEET_ID = '1_Ln8S1m3r4bcFPtc6Cq631u4pKQiGCo2xrap-AIY8MI';

const CONFIG = {
  title: '第2回JCSAアートフェス ワークショップ',
  organizer: 'JCSA アートフェス事務局',
  // 新しい予約・キャンセルが入ったときに知らせる宛先（空なら送らない）
  notifyTo: 'ai@jiujitsu.co.jp',
  // キャンセルページのURL（メールのリンクに使う）
  cancelUrl: 'https://jiujitsu.co.jp/workshop/cancel.html',
  // 開始の何時間前までキャンセルを受け付けるか（0なら開始まで）
  cancelDeadlineHours: 24,
  products: ['アートバック', 'アートタンブラー'],
  ages: ['大人', '中学生', '小学6年', '小学5年', '小学4年', '小学3年', '小学2年', '小学1年', '年長', '年中', '年少', 'その他'],
  sources: ['Instagram', 'チラシ・ポスター', 'ホームページ', '知人の紹介', 'その他'],
};

const SHEET_RESV = '予約';
const SHEET_SLOT = '枠';
const RESV_HEADERS = ['予約番号', '受付日時', '状態', 'お名前', 'ふりがな', 'メールアドレス', '住所', '電話番号',
  '年齢', 'ご希望の制作物', 'ご希望の日時', 'このイベントをどこで知りましたか？', '同意', 'キャンセル日時', 'キー'];
const SLOT_HEADERS = ['日時（表示）', '開始', '定員', '受付'];
const ACTIVE = '予約中';
const CANCELED = 'キャンセル';

/** 最初に一度だけ実行：シートと見出しを用意する */
function setup() {
  const ss = book_();
  let r = ss.getSheetByName(SHEET_RESV) || ss.insertSheet(SHEET_RESV);
  if (r.getLastRow() === 0) {
    r.appendRow(RESV_HEADERS);
    r.setFrozenRows(1);
    r.getRange(1, 1, 1, RESV_HEADERS.length).setFontWeight('bold');
  }
  let s = ss.getSheetByName(SHEET_SLOT) || ss.insertSheet(SHEET_SLOT);
  if (s.getLastRow() === 0) {
    s.appendRow(SLOT_HEADERS);
    s.appendRow(['7月18日14時30分〜', '2027/07/18 14:30', 6, '○']);
    s.appendRow(['7月18日16時30分〜', '2027/07/18 16:30', 6, '○']);
    s.appendRow(['7月19日11時30分〜', '2027/07/19 11:30', 6, '○']);
    s.setFrozenRows(1);
    s.getRange(1, 1, 1, SLOT_HEADERS.length).setFontWeight('bold');
    s.getRange('B:B').setNumberFormat('yyyy/mm/dd hh:mm');
  }
}

/* ---------- 入口 ---------- */

function doGet(e) {
  const p = (e && e.parameter) || {};
  try {
    if (p.action === 'lookup') return json(lookup_(p.id, p.key, p.email));
    return json(config_());
  } catch (err) {
    return json({ ok: false, error: String(err.message || err) });
  }
}

function doPost(e) {
  let body = {};
  try { body = JSON.parse(e.postData.contents); } catch (_) { return json({ ok: false, error: '送信内容を読み取れませんでした。' }); }
  const lock = LockService.getScriptLock();
  if (!lock.tryLock(20000)) return json({ ok: false, error: '混み合っています。少し待ってからもう一度お試しください。' });
  try {
    if (body.action === 'reserve') return json(reserve_(body));
    if (body.action === 'cancel') return json(cancel_(body));
    return json({ ok: false, error: '不明な操作です。' });
  } catch (err) {
    return json({ ok: false, error: String(err.message || err) });
  } finally {
    lock.releaseLock();
  }
}

function json(o) {
  return ContentService.createTextOutput(JSON.stringify(o)).setMimeType(ContentService.MimeType.JSON);
}

/* ---------- 枠と残り ---------- */

function slots_() {
  const s = book_().getSheetByName(SHEET_SLOT);
  const rows = s.getDataRange().getValues().slice(1).filter(r => r[0] !== '');
  const used = {};
  resvRows_().forEach(r => { if (r.row[2] === ACTIVE) used[r.row[10]] = (used[r.row[10]] || 0) + 1; });
  const now = new Date();
  return rows.map(r => {
    const label = String(r[0]).trim();
    const start = r[1] instanceof Date ? r[1] : (r[1] ? new Date(r[1]) : null);
    const cap = Number(r[2]) || 0;
    const open = String(r[3]).trim() !== '×' && !(start && start <= now);
    return { label: label, start: start ? start.toISOString() : null, capacity: cap, remaining: Math.max(0, cap - (used[label] || 0)), open: open };
  });
}

function config_() {
  return {
    ok: true,
    title: CONFIG.title,
    products: CONFIG.products,
    ages: CONFIG.ages,
    sources: CONFIG.sources,
    cancelDeadlineHours: CONFIG.cancelDeadlineHours,
    slots: slots_().map(s => ({ label: s.label, start: s.start, remaining: s.remaining, open: s.open })),
  };
}

/* ---------- 予約 ---------- */

function reserve_(b) {
  if (b.website) return { ok: false, error: '送信できませんでした。' }; // 機械的な送信よけ
  const f = {
    name: clean_(b.name, 60), kana: clean_(b.kana, 60), email: clean_(b.email, 120).toLowerCase(),
    address: clean_(b.address, 200), tel: clean_(b.tel, 30), age: clean_(b.age, 20),
    product: clean_(b.product, 40), slot: clean_(b.slot, 60), source: clean_(b.source, 40),
  };
  const miss = Object.keys(f).filter(k => !f[k]);
  if (miss.length) return { ok: false, error: '未入力の項目があります。' };
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(f.email)) return { ok: false, error: 'メールアドレスの形をご確認ください。' };
  if (b.agree !== true) return { ok: false, error: '同意事項へのご同意が必要です。' };
  if (CONFIG.products.indexOf(f.product) < 0 || CONFIG.ages.indexOf(f.age) < 0 || CONFIG.sources.indexOf(f.source) < 0) {
    return { ok: false, error: '選択肢をご確認ください。' };
  }
  const slot = slots_().filter(s => s.label === f.slot)[0];
  if (!slot || !slot.open) return { ok: false, error: 'この日時は受付を終了しました。別の日時をお選びください。' };
  if (slot.remaining <= 0) return { ok: false, error: 'この日時は満席になりました。別の日時をお選びください。' };

  const id = newId_();
  const key = Utilities.getUuid().replace(/-/g, '').slice(0, 20);
  const now = new Date();
  book_().getSheetByName(SHEET_RESV).appendRow([
    id, now, ACTIVE, safe_(f.name), safe_(f.kana), safe_(f.email), safe_(f.address), "'" + f.tel, f.age, f.product, f.slot, f.source, '同意する', '', key,
  ]);

  const link = cancelLink_(id, key);
  mail_(f.email, '【ご予約完了】' + CONFIG.title,
    f.name + ' 様\n\n' + CONFIG.title + 'へのお申し込みありがとうございます。\n以下の内容でご予約を承りました。\n\n' +
    detail_(id, f) +
    '\n■お支払い\n当日現金のみです。お釣りのないようご準備にご協力ください。\n\n' +
    '■キャンセルされる場合\n下のリンクからお手続きください' + deadlineNote_() + '。\n' + link + '\n' +
    '（予約番号とこのメールアドレスでもお手続きできます）\n\n' + CONFIG.organizer);
  if (CONFIG.notifyTo) {
    mail_(CONFIG.notifyTo, '[新規予約] ' + f.slot + ' / ' + f.name, detail_(id, f) + '\n残り ' + (slot.remaining - 1) + ' 席');
  }
  return { ok: true, id: id, key: key, slot: f.slot, product: f.product, name: f.name };
}

/* ---------- 照会・キャンセル ---------- */

function find_(id, key, email) {
  id = String(id || '').trim().toUpperCase();
  if (!id) return null;
  const hit = resvRows_().filter(r => r.row[0] === id)[0];
  if (!hit) return null;
  const okKey = key && String(key) === String(hit.row[14]);
  const okMail = email && String(email).trim().toLowerCase() === String(hit.row[5]).toLowerCase();
  return (okKey || okMail) ? hit : null;
}

function view_(r) {
  return { id: r[0], status: r[2], name: r[3], product: r[9], slot: r[10], age: r[8] };
}

function lookup_(id, key, email) {
  const hit = find_(id, key, email);
  if (!hit) return { ok: false, error: '予約が見つかりませんでした。予約番号とメールアドレスをご確認ください。' };
  const v = view_(hit.row);
  const d = canCancel_(v.slot);
  v.cancelable = v.status === ACTIVE && d.ok;
  if (v.status === ACTIVE && !d.ok) v.note = d.msg;
  return { ok: true, reservation: v };
}

function cancel_(b) {
  const hit = find_(b.id, b.key, b.email);
  if (!hit) return { ok: false, error: '予約が見つかりませんでした。予約番号とメールアドレスをご確認ください。' };
  const r = hit.row;
  if (r[2] === CANCELED) return { ok: true, already: true, reservation: view_(r) };
  const d = canCancel_(r[10]);
  if (!d.ok) return { ok: false, error: d.msg };

  const sh = book_().getSheetByName(SHEET_RESV);
  sh.getRange(hit.index, 3).setValue(CANCELED);
  sh.getRange(hit.index, 14).setValue(new Date());
  r[2] = CANCELED;

  mail_(r[5], '【キャンセル受付】' + CONFIG.title,
    r[3] + ' 様\n\n以下のご予約のキャンセルを承りました。\n\n予約番号：' + r[0] + '\nご希望の日時：' + r[10] + '\nご希望の制作物：' + r[9] +
    '\n\nまたの機会にお会いできるのを楽しみにしております。\n\n' + CONFIG.organizer);
  if (CONFIG.notifyTo) mail_(CONFIG.notifyTo, '[キャンセル] ' + r[10] + ' / ' + r[3], '予約番号：' + r[0] + '\n' + r[10] + ' の枠が1席空きました。');
  return { ok: true, reservation: view_(r) };
}

function canCancel_(label) {
  const slot = slots_().filter(s => s.label === label)[0];
  if (!slot || !slot.start) return { ok: true };
  const limit = new Date(new Date(slot.start).getTime() - CONFIG.cancelDeadlineHours * 3600 * 1000);
  if (new Date() > limit) {
    return { ok: false, msg: 'キャンセル受付期限（開始の' + CONFIG.cancelDeadlineHours + '時間前）を過ぎています。お手数ですが事務局へ直接ご連絡ください。' };
  }
  return { ok: true };
}

/* ---------- 小道具 ---------- */

function book_() {
  return SHEET_ID ? SpreadsheetApp.openById(SHEET_ID) : SpreadsheetApp.getActive();
}

function resvRows_() {
  const v = book_().getSheetByName(SHEET_RESV).getDataRange().getValues();
  const out = [];
  for (let i = 1; i < v.length; i++) out.push({ index: i + 1, row: v[i] });
  return out;
}

function newId_() {
  // 読み違えやすい 0/O・1/I を除いた6文字
  const chars = 'ABCDEFGHJKLMNPQRSTUVWXYZ23456789';
  const used = {};
  resvRows_().forEach(r => { used[r.row[0]] = true; });
  let id;
  do {
    id = '';
    for (let i = 0; i < 6; i++) id += chars.charAt(Math.floor(Math.random() * chars.length));
  } while (used[id]);
  return id;
}

function clean_(v, max) {
  return String(v == null ? '' : v).replace(/[\u0000-\u001f]/g, ' ').trim().slice(0, max);
}

// 「=」などで始まる入力が数式として動かないようにする
function safe_(v) {
  return /^[=+\-@]/.test(v) ? "'" + v : v;
}

function detail_(id, f) {
  return '予約番号：' + id + '\nご希望の日時：' + f.slot + '\nご希望の制作物：' + f.product +
    '\nお名前：' + f.name + '（' + f.kana + '）\n年齢：' + f.age + '\n電話番号：' + f.tel + '\n';
}

function deadlineNote_() {
  return CONFIG.cancelDeadlineHours > 0 ? '（開始の' + CONFIG.cancelDeadlineHours + '時間前まで）' : '';
}

function cancelLink_(id, key) {
  return CONFIG.cancelUrl + '?id=' + encodeURIComponent(id) + '&key=' + encodeURIComponent(key);
}

function mail_(to, subject, body) {
  MailApp.sendEmail({ to: to, subject: subject, body: body, name: CONFIG.organizer });
}
