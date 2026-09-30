# 毎晩のクラウド日記：ルーティンの手順

Claude Code のルーティン（毎晩 23:41 JST）が、このファイルを読んで上から順におこなう。
APIキーは使わない。日記の文章は、実行中の Claude 自身が書く。

**日記は PR で出すだけ。main には push しない・マージしない。** 村田さんが読んで、よければ自分でマージする。

## 1. 最新の main にそろえる

```bash
git fetch origin main
# ルーティンが遅れて日付をまたいでも（0〜5時台）、前の日の日記にする
DATE=$(TZ=Asia/Tokyo date -d '-6 hours' +%Y-%m-%d)
git checkout -B "nikki/$DATE" origin/main
```

## 2. 今日の材料を集める

```bash
python3 tools/nikki/build.py --collect data/nikki/inbox --date "$DATE"
```

- 「日記にする作業がありません」と出たら、**ここで終わり**（何もコミットしない・PR も作らない）。
  「今日はお休みでした」とだけ報告する。

## 3. 日記を書く

`data/nikki/inbox/prompt.md` を**全部**読み、そこに書かれた決まりどおりに
`data/nikki/inbox/result.json` を書く。

- 村田亜衣さんの一人称（「私」）。ブログ（`blog/*/index.html`）の口調をまねる。迷ったら1本読んでから書く。
- 材料にないこと（人の名前・数字・お客さまの話・感情の作り話）は足さない。
- 非公開のページのことは書かない（`prompt.md` に言葉の一覧がある）。

## 4. ページを作る

```bash
python3 tools/nikki/build.py --apply data/nikki/inbox
python3 tools/nikki/test_build.py
rm -rf data/nikki/inbox
```

- `--apply` が「result.json を直してください」と言ったら、その内容どおりに直してもう一度。

## 5. PR を出す

```bash
git add -A blog/nikki data/nikki
git commit -m "chore(nikki): クラウド日記 ($DATE)"
git push -u origin "nikki/$DATE"
```

- 触ってよいのは `blog/nikki/` と `data/nikki/` だけ。ほかのファイルが変わっていたらコミットしない。
- GitHub のツール（`create_pull_request`）で `ai-murata/jiujitsu-site` に PR を作る。
  - base: `main` / head: `nikki/$DATE`
  - タイトル: `クラウド日記 $DATE：<日記のタイトル>`
  - 本文: 日記の本文（タイトル・書き出し・項目・ひとこと）をそのまま貼り、最後に
    「公開してよければマージしてください。直したいところはこの PR にコメントするか、ブランチで直してください。」と書く。
- **マージはしない。**

## 6. 報告

PR の URL と日記のタイトルを短く書いて終わる。
