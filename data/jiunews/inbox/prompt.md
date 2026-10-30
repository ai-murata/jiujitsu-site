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
  "id": "17841ef3357b",
  "region": "jp",
  "source": "UFC.com",
  "title": "Tristan Sainz Bowl Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-30T00:34:44+00:00"
 },
 {
  "id": "8c471a164add",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "茨城県龍ケ崎市で王者を決める格闘技の祭典！「マッハ祭り 龍王杯」11月21日（土）ニューライフアリーナにて開催決定",
  "snippet": "",
  "published": "2026-10-29T11:06:32+00:00"
 },
 {
  "id": "fca76f8fd646",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "フエ市のスポーツ代表団は、第10回全国スポーツ大会に出場する準備ができています。",
  "snippet": "",
  "published": "2026-10-29T05:28:17+00:00"
 },
 {
  "id": "77944923adbc",
  "region": "jp",
  "source": "愛媛新聞",
  "title": "朝クラスが11月からスタートします",
  "snippet": "",
  "published": "2026-10-29T00:09:28+00:00"
 },
 {
  "id": "9b0f208e817a",
  "region": "jp",
  "source": "YouTube",
  "title": "【RIZIN 55】鶴屋さんイチオシの井上舜矢選手、ついにデビュー！",
  "snippet": "",
  "published": "2026-10-29T12:32:20+00:00"
 },
 {
  "id": "b9df83e3fd5a",
  "region": "intl",
  "source": "WFTV",
  "title": "Davenport jiu-jitsu community brings together beginners, families and a 61-year-old black belt",
  "snippet": "",
  "published": "2026-10-29T19:47:10+00:00"
 },
 {
  "id": "225980624de9",
  "region": "intl",
  "source": "Laredo Morning Times",
  "title": "Alberto Gonzalez captures jiu-jitsu title in unexpected run",
  "snippet": "",
  "published": "2026-10-29T20:19:47+00:00"
 },
 {
  "id": "3fda1a95288b",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "UFC BJJ 13 Live Results: Two Vacant Belts are Up for Grabs",
  "snippet": "",
  "published": "2026-10-29T22:53:11+00:00"
 },
 {
  "id": "888084ab2fe9",
  "region": "intl",
  "source": "MyMMANews",
  "title": "Brian DeMuro, MMA fighter and Jiu Jitsu instructor, shot dead by brother according to police report",
  "snippet": "",
  "published": "2026-10-30T00:18:34+00:00"
 },
 {
  "id": "49859d589c6e",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 13 Results",
  "snippet": "",
  "published": "2026-10-29T18:55:54+00:00"
 },
 {
  "id": "1e7c5a8096de",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Danijel Komljenovic vs Nicolas Gabriel Guy Lavende 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-10-29T14:39:22+00:00"
 },
 {
  "id": "58c916878a3a",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Timothy Vincent O'Keeffe vs Matteo Marino 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-10-29T16:13:27+00:00"
 },
 {
  "id": "9137a68d0db6",
  "region": "intl",
  "source": "Kayo Sports",
  "title": "UFC BJJ 13: Tackett v Rodriguez",
  "snippet": "",
  "published": "2026-10-29T21:34:13+00:00"
 },
 {
  "id": "bd0d0a56e01c",
  "region": "intl",
  "source": "The National",
  "title": "President Sheikh Mohamed offers to teach flydubai captain Smit Machchhar some jiu-jitsu moves",
  "snippet": "",
  "published": "2026-10-29T07:32:11+00:00"
 },
 {
  "id": "4724ea5131ae",
  "region": "intl",
  "source": "News Mobile",
  "title": "Captain Smit’s Head Stitches Catch UAE President’s Eye, Jiu-Jitsu Offer Goes Viral",
  "snippet": "",
  "published": "2026-10-29T09:21:52+00:00"
 },
 {
  "id": "13513304667a",
  "region": "intl",
  "source": "thenationalnews.com",
  "title": "UAE President jokes about jiu-jitsu lessons for hero flydubai pilot",
  "snippet": "",
  "published": "2026-10-29T05:53:31+00:00"
 },
 {
  "id": "48990b4b4bbb",
  "region": "intl",
  "source": "Kayo Sports",
  "title": "Stream Sports Online",
  "snippet": "",
  "published": "2026-10-29T21:34:06+00:00"
 },
 {
  "id": "446dcf4eb394",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Callie Marie Nelson vs Maria Luiza Rodrigues De C. L. S 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-10-29T00:14:35+00:00"
 },
 {
  "id": "1aee9ecb4d8d",
  "region": "intl",
  "source": "India Today",
  "title": "Jiu-jitsu once you recover: Capt Smit's head stitches catch UAE president's eye",
  "snippet": "",
  "published": "2026-10-29T06:18:01+00:00"
 },
 {
  "id": "d7a7d0139af7",
  "region": "intl",
  "source": "Turkmenportal.com",
  "title": "Tom Hardy received a brown belt in Brazilian jiu-jitsu",
  "snippet": "",
  "published": "2026-10-29T01:35:17+00:00"
 },
 {
  "id": "d55f22d82ab0",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "UFC BJJ Introduces Submission Of The Night Bonus Ahead Of UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-29T16:32:50+00:00"
 },
 {
  "id": "e7ec735a9e1c",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Rafael Lovato Jr: Jiu Jitsu Is Not A Sport – It’s A Martial Art",
  "snippet": "",
  "published": "2026-10-29T09:11:48+00:00"
 },
 {
  "id": "59fd0b67fc16",
  "region": "intl",
  "source": "BJJDOC",
  "title": "First Responders Compete in Exclusive Jiu-Jitsu Tournament Pitting Them Against Each Other",
  "snippet": "",
  "published": "2026-10-29T12:22:02+00:00"
 },
 {
  "id": "b0c7ed12c293",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "UFC BJJ 13 Results: Tackett vs. Rodriguez",
  "snippet": "",
  "published": "2026-10-29T15:58:57+00:00"
 },
 {
  "id": "858c9b37703d",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Ryan Hall: Coaches Try To BS Students With 1000s Of Tiny Details Before They Know Their Fundamentals",
  "snippet": "",
  "published": "2026-10-29T10:16:59+00:00"
 },
 {
  "id": "5df6af005a6a",
  "region": "intl",
  "source": "BJJDOC",
  "title": "UAE President Jokes About Jiu-Jitsu Lessons for Flydubai Pilot Who Foiled Hijacking Attempt",
  "snippet": "",
  "published": "2026-10-29T18:39:18+00:00"
 },
 {
  "id": "1964172b1619",
  "region": "intl",
  "source": "South Wales Argus",
  "title": "Welsh firefighter Chance Morgan crowned jiu-jitsu champion after ACL injury",
  "snippet": "",
  "published": "2026-10-29T23:30:00+00:00"
 },
 {
  "id": "2055d1347351",
  "region": "intl",
  "source": "BJJEE",
  "title": "Chris Haueter: “People Who Do Only No-Gi Lack Control & Pressure”",
  "snippet": "Chris Haueter has explained why academies once barred students from no-gi until purple belt. And, well, he argues that learning to grapple in the gi builds control and pressure that no-gi-only training can lack. Speaking about the old-school approach, he recalled that early years belonged to the gi: In my early days, you didn’t get to do no-gi until you were a purple belt. Based on the belief that you had to learn the complexities and control that you get from the gi. And I noticed people who do no-gi only lack that control. And they lack the pressure. Generally speaking, there are exceptions…",
  "published": "2026-10-29T09:39:48+00:00"
 },
 {
  "id": "a2bd36680bbe",
  "region": "intl",
  "source": "BJJEE",
  "title": "Qatari Wrestler Disqualified After Refusing To Let Female Referee Raise His Hand",
  "snippet": "A Greco-Roman qualification bout at the 2026 Senior World Championships in Astana, Kazakhstan, ended in a disqualification after Qatar’s Amer Ebrahim A A Alhammadi refused to allow a female referee to take his hand when the result was announced. The bout was in the 67 kg (147.7 lbs) division against Australia’s Tsuchika Shimoyamada. Once the match ended with Shimoyamada the apparent winner, standard protocol called for the referee to raise the victor’s hand. When the referee moved to complete the ceremony, Alhammadi reportedly told her not to touch him. A standoff followed on the mat. The mat…",
  "published": "2026-10-29T09:18:58+00:00"
 }
]
