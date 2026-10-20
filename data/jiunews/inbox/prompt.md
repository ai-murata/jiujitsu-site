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
  "id": "6275730d8d84",
  "region": "jp",
  "source": "Unisba Media",
  "title": "【柔術女子48kg級】日本柔術“初”のアジア大会 関節技に屈す【アジア大会】｜トヨタイムズスポーツ Marshals (VoNqFxkoKF)",
  "snippet": "",
  "published": "2026-10-19T07:00:56+00:00"
 },
 {
  "id": "6ac3a4acf15b",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【ONE】『ONE SAMURAI 4』のパフォーマンスボーナス合計金額は「4500万円」吉成名高、ハガティー、阿部光太ら8名が獲得",
  "snippet": "",
  "published": "2026-10-19T08:10:00+00:00"
 },
 {
  "id": "6d4083fa9626",
  "region": "jp",
  "source": "Infoseek",
  "title": "敗戦のガリットチュウ福島「49歳になって、こんなに悔しい思いをするとは…」",
  "snippet": "",
  "published": "2026-10-19T02:17:00+00:00"
 },
 {
  "id": "c7259689945a",
  "region": "jp",
  "source": "YouTube",
  "title": "太田忍vs鹿志村仁之介 試合展開予想",
  "snippet": "",
  "published": "2026-10-18T15:30:41+00:00"
 },
 {
  "id": "a9462cca460e",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "《ブラジル》商議所＝伝説の柔道家・前田光世の半生描く＝大友啓史監督『コンデコマ』始動＝日伯米合作のアクション超大作",
  "snippet": "",
  "published": "2026-10-19T22:07:10+00:00"
 },
 {
  "id": "d9893c724213",
  "region": "jp",
  "source": "매일경제",
  "title": "「ビッグガイ」梁丹謙（ヤン·ダンギョム、改名前のヤン·ヘジュン、38）は2006年第31回KBS杯全国レスリング大会自由形120㎏銀メダリストだ。 2008年の総合格闘技(MMA)転向後、翌年の第2回..",
  "snippet": "",
  "published": "2026-10-19T02:00:00+00:00"
 },
 {
  "id": "fcaddab19698",
  "region": "jp",
  "source": "efight.jp",
  "title": "『PANCRASE 368』",
  "snippet": "",
  "published": "2026-10-19T15:18:29+00:00"
 },
 {
  "id": "dcec2b92d0d3",
  "region": "jp",
  "source": "Howl.link",
  "title": "Rangel Yamaguchi Rodrigues on Instagram: \"デラヒーバスイープからのサイドコントロール\"",
  "snippet": "",
  "published": "2026-10-19T14:20:25+00:00"
 },
 {
  "id": "2d38b90341a3",
  "region": "jp",
  "source": "4Gamer.net",
  "title": "画像ギャラリー No.002 | 猫の探検家がドリルを使って地下を掘り進み，グラップリングフックを放って宝物を回収する。インクリメンタル「ねこねこ採掘会社」，体験版配信中",
  "snippet": "",
  "published": "2026-10-19T11:35:23+00:00"
 },
 {
  "id": "9b1c6f0c2c1b",
  "region": "jp",
  "source": "AGARA 紀伊民報",
  "title": "砂浜のリングで熱戦 格闘技とプロレス大会 和歌山・白浜",
  "snippet": "",
  "published": "2026-10-19T05:30:00+00:00"
 },
 {
  "id": "decfbd362b9a",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "“圧倒的に好評”デモ版のメトロイドヴァニア『Iron Bramble』ユーザー要望に応えたデモ版の最終アップデート配信―これからは製品版の開発に注力",
  "snippet": "",
  "published": "2026-10-19T16:00:00+00:00"
 },
 {
  "id": "8174d6228dc7",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【Lemino修斗】死闘、野瀬翔平が齋藤奨司に3R TKO勝ちでバンタム級T優勝！ シモンスズキが山内渉の蹴りを崩してRNC！ パク・チウが倉本にスプリット判定勝ち、吉野光が...",
  "snippet": "",
  "published": "2026-10-19T08:10:00+00:00"
 },
 {
  "id": "2d461fcec207",
  "region": "jp",
  "source": "4Gamer.net",
  "title": "猫の探検家がドリルを使って地下を掘り進み，グラップリングフックを放って宝物を回収する。インクリメンタル「ねこねこ採掘会社」，体験版配信中",
  "snippet": "",
  "published": "2026-10-19T07:37:28+00:00"
 },
 {
  "id": "081bba7b26c5",
  "region": "intl",
  "source": "Community Impact",
  "title": "Momo Brazilian Jiu-Jitsu offers classes, athlete development in Frisco",
  "snippet": "",
  "published": "2026-10-19T19:49:01+00:00"
 },
 {
  "id": "269851a37fb6",
  "region": "intl",
  "source": "Big Rapids Pioneer",
  "title": "New Big Rapids jiu-jitsu academy welcomes all skill levels",
  "snippet": "",
  "published": "2026-10-19T17:04:58+00:00"
 },
 {
  "id": "fdfd97a401dc",
  "region": "intl",
  "source": "FloGrappling",
  "title": "How to Watch: Majestic BJJ Challenge 7 | Grappling",
  "snippet": "",
  "published": "2026-10-19T17:37:52+00:00"
 },
 {
  "id": "52962c8551e5",
  "region": "intl",
  "source": "GilaValleyCentral",
  "title": "Safford’s Onyx BJJ wins team championship at Southwest Classic",
  "snippet": "",
  "published": "2026-10-19T19:11:34+00:00"
 },
 {
  "id": "caa66ac42de9",
  "region": "intl",
  "source": "Sharjah24",
  "title": "Al Hamriyah Jiu-Jitsu wins 16 medals at Championship Finale",
  "snippet": "",
  "published": "2026-10-19T14:54:29+00:00"
 },
 {
  "id": "136e1c1c3239",
  "region": "intl",
  "source": "InYourArea",
  "title": "3 Derbyshire brothers win Jiu-Jitsu gold in Portugal",
  "snippet": "",
  "published": "2026-10-19T18:25:24+00:00"
 },
 {
  "id": "7a5285648992",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "Baniyas, Sharjah Self-Defence retain season titles as Khaled bin Mohamed bin Zayed Jiu-Jitsu Championship concludes",
  "snippet": "",
  "published": "2026-10-19T16:08:26+00:00"
 },
 {
  "id": "d998ebd56487",
  "region": "intl",
  "source": "Demócrata",
  "title": "Mallorca BJJ & Yoga Festival 2026 grows by 8% in registrations for its autumn edition",
  "snippet": "",
  "published": "2026-10-19T14:44:46+00:00"
 },
 {
  "id": "59a6b9d56d4b",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Albert Tapia",
  "snippet": "",
  "published": "2026-10-19T02:58:55+00:00"
 },
 {
  "id": "eee6b360cc27",
  "region": "intl",
  "source": "Men's Fitness",
  "title": "Inside Lawrence Jones's 4 A.M. Fitness Routine: How the FOX & Friends Host Trains, Eats, and Recovers",
  "snippet": "",
  "published": "2026-10-19T13:00:00+00:00"
 },
 {
  "id": "0072a99ddc7f",
  "region": "intl",
  "source": "Demokratis.co.id",
  "title": "Charles Oliveira Targets Lightweight Title After UFC 335",
  "snippet": "",
  "published": "2026-10-19T18:57:00+00:00"
 },
 {
  "id": "057794f04c6d",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Baniyas, Sharjah Win 2026 UAE Jiu-Jitsu Titles",
  "snippet": "",
  "published": "2026-10-19T19:36:24+00:00"
 },
 {
  "id": "6ff07647da75",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Andy Murasaki Set For IBJJF Crown Defense Following AOJ Switch",
  "snippet": "",
  "published": "2026-10-19T09:00:42+00:00"
 },
 {
  "id": "ce42732dc00c",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Erich Munis Returns For Fourth Straight IBJJF Crown Title Bid",
  "snippet": "",
  "published": "2026-10-19T09:00:43+00:00"
 },
 {
  "id": "424c292f6007",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Gabi Pessanha Confirmed For IBJJF Crown Title Defense On November 8",
  "snippet": "",
  "published": "2026-10-19T09:00:42+00:00"
 },
 {
  "id": "f3409fd2c6b7",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Rerisson Gabriel Joins IBJJF Crown Featherweight Field",
  "snippet": "",
  "published": "2026-10-19T04:45:35+00:00"
 },
 {
  "id": "98e828870d6d",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Colby Covington Leads RAF Men’s Crossover Rankings",
  "snippet": "",
  "published": "2026-10-19T16:04:11+00:00"
 },
 {
  "id": "7db392f1a19f",
  "region": "intl",
  "source": "BJJDOC",
  "title": "\"Rickson Gracie Would Crush Me\" - Megaton Dias On Technical Difference With Rickson Gracie",
  "snippet": "",
  "published": "2026-10-19T09:10:37+00:00"
 },
 {
  "id": "fa55a1583041",
  "region": "intl",
  "source": "BJJEE",
  "title": "Ryan Hall Says Jiu-Jitsu Is ‘A Philosophy’: “Real Life Aikido”",
  "snippet": "Asked by Lex Fridman to explain the essence of Jiu-Jitsu to someone who has never stepped on a mat, Ryan Hall skipped techniques, submissions and belt ranks… And described a philosophy that joins physical ability with mental development: I think that Jiu-Jitsu is a philosophy that’s expressed physically… The kind of development of mental capacity and physical capacity working in unison, to move efficiently and almost flowingly, unresistantly, with a given situation, with a physically resisting opponent… Learning how to generate force on your own and how to steal force from the floor, how to st…",
  "published": "2026-10-19T14:24:29+00:00"
 },
 {
  "id": "58766a1ae719",
  "region": "intl",
  "source": "BJJEE",
  "title": "Bernardo Faria: “World Champions Can Make Poor Instructors…”",
  "snippet": "World champion black belt Bernardo Faria says a world title does not make someone a good instructor. He has a close view of the question as the force behind BJJ Fanatics, which carries more than 3,000 instructional videos from over 1,200 instructors. His core argument is that elite performers often operate on instinct: Many times with the world champion, sometimes they don’t know what they do. They just do it… So that doesn’t translate so well for education, right? At the end of the day, the one who sells the most is the one who can articulate concepts in the best way. When BJJ Fanatics launch…",
  "published": "2026-10-19T14:15:44+00:00"
 }
]
