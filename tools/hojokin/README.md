# /hojokin/ 補助金ページ

全国の柔術道場・ジムが申請できそうな補助金を [Jグランツ公開API](https://developers.digital.go.jp/documents/jgrants/api/)
から毎朝 06:30 JST に取得し、`hojokin/index.html` を生成して push する。

## 作り

- `build.py` — 取得・絞り込み・採点・ページ生成まで。標準ライブラリのみ。
- `config.json` — 検索語と除外条件。ここだけ触れば挙動が変わる。
- `fixtures/sample.json` — API応答を模した固定データ。ネットワークなしで動作確認できる。
- `test_build.py` — オフラインテスト（都道府県展開、除外、XSS対策、テンプレートの健全性）。
- `make_thumb.py` — トップページのカード用サムネイル `assets/hojokin.jpg` を作り直す。
- `.github/workflows/hojokin.yml` — 日次実行。PR時はテストのみ。

## 絞り込みの方針

サーバー側（`build.py`）では**落としすぎない**。落とすのは次の3つだけ:

1. 募集が終了しているもの
2. `901名以上` の枠しかないもの（従業員数欄は「上限」表記なので、小規模な道場はそれ以外どの枠でも対象）
3. タイトルが明確に業種違いのもの（農業・漁業・医療機関など。`exclude_title_keywords`）

都道府県・キーワード・締切での絞り込みは**ページ側**でおこなう。地域欄が空の案件は
取りこぼしを避けて全国扱いにし、「指定なし」と表示する。

「道場向き順」は `preferred_use_purposes` / `preferred_industries` / `title_bonus_keywords`
による加点で並べているだけで、除外には使っていない。

## 手元で動かす

```bash
# 固定データ（ネットワーク不要）
python3 tools/hojokin/build.py --fixture tools/hojokin/fixtures/sample.json --out /tmp/preview.html

# 実データ
python3 tools/hojokin/build.py --out hojokin/index.html

# テスト
python3 tools/hojokin/test_build.py
```

## 注意

- 収録元は jGrants のみ。自治体が自前サイトだけで公募する助成金は載らない。
- 公開ページなので**出典表示（Jグランツからの出典である旨）は消さないこと**。フッターに入れてある。
- 掲載はあくまで候補出し。申請可否は公募要領の原文で確認する旨もフッターに明記してある。
