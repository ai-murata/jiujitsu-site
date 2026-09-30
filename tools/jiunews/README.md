# /jiunews/ きょうの柔術ニュース

国内と海外の柔術ニュースを毎朝集め、柔術に関係ある記事を選んで、日本語で見出し・要約・ポイントを書き、
`/jiunews/` を作り直して main に反映する。海外（英語）の記事はこのとき日本語に訳される。

## 毎朝の動き（APIキー不要）

| 時刻 (JST) | だれが | なにを |
|---|---|---|
| 06:30 | GitHub Actions（`jiunews.yml`） | `build.py --collect-only data/jiunews/inbox` で RSS から候補を集め、`candidates.json` と `prompt.md` を main に置く |
| 06:49 | Claude Code のルーティン | [`ROUTINE.md`](ROUTINE.md) の手順で `prompt.md` を読み、`result.json`（選んだ記事と日本語の文章）を書き、`build.py --apply` で号とページを作って main に push |

- 外部のニュースサイトにつなぐのは Actions だけ。ルーティンは GitHub にだけつながればよいので、
  環境のネットワーク設定を変える必要はない。
- 翻訳・要約は Claude の月額プランの使用枠の中でおこなわれ、APIの料金はかからない。
- 手順を変えたいときは `ROUTINE.md` を直せばよい（ルーティンは毎回このファイルを読む）。
- ルーティンが動かなかった日の inbox は、翌朝の Actions が捨てて取り直す。

`build.py` を引数なしで動かすと、APIキー（`ANTHROPIC_API_KEY`）で Claude を呼んで取得から要約まで
1回でおこなう（手元で試すとき用）。

## 作り

- `build.py` — 取得・保存・ページ生成（標準ライブラリのみ）。APIで要約するときだけ `anthropic` SDK を使う。
- `ROUTINE.md` — 毎朝のルーティンが読む手順書。
- `config.json` — 取得元のRSS、何時間前までを見るか、国内/海外それぞれ最大何件載せるか。
- `fixtures/*.xml` — RSS を模した固定データ。ネットワークなしで動作確認できる。
- `test_build.py` — オフラインテスト（RSS/Atom の読み取り、重複・既出の除外、でっち上げidの除外、XSS対策、2段階実行）。
- `.github/workflows/jiunews.yml` — 毎朝の候補集め。PR時はテストのみ。

できあがるもの:

- `data/jiunews/editions/YYYY-MM-DD.json` — その日の号（ページの元データ）
- `data/jiunews/inbox/` — その朝の候補（ルーティンが使い終わったら消す）
- `data/jiunews/seen.json` — 一度候補に出た記事の記録（翌日また拾わないため。21日で忘れる）
- `jiunews/index.html` — 最新号＋過去の号の一覧
- `jiunews/YYYY-MM-DD/index.html` — 各日のページ

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

# ルーティンと同じ2段階（result.json は自分で書く）
python3 tools/jiunews/build.py --collect-only /tmp/jiunews
python3 tools/jiunews/build.py --apply /tmp/jiunews

# APIで一気に（ANTHROPIC_API_KEY が要る）
pip install anthropic
python3 tools/jiunews/build.py

# 保存済みの号からページだけ作り直す（デザインを変えたとき）
python3 tools/jiunews/build.py --render-only

# テスト
python3 tools/jiunews/test_build.py
```

## お金のこと

ルーティンで動かす限り、Claude の月額プランの使用枠を毎朝少し使うだけで、追加の料金はかからない。
APIキーで動かす場合は、1日1回 Claude Opus 5.5 を呼ぶので、1日あたり数十円ほどの見込み。
