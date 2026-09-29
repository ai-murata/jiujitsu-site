"""結果投稿ページ内のリンク（ナビ以外）を出す。個人名は含まない。"""
import re, urllib.request, urllib.parse, html as H
UA = {"User-Agent": "Mozilla/5.0 (jiujitsu.co.jp data research)"}
def get(u):
    with urllib.request.urlopen(urllib.request.Request(u, headers=UA), timeout=30) as r: return r.geturl(), r.read().decode("utf-8","replace")
for u in ["https://www.jbjjf.com/2026/05/51747/", "https://www.jbjjf.com/2025/02/44704/", "https://www.jbjjf.com/2023/04/35780/"]:
    f, t = get(u)
    body = t.split('class="entry-content')[-1] if 'entry-content' in t else t
    print("\n###", u, "entry-content" in t)
    for h, x in re.findall(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', body, re.S)[:60]:
        x = H.unescape(re.sub(r"<[^>]+>|\s+", " ", x)).strip()[:50]
        if "category" in h or "/upcoming-events/" == h[-17:]: continue
        print("  ", x, "->", urllib.parse.urljoin(f, h))
    for m in sorted(set(re.findall(r'(?:src|href)="([^"]*(?:entrylist|result|\.pdf|ibjjfdb|compsystem)[^"]*)"', t)))[:30]: print("  REF", m)
