"""JBJJF の公開エントリーリスト（2023〜2026年）を集め、集計用のレコードを作る。

出力（out/ 以下、Actions の artifact としてだけ保存し、リポジトリには入れない）:
  tournaments.json : 大会ごとの URL・タイトル・エントリーリスト URL
  records.jsonl    : 1エントリー1行。氏名はハッシュ化し、元の氏名は出力しない
ログには件数などの集計だけを出す。
"""
import hashlib, html as H, json, os, re, sys, time, unicodedata, urllib.parse, urllib.request

UA = {"User-Agent": "Mozilla/5.0 (jiujitsu.co.jp data research; contact info@jiujitsu.co.jp)"}
CAL = ["https://www.jbjjf.com/calendar2016/old2023/", "https://www.jbjjf.com/calendar2016/old2024/",
       "https://www.jbjjf.com/calendar2016/old2025/", "https://www.jbjjf.com/upcoming-events/calendar2016/"]
OUT = sys.argv[1] if len(sys.argv) > 1 else "out"
SALT = os.environ.get("NAME_SALT", "jiulabo")

def get(u, tries=3):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=40) as r:
                return r.geturl(), r.read()
        except Exception as e:
            err = e; time.sleep(2 * (i + 1))
    raise err

def dec(b):
    for enc in ("utf-8", "cp932", "euc_jp"):
        try: return b.decode(enc)
        except UnicodeDecodeError: pass
    return b.decode("utf-8", "replace")

def text(x): return H.unescape(re.sub(r"<[^>]+>", " ", x)).replace("\xa0", " ").strip()

def links(url):
    f, b = get(url); t = dec(b)
    return f, t, [(urllib.parse.urljoin(f, h), text(x)) for h, x in re.findall(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', t, re.S)]

os.makedirs(OUT, exist_ok=True)
posts = {}
for c in CAL:
    try: _, _, ls = links(c)
    except Exception as e: print("ERR calendar", c, e); continue
    n = 0
    for u, x in ls:
        if re.match(r"https://www\.jbjjf\.com/20(2[3-6])/\d\d/\d+/?$", u) and u not in posts:
            posts[u] = x; n += 1
    print(f"calendar {c}: {n} posts")
print("posts total", len(posts))

tours, lists = [], {}
for u, x in posts.items():
    time.sleep(0.4)
    try: f, t, ls = links(u)
    except Exception as e: print("ERR post", u, e); continue
    title = re.search(r"<title>(.*?)</title>", t, re.S)
    title = text(title.group(1)).split("|")[0].strip() if title else x
    els = sorted({l for l, _ in ls if re.search(r"/entrylist/20\d\d/[^/]+/entry_list2\.htm$", l)})
    tours.append({"post": u, "title": title, "lists": els})
    for l in els: lists[l] = title
print("tournaments", len(tours), "with lists", sum(1 for t in tours if t["lists"]), "lists", len(lists))

def h(name):
    n = re.sub(r"\s+", "", unicodedata.normalize("NFKC", name)).lower()
    return hashlib.sha256((SALT + n).encode()).hexdigest()[:16]

recs, latin = [], 0
with open(f"{OUT}/records.jsonl", "w", encoding="utf-8") as out:
    for l, title in lists.items():
        time.sleep(0.4)
        try: _, b = get(l)
        except Exception as e: print("ERR list", l, e); continue
        t = dec(b)
        stamp = re.search(r"(20\d\d)/(\d+)/(\d+)\s+\d\d:\d\d", t)
        div = None; n = 0
        for row in re.findall(r"<tr[^>]*>(.*?)</tr>", t, re.S | re.I):
            cells = [text(c) for c in re.findall(r"<t[dh][^>]*>(.*?)</t[dh]>", row, re.S | re.I)]
            if len(cells) == 1 and re.search(r"Total:\s*\d+", cells[0]):
                div = cells[0]; continue
            if len(cells) >= 2 and div and cells[0]:
                if re.search(r"[A-Za-z]{3}", cells[0]): latin += 1
                m = re.search(r"\)\s+(.*?)\s*\(Total", div)
                out.write(json.dumps({"list": l, "title": title, "year": int(l.split("/entrylist/")[1][:4]),
                                      "div_ja": div.split("（")[0].strip(), "div_en": m.group(1) if m else "",
                                      "open": "※" in row, "name": h(cells[0]), "academy": cells[1]}, ensure_ascii=False) + "\n")
                n += 1
        recs.append(n)
json.dump(tours, open(f"{OUT}/tournaments.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print("entries", sum(recs), "lists parsed", len(recs), "rows with latin names", latin)
