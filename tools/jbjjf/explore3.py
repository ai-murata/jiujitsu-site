"""結果ページの「トーナメント表[Online]」（Google スプレッドシート公開版）の形式を調べる。
人名らしきセルは中身を出さず、長さと文字種だけを出す。"""
import re, urllib.request, html as H
UA = {"User-Agent": "Mozilla/5.0 (jiujitsu.co.jp data research)"}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40) as r: return r.read().decode("utf-8","replace")
KW = re.compile(r"(?i)white|blue|purple|brown|black|gray|grey|yellow|orange|green|master|adult|juvenile|kids?|infant|junior|teen|feather|light|heavy|rooster|middle|open|male|female|帯|級|男子|女子|マスター|アダルト|ジュブナイル|キッズ|total|名|\d+kg|第?\d+試合|mat|マット")
u = "https://docs.google.com/spreadsheets/d/e/2PACX-1vQXfC7YX3Q1HBfQJxAu0JWtn7pJ8Yck2AlzuztbiK1TUU3C_6fwcbc7yc7FH8l_BCgoS1SVDKKgyJRd/pubhtml"
t = get(u)
print("len", len(t), "tables", t.count("<table"), "sheet names", [H.unescape(x) for x in re.findall(r'id="sheet-button-[^"]*"[^>]*>(?:<a[^>]*>)?([^<]*)', t)][:30])
print("head", re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", t.split("<table")[0]))[-300:])
rows = re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S)
print("rows", len(rows))
shown = 0
for r in rows:
    cells = [H.unescape(re.sub(r"<[^>]+>", "", c)).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S)]
    cells = [c for c in cells if c]
    if not cells: continue
    print([c if KW.search(c) or len(c) <= 2 else f"<{len(c)}:{'JP' if re.search(r'[ぁ-んァ-ン一-龥]', c) else 'EN'}>" for c in cells][:10])
    shown += 1
    if shown > 60: break
