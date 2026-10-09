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
  "id": "70548936ebd4",
  "region": "jp",
  "source": "タウンニュース",
  "title": "ブラジリアン柔術 世界大会で銀 桜台のジムの堀井さん",
  "snippet": "",
  "published": "2026-10-08T15:00:00+00:00"
 },
 {
  "id": "ebdf29202540",
  "region": "jp",
  "source": "N高等学校",
  "title": "N高2年 鈴木美結さんがブラジリアン柔術選手としてタイの『国家スポーツ功労者表彰』を受賞！",
  "snippet": "",
  "published": "2026-10-08T02:00:06+00:00"
 },
 {
  "id": "1e0156d8003f",
  "region": "jp",
  "source": "十勝毎日新聞",
  "title": "カルペディエムの阿部、武石Ｖ アジア柔術チャンピオンシップ",
  "snippet": "",
  "published": "2026-10-08T06:00:00+00:00"
 },
 {
  "id": "a0dff06807c1",
  "region": "jp",
  "source": "タウンニュース",
  "title": "ブラジリアン柔術の世界大会で準優勝した 堀井 慎也さん 厚木市在住 45歳",
  "snippet": "",
  "published": "2026-10-08T15:00:00+00:00"
 },
 {
  "id": "e39edfcdca5c",
  "region": "jp",
  "source": "福井新聞社",
  "title": "ガリットチュウ福島『ONE』緊急参戦 “朝倉未来の柔術コーチ”竹浦正起とグラップリングマッチ",
  "snippet": "",
  "published": "2026-10-07T14:51:45+00:00"
 },
 {
  "id": "c1696b86bf56",
  "region": "jp",
  "source": "イーファイト",
  "title": "【ONE】ガリットチュウ福島善成、国内最高峰グラップラー竹浦正起と対戦決定「とんでもないオファー」＝10.17",
  "snippet": "",
  "published": "2026-10-08T10:14:40+00:00"
 },
 {
  "id": "7b409663979f",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "「ガリットチュウ」福島、「ＯＮＥ ＳＡＭＵＲＡＩ ４」参戦「とんでもないオファーが来たなと思っております…１０・１７有明アリーナ",
  "snippet": "",
  "published": "2026-10-07T22:19:00+00:00"
 },
 {
  "id": "7e92b20ff022",
  "region": "jp",
  "source": "Howl.Link",
  "title": "柔術ナビ｜JIU-JITSU NAVI (@jiujitsunavi) on X",
  "snippet": "",
  "published": "2026-10-08T09:53:22+00:00"
 },
 {
  "id": "54af8d31e3dd",
  "region": "jp",
  "source": "Howl.link",
  "title": "Media Clips (@mediaterrace) on X",
  "snippet": "",
  "published": "2026-10-07T15:47:55+00:00"
 },
 {
  "id": "df68af6809de",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "ガリットチュウ福島善成、国内最高峰グラップラー竹浦正起と対戦決定「とんでもないオファー」＝10.17 ONE（イーファイト）",
  "snippet": "",
  "published": "2026-10-08T10:15:57+00:00"
 },
 {
  "id": "05cf237921ae",
  "region": "jp",
  "source": "AERA DIGITAL",
  "title": "「ONE SAMURAI 4」 追加対戦カードを発表！ONEライト級サブミッショングラップリング 福島善成 vs 竹浦正起",
  "snippet": "",
  "published": "2026-10-08T01:16:43+00:00"
 },
 {
  "id": "d58344c02142",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 12: Moura vs Fornarino Fight Card",
  "snippet": "",
  "published": "2026-10-08T23:40:33+00:00"
 },
 {
  "id": "5b5e66036a08",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "UFC BJJ 12 Live Results: A New Champion Will Be Crowned",
  "snippet": "",
  "published": "2026-10-08T23:44:26+00:00"
 },
 {
  "id": "a2b9da264522",
  "region": "intl",
  "source": "FloGrappling",
  "title": "PBJJF World Jiu-Jitsu Championships",
  "snippet": "",
  "published": "2026-10-08T02:06:25+00:00"
 },
 {
  "id": "d953457421fe",
  "region": "intl",
  "source": "Sherdog",
  "title": "PFL Africa's Rivaldo Pereira targets KO of unbeaten David Samuel",
  "snippet": "",
  "published": "2026-10-08T05:48:31+00:00"
 },
 {
  "id": "ca3fc2d5de54",
  "region": "intl",
  "source": "UFC.com",
  "title": "Landon Elmore Bowl Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-09T01:00:00+00:00"
 },
 {
  "id": "9d5d6412c1aa",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship - Videos",
  "snippet": "",
  "published": "2026-10-08T03:01:47+00:00"
 },
 {
  "id": "b6ecfbb832f9",
  "region": "intl",
  "source": "UFC.com",
  "title": "Gilbert Burns Media Day Interview | UFC BJJ",
  "snippet": "",
  "published": "2026-10-08T19:14:38+00:00"
 },
 {
  "id": "dc16abc454d5",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Luke Griffith Makes A Comeback With A Submission In The ADCC Finals | Submission Of The Month (September)",
  "snippet": "",
  "published": "2026-10-08T02:06:25+00:00"
 },
 {
  "id": "ebdf7bed6380",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 12 Results",
  "snippet": "",
  "published": "2026-10-08T16:57:49+00:00"
 },
 {
  "id": "cd928e4180e0",
  "region": "intl",
  "source": "The National",
  "title": "‘My country deserves this’: UAE Asian Games champions Al Hosani and Al Shehhi on gold and World Pro dreams",
  "snippet": "",
  "published": "2026-10-08T08:28:10+00:00"
 },
 {
  "id": "0aa33bb4fa38",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - Finals - M/W",
  "snippet": "",
  "published": "2026-10-07T23:37:36+00:00"
 },
 {
  "id": "6da1e5fa0729",
  "region": "intl",
  "source": "3AW",
  "title": "Melburnian crowned Jiu-Jitsu World Champion",
  "snippet": "",
  "published": "2026-10-08T22:20:04+00:00"
 },
 {
  "id": "54d8faadcb18",
  "region": "intl",
  "source": "The Body Lock",
  "title": "Two Champions Collide: Moura and Fornarino Battle for New UFC BJJ Title",
  "snippet": "",
  "published": "2026-10-08T21:41:13+00:00"
 },
 {
  "id": "7d0460d290cf",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Draculino Explains How Modern Jiu Jitsu Drifted Away From Real Combat",
  "snippet": "",
  "published": "2026-10-08T15:32:48+00:00"
 },
 {
  "id": "1df86009626e",
  "region": "intl",
  "source": "BJJDOC",
  "title": "LL Cool J Is Training Jiu-Jitsu At Renzo Gracie’s In Brooklyn",
  "snippet": "",
  "published": "2026-10-08T08:14:06+00:00"
 },
 {
  "id": "63b77e55db70",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Your BJJ Instructor Should Not Be Your Guru or A Life Coach, BJJ Legend Draculino Cautions",
  "snippet": "",
  "published": "2026-10-08T15:41:41+00:00"
 },
 {
  "id": "58f8080b02f9",
  "region": "intl",
  "source": "Quotidiano Sportivo",
  "title": "Brazilian Jiu-Jitsu. Fight Gym at the top with Pucci and Becuzzi.",
  "snippet": "",
  "published": "2026-10-08T06:36:28+00:00"
 },
 {
  "id": "35a44499e1df",
  "region": "intl",
  "source": "BJJEE",
  "title": "Draculino Warns BJJ Instructors Against Posing As Life Coaches: “They Think They’re Gurus Or Something”",
  "snippet": "Draculino, who has spent more than 40 years on the mats, has a message for the modern Jiu-Jitsu world: instructors should not cast themselves as gurus or life coaches. The coral belt grew up alongside the Gracie family in Rio de Janeiro’s Barra da Tijuca and built one of the most respected academies in Brazilian Jiu-Jitsu. He made the remarks on The Resilient Show, where he also traced his path from a young surfer who stumbled into the sport to competitor, instructor and mentor. He described a growing tendency among Jiu-Jitsu people, and he was clear that he did not mean veterans who have been…",
  "published": "2026-10-08T23:32:45+00:00"
 },
 {
  "id": "3978ed029afd",
  "region": "intl",
  "source": "BJJEE",
  "title": "Victor Hugo Announces Possible Retirement From ADCC: “Everything’s Moving Fast”",
  "snippet": "Victor Hugo finished ADCC 2026 by submitting his way through the +220 lb (+99 kg) division, then announced his retirement from ADCC competition before the absolute bracket began. Hugo said a conversation with FloGrappling GM Ben Kovacs shortly before the decision planted the seed: It was brewing on my head a little bit. I think the last person before it actually happened that I talked to was Ben. Ben asked me: “Hey, if you win everything, are you retiring?” I was like: “I haven’t thought about it.” As the submissions kept coming, the thought hardened: The more it went the way that it went like…",
  "published": "2026-10-08T23:27:43+00:00"
 }
]
