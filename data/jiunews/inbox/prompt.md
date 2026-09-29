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
  "id": "227a12b01d2a",
  "region": "jp",
  "source": "読売新聞",
  "title": "ノーギ柔術の世界選手権ベスト１６、中３がポーランドで熱戦…かえつ有明",
  "snippet": "",
  "published": "2026-09-28T20:00:00+00:00"
 },
 {
  "id": "8cafa214e720",
  "region": "jp",
  "source": "伊豆新聞デジタル",
  "title": "世界柔術で兄弟躍進 龍乃丞さん２冠、弟の樟乃丞さん銀―函南",
  "snippet": "",
  "published": "2026-09-28T18:00:15+00:00"
 },
 {
  "id": "eadc11d10b75",
  "region": "jp",
  "source": "静岡新聞DIGITAL",
  "title": "柔術 兄弟で世界 金・銀 函南の小川龍乃丞さん 樟乃丞さん 「格闘技王者に」「高みへ」",
  "snippet": "",
  "published": "2026-09-27T21:00:00+00:00"
 },
 {
  "id": "d985af89208d",
  "region": "jp",
  "source": "Chosunbiz",
  "title": "柔術韓国代表が再審申請で懲戒効力停止しアジア大会出場へ - CHOSUNBIZ",
  "snippet": "",
  "published": "2026-09-28T01:23:00+00:00"
 },
 {
  "id": "606e30875ce3",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "優しい顔のシロイルカから得た癒しを活力に、アジア大会への活躍を誓う 柔術・田中美佳",
  "snippet": "",
  "published": "2026-09-28T10:05:00+00:00"
 },
 {
  "id": "f413d7db1e3b",
  "region": "jp",
  "source": "Infoseek",
  "title": "ねずみ視点の最大4人マルチ対応、心温まるオープンワールドADV『Hela: ちいさなねずみと魔法の森』松竹ゲームズより日本展開決定！発売は12月1日",
  "snippet": "",
  "published": "2026-09-28T03:00:03+00:00"
 },
 {
  "id": "d2adaec40369",
  "region": "jp",
  "source": "게임메카",
  "title": "PvEマッチメイキング開始、『アーク・レイダーズ』「凍てついた山道」予告",
  "snippet": "",
  "published": "2026-09-28T08:55:31+00:00"
 },
 {
  "id": "a1b92cdc68a2",
  "region": "intl",
  "source": "KTOO",
  "title": "Tongass Voices: Double gold jiu-jitsu champion Becca Charbonneau of Juneau on consistency and community",
  "snippet": "",
  "published": "2026-09-28T22:17:16+00:00"
 },
 {
  "id": "55f024cef607",
  "region": "intl",
  "source": "Eyewitness News (WEHT/WTVW)",
  "title": "Illinois firefighters receive jiu-jitsu training for self-defense in the field",
  "snippet": "",
  "published": "2026-09-28T19:27:18+00:00"
 },
 {
  "id": "e036ecc60244",
  "region": "intl",
  "source": "KCAU 9 News",
  "title": "Siouxland Jiu Jitsu athletes traveling to France to compete",
  "snippet": "",
  "published": "2026-09-29T00:07:24+00:00"
 },
 {
  "id": "a4149f2d0b50",
  "region": "intl",
  "source": "citylifestyle.com",
  "title": "Jesus & Jiu Jitsu",
  "snippet": "",
  "published": "2026-09-28T07:47:20+00:00"
 },
 {
  "id": "e25edbdd8dab",
  "region": "intl",
  "source": "FloGrappling",
  "title": "FloGrappling Schedule: Events Streaming Sept. 28-Oct. 4",
  "snippet": "",
  "published": "2026-09-28T11:45:07+00:00"
 },
 {
  "id": "70c42630138b",
  "region": "intl",
  "source": "Search Engine Roundtable",
  "title": "Google Jiu-Jitsu Rolling Shirt",
  "snippet": "",
  "published": "2026-09-28T11:00:00+00:00"
 },
 {
  "id": "938340c1bd6d",
  "region": "intl",
  "source": "mymmanews.com",
  "title": "Bryce Mitchell vs. Mikey Musumeci headlines UFC BJJ 11",
  "snippet": "",
  "published": "2026-09-28T05:10:52+00:00"
 },
 {
  "id": "97de9f5f5955",
  "region": "intl",
  "source": "Chron",
  "title": "Meet the gym leader teaching LGBTQ+ Houstonians how to protect themselves",
  "snippet": "",
  "published": "2026-09-28T00:10:16+00:00"
 },
 {
  "id": "b9f57032bc9c",
  "region": "intl",
  "source": "The Meaford Independent",
  "title": "Georgian Bay Brazilian Jiu-Jitsu Members Compete in Brampton",
  "snippet": "",
  "published": "2026-09-28T13:40:42+00:00"
 },
 {
  "id": "578406cdbbad",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan Kids Jiu-Jitsu IBJJF Championship",
  "snippet": "",
  "published": "2026-09-28T02:36:18+00:00"
 },
 {
  "id": "ae35d2079d24",
  "region": "intl",
  "source": "Chosunbiz",
  "title": "Jiu-jitsu athletes file appeal, win stay to compete at Asian Games in Korea - CHOSUNBIZ",
  "snippet": "",
  "published": "2026-09-28T01:23:00+00:00"
 },
 {
  "id": "1a896fb88581",
  "region": "intl",
  "source": "The Bugle app",
  "title": "Gracie Barra Jiu-Jitsu school taking Kiama to the mat",
  "snippet": "",
  "published": "2026-09-28T06:24:49+00:00"
 },
 {
  "id": "6a1d88db5d0a",
  "region": "intl",
  "source": "oxfordtimes.co.uk",
  "title": "Architect strikes gold at first ever national martial arts contest",
  "snippet": "",
  "published": "2026-09-27T15:00:00+00:00"
 },
 {
  "id": "b7ad70f64a9b",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 World Jiu-Jitsu IBJJF Championship",
  "snippet": "",
  "published": "2026-09-27T14:58:37+00:00"
 },
 {
  "id": "d86c783204b6",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Polaris 37",
  "snippet": "",
  "published": "2026-09-28T05:49:50+00:00"
 },
 {
  "id": "aee81f41d447",
  "region": "intl",
  "source": "Cairns Local News",
  "title": "Gold medals for Girren lads",
  "snippet": "",
  "published": "2026-09-28T01:00:00+00:00"
 },
 {
  "id": "05d791e6ccda",
  "region": "intl",
  "source": "Estero Bay News",
  "title": "New Martial Arts Studio Opens in MB",
  "snippet": "",
  "published": "2026-09-28T18:23:09+00:00"
 },
 {
  "id": "d0bb1815799a",
  "region": "intl",
  "source": "Yahoo News Singapore",
  "title": "Tom Brady Was Reportedly 'Blindsided' By Gisele Bündchen Divorce After 'Cheating' Rumors With Her Jiu Jitsu Instructor, Biographer Reveals: 'Something Very Bad' Happened",
  "snippet": "",
  "published": "2026-09-28T13:00:11+00:00"
 },
 {
  "id": "d24f928642b1",
  "region": "intl",
  "source": "Fightomic",
  "title": "Luis Hernandez: UFC Record, Stats and Bio of The Stache",
  "snippet": "",
  "published": "2026-09-27T15:24:59+00:00"
 },
 {
  "id": "f5a85f14863c",
  "region": "intl",
  "source": "BJJDOC",
  "title": "BJJ Legend Chris Haueter Cautions Students To Leave Controlling/Toxic BJJ Academies Which Dictate What Students Can Wear Or Teach",
  "snippet": "",
  "published": "2026-09-28T08:47:12+00:00"
 },
 {
  "id": "f26f9239c4df",
  "region": "intl",
  "source": "BJJDOC",
  "title": "UFC BJJ Open Called Out For Inept Handling Of Slams",
  "snippet": "",
  "published": "2026-09-28T10:18:21+00:00"
 },
 {
  "id": "d04aca399fd6",
  "region": "intl",
  "source": "Shredder News",
  "title": "UFC Legend Royce Gracie Reveals Vans Is Entering the Jiu Jitsu and MMA Game",
  "snippet": "",
  "published": "2026-09-28T16:16:25+00:00"
 }
]
