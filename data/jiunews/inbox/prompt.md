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
  "id": "06c0148d3490",
  "region": "jp",
  "source": "中日新聞Web",
  "title": "柔術女子52キロ級、浜松市出身の鈴木清香選手敗れる 愛知・名古屋アジア大会",
  "snippet": "",
  "published": "2026-10-02T04:06:51+00:00"
 },
 {
  "id": "de65d2ac4674",
  "region": "jp",
  "source": "北海道新聞デジタル",
  "title": "書道パフォーマンスや柔術体験… お寺から 北広島盛り上げよう あすフェス 豚汁を無料提供",
  "snippet": "",
  "published": "2026-10-02T19:00:00+00:00"
 },
 {
  "id": "efc8b5aabcab",
  "region": "jp",
  "source": "アラブニュース",
  "title": "UAEのハーリド・アルシェヒがアジア大会タイトルを保持、同胞オマル・アルスワイディを破る",
  "snippet": "",
  "published": "2026-10-02T20:06:44+00:00"
 },
 {
  "id": "95cbfb014aef",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "本日（10月3日）のアジア競技大会スケジュール：セパタクロー金メダル決定戦。",
  "snippet": "",
  "published": "2026-10-02T17:09:06+00:00"
 },
 {
  "id": "13b24c5fb8d0",
  "region": "jp",
  "source": "YouTube",
  "title": "アジア大会柔術競技初日終了。失われた10年…？？厳しい…されど頑張れ若者よ！",
  "snippet": "",
  "published": "2026-10-01T16:44:45+00:00"
 },
 {
  "id": "dce6b2bff567",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月2日のアジア競技大会のスケジュール：グエン・ティ・タム選手がボクシングで金メダルを目指して競技に臨む。",
  "snippet": "",
  "published": "2026-10-02T04:38:48+00:00"
 },
 {
  "id": "cf30348d2e02",
  "region": "jp",
  "source": "読売新聞",
  "title": "柔術 女子48キロ級 試合結果・記録 アジア競技大会2026 愛知・名古屋",
  "snippet": "",
  "published": "2026-10-01T13:09:00+00:00"
 },
 {
  "id": "d9c4cbc824e2",
  "region": "jp",
  "source": "olympics.com",
  "title": "【アジア競技大会2026】10月3日の見どころ｜日本代表・主な出場選手・開始時間・放送配信予定",
  "snippet": "",
  "published": "2026-10-02T16:37:00+00:00"
 },
 {
  "id": "b89abb165d18",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月3日から10日まで開催される第20回アジア競技大会におけるベトナムスポーツ代表団のスケジュール。",
  "snippet": "",
  "published": "2026-10-02T23:54:32+00:00"
 },
 {
  "id": "20f8befeed55",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "ジゼル・ブンチェンの家族は、彼女の新しい夫が「無一文」であることに強く反対している。",
  "snippet": "",
  "published": "2026-10-02T09:30:08+00:00"
 },
 {
  "id": "886c624ce3e2",
  "region": "jp",
  "source": "Goal.com",
  "title": "【10月2日】アジア大会2026の地上波TBS・U-NEXTネット中継予定",
  "snippet": "",
  "published": "2026-10-02T09:53:01+00:00"
 },
 {
  "id": "4a527e7abf67",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "富士市出身の山本泰輝選手敗れる アジア大会レスリング男子フリースタイル125キロ級敗者復活戦",
  "snippet": "",
  "published": "2026-10-02T05:19:00+00:00"
 },
 {
  "id": "c27792d15b58",
  "region": "jp",
  "source": "Goal.com",
  "title": "全競技スケジュール・日程｜第20回アジア大会",
  "snippet": "",
  "published": "2026-10-02T14:24:10+00:00"
 },
 {
  "id": "e5f2e51fcc69",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "水上スキーの技を競う 湖西市のボートレース浜名湖で静岡県選手権",
  "snippet": "",
  "published": "2026-10-01T20:05:00+00:00"
 },
 {
  "id": "4c47ca24cea6",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "かまいたち濱家＆間宮祥太朗＆森本慎太郎、冠番組『濱太郎』開店 ゲストは玉木宏＆桐谷健太",
  "snippet": "",
  "published": "2026-10-02T21:00:19+00:00"
 },
 {
  "id": "6f0bae30fb8a",
  "region": "jp",
  "source": "Laodong.vn",
  "title": "本日(10月3日)の第20回アジア競技大会に出場するベトナム代表団の生中継",
  "snippet": "",
  "published": "2026-10-02T23:54:58+00:00"
 },
 {
  "id": "85fbbd0e3f6c",
  "region": "jp",
  "source": "efight.jp",
  "title": "“野球歴20年超”グラドル、91cm“捕手の桃尻”で写真集「キャッチャーの安定感」",
  "snippet": "",
  "published": "2026-10-01T23:39:00+00:00"
 },
 {
  "id": "c3a08c7d2466",
  "region": "jp",
  "source": "ぐぐスポ！",
  "title": "【柔術】アジア大会2026 日本代表の結果速報・日程・組み合わせ・放送予定",
  "snippet": "",
  "published": "2026-10-01T15:17:28+00:00"
 },
 {
  "id": "52d694c1bfcd",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "【399円】『モンスターハンターライズ』がSteamで90%オフで購入できるセールが開催中！超大型DLC『サンブレイク",
  "snippet": "",
  "published": "2026-10-02T01:45:20+00:00"
 },
 {
  "id": "e48a764a8bec",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T22:45:39+00:00"
 },
 {
  "id": "fe1fdb9da1c3",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Matthew Smajlaj vs Declain 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T19:55:25+00:00"
 },
 {
  "id": "2cdc06972569",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Aileen Tsai vs Keren Laura Furrow 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T17:58:46+00:00"
 },
 {
  "id": "0b22a21786ec",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Jordan A Quidachay vs Sean Michael Fitzpatrick 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T20:29:29+00:00"
 },
 {
  "id": "665c93a8e203",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Continue Watching",
  "snippet": "",
  "published": "2026-10-02T17:25:08+00:00"
 },
 {
  "id": "686786ae4cf1",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Featured",
  "snippet": "",
  "published": "2026-10-02T14:52:41+00:00"
 },
 {
  "id": "71a6525244bb",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Joshua Cade Reynolds vs Caleb Wayne Spears 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T13:49:20+00:00"
 },
 {
  "id": "472032797427",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Pedigo Submission Fighting",
  "snippet": "",
  "published": "2026-10-02T19:16:58+00:00"
 },
 {
  "id": "d42236ab72ea",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Lukas Andrew Hernandez vs James Landon Weaver 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T13:01:38+00:00"
 },
 {
  "id": "066080afdb4f",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Jace Christian Abrahamsson vs David Richard Ribeiro Da Silva 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T16:29:49+00:00"
 },
 {
  "id": "e457ee1640ee",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T16:29:48+00:00"
 },
 {
  "id": "72bfd5437795",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Keith-Khalif Lanier Henry Jr. vs Ethan E B Schwartz 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T13:58:37+00:00"
 },
 {
  "id": "004a10857dbd",
  "region": "intl",
  "source": "The Korea Times",
  "title": "S. Korea wins two silvers, two bronzes in jiu-jitsu",
  "snippet": "",
  "published": "2026-10-02T07:58:02+00:00"
 },
 {
  "id": "fb79086de815",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Euclides Ferreira De Castro",
  "snippet": "",
  "published": "2026-10-02T06:03:21+00:00"
 },
 {
  "id": "2d8be99278aa",
  "region": "intl",
  "source": "Khaosod English",
  "title": "Nuchanat wins bronze as Thailand adds second jiu-jitsu medal",
  "snippet": "",
  "published": "2026-10-02T08:10:24+00:00"
 },
 {
  "id": "31eb50ce6034",
  "region": "intl",
  "source": "Dubai Eye 103.8",
  "title": "UAE wins 2 jiu-jitsu golds, one bronze at Asian Games",
  "snippet": "",
  "published": "2026-10-02T22:51:07+00:00"
 },
 {
  "id": "a432b7ab23ae",
  "region": "intl",
  "source": "thenationalnews.com",
  "title": "UAE clinch seventh Asian Games gold as jiu-jitsu contingent shines",
  "snippet": "",
  "published": "2026-10-02T08:00:54+00:00"
 },
 {
  "id": "ceddfe42aa61",
  "region": "intl",
  "source": "ABS-CBN",
  "title": "World champ Annie Ramirez makes early exit as woes continue for PH jiu jitsu in Asiad",
  "snippet": "",
  "published": "2026-10-02T20:18:51+00:00"
 },
 {
  "id": "0447035253c2",
  "region": "intl",
  "source": "manilastandard.net",
  "title": "Napolis fights back to claim Jiu-Jitsu bronze",
  "snippet": "",
  "published": "2026-10-02T16:15:11+00:00"
 },
 {
  "id": "d414d826047d",
  "region": "intl",
  "source": "Seoul Economic Daily",
  "title": "Korea Takes Two Jiu-Jitsu Silvers in Nagoya",
  "snippet": "",
  "published": "2026-10-02T08:42:09+00:00"
 },
 {
  "id": "949963def4d6",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Kassidy Hong Tran vs Aubree Annalynn Celis 2026 IBJJF Jiu-Jitsu CON International - FloGrappling - Grappling",
  "snippet": "",
  "published": "2026-10-01T15:57:01+00:00"
 },
 {
  "id": "de3e0e7fb1ce",
  "region": "intl",
  "source": "sports.inquirer.net",
  "title": "Asian Games: Kaila Napolis repeats as jiu jitsu bronze medalist",
  "snippet": "",
  "published": "2026-10-02T08:51:00+00:00"
 },
 {
  "id": "2ee3d4a7fcc0",
  "region": "intl",
  "source": "facebook.com",
  "title": "KAILA ROLLS TO BRONZE 🥉 Kaila Napolis captures bronze in jiu jitsu women’s -52kg with a 2-0 win over Mongolia's Tsagaanbileg Altangerel. Napolis, who also won bronze in the 2022 Asiad, is the first jiu jitsu athlete to win a medal in the 2026 Asian Games",
  "snippet": "",
  "published": "2026-10-02T06:48:18+00:00"
 },
 {
  "id": "eda49a366ab3",
  "region": "intl",
  "source": "GulfToday",
  "title": "UAE Jiu-Jitsu National Team wins two more gold medals at Asian Games, tally rises to 8",
  "snippet": "",
  "published": "2026-10-02T12:16:34+00:00"
 },
 {
  "id": "d774557d4694",
  "region": "intl",
  "source": "Sharjah24",
  "title": "UAE Jiu-Jitsu team wins two golds at Asian Games",
  "snippet": "",
  "published": "2026-10-02T13:02:31+00:00"
 },
 {
  "id": "d2bf0a9ee983",
  "region": "intl",
  "source": "BJJEE",
  "title": "BJJ Black Belt With Massive Online Following Joins OnlyFans",
  "snippet": "Brazilian Jiu-Jitsu black belt Giovanna “Ghi” Eburneo is making headlines beyond the mats after joining OnlyFans, adding her name to a growing list of BJJ athletes exploring subscription-based content platforms. With more than 570,000 Instagram followers and a subscription price of $17.99 per month , the Brazilian grappler has another way to monetize the audience she has built through Jiu-Jitsu, professional wrestling and social media. But Eburneo is far from being just another Instagram personality. A Legitimate BJJ Black Belt Who Made It to WWE Before building her massive social media follow…",
  "published": "2026-10-02T10:23:22+00:00"
 },
 {
  "id": "32b436b65cfa",
  "region": "intl",
  "source": "BJJEE",
  "title": "Researcher Finds Translator Erased References To The Gracie Family From Book On Mitsuyo Maeda",
  "snippet": "The history of Brazilian Jiu-Jitsu is full of disputed narratives, but one recent discovery stands out for what it reveals about how that history has been handled over time. According to martial arts researcher Gustavo Maçaneiro, a Japanese translator appears to have deliberately removed references to the Gracie family from a book about Mitsuyo Maeda, the judoka widely credited with introducing judo to Brazil. The book in question is the third volume of a series documenting Maeda’s travels, compiled from letters and telegrams he sent to a friend in Japan and published shortly after his death i…",
  "published": "2026-10-02T06:45:33+00:00"
 },
 {
  "id": "77f4b317861d",
  "region": "intl",
  "source": "BJJEE",
  "title": "ADCC Silver Medalist Marlon Tajik Opens Up On Faking His Age To Compete As A Teen",
  "snippet": "Marlon Tajik’s path to becoming an ADCC silver medalist includes an unusual chapter from his teenage years – a one-year competition ban in Sweden after he falsified his age to face tougher opponents. Tajik began training traditional Japanese Jiu-Jitsu at age seven before switching to Brazilian Jiu-Jitsu around 11. By 14, he’d already run out of real competition locally, repeatedly beating the same opponents in his age bracket even after six-hour drives to tournaments. Rather than accept that, he and his father decided he’d compete as a juvenile against 16- and 17-year-olds instead of his actua…",
  "published": "2026-10-02T06:41:06+00:00"
 }
]
