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
  "id": "6b58d7e710bc",
  "region": "jp",
  "source": "WEBザテレビジョン",
  "title": "画像・写真 ＜刃牙道＞素手の格闘では持ち味を出せずにいた実戦柔術の使い手・本部以蔵が大舞台に臨む…第17話あらすじ＆先行カット公開(1/7)",
  "snippet": "",
  "published": "2026-10-25T21:59:48+00:00"
 },
 {
  "id": "5efd45c3f0eb",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "【熱狂LIVE】金・銀・銅メダリスト生出演！ハートに残るアジアパラ",
  "snippet": "",
  "published": "2026-10-24T13:30:33+00:00"
 },
 {
  "id": "1e0dd4af8502",
  "region": "intl",
  "source": "Arab Times Kuwait News",
  "title": "Al-Hatem claims gold at AJP Qatar Jiu-Jitsu Championship",
  "snippet": "",
  "published": "2026-10-25T17:07:28+00:00"
 },
 {
  "id": "6579b624763c",
  "region": "intl",
  "source": "برق الإمارات",
  "title": "UAE adds three jiu-jitsu medals at Asian Games Aichi-Nagoya 2026, tally rises to eight",
  "snippet": "",
  "published": "2026-10-25T09:36:13+00:00"
 },
 {
  "id": "52eeb54d56c1",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Continue Watching",
  "snippet": "",
  "published": "2026-10-24T15:31:43+00:00"
 },
 {
  "id": "de36eef6613d",
  "region": "intl",
  "source": "The Wausonian",
  "title": "Rising Son martial arts gym moves from Wausau to Rothschild in major expansion",
  "snippet": "",
  "published": "2026-10-25T10:45:33+00:00"
 },
 {
  "id": "c9fb2ccfd746",
  "region": "intl",
  "source": "白鲸出海",
  "title": "dante leon",
  "snippet": "",
  "published": "2026-10-25T15:52:52+00:00"
 },
 {
  "id": "c20dc932b935",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Daniel Jin vs Kanoa Brown 2026 ADCC Vancouver Open",
  "snippet": "",
  "published": "2026-10-24T22:57:22+00:00"
 },
 {
  "id": "0e20408d8be3",
  "region": "intl",
  "source": "TMZ",
  "title": "Tom Brady & Candice Swanepoel Dating: Reports",
  "snippet": "",
  "published": "2026-10-25T21:05:49+00:00"
 },
 {
  "id": "58598df01ac5",
  "region": "intl",
  "source": "BJJDOC",
  "title": "John Danaher Talks Joslyn Molina Becoming The Youngest ADCC Competitor & Medalist Ever",
  "snippet": "",
  "published": "2026-10-25T19:53:46+00:00"
 },
 {
  "id": "ccba0b556c62",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Jozef Chen Won ADCC Bronze With A Completely Ruptured Knee Ligament",
  "snippet": "",
  "published": "2026-10-25T22:04:06+00:00"
 },
 {
  "id": "b5f296db3e68",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Rafael Lovato Jr Cautions Against Gym Switching: Bounce Around Couple Times And You Don't Have a Family Any More",
  "snippet": "",
  "published": "2026-10-25T09:06:04+00:00"
 },
 {
  "id": "5158e0e72b91",
  "region": "intl",
  "source": "BJJDOC",
  "title": "WATCH: Abus Magomedov Finishes UFC 333 Opponent With Rarely Seen Prayer Choke",
  "snippet": "",
  "published": "2026-10-25T11:12:09+00:00"
 },
 {
  "id": "ef2904912ae2",
  "region": "intl",
  "source": "UrduPoint",
  "title": "UAE Ministry Of Interior Trains 30 Latin American Peacekeepers In Argentina",
  "snippet": "",
  "published": "2026-10-24T13:00:15+00:00"
 },
 {
  "id": "0d9369a4932e",
  "region": "intl",
  "source": "BJJEE",
  "title": "(WATCH) Arman Tsarukyan Beats Dillon Danis At RAF 14 – Then Steps On Him",
  "snippet": "Arman Tsarukyan came close to setting off another brawl with Dillon Danis after a dominant win in the RAF 14 main event on Friday night… As he ended the match by technical superiority, then stepped on Danis as he got to his feet. But the security was on high alert after the pre-event press conference the day before, where Tsarukyan attacked Danis. The match itself was one-sided. Tsarukyan appeared to slap Danis to open and scored with a push out, drawing a quick warning from the referee. He added a takedown for two, then another step out to go up four. A further takedown set off a fast run of…",
  "published": "2026-10-25T21:36:10+00:00"
 },
 {
  "id": "64f1e69a9c50",
  "region": "intl",
  "source": "BJJEE",
  "title": "Merab Dvalishvili Won’t Train With Mikey Musumeci: “There Is No Point”",
  "snippet": "UFC bantamweight contender Merab Dvalishvili says he refuses to roll with Mikey Musumeci – even though they train at the same gym. Dvalishvili said the decision came after he heard how Musumeci was finishing top names: Mikey submitted Aljo [Aljamain Sterling] and I was surprised because it’s so hard to submit Aljo… Aljo usually never taps but I guess he has this leg lock game. You also told me, Demetrious, that Mikey submitted you. That time I make a decision, no I’m not going to train with him, because (it) doesn’t make sense. His objection is about what he would gain for MMA: There is no poi…",
  "published": "2026-10-24T21:29:03+00:00"
 }
]
