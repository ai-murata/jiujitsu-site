"""JBJJF の公開エントリーリスト（2023〜2026年）を集めて集計する。

1. Wayback Machine の CDX で jbjjf.com/entrylist/ の URL を列挙
2. 各 entry_list2.htm（階級別の一覧）を jbjjf.com から直接取得
3. 帯・年代・男女・年別の人数などを集計し、集計値だけを JSON で出力する

氏名はプログラムの中で名寄せ（同一人物の判定）に使うだけで、出力には一切含めない。
道場名は公開されている団体名なので、道場ごとの件数は出力する。
"""
import collections, hashlib, html as H, json, re, sys, time, unicodedata, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (jiujitsu.co.jp data research)"}
BELTS = ["White", "Blue", "Purple", "Brown", "Black"]
KIDBELTS = ["Grey", "Gray", "Yellow", "Orange", "Green"]

def get(u, t=60, tries=4):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t) as r:
                return r.read()
        except Exception as e:
            err = e; time.sleep(min(60, 10 * (i + 1)))
    raise err

def dec(b):
    for enc in ("cp932", "utf-8", "euc_jp"):
        try: return b.decode(enc)
        except UnicodeDecodeError: pass
    return b.decode("cp932", "replace")

def text(x): return H.unescape(re.sub(r"<[^>]+>", " ", x)).replace("\xa0", " ").strip()

cdx = json.loads(get("https://web.archive.org/cdx/search/cdx?url=jbjjf.com/entrylist/*&output=json&fl=original&collapse=urlkey&limit=20000", 180, 8))[1:]
urls = sorted({re.sub(r"^https?://(www\.)?", "https://www.", r[0]).split("?")[0] for r in cdx})
lists = [u for u in urls if re.search(r"/entrylist/20(2[3-6])/[^/]+/entry_list2\.htm$", u)]
print("entry lists 2023-2026:", len(lists), file=sys.stderr)

def tour_code(u):  # 日別リスト（xx_1008 など）をまとめた大会コード
    c = u.split("/entrylist/")[1].split("/")[1]
    return re.sub(r"_\d{2,4}$", "", c)

rows, failed = [], []
for u in lists:
    time.sleep(0.3)
    try: t = dec(get(u))
    except Exception as e: failed.append(u); continue
    div = None
    for tr in re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S | re.I):
        cells = [text(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", tr, re.S | re.I)]
        if len(cells) == 1 and re.search(r"Total:\s*\d+", cells[0]):
            div = cells[0]; continue
        if len(cells) >= 2 and div and cells[0]:
            m = re.search(r"[)）]\s+(.*?)\s*\(Total", div)
            nm = re.sub(r"\s+", "", unicodedata.normalize("NFKC", cells[0])).lower()
            rows.append({"y": int(u.split("/entrylist/")[1][:4]), "code": tour_code(u), "ja": div.split("（")[0].strip(),
                         "en": (m.group(1) if m else ""), "who": hashlib.sha256(nm.encode()).hexdigest()[:16],
                         "ac": unicodedata.normalize("NFKC", cells[1]).strip()})
print("rows", len(rows), "failed", len(failed), file=sys.stderr)

def belt(r):
    for b in BELTS + KIDBELTS:
        if re.search(rf"\b{b}\b", r["en"], re.I): return "Gray" if b == "Grey" else b
    for ja, b in [("白帯", "White"), ("青帯", "Blue"), ("紫帯", "Purple"), ("茶帯", "Brown"), ("黒帯", "Black")]:
        if ja in r["ja"]: return b
    return "?"
def group(r):
    e = r["en"].lower()
    if e.startswith("master") or "マスター" in r["ja"]: return "master"
    if e.startswith("adult") or "アダルト" in r["ja"]: return "adult"
    if e.startswith("juvenile") or "ジュブナイル" in r["ja"]: return "juvenile"
    return "kids"
def female(r): return "女子" in r["ja"] or "female" in r["en"].lower() or "women" in r["en"].lower()
def openclass(r): return "open class" in r["en"].lower() or "無差別" in r["ja"] or "オープンクラス" in r["ja"]

W = [r for r in rows if not openclass(r)]
out = {"lists": len(lists), "failed": len(failed), "rows_all": len(rows), "rows_no_openclass": len(W),
       "div_prefix_sample": collections.Counter(" ".join(r["en"].split()[:2]) for r in W).most_common(40),
       "female_detected": sum(female(r) for r in W), "years": {}}
for y in sorted({r["y"] for r in W}):
    g = [r for r in W if r["y"] == y]
    ad = [r for r in g if group(r) != "kids"]
    bc = collections.Counter(belt(r) for r in ad)
    out["years"][y] = {
        "tournaments": len({r["code"] for r in g}), "entries": len(g), "unique_people": len({r["who"] for r in g}),
        "kids_entries": len(g) - len(ad), "adult_entries": len(ad),
        "adult_belts": dict(bc), "adult_groups": dict(collections.Counter(group(r) for r in ad)),
        "female_adult": sum(female(r) for r in ad), "female_kids": sum(female(r) for r in g if group(r) == "kids"),
        "academies": len({r["ac"].lower() for r in g}),
    }
P = collections.defaultdict(set)
for r in W: P[r["who"]].add(r["code"])
out["people_total"] = len(P)
out["people_2plus_tournaments"] = sum(len(v) >= 2 for v in P.values())
yrs = collections.defaultdict(set)
for r in W: yrs[r["who"]].add(r["y"])
out["return_next_year"] = {y: round(sum((y + 1) in v for v in yrs.values() if y in v) / max(1, sum(y in v for v in yrs.values())) * 100, 1) for y in (2023, 2024, 2025)}
out["academies_all"] = collections.Counter(r["ac"] for r in W).most_common()
out["tournaments"] = collections.Counter(f'{r["y"]} {r["code"]}' for r in W).most_common()
print("=====JSON=====")
print(json.dumps(out, ensure_ascii=False))
print("=====END=====")
