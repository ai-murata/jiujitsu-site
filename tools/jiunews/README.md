# /jiunews/ きょうの柔術ニュース

国内と海外の柔術ニュースを毎朝 07:00 JST に集め、Claude に「柔術に関係ある記事を選んで、
日本語で見出し・要約・ポイントを書く」よう頼み、`/jiunews/` を作り直して push する。
海外（英語）の記事はこのとき日本語に訳される。

## 作り

- `build.py` — 取得・Claudeでの要約・保存・ページ生成まで。取得とページ生成は標準ライブラリのみ、
  要約だけ `anthropic` SDK を使う。
- `config.json` — 取得元のRSS、何時間前までを見るか、国内/海外それぞれ最大何件載せるか、使うモデル。
- `fixtures/*.xml` — RSS を模した固定データ。ネットワークなしで動作確認できる。
- `test_build.py` — オフラインテスト（RSS/Atom の読み取り、重複・既出の除外、でっち上げidの除外、XSS対策）。
- `.github/workflows/jiunews.yml` — 日次実行。PR時はテストのみ。

できあがるもの:

- `data/jiunews/editions/YYYY-MM-DD.json` — その日の号（ページの元データ）
- `data/jiunews/seen.json` — 一度候補に出た記事の記録（翌日また拾わないため。21日で忘れる）
- `jiunews/index.html` — 最新号＋過去の号の一覧
- `jiunews/YYYY-MM-DD/index.html` — 各日のページ

## 最初の1回だけ：APIキーを入れる

1. [Claude Console](https://platform.claude.com/) で API キーを発行する
2. GitHub の `ai-murata/jiujitsu-site` → Settings → Secrets and variables → Actions →
   **New repository secret** で、名前 `ANTHROPIC_API_KEY`、値にそのキーを貼る
3. Actions タブの「柔術ニュース更新」→ **Run workflow** で試しに1回動かす

キーを入れるまでは、ワークフローは「準備中」のページを作るだけで、Claude は呼ばない。

## 決めごと（大事）

- **リンクURL・出典名・国内/海外の別は RSS の値を使う。** Claude に任せるのは「どれを載せるか」と
  「日本語の文章」だけ。返ってきた id が候補にないもの（でっち上げ）は捨てる（`to_edition`）。
- RSS に載っている**見出しと冒頭部分だけ**を渡し、書かれていないことは補わせない。
  Googleニュース経由の記事は冒頭が取れないので、要約は短めになる。
- 原文を長く訳し写さず、短く要約させる。出典と元記事へのリンクは必ず出す。
- ページ下の「AIが要約・翻訳している／くわしくは元記事で」という注記は消さないこと。
- 同じ日に2回走っても号は作り直さない（`--force` で作り直し）。
- 柔術と関係ある記事が0件の日は号を作らない。

## 取得元を足す・減らす

`config.json` の `feeds` に `name`（出典名として表示）、`region`（`jp` か `intl`）、`url` を足すだけ。
1つのフィードが落ちても他は続行する（全部落ちたときだけ失敗扱い）。

最初に入れてあるのは、Googleニュース検索（日本語2本・英語1本）と、BJJEE / Jits Magazine /
Grappling Insider の RSS。**作成時の環境からは外部に出られず、実際に取れるかは未確認。**
初回の実行ログ（`! 〇〇: 取得失敗`）を見て、取れないものは差し替える。

## 手元で動かす

```bash
# 固定データ＋見本の文章（ネットワークもAPIも不要）
python3 tools/jiunews/build.py --root /tmp/jn --fixture-dir tools/jiunews/fixtures --fake-llm

# 本番と同じ（ANTHROPIC_API_KEY が要る）
pip install anthropic
python3 tools/jiunews/build.py

# 保存済みの号からページだけ作り直す（デザインを変えたとき）
python3 tools/jiunews/build.py --render-only

# テスト
python3 tools/jiunews/test_build.py
```

## お金のこと

1日1回、Claude Opus 5.5 を1回呼ぶだけ（候補50件前後を渡して1回で返してもらう）。
入力・出力あわせて1回数万トークン程度なので、1日あたり数十円ほどの見込み。
