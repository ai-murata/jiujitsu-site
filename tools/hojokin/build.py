#!/usr/bin/env python3
"""募集中の補助金を jGrants 公開APIから集め、/hojokin/index.html を生成する。

全国ぶんを取得し、絞り込み（都道府県・キーワード・締切）はページ側でおこなう。
標準ライブラリのみ。GitHub Actions から毎日実行する想定。

    python3 tools/hojokin/build.py --out hojokin/index.html
    python3 tools/hojokin/build.py --fixture tools/hojokin/fixtures/sample.json --out -

API: https://developers.digital.go.jp/documents/jgrants/api/
出典表示（Jグランツからの出典である旨）はページ内に必ず入れること。
"""

import argparse
import html
import json
import pathlib
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone

API_BASE = "https://api.jgrants-portal.go.jp/exp/v1/public"
JST = timezone(timedelta(hours=9))
USER_AGENT = "jiujitsu.co.jp-hojokin/1.0 (+https://jiujitsu.co.jp/hojokin/)"
ROOT = pathlib.Path(__file__).resolve().parent

REGIONS = {
    "北海道地方": ["北海道"],
    "東北地方": ["青森県", "岩手県", "宮城県", "秋田県", "山形県", "福島県"],
    "関東・甲信越地方": ["茨城県", "栃木県", "群馬県", "埼玉県", "千葉県", "東京都",
                        "神奈川県", "新潟県", "山梨県", "長野県"],
    "東海・北陸地方": ["富山県", "石川県", "福井県", "岐阜県", "静岡県", "愛知県", "三重県"],
    "近畿地方": ["滋賀県", "京都府", "大阪府", "兵庫県", "奈良県", "和歌山県"],
    "中国地方": ["鳥取県", "島根県", "岡山県", "広島県", "山口県"],
    "四国地方": ["徳島県", "香川県", "愛媛県", "高知県"],
    "九州・沖縄地方": ["福岡県", "佐賀県", "長崎県", "熊本県", "大分県", "宮崎県",
                      "鹿児島県", "沖縄県"],
}
PREFECTURES = [p for prefs in REGIONS.values() for p in prefs]


# --------------------------------------------------------------------------- #
# 取得
# --------------------------------------------------------------------------- #
def fetch_keyword(keyword, timeout=30, retries=3):
    params = {
        "keyword": keyword,
        "sort": "acceptance_end_datetime",
        "order": "ASC",
        "acceptance": "1",
    }
    url = f"{API_BASE}/subsidies?" + urllib.parse.urlencode(params)
    last_error = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return json.loads(resp.read().decode("utf-8")).get("result") or []
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError, TimeoutError) as e:
            last_error = e
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"jGrants API 取得失敗 (keyword={keyword}): {last_error}")


def fetch_detail(subsidy_id, timeout=30, retries=2):
    """詳細API。一覧APIは利用目的・業種・申請URLを返さないので、ここで補う。

    仕様: GET /subsidies/id/{id}
    https://developers.digital.go.jp/documents/jgrants/api/
    """
    url = f"{API_BASE}/subsidies/id/{urllib.parse.quote(subsidy_id)}"
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                payload = json.loads(resp.read().decode("utf-8"))
        except (urllib.error.URLError, urllib.error.HTTPError, ValueError, TimeoutError):
            if attempt < retries - 1:
                time.sleep(1)
            continue
        result = payload.get("result", payload)
        if isinstance(result, list):
            return result[0] if result else None
        return result if isinstance(result, dict) else None
    return None


# 詳細APIから引き継ぐ項目。欠けていても止めない（一覧側の値を残す）。
DETAIL_FIELDS = (
    "use_purpose", "industry", "target_number_of_employees", "target_area_search",
    "subsidy_catch_phrase", "subsidy_max_limit", "institution_name",
    "front_subsidy_detail_page_url",
)


def enrich(items, config, fetcher=fetch_detail):
    """一覧の各件に詳細APIの内容をかぶせる。取れなかった件はそのまま通す。"""
    interval = config.get("detail_interval_seconds", 0.25)
    enriched = 0
    for i, item in enumerate(items):
        if not item.get("id"):
            continue
        if i:
            time.sleep(interval)
        detail = fetcher(item["id"])
        if not detail:
            continue
        enriched += 1
        for key in DETAIL_FIELDS:
            value = detail.get(key)
            if value not in (None, "", []):
                item[key] = value
    return enriched


def collect(config, fetcher=fetch_keyword):
    """全キーワードを引いて id で名寄せする。1語こけても全体は止めない。"""
    merged, errors = {}, []
    interval = config.get("request_interval_seconds", 1.0)
    for i, keyword in enumerate(config["keywords"]):
        if i:
            time.sleep(interval)
        try:
            items = fetcher(keyword)
        except RuntimeError as e:
            errors.append(str(e))
            continue
        for item in items:
            if item.get("id"):
                merged.setdefault(item["id"], dict(item))
    return list(merged.values()), errors


# --------------------------------------------------------------------------- #
# 整形・絞り込み
# --------------------------------------------------------------------------- #
def parse_dt(value):
    if not value or not isinstance(value, str):
        return None
    text = value.strip().replace("Z", "+00:00")
    for candidate in (text, text[:19], text[:10]):
        try:
            dt = datetime.fromisoformat(candidate)
        except ValueError:
            continue
        return dt if dt.tzinfo else dt.replace(tzinfo=JST)
    return None


def industry_values(item):
    """業種。一覧APIは返さないので、詳細APIで補ってから読む。

    多くの補助金が20業種すべてを並べてくるため、一致しても「誰でも対象」以上の
    意味はない。除外には使わず、加点と「使いどころ」の必要条件としてだけ使う。
    """
    return values(item, "industry")


def values(item, key):
    """複数値は「 / 」区切り。値自体が読点を含む（例: 生活関連サービス業、娯楽業）ので読点では割らない。"""
    raw = item.get(key)
    if not raw:
        return []
    if isinstance(raw, list):
        return [str(v).strip() for v in raw if str(v).strip()]
    return [part.strip() for part in re.split(r"\s*/\s*", str(raw)) if part.strip()]


def expand_areas(area_values):
    """対象地域を都道府県の集合に展開する。全国／地方名はその配下すべてに広げる。

    地域欄が空の案件は取りこぼしを避けるため全国扱いにする（表示は「指定なし」）。
    """
    if not area_values:
        return list(PREFECTURES), True
    prefs = set()
    nationwide = False
    for value in area_values:
        if "全国" in value:
            nationwide = True
            prefs.update(PREFECTURES)
            continue
        matched = False
        for region, members in REGIONS.items():
            if region in value:
                prefs.update(members)
                matched = True
        if matched:
            continue
        for pref in PREFECTURES:
            if pref in value:
                prefs.add(pref)
    return sorted(prefs, key=PREFECTURES.index), nationwide


def employees_ok(item, excluded):
    vals = values(item, "target_number_of_employees")
    return not vals or not all(v in excluded for v in vals)


def excluded_by_title(item, words):
    haystack = f"{item.get('title') or ''} {item.get('subsidy_catch_phrase') or ''}"
    return any(w in haystack for w in words)


def score_item(item, config):
    """道場・ジムにとっての近さ。ページの「おすすめ順」に使う。"""
    score = 0
    score += 12 * len(set(values(item, "use_purpose")) & set(config["preferred_use_purposes"]))
    score += 15 * len(set(industry_values(item)) & set(config["preferred_industries"]))
    haystack = f"{item.get('title') or ''} {item.get('subsidy_catch_phrase') or ''}"
    score += 6 * len([w for w in config["title_bonus_keywords"] if w in haystack])
    if any(v in ("5名以下", "20名以下") for v in values(item, "target_number_of_employees")):
        score += 10
    return score


ORG_CODE = re.compile(r"^[A-Z]-?\d+$")


def program_alias(item):
    """制度の通称。

    このAPIは実施機関名を返さない。`name` は内部コード（S-00007152）で、
    `institution_name` は機関名ではなく制度名（「ものづくり補助金」など）だった。
    タイトルに含まれていれば情報が増えないので出さない。
    """
    alias = (item.get("institution_name") or "").strip()
    title = item.get("title") or ""
    if not alias or ORG_CODE.match(alias) or alias in title:
        return ""
    if len(alias) >= len(title):
        return ""  # 通称が本題より長いのは、別制度の名前が紛れ込んでいる（実データにあり）
    return alias


def portal_url(item, config):
    """詳細ページURL。詳細APIが返す正のURLを使い、無いときだけ組み立てる。"""
    url = (item.get("front_subsidy_detail_page_url") or "").strip()
    return url if url.startswith("http") else config["portal_url_template"].format(id=item.get("id"))


def use_hints(item, config, purposes):
    """道場から見た「使いどころ」。書けないときは黙る。

    jGrants の利用目的は「設備整備・IT導入をしたい」が全体の7割に付くような粗い区分で、
    これを頼りに書くと石油精製の補助金に「2店舗目の出店に」と添えてしまう（実データで確認）。
    そこで次の2つを満たしたときだけ書く:

    1. 道場の業種が対象業種に入っていること
    2. タイトルかキャッチに具体的な語（持続化・空き店舗・創業など）が出ていること

    「設備」「省エネ」のような汎用語は、天然ガス設備やZEBの補助金にも当たるため使わない。
    利用目的は、1と2を満たした案件の補足としてのみ添える。
    """
    if not set(industry_values(item)) & set(config["preferred_industries"]):
        return []
    haystack = f"{item.get('title') or ''} {item.get('subsidy_catch_phrase') or ''}"
    hints = []
    for word, hint in config.get("title_hints", []):
        if word in haystack and hint not in hints:
            hints.append(hint)
    if not hints:
        return []
    for purpose in purposes:
        hint = config.get("purpose_hints", {}).get(purpose)
        if hint and hint not in hints:
            hints.append(hint)
    small = config.get("small_business_hint")
    if small and small not in hints and any(
            v in ("5名以下", "20名以下") for v in values(item, "target_number_of_employees")):
        hints.append(small)
    return hints[:3]


def to_records(items, config, now):
    """ページに埋め込む形へ正規化する。"""
    records, dropped = [], {"従業員規模外": 0, "業種違い": 0, "募集終了": 0}
    for item in items:
        end = parse_dt(item.get("acceptance_end_datetime"))
        if end and end < now:
            dropped["募集終了"] += 1
            continue
        if not employees_ok(item, config["exclude_employee_values"]):
            dropped["従業員規模外"] += 1
            continue
        if excluded_by_title(item, config["exclude_title_keywords"]):
            dropped["業種違い"] += 1
            continue
        areas = values(item, "target_area_search")
        prefs, nationwide = expand_areas(areas)
        purposes = values(item, "use_purpose")
        records.append({
            "id": item.get("id") or "",
            "title": item.get("title") or "（名称不明）",
            "alias": program_alias(item),
            "catch": item.get("subsidy_catch_phrase") or "",
            "max": item.get("subsidy_max_limit"),
            "start": (parse_dt(item.get("acceptance_start_datetime")) or now).astimezone(JST).strftime("%Y-%m-%d")
            if item.get("acceptance_start_datetime") else "",
            "end": end.astimezone(JST).strftime("%Y-%m-%d") if end else "",
            "days": (end - now).days if end else None,
            "areas": areas,
            "prefs": prefs,
            "nationwide": nationwide,
            "emp": values(item, "target_number_of_employees"),
            "purpose": purposes,
            "industry": industry_values(item),
            "score": score_item(item, config),
            "hints": use_hints(item, config, purposes),
            "url": portal_url(item, config),
        })
    records.sort(key=lambda r: (r["days"] if r["days"] is not None else 10**6, -r["score"]))
    return records, dropped


# --------------------------------------------------------------------------- #
# ページ生成
# --------------------------------------------------------------------------- #
def embed_json(data):
    """</script> でHTMLが割れないようにしてJSONを埋め込む。"""
    return json.dumps(data, ensure_ascii=False, separators=(",", ":")).replace("<", "\\u003c")


def render_page(records, config, now, errors=()):
    updated = now.astimezone(JST).strftime("%Y年%m月%d日")
    urgent = sum(1 for r in records if r["days"] is not None and 0 <= r["days"] <= config["urgent_days"])
    options = "".join(
        f'<option value="{html.escape(p)}">{html.escape(p)}</option>' for p in PREFECTURES
    )
    note = ""
    if errors:
        note = ('<p class="warn">※ 一部のキーワードで取得に失敗しています。'
                "件数がいつもより少ない場合があります。</p>")
    return TEMPLATE.format(
        updated=updated,
        total=len(records),
        urgent=urgent,
        options=options,
        note=note,
        data=embed_json(records),
        urgent_days=config["urgent_days"],
        generated=now.astimezone(JST).isoformat(timespec="seconds"),
    )


TEMPLATE = """<!DOCTYPE html>
<html lang="ja">
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-H79CRFSZFH"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){{dataLayer.push(arguments);}}
  gtag('js', new Date());
  gtag('config', 'G-H79CRFSZFH');
</script>
<title>道場が使える補助金 | jiujitsu.co.jp</title>
<meta name="description" content="全国の柔術道場・ジムが申請できそうな補助金・助成金を、Jグランツの公開データから毎日自動で集めて都道府県別に探せるようにしました。">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;600;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap">
<style>
  :root {{
    --paper: #ffffff; --panel: #faf8f2; --line: #e7e1d1;
    --gold: #a3801a; --gold-hi: #c9a227; --ink: #17140d;
    --body-c: #5d5745; --faint: #948c74; --urgent: #a8341f;
    --mincho: "Shippori Mincho", "Hiragino Mincho ProN", serif;
    --gothic: "Zen Kaku Gothic New", "Hiragino Kaku Gothic ProN", sans-serif;
  }}
  * {{ box-sizing: border-box; }}
  body {{ background: var(--paper); color: var(--body-c); font-family: var(--gothic); line-height: 1.9; margin: 0; -webkit-font-smoothing: antialiased; }}
  .wrap {{ max-width: 880px; margin: 0 auto; padding: 0 24px; }}
  a {{ color: var(--gold); }}

  header {{ text-align: center; padding: 72px 24px 40px; position: relative; }}
  header::before {{ content: ""; position: absolute; inset: 0; background: radial-gradient(ellipse 70% 60% at 50% 30%, rgba(201,162,39,.08), transparent 70%); pointer-events: none; }}
  .eyebrow {{ font-family: var(--mincho); font-size: 12px; letter-spacing: .24em; color: var(--gold); margin: 0 0 14px; }}
  h1 {{ font-family: var(--mincho); font-weight: 600; font-size: clamp(30px, 6vw, 46px); line-height: 1.25; letter-spacing: .04em; color: var(--ink); margin: 0; }}
  .lead {{ font-size: 14px; margin: 24px auto 0; max-width: 34em; text-wrap: pretty; }}
  .back {{ display: inline-block; margin-top: 26px; font-size: 12px; letter-spacing: .1em; text-decoration: none; }}
  .back:hover {{ text-decoration: underline; }}

  .rank {{ display: flex; height: 4px; }}
  .rank span {{ flex: 1; }}
  .rank .w {{ background: #eceadf; }} .rank .b {{ background: #274a7a; }} .rank .p {{ background: #4d3070; }}
  .rank .br {{ background: #5a3c22; }} .rank .k {{ background: #17140d; }}

  main.wrap {{ padding: 40px 24px 80px; }}
  .meta {{ font-size: 12.5px; color: var(--faint); letter-spacing: .04em; margin: 0 0 22px; }}
  .meta b {{ color: var(--ink); font-family: var(--mincho); font-size: 15px; }}
  .meta span {{ white-space: nowrap; }}
  .warn {{ font-size: 12.5px; color: var(--urgent); margin: 0 0 18px; }}

  .controls {{ background: var(--panel); border: 1px solid var(--line); padding: 18px 20px; display: grid; grid-template-columns: repeat(auto-fit, minmax(190px, 1fr)); gap: 14px 18px; align-items: end; position: sticky; top: 0; z-index: 5; }}
  .field {{ display: grid; gap: 6px; }}
  .field label {{ font-size: 11px; letter-spacing: .18em; color: var(--gold); font-weight: 700; }}
  .field select, .field input[type=search] {{ font-family: var(--gothic); font-size: 14px; color: var(--ink); background: var(--paper); border: 1px solid var(--line); padding: 9px 10px; width: 100%; }}
  .field select:focus, .field input:focus {{ outline: 2px solid var(--gold); outline-offset: 1px; }}
  .check {{ display: flex; align-items: center; gap: 8px; font-size: 13px; padding-bottom: 9px; }}
  .check input {{ accent-color: var(--gold); width: 16px; height: 16px; }}

  .count {{ font-size: 12.5px; color: var(--faint); margin: 20px 0 14px; letter-spacing: .06em; }}
  .list {{ display: grid; gap: 14px; }}
  .item {{ background: var(--panel); border: 1px solid var(--line); border-left: 3px solid var(--line); padding: 20px 22px; }}
  .item.is-urgent {{ border-left-color: var(--urgent); }}
  .item.is-wide {{ border-left-color: var(--gold); }}
  .item h2 {{ font-family: var(--mincho); font-weight: 700; font-size: 17px; line-height: 1.6; color: var(--ink); letter-spacing: .04em; margin: 0 0 6px; }}
  .item h2 a {{ text-decoration: none; color: inherit; }}
  .item h2 a:hover {{ color: var(--gold); text-decoration: underline; }}
  .org {{ font-size: 12px; color: var(--faint); margin: 0 0 12px; }}
  .catch {{ font-size: 13px; margin: 0 0 12px; }}
  .facts {{ display: flex; flex-wrap: wrap; gap: 6px 18px; font-size: 12.5px; margin: 0 0 10px; padding: 0; list-style: none; }}
  .facts b {{ font-family: var(--mincho); color: var(--ink); font-weight: 700; margin-right: 6px; letter-spacing: .04em; }}
  .deadline.urgent {{ color: var(--urgent); font-weight: 700; }}
  .hints {{ background: rgba(201,162,39,.07); border-left: 2px solid var(--gold-hi); margin: 0 0 12px; padding: 10px 14px; list-style: none; }}
  .hints li {{ font-size: 12.5px; line-height: 1.75; color: var(--ink); }}
  .hints li + li {{ margin-top: 2px; }}
  .hints-label {{ display: block; font-family: var(--mincho); font-size: 10.5px; letter-spacing: .18em; color: var(--gold); margin-bottom: 3px; }}
  .tags {{ display: flex; flex-wrap: wrap; gap: 6px; margin: 12px 0 0; }}
  .tag {{ font-size: 10.5px; letter-spacing: .06em; color: var(--gold); border: 1px solid rgba(163,128,26,.35); border-radius: 999px; padding: 2px 10px; }}
  .empty {{ background: var(--panel); border: 1px solid var(--line); padding: 40px 24px; text-align: center; font-size: 13.5px; }}

  footer.wrap {{ border-top: 1px solid var(--line); margin-top: 64px; padding: 28px 24px 60px; font-size: 12px; color: var(--faint); }}
  footer p {{ margin: 0 0 8px; max-width: 46em; }}
  @media (max-width: 660px) {{
    .controls {{ position: static; }}
    header {{ padding-top: 56px; }}
  }}
</style>

<div class="rank"><span class="w"></span><span class="b"></span><span class="p"></span><span class="br"></span><span class="k"></span></div>

<header>
  <p class="eyebrow">HOJOKIN</p>
  <h1>道場が使える補助金</h1>
  <p class="lead">全国の柔術道場・ジムが申請できそうな補助金を、国の公開データ（Jグランツ）から毎日自動で集めています。マットの入れ替え、更衣室の改修、予約システムの導入、スタッフ採用——「これ、補助金出るのでは？」を探すための一覧です。</p>
  <a class="back" href="/">← jiujitsu.co.jp</a>
</header>

<main class="wrap">
  <p class="meta"><span><b>{updated}</b> 更新</span> ／ <span>掲載 <b>{total}</b> 件</span> ／ <span>締切{urgent_days}日以内 <b>{urgent}</b> 件</span></p>
  {note}

  <div class="controls">
    <div class="field">
      <label for="pref">都道府県</label>
      <select id="pref">
        <option value="">すべて</option>
        {options}
      </select>
    </div>
    <div class="field">
      <label for="q">キーワード</label>
      <input id="q" type="search" placeholder="設備、人材、IT など" autocomplete="off">
    </div>
    <div class="field">
      <label for="sort">並び順</label>
      <select id="sort">
        <option value="deadline">締切が近い順</option>
        <option value="score">道場向き順</option>
        <option value="amount">上限額が大きい順</option>
      </select>
    </div>
    <label class="check"><input type="checkbox" id="urgentOnly">締切間近のみ</label>
    <label class="check"><input type="checkbox" id="dojoOnly">道場向きのみ</label>
  </div>

  <p class="count" id="count"></p>
  <div class="list" id="list"></div>
</main>

<footer class="wrap">
  <p>出典: <a href="https://www.jgrants-portal.go.jp/" rel="noopener">Jグランツ（jGrants）</a>公開API。デジタル庁が公開する補助金データを毎日取得して掲載しています。</p>
  <p>掲載は募集中（受付期間内）のものに限っています。対象地域・従業員数・業種でおおまかに絞り込んでいますが、<strong>申請できるかどうかは必ず公募要領の原文で確認してください</strong>。金額・締切・要件の最終的な正はJグランツ側にあります。</p>
  <p>生成日時: {generated} ／ <a href="/">jiujitsu.co.jp</a></p>
</footer>

<script>
const DATA = {data};
const URGENT_DAYS = {urgent_days};

const listEl = document.getElementById('list');
const countEl = document.getElementById('count');
const prefEl = document.getElementById('pref');
const qEl = document.getElementById('q');
const sortEl = document.getElementById('sort');
const urgentEl = document.getElementById('urgentOnly');
const dojoEl = document.getElementById('dojoOnly');

function yen(v) {{
  const n = Number(v);
  if (!v || Number.isNaN(n)) return '記載なし';
  if (n >= 100000000) return (n / 100000000).toFixed(1).replace(/\\.0$/, '') + '億円';
  if (n >= 10000) return Math.round(n / 10000).toLocaleString() + '万円';
  return n.toLocaleString() + '円';
}}

function esc(s) {{
  return String(s == null ? '' : s).replace(/[&<>"']/g, c => (
    {{ '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }}[c]
  ));
}}

function matches(r) {{
  const pref = prefEl.value;
  if (pref && !r.prefs.includes(pref)) return false;
  if (urgentEl.checked && !(r.days !== null && r.days <= URGENT_DAYS)) return false;
  if (dojoEl.checked && !r.hints.length) return false;
  const q = qEl.value.trim();
  if (q) {{
    const hay = [r.title, r.alias, r.catch, r.purpose.join(' '), r.industry.join(' ')].join(' ');
    if (!hay.toLowerCase().includes(q.toLowerCase())) return false;
  }}
  return true;
}}

function sortRows(rows) {{
  const mode = sortEl.value;
  const copy = rows.slice();
  if (mode === 'score') copy.sort((a, b) => b.score - a.score || (a.days ?? 1e6) - (b.days ?? 1e6));
  else if (mode === 'amount') copy.sort((a, b) => (Number(b.max) || 0) - (Number(a.max) || 0));
  else copy.sort((a, b) => (a.days ?? 1e6) - (b.days ?? 1e6) || b.score - a.score);
  return copy;
}}

function row(r) {{
  const urgent = r.days !== null && r.days <= URGENT_DAYS;
  const deadline = r.end
    ? esc(r.end) + (r.days !== null ? '（あと' + r.days + '日）' : '')
    : '未定';
  const area = r.nationwide ? (r.areas.length ? '全国' : '指定なし') : esc(r.areas.join('／') || '—');
  const tags = r.purpose.concat(r.emp.length ? ['従業員 ' + r.emp.join('・')] : [])
    .slice(0, 5)
    .map(t => '<span class="tag">' + esc(t) + '</span>').join('');
  return [
    '<article class="item' + (urgent ? ' is-urgent' : (r.nationwide ? ' is-wide' : '')) + '">',
    '<h2><a href="' + esc(r.url) + '" rel="noopener" target="_blank">' + esc(r.title) + '</a></h2>',
    r.alias ? '<p class="org">通称: ' + esc(r.alias) + '</p>' : '',
    r.catch ? '<p class="catch">' + esc(r.catch) + '</p>' : '',
    r.hints.length
      ? '<ul class="hints"><span class="hints-label">使いどころ</span>'
        + r.hints.map(h => '<li>' + esc(h) + '</li>').join('') + '</ul>'
      : '',
    '<ul class="facts">',
    '<li><b>上限</b>' + yen(r.max) + '</li>',
    '<li class="deadline' + (urgent ? ' urgent' : '') + '"><b>締切</b>' + deadline + '</li>',
    '<li><b>対象</b>' + area + '</li>',
    '</ul>',
    tags ? '<div class="tags">' + tags + '</div>' : '',
    '</article>'
  ].join('');
}}

function render() {{
  const rows = sortRows(DATA.filter(matches));
  countEl.textContent = rows.length + ' 件';
  listEl.innerHTML = rows.length
    ? rows.map(row).join('')
    : '<p class="empty">条件に合う補助金が見つかりませんでした。都道府県を「すべて」に戻すか、キーワードを短くしてみてください。</p>';
}}

[prefEl, qEl, sortEl, urgentEl, dojoEl].forEach(el => {{
  el.addEventListener('input', render);
  el.addEventListener('change', render);
}});
render();
</script>
</html>
"""


# --------------------------------------------------------------------------- #
# CLI
# --------------------------------------------------------------------------- #
def main(argv=None):
    parser = argparse.ArgumentParser(description="補助金ページを生成する")
    parser.add_argument("--config", default=str(ROOT / "config.json"))
    parser.add_argument("--out", default="-", help="出力先（- で標準出力）")
    parser.add_argument("--fixture", help="APIを叩かずこのJSONを使う（テスト用）")
    parser.add_argument("--json-out", help="抽出結果をJSONでも書き出す")
    args = parser.parse_args(argv)

    config = json.loads(pathlib.Path(args.config).read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc).astimezone(JST)
    errors = []

    if args.fixture:
        raw = json.loads(pathlib.Path(args.fixture).read_text(encoding="utf-8"))
        items = raw.get("result", raw) if isinstance(raw, dict) else raw
        details = raw.get("details") if isinstance(raw, dict) else None
        if details:
            enrich(items, dict(config, detail_interval_seconds=0),
                   fetcher=details.get)
    else:
        items, errors = collect(config)
        if errors and not items:
            print("\n".join(errors), file=sys.stderr)
            return 1
        enriched = enrich(items, config)
        print(f"詳細API: {enriched}/{len(items)}件を補完", file=sys.stderr)

    records, dropped = to_records(items, config, now)
    page = render_page(records, config, now, errors)

    if args.out == "-":
        sys.stdout.write(page)
    else:
        out = pathlib.Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(page, encoding="utf-8")
        print(f"{out}: {len(records)}件 (除外: {dropped})", file=sys.stderr)
    if args.json_out:
        pathlib.Path(args.json_out).write_text(
            json.dumps(records, ensure_ascii=False, indent=1), encoding="utf-8"
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
