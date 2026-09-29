"""jbjjf.com のサイト構造を調べる（リンク一覧だけを出力。個人データは出さない）。"""
import re, sys, urllib.request, urllib.parse
from collections import deque

START = sys.argv[1:] or ["https://www.jbjjf.com/"]
KEY = re.compile(r"entry|エントリー|result|結果|tournament|大会|competition|pdf|event|championship|選手権", re.I)
UA = {"User-Agent": "Mozilla/5.0 (jiujitsu.co.jp data research)"}

def get(u):
    req = urllib.request.Request(u, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as r:
        return r.geturl(), r.headers.get("Content-Type", ""), r.read()

seen, q = set(), deque((u, 0) for u in START)
while q and len(seen) < 40:
    u, d = q.popleft()
    if u in seen: continue
    seen.add(u)
    try:
        final, ctype, body = get(u)
    except Exception as e:
        print(f"ERR {u} {e}"); continue
    print(f"\n### {final} [{ctype}] {len(body)} bytes depth={d}")
    if "html" not in ctype: continue
    html = body.decode("utf-8", "replace")
    t = re.search(r"<title>(.*?)</title>", html, re.S)
    print("title:", t.group(1).strip()[:100] if t else "")
    for href, text in re.findall(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', html, re.S):
        text = re.sub(r"<[^>]+>|\s+", " ", text).strip()[:60]
        full = urllib.parse.urljoin(final, href)
        if KEY.search(href + " " + text):
            print(f"  {text} -> {full}")
            host = urllib.parse.urlparse(full).netloc
            if d < 2 and "jbjjf" in host and not full.lower().endswith(".pdf"):
                q.append((full, d + 1))
