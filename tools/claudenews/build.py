#!/usr/bin/env python3
"""Claude（Anthropic）に関する国内と海外のニュースを毎朝集め、日本語でまとめて /claudenews/ を生成する。

1. config.json の RSS から、直近 lookback_hours 時間ぶんの記事を集める（取得は標準ライブラリのみ）
2. Claude に「新モデル・新サービスを優先して記事を選び、日本語で見出し・要約・ポイントを書く」よう頼む
   （海外の英語記事はここで日本語になる）
3. data/claudenews/editions/YYYY-MM-DD.json に保存し、そこから HTML を作り直す

    python3 tools/claudenews/build.py                  # 取得 → 要約 → ページ生成（ANTHROPIC_API_KEY が要る）
    python3 tools/claudenews/build.py --render-only    # 保存済みの号からページだけ作り直す
    python3 tools/claudenews/build.py --fixture-dir tools/claudenews/fixtures --fake-llm --root /tmp/jn
                                                    # ネットワークもAPIも使わずに試す

リンクURL・出典名・国内/海外の別は、Claude の返答ではなく取得した RSS の値を使う。
Claude に任せるのは「どれを載せるか」と「日本語の文章」だけ。
"""

import argparse
import hashlib
import html
import json
import os
import pathlib
import re
import sys
import time
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timedelta, timezone
from email.utils import parsedate_to_datetime

JST = timezone(timedelta(hours=9))
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
USER_AGENT = "Mozilla/5.0 (compatible; jiujitsu.co.jp-claudenews/1.0; +https://jiujitsu.co.jp/claudenews/)"

CATEGORIES = ["新モデル", "新機能・サービス", "Claude Code", "料金・プラン", "提携・会社", "研究・安全性", "その他"]
REGION_LABEL = {"jp": "国内", "intl": "海外"}
WEEKDAYS = "月火水木金土日"


# --------------------------------------------------------------------------- #
# 取得
# --------------------------------------------------------------------------- #
def fetch_url(url, timeout=30, retries=3):
    last_error = None
    for attempt in range(retries):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                return resp.read()
        except (urllib.error.URLError, urllib.error.HTTPError, TimeoutError, ConnectionError) as e:
            last_error = e
            if attempt < retries - 1:
                time.sleep(2 ** attempt)
    raise RuntimeError(f"取得失敗 ({url}): {last_error}")


def strip_html(text, limit=600):
    if not text:
        return ""
    text = re.sub(r"<(script|style)\b.*?</\1>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = html.unescape(text)
    text = re.sub(r"\s+", " ", text).strip()
    if len(text) > limit:
        text = text[:limit].rstrip() + "…"
    return text


def parse_date(value):
    if not value:
        return None
    value = value.strip()
    try:
        dt = parsedate_to_datetime(value)
    except (TypeError, ValueError):
        dt = None
    if dt is None:
        try:
            dt = datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None
    return dt if dt.tzinfo else dt.replace(tzinfo=timezone.utc)


def _local(tag):
    return tag.rsplit("}", 1)[-1]


def _child(el, name):
    for c in el:
        if _local(c.tag) == name:
            return c
    return None


def _text(el, name):
    c = _child(el, name)
    return (c.text or "").strip() if c is not None and c.text else ""


def item_id(link, title):
    return hashlib.sha1((link or title).encode("utf-8")).hexdigest()[:12]


def parse_feed(data, feed):
    """RSS 2.0 と Atom の両方を読む。壊れた1件は飛ばす。"""
    # WordPress のフィードには、XML宣言の前に空行や BOM が入っているものがある（BJJEE など）
    root = ET.fromstring(data.lstrip(b"\xef\xbb\xbf \t\r\n"))
    entries = [el for el in root.iter() if _local(el.tag) in ("item", "entry")]
    out = []
    for el in entries:
        title = strip_html(_text(el, "title"), limit=300)
        link = _text(el, "link")
        if not link:
            link_el = _child(el, "link")
            if link_el is not None:
                link = link_el.get("href", "")
        if not title or not link.startswith(("http://", "https://")):
            continue
        source = feed["name"]
        source_el = _child(el, "source")
        if source_el is not None and (source_el.text or "").strip():
            # Googleニュースは元の媒体名を <source> に入れ、タイトル末尾にも「 - 媒体名」を付ける
            source = source_el.text.strip()
            suffix = f" - {source}"
            if title.endswith(suffix):
                title = title[: -len(suffix)].rstrip()
        snippet = ""
        for name in ("encoded", "description", "summary", "content"):
            snippet = strip_html(_text(el, name))
            if snippet:
                break
        if snippet == title or snippet.startswith(title + " " + source):
            snippet = ""  # Googleニュースの description はタイトルの繰り返しでしかない
        published = parse_date(_text(el, "pubDate") or _text(el, "published") or _text(el, "updated"))
        out.append({
            "id": item_id(link, title),
            "region": feed["region"],
            "feed": feed["name"],
            "source": source,
            "title": title,
            "link": link,
            "snippet": snippet,
            "published": published.isoformat() if published else "",
        })
    return out


def normalize_title(title):
    return re.sub(r"[\W_]+", "", title.lower())


def collect(config, now, seen, fetcher=fetch_url):
    """全フィードから候補を集める。古いもの・既出・同じ見出しは落とす。1つこけても止めない。"""
    since = now - timedelta(hours=config.get("lookback_hours", 36))
    per_feed = config.get("max_candidates_per_feed", 25)
    candidates, errors, titles = [], [], set()
    for feed in config["feeds"]:
        try:
            items = parse_feed(fetcher(feed["url"]), feed)
        except (RuntimeError, ET.ParseError) as e:
            errors.append(f"{feed['name']}: {e}")
            continue
        kept = 0
        for item in items:
            if kept >= per_feed:
                break
            if item["id"] in seen:
                continue
            if item["published"] and datetime.fromisoformat(item["published"]) < since:
                continue
            key = normalize_title(item["title"])
            if key in titles:
                continue
            titles.add(key)
            candidates.append(item)
            kept += 1
    return candidates, errors


# --------------------------------------------------------------------------- #
# Claude で選んで日本語にする
# --------------------------------------------------------------------------- #
SYSTEM_PROMPT = """\
あなたは、Claude を使って仕事や暮らしを工夫しているサイト「Jiu Labo」の編集担当です。
毎朝、Claude（Anthropic 社の AI）に関する国内と海外のニュースを「Claude を使っている人・これから始める人」向けに、
やさしい日本語で紹介する「きょうの Claude ニュース」を作ります。

## 選び方
- 渡された候補の中から、Claude や Anthropic に直接関係するものだけを選んでください。
- 読者がいちばん知りたいのは次の2つです。候補にあれば必ず選び、いちばん上に並べてください。
  1. 新しいモデルの発表・リリース（例：Claude Opus／Sonnet／Haiku／Fable の新しい版）
  2. 新しいサービス・機能の開始（例：Claude Marketplace、アプリや Claude Code の新機能、コネクタ、プラグイン）
- その次に、料金・使用枠の変更、提携、研究・安全性の発表など、Claude の使い方に関わるものを選んでください。
- 次のものは選ばないでください：株価・資金調達のうわさだけの記事、Claude が一言出てくるだけの AI 業界全般の記事、
  「Claude」という名前の別の人物・商品の話題、広告・通販ページ、ハウツーの宣伝記事。
- 同じ出来事を扱う候補が複数あれば、情報が多いものを1つだけ選んでください。
- 国内（region=jp）は最大 {max_jp} 件、海外（region=intl）は最大 {max_intl} 件。
  良い候補がなければ少なくてかまいません。0件でもかまいません。

## 書き方
- すべて日本語で書いてください。英語の記事は日本語に訳したうえで要約します。
- 渡された見出しと抜粋に書かれていることだけを使ってください。書かれていない数字・性能・料金・日付・発言を
  補ったり推測したりしないでください。抜粋が短いときは、要約も短くてかまいません。
- 原文をそのまま長く訳し写さず、自分の言葉で短くまとめてください。
- モデル名・製品名は原語のまま書き、はじめて出るときは必要に応じて短い説明を添えてください。
  例：Claude Code（プログラミング用の Claude）
- 「です・ます」調で、AI にくわしくない人にも伝わるように。専門用語には短い補足を。
- title：日本語の見出し。40字以内。
- summary：何があったか。2〜4文。
- point：Claude を使っている人にとって何が変わるか、知っておくとよいことを1文で。
  抜粋から言えることがなければ、空文字にしてください。
- category：{categories} のどれか。
- lead：その日のニュース全体をひとことで紹介する1〜2文。選んだ記事が0件なら空文字。
"""

OUTPUT_SCHEMA = {
    "type": "object",
    "properties": {
        "lead": {"type": "string"},
        "items": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "string"},
                    "category": {"type": "string", "enum": CATEGORIES},
                    "title": {"type": "string"},
                    "summary": {"type": "string"},
                    "point": {"type": "string"},
                },
                "required": ["id", "category", "title", "summary", "point"],
                "additionalProperties": False,
            },
        },
    },
    "required": ["lead", "items"],
    "additionalProperties": False,
}


def build_prompt(candidates, config):
    system = SYSTEM_PROMPT.format(
        max_jp=config.get("max_items_jp", 5),
        max_intl=config.get("max_items_intl", 6),
        categories="／".join(CATEGORIES),
    )
    rows = [
        {k: c[k] for k in ("id", "region", "source", "title", "snippet", "published")}
        for c in candidates
    ]
    user = (
        "今日の候補です。選んだ記事は、渡した順ではなく、読者にとって大事な順に並べてください。\n\n"
        + json.dumps(rows, ensure_ascii=False, indent=1)
    )
    return system, user


class Refused(RuntimeError):
    pass


def call_claude(system, user, config):
    import anthropic  # 実行時だけ必要。テストとページ生成は SDK なしで動く

    client = anthropic.Anthropic()
    response = client.beta.messages.create(
        model=config.get("model", "claude-opus-5-5"),
        max_tokens=16000,
        system=system,
        messages=[{"role": "user", "content": user}],
        output_config={
            "effort": config.get("effort", "medium"),
            "format": {"type": "json_schema", "schema": OUTPUT_SCHEMA},
        },
        betas=["server-side-fallback-2026-07-01"],
        fallbacks="default",
    )
    if response.stop_reason == "refusal":
        raise Refused(f"Claude が応答を断りました: {response.stop_details}")
    if response.stop_reason == "max_tokens":
        raise RuntimeError("応答が max_tokens で途切れました")
    text = next(b.text for b in response.content if b.type == "text")
    return json.loads(text)


def fake_claude(system, user, config):
    """--fake-llm 用。候補の先頭から機械的に選ぶだけ（見た目の確認用）。"""
    rows = json.loads(user.split("\n\n", 1)[1])
    items = []
    for row in rows[:6]:
        items.append({
            "id": row["id"],
            "category": "その他",
            "title": f"（仮）{row['title'][:36]}",
            "summary": row["snippet"][:120] or "（要約の見本）",
            "point": "",
        })
    return {"lead": "（見本）きょうのニュースです。", "items": items}


def to_edition(result, candidates, date, config, now):
    """Claude の返答を検算しながら号にする。URL・出典・地域は候補側の値だけを使う。"""
    by_id = {c["id"]: c for c in candidates}
    limits = {"jp": config.get("max_items_jp", 5), "intl": config.get("max_items_intl", 6)}
    counts = {"jp": 0, "intl": 0}
    items, used = [], set()
    for r in result.get("items", []):
        c = by_id.get(r.get("id"))
        if not c or c["id"] in used:
            continue  # 知らない id（でっち上げ）や重複は捨てる
        if counts[c["region"]] >= limits[c["region"]]:
            continue
        title = (r.get("title") or "").strip()
        summary = (r.get("summary") or "").strip()
        if not title or not summary:
            continue
        used.add(c["id"])
        counts[c["region"]] += 1
        items.append({
            "id": c["id"],
            "region": c["region"],
            "category": r.get("category") if r.get("category") in CATEGORIES else "その他",
            "title": title,
            "summary": summary,
            "point": (r.get("point") or "").strip(),
            "source": c["source"],
            "original_title": c["title"],
            "link": c["link"],
            "published": c["published"],
        })
    return {
        "date": date,
        "generated_at": now.astimezone(JST).isoformat(timespec="seconds"),
        "lead": (result.get("lead") or "").strip() if items else "",
        "items": items,
    }


# --------------------------------------------------------------------------- #
# 保存
# --------------------------------------------------------------------------- #
def editions_dir(root):
    return root / "data" / "claudenews" / "editions"


def load_editions(root):
    out = []
    for path in sorted(editions_dir(root).glob("*.json"), reverse=True):
        ed = json.loads(path.read_text(encoding="utf-8"))
        if ed.get("items"):
            out.append(ed)
    return out


def load_seen(root):
    path = root / "data" / "claudenews" / "seen.json"
    if not path.exists():
        return {}
    return json.loads(path.read_text(encoding="utf-8")).get("seen", {})


def save_seen(root, seen, today, keep_days):
    """一度候補に出した記事は、載せなかったものも含めて覚えておく（翌日また悩まないように）。"""
    cutoff = (datetime.fromisoformat(today) - timedelta(days=keep_days)).date().isoformat()
    seen = {k: v for k, v in seen.items() if v >= cutoff}
    path = root / "data" / "claudenews" / "seen.json"
    path.parent.mkdir(parents=True, exist_ok=True)
    body = {"_説明": "候補に出た記事のid（リンクのハッシュ）と日付。翌日以降に同じ記事を拾わないために使う。",
            "seen": dict(sorted(seen.items()))}
    path.write_text(json.dumps(body, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


def write_edition(root, edition):
    d = editions_dir(root)
    d.mkdir(parents=True, exist_ok=True)
    path = d / f"{edition['date']}.json"
    path.write_text(json.dumps(edition, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return path


# --------------------------------------------------------------------------- #
# ページ生成
# --------------------------------------------------------------------------- #
def esc(text):
    return html.escape(text or "", quote=True)


def safe_url(url):
    return url if isinstance(url, str) and url.startswith(("https://", "http://")) else "#"


def date_label(date):
    d = datetime.fromisoformat(date)
    return f"{d.year}.{d.month:02d}.{d.day:02d}（{WEEKDAYS[d.weekday()]}）"


HEAD = """<!DOCTYPE html>
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

<title>{title}</title>
<link rel="icon" href="/favicon.ico" sizes="48x48">
<link rel="icon" href="/assets/icon-192.png" type="image/png" sizes="192x192">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="description" content="{description}">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;600;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap">
<style>
  :root {{
    --paper: #ffffff; --panel: #faf8f2; --line: #e7e1d1;
    --gold: #a3801a; --gold-hi: #c9a227;
    --ink: #17140d; --body-c: #4d4737; --faint: #948c74;
    --jp: #274a7a; --intl: #4d3070;
    --mincho: "Shippori Mincho", "Hiragino Mincho ProN", serif;
    --gothic: "Zen Kaku Gothic New", "Hiragino Kaku Gothic ProN", sans-serif;
    --w: #eceadf; --b: #274a7a; --p: #4d3070; --br: #5a3c22; --k: #17140d;
  }}
  * {{ box-sizing: border-box; }}
  body {{ background: var(--paper); color: var(--body-c); font-family: var(--gothic); line-height: 1.9; margin: 0; -webkit-font-smoothing: antialiased; }}
  .wrap {{ max-width: 680px; margin: 0 auto; padding: 0 22px 80px; }}
  a {{ color: var(--gold); }}

  header {{ text-align: center; padding: 64px 20px 40px; }}
  .brand {{ font-size: 11px; letter-spacing: .3em; color: var(--gold); font-weight: 500; margin: 0; }}
  .brand a {{ color: inherit; text-decoration: none; }}
  h1 {{ font-family: var(--mincho); font-weight: 700; font-size: clamp(26px, 6vw, 38px); color: var(--ink); letter-spacing: .12em; margin: 10px 0 12px; }}
  .lede {{ font-size: 13px; color: var(--faint); margin: 0; letter-spacing: .06em; }}

  .rank {{ display: flex; height: 4px; }}
  .rank span {{ flex: 1; }}
  .rank .w {{ background: var(--w); }} .rank .b {{ background: var(--b); }} .rank .p {{ background: var(--p); }}
  .rank .br {{ background: var(--br); }} .rank .k {{ background: var(--k); }}

  .edition-head {{ margin: 44px 0 0; }}
  .edition-head h2 {{ font-family: var(--mincho); font-size: 22px; color: var(--ink); letter-spacing: .06em; margin: 2px 0 10px; }}
  .edition-lead {{ background: var(--panel); border-left: 3px solid var(--gold); padding: 14px 18px; margin: 0; font-size: 14.5px; }}

  .group {{ margin: 36px 0 0; }}
  .group-label {{ font-size: 12px; font-weight: 700; letter-spacing: .2em; margin: 0 0 4px; }}
  .group-label.jp {{ color: var(--jp); }} .group-label.intl {{ color: var(--intl); }}
  .items {{ list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--line); }}
  .item {{ padding: 22px 2px; border-bottom: 1px solid var(--line); }}
  .tags {{ display: flex; gap: 6px; flex-wrap: wrap; margin: 0 0 4px; }}
  .tag {{ font-size: 10.5px; font-weight: 700; letter-spacing: .08em; border-radius: 3px; padding: 0 7px; line-height: 1.8; border: 1px solid var(--line); color: var(--faint); }}
  .tag.jp {{ background: var(--jp); color: #fff; border-color: var(--jp); }}
  .tag.intl {{ background: var(--intl); color: #fff; border-color: var(--intl); }}
  .item h3 {{ font-family: var(--mincho); font-weight: 700; font-size: 18px; color: var(--ink); letter-spacing: .04em; line-height: 1.6; margin: 4px 0 8px; word-break: auto-phrase; text-wrap: pretty; }}
  .item p {{ margin: 0 0 8px; font-size: 14.5px; }}
  .point {{ font-size: 13.5px !important; background: var(--panel); border-radius: 6px; padding: 8px 12px; }}
  .point b {{ color: var(--gold); margin-right: 6px; }}
  .src {{ font-size: 12px !important; color: var(--faint); margin: 10px 0 0 !important; line-height: 1.7; }}
  .src a {{ font-weight: 700; text-decoration: none; }}
  .src a:hover {{ text-decoration: underline; }}
  .orig {{ display: block; font-style: italic; overflow-wrap: anywhere; }}

  .empty {{ text-align: center; background: var(--panel); border-radius: 8px; padding: 36px 20px; margin: 44px 0 0; font-size: 14px; }}

  .archive {{ margin: 64px 0 0; }}
  .archive h2 {{ font-family: var(--mincho); font-size: 18px; color: var(--ink); letter-spacing: .1em; margin: 0 0 8px; }}
  .archive ul {{ list-style: none; margin: 0; padding: 0; border-top: 1px solid var(--line); }}
  .archive a {{ display: block; padding: 14px 4px; border-bottom: 1px solid var(--line); text-decoration: none; color: inherit; }}
  .archive a:hover b {{ color: var(--gold); }}
  .archive time {{ font-size: 12px; color: var(--faint); letter-spacing: .08em; font-variant-numeric: tabular-nums; }}
  .archive b {{ display: block; font-size: 14px; color: var(--ink); font-weight: 500; line-height: 1.7; }}
  .archive .count {{ font-size: 12px; color: var(--faint); }}

  .pager {{ display: flex; justify-content: space-between; gap: 12px; margin: 40px 0 0; font-size: 13px; }}
  .note {{ margin: 56px 0 0; font-size: 12px; color: var(--faint); line-height: 1.9; }}

  footer {{ margin-top: 56px; border-top: 1px solid var(--line); padding: 30px 0 0; text-align: center; font-size: 12px; letter-spacing: .1em; color: var(--faint); line-height: 2; }}
  footer a {{ color: var(--gold); text-decoration: none; }}
  footer a:hover {{ text-decoration: underline; }}

  @media (max-width: 560px) {{
    header {{ padding: 36px 18px 26px; }}
    .edition-head {{ margin-top: 28px; }}
    .edition-head h2 {{ font-size: 19px; }}
    .item {{ padding: 18px 0; }}
    .item h3 {{ font-size: 16.5px; }}
    .item p {{ font-size: 14px; }}
  }}
  /* スマホで小さい字と押しにくいボタンを底上げ（~/.claude/scripts/sp_readable.py と同じ値） */
  @media (max-width:640px){{.tag{{font-size:12px}}}}
</style>

<header>
  <p class="brand"><a href="/">JIUJITSU.CO.JP</a></p>
  <h1>きょうの Claude ニュース</h1>
  <p class="lede">新しいモデルやサービスを中心に、Claude のニュースを毎朝やさしい日本語で。</p>
</header>

<div class="rank" aria-hidden="true"><span class="w"></span><span class="b"></span><span class="p"></span><span class="br"></span><span class="k"></span></div>

<div class="wrap">
"""

NOTE = """  <p class="note">
    ※ 各ニュースは、公開されている記事の見出しと冒頭部分をもとに、AI（Claude）が選んで日本語で要約したものです。
    海外の記事はAIが翻訳しています。訳や要約にまちがいがある場合があるので、くわしくは必ず元の記事でご確認ください。
    記事の著作権は各媒体に帰属します。
  </p>
"""

FOOT = """  <footer>
    <a href="/claudenews/">Claude ニュースの一覧へ</a>　／　<a href="/blog/">ブログ</a>　／　<a href="/">jiujitsu.co.jp トップへ</a>
    <br>© 2026 BUTTI ON LINE Inc.
  </footer>
</div>
"""


def render_item(item):
    region = item["region"]
    source_lang = "英語" if region == "intl" else ""
    src_label = esc(item["source"]) + (f"（{source_lang}）" if source_lang else "")
    parts = [
        '    <li class="item">',
        '      <p class="tags">'
        f'<span class="tag {region}">{REGION_LABEL.get(region, "")}</span>'
        f'<span class="tag">{esc(item["category"])}</span></p>',
        f'      <h3>{esc(item["title"])}</h3>',
        f'      <p>{esc(item["summary"])}</p>',
    ]
    if item.get("point"):
        parts.append(f'      <p class="point"><b>ここがポイント</b>{esc(item["point"])}</p>')
    orig = ""
    if region == "intl" and item.get("original_title"):
        orig = f'<span class="orig" lang="en">{esc(item["original_title"])}</span>'
    parts.append(
        f'      <p class="src">出典：{src_label}　'
        f'<a href="{esc(safe_url(item["link"]))}" target="_blank" rel="noopener">元の記事を読む →</a>{orig}</p>'
    )
    parts.append("    </li>")
    return "\n".join(parts)


def render_edition_body(edition, heading_tag="h2"):
    out = [
        '  <section class="edition-head">',
        f'    <{heading_tag}><time datetime="{esc(edition["date"])}">{date_label(edition["date"])}</time></{heading_tag}>',
    ]
    if edition.get("lead"):
        out.append(f'    <p class="edition-lead">{esc(edition["lead"])}</p>')
    out.append("  </section>")
    for region in ("jp", "intl"):
        items = [i for i in edition["items"] if i["region"] == region]
        if not items:
            continue
        label = "国内のニュース" if region == "jp" else "海外のニュース（日本語訳）"
        out.append(f'  <section class="group">\n    <p class="group-label {region}">{label}</p>\n    <ul class="items">')
        out.extend(render_item(i) for i in items)
        out.append("    </ul>\n  </section>")
    return "\n".join(out) + "\n"


def render_archive(editions, limit=None):
    rows = []
    for ed in editions[:limit] if limit else editions:
        first = ed["items"][0]["title"] if ed["items"] else ""
        rows.append(
            f'    <li><a href="/claudenews/{esc(ed["date"])}/">'
            f'<time datetime="{esc(ed["date"])}">{date_label(ed["date"])}</time>'
            f'<b>{esc(first)} ほか</b><span class="count">{len(ed["items"])}件</span></a></li>'
        )
    return "\n".join(rows)


def render_index(editions):
    desc = "Claude（Anthropic）の新しいモデルやサービスを中心に、国内と海外のニュースを毎朝集めて、やさしい日本語で紹介します。海外の記事は日本語に訳しています。"
    out = [HEAD.format(title="きょうの Claude ニュース｜Jiu Labo", description=esc(desc),
                       url="https://jiujitsu.co.jp/claudenews/")]
    if editions:
        latest = editions[0]
        out.append(render_edition_body(latest))
        out.append(f'  <p class="pager"><span></span><a href="/claudenews/{esc(latest["date"])}/">この日のページ →</a></p>\n')
        if len(editions) > 1:
            out.append('  <section class="archive">\n    <h2>これまでのニュース</h2>\n    <ul>\n')
            out.append(render_archive(editions[1:]) + "\n")
            out.append("    </ul>\n  </section>\n")
    else:
        out.append('  <p class="empty">準備中です。毎朝8時ごろに、その日のニュースが届きます。</p>\n')
    out.append(NOTE)
    out.append(FOOT)
    return "".join(out)


def render_day(edition, newer, older):
    first = edition["items"][0]["title"] if edition["items"] else ""
    desc = f"{date_label(edition['date'])}の Claude ニュース。{first} ほか{len(edition['items'])}件。"
    out = [HEAD.format(title=f"{date_label(edition['date'])[:10]} の Claude ニュース｜Jiu Labo",
                       description=esc(desc),
                       url=f"https://jiujitsu.co.jp/claudenews/{esc(edition['date'])}/")]
    out.append(render_edition_body(edition))
    prev_link = f'<a href="/claudenews/{esc(older["date"])}/">← {date_label(older["date"])}</a>' if older else "<span></span>"
    next_link = f'<a href="/claudenews/{esc(newer["date"])}/">{date_label(newer["date"])} →</a>' if newer else "<span></span>"
    out.append(f'  <p class="pager">{prev_link}{next_link}</p>\n')
    out.append(NOTE)
    out.append(FOOT)
    return "".join(out)


def render_all(root):
    editions = load_editions(root)
    base = root / "claudenews"
    base.mkdir(parents=True, exist_ok=True)
    (base / "index.html").write_text(render_index(editions), encoding="utf-8")
    for i, ed in enumerate(editions):
        newer = editions[i - 1] if i > 0 else None
        older = editions[i + 1] if i + 1 < len(editions) else None
        day = base / ed["date"]
        day.mkdir(parents=True, exist_ok=True)
        (day / "index.html").write_text(render_day(ed, newer, older), encoding="utf-8")
    return editions


# --------------------------------------------------------------------------- #
# 実行
# --------------------------------------------------------------------------- #
def fixture_fetcher(fixture_dir):
    files = sorted(pathlib.Path(fixture_dir).glob("*.xml"))

    def fetch(url):
        # config の順番どおりにフィクスチャを返す。足りなければ取得失敗扱い。
        if not files:
            raise RuntimeError(f"フィクスチャ切れ ({url})")
        return files.pop(0).read_bytes()
    return fetch


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=str(REPO), help="書き出し先（リポジトリのルート）")
    ap.add_argument("--config", default=str(HERE / "config.json"))
    ap.add_argument("--date", help="号の日付 YYYY-MM-DD（既定は今日のJST）")
    ap.add_argument("--render-only", action="store_true", help="取得・要約はせず、ページだけ作り直す")
    ap.add_argument("--collect-only", metavar="DIR",
                    help="取得だけして DIR に candidates.json と prompt.md を書く（要約は別の誰かが書く）")
    ap.add_argument("--apply", metavar="DIR",
                    help="DIR の candidates.json と result.json から号を作ってページを生成する")
    ap.add_argument("--force", action="store_true", help="今日の号があっても作り直す")
    ap.add_argument("--fixture-dir", help="RSS の代わりにこのフォルダの *.xml を使う")
    ap.add_argument("--fake-llm", action="store_true", help="Claude を呼ばずに見本の文章で埋める")
    args = ap.parse_args(argv)

    root = pathlib.Path(args.root)
    config = json.loads(pathlib.Path(args.config).read_text(encoding="utf-8"))
    now = datetime.now(timezone.utc)
    today = args.date or now.astimezone(JST).date().isoformat()

    if args.collect_only:
        return collect_to_dir(root, config, now, today, args, pathlib.Path(args.collect_only))
    if args.apply:
        apply_from_dir(root, config, now, today, pathlib.Path(args.apply))
    elif not args.render_only:
        run_daily(root, config, now, today, args)

    editions = render_all(root)
    print(f"ページを生成しました: {len(editions)}号 → {root / 'claudenews'}")
    return 0


def gather(root, config, now, today, args):
    """今日の候補を集める。号を作る必要がなければ None。"""
    if (editions_dir(root) / f"{today}.json").exists() and not args.force:
        print(f"{today} の号はもうあります（作り直すなら --force）")
        return None
    fetcher = fixture_fetcher(args.fixture_dir) if args.fixture_dir else fetch_url
    if args.fixture_dir:
        config = {**config, "lookback_hours": 24 * 365 * 50}  # フィクスチャの日付は古いので期間で落とさない
    candidates, errors = collect(config, now, load_seen(root), fetcher)
    for e in errors:
        print(f"  ! {e}", file=sys.stderr)
    print(f"候補 {len(candidates)} 件（取得失敗 {len(errors)} / {len(config['feeds'])} フィード）")
    if len(errors) == len(config["feeds"]):
        raise SystemExit("すべてのフィードの取得に失敗しました")
    if not candidates:
        print("新しい候補がないため、今日の号は作りません")
        return None
    return candidates


def publish(root, config, now, today, candidates, result):
    """Claude の返答から号を作って保存し、候補を既出として記録する。"""
    edition = to_edition(result, candidates, today, config, now)
    seen = load_seen(root)
    for c in candidates:
        seen.setdefault(c["id"], today)
    save_seen(root, seen, today, config.get("seen_keep_days", 21))
    if not edition["items"]:
        print("Claude に関係する記事がなかったため、今日の号は作りません")
        return
    path = write_edition(root, edition)
    print(f"{len(edition['items'])} 件を掲載: {path}")


def run_daily(root, config, now, today, args):
    """取得から要約まで一気に。要約は API（ANTHROPIC_API_KEY）で Claude を呼ぶ。"""
    if not args.fake_llm and not os.environ.get("ANTHROPIC_API_KEY"):
        print("ANTHROPIC_API_KEY が未設定のため、ニュースの取得・要約はスキップします。", file=sys.stderr)
        return
    candidates = gather(root, config, now, today, args)
    if candidates is None:
        return
    system, user = build_prompt(candidates, config)
    caller = fake_claude if args.fake_llm else call_claude
    publish(root, config, now, today, candidates, caller(system, user, config))


PROMPT_TAIL = """
## 返し方

上の決まりに従って、次の形の JSON を `result.json` として、このファイルと同じフォルダに保存してください。
JSON 以外は書かないでください。`id` は候補の `id` をそのまま写してください。

```json
{schema}
```

## 候補

{user}
"""


def collect_to_dir(root, config, now, today, args, out):
    """ルーティン（Claude Code の定期実行）用の前半。要約は実行中の Claude が prompt.md を読んで書く。"""
    candidates = gather(root, config, now, today, args)
    if candidates is None:
        return 0
    out.mkdir(parents=True, exist_ok=True)
    body = {"date": today, "candidates": candidates}
    (out / "candidates.json").write_text(json.dumps(body, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    system, user = build_prompt(candidates, config)
    schema = json.dumps(OUTPUT_SCHEMA, ensure_ascii=False, indent=1)
    (out / "prompt.md").write_text(system + PROMPT_TAIL.format(schema=schema, user=user), encoding="utf-8")
    print(f"候補を書き出しました: {out / 'prompt.md'} を読んで {out / 'result.json'} を書いてください")
    return 0


def apply_from_dir(root, config, now, today, src):
    """ルーティン用の後半。collect_to_dir が書いた候補と、Claude が書いた result.json から号を作る。"""
    body = json.loads((src / "candidates.json").read_text(encoding="utf-8"))
    result = json.loads((src / "result.json").read_text(encoding="utf-8"))
    publish(root, config, now, body.get("date") or today, body["candidates"], result)


if __name__ == "__main__":
    sys.exit(main())
