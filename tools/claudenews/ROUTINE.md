# 毎朝の Claude ニュース：ルーティンの手順

Claude Code のルーティン（毎日 11:52 JST）が、このファイルを読んで上から順におこなう。
APIキーは使わない。翻訳・要約は、実行中の Claude 自身が書く。

ニュースの取得は、その前の 07:10 JST に GitHub Actions（`.github/workflows/claudenews.yml`）が済ませ、
`data/claudenews/inbox/` に `candidates.json` と `prompt.md` を置いている。
**ルーティンは外部のニュースサイトにアクセスしない。**

## 1. 最新の main にそろえる

```bash
git fetch origin main
git checkout -B claudenews-daily origin/main
```

## 2. 今日の候補があるか確かめる

```bash
python3 -c "import json;print(json.load(open('data/claudenews/inbox/candidates.json'))['date'])"
TZ=Asia/Tokyo date +%Y-%m-%d
```

- ファイルが無い、または日付が今日（JST）でなければ、**ここで終わり**（何もコミットしない）。
  Actions の「Claude ニュースの候補集め」が失敗していないかだけ報告する。

## 3. 選んで日本語にまとめる

`data/claudenews/inbox/prompt.md` を**全部**読み、そこに書かれた決まりどおりに
`data/claudenews/inbox/result.json` を書く。

- 新しいモデルの発表と、新しいサービス・機能の開始（Marketplace など）を最優先で選び、上に並べる。
- 候補にない話や、見出し・抜粋に書かれていないこと（数字、性能、料金、発言）を足さない。
- `id` は候補の `id` をそのまま写す。リンクURLは書かない（プログラムが候補から付ける）。
- 英語の記事は日本語に訳して要約する。原文を長く訳し写さない。

## 4. 号にしてページを作る

```bash
python3 tools/claudenews/build.py --apply data/claudenews/inbox
python3 tools/claudenews/test_build.py
rm -rf data/claudenews/inbox
```

## 5. main に反映する

```bash
git add -A claudenews data/claudenews
git commit -m "chore(claudenews): Claude ニュースを更新 ($(TZ=Asia/Tokyo date +%Y-%m-%d))"
git push origin HEAD:main
```

- 触ってよいのは `claudenews/` と `data/claudenews/` だけ。ほかのファイルが変わっていたらコミットしない。
- push が弾かれたら `git pull --rebase origin main` してもう一度（3回まで）。
- PR は作らない。

## 6. 報告

載せた記事の見出しを、新モデル・新サービスのものを先頭にして箇条書きで短く書き、
最後に https://jiujitsu.co.jp/claudenews/ を添えて終わる。
