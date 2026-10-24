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
  "id": "c52b337feec3",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "【パラ水泳 自由形】南井瑛翔 3つ目の金は自己新！大会新！日本新！【アジアパラ】",
  "snippet": "",
  "published": "2026-10-24T07:09:18+00:00"
 },
 {
  "id": "d659f3d94320",
  "region": "jp",
  "source": "MMAPLANET",
  "title": "【LFA244】「柔術やキックはダサい。レッスル&ボックスでUFCでも勝つ!!」ウッドリーが新ミドル級王者に",
  "snippet": "",
  "published": "2026-10-24T03:57:17+00:00"
 },
 {
  "id": "d061cf069251",
  "region": "jp",
  "source": "TOKYO MX",
  "title": "2026年10月25日(日)23:30～「刃牙道」＃１７「守護（しゅご）り」",
  "snippet": "",
  "published": "2026-10-24T11:03:17+00:00"
 },
 {
  "id": "254caa846ec1",
  "region": "jp",
  "source": "Howl.Link",
  "title": "石黒翔也Shoya Ishiguro (@ShoyaIshiguro) on X",
  "snippet": "",
  "published": "2026-10-24T10:44:35+00:00"
 },
 {
  "id": "8f8dd41213f7",
  "region": "jp",
  "source": "https://mediadogs.jp/",
  "title": "岸田宙大、11月8日のPANCRASE 368でBTTのダヴィ・チュンと対戦 5月のフライ級王座決定戦は時田隆成に2-1判定負け、柔術黒帯の経歴と戦績",
  "snippet": "",
  "published": "2026-10-24T16:12:08+00:00"
 },
 {
  "id": "4734e2fb65e2",
  "region": "jp",
  "source": "YouTube",
  "title": "【Fallout4】連邦をグラップリングで移動！？ゲーム性を根本から変えてしまうMOD【ゆっくり実況】",
  "snippet": "",
  "published": "2026-10-24T03:30:26+00:00"
 },
 {
  "id": "c5d8f886770c",
  "region": "jp",
  "source": "YouTube",
  "title": "@骨法復興は、オレがやる‼️骨法一筋37年のオレが…そして、オレに集いし門下生たちと共に…大原やってやろうじゃねーか‼️骨法グラップリング19Part14総括タイム〜完〜",
  "snippet": "",
  "published": "2026-10-24T02:18:39+00:00"
 },
 {
  "id": "b3e26ccb5cba",
  "region": "intl",
  "source": "FloGrappling",
  "title": "CAMERON ASHMAN vs SUNG KIM 2026 PBJJF World Jiu-Jitsu Championships",
  "snippet": "",
  "published": "2026-10-24T22:01:45+00:00"
 },
 {
  "id": "8c457242392d",
  "region": "intl",
  "source": "مكتب أبوظبي الإعلامي",
  "title": "Hamdan bin Mohamed bin Zayed attends Jiu-Jitsu President’s Cup",
  "snippet": "",
  "published": "2026-10-24T16:55:18+00:00"
 },
 {
  "id": "2ce77c342b24",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Continue Watching",
  "snippet": "",
  "published": "2026-10-24T22:01:46+00:00"
 },
 {
  "id": "41d0726dbae0",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "Al Wahda clinches Jiu-Jitsu President’s Cup for third consecutive year",
  "snippet": "",
  "published": "2026-10-24T21:15:38+00:00"
 },
 {
  "id": "094234d875d9",
  "region": "intl",
  "source": "Laurel Leader-Call",
  "title": "OpenMapp Launches Free Map of BJJ Open Mats and Drop-In Prices in 600+ US Cities",
  "snippet": "",
  "published": "2026-10-24T01:20:01+00:00"
 },
 {
  "id": "9091e28f2cea",
  "region": "intl",
  "source": "Sharjah24",
  "title": "Al Wahda crowned champions of Jiu-Jitsu President’s Cup",
  "snippet": "",
  "published": "2026-10-24T20:21:26+00:00"
 },
 {
  "id": "8f9464823d7c",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "Thani Al Zeyoudi: Leadership support key to regional and global jiu-jitsu achievements",
  "snippet": "",
  "published": "2026-10-24T18:28:52+00:00"
 },
 {
  "id": "bf72d59472f6",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Watch Jiu-Jitsu",
  "snippet": "",
  "published": "2026-10-23T18:05:55+00:00"
 },
 {
  "id": "4b8d8b420165",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "Top clubs chase Jiu-Jitsu President's Cup title in Abu Dhabi on Saturday",
  "snippet": "",
  "published": "2026-10-23T15:17:20+00:00"
 },
 {
  "id": "9bdf9b16fefa",
  "region": "intl",
  "source": "umlconnector.com",
  "title": "Venum Gladiator 3.0 Vale Tudo Shorts - Men's Compression Fight Shorts With Dry Tech",
  "snippet": "",
  "published": "2026-10-24T21:04:13+00:00"
 },
 {
  "id": "a76f59453d43",
  "region": "intl",
  "source": "Mixtape Madness",
  "title": "Tinie Tempah: An MM Exclusive Interview",
  "snippet": "",
  "published": "2026-10-23T12:03:23+00:00"
 },
 {
  "id": "ab7d96e0ea03",
  "region": "intl",
  "source": "Royal Navy",
  "title": "Combat Sports Takeover Brings Martial Arts to HMS Collingwood",
  "snippet": "",
  "published": "2026-10-24T13:17:33+00:00"
 },
 {
  "id": "e422f622197f",
  "region": "intl",
  "source": "BJJDOC",
  "title": "UFC Veteran Credits ‘Removing Toxic People’ For Successfully Running A BJJ Gym Since 1998",
  "snippet": "",
  "published": "2026-10-24T10:47:12+00:00"
 },
 {
  "id": "e82d462aea90",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Matt Serra Reveals How Gracie Camp Politics Cost Him A Gold Medal In IBJJF History Books",
  "snippet": "",
  "published": "2026-10-24T16:55:07+00:00"
 },
 {
  "id": "97f0c8a2d4c3",
  "region": "intl",
  "source": "BJJDOC",
  "title": "John Danaher: \"You Can't Just Teach Takedowns. You Have To Teach The Skills That Get You To The Takedowns.\"",
  "snippet": "",
  "published": "2026-10-24T08:22:30+00:00"
 },
 {
  "id": "77eee4726bbd",
  "region": "intl",
  "source": "BJJEE",
  "title": "B Team’s Owen Jones On Confronting Bad Training Partners: “You Kicked Me 4 Times…”",
  "snippet": "Owen Jones, one of Jiu-Jitsu’s most promising competitors, is willing to have the awkward conversation when a training partner makes the room unsafe. On a recent podcast , he described telling one partner he would not train with him again: I’ve literally trained with a guy, and I’ve just told him right around: “Yo, I’m actually never going to train with you again.” And he was like, why? I was like: “ou’re so spazzy. You kicked me like four times. You almost spinning elbowed me. I’ve got nothing productive from this session.” Jones also compared gym cultures: Everyone takes it way more seriousl…",
  "published": "2026-10-24T05:59:04+00:00"
 },
 {
  "id": "88448b1581f9",
  "region": "intl",
  "source": "BJJEE",
  "title": "Andre Galvao vs Rousimar Palhares Set For Combat Jiu-Jitsu Match At ACBJJ 23",
  "snippet": "Andre Galvao and Rousimar Palhares will meet again more than a decade after their ADCC final, this time under Combat Jiu-Jitsu rules. The two will headline ACBJJ 23 on November 13 at Farmasi Arena in Rio de Janeiro, according to sources . Their first meeting was the 2011 ADCC final in the under-194 lbs (88 kg) division in Nottingham, England, which Galvao won 9-4. The rematch will be at 220 lbs (100 kg). Former UFC competitor and event promoter Davi Ramos explained the format: Combat Jiu-Jitsu allows punches and kicks to the body, but strikes to the head are prohibited. The rounds are scored u…",
  "published": "2026-10-24T05:49:45+00:00"
 }
]
