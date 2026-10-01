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
  "id": "92f9d801c1c2",
  "region": "jp",
  "source": "hokkaido-np.co.jp",
  "title": "極めた寝技 野中さん全国3位 ブラジリアン柔術大会 江別高2年 競技歴2年「次は世界」",
  "snippet": "",
  "published": "2026-09-30T19:00:00+00:00"
 },
 {
  "id": "8f944c803e50",
  "region": "jp",
  "source": "ベースボールチャンネル",
  "title": "アジア大会2026 柔術日本代表のテレビ放送・配信予定・日程｜アジア競技大会 愛知・名古屋",
  "snippet": "",
  "published": "2026-09-30T22:00:53+00:00"
 },
 {
  "id": "cf111874c4a3",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "カン・トー柔術は全国スポーツ大会に向けて加速している。",
  "snippet": "",
  "published": "2026-09-30T06:37:40+00:00"
 },
 {
  "id": "658748667fd3",
  "region": "jp",
  "source": "YouTube",
  "title": "【FULL FIGHT】前田直紀 vs ジョアオ・コバヤシ / SJJIF WORLD 2026 【ブラジリアン柔術】 Naoki Maeda vs Joao Kobayashi",
  "snippet": "",
  "published": "2026-09-30T05:26:03+00:00"
 },
 {
  "id": "d303f547ecde",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "「最強芸能人」ランキング、\"剣道二段\"吉沢亮を抑えた「かっこいいのに強い」イケオジ俳優は【総合順位】（ピンズバNEWS）",
  "snippet": "",
  "published": "2026-09-30T02:00:37+00:00"
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
  "id": "bc11e5c6c23f",
  "region": "jp",
  "source": "ピンズバNEWS",
  "title": "「最強芸能人」ランキング、\"空手世界一\"横浜流星を抑えた「別格の強さ」の人物は【トップ3】｜ニュース",
  "snippet": "",
  "published": "2026-09-29T23:30:00+00:00"
 },
 {
  "id": "87d2052c04e1",
  "region": "jp",
  "source": "Infoseek",
  "title": "レスリング日下、尾崎ら登場 第13日見どころ",
  "snippet": "",
  "published": "2026-09-30T08:24:01+00:00"
 },
 {
  "id": "3b9e4cde68a2",
  "region": "jp",
  "source": "Laodong.vn",
  "title": "本日(10月1日)の第20回アジア競技大会に出場するベトナム代表団の生中継",
  "snippet": "",
  "published": "2026-09-30T23:48:00+00:00"
 },
 {
  "id": "c4fbcb5e1307",
  "region": "jp",
  "source": "au Webポータル",
  "title": "「最強芸能人」ランキング、\"空手世界一\"横浜流星を抑えた「別格の強さ」の人物は【トップ3】",
  "snippet": "",
  "published": "2026-09-30T02:08:55+00:00"
 },
 {
  "id": "1ab1576d3620",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月1日のアジア競技大会（ASIAD 20）のスケジュール：eスポーツによる「衝撃」が期待できる。テコンドー競技も開催される。",
  "snippet": "",
  "published": "2026-10-01T00:00:12+00:00"
 },
 {
  "id": "8f82fe15cc63",
  "region": "jp",
  "source": "Laodong.vn",
  "title": "柔術選手のダン・ディン・トゥン、フン・ティ・フエがアジア大会20のメダル獲得のチャンスを狙う",
  "snippet": "",
  "published": "2026-09-30T02:42:38+00:00"
 },
 {
  "id": "c27792d15b58",
  "region": "jp",
  "source": "Goal.com",
  "title": "全競技スケジュール・日程｜第20回アジア大会",
  "snippet": "",
  "published": "2026-09-30T09:42:56+00:00"
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
  "id": "c27fd40c8e57",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月1日から10日まで開催される第20回アジア競技大会におけるベトナムスポーツ代表団のスケジュール。",
  "snippet": "",
  "published": "2026-10-01T00:05:49+00:00"
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
  "id": "d46320940912",
  "region": "jp",
  "source": "au Webポータル",
  "title": "「最強芸能人」ランキング、\"剣道二段\"吉沢亮を抑えた「かっこいいのに強い」イケオジ俳優は【総合順位】",
  "snippet": "",
  "published": "2026-09-30T02:06:00+00:00"
 },
 {
  "id": "a594218adc91",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月1日のアジア競技大会（ASIAD 20）のスケジュール：ベトナム代表は、決定的な試合での突破口を待ち望んでいる。",
  "snippet": "",
  "published": "2026-10-01T00:05:53+00:00"
 },
 {
  "id": "1180d03e30e1",
  "region": "jp",
  "source": "oita-press.co.jp",
  "title": "レスリング日下、尾崎ら登場",
  "snippet": "",
  "published": "2026-09-29T20:30:36+00:00"
 },
 {
  "id": "c3a08c7d2466",
  "region": "jp",
  "source": "ぐぐスポ！",
  "title": "【柔術】アジア大会2026 日本代表の結果速報・日程・組み合わせ・放送予定",
  "snippet": "",
  "published": "2026-09-30T10:51:53+00:00"
 },
 {
  "id": "811186980c3f",
  "region": "jp",
  "source": "スポカレ",
  "title": "【石黒翔也】ONE Fight Night 48の視聴方法！配信サービス、対戦カードを解説",
  "snippet": "",
  "published": "2026-09-30T03:49:37+00:00"
 },
 {
  "id": "72035b4e6491",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "フエ市国境警備隊が、海上で遭難した人々を救助するための訓練を実施した。",
  "snippet": "",
  "published": "2026-09-30T18:04:59+00:00"
 },
 {
  "id": "df2af45b9c94",
  "region": "jp",
  "source": "au Webポータル",
  "title": "“圧倒的に好評”デモ版が配信中のメトロイドヴァニア『Iron Bramble』ウィッシュリスト数10万件突破",
  "snippet": "",
  "published": "2026-09-29T16:16:00+00:00"
 },
 {
  "id": "257c8031ed84",
  "region": "intl",
  "source": "Community Impact Newspaper",
  "title": "Gracie Barra Brazilian jiu-jitsu academy to open in Liberty Hill",
  "snippet": "",
  "published": "2026-09-30T21:01:04+00:00"
 },
 {
  "id": "d58344c02142",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 12: Moura vs Fornarino Fight Card",
  "snippet": "",
  "published": "2026-09-30T16:00:00+00:00"
 },
 {
  "id": "f6fbad4f8649",
  "region": "intl",
  "source": "FloGrappling",
  "title": "The Black Belt Brackets Are Out For The IBJJF No-Gi Pan Championship",
  "snippet": "",
  "published": "2026-09-30T21:13:22+00:00"
 },
 {
  "id": "0bb2e8cace4e",
  "region": "intl",
  "source": "Sportscape Magazine",
  "title": "WATCH: Charles Oliveira Hilariously Reacts to ‘Purple Belt Syndrome’ in New BJJ Skit",
  "snippet": "",
  "published": "2026-09-30T18:56:41+00:00"
 },
 {
  "id": "dc0ffa5feb9c",
  "region": "intl",
  "source": "boxingnews.com",
  "title": "UFC BJJ 12: Moura vs Fornarino — Full Card, Start Time & How to Watch",
  "snippet": "",
  "published": "2026-09-30T22:07:40+00:00"
 },
 {
  "id": "6bdb8d641625",
  "region": "intl",
  "source": "dailydispatch.com",
  "title": "Firefighters receive jiu-jitsu training in Springfield for self-defense in the field",
  "snippet": "",
  "published": "2026-09-29T14:46:37+00:00"
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
  "id": "1fb1fc189be8",
  "region": "intl",
  "source": "Inside The Games",
  "title": "South Korean jiu-jitsu athletes cleared for Asian Games",
  "snippet": "",
  "published": "2026-09-29T19:56:33+00:00"
 },
 {
  "id": "296704fec2fc",
  "region": "intl",
  "source": "Bloody Elbow",
  "title": "Mikey Musumeci outlines plans to win UFC title once held by Demetrius Johnson after BJJ switch",
  "snippet": "",
  "published": "2026-09-30T02:54:07+00:00"
 },
 {
  "id": "88aa2ec6a1f8",
  "region": "intl",
  "source": "jordannews.jo",
  "title": "Jordan’s jiu-jitsu team begins Asian Games campaign in Nagoya tomorrow",
  "snippet": "",
  "published": "2026-09-30T12:58:35+00:00"
 },
 {
  "id": "b63b3072b68b",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Everything To Know About The 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-09-29T15:13:00+00:00"
 },
 {
  "id": "d18ad9f69f69",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship Schedule",
  "snippet": "",
  "published": "2026-09-29T15:32:21+00:00"
 },
 {
  "id": "1ef9a70ea258",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 CBJJ Brazilian Jiu-Jitsu Championship No-Gi",
  "snippet": "",
  "published": "2026-09-30T00:30:57+00:00"
 },
 {
  "id": "a49e0c6efa8d",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-09-29T15:28:51+00:00"
 },
 {
  "id": "8e185a9862e8",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Lucas Gualberto Gomes Nascimento",
  "snippet": "",
  "published": "2026-09-29T21:31:10+00:00"
 },
 {
  "id": "f9ee79e20836",
  "region": "intl",
  "source": "FloGrappling",
  "title": "How Helena Crevar Submitted Everyone And Made ADCC History | The FloGrappling Show (Ep 106)",
  "snippet": "",
  "published": "2026-09-29T16:50:30+00:00"
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
  "id": "0bab1b41d97f",
  "region": "intl",
  "source": "jordannews.jo",
  "title": "Jordan’s Jiu-Jitsu Team Begins Training Ahead of the Asian Games",
  "snippet": "",
  "published": "2026-09-29T13:59:15+00:00"
 },
 {
  "id": "81a5937ab388",
  "region": "intl",
  "source": "CTV News",
  "title": "Cambridge athlete wins gold again at Brazilian jiu-jitsu championship",
  "snippet": "",
  "published": "2026-09-29T23:24:48+00:00"
 },
 {
  "id": "79920095f084",
  "region": "intl",
  "source": "FloGrappling",
  "title": "WHO'S IN For the 2026 IBJJF No-Gi Pan Championships",
  "snippet": "",
  "published": "2026-09-29T20:17:23+00:00"
 },
 {
  "id": "21d68a055ecd",
  "region": "intl",
  "source": "Secret NYC",
  "title": "‘It’s my job to make you a mountain climber’: inside the Webster Ave dojo where a 6-time world champion has combined karate, kickboxing, and jiu-jitsu to mentor Bronx youth for over 20 years",
  "snippet": "",
  "published": "2026-09-30T18:54:23+00:00"
 },
 {
  "id": "df177775ec1c",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 ADCC World Championships Presented by FloGrappling",
  "snippet": "",
  "published": "2026-09-29T15:01:07+00:00"
 },
 {
  "id": "1c09601ce92b",
  "region": "intl",
  "source": "sherdog.com",
  "title": "Mikey Musumeci targets UFC flyweight title with MMA transition",
  "snippet": "",
  "published": "2026-09-30T07:47:22+00:00"
 },
 {
  "id": "f7ddabb085b9",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "Mikey Musumeci Makes MMA Case With Bryce Mitchell-Ilia Topuria Wrestling Comparison",
  "snippet": "",
  "published": "2026-09-30T05:59:45+00:00"
 },
 {
  "id": "9f746775cba8",
  "region": "intl",
  "source": "Inquirer.net",
  "title": "Asian Games 2026: Team Philippines’ schedule for October 1",
  "snippet": "",
  "published": "2026-09-30T14:51:00+00:00"
 },
 {
  "id": "e72d9f483d3e",
  "region": "intl",
  "source": "BJJEE",
  "title": "Tye Ruotolo To Compete For The Lightweight MMA Title At ONE: The Inner Circle 37",
  "snippet": "ONE Championship has booked one of its most compelling title fights of the year, pitting two athletes from major martial arts lineages against each other… As the reigning ONE Lightweight and Welterweight MMA World Champion Christian Lee will defend his lightweight belt against reigning ONE Welterweight Submission Grappling World Champion Tye Ruotolo, at The Inner Circle 37. Ruotolo already holds the distinction of handing Christian’s younger brother, Adrian Lee, his first career loss, and now the 23-year-old grappling prodigy has a shot at defeating a second member of the Lee family, this time…",
  "published": "2026-09-30T06:19:17+00:00"
 },
 {
  "id": "2f52fb9c7a46",
  "region": "intl",
  "source": "BJJEE",
  "title": "ADCC Introduces New Rule: Interference From Coaches Or Spectators Can Cost Athletes The Match",
  "snippet": "The ADCC has rolled out a new policy that puts athletes’ results directly at risk when coaches, parents, or spectators overstep boundaries during a match. Under the updated code of conduct, unauthorized individuals are now barred from entering the competition area while a match is underway, with the restricted zone covering both the mat itself and a clearly marked perimeter around it. Anyone who breaks this rule, threatens participants or officials, or disregards referee instructions triggers immediate consequences that can end an athlete’s competition on the spot. Notably, the rule applies ev…",
  "published": "2026-09-30T06:11:38+00:00"
 },
 {
  "id": "5640a3d4a5bd",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "Tye Ruotolo Set For First ONE Title-Fight Against Christian Lee",
  "snippet": "Tye Ruotolo has just taken a huge leap in his MMA career as he will now be challenging Christian Lee for the ONE Championship lightweight world title at ONE: The Inner Circle 37 on November 6th, 2026. It’s going to be the biggest challenge he’s ever faced and not just because there’s a title on the line, but also because Lee will be the most experienced opponent he’s had. Ruotolo is currently just 2-0 in professional MMA and only a little over a year removed from making his debut . It’s an unprecedented rise through the ONE Championship ranks but if anyone is capable of doing it, it’s one of t…",
  "published": "2026-09-30T15:08:36+00:00"
 }
]
