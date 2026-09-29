"""Wayback CDX から jbjjf.com のエントリーリスト URL（2023〜2026年）だけを出力する。個人データは含まない。"""
import json, re, time, urllib.request
UA = {"User-Agent": "Mozilla/5.0 (jiujitsu.co.jp data research)"}
for i in range(8):
    try:
        b = urllib.request.urlopen(urllib.request.Request("https://web.archive.org/cdx/search/cdx?url=jbjjf.com/entrylist/*&output=json&fl=original&collapse=urlkey&limit=20000", headers=UA), timeout=180).read(); break
    except Exception as e: print("retry", e); time.sleep(10 * (i + 1))
urls = sorted({re.sub(r"^https?://(www\.)?", "https://www.", r[0]).split("?")[0] for r in json.loads(b)[1:]})
print("=====URLS=====")
for u in urls:
    if re.search(r"/entrylist/20(2[3-6])/[^/]+/entry_list2\.htm$", u): print(u)
print("=====END=====")
