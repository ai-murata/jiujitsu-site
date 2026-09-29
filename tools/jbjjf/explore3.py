"""Wayback Machine の CDX から jbjjf.com/entrylist/ の URL 一覧を取り、今も開けるか確かめる。"""
import json, re, urllib.request, collections
UA = {"User-Agent": "Mozilla/5.0 (jiujitsu.co.jp data research)"}
import time
def get(u, t=90, tries=1):
    for i in range(tries):
        try:
            with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=t) as r: return r.status, r.read()
        except Exception as e:
            print("retry", i, e); err = e; time.sleep(min(60, 10 * (i + 1)))
    raise err
_, b = get("https://web.archive.org/cdx/search/cdx?url=jbjjf.com/entrylist/*&output=json&fl=original,timestamp,statuscode&collapse=urlkey&limit=20000", 180, 8)
rows = json.loads(b)[1:]
urls = sorted({re.sub(r"^https?://(www\.)?", "https://www.", r[0]).split("?")[0] for r in rows})
print("cdx rows", len(rows), "unique", len(urls))
el = [u for u in urls if re.search(r"/entrylist/20(2[3-6])/[^/]+/entry_list2?\.htm", u, re.I)]
print("2023-2026 entry_list urls", len(el))
by = collections.Counter((u.split("/entrylist/")[1][:4], u.rsplit("/", 1)[1]) for u in el); print(by)
print("sample", el[:15])
ok = 0
for u in el[:8]:
    try: s, b = get(u, 30); ok += 1; print("live", s, len(b), u)
    except Exception as e: print("dead", e, u)
print("other files", collections.Counter(u.rsplit("/",1)[1] for u in urls if "/entrylist/202" in u).most_common(15))
