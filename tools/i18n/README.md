# 外国語版（/en/ /ko/ /pt/）

トップ・柔術の主要ページ・ブログを、日本語のページから英語・韓国語・ポルトガル語に作る道具。
見た目は日本語版のまま文章だけを差し替える。ページ右上の言語ボタンは `assets/langs.js`。

- 訳の本体：`data/i18n/<言語>.json`（日本語の文 → 訳文の対応表）
- できるページ：`en/` `ko/` `pt/`（手で直さない。build で上書きされる）
- 対象のページ：`build.py` の `MAIN_PAGES` と、`blog/` の公開中の全記事

## 記事を足した・日本語を直したとき

```
python3 tools/i18n/build.py todo /tmp/i18n-work     # 未訳の文を todo/<言語>/ に書き出す
# todo の番号どおりに訳して done/<言語>/<ページ>.json に書く
python3 tools/i18n/build.py absorb /tmp/i18n-work   # 対応表に取り込む
python3 tools/i18n/build.py build                   # 3言語のページを作り直す
python3 tools/i18n/build.py check                   # 訳もれ・タグ違い・日本語の残りを調べる
```

訳語の統一ルール（人名・柔術用語）は `tools/i18n/GLOSSARY.md`。

## 注意

- トップの外国語版には、毎朝変わる新着欄とニュース欄を出さない。外国語版がないページのカードも外す（`prune_home`）
- ブログ一覧の外国語版には、訳があるページだけを出す（`prune_blog_list`）
- 道場ガイドと教科書は訳さず日本語版へリンクする。教科書は `?lang=en` で言語を選んだ状態で開く
- `/search/` の検索は日本語のページだけを探す（`tools/search/build.py` で外している）
- 画像の中の日本語は訳されない
