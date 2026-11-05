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
  "id": "4c849a44d2a4",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "勝海舟と同じ剣術道場で学び、柔術・砲術にも通じた小栗上野介。2027年大河ドラマ『逆賊の幕臣』の主人公が、武芸を通じて海外情報も得ていた青年時代（婦人公論.jp）",
  "snippet": "",
  "published": "2026-11-04T03:30:38+00:00"
 },
 {
  "id": "c2c5f398a6b7",
  "region": "jp",
  "source": "YouTube",
  "title": "【ブラジリアン柔術ジム巡り Vol.1】静岡県沼津市「FAITHNINE柔術」を訪問！2店舗目オープンに向けて全国の道場を巡る！｜NOW or NEVER",
  "snippet": "",
  "published": "2026-11-04T02:21:47+00:00"
 },
 {
  "id": "710b4f736946",
  "region": "jp",
  "source": "BOUTREVIEW",
  "title": "パンクラス 11.8 ニューピア：菊入正行の相手、平信一に再変更。ボンサイ柔術 眞藤源太が緊急出場しブラジリアン・トップチームの選手と対戦",
  "snippet": "",
  "published": "2026-11-04T09:34:07+00:00"
 },
 {
  "id": "e359c0163e1a",
  "region": "jp",
  "source": "Howl.Link",
  "title": "【BJJ-WAVE】プロ柔術「ART.8」全試合 総括【ブラジリアン柔術】",
  "snippet": "",
  "published": "2026-11-03T17:18:55+00:00"
 },
 {
  "id": "a94965b14746",
  "region": "jp",
  "source": "Infoseek",
  "title": "「これは兄のために取り返してやる」――クリスチャン・リー、『インナー・サークル37』でのタイ・ルオトロに対する痛快なリベンジを狙う",
  "snippet": "",
  "published": "2026-11-03T22:15:56+00:00"
 },
 {
  "id": "7af3fa86a187",
  "region": "jp",
  "source": "Infoseek",
  "title": "「自分のペースを押し付けたい」――無敗のマゴメド・マゴメドフ、ONE Fight Night 49でのルーカス・ガブリエル戦での華々しいデビューを目指す",
  "snippet": "",
  "published": "2026-11-04T02:36:45+00:00"
 },
 {
  "id": "bf550f4f0f76",
  "region": "intl",
  "source": "New Orleans CityBusiness",
  "title": "New wrestling, jiu-jitsu academy opens in Metairie",
  "snippet": "",
  "published": "2026-11-04T20:30:48+00:00"
 },
 {
  "id": "aedef8b5d55b",
  "region": "intl",
  "source": "TheUnion.com",
  "title": "Cool, calm, and collected: Local jiu-jitsu academy helps students build confidence beyond the mat",
  "snippet": "",
  "published": "2026-11-04T11:00:00+00:00"
 },
 {
  "id": "4ab23cf42080",
  "region": "intl",
  "source": "StreetInsider",
  "title": "In HelloNation, Martial Arts Expert Wayne Marble Examines Brazilian Jiu-Jitsu for Real-World Self-Defense",
  "snippet": "",
  "published": "2026-11-04T18:00:33+00:00"
 },
 {
  "id": "3769c628b622",
  "region": "intl",
  "source": "Caribbean Today",
  "title": "Blackman Wins Gold at European Jiu-Jitsu Championships",
  "snippet": "",
  "published": "2026-11-04T15:06:03+00:00"
 },
 {
  "id": "5f8a8735c03b",
  "region": "intl",
  "source": "Los Altos Town Crier",
  "title": "Health tech CEO from Los Altos wins gold in jiu-jitsu",
  "snippet": "",
  "published": "2026-11-03T22:48:28+00:00"
 },
 {
  "id": "4a1148fff233",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship - Videos",
  "snippet": "",
  "published": "2026-11-04T00:27:04+00:00"
 },
 {
  "id": "905663bbeb96",
  "region": "intl",
  "source": "Star of Mysore",
  "title": "UoM Jiu-Jitsu Team bags 18 Medals",
  "snippet": "",
  "published": "2026-11-04T14:30:17+00:00"
 },
 {
  "id": "44a0c53c3aac",
  "region": "intl",
  "source": "مكتب أبوظبي الإعلامي",
  "title": "Under the patronage of Khaled bin Mohamed bin Zayed, 18th Abu Dhabi World Professional Jiu-Jitsu Championship to take place in November 2026",
  "snippet": "",
  "published": "2026-11-04T07:03:09+00:00"
 },
 {
  "id": "8d11c3998242",
  "region": "intl",
  "source": "Neos Kosmos",
  "title": "Teenage jiu-jitsu champion Mary Nomikos sets her sights on world titles",
  "snippet": "",
  "published": "2026-11-04T00:17:45+00:00"
 },
 {
  "id": "4661e945e7b4",
  "region": "intl",
  "source": "Bristol Live",
  "title": "Bristol 17-year-old crowned European Jiu-Jitsu Champion",
  "snippet": "",
  "published": "2026-11-04T09:55:00+00:00"
 },
 {
  "id": "1862b76763b1",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "BJJ Rankings Update – November 2026",
  "snippet": "",
  "published": "2026-11-04T13:49:29+00:00"
 },
 {
  "id": "f7b1c3681b51",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Xande Ribeiro Slams Attention Driven Economy In BJJ: Organizations Are Telling Athletes They Must Be Entertaining, This Is A Dangerous Approach",
  "snippet": "",
  "published": "2026-11-04T14:00:52+00:00"
 },
 {
  "id": "cbdc8443a241",
  "region": "intl",
  "source": "BJJDOC",
  "title": "BJJ Legend Xande Ribeiro: I Tried TRT For 4 Months, Didn’t Like It",
  "snippet": "",
  "published": "2026-11-04T12:57:54+00:00"
 },
 {
  "id": "5a84d09e8013",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "IBJJF No Gi European Championship 2026 Full Results And Highlights",
  "snippet": "",
  "published": "2026-11-04T11:39:29+00:00"
 },
 {
  "id": "8bc86c42a49c",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Japanese National IBJJF Jiu-Jitsu Championship 2026",
  "snippet": "",
  "published": "2026-11-04T19:31:58+00:00"
 },
 {
  "id": "a78144c18c6c",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Edson Barboza to Face Rashid Magomedov in ACBJJ Battle Match on November 13",
  "snippet": "",
  "published": "2026-11-03T23:54:01+00:00"
 },
 {
  "id": "761c82628785",
  "region": "intl",
  "source": "BJJEE",
  "title": "Five Finger Death Punch’s Zoltan Bathory Donates $100,000 To USA Judo",
  "snippet": "Zoltan Bathory – guitarist for Five Finger Death Punch, co-owner of the Professional Grappling Federation, and organiser of the Pro Judo tournament – has announced a $100,000 donation to USA Judo on World Judo Day. The money comes from proceeds of the band’s 2026 tour and is meant to support American athletes at the top of the sport, covering training camps, equipment and other essential costs. Bathory, who was born in Hungary, began judo at nine, when it was state-sponsored and free there, and says it shaped his life and career: I started judo at nine years old, and I still compete today. I k…",
  "published": "2026-11-04T12:12:42+00:00"
 },
 {
  "id": "fd22235afcd9",
  "region": "intl",
  "source": "BJJEE",
  "title": "Danaher Brown Belt Abraham La Montagne: “Most Black Belts Should Probably Be Blue Or Purple Belts”",
  "snippet": "Abraham La Montagne, a John Danaher brown belt, says Brazilian Jiu-Jitsu has advanced faster than its belt standards. On the Jits and Giggles podcast , he argued that most people wearing black belts should probably hold blue or purple instead. He started by comparing ranks to academic credentials: Nobody gets upset that they don’t have a PhD. I think you’re literally called a professor when you get a black belt, which is same as having a PhD or teaching at college. The bar, he said, should rise with the sport: Maybe back in the day, Helio Gracie time, you got a good half guard, maybe you’re a…",
  "published": "2026-11-04T11:47:34+00:00"
 }
]
