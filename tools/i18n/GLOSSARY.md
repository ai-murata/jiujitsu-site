# jiujitsu.co.jp 翻訳の指示書

jiujitsu.co.jp（Jiu Labo）は、柔術道場のマネージャー村田亜衣さんが、AI（Claude）で作ったものを置いているサイト。
読者は海外の柔術関係者と、AIに興味のある非エンジニア。

## ファイルの形
- 入力: `todo/<言語>/<ページ>.json` … `{"1": "日本語", "2": "日本語", ...}`
- 出力: `done/<言語>/<ページ>.json` … `{"1": "訳文", "2": "訳文", ...}` 同じ番号をすべて埋める。Write ツールで書く
- 正しいJSONにする（訳文の中の `"` は `\"`、改行は `\n`）。書いたら python3 -m json.tool で壊れていないか確かめる
- 同じページの番号は上から順に本文の流れになっている。前後を読んで文脈に合わせて訳す

## 崩してはいけないもの
- HTMLタグと属性は全部そのまま残す（`<a href="...">`、`<b>`、`<span class="...">`、`<time datetime="...">`、`<br>`）。開き閉じの数を変えない。href の値は変えない。文の並びに合わせてタグの位置は動かしてよい
- ただし `<ruby>` `<rt>` `<rp>`（日本語のふりがな）は訳文では取り除いて普通の文字にしてよい
- `<img>` の alt など、タグの中の属性の日本語は訳す
- `${...}` はそのまま残す（プログラムの中の文字列）
- `\n` や `\'` などのエスケープは入力にあればそのまま扱う
- 訳文に日本語の文字を残さない。必要な固有名詞はローマ字にする。例外なし
  - 日本語そのものを説明している箇所（語呂合わせ、ふりがな、日本語の言葉遊び）は、ローマ字＋意味の説明にするか、その言語で同じ狙いが伝わる言い方に変える

## 訳し方
- 直訳しない。その言語の読者が自然に読める、話し言葉寄りのやさしい文章にする。亜衣さんのブログは一人称で親しみやすい語り口。語り口を残す
- 中身を足さない・削らない。数字・金額・日付・製品名は変えない。金額は円のまま（例: 3,000 yen）
- 見出しは短く保つ。ボタン文言・短いラベルは短く訳す（カードやボタンからはみ出さないように）
- 「ですます」の丁寧さは、英語: friendly plain English／韓国語: 해요체 または 합니다체（ブログは해요체、説明文・会社情報は합니다체）／ポルトガル語: ブラジルのポルトガル語、você
- 日付: 2026.09.28 のような表記はそのまま。「2026年9月28日」は各言語の普通の書き方に
- 「やさしい日本語で」「日本語で要約」など日本語版を説明する文は、その言語版として不自然なら正直な形に直す（要約が日本語で書かれたこと自体を偽らない。例: 「summarized from overseas papers」）
- 読者に日本の文脈が必要な語（例: ワープロ、確定申告）は、短い補いを入れてよい
- 「亜衣（AI）」のしゃれ: トップの「AIが運用する、AI研究所。」は英語なら "An AI lab, run by Ai." のように、亜衣さんの名前 Ai と AI を掛けて残す

## 統一する名前
| 日本語 | en / pt | ko |
|---|---|---|
| 村田良蔵 | Ryozo Murata | 무라타 료조 |
| 村田亜衣 | Ai Murata | 무라타 아이 |
| 良蔵さん | Ryozo | 료조 씨 |
| 亜衣さん | Ai | 아이 씨 |
| 濱田さん | Hamada | 하마다 씨 |
| 河野さん | Kono | 고노 씨 |
| カリオカ先生／クリスチアーノ・カリオカ | Cristiano Carioca | 크리스치아누 카리오카 |
| ホイラー・グレイシー | Royler Gracie | 호일러 그레이시 |
| Jiu Labo / YAWARA / SWEEP / OVER LIMIT SAPPORO / Jiu Fight / JiuFlow / SJJJF / SJJIF / ASJJF / IBJJF / Claude / Claude Code | そのまま | そのまま |
| 株式会社BUTTI ON LINE | BUTTI ON LINE Inc. | BUTTI ON LINE Inc. |
| スポーツ柔術日本連盟 | Sports Jiu-Jitsu Japan Federation | 일본 스포츠 주짓수 연맹 |
| 原宿・北参道・札幌 | Harajuku, Kitasando, Sapporo | 하라주쿠, 기타산도, 삿포로 |

他の日本人の名前は、名→姓の順にせず一般的なローマ字で（en/pt）。ko は日本語の読みをハングルで。さん付けは en/pt では外し、ko は 씨。

## 柔術の用語
| 日本語 | en | ko | pt |
|---|---|---|---|
| ブラジリアン柔術／柔術 | Brazilian jiu-jitsu / jiu-jitsu | 브라질리언 주짓수 / 주짓수 | jiu-jitsu brasileiro / jiu-jitsu |
| 道場／ジム | gym / academy | 도장 | academia |
| 白帯 青帯 紫帯 茶帯 黒帯 | White belt, Blue belt, Purple belt, Brown belt, Black belt | 화이트 벨트 블루 벨트 퍼플 벨트 브라운 벨트 블랙 벨트 | Faixa branca, Faixa azul, Faixa roxa, Faixa marrom, Faixa preta |
| 帯（単独の語。「白帯」から「帯」を除く処理に使う） | ` belt`（先頭に空白） | ` 벨트`（先頭に空白） | `Faixa `（末尾に空白） |
| 道着 | gi | 도복 | kimono |
| 計量 | weigh-in | 계체 | pesagem |
| 減量 | weight cut | 체중 감량 | corte de peso |
| 一本勝ち | submission win | 서브미션 승 | vitória por finalização |
| 優勝 | champion / gold | 우승 | campeão |
| 出稽古 | visiting another gym to train | 타 도장 방문 훈련 | treinar em outra academia |
| インストラクター養成講座 | Instructor Course | 인스트럭터 양성 과정 | Curso de Instrutores |
| マスター2 黒帯フェザー級 | Master 2 Black Belt Feather | 마스터2 블랙 벨트 페더급 | Master 2 Faixa Preta Pena |
| ライト級／レーヴィ級／ペナ級 | Light / Leve / Pena | 라이트급 / 레베급 / 페나급 | Leve / Leve / Pena |
| アブソルート級 | Absolute | 앱솔루트 | Absoluto |
| 大会 | tournament | 대회 | campeonato |
| マット | mat | 매트 | tatame |
| 速報 | live results | 실시간 결과 | resultados ao vivo |

## 進め方
割り当てられたページを順に訳し、1ページごとに done に書き出す（途中で止まっても済んだ分が残るように）。
全部終わったら、終えたページ名と、判断に迷った箇所があれば数行で報告する。報告は日本語で。
