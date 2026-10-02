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
  "id": "068796aadcec",
  "region": "jp",
  "source": "nnn.ed.jp",
  "title": "N高2年 鈴木美結選手が「第20回アジア競技大会」柔術で銅メダルを獲得！",
  "snippet": "",
  "published": "2026-10-02T00:45:30+00:00"
 },
 {
  "id": "5a02b2d85595",
  "region": "jp",
  "source": "読売新聞",
  "title": "柔術 男子69キロ級 試合結果・記録 アジア競技大会2026 愛知・名古屋",
  "snippet": "",
  "published": "2026-10-01T13:09:00+00:00"
 },
 {
  "id": "68e59705e3d3",
  "region": "jp",
  "source": "河北新報オンライン",
  "title": "柔術男子69キロ級・熊田堅信（宮城・名取出身）人生を変えた柔術「才能よりも努力がものをいう。練習すればするだけ強くなる」＜アジア大会",
  "snippet": "",
  "published": "2026-10-01T09:21:00+00:00"
 },
 {
  "id": "0907e97a1846",
  "region": "jp",
  "source": "TVer",
  "title": "佐々木と町田がブラジリアン柔術でガチ対決！？ 仙台市・カルペディエム仙台",
  "snippet": "",
  "published": "2026-10-01T15:20:24+00:00"
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
  "id": "92f9d801c1c2",
  "region": "jp",
  "source": "北海道新聞デジタル",
  "title": "極めた寝技 野中さん全国3位 ブラジリアン柔術大会 江別高2年 競技歴2年「次は世界」",
  "snippet": "",
  "published": "2026-09-30T19:00:00+00:00"
 },
 {
  "id": "de9870bd8408",
  "region": "jp",
  "source": "UFC公式",
  "title": "UFC BJJ 12: Moura vs Fornarino Fight Card",
  "snippet": "",
  "published": "2026-09-30T16:00:00+00:00"
 },
 {
  "id": "a3cfe956df0b",
  "region": "jp",
  "source": "Laodong.vn",
  "title": "ベトナムのeスポーツは、アジア大会20でさらに銅メダルを獲得するという任務を完了しました。",
  "snippet": "",
  "published": "2026-10-01T07:07:10+00:00"
 },
 {
  "id": "d2e6a405d408",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "アジア競技大会ライブ中継 10月1日：セパタクローがグループリーグ全3試合に勝利。eスポーツが銅メダルを獲得。",
  "snippet": "",
  "published": "2026-10-01T12:39:47+00:00"
 },
 {
  "id": "94bb7587e562",
  "region": "jp",
  "source": "YouTube",
  "title": "[CHAINSAW BLOOD･10/8&10/29]反転柔術式208外伝1359",
  "snippet": "",
  "published": "2026-09-30T16:41:15+00:00"
 },
 {
  "id": "25131833e09b",
  "region": "jp",
  "source": "Laodong.vn",
  "title": "本日(10月2日)の第20回アジア競技大会でのベトナム代表団の試合を生中継",
  "snippet": "",
  "published": "2026-10-02T00:05:00+00:00"
 },
 {
  "id": "8201be6c6887",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "ベトナムとブラジルのスポーツ協力関係の強化",
  "snippet": "",
  "published": "2026-10-01T01:14:51+00:00"
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
  "id": "ccaad092e16c",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "2026年アジア競技大会、10月1日：ベトナムのスポーツ界には多くのメダル獲得のチャンスが待っている。",
  "snippet": "",
  "published": "2026-10-01T00:59:46+00:00"
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
  "id": "59355d655b72",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "50代になっても「若い頃と同じ頑張り方」をする人が、うまくいかなくなる理由（ダイヤモンド・オンライン）",
  "snippet": "",
  "published": "2026-10-01T22:39:45+00:00"
 },
 {
  "id": "7eb6f358808d",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "体重５０キロ台力士で注目の新道が相撲教習所入所「序ノ口で勝ち越したい」九州場所へ闘志【大相撲】",
  "snippet": "",
  "published": "2026-10-01T08:37:30+00:00"
 },
 {
  "id": "d0c19e81a6b9",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月2日から10日まで開催される第20回アジア競技大会におけるベトナムスポーツ代表団のスケジュール。",
  "snippet": "",
  "published": "2026-10-01T23:56:08+00:00"
 },
 {
  "id": "c79b0f9d0971",
  "region": "jp",
  "source": "Goal.com",
  "title": "【10月1日】アジア大会の地上波TBS・ネットU-NEXT中継予定",
  "snippet": "",
  "published": "2026-09-30T21:00:00+00:00"
 },
 {
  "id": "320fa0290a2a",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "2026年アジア競技大会、10月2日：ボクシングの金メダル獲得への期待は高く、女子セパタクローは決勝進出を目指す。",
  "snippet": "",
  "published": "2026-10-02T00:50:44+00:00"
 },
 {
  "id": "4c9859b2003a",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月1日のアジア競技大会のスケジュール：ダン・コン・ドゥック選手はアーチェリーの準々決勝、リーグ・オブ・レジェンドの準決勝に出場します。",
  "snippet": "",
  "published": "2026-10-01T02:41:19+00:00"
 },
 {
  "id": "00e534be0e17",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "本日、グエン・ティ・タムはオリンピックチャンピオンと金メダルをかけて競い合います。",
  "snippet": "",
  "published": "2026-10-01T22:43:59+00:00"
 },
 {
  "id": "f2a1455ec799",
  "region": "jp",
  "source": "Goal.com",
  "title": "【番組表】アジア大会2026全競技のテレビ放送・地上波中継・ネット配信予定",
  "snippet": "",
  "published": "2026-10-01T13:22:52+00:00"
 },
 {
  "id": "ebf462338665",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月1日時点のアジア競技大会20のメダル順位：eスポーツが銅メダルを獲得、セパタクローも素晴らしいパフォーマンスを見せた。",
  "snippet": "",
  "published": "2026-10-01T14:34:29+00:00"
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
  "id": "e4d7409cfd29",
  "region": "jp",
  "source": "YouTube",
  "title": "ドンマイ川端さんと岩崎正寛さんに小内刈を教えてもらったよ",
  "snippet": "",
  "published": "2026-10-01T12:43:56+00:00"
 },
 {
  "id": "cc7e7473afbf",
  "region": "jp",
  "source": "news.nicovideo.jp",
  "title": "【RIZIN】芦澤竜誠、4連敗から復活へ 対戦相手に助言も「操られたピエロになるな。自分の意志で生きて」",
  "snippet": "",
  "published": "2026-10-01T05:09:27+00:00"
 },
 {
  "id": "f359eae75589",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【RIZIN】BDで屈辱の敗戦から7カ月、芦澤竜誠「死んでも負けたくないって言ってたんですけど、今は必死で頑張りたい」井上の挑発には「言わされてるから台本があるんじゃないですか」",
  "snippet": "",
  "published": "2026-10-01T09:10:00+00:00"
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
  "id": "4715049a39e6",
  "region": "intl",
  "source": "The Vacaville Reporter",
  "title": "Vacaville man, former Vanden wrestler, wins jiu-jitsu championship",
  "snippet": "",
  "published": "2026-10-01T22:57:07+00:00"
 },
 {
  "id": "a49e0c6efa8d",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship - Videos",
  "snippet": "",
  "published": "2026-10-02T00:07:56+00:00"
 },
 {
  "id": "ee66315cd922",
  "region": "intl",
  "source": "holtonrecorder.net",
  "title": "Holton native Binkley earns jiu jitsu championship",
  "snippet": "",
  "published": "2026-10-01T14:20:33+00:00"
 },
 {
  "id": "ebedc95bca4f",
  "region": "intl",
  "source": "shafaq.com",
  "title": "Shafaq News..Iraqi competitor opens jiu-jitsu campaign",
  "snippet": "",
  "published": "2026-10-01T23:02:14+00:00"
 },
 {
  "id": "df05eed00945",
  "region": "intl",
  "source": "Idaho State Journal",
  "title": "Asian Games Jiu-Jitsu",
  "snippet": "",
  "published": "2026-10-01T09:53:55+00:00"
 },
 {
  "id": "257c8031ed84",
  "region": "intl",
  "source": "Community Impact Newspaper",
  "title": "Gracie Barra Brazilian jiu-jitsu academy to open in Liberty Hill",
  "snippet": "",
  "published": "2026-10-01T01:53:59+00:00"
 },
 {
  "id": "bf72d59472f6",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Watch Jiu-Jitsu",
  "snippet": "",
  "published": "2026-10-01T09:31:30+00:00"
 },
 {
  "id": "6971e7bbde3b",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan Kids Jiu-Jitsu IBJJF Championship",
  "snippet": "",
  "published": "2026-10-01T02:31:58+00:00"
 },
 {
  "id": "7fa18e34ca8d",
  "region": "intl",
  "source": "facebook.com",
  "title": "World champion jiu-jitsu Kimberly Custodio made an early exit at the 20th Asian Games after bowing to to the United Arab Emirates’ Balqees Abdulla in the round-of-16 of the women's -48kg class. See comments section for the full story.",
  "snippet": "",
  "published": "2026-10-01T14:45:03+00:00"
 },
 {
  "id": "12a98ace14dd",
  "region": "intl",
  "source": "Qazinform",
  "title": "Nurzhan Batyrbekov wins Asian Games jiu-jitsu silver",
  "snippet": "",
  "published": "2026-10-01T08:45:23+00:00"
 },
 {
  "id": "dfc606043405",
  "region": "intl",
  "source": "Sportscape Magazine",
  "title": "WATCH: “No Time for Pictures!” UFC BJJ Hypes Adele Fornarino vs. Cassia Moura Title Clash",
  "snippet": "",
  "published": "2026-10-01T19:25:34+00:00"
 },
 {
  "id": "e601e86e848a",
  "region": "intl",
  "source": "ABS-CBN",
  "title": "Asiad: World champ Custodio bows out in rough start for PH jiu-jitsu",
  "snippet": "",
  "published": "2026-10-01T22:29:00+00:00"
 },
 {
  "id": "0c848d6f1b1f",
  "region": "intl",
  "source": "thenationalnews.com",
  "title": "UAE win three Asian Games gold medals in jiu-jitsu",
  "snippet": "",
  "published": "2026-10-01T08:42:03+00:00"
 },
 {
  "id": "20bdf20bc716",
  "region": "intl",
  "source": "FloGrappling",
  "title": "The Black Belt Brackets Are Out For The IBJJF No-Gi Pan Championship",
  "snippet": "",
  "published": "2026-09-30T21:13:22+00:00"
 },
 {
  "id": "9358b8b1c851",
  "region": "intl",
  "source": "uaebarq.ae",
  "title": "UAE wins three golds, two silvers in jiu-jitsu at Aichi-Nagoya Asian Games",
  "snippet": "",
  "published": "2026-10-01T16:44:20+00:00"
 },
 {
  "id": "aacc7463456b",
  "region": "intl",
  "source": "atlaspress.news",
  "title": "Afghanistan’s Jiu-Jitsu Athlete Reaches Asian Games Quarter-Finals",
  "snippet": "",
  "published": "2026-10-01T08:20:16+00:00"
 },
 {
  "id": "50d3d98336ef",
  "region": "intl",
  "source": "Sharjah24",
  "title": "UAE jiu-jitsu wins five medals in single day at Asian Games",
  "snippet": "",
  "published": "2026-10-01T19:56:55+00:00"
 },
 {
  "id": "3894676980e2",
  "region": "intl",
  "source": "Dubai Eye 103.8",
  "title": "UAE wins three jiu-jitsu golds, two silvers at Asian Games",
  "snippet": "",
  "published": "2026-10-01T12:55:43+00:00"
 },
 {
  "id": "69698425bfed",
  "region": "intl",
  "source": "Gulf News",
  "title": "UAE claim three jiu-jitsu golds at Asian Games",
  "snippet": "",
  "published": "2026-10-01T08:11:52+00:00"
 },
 {
  "id": "0bb2e8cace4e",
  "region": "intl",
  "source": "Sportscape Magazine",
  "title": "WATCH: Charles Oliveira Hilariously Reacts to ‘Purple Belt Syndrome’ in New BJJ Skit",
  "snippet": "",
  "published": "2026-09-30T19:49:35+00:00"
 },
 {
  "id": "9ebef23e07b8",
  "region": "intl",
  "source": "SPIN.ph: Sports Interactive Network Philippines",
  "title": "World champion Custodio ousted in first day of Asiad jiu-jitsu",
  "snippet": "",
  "published": "2026-10-01T08:29:39+00:00"
 },
 {
  "id": "548df8f4e765",
  "region": "intl",
  "source": "thenationalnews.com",
  "title": "UAE win a record six medals including three golds at Asian Games",
  "snippet": "",
  "published": "2026-10-01T10:56:52+00:00"
 },
 {
  "id": "dc0ffa5feb9c",
  "region": "intl",
  "source": "boxingnews.com",
  "title": "UFC BJJ 12: Moura vs Fornarino — Full Card, Start Time & How to Watch",
  "snippet": "",
  "published": "2026-09-30T17:46:32+00:00"
 },
 {
  "id": "9da9c73376be",
  "region": "intl",
  "source": "Mindanao Gold Star Daily",
  "title": "Mindanao jiu-jitsu team brings home 29 medals",
  "snippet": "",
  "published": "2026-10-01T06:59:04+00:00"
 },
 {
  "id": "7e1fedad7ee4",
  "region": "intl",
  "source": "News of Bahrain",
  "title": "UAE Claim 3 Jiu-Jitsu Golds At Asian Games",
  "snippet": "",
  "published": "2026-10-01T09:00:43+00:00"
 },
 {
  "id": "abd9247bef47",
  "region": "intl",
  "source": "BJJEE",
  "title": "Mikey Musumeci Says PED Use In Jiu-Jitsu Has Him Ready To “Transfer” To MMA",
  "snippet": "Mikey Musumeci has reached a breaking point with PED use in Brazilian Jiu-Jitsu, and his recent win over Bryce Mitchell at UFC BJJ 11 may end up being one of his final traditional grappling matches because of it. The five-time IBJJF world champion and reigning UFC bantamweight grappling champion opened up about his frustration during a recent appearance on The Ariel Helwani Show. Asked about the issue, he didn’t soften his response: Nothing’s gotten better in this sport, you know? So, it’s just very discouraging for me to continue in a sport that nothing’s gotten better. Musumeci pointed to th…",
  "published": "2026-10-01T08:00:55+00:00"
 },
 {
  "id": "958db40a40e2",
  "region": "intl",
  "source": "BJJEE",
  "title": "Claudia Gadelha Questions UFC BJJ’s Policy On Minors After 17-Year-Old Suffers Arm Break",
  "snippet": "A gruesome arm injury suffered by a 17-year-old competitor at UFC BJJ 11 has sparked a serious conversation about athlete safety within the organization… With Claudia Gadelha now questioning whether minors should be competing at the professional level at all. Speaking at the post-event press conference, Gadelha didn’t hold back her reaction to the injury sustained by Kolby Gonzales: It was nasty. I felt physically sick with that arm breaking. I felt like the submission was there. I didn’t think that Kolby Gonzales wouldn’t tap and he didn’t tap. He showed how tough he is and he’s so young. I t…",
  "published": "2026-10-01T07:55:34+00:00"
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
