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
  "id": "c6a83f286ade",
  "region": "jp",
  "source": "アラブニュース",
  "title": "アブダビでのハリード・ビン・ムハンマド・ビン・ザイード柔術選手権でシーズンタイトルがかかる",
  "snippet": "",
  "published": "2026-10-14T20:07:02+00:00"
 },
 {
  "id": "efe9a69d6588",
  "region": "jp",
  "source": "Excite エキサイト",
  "title": "【開催レポート】クレベル・コイケ選手による特別柔術クラスを開催！渋谷アカデミーにて。ボンサイファミリーの絆を深める一日に",
  "snippet": "",
  "published": "2026-10-15T06:15:00+00:00"
 },
 {
  "id": "965770eb083d",
  "region": "jp",
  "source": "Dellows News",
  "title": "ボンサイ柔術渋谷アカデミーがクレベル・コイケ選手の特別柔術クラスを開催",
  "snippet": "",
  "published": "2026-10-15T06:17:25+00:00"
 },
 {
  "id": "b0342683b3af",
  "region": "jp",
  "source": "매일경제",
  "title": "■ ユ·スヨン、カナダのエドモントン遠征で無敗の有望株チョバンセックを相手に218日ぶりの再起戦出撃",
  "snippet": "",
  "published": "2026-10-15T22:31:28+00:00"
 },
 {
  "id": "c2de5019001c",
  "region": "jp",
  "source": "BOUTREVIEW",
  "title": "ROMAN 11.14 大田区産業プラザPiO：関根“シュレック”秀樹と田馬場貴裕が台湾の選手とバーリトゥード戦。白木大輔×ボグダノフ、井上智裕×西願寺哲平の組技戦も",
  "snippet": "",
  "published": "2026-10-15T03:30:45+00:00"
 },
 {
  "id": "4286c1b75912",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【RIZIN甲子園】12名→8名。「4名脱落」の非情のセレクション試合をいかに戦ったか？ 10月17日（土）「準決勝トーナメント」進出者決まる！",
  "snippet": "",
  "published": "2026-10-15T03:41:01+00:00"
 },
 {
  "id": "1b8399d394a1",
  "region": "jp",
  "source": "efight.jp",
  "title": "【ONE】平田樹、試合直前の“バキバキ腹筋”！4年7ヶ月ぶり雪辱戦へ仕上がりアピール",
  "snippet": "",
  "published": "2026-10-15T10:54:00+00:00"
 },
 {
  "id": "7227fbf89437",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE SAMURAI 4】チャトリCEO、ガリットチュウ福島vs竹浦戦の実現に当初は躊躇（オリコン）",
  "snippet": "",
  "published": "2026-10-15T03:58:34+00:00"
 },
 {
  "id": "cc1d25267289",
  "region": "jp",
  "source": "Martin Cid Magazine",
  "title": "『Tomb Raider: Legacy of Atlantis』は初代トゥームレイダーのリメイク、ララにグラップリングフック、謎解きは一から作り直し",
  "snippet": "",
  "published": "2026-10-15T09:16:28+00:00"
 },
 {
  "id": "f02d4b75ecc9",
  "region": "intl",
  "source": "Daily Freeman",
  "title": "Martial Arts: Kerr-Finell of Midtown Jiu Jitsu captures gold at New Jersey event",
  "snippet": "",
  "published": "2026-10-15T18:55:40+00:00"
 },
 {
  "id": "bc6d7c2ef7e9",
  "region": "intl",
  "source": "The Jewish Link",
  "title": "From Outsider to Community Builder: Isaac Mass on Jews of Jiu-Jitsu and Life’s Struggles on the ‘Pitch Meeting’ Podcast",
  "snippet": "",
  "published": "2026-10-15T13:06:11+00:00"
 },
 {
  "id": "139c4b9ca8ac",
  "region": "intl",
  "source": "The Guam Daily Post",
  "title": "Purebred excels in Påtgon jiu-jitsu competition",
  "snippet": "",
  "published": "2026-10-15T07:19:06+00:00"
 },
 {
  "id": "38c1ec7ffac1",
  "region": "intl",
  "source": "Sonic Perspectives",
  "title": "Half Sumo Unveils Its First-Ever OZZY OSBOURNE Jiu-Jitsu Collection",
  "snippet": "",
  "published": "2026-10-14T22:18:54+00:00"
 },
 {
  "id": "0fb584d5ecec",
  "region": "intl",
  "source": "مكتب أبوظبي الإعلامي",
  "title": "Concluding round of Khaled bin Mohamed bin Zayed Jiu-Jitsu Championship 2026 to take place in Abu Dhabi",
  "snippet": "",
  "published": "2026-10-15T07:06:39+00:00"
 },
 {
  "id": "a85927103477",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "Abu Dhabi to host final round of Khaled bin Mohamed bin Zayed Jiu-Jitsu Championship on Friday",
  "snippet": "",
  "published": "2026-10-15T10:51:23+00:00"
 },
 {
  "id": "c05ff9266a61",
  "region": "intl",
  "source": "Swindon Advertiser",
  "title": "12-year-old Swindon boy crowned European Brazilian Jiu-Jitsu champion",
  "snippet": "",
  "published": "2026-10-15T04:00:00+00:00"
 },
 {
  "id": "04afa5dccc93",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Simple Man Martial Arts",
  "snippet": "",
  "published": "2026-10-14T17:00:00+00:00"
 },
 {
  "id": "f9700a7b5583",
  "region": "intl",
  "source": "BBC",
  "title": "Martial arts club owner jailed for raping woman at Reading studio",
  "snippet": "",
  "published": "2026-10-14T11:44:36+00:00"
 },
 {
  "id": "ec54419b0209",
  "region": "intl",
  "source": "Spin.ph",
  "title": "Asian Beach Games medalists get rewarded with cash incentives from PSC",
  "snippet": "",
  "published": "2026-10-15T11:20:45+00:00"
 },
 {
  "id": "9ab16e243828",
  "region": "intl",
  "source": "BJJDOC",
  "title": "WATCH: BJJ Blue Belt takes On A Reticulated Python",
  "snippet": "",
  "published": "2026-10-15T08:31:44+00:00"
 },
 {
  "id": "16c6ece0d0ac",
  "region": "intl",
  "source": "IndiaPost NewsPaper",
  "title": "Indian health-tech CEO Parveen Panwar wins Brazilian Jiu-Jitsu Gold after taking on a new challenge",
  "snippet": "",
  "published": "2026-10-15T09:02:51+00:00"
 },
 {
  "id": "ff5c478a1430",
  "region": "intl",
  "source": "THE SCRAP",
  "title": "Ryan Gracie: The Bad Boy of Brazilian Jiu-Jitsu",
  "snippet": "",
  "published": "2026-10-15T04:23:06+00:00"
 },
 {
  "id": "4d5a33a3842e",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Over 3,000 Athletes Set for Khaled bin Mohamed bin Zayed Jiu-Jitsu Finale",
  "snippet": "",
  "published": "2026-10-15T15:04:16+00:00"
 },
 {
  "id": "a24215e9de87",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Judo Influencer: Gordon Ryan’s Social-Media Antics Wouldn’t Be Tolerated In Judo Culture",
  "snippet": "",
  "published": "2026-10-15T11:42:58+00:00"
 },
 {
  "id": "79b9c388de92",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Sarah Galvão Returns To Defend IBJJF Crown Lightweight Title",
  "snippet": "",
  "published": "2026-10-15T13:08:57+00:00"
 },
 {
  "id": "bea58960f66b",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Kayla Harrison: Ronda Rousey Dominated Women From Cardio-Kickboxing Classes",
  "snippet": "",
  "published": "2026-10-14T13:09:30+00:00"
 },
 {
  "id": "37e48b37ab34",
  "region": "intl",
  "source": "BJJEE",
  "title": "BJJ Coach Juan Miguel Figueroa-Ball Jailed For Eight Years After SA On Free Trial Student",
  "snippet": "Juan Miguel Figueroa-Ball, a 44-year-old instructor at Ceres Brazilian Jiu-Jitsu, was sentenced to eight years in prison at Reading Crown Court on October 8 for sexually assaulting a woman who had come in for a free trial class. He had invited the woman to a complimentary one-to-one introductory session at his studio. On July 21, 2023, during what should have been a routine roll, he assaulted her. A jury found him guilty on August 25 after a six-day trial, and cleared him of a separate sexual assault charge from the same encounter. The judge also imposed a 10-year restraining order, and he wil…",
  "published": "2026-10-15T09:23:17+00:00"
 },
 {
  "id": "53bf35505503",
  "region": "intl",
  "source": "BJJEE",
  "title": "Keith Krikorian Calls Dating Bans In BJJ Gyms “Cult-Like”",
  "snippet": "Keith Krikorian says Jiu-Jitsu gyms that forbid students from dating each other are behaving like cults. He expanded on a social media take, arguing that coaches should encourage healthy relationships instead of policing the private lives of consenting adults. Krikorian met his girlfriend through a mutual friend who worked at both of their gyms: We got set up by a mutual friend… I didn’t prey on her at the gym. His case against bans is that coaches should model good behavior: Rather than a coach or a black belt just outright banning students from dating each other, I think that’s cult-like beh…",
  "published": "2026-10-15T08:29:39+00:00"
 }
]
