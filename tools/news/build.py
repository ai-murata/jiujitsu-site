#!/usr/bin/env python3
"""data/news.json から feed.xml を作り、トップページの新着欄を差し替える。

  python3 tools/news/build.py

ネットワークは使わない。書き換えるのは feed.xml と index.html の
<!-- news:start --> 〜 <!-- news:end --> の間だけ。
"""
import html
import json
import re
import sys
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SITE = "https://jiujitsu.co.jp"
JST = timezone(timedelta(hours=9))
TOP_N = 4  # トップページに出す件数

START = "<!-- news:start -->"
END = "<!-- news:end -->"


def load(path=None):
    path = path or ROOT / "data" / "news.json"
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    entries = data.get("entries", [])
    seen = set()
    for e in entries:
        for key in ("id", "date", "title", "url", "summary"):
            if not e.get(key):
                raise ValueError(f"news.json: {e.get('id', '?')} に {key} がありません")
        if e["id"] in seen:
            raise ValueError(f"news.json: id が重複しています: {e['id']}")
        seen.add(e["id"])
        datetime.strptime(e["date"], "%Y-%m-%d")
        if not e["url"].startswith("/"):
            raise ValueError(f"news.json: url は / から始めてください: {e['url']}")
    entries.sort(key=lambda e: e["date"], reverse=True)
    return data, entries


def build_feed(entries):
    now = datetime.now(JST).replace(microsecond=0).isoformat()
    parts = [
        '<?xml version="1.0" encoding="utf-8"?>',
        '<feed xmlns="http://www.w3.org/2005/Atom">',
        "  <title>jiujitsu.co.jp</title>",
        "  <subtitle>柔術の現場で、必要にせまられて作ったものたち。</subtitle>",
        f'  <link href="{SITE}/"/>',
        f'  <link rel="self" type="application/atom+xml" href="{SITE}/feed.xml"/>',
        f"  <id>{SITE}/</id>",
        f"  <updated>{now}</updated>",
        "  <author><name>BUTTI ON LINE</name></author>",
    ]
    for e in entries:
        url = SITE + e["url"]
        stamp = f"{e['date']}T09:00:00+09:00"
        parts += [
            "  <entry>",
            f"    <title>{html.escape(e['title'])}</title>",
            f'    <link href="{url}"/>',
            f"    <id>tag:jiujitsu.co.jp,{e['date']}:{e['id']}</id>",
            f"    <updated>{stamp}</updated>",
            f"    <summary>{html.escape(e['summary'])}</summary>",
            "  </entry>",
        ]
    parts.append("</feed>")
    return "\n".join(parts) + "\n"


def build_block(entries, line_url=""):
    rows = []
    for e in entries[:TOP_N]:
        y, m, d = e["date"].split("-")
        rows.append(
            f'        <li><a href="{e["url"]}">'
            f"<time>{y}.{m}.{d}</time>"
            f'<b>{html.escape(e["title"])}</b>'
            f'<span class="arrow">→</span></a></li>'
        )
    follow = ""
    if line_url:
        follow = (
            f'        <a class="linebtn" href="{html.escape(line_url)}" '
            f'target="_blank" rel="noopener">LINEで更新を受け取る</a>\n'
        )
    return (
        f"{START}\n"
        '  <div class="wrap">\n'
        '    <section class="news rise d2">\n'
        '      <p class="sec-label">新着</p>\n'
        '      <ul class="newslist">\n'
        + "\n".join(rows)
        + "\n      </ul>\n"
        '      <p class="newsfoot">\n'
        + follow
        + '        <a class="feedlink" href="/feed.xml">RSSで受け取る</a>\n'
        "      </p>\n"
        "    </section>\n"
        "  </div>\n"
        f"{END}"
    )


def inject(index_html, block):
    if START not in index_html or END not in index_html:
        raise ValueError(f"index.html に {START} / {END} の目印がありません")
    return re.sub(
        re.escape(START) + r".*?" + re.escape(END), lambda _: block, index_html, flags=re.S
    )


def main():
    data, entries = load()
    feed_path = ROOT / "feed.xml"
    index_path = ROOT / "index.html"

    feed = build_feed(entries)
    index = inject(index_path.read_text(encoding="utf-8"),
                   build_block(entries, data.get("line_url", "")))

    changed = []
    for path, text in ((feed_path, feed), (index_path, index)):
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")
            changed.append(path.name)

    print(f"お知らせ {len(entries)} 件 / 更新: {', '.join(changed) if changed else 'なし'}")


if __name__ == "__main__":
    sys.exit(main())
