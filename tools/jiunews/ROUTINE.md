# 毎朝の柔術ニュース：ルーティンの手順

Claude Code のルーティン（毎朝 06:49 JST）が、このファイルを読んで上から順におこなう。
APIキーは使わない。翻訳・要約は、実行中の Claude 自身が書く。

ニュースの取得は、その前の 06:30 JST に GitHub Actions（`.github/workflows/jiunews.yml`）が済ませ、
`data/jiunews/inbox/` に `candidates.json` と `prompt.md` を置いている。
**ルーティンは外部のニュースサイトにアクセスしない。**

## 1. 最新の main にそろえる

```bash
git fetch origin main
git checkout -B jiunews-daily origin/main
```

## 2. 今日の候補があるか確かめる

```bash
python3 -c "import json;print(json.load(open('data/jiunews/inbox/candidates.json'))['date'])"
TZ=Asia/Tokyo date +%Y-%m-%d
```

- ファイルが無い、または日付が今日（JST）でなければ、**ここで終わり**（何もコミットしない）。
  Actions の「柔術ニュースの候補集め」が失敗していないかだけ報告する。

## 3. 選んで日本語にまとめる

`data/jiunews/inbox/prompt.md` を**全部**読み、そこに書かれた決まりどおりに
`data/jiunews/inbox/result.json` を書く。

- 候補にない話や、見出し・抜粋に書かれていないこと（数字、結果、発言）を足さない。
- `id` は候補の `id` をそのまま写す。リンクURLは書かない（プログラムが候補から付ける）。
- 英語の記事は日本語に訳して要約する。原文を長く訳し写さない。

## 4. 号にしてページを作る

```bash
python3 tools/jiunews/build.py --apply data/jiunews/inbox
python3 tools/jiunews/test_build.py
rm -rf data/jiunews/inbox
```

## 5. main に反映する

```bash
git add -A jiunews data/jiunews
git commit -m "chore(jiunews): 柔術ニュースを更新 ($(TZ=Asia/Tokyo date +%Y-%m-%d))"
git push origin HEAD:main
```

- 触ってよいのは `jiunews/` と `data/jiunews/` だけ。ほかのファイルが変わっていたらコミットしない。
- push が弾かれたら `git pull --rebase origin main` してもう一度（3回まで）。
- PR は作らない。

## 6. 報告

何件載せたか（国内○件・海外○件）を短く書いて終わる。
