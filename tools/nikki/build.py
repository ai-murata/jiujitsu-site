#!/usr/bin/env python3
"""クラウド日記（/blog/nikki/）：その日に Claude Code とやったことを、アイさん目線の短い日記にする。

毎晩のルーティン（ROUTINE.md）が2段階で使う。

    python3 tools/nikki/build.py --collect data/nikki/inbox [--date YYYY-MM-DD]
        その日（JST）の main のコミットを集め、candidates.json と prompt.md を置く
    （ルーティンの Claude が prompt.md を読んで result.json を書く）
    python3 tools/nikki/build.py --apply data/nikki/inbox
        result.json を確かめて data/nikki/entries/YYYY-MM-DD.json に保存し、ページを作り直す
    python3 tools/nikki/build.py --render-only
        保存済みの日記からページだけ作り直す（デザインを変えたとき）

非公開のページ（config.json の private_paths / private_words）に関わるコミットは材料に入れず、
日記の文章にそれらの言葉が入っていたら保存しない。自動更新（Actions やルーティンの chore コミット）は
中身を書かず件数だけ数える。
"""

import argparse
import html
import json
import pathlib
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone

JST = timezone(timedelta(hours=9))
HERE = pathlib.Path(__file__).resolve().parent
REPO = HERE.parent.parent
WEEKDAYS = "月火水木金土日"
SEP = "\x1e"  # コミットの区切り
FSEP = "\x1f"  # 項目の区切り


def load_config():
    return json.loads((HERE / "config.json").read_text(encoding="utf-8"))


# --------------------------------------------------------------------------- #
# 集める
# --------------------------------------------------------------------------- #
def git_log(repo, branch):
    fmt = SEP + FSEP.join(["%H", "%an", "%cI", "%s", "%b"]) + FSEP
    out = subprocess.run(
        ["git", "-C", str(repo), "log", branch, "--no-merges", "--name-only", f"--format={fmt}", "-n", "400"],
        check=True, capture_output=True, text=True,
    ).stdout
    commits = []
    for chunk in out.split(SEP)[1:]:
        parts = chunk.split(FSEP)
        sha, author, cdate, subject, body, files = parts[0], parts[1], parts[2], parts[3], parts[4], parts[5]
        commits.append({
            "sha": sha,
            "author": author,
            "date": datetime.fromisoformat(cdate).astimezone(JST),
            "subject": subject.strip(),
            "body": body.strip(),
            "files": [f for f in files.strip().splitlines() if f.strip()],
        })
    return commits


def is_private_path(path, config):
    return any(path.startswith(p) for p in config["private_paths"])


def has_private_word(text, config):
    low = (text or "").lower()
    return any(w.lower() in low for w in config["private_words"])


def is_auto(c, config):
    return c["author"] in config["auto_authors"] or c["subject"].startswith(tuple(config["auto_subject_prefixes"]))


def clean_body(body):
    # Co-Authored-By などの署名行は材料にしない
    lines = [ln for ln in body.splitlines()
             if ln.strip() and not re.match(r"^(Co-Authored-By|Claude-Session|Signed-off-by):", ln.strip(), re.I)]
    return "\n".join(lines)[:400]


def select(commits, date, config):
    """その日のコミットを、日記の材料・自動更新・外したもの に分ける。"""
    work, auto, skipped = [], [], 0
    for c in commits:
        if c["date"].strftime("%Y-%m-%d") != date:
            continue
        if is_auto(c, config):
            auto.append(c["subject"])
            continue
        body = clean_body(c["body"])
        public_files = [f for f in c["files"] if not is_private_path(f, config)]
        if has_private_word(c["subject"] + "\n" + body, config) or (c["files"] and not public_files):
            skipped += 1
            continue
        work.append({
            "sha": c["sha"],
            "time": c["date"].strftime("%H:%M"),
            "subject": c["subject"],
            "body": body,
            "files": public_files[:12],
        })
    work.sort(key=lambda w: w["time"])
    return work, auto, skipped


def auto_summary(subjects):
    """自動更新の件数を、種類ごとにまとめる（例：柔術ニュース 2件、補助金一覧 1件）。"""
    names = {"jiunews": "柔術ニュース", "hojokin": "補助金一覧", "news": "お知らせ", "nikki": "クラウド日記"}
    counts = {}
    for s in subjects:
        m = re.match(r"chore\(([^)]+)\)", s)
        key = names.get(m.group(1), m.group(1)) if m else "そのほか"
        counts[key] = counts.get(key, 0) + 1
    return [{"name": k, "count": v} for k, v in counts.items()]


PROMPT = """# クラウド日記の下書きを書く（{date_label}）

あなたは、株式会社BUTTI ON LINE のマネージャー **村田亜衣（アイ）** になりきって、
その日に Claude Code（クラウド）とやったことから、**読んだ人が「自分もやってみよう」と思える**短い日記を書きます。
材料は、下の「今日の作業」（このサイトのリポジトリに今日入った変更の記録）だけです。

## 読む人
道場やサロン、小さなお店を切り盛りしている人、事務仕事を楽にしたい人。エンジニアではない。
AIの一般的な使い方の記事はもう読み飽きている。**「え、そんなこともできるの？」「それは知らなかった」**が読みたい。

## 何を書くか（いちばん大事）
- 今日の作業から、**読む人にとって目新しいこと**を 1〜{max_items} つだけ選ぶ。選ぶ順番：
  1. Claude Code に「こんなことまで任せられた」という実例（自動で毎日動く仕組み、道具づくり、デザイン など）
  2. 実際につまずいたことと、どう解決したか（fix のコミットは宝物。何が起きて、何が原因で、どう直したか）
  3. やってみて初めて分かった具体的な発見（例：小さいアイコンでは2段の文字は読めない → タブとホーム画面で分けた）
- **誰でも言える一般論は書かない。** 「あとから足せばいい」「まとめて頼むといい」「完璧を目指さない」のような、
  AIの記事によくあるコツは禁止。その日の作業でしか言えない、具体的なことだけを書く。
- 作業の中身は、材料の一覧だけでなく `git show <番号>` で実際の変更を見て、具体的に書いてよい
  （仕組みの動き方、何回作り直したか、どんな順番で進めたか、など）。ただし推測で数字や結果を足さない。
- 見た目の小さな調整、文言の直し、ほかの人に関係のない作業は捨てる。
- 目新しいことが1つもない日は、items を1つにして短く書く。

## 書き方
- 1つの話ごとに次を書く：
  1. heading：読む人が「え？」と思う見出し（「〇〇を毎朝Claudeが勝手にやってくれる」「アイコンを5回作り直して分かったこと」など）
  2. text：何をしたか、どう動くのか、何が起きたかを具体的に（2〜5文）。仕組みはたとえ話でかみくだく
  3. ask：真似するときの頼み方の例（読む人が自分の仕事に置きかえて使える一言。「」は付けない）。
     アイさんが実際にそう言ったとは書かない
  4. tip：この作業でしか分からなかった発見・つまずき・注意点（1〜2文）。一般論は禁止
  5. link：このサイトの公開ページで実物が見られるなら、そのパス（例："/jiunews/"）。無ければ ""
- アイさんの一人称（「私」）。やさしい、です・ます調。ブログ（/blog/）の口調に合わせる。
  専門用語は使うなら（　）でひとこと説明する。
- **材料と変更の中身から言えないことは足さない。** 人の名前、数字、お客さまの話、かかった時間を作らない。
- title は、いちばん目新しい話がひと目で分かるように。
- ファイル名・コミットの番号・外部のURLは書かない（link だけはサイト内のパス）。
- 次の言葉や、それを指す内容は **絶対に書かない**（非公開のページのため）：{private_words}

## 出力
`{inbox}/result.json` に、次の形の JSON を UTF-8 で書く（ほかのキーは足さない）。

```json
{{
  "date": "{date}",
  "title": "日記のタイトル（25字くらいまで）",
  "lead": "書き出し（1〜2文。今日いちばんの「え？」を先に言う）",
  "items": [
    {{"heading": "見出し（25字くらいまで）", "text": "何をしたか・どう動くか・何が起きたか",
      "ask": "真似するときの頼み方の例", "tip": "この作業でしか分からなかった発見", "link": "/jiunews/ または \"\""}}
  ],
  "closing": "ひとこと（1〜2文。読んだ人へのひと押し）"
}}
```

## 今日の作業（{n} 件）

{work}
## 自動で動いたもの（参考。日記の本文には書かなくてよい。ページの最後にプログラムが件数を載せる）

{auto}
"""


def build_prompt(date, work, auto, config, inbox):
    lines = []
    for w in work:
        lines.append(f"- {w['time']}　{w['subject']}　（番号 {w['sha'][:7]}）")
        if w["body"]:
            lines.extend("    " + ln for ln in w["body"].splitlines())
        if w["files"]:
            lines.append("    （変更した場所：" + "、".join(w["files"]) + "）")
    auto_lines = [f"- {a['name']} {a['count']}件" for a in auto] or ["- なし"]
    return PROMPT.format(
        date=date, date_label=date_label(date), n=len(work), max_items=config["max_items"],
        private_words="、".join(config["private_words"]), inbox=inbox,
        work="\n".join(lines) + "\n", auto="\n".join(auto_lines) + "\n",
    )


def collect(repo, root, out, date, config):
    """材料を out に置く。日記にする作業が無ければ False。"""
    if (entries_dir(root) / f"{date}.json").exists():
        print(f"{date} の日記はもうあります")
        return False
    work, auto_subjects, skipped = select(git_log(repo, config["branch"]), date, config)
    auto = auto_summary(auto_subjects)
    print(f"{date}: 日記の材料 {len(work)} 件 / 自動更新 {len(auto_subjects)} 件 / 非公開のため外した {skipped} 件")
    if not work:
        return False
    out.mkdir(parents=True, exist_ok=True)
    (out / "candidates.json").write_text(json.dumps(
        {"date": date, "work": work, "auto": auto}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    (out / "prompt.md").write_text(build_prompt(date, work, auto, config, out.as_posix()), encoding="utf-8")
    return True


# --------------------------------------------------------------------------- #
# 確かめて保存
# --------------------------------------------------------------------------- #
LIMITS = {"title": 60, "lead": 300, "heading": 50, "text": 500, "ask": 200, "tip": 250, "closing": 300}


def _text(value, key, errors):
    if not isinstance(value, str) or not value.strip():
        errors.append(f"{key} が空です")
        return ""
    value = value.strip()
    if len(value) > LIMITS[key]:
        errors.append(f"{key} が長すぎます（{len(value)}字 > {LIMITS[key]}字）")
    return value


def check_link(link, root, config, errors):
    """サイト内の公開ページへのパスだけを通す（無ければ ""）。"""
    if not link:
        return ""
    if not isinstance(link, str) or not re.fullmatch(r"/[a-z0-9-]+(/[a-z0-9-]+)*/", link):
        errors.append(f"link「{link}」は /jiunews/ のようなサイト内のパスにしてください")
        return ""
    rel = link.strip("/") + "/"
    if is_private_path(rel, config) or has_private_word(link, config):
        errors.append(f"link「{link}」は非公開のページです")
        return ""
    if not (root / rel / "index.html").exists():
        errors.append(f"link「{link}」のページがありません")
        return ""
    return link


def to_entry(result, candidates, config, root=REPO):
    errors = []
    date = candidates["date"]
    if result.get("date") != date:
        errors.append(f"date が {date} ではありません")
    entry = {
        "date": date,
        "title": _text(result.get("title"), "title", errors),
        "lead": _text(result.get("lead"), "lead", errors),
        "items": [],
        "closing": _text(result.get("closing"), "closing", errors),
        "auto": candidates.get("auto", []),
    }
    items = result.get("items")
    if not isinstance(items, list) or not items:
        errors.append("items が空です")
        items = []
    if len(items) > config["max_items"]:
        errors.append(f"items が多すぎます（{len(items)} > {config['max_items']}）")
    for i, it in enumerate(items):
        it = it if isinstance(it, dict) else {}
        item = {k: _text(it.get(k), k, errors) for k in ("heading", "text", "ask", "tip")}
        item["link"] = check_link(it.get("link"), root, config, errors)
        entry["items"].append(item)
    everything = json.dumps({k: entry[k] for k in ("title", "lead", "items", "closing")}, ensure_ascii=False)
    for w in config["private_words"]:
        if w.lower() in everything.lower():
            errors.append(f"非公開の言葉「{w}」が入っています")
    if re.search(r"https?://|\b[0-9a-f]{7,40}\b", everything):
        errors.append("URLやハッシュが入っています")
    if errors:
        raise ValueError("result.json を直してください：\n- " + "\n- ".join(errors))
    return entry


def entries_dir(root):
    return root / "data" / "nikki" / "entries"


def load_entries(root):
    d = entries_dir(root)
    files = sorted(d.glob("*.json"), reverse=True) if d.exists() else []
    return [json.loads(f.read_text(encoding="utf-8")) for f in files]


def apply(root, inbox, config):
    candidates = json.loads((inbox / "candidates.json").read_text(encoding="utf-8"))
    result = json.loads((inbox / "result.json").read_text(encoding="utf-8"))
    entry = to_entry(result, candidates, config, root)
    d = entries_dir(root)
    d.mkdir(parents=True, exist_ok=True)
    (d / f"{entry['date']}.json").write_text(json.dumps(entry, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    render_all(root)
    return entry


# --------------------------------------------------------------------------- #
# ページ
# --------------------------------------------------------------------------- #
def esc(text):
    return html.escape(text or "", quote=True)


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
<meta property="og:type" content="{og_type}">
<link rel="canonical" href="{url}">
<link rel="alternate" type="application/atom+xml" title="Jiu Labo の新着" href="/feed.xml">
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Shippori+Mincho:wght@500;600;700&family=Zen+Kaku+Gothic+New:wght@400;500;700&display=swap">
<style>
  :root {{
    --paper: #ffffff; --panel: #faf8f2; --line: #e7e1d1;
    --gold: #a3801a; --gold-hi: #c9a227;
    --ink: #17140d; --body-c: #4d4737; --faint: #948c74;
    --mincho: "Shippori Mincho", "Hiragino Mincho ProN", serif;
    --gothic: "Zen Kaku Gothic New", "Hiragino Kaku Gothic ProN", sans-serif;
    --w: #eceadf; --b: #274a7a; --p: #4d3070; --br: #5a3c22; --k: #17140d;
  }}
  * {{ box-sizing: border-box; }}
  body {{ background: var(--paper); color: var(--body-c); font-family: var(--gothic); line-height: 1.95; margin: 0; -webkit-font-smoothing: antialiased; }}
  .wrap {{ max-width: 680px; margin: 0 auto; padding: 0 22px 80px; }}
  a {{ color: var(--gold); }}

  header {{ text-align: center; padding: 64px 20px 40px; }}
  .brand {{ font-size: 11px; letter-spacing: .3em; color: var(--gold); font-weight: 500; margin: 0; }}
  .brand a {{ color: inherit; text-decoration: none; }}
  h1 {{ font-family: var(--mincho); font-weight: 700; font-size: clamp(22px, 5vw, 32px); color: var(--ink); letter-spacing: .08em; line-height: 1.6; margin: 14px auto 16px; max-width: 20em; word-break: auto-phrase; text-wrap: balance; }}
  .meta, .lede {{ font-size: 12.5px; color: var(--faint); margin: 0; letter-spacing: .08em; }}

  .rank {{ display: flex; height: 4px; }}
  .rank span {{ flex: 1; }}
  .rank .w {{ background: var(--w); }} .rank .b {{ background: var(--b); }} .rank .p {{ background: var(--p); }}
  .rank .br {{ background: var(--br); }} .rank .k {{ background: var(--k); }}

  article {{ font-size: 15.5px; padding-top: 40px; }}
  article p {{ margin: 0 0 1.4em; }}
  .did {{ list-style: none; margin: 8px 0 32px; padding: 0; counter-reset: did; border-top: 1px solid var(--line); }}
  .did li {{ counter-increment: did; padding: 18px 0 16px 44px; border-bottom: 1px solid var(--line); position: relative; }}
  .did li::before {{ content: counter(did); position: absolute; left: 4px; top: 20px; width: 26px; height: 26px; border-radius: 50%; background: var(--panel); border: 1px solid var(--gold); color: var(--gold); font-size: 12.5px; font-weight: 700; text-align: center; line-height: 24px; }}
  .did h2 {{ font-family: var(--mincho); font-weight: 700; font-size: 17px; color: var(--ink); letter-spacing: .04em; line-height: 1.6; margin: 0 0 4px; word-break: auto-phrase; text-wrap: pretty; }}
  .did p {{ margin: 0; font-size: 14.5px; }}
  .ask {{ margin: 12px 0 0; background: var(--panel); border: 1px solid var(--line); border-radius: 6px; padding: 10px 14px; }}
  .ask span {{ display: block; font-size: 11.5px; font-weight: 700; letter-spacing: .08em; color: var(--gold); }}
  .did .ask p {{ font-size: 14.5px; color: var(--ink); }}
  .did .ask p::before {{ content: "「"; }} .did .ask p::after {{ content: "」"; }}
  .did .tip {{ margin: 10px 0 0; font-size: 13.5px; }}
  .tip b {{ color: var(--gold); margin-right: 8px; font-size: 12px; letter-spacing: .08em; }}
  .did .see {{ margin: 8px 0 0; font-size: 13.5px; font-weight: 700; }}
  .did .see a {{ text-decoration: none; }}
  .closing {{ background: var(--panel); border-left: 3px solid var(--gold); padding: 14px 18px; }}
  .auto {{ font-size: 12.5px; color: var(--faint); }}
  .note {{ font-size: 12px; color: var(--faint); border-top: 1px solid var(--line); padding-top: 16px; margin-top: 40px; }}

  .pager {{ display: flex; justify-content: space-between; gap: 12px; margin: 36px 0 0; font-size: 13.5px; }}
  .pager a {{ text-decoration: none; }}

  .posts {{ list-style: none; margin: 40px 0 0; padding: 0; border-top: 1px solid var(--line); }}
  .posts a {{ display: block; padding: 20px 4px; border-bottom: 1px solid var(--line); text-decoration: none; color: inherit; }}
  .posts a:hover h2 {{ color: var(--gold); }}
  .posts time {{ font-size: 12px; color: var(--faint); letter-spacing: .1em; font-variant-numeric: tabular-nums; }}
  .posts h2 {{ font-family: var(--mincho); font-weight: 700; font-size: 17px; color: var(--ink); letter-spacing: .05em; line-height: 1.6; margin: 2px 0 4px; word-break: auto-phrase; text-wrap: pretty; }}
  .posts p {{ font-size: 13.5px; margin: 0; }}
  .posts li:first-child a {{ background: var(--panel); border-top: 3px solid var(--gold); padding: 24px 20px; }}
  .empty {{ text-align: center; background: var(--panel); border-radius: 8px; padding: 36px 20px; margin: 44px 0 0; font-size: 14px; }}

  footer {{ margin-top: 72px; border-top: 1px solid var(--line); padding: 30px 0 0; text-align: center; font-size: 12px; letter-spacing: .1em; color: var(--faint); line-height: 2; }}
  footer a {{ color: var(--gold); text-decoration: none; }}
  footer a:hover {{ text-decoration: underline; }}

  @media (max-width: 560px) {{
    header {{ padding: 36px 18px 26px; }}
    h1 {{ font-size: 20px; letter-spacing: .02em; line-height: 1.5; margin: 10px auto 10px; }}
    article {{ font-size: 15px; }}
    .did li {{ padding-left: 38px; }}
    .did h2, .posts h2 {{ font-size: 16px; }}
    .posts a {{ padding: 16px 2px; }}
    .posts li:first-child a {{ padding: 20px 14px; }}
  }}
</style>
"""

RANK = '\n<div class="rank" aria-hidden="true"><span class="w"></span><span class="b"></span><span class="p"></span><span class="br"></span><span class="k"></span></div>\n'

NOTE = ('    <p class="note">この日記は、その日にこのサイトへ入った変更の記録をもとに Claude が下書きし、'
        '村田が読んでから載せています。</p>\n')


def render_entry(entry, newer, older):
    date = entry["date"]
    url = f"https://jiujitsu.co.jp/blog/nikki/{date}/"
    out = [HEAD.format(title=esc(f"{entry['title']}｜クラウド日記"), description=esc(entry["lead"]),
                       url=url, og_type="article")]
    out.append(f"""
<header>
  <p class="brand"><a href="/blog/nikki/">クラウド日記</a></p>
  <h1>{esc(entry['title'])}</h1>
  <p class="meta"><time datetime="{esc(date)}">{date_label(date)}</time>　村田亜衣（マネージャー）</p>
</header>
""")
    out.append(RANK)
    out.append('\n<div class="wrap">\n  <article>\n')
    out.append(f"    <p>{esc(entry['lead'])}</p>\n")
    out.append('    <ol class="did">\n')
    for it in entry["items"]:
        out.append(f"      <li><h2>{esc(it['heading'])}</h2><p>{esc(it['text'])}</p>\n"
                   f'        <div class="ask"><span>真似するなら、こう頼む</span><p>{esc(it["ask"])}</p></div>\n'
                   f'        <p class="tip"><b>発見</b>{esc(it["tip"])}</p>\n'
                   + (f'        <p class="see"><a href="{esc(it["link"])}">できたものを見る →</a></p>\n' if it.get("link") else "")
                   + "      </li>\n")
    out.append("    </ol>\n")
    out.append(f'    <p class="closing">{esc(entry["closing"])}</p>\n')
    auto = entry.get("auto") or []
    if auto:
        parts = "、".join(f"{esc(a['name'])} {int(a['count'])}件" for a in auto)
        out.append(f'    <p class="auto">このほか、自動の更新が動きました（{parts}）。</p>\n')
    out.append('\n    <div class="share"></div>\n    <script src="/blog/share.js"></script>\n')
    prev_link = f'<a href="/blog/nikki/{esc(older["date"])}/">← {date_label(older["date"])}</a>' if older else "<span></span>"
    next_link = f'<a href="/blog/nikki/{esc(newer["date"])}/">{date_label(newer["date"])} →</a>' if newer else "<span></span>"
    out.append(f'    <p class="pager">{prev_link}{next_link}</p>\n')
    out.append(NOTE)
    out.append("  </article>\n")
    out.append(FOOT)
    return "".join(out)


FOOT = """
  <footer>
    <a href="/blog/nikki/">クラウド日記の一覧へ</a>　／　<a href="/blog/">ブログへ</a>　／　<a href="/">jiujitsu.co.jp トップへ</a>
    <br>© 2026 BUTTI ON LINE Inc.
  </footer>
</div>
"""


def render_index(entries):
    desc = "マネージャーの村田亜衣が、その日 Claude Code（クラウド）といっしょにやったことを、毎日みじかく書く日記です。"
    out = [HEAD.format(title="クラウド日記｜Jiu Labo", description=esc(desc),
                       url="https://jiujitsu.co.jp/blog/nikki/", og_type="website")]
    out.append("""
<header>
  <p class="brand"><a href="/blog/">JIU LABO BLOG</a></p>
  <h1>クラウド日記</h1>
  <p class="lede">今日、Claude Codeとこんなことをしました。</p>
</header>
""")
    out.append(RANK)
    out.append('\n<div class="wrap">\n')
    if entries:
        out.append('  <ul class="posts">\n')
        for e in entries:
            out.append(f'    <li>\n      <a href="/blog/nikki/{esc(e["date"])}/">\n'
                       f'        <time datetime="{esc(e["date"])}">{date_label(e["date"])}</time>\n'
                       f'        <h2>{esc(e["title"])}</h2>\n'
                       f'        <p>{esc(e["lead"])}</p>\n      </a>\n    </li>\n')
        out.append("  </ul>\n")
    else:
        out.append('  <p class="empty">1日目は準備中です。</p>\n')
    out.append(FOOT)
    return "".join(out)


def render_all(root):
    entries = load_entries(root)
    base = root / "blog" / "nikki"
    base.mkdir(parents=True, exist_ok=True)
    (base / "index.html").write_text(render_index(entries), encoding="utf-8")
    for i, e in enumerate(entries):
        newer = entries[i - 1] if i > 0 else None
        older = entries[i + 1] if i + 1 < len(entries) else None
        day = base / e["date"]
        day.mkdir(parents=True, exist_ok=True)
        (day / "index.html").write_text(render_entry(e, newer, older), encoding="utf-8")
    return entries


# --------------------------------------------------------------------------- #
def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--collect", metavar="DIR", help="その日の材料を DIR に置く")
    g.add_argument("--apply", metavar="DIR", help="DIR/result.json から日記を保存してページを作る")
    g.add_argument("--render-only", action="store_true", help="保存済みの日記からページだけ作り直す")
    ap.add_argument("--date", help="日記の日付（YYYY-MM-DD、JST）。省略すると今日")
    ap.add_argument("--root", default=str(REPO), help="サイトのルート（テスト用）")
    args = ap.parse_args(argv)

    root = pathlib.Path(args.root)
    config = load_config()
    if args.collect:
        date = args.date or datetime.now(JST).strftime("%Y-%m-%d")
        ok = collect(REPO, root, pathlib.Path(args.collect), date, config)
        if not ok:
            print("今日は日記にする作業がありません（何も作りません）")
        return 0
    if args.apply:
        try:
            entry = apply(root, pathlib.Path(args.apply), config)
        except ValueError as e:
            print(e, file=sys.stderr)
            return 1
        print(f"{entry['date']} の日記を作りました：{entry['title']}（{len(entry['items'])}項目）")
        return 0
    entries = render_all(root)
    print(f"{len(entries)} 日ぶんのページを作り直しました")
    return 0


if __name__ == "__main__":
    sys.exit(main())
