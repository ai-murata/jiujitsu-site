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
  "id": "7173ff64b8f7",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "ベトナムの柔術選手は、第20回アジア競技大会でメダルの色を変えることを目指している。",
  "snippet": "",
  "published": "2026-09-29T11:44:41+00:00"
 },
 {
  "id": "02caf267897b",
  "region": "jp",
  "source": "ダイヤモンド・オンライン",
  "title": "50代になっても「若い頃と同じ頑張り方」をする人が、うまくいかなくなる理由",
  "snippet": "",
  "published": "2026-09-29T22:35:00+00:00"
 },
 {
  "id": "2c8614730588",
  "region": "jp",
  "source": "朝日新聞",
  "title": "なぜアジアは格闘技が強くて盛んなのか？ 五輪金メダルの6割占める [アジア大会2026]",
  "snippet": "",
  "published": "2026-09-29T02:28:09+00:00"
 },
 {
  "id": "600f7866c330",
  "region": "jp",
  "source": "ピンズバNEWS",
  "title": "「最強芸能人」ランキング、\"空手世界一\"横浜流星を抑えた「別格の強さ」の人物は【トップ3】｜概要｜ニュース",
  "snippet": "",
  "published": "2026-09-29T23:30:00+00:00"
 },
 {
  "id": "81620a4231c6",
  "region": "jp",
  "source": "efight.jp",
  "title": "“工場勤務10年”まゆゆ、むっちり健康美！ミニワンピでラウンドガール",
  "snippet": "",
  "published": "2026-09-29T16:12:21+00:00"
 },
 {
  "id": "1ce51b70f1d3",
  "region": "jp",
  "source": "クランクイン！",
  "title": "“日本好き”モデルのバーバラ・パルヴィン、第1子出産 ドジャース大谷のユニフォームを着て報告",
  "snippet": "",
  "published": "2026-09-29T07:55:14+00:00"
 },
 {
  "id": "6bc2ab4780e2",
  "region": "jp",
  "source": "ピンズバNEWS",
  "title": "「最強芸能人」ランキング、\"剣道二段\"吉沢亮を抑えた「かっこいいのに強い」イケオジ俳優は【第4位以下】｜概要｜ニュース",
  "snippet": "",
  "published": "2026-09-29T23:30:00+00:00"
 },
 {
  "id": "c3a08c7d2466",
  "region": "jp",
  "source": "ぐぐスポ！",
  "title": "【柔術】アジア大会2026 日本代表の結果速報・日程・組み合わせ・放送予定",
  "snippet": "",
  "published": "2026-09-29T13:50:43+00:00"
 },
 {
  "id": "a85bcdc4719a",
  "region": "jp",
  "source": "t.co",
  "title": "まこあᜊ⍤⃝ᜊ (@makoawallflower) on X",
  "snippet": "",
  "published": "2026-09-28T13:12:56+00:00"
 },
 {
  "id": "6e1d5209262c",
  "region": "jp",
  "source": "t.co",
  "title": "アジア大会ライバル選手をざっくり紹介｜伯柔記",
  "snippet": "",
  "published": "2026-09-29T06:28:56+00:00"
 },
 {
  "id": "152924914d06",
  "region": "jp",
  "source": "Infoseek",
  "title": "“圧倒的に好評”デモ版が配信中のメトロイドヴァニア『Iron Bramble』ウィッシュリスト数10万件突破",
  "snippet": "",
  "published": "2026-09-29T15:45:03+00:00"
 },
 {
  "id": "d566d9556c3d",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "【最大4人協力】ネズミたちがおんぼろ蒸気船を動かすアクションゲーム『All Rats on",
  "snippet": "",
  "published": "2026-09-29T07:54:10+00:00"
 },
 {
  "id": "b63b3072b68b",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Everything To Know About The 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-09-29T15:13:00+00:00"
 },
 {
  "id": "1fb1fc189be8",
  "region": "intl",
  "source": "Inside The Games",
  "title": "South Korean jiu-jitsu athletes cleared for Asian Games",
  "snippet": "",
  "published": "2026-09-29T19:56:33+00:00"
 },
 {
  "id": "5b352664ea72",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "How To Watch The 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-09-29T14:51:09+00:00"
 },
 {
  "id": "2b91302e4964",
  "region": "intl",
  "source": "dailydispatch.com",
  "title": "Firefighters in Illinois receive jiu-jitsu training for self-defense in the field",
  "snippet": "",
  "published": "2026-09-28T17:54:43+00:00"
 },
 {
  "id": "d18ad9f69f69",
  "region": "intl",
  "source": "flograppling.com",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship Schedule",
  "snippet": "",
  "published": "2026-09-29T15:32:21+00:00"
 },
 {
  "id": "54c783739822",
  "region": "intl",
  "source": "CTV News",
  "title": "Canadian Brazilian jiu-jitsu athlete wins another gold medal at international championship",
  "snippet": "",
  "published": "2026-09-29T22:22:56+00:00"
 },
 {
  "id": "6db8f53fa2e7",
  "region": "intl",
  "source": "Eyewitness News (WEHT/WTVW)",
  "title": "Illinois firefighters receive jiu-jitsu training for self-defense in the field",
  "snippet": "",
  "published": "2026-09-28T14:27:18+00:00"
 },
 {
  "id": "0bab1b41d97f",
  "region": "intl",
  "source": "jordannews.jo",
  "title": "Jordan’s Jiu-Jitsu Team Begins Training Ahead of the Asian Games",
  "snippet": "",
  "published": "2026-09-29T11:02:42+00:00"
 },
 {
  "id": "a49e0c6efa8d",
  "region": "intl",
  "source": "flograppling.com",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-09-29T15:28:51+00:00"
 },
 {
  "id": "81a5937ab388",
  "region": "intl",
  "source": "CTV News",
  "title": "Cambridge athlete wins gold again at Brazilian jiu-jitsu championship",
  "snippet": "",
  "published": "2026-09-29T22:55:37+00:00"
 },
 {
  "id": "491136a2f1bf",
  "region": "intl",
  "source": "flograppling.com",
  "title": "How Helena Crevar Submitted Everyone And Made ADCC History | The FloGrappling Show (Ep 106)",
  "snippet": "",
  "published": "2026-09-29T16:30:28+00:00"
 },
 {
  "id": "79920095f084",
  "region": "intl",
  "source": "flograppling.com",
  "title": "WHO'S IN For the 2026 IBJJF No-Gi Pan Championships",
  "snippet": "",
  "published": "2026-09-29T20:17:23+00:00"
 },
 {
  "id": "5d43eb2372a2",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Cassia Moura Can Make UFC BJJ History — Adele Fornarino Stands in Her Way",
  "snippet": "",
  "published": "2026-09-29T21:15:17+00:00"
 },
 {
  "id": "05115e337c5d",
  "region": "intl",
  "source": "LowKickMMA.com",
  "title": "“People Are Going To Be Really Surprised” – Mikey Musumeci Ready for MMA Move, Wants to Chase UFC Flyweight Championship",
  "snippet": "",
  "published": "2026-09-29T21:30:35+00:00"
 },
 {
  "id": "97a20aa869ac",
  "region": "intl",
  "source": "bjjdoc.com",
  "title": "Top Divorce Lawyer Says Daddy Issues Turn Men Into BJJ Guys",
  "snippet": "",
  "published": "2026-09-29T07:19:02+00:00"
 },
 {
  "id": "50bfbc1bdfa8",
  "region": "intl",
  "source": "bjjdoc.com",
  "title": "UFC Cop Luis Hernandez Promoted To BJJ Black Belt After Submitting Wanted Man At UFC Apex",
  "snippet": "",
  "published": "2026-09-29T07:48:11+00:00"
 },
 {
  "id": "b2a9e622471e",
  "region": "intl",
  "source": "SheFinds",
  "title": "Tom Brady Was Reportedly 'Blindsided' By Gisele Bündchen Divorce After 'Cheating' Rumors With Her Jiu Jitsu Instructor, Biographer Reveals: 'Something Very Bad' Happened",
  "snippet": "",
  "published": "2026-09-28T21:00:11+00:00"
 },
 {
  "id": "1808ec2728a4",
  "region": "intl",
  "source": "Mix Vale",
  "title": "Willian Masuda returns home facing paralysis after illegal jiu-jitsu slam",
  "snippet": "",
  "published": "2026-09-29T19:26:38+00:00"
 },
 {
  "id": "98a423af8cac",
  "region": "intl",
  "source": "BJJEE",
  "title": "Top Divorce Lawyer: “When A Guy Has Daddy Issues, He Ends Up Doing BJJ”",
  "snippet": "Brazilian jiu-jitsu has picked up an unusual reputation online in recent years – with the sport sometimes joked about as something for “divorced dads”. On the Mostly Wise podcast, divorce lawyer James Sexton addressed the stereotype and offered an explanation for where it comes from: When a girl has daddy issues, you end up with a stri**er. And when a guy has daddy issues, you end up with a guy who does BJJ. The line got laughs, but the conversation quickly shifted toward what Sexton, who’s practiced divorce law for decades, believes actually draws men to the sport: Because it is really like a…",
  "published": "2026-09-29T07:50:05+00:00"
 },
 {
  "id": "427cdb6523c7",
  "region": "intl",
  "source": "BJJEE",
  "title": "Chris Haueter Warns Against Academies That Try To Control Students Off The Mat: “Toxic Relationship”",
  "snippet": "Chris Haueter, one of the first twelve non-Brazilians to earn a Brazilian Jiu-Jitsu black belt and a member of the “Dirty Dozen”, has spent decades around the sport. In a recent podcast conversation, the 61-year-old had a warning for anyone training under an instructor who tries to extend their authority well past technique: If you’re stuck in one of those unhealthy relationships where you’re paying some man to tell you what you can and can’t wear, you can’t and can’t teach, you might be in a toxic relationship. The comment took direct aim at academies that police things like uniforms, appeara…",
  "published": "2026-09-29T07:38:56+00:00"
 },
 {
  "id": "78cfe7824a7b",
  "region": "intl",
  "source": "BJJEE",
  "title": "Fighters talk BKFC Fight Night Belgrade, World’s Baddest Man global tournament tryouts come to Belgrade, Serbia, in October 2026",
  "snippet": "The Bare Knuckle Fighting Championship (BKFC) is bringing one of the biggest combat sports events of 2026 to the brilliant Belgrade, Serbia! BKFC Belgrade fight week festivities are coming to Serbia and the Balkans. The combat sports happenings in Eastern Europe will decide the future of the fight game worldwide. First comes the highly anticipated BKFC Belgrade tryouts for the $20 million World’s Baddest Man (WBM) global tournament (2026-2027) , on October 15, 2026. Second comes the BKFC Fight Night Belgrade (aka BKFC Belgrade) event – featuring a stacked fight card of pivotal bare-knuckle box…",
  "published": "2026-09-28T15:35:59+00:00"
 }
]
