"""結果ページの「トーナメント表[Online]」（Google スプレッドシート公開版）の形式を調べる。
人名らしきセルは中身を出さず、長さと文字種だけを出す。"""
import re, urllib.request, html as H
UA = {"User-Agent": "Mozilla/5.0 (jiujitsu.co.jp data research)"}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40) as r: return r.read().decode("utf-8","replace")
KW = re.compile(r"(?i)white|blue|purple|brown|black|gray|grey|yellow|orange|green|master|adult|juvenile|kids?|infant|junior|teen|feather|light|heavy|rooster|middle|open|male|female|帯|級|男子|女子|マスター|アダルト|ジュブナイル|キッズ|total|名|\d+kg|第?\d+試合|mat|マット")
u = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQXfC7YX3Q1HBfQJxAu0JWtn7pJ8Yck2AlzuztbiK1TUU3C_6fwcbc7yc7FH8l_BCgoS1SVDKKgyJRd/pubhtml"
t = get(u)
tabs = re.findall(r'<li[^>]*id="sheet-button-(\d+)"[^>]*>.*?<a[^>]*>(.*?)</a>', t, re.S)
print("len", len(t), "tabs", len(tabs), [H.unescape(x) for _, x in tabs][:40])
grids = re.findall(r'<div[^>]+id="(\d+)"[^>]*>(.*?)</table>', t, re.S)
print("grids", len(grids))
for gid, g in grids[:2]:
    rows = re.findall(r"<tr[^>]*>(.*?)</tr>", g, re.S)
    print(f"\n## grid {gid} rows {len(rows)}")
    shown = 0
    for r in rows:
        cells = [H.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<td[^>]*>(.*?)</td>", r, re.S)]
        cells = [c for c in cells if c]
        if not cells: continue
        print([c if KW.search(c) or len(c) <= 2 else f"<{len(c)}:{'JP' if re.search(r'[ぁ-んァ-ン一-龥]', c) else 'EN'}>" for c in cells][:10])
        shown += 1
        if shown > 45: break
