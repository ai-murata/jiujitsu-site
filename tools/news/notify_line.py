#!/usr/bin/env python3
"""まだ配信していないお知らせを、LINE公式アカウントの友だち全員に1通送る。

  python3 tools/news/notify_line.py            # 何を送るか見るだけ（送信しない）
  python3 tools/news/notify_line.py --send     # 実際に送る

環境変数 LINE_CHANNEL_ACCESS_TOKEN が必要。無いときは中身を表示するだけで終わる。
配信済みの id は data/news-sent.json に記録され、二度と送られない。
何件たまっていても送るのは1通なので、LINEの無料枠（月200通）は1回分しか減らない。
"""
import argparse
import json
import os
import sys
import urllib.error
import urllib.request
import uuid
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from build import ROOT, SITE, load  # noqa: E402

SENT_PATH = ROOT / "data" / "news-sent.json"
API = "https://api.line.me/v2/bot/message/broadcast"
MAX_AT_ONCE = 5  # これを超えるときは事故とみなして止める


def read_sent():
    if not SENT_PATH.exists():
        return {"_説明": "LINEへ配信済みのお知らせid。手で消すと再配信されます。", "sent": []}
    return json.loads(SENT_PATH.read_text(encoding="utf-8"))


def compose(entries):
    head = "jiujitsu.co.jp に新しいページができました。"
    if len(entries) == 1:
        e = entries[0]
        return f"{head}\n\n{e['title']}\n{e['summary']}\n\n{SITE}{e['url']}"
    body = "\n\n".join(f"▼ {e['title']}\n{SITE}{e['url']}" for e in entries)
    return f"{head}\n\n{body}"


def broadcast(text, token):
    req = urllib.request.Request(
        API,
        data=json.dumps({"messages": [{"type": "text", "text": text}]}).encode("utf-8"),
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}",
            "X-Line-Retry-Key": str(uuid.uuid4()),
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=30) as res:
        return res.status


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--send", action="store_true", help="実際にLINEへ送る")
    ap.add_argument("--force", action="store_true", help="未配信が多くても送る")
    args = ap.parse_args()

    _, entries = load()
    state = read_sent()
    sent = set(state.get("sent", []))
    pending = [e for e in entries if e["id"] not in sent]
    pending.reverse()  # 古い順に並べる

    if not pending:
        print("未配信のお知らせはありません。")
        return 0

    text = compose(pending)
    print(f"未配信 {len(pending)} 件:")
    print("-" * 40)
    print(text)
    print("-" * 40)

    if len(pending) > MAX_AT_ONCE and not args.force:
        print(f"未配信が {len(pending)} 件あります（上限 {MAX_AT_ONCE} 件）。"
              "配信済みの記録が消えている可能性があるので送りません。"
              "本当に送るなら --force を付けてください。", file=sys.stderr)
        return 1

    token = os.environ.get("LINE_CHANNEL_ACCESS_TOKEN", "").strip()
    if not args.send:
        print("※ 送信していません（送るには --send）")
        return 0
    if not token:
        print("※ LINE_CHANNEL_ACCESS_TOKEN が未設定のため送信していません。", file=sys.stderr)
        return 0

    try:
        status = broadcast(text, token)
    except urllib.error.HTTPError as err:
        print(f"LINEへの送信に失敗しました: {err.code} {err.read().decode('utf-8', 'replace')}",
              file=sys.stderr)
        return 1

    state["sent"] = list(state.get("sent", [])) + [e["id"] for e in pending]
    SENT_PATH.write_text(
        json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"LINEへ1通送りました（HTTP {status}・{len(pending)} 件ぶん）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
