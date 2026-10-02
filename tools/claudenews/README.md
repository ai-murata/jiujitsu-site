# /claudenews/ きょうの Claude ニュース

Claude（Anthropic）に関する国内と海外のニュースを毎朝集め、**新しいモデルの発表**と
**新しいサービス・機能の開始**（Marketplace など）を優先して選び、日本語で見出し・要約・ポイントを書き、
`/claudenews/` を作り直して main に反映する。

仕組みは [/jiunews/](../jiunews/README.md)（きょうの柔術ニュース）と同じ。
`build.py` は jiunews のものを写して、文言・選び方・保存先だけを変えてある。

## 毎朝の動き（APIキー不要）

| 時刻 (JST) | だれが | なにを |
|---|---|---|
| 07:10 | GitHub Actions（`claudenews.yml`） | `build.py --collect-only data/claudenews/inbox` で RSS から候補を集め、`candidates.json` と `prompt.md` を main に置く |
| 11:52 | Claude Code のルーティン | [`ROUTINE.md`](ROUTINE.md) の手順で `prompt.md` を読み、`result.json` を書き、`build.py --apply` で号とページを作って main に push |

- GitHub Actions の時刻指定は混んでいると数時間遅れる（実際に 07:10 予定が 10:15 ごろになった）。
  ルーティンはその遅れを見込んで昼前に動かしている。
- 外部のニュースサイトにつなぐのは Actions だけ。ルーティンは GitHub にだけつながればよい。
- 手順を変えたいときは `ROUTINE.md` を直せばよい（ルーティンは毎回このファイルを読む）。
- 選び方（何を優先するか・何を載せないか）を変えたいときは `build.py` の `SYSTEM_PROMPT` を直す。

## 取得元

`config.json` の `feeds`。最初に入れてあるのは:

- Googleニュース検索（日本語・英語）: `Anthropic OR "Claude AI" OR "Claude Code"`
- Googleニュース検索: `site:anthropic.com OR site:claude.com`（公式の発表）
- Claude Code の GitHub リリース（Atom）

**作成時の環境からは外部に出られず、実際に取れるかは未確認。** 初回の実行ログ
（`! 〇〇: 取得失敗`）を見て、取れないものは差し替える。

## できあがるもの

- `data/claudenews/editions/YYYY-MM-DD.json` — その日の号
- `data/claudenews/seen.json` — 一度候補に出た記事の記録（21日で忘れる）
- `claudenews/index.html` — 最新号＋過去の号の一覧
- `claudenews/YYYY-MM-DD/index.html` — 各日のページ

## 手元で動かす

```bash
python3 tools/claudenews/build.py --root /tmp/cn --fixture-dir tools/jiunews/fixtures --fake-llm
python3 tools/claudenews/test_build.py
```
