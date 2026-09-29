# 毎朝の柔術ニュース：ルーティンの手順

Claude Code のルーティン（毎朝 06:49 JST）が、このファイルを読んで上から順におこなう。
APIキーは使わない。翻訳・要約は、実行中の Claude 自身が書く。

作業フォルダは `/tmp/jiunews`（リポジトリの外）を使う。

## 1. 最新の main にそろえる

```bash
git fetch origin main
git checkout -B jiunews-daily origin/main
```

## 2. ニュースの候補を集める

```bash
python3 tools/jiunews/build.py --collect-only /tmp/jiunews
```

- 「今日の号はもうあります」「新しい候補がない」と出たら、**ここで終わり**（何もコミットしない）。
- 「すべてのフィードの取得に失敗しました」と出たら、ネットワーク設定で次のホストが
  許可されているかが原因のことが多い。失敗したホスト名を報告して終わる：
  `news.google.com` `www.bjjee.com` `jitsmagazine.com` `grapplinginsider.com`
- 一部のフィードだけ `! 〇〇: 取得失敗` と出るのは続けてよい。

## 3. 選んで日本語にまとめる

`/tmp/jiunews/prompt.md` を**全部**読み、そこに書かれた決まりどおりに
`/tmp/jiunews/result.json` を書く。

- 候補にない話や、見出し・抜粋に書かれていないこと（数字、結果、発言）を足さない。
- `id` は候補の `id` をそのまま写す。リンクURLは書かない（プログラムが候補から付ける）。
- 英語の記事は日本語に訳して要約する。原文を長く訳し写さない。

## 4. 号にしてページを作る

```bash
python3 tools/jiunews/build.py --apply /tmp/jiunews
python3 tools/jiunews/test_build.py
```

## 5. main に反映する

```bash
git add -A jiunews data/jiunews
git commit -m "chore(jiunews): 柔術ニュースを更新 ($(TZ=Asia/Tokyo date +%Y-%m-%d))"
git push origin HEAD:main
```

- 触ってよいのは `jiunews/` と `data/jiunews/` だけ。ほかのファイルが変わっていたらコミットしない。
- push が弾かれたら `git pull --rebase origin main` してもう一度（3回まで）。
- それでも git で push できないときは、GitHub のツール（push_files）で同じファイルを main に書き込む。
- PR は作らない。

## 6. 報告

何件載せたか（国内○件・海外○件）と、取得に失敗したフィードがあればその名前を、短く書いて終わる。
