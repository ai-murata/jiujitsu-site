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
  "id": "448d5f4df3b4",
  "region": "jp",
  "source": "山陽新聞",
  "title": "ガリットチュウ福島『ONE』緊急参戦 “朝倉未来の柔術コーチ”竹浦正起とグラップリングマッチ",
  "snippet": "",
  "published": "2026-10-09T20:08:31+00:00"
 },
 {
  "id": "658292e015cc",
  "region": "jp",
  "source": "四国新聞",
  "title": "柔術全国大会Ｖ、市長に喜び報告 坂出・道場所属の前田選手｜四国新聞WEB朝刊",
  "snippet": "",
  "published": "2026-10-09T19:03:30+00:00"
 },
 {
  "id": "10508e6a2469",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "「ガリットチュウ」福島、「ＯＮＥ ＳＡＭＵＲＡＩ ４」参戦「とんでもないオファーが来たなと思っております…」１０・１７有明アリーナ",
  "snippet": "",
  "published": "2026-10-09T07:08:00+00:00"
 },
 {
  "id": "ac1936cd05ab",
  "region": "jp",
  "source": "シネマトゥデイ",
  "title": "どこよりも遠い場所にいる君へ (2026)：予告編・動画",
  "snippet": "",
  "published": "2026-10-09T16:58:50+00:00"
 },
 {
  "id": "267ab7084637",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "パーキンソン病に苦しみ…〝400戦無敗の男〟ヒクソン・グレイシー、66歳の稽古姿に「病気に立ち向かう姿すらも神々しい」「これこそが柔術の真髄」の声（西スポWEB OTTO!）",
  "snippet": "",
  "published": "2026-10-08T20:20:08+00:00"
 },
 {
  "id": "dc0eed958335",
  "region": "jp",
  "source": "UFC.com",
  "title": "Landon Elmore Bowl Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-09T01:00:00+00:00"
 },
 {
  "id": "e57c2ab828b7",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "湘南里川づくりみんなの会 国交省大臣表彰を受賞 河川の保全などに功績〈伊勢原市〉",
  "snippet": "",
  "published": "2026-10-09T08:00:00+00:00"
 },
 {
  "id": "b19865d04478",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "伊勢原市社協 ボランティア募集 みかん狩りの運営補助〈伊勢原市〉",
  "snippet": "",
  "published": "2026-10-08T22:00:00+00:00"
 },
 {
  "id": "947e0d73edf2",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "トイカツ道場、秋の入会キャンペーンを開催！入会にかかる費用・初月月謝など合計28,800円が無料に",
  "snippet": "",
  "published": "2026-10-08T15:45:25+00:00"
 },
 {
  "id": "4eed6736a789",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "観月ありさ、家政婦・志麻さんの古民家にほれぼれ「夢の生活って感じですよね」 玉木宏は伝統の職人技に挑む＜沸騰ワード10",
  "snippet": "",
  "published": "2026-10-09T06:36:06+00:00"
 },
 {
  "id": "4a1981206553",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "虹咲カリナ 2ndイメージDVD、動画配信サービス「アイドル・オン・デマンド」にて4K高画質で独占先行配信開始",
  "snippet": "",
  "published": "2026-10-09T06:09:17+00:00"
 },
 {
  "id": "db562d4d7f94",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "テクノロジーでパラスポーツ観戦をさらに楽しく！～AI実況を初導入！ユニバーサルコミュニケーション（UC）技術を活用し",
  "snippet": "",
  "published": "2026-10-08T17:30:31+00:00"
 },
 {
  "id": "b84eed26362c",
  "region": "jp",
  "source": "Howl.Link",
  "title": "柔術ナビ｜JIU-JITSU NAVI (@jiujitsunavi) on X",
  "snippet": "",
  "published": "2026-10-09T13:09:41+00:00"
 },
 {
  "id": "032350aeb8fe",
  "region": "jp",
  "source": "AERA DIGITAL",
  "title": "「ONE SAMURAI 4」 追加対戦カードを発表！ONEライト級サブミッショングラップリング 福島善成 vs 竹浦正起",
  "snippet": "",
  "published": "2026-10-09T16:57:47+00:00"
 },
 {
  "id": "0562070feb76",
  "region": "jp",
  "source": "Infoseek",
  "title": "【RIZIN】11・８千葉大会チケット販売開始、王者・神龍誠VSララミーフライ級王座戦など",
  "snippet": "",
  "published": "2026-10-09T15:14:12+00:00"
 },
 {
  "id": "c4d13cb56f17",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "11月8日（日）開催『abc presents RIZIN.55』を「ABEMA",
  "snippet": "",
  "published": "2026-10-09T11:48:32+00:00"
 },
 {
  "id": "a39db179c5fa",
  "region": "jp",
  "source": "Howl.Link",
  "title": "にこやかざんぱん🦀 (@ZANPAN_KING) on X",
  "snippet": "",
  "published": "2026-10-09T03:22:01+00:00"
 },
 {
  "id": "5d4978d21d56",
  "region": "intl",
  "source": "MMA Fighting",
  "title": "Mikey Musumeci vacates UFC BJJ title to ‘prioritize my training for MMA’",
  "snippet": "",
  "published": "2026-10-09T21:00:00+00:00"
 },
 {
  "id": "41f514f7a6ce",
  "region": "intl",
  "source": "MMA Mania",
  "title": "Mikey Musumeci drops UFC BJJ title to ‘prioritize’ MMA, ends serious jiu-jitsu career",
  "snippet": "",
  "published": "2026-10-09T10:00:00+00:00"
 },
 {
  "id": "9571ada5fba1",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "Mikey Musumeci relinquishes his UFC BJJ belt to prioritise his training for MMA",
  "snippet": "",
  "published": "2026-10-10T00:14:20+00:00"
 },
 {
  "id": "0974c3601884",
  "region": "intl",
  "source": "WFIW",
  "title": "ELEVATION JIU JITSU TO HOLD GRAND OPENING AND RIBBON CUTTING",
  "snippet": "",
  "published": "2026-10-09T17:06:09+00:00"
 },
 {
  "id": "7fa2ce958f5c",
  "region": "intl",
  "source": "FightNews",
  "title": "Boxing News: Results From UFC BJJ 12 In Las Vegas, Nevada » October 9, 2026",
  "snippet": "",
  "published": "2026-10-09T13:53:52+00:00"
 },
 {
  "id": "ced76fe8f5f1",
  "region": "intl",
  "source": "Royal Gazette | Bermuda",
  "title": "Jiu-jitsu fighters scoop medals in New Jersey",
  "snippet": "",
  "published": "2026-10-09T13:05:03+00:00"
 },
 {
  "id": "2a13e0bebe4d",
  "region": "intl",
  "source": "Bloody Elbow",
  "title": "Ex-UFC title challenger grimaces in pain as he taps out to a nasty heel hook in BJJ match",
  "snippet": "",
  "published": "2026-10-09T12:00:00+00:00"
 },
 {
  "id": "47cb03e8588d",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "UFC BJJ Women's Flyweight Title Ends in Controversial Decision",
  "snippet": "",
  "published": "2026-10-09T23:59:21+00:00"
 },
 {
  "id": "57a936e0cf54",
  "region": "intl",
  "source": "MMA Fighting",
  "title": "Watch Gabriel Almeida tap out Gilbert Burns at UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-09T13:31:58+00:00"
 },
 {
  "id": "c781fd5ae597",
  "region": "intl",
  "source": "UFC.com",
  "title": "Cassia Moura Bowl Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-09T03:00:55+00:00"
 },
 {
  "id": "1a67c839ca75",
  "region": "intl",
  "source": "UFC.com",
  "title": "Gabriel Almeida Bowl Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-09T01:45:22+00:00"
 },
 {
  "id": "14ebd5853b58",
  "region": "intl",
  "source": "UFC.com",
  "title": "Thaynara Victoria Bowl Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-09T01:30:41+00:00"
 },
 {
  "id": "d92eb06eccfe",
  "region": "intl",
  "source": "UFC.com",
  "title": "Kade Anastasios Bowl Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-09T01:00:00+00:00"
 },
 {
  "id": "b93625cb08d6",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 World Master IBJJF Jiu-Jitsu Championship - Videos",
  "snippet": "",
  "published": "2026-10-09T06:02:18+00:00"
 },
 {
  "id": "74325708c56f",
  "region": "intl",
  "source": "MMA Mania",
  "title": "Controversy! Cassia Moura survives Fornarino, becomes first UFC BJJ double champ; Burns submitted",
  "snippet": "",
  "published": "2026-10-09T04:04:00+00:00"
 },
 {
  "id": "62a31d00cecf",
  "region": "intl",
  "source": "UFC.com",
  "title": "Renato Canuto Bowl Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-08T17:36:02+00:00"
 },
 {
  "id": "80875dcaefc6",
  "region": "intl",
  "source": "UFC.com.br",
  "title": "UFC BJJ 12: Moura vs Fornarino Results",
  "snippet": "",
  "published": "2026-10-09T00:54:56+00:00"
 },
 {
  "id": "ca0c262c0017",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - M/W",
  "snippet": "",
  "published": "2026-10-08T20:35:55+00:00"
 },
 {
  "id": "9ec4ec14b92f",
  "region": "intl",
  "source": "Turkmenportal.com",
  "title": "Turkmen athletes won 16 medals at the World Jiu-Jitsu Championships in Antalya",
  "snippet": "",
  "published": "2026-10-08T14:43:16+00:00"
 },
 {
  "id": "17a8c525424c",
  "region": "intl",
  "source": "The Body Lock",
  "title": "Gilbert Burns Taps Out to Brutal Heel Hook in Second UFC BJJ Match",
  "snippet": "",
  "published": "2026-10-09T19:01:18+00:00"
 },
 {
  "id": "f05cc6d2af3d",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Gabriel Almeida Submits Gilbert Burns With First-Round Heel Hook At UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-09T12:56:28+00:00"
 },
 {
  "id": "c6f865af9622",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Mikey Musumeci Vacates UFC BJJ Belt, Moving On to MMA",
  "snippet": "",
  "published": "2026-10-09T09:59:00+00:00"
 },
 {
  "id": "4435ad85b213",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Examining the Diminishing Effect of Competing at UFC BJJ",
  "snippet": "",
  "published": "2026-10-09T10:26:12+00:00"
 },
 {
  "id": "a892f36f0ea8",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Flograppling GM Breaks Down Why UFC BJJ is Losing Money: What was worth $100,000 to pay Gordon Ryan is literally worth $400 to pay you",
  "snippet": "",
  "published": "2026-10-09T09:44:21+00:00"
 },
 {
  "id": "f93680ccea90",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Craig Jones Calls Out UFC BJJ Ref After Adele Fornarino Gets Eyepoked and Robbed on the Scorecards",
  "snippet": "",
  "published": "2026-10-09T09:10:41+00:00"
 },
 {
  "id": "c71138d78e1e",
  "region": "intl",
  "source": "BJJEE",
  "title": "Joe Rogan Renews Deal With Spotify With A $250 Million Contract",
  "snippet": "Spotify has secured a new multiyear agreement with Joe Rogan, keeping licensing rights and advertising sales for The Joe Rogan Experience. People familiar with the matter say the terms resemble the previous contract, which included an earnout estimated at $250 million. Rogan said the relationship suits him: The partnership with Spotify has been an amazing fit, and they’re incredible to work with. I’m extremely happy and excited to continue with them for years to come. The show’s reach supports the deal. Edison Research has ranked it No. 1 U.S. podcast every year since 2019, and it counts more…",
  "published": "2026-10-09T16:07:31+00:00"
 },
 {
  "id": "3a0ff6d6d885",
  "region": "intl",
  "source": "BJJEE",
  "title": "UFC Veteran & BJJ Black Belt Tim Kennedy Reportedly Wounded In Ambush In Congo",
  "snippet": "Former UFC fighter and U.S. Army Green Beret Tim Kennedy has reportedly been wounded in an ambush in the Democratic Republic of the Congo. A former New Zealand SAS member who was with him did not survive, as reported by MMA Weekly . Kennedy is a decorated Army sniper and special forces operator who served in Iraq and Afghanistan. According to reports, he was part of a three-man element that came under fire in Central Africa on September 17. He took multiple gunshot wounds, including three to the leg. The squad’s evacuation allegedly lasted close to eight hours. Kennedy was then medevaced to th…",
  "published": "2026-10-09T15:59:41+00:00"
 }
]
