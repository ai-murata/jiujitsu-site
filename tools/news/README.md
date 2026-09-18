# 新着のお知らせ と LINE配信

新しいページを作ったとき、**読者に「できました」を届ける**ための仕組みです。

## お知らせを1件足す

`data/news.json` の `entries` の **いちばん上** に、1つ足して push するだけ。

```json
{
  "id": "genryo",
  "date": "2026-10-01",
  "title": "減量帳",
  "url": "/genryo/",
  "summary": "試合前の減量を、記録と計画で乗り切るための道具です。"
}
```

| 項目 | 書き方 |
|---|---|
| `id` | 英数字で短く。**一度付けたら変えない**（変えるともう一度LINEに流れます） |
| `date` | `2026-10-01` の形 |
| `title` | 新着欄とLINEに出る見出し |
| `url` | `/genryo/` のように `/` から始める |
| `summary` | 1〜2文。LINEの本文にもそのまま出ます |

push すると自動で、

1. トップページの「新着」欄が新しくなる（上から4件）
2. `feed.xml`（RSS）が作り直される
3. **LINE公式アカウントの友だち全員に1通** 届く

## 手元で確かめる

```bash
python3 tools/news/test_build.py    # おかしなところがないか検査
python3 tools/news/build.py         # 新着欄と feed.xml を作り直す
python3 tools/news/notify_line.py   # LINEに何が送られるか見るだけ（送らない）
```

## LINE配信を動かすための準備（最初の1回だけ）

1. LINE公式アカウントを決める（新規に作るか、既存のアカウントを使うか）
2. [LINE Developers](https://developers.line.biz/) でそのアカウントの **Messaging API** を有効にし、**チャネルアクセストークン（長期）** を発行する
3. GitHub の `ai-murata/jiujitsu-site` → Settings → Secrets and variables → Actions →
   **New repository secret** で、名前 `LINE_CHANNEL_ACCESS_TOKEN`、値にそのトークンを貼る
4. `data/news.json` の `line_url` に友だち追加URL（`https://lin.ee/～`）を入れて push
   → トップページに「LINEで更新を受け取る」ボタンが出ます

トークンを入れるまでは、新着欄とRSSだけが動き、LINEへは何も送りません。

## 気をつけること

- **配信は1回のpushにつき1通**。何件まとめて足しても1通にまとまるので、LINEの通数は1しか減りません
- 送ったお知らせの `id` は `data/news-sent.json` に記録され、二度と送られません。**この記録を手で消すと、消した分がもう一度流れます**
- 未配信が6件以上たまっていると、事故とみなして自動では送りません（記録が壊れたとき用の安全装置）
- **大会当日の速報は、ここには流しません。** `/tournament/` は1日に何十回も更新されるので、混ぜると読者に嫌われます
