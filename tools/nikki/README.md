# /blog/nikki/ クラウド日記

その日に Claude Code とやったこと（このリポジトリの main に入った変更）をもとに、
マネージャー村田亜衣の目線で短い日記を書き、`/blog/nikki/` に載せる。

## 毎晩の動き（APIキー不要）

| 時刻 (JST) | だれが | なにを |
|---|---|---|
| 23:41 | Claude Code のルーティン | [`ROUTINE.md`](ROUTINE.md) の手順で材料を集め、日記を書き、`nikki/YYYY-MM-DD` ブランチで **PR を作る** |
| 翌日 | 村田さん | PR を読んで、よければマージ → 公開 |

- 作業がなかった日は PR を作らない。
- 自動の更新（柔術ニュース・補助金一覧など、`chore(...)` のコミットや Actions のコミット）は
  本文に書かず、ページの最後に件数だけ載せる。
- 手順を変えたいときは `ROUTINE.md`、書き方を変えたいときは `build.py` の `PROMPT` を直す。

## 非公開のページを守る決まり

`config.json` の

- `private_paths` — ここに入るファイルだけを触ったコミットは材料から外す。公開ページといっしょに触ったコミットは、ファイル名の一覧から消す。
- `private_words` — これを含むコミットは丸ごと外す。日記の文章にこれが入っていたら `--apply` が保存を断る。

新しく限定公開のページを作ったら、ここに足すこと。最後は PR を読む村田さんの目が頼り。

## 作り

- `build.py` — 材料集め（`--collect`）、確認と保存（`--apply`）、ページ生成（`--render-only`）。標準ライブラリのみ。
- `test_build.py` — オフラインテスト（日付の切り分け、自動更新・非公開の除外、文章のチェック、エスケープ）。
- `data/nikki/entries/YYYY-MM-DD.json` — 各日の日記（ページの元データ）。手で直したら `--render-only` でページを作り直す。
- `blog/nikki/index.html` — 一覧 / `blog/nikki/YYYY-MM-DD/index.html` — 各日のページ

## 手元で動かす

```bash
python3 tools/nikki/build.py --collect /tmp/nikki --date 2026-09-29   # 材料と prompt.md を作る
# /tmp/nikki/result.json を書く
python3 tools/nikki/build.py --apply /tmp/nikki
python3 tools/nikki/build.py --render-only
python3 tools/nikki/test_build.py
```
