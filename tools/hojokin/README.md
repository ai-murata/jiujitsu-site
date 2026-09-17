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

## APIの実際の返り（重要）

一覧API `GET /subsidies` は**利用目的・業種・キャッチコピーを返さない**。返ってくるのは
`id / title / name / institution_name / subsidy_max_limit / acceptance_* /
target_area_search / target_number_of_employees` だけ。

そのため各件について詳細API `GET /subsidies/id/{id}` を引き、`use_purpose` / `industry` /
`subsidy_catch_phrase` / `front_subsidy_detail_page_url` を補っている（`build.enrich`）。

- `name` は `S-00007152` のような内部コード。**表に出さない。**
- `institution_name` は実施機関名ではなく制度の通称（「ものづくり補助金」など）。
  162件中108件はタイトルの一部だったので、タイトルに無いときだけ「通称」として出す。
  **このAPIは実施機関名を返さない。**
- 詳細ページURLは `front_subsidy_detail_page_url` が正。`portal_url_template` は保険。
- `industry` は20業種すべてを並べる案件が全体の7割。一致しても「誰でも対象」以上の意味はない。

`fixtures/sample.json` はこの形（一覧は薄く、詳細で補う）に合わせてある。**実APIが返さない
フィールドをフィクスチャに足さないこと。** ここがずれていたせいで、実施機関名に内部コードが
出たまま公開してしまったことがある。

## 「使いどころ」の出し方

カードに出る「使いどころ」は、次の2つを**両方**満たしたときだけ出す。当たらなければ黙る。

1. 道場の業種（`preferred_industries`）が対象業種に入っている
2. タイトルかキャッチに具体的な語（`title_hints`: 持続化・空き店舗・創業など）が出ている

利用目的（`purpose_hints`）は1と2を満たした案件の**補足としてのみ**添える。利用目的だけで
書かせると、「設備整備・IT導入をしたい」が全体の7割に付くため、石油精製や天然ガス設備の
補助金に「2店舗目の出店に」と書いてしまう（実データで確認済み）。同じ理由で「設備」「省エネ」
「販路」のような汎用語は `title_hints` に入れない。

実データでは162件中19件ほどにだけ「使いどころ」が付く。付かないほうが多いのが正常。

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
