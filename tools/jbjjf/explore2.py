"""JBJJF の大会一覧とエントリーリストの形式を調べる（個人名は出力しない）。"""
import re, urllib.request, urllib.parse, html as H
UA = {"User-Agent": "Mozilla/5.0 (jiujitsu.co.jp data research)"}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30) as r:
        return r.geturl(), r.status, r.read()
def links(u):
    try: f, s, b = get(u)
    except Exception as e: print("ERR", u, e); return []
    t = b.decode("utf-8", "replace")
    out = [(urllib.parse.urljoin(f, h), re.sub(r"<[^>]+>|\s+", " ", x).strip()[:70]) for h, x in re.findall(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', t, re.S)]
    print(f"\n### {u} -> {f} {s} {len(b)}B links={len(out)}")
    return out
for u in ["https://www.jbjjf.com/result/", "https://www.jbjjf.com/entrylist/", "https://www.jbjjf.com/entrylist/2025/", "https://www.jbjjf.com/upcoming-events/calendar2016/"]:
    for l, x in links(u):
        if re.search(r"result|entrylist|202[3-6]|ibjjfdb|sakura", l): print("  ", x, "->", l)
# エントリーリストの形式（名前は伏せる）
u = "https://www.jbjjf.com/entrylist/2026/es_ch13_1226/entry_list2.htm"
f, s, b = get(u)
for enc in ("utf-8", "shift_jis", "cp932", "euc_jp"):
    try: t = b.decode(enc); print("\nencoding", enc); break
    except Exception: pass
print("len", len(t), "tables", t.count("<table"), "rows", t.lower().count("<tr"))
rows = re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S | re.I)
for r in rows[:12]:
    cells = [H.unescape(re.sub(r"<[^>]+>|\s+", " ", c)).strip() for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", r, re.S | re.I)]
    # 3列目以降の人名らしき列はマスク：文字数と文字種だけ出す
    print(len(cells), [c if (i == 0 or len(c) < 3 or re.search(r"(?i)white|blue|purple|brown|black|master|adult|juvenile|kg|feather|light|heavy|rooster|middle|帯|級|男|女|division|name|team|academy", c)) else f"<{len(c)}:{'JP' if re.search(r'[ぁ-んァ-ン一-龥]', c) else 'EN'}>" for i, c in enumerate(cells)])
print("\nnon-table text sample:", re.sub(r"<[^>]+>|\s+", " ", t)[:300] if not rows else "")
