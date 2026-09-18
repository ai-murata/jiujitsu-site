#!/usr/bin/env python3
"""新着まわりのテスト。ネットワークは使わない。

  python3 tools/news/test_build.py
"""
import json
import sys
import tempfile
import xml.etree.ElementTree as ET
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402
import notify_line  # noqa: E402

ok = fail = 0


def check(name, cond):
    global ok, fail
    if cond:
        ok += 1
    else:
        fail += 1
        print(f"  NG: {name}")


def bad(name, payload, fragment):
    path = Path(tempfile.mkdtemp()) / "news.json"
    path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    try:
        build.load(path)
    except ValueError as err:
        check(name, fragment in str(err))
        return
    except Exception:
        pass
    check(name, False)


def entry(**over):
    e = {"id": "a", "date": "2026-09-17", "title": "見出し",
         "url": "/a/", "summary": "説明"}
    e.update(over)
    return e


print("news.json の検査")
bad("項目の抜けを弾く", {"entries": [entry(summary="")]}, "summary")
bad("idの重複を弾く", {"entries": [entry(), entry()]}, "重複")
bad("相対URLを弾く", {"entries": [entry(url="a/")]}, "/ から始めて")

print("並び順")
_, es = build.load()
check("新しい順に並ぶ", [e["date"] for e in es] == sorted((e["date"] for e in es), reverse=True))
check("お知らせが1件以上ある", len(es) > 0)

print("feed.xml")
feed = build.build_feed(es)
root = ET.fromstring(feed)
ns = "{http://www.w3.org/2005/Atom}"
check("Atomとして読める", root.tag == ns + "feed")
check("件数が一致する", len(root.findall(ns + "entry")) == len(es))
check("リンクが絶対URL", all(
    x.find(ns + "link").get("href").startswith("https://jiujitsu.co.jp/")
    for x in root.findall(ns + "entry")))
check("idが重複しない", len({x.find(ns + "id").text for x in root.findall(ns + "entry")}) == len(es))

print("トップページへの差し込み")
block = build.build_block(es, "")
check("LINEのURLが空ならボタンを出さない", "linebtn" not in block)
check("URLがあればボタンを出す", "linebtn" in build.build_block(es, "https://lin.ee/x"))
check("トップの件数を守る", block.count("<li>") == min(build.TOP_N, len(es)))
src = "A\n" + build.START + "ふるい\n" + build.END + "\nB"
once = build.inject(src, block)
check("目印の間だけ入れ替える", once.startswith("A\n") and once.endswith("\nB"))
check("何度やっても同じ", build.inject(once, block) == once)
try:
    build.inject("目印なし", block)
    check("目印が無ければ止まる", False)
except ValueError:
    check("目印が無ければ止まる", True)

print("実ファイル")
index = (build.ROOT / "index.html").read_text(encoding="utf-8")
check("index.htmlに目印がある", build.START in index and build.END in index)
check("index.htmlが最新", build.inject(index, block) == index)
check("feed.xmlが最新", (build.ROOT / "feed.xml").exists())

print("LINEの文面")
one = notify_line.compose([es[0]])
check("1件なら説明文が入る", es[0]["summary"] in one)
check("1件でもURLが入る", "https://jiujitsu.co.jp" + es[0]["url"] in one)
many = notify_line.compose(es[:3])
check("複数件は全部のURLが並ぶ", all("https://jiujitsu.co.jp" + e["url"] in many for e in es[:3]))
check("LINEの文字数上限に収まる", len(notify_line.compose(es)) < 5000)

print("配信済みの記録")
state = notify_line.read_sent()
ids = {e["id"] for e in es}
check("記録は既存のidだけ", set(state["sent"]) <= ids)
check("いまは未配信ゼロ", [e for e in es if e["id"] not in set(state["sent"])] == [])

print(f"\n{ok} 件OK / {fail} 件NG")
sys.exit(1 if fail else 0)
