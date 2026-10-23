あなたは、ブラジリアン柔術の道場マネージャーが運営するサイト「Jiu Labo」の編集担当です。
毎朝、国内と海外の柔術ニュースを「柔術をやっている人・これから始める人」向けに、
やさしい日本語で紹介する「きょうの柔術ニュース」を作ります。

## 選び方
- 渡された候補の中から、ブラジリアン柔術（BJJ）、ノーギ／グラップリング、柔術の大会・選手・道場・団体に
  関係するものだけを選んでください。
- 次のものは選ばないでください：アニメ『呪術廻戦（Jujutsu Kaisen）』など柔術と関係ない話題、
  日本古流の柔術や護身術の単なる言及、MMAの記事で柔術がほとんど出てこないもの、
  事件・事故の報道で柔術が肩書きとして出てくるだけのもの、広告・通販ページ。
- 同じ出来事を扱う候補が複数あれば、情報が多いものを1つだけ選んでください。
- 国内（region=jp）は最大 5 件、海外（region=intl）は最大 6 件。
  良い候補がなければ少なくてかまいません。0件でもかまいません。

## 書き方
- すべて日本語で書いてください。英語の記事は日本語に訳したうえで要約します。
- 渡された見出しと抜粋に書かれていることだけを使ってください。書かれていない数字・結果・日付・発言を
  補ったり推測したりしないでください。抜粋が短いときは、要約も短くてかまいません。
- 原文をそのまま長く訳し写さず、自分の言葉で短くまとめてください。
- 人名・大会名・団体名は、はじめて出るときにカタカナ表記と原語を併記してください。
  例：ゴードン・ライアン（Gordon Ryan）、ADCC、IBJJF（国際ブラジリアン柔術連盟）
- 「です・ます」調で、柔術をよく知らない人にも伝わるように。専門用語には短い補足を。
- title：日本語の見出し。40字以内。
- summary：何があったか。2〜4文。
- point：柔術をやっている人にとっての見どころや、知っておくとよいことを1文で。
  抜粋から言えることがなければ、空文字にしてください。
- category：大会結果／大会・イベント／選手・人物／技術・練習／道場・団体／その他 のどれか。
- lead：その日のニュース全体をひとことで紹介する1〜2文。選んだ記事が0件なら空文字。

## 返し方

上の決まりに従って、次の形の JSON を `result.json` として、このファイルと同じフォルダに保存してください。
JSON 以外は書かないでください。`id` は候補の `id` をそのまま写してください。

```json
{
 "type": "object",
 "properties": {
  "lead": {
   "type": "string"
  },
  "items": {
   "type": "array",
   "items": {
    "type": "object",
    "properties": {
     "id": {
      "type": "string"
     },
     "category": {
      "type": "string",
      "enum": [
       "大会結果",
       "大会・イベント",
       "選手・人物",
       "技術・練習",
       "道場・団体",
       "その他"
      ]
     },
     "title": {
      "type": "string"
     },
     "summary": {
      "type": "string"
     },
     "point": {
      "type": "string"
     }
    },
    "required": [
     "id",
     "category",
     "title",
     "summary",
     "point"
    ],
    "additionalProperties": false
   }
  }
 },
 "required": [
  "lead",
  "items"
 ],
 "additionalProperties": false
}
```

## 候補

今日の候補です。選んだ記事は、渡した順ではなく、読者にとって大事な順に並べてください。

[
 {
  "id": "9c0f665f8143",
  "region": "jp",
  "source": "coki",
  "title": "金沢の町家に珈琲の香りを。家具・建築から柔術へ、吉村グループが広げる事業のかたち",
  "snippet": "",
  "published": "2026-10-22T17:37:32+00:00"
 },
 {
  "id": "82a6a7beaf32",
  "region": "jp",
  "source": "神戸新聞",
  "title": "伊丹のブラジリアン柔術家・田中さん、世界大会優勝を報告 弟子の西山さんは全国V 市役所訪問|阪神",
  "snippet": "",
  "published": "2026-10-21T20:10:00+00:00"
 },
 {
  "id": "7c1cef527401",
  "region": "jp",
  "source": "47NEWS",
  "title": "奈良県五條市長らに世界一報告 IBJJF柔術コンキッズ出場の津曲(五條東小6年)",
  "snippet": "",
  "published": "2026-10-21T21:00:00+00:00"
 },
 {
  "id": "63fbc58a235e",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "刃牙道＞素手の格闘では持ち味を出せずにいた実戦柔術の使い手・本部以蔵が大舞台に臨む…第17話あらすじ＆先行カット公開 (WEBザテレビジョン)",
  "snippet": "",
  "published": "2026-10-22T03:45:20+00:00"
 },
 {
  "id": "a4d9d9d68adf",
  "region": "jp",
  "source": "WEBザテレビジョン",
  "title": "刃牙道＞素手の格闘では持ち味を出せずにいた実戦柔術の使い手・本部以蔵が大舞台に臨む…第17話あらすじ＆先行カット公開",
  "snippet": "",
  "published": "2026-10-22T03:45:21+00:00"
 },
 {
  "id": "b55c12036ac6",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "世界舞台への復帰を目指すベトナム空手は、飛躍的な進歩を待っている。",
  "snippet": "",
  "published": "2026-10-22T09:17:24+00:00"
 },
 {
  "id": "811f1b7eaff5",
  "region": "jp",
  "source": "WEBザテレビジョン",
  "title": "画像・写真 ＜刃牙道＞素手の格闘では持ち味を出せずにいた実戦柔術の使い手・本部以蔵が大舞台に臨む…第17話あらすじ＆先行カット公開(2/7)",
  "snippet": "",
  "published": "2026-10-22T09:11:15+00:00"
 },
 {
  "id": "eca5613cb195",
  "region": "jp",
  "source": "アニメージュプラス",
  "title": "『刃牙道』第17話 「守護（しゅご）り」あらすじ＆先行カット公開！",
  "snippet": "",
  "published": "2026-10-22T03:07:17+00:00"
 },
 {
  "id": "a50d89de13af",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "JRE MMAショー #187 ロバート・ウィテカー出演回｜The Joe Rogan Experience",
  "snippet": "",
  "published": "2026-10-22T11:31:34+00:00"
 },
 {
  "id": "740eb12b65c6",
  "region": "jp",
  "source": "Howl.link",
  "title": "無職柔術師範 (@mushokushihan) on X",
  "snippet": "",
  "published": "2026-10-22T08:51:29+00:00"
 },
 {
  "id": "7d1a2c16f192",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "「ONE SAMURAI 5」 の追加対戦カード4試合を発表！ONEストロー級総合格闘技 和田竜光 vs",
  "snippet": "",
  "published": "2026-10-21T17:51:22+00:00"
 },
 {
  "id": "8693b8b8b920",
  "region": "intl",
  "source": "Valley Roadrunner",
  "title": "Local does well in JIU Jitsu World League",
  "snippet": "",
  "published": "2026-10-22T14:40:28+00:00"
 },
 {
  "id": "94c2354da8ab",
  "region": "intl",
  "source": "The National",
  "title": "President Sheikh Mohamed congratulates jiu-jitsu team after Asian Games medal haul in Japan",
  "snippet": "",
  "published": "2026-10-22T16:56:24+00:00"
 },
 {
  "id": "447e483d6f17",
  "region": "intl",
  "source": "Orangeville Citizen |",
  "title": "Orangeville BJJ coach earns black belt, inspires young athletes",
  "snippet": "",
  "published": "2026-10-22T21:41:50+00:00"
 },
 {
  "id": "1794f00ae37f",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "UAE President receives UAE jiu-jitsu Asian Games medallists",
  "snippet": "",
  "published": "2026-10-22T14:24:49+00:00"
 },
 {
  "id": "a5b61f48bc83",
  "region": "intl",
  "source": "lovin.co",
  "title": "Abu Dhabi World Professional Jiu-Jitsu Championship Prepares For Its 18th Edition",
  "snippet": "",
  "published": "2026-10-22T11:11:50+00:00"
 },
 {
  "id": "991a4d97db1c",
  "region": "intl",
  "source": "boxingnews.com",
  "title": "Palhares Faces Galvao In ADCC Rematch With Strikes",
  "snippet": "",
  "published": "2026-10-22T23:30:45+00:00"
 },
 {
  "id": "86d445e12c18",
  "region": "intl",
  "source": "FloGrappling",
  "title": "PBJJF World Jiu-Jitsu Championships",
  "snippet": "",
  "published": "2026-10-22T04:30:43+00:00"
 },
 {
  "id": "9c36815dd944",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 World Jiu-Jitsu IBJJF Championship",
  "snippet": "",
  "published": "2026-10-21T17:00:00+00:00"
 },
 {
  "id": "fd4d44f139bc",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Marlon Tanaka Fagundes",
  "snippet": "",
  "published": "2026-10-22T06:59:12+00:00"
 },
 {
  "id": "d351d54edd8f",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Margot Ciccarelli",
  "snippet": "",
  "published": "2026-10-22T00:33:41+00:00"
 },
 {
  "id": "69810a0359ef",
  "region": "intl",
  "source": "The Bury Times",
  "title": "Whitefield's Sienna becomes European Thai boxing champion",
  "snippet": "",
  "published": "2026-10-22T06:19:00+00:00"
 },
 {
  "id": "2bc580c3dfe5",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Bella Mir Aims For Late-January MMA Return Amid RAF Schedule",
  "snippet": "",
  "published": "2026-10-22T15:15:40+00:00"
 },
 {
  "id": "c262aab7c13b",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Al Wahda Defends Jiu-Jitsu President’s Cup Title in Abu Dhabi",
  "snippet": "",
  "published": "2026-10-22T20:01:24+00:00"
 },
 {
  "id": "a5ece075e1c2",
  "region": "intl",
  "source": "BJJDOC",
  "title": "UFC 1 Participant Claims His Striking Made The UFC Popular, Not Royce Gracie’s Jiu-jitsu",
  "snippet": "",
  "published": "2026-10-22T12:59:33+00:00"
 },
 {
  "id": "e58d64061be7",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Texan Entrepreneur Explains What Makes Danaher And Gordon Ryan So Successful In JRE Appearance",
  "snippet": "",
  "published": "2026-10-22T12:09:42+00:00"
 },
 {
  "id": "4c90918b1f79",
  "region": "intl",
  "source": "TWSN",
  "title": "Mikey Musumeci’s MMA Hype: Pump the Breaks",
  "snippet": "",
  "published": "2026-10-22T13:00:00+00:00"
 },
 {
  "id": "b38ef7eb8f2d",
  "region": "intl",
  "source": "Menafn",
  "title": "Top Clubs Chase Jiu-Jitsu President's Cup Title In Abu Dhabi On Saturday",
  "snippet": "",
  "published": "2026-10-22T10:15:54+00:00"
 },
 {
  "id": "979293ba1bdf",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Jordan Burroughs Ranks MMA Wrestlers",
  "snippet": "",
  "published": "2026-10-22T14:36:25+00:00"
 },
 {
  "id": "d03b0b796b9a",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Joe Rogan: MMA Has Evolved More In 33 Years Than In The Previous 33,000",
  "snippet": "",
  "published": "2026-10-22T06:50:30+00:00"
 },
 {
  "id": "5cb07e85bbf5",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Palhares vs. Galvao, Gastelum vs. Vieira Announced For ACBJJ 23",
  "snippet": "",
  "published": "2026-10-22T00:39:55+00:00"
 },
 {
  "id": "9887e9b30f2a",
  "region": "intl",
  "source": "The Grueling Truth",
  "title": "Roger Costa: From Overcoming Bullying to Helping Others Find Confidence Through Brazilian Jiu-Jitsu",
  "snippet": "",
  "published": "2026-10-21T22:03:09+00:00"
 },
 {
  "id": "1d7d890cc479",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Dvalishvili Thinks There's 'No Point In Training With Musumeci' Despite Being At The Same Gym",
  "snippet": "",
  "published": "2026-10-22T08:50:02+00:00"
 },
 {
  "id": "e2e2bf9e4d15",
  "region": "intl",
  "source": "Howl.link",
  "title": "INFLUENCER MIKE HOLSTON FACES NEAR-FATAL ENCOUNTER WITH MASSIVE RETICULATED PYTHON IN INDONESIA",
  "snippet": "",
  "published": "2026-10-22T20:43:19+00:00"
 }
]
