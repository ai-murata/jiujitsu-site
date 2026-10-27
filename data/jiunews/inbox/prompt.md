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
  "id": "32a942292747",
  "region": "jp",
  "source": "Excite エキサイト",
  "title": "世界大会3位の柔術家が奈良・生駒に新ジムをオープン！SPINS BJJ が新規生徒を募集",
  "snippet": "",
  "published": "2026-10-26T02:10:00+00:00"
 },
 {
  "id": "7b5e8121081c",
  "region": "jp",
  "source": "au Webポータル",
  "title": "上白石萌音、映画撮影中“勧誘”してきた俳優を告白「萌音ちゃんまで勧誘したの？笑」「ノリいいから」",
  "snippet": "",
  "published": "2026-10-26T22:37:30+00:00"
 },
 {
  "id": "a2ce0ad9d3cf",
  "region": "jp",
  "source": "Infoseek",
  "title": "角田夏実さん 寝技極めたきっかけは“休日の柔道場”「私もそれに参加させてもらいたいって」",
  "snippet": "",
  "published": "2026-10-26T07:50:01+00:00"
 },
 {
  "id": "13f33399daee",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "武道への情熱を育む場所。",
  "snippet": "",
  "published": "2026-10-26T05:58:59+00:00"
 },
 {
  "id": "2367615ce5a3",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "「容赦しない」高須克弥氏 堀大輔氏の息子・幹弥氏への”ぶっ殺せる”発言にブチ切れ…堀氏は一歩も引かぬ泥沼展開",
  "snippet": "",
  "published": "2026-10-26T10:10:48+00:00"
 },
 {
  "id": "2943c4512a64",
  "region": "jp",
  "source": "매일경제",
  "title": "［毎日放送（MBN）］「男らしい男」チュ・ソンフンの台湾紀行",
  "snippet": "",
  "published": "2026-10-26T08:09:44+00:00"
 },
 {
  "id": "341b29d1d69c",
  "region": "jp",
  "source": "Laodong.vn",
  "title": "2026年全国スポーツ大会組織委員会、ドーピング検査を強化",
  "snippet": "",
  "published": "2026-10-26T12:29:56+00:00"
 },
 {
  "id": "e13b4846c50a",
  "region": "jp",
  "source": "coki",
  "title": "高須克弥、堀大輔「高須幹弥をぶっ殺せる」に再警告 「もう高須に絡まないでくれ」",
  "snippet": "",
  "published": "2026-10-25T19:46:30+00:00"
 },
 {
  "id": "713709f6312a",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "世界大会3位の柔術家が奈良・生駒に新ジムをオープン！SPINS BJJ が新規生徒を募集 (2026年10月26日掲載)",
  "snippet": "",
  "published": "2026-10-26T03:51:14+00:00"
 },
 {
  "id": "a884d20974d0",
  "region": "jp",
  "source": "https://mediadogs.jp/",
  "title": "高須幹弥氏、堀大輔氏の発言に動画で説明 柔術なら応じる考え",
  "snippet": "",
  "published": "2026-10-26T01:26:01+00:00"
 },
 {
  "id": "ee269c56650d",
  "region": "jp",
  "source": "매일경제",
  "title": "忠清北道清州市のオリンパスアリーナでは10月24日土曜日、総合格闘技(MMA)大会のゼウスFC17が開かれた。 メインカード8試合とアンダーカード6試合で計14試合規模だ。「大韓民国UFC22号ファイ..",
  "snippet": "",
  "published": "2026-10-26T14:29:20+00:00"
 },
 {
  "id": "53e277a1e0aa",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "初代『トゥームレイダー』を再構築したゲーム『トゥームレイダー：レガシー・オブ・アトランティス』の最新映像が公開。シリー",
  "snippet": "",
  "published": "2026-10-25T23:24:24+00:00"
 },
 {
  "id": "a4ec864dce96",
  "region": "intl",
  "source": "The New York Times",
  "title": "Why the world is falling in love with Brazilian jiu-jitsu - The Athletic",
  "snippet": "",
  "published": "2026-10-26T15:13:07+00:00"
 },
 {
  "id": "4ecf29934ff4",
  "region": "intl",
  "source": "Facebook",
  "title": "From The Athletic: Brazilian jiu-jitsu is soaring in popularity globally. \"It’s grown massively in terms of numbers, particularly with women, but also in pop culture with numerous celebrities taking part.\" https://nyti.ms/4dYQEQW",
  "snippet": "",
  "published": "2026-10-27T00:15:31+00:00"
 },
 {
  "id": "eb0f020ef1c3",
  "region": "intl",
  "source": "AL.com",
  "title": "This sport rising in popularity in US and abroad",
  "snippet": "",
  "published": "2026-10-26T15:43:00+00:00"
 },
 {
  "id": "6c16d3102d84",
  "region": "intl",
  "source": "MMA Fighting",
  "title": "BJJ wiz Kade Ruotolo draws former MMA champion in ONE return",
  "snippet": "",
  "published": "2026-10-26T12:45:15+00:00"
 },
 {
  "id": "1a3c02733155",
  "region": "intl",
  "source": "The Owensboro Times",
  "title": "FUJI Brazilian Jiu-Jitsu Competition coming to Owensboro",
  "snippet": "",
  "published": "2026-10-26T05:17:11+00:00"
 },
 {
  "id": "e2842187ef44",
  "region": "intl",
  "source": "Forces News",
  "title": "Grappling their way to glory: Royal Navy BJJ named Navy Team of the Year",
  "snippet": "",
  "published": "2026-10-26T12:31:41+00:00"
 },
 {
  "id": "78ca783532f9",
  "region": "intl",
  "source": "DVIDS",
  "title": "Images - U.S. Reconnaissance Marines Conduct Jujitsu and Live Fire Range with Korea Coast Guard",
  "snippet": "",
  "published": "2026-10-26T06:02:00+00:00"
 },
 {
  "id": "1a1eb5b522b3",
  "region": "intl",
  "source": "Noosa Today",
  "title": "Taking on the world",
  "snippet": "",
  "published": "2026-10-26T20:00:04+00:00"
 },
 {
  "id": "c60bcde0f2d2",
  "region": "intl",
  "source": "Colac Herald",
  "title": "Ebeyer celebrates golden return",
  "snippet": "",
  "published": "2026-10-26T18:59:00+00:00"
 },
 {
  "id": "54945429e4ad",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Marlon Tajik Ranks The Best Kits From ADCC | The FloGrappling Show (Ep 110)",
  "snippet": "",
  "published": "2026-10-26T16:03:54+00:00"
 },
 {
  "id": "d6fe1f628dd2",
  "region": "intl",
  "source": "TMZ",
  "title": "Gisele Bündchen Doesn't See Candice Swanepoel's Tom Brady Romance as Betrayal",
  "snippet": "",
  "published": "2026-10-26T23:50:02+00:00"
 },
 {
  "id": "98e24ceb0209",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Steven Ortiz vs Kingston Quartuccio 2026 ADCC Nashville Open",
  "snippet": "",
  "published": "2026-10-26T06:06:19+00:00"
 },
 {
  "id": "8945c2ac793f",
  "region": "intl",
  "source": "NivervilleOnline",
  "title": "Niverville's up to date election day coverage on NivervilleOnline",
  "snippet": "",
  "published": "2026-10-26T09:09:12+00:00"
 },
 {
  "id": "d094ca68c693",
  "region": "intl",
  "source": "매일경제",
  "title": "[MBN] Choo Sung-hoon, the “tough guy,” on a trip to Taiwan",
  "snippet": "",
  "published": "2026-10-26T08:09:44+00:00"
 },
 {
  "id": "1b814240a0ea",
  "region": "intl",
  "source": "Sharjah24",
  "title": "Al Hamriyah wins 14 medals as Al Shehi sets new record",
  "snippet": "",
  "published": "2026-10-25T17:19:33+00:00"
 },
 {
  "id": "626aa7a69dc0",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "Windows Announce Landmark Partnership With Ruotolo Brothers",
  "snippet": "",
  "published": "2026-10-26T16:29:35+00:00"
 },
 {
  "id": "c913f12a4a44",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Gavin Corbe Won An ADCC Silver Medal - Yet His Training Regimen Is Nothing Like The Other Athletes",
  "snippet": "",
  "published": "2026-10-26T14:06:49+00:00"
 },
 {
  "id": "d1d72da4b900",
  "region": "intl",
  "source": "BJJDOC",
  "title": "John Danaher: Athlete’s Confidence Comes From Physicality Not From Visualization",
  "snippet": "",
  "published": "2026-10-26T09:33:37+00:00"
 },
 {
  "id": "74b5575fe8a8",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Kade Ruotolo Faces Former ONE MMA Champion on Dec. 18",
  "snippet": "",
  "published": "2026-10-26T16:32:37+00:00"
 },
 {
  "id": "4057d0fac68a",
  "region": "intl",
  "source": "The Babylon Bee",
  "title": "After Late-Night Ballot Drop, Joe Biden Wins Brazilian Presidency With 81 Million Votes",
  "snippet": "",
  "published": "2026-10-26T15:48:24+00:00"
 },
 {
  "id": "3a2bf1d3ed3d",
  "region": "intl",
  "source": "BJJEE",
  "title": "Arman Tsarukyan Calls For A Georges St-Pierre Match: “I’d Like To Wrestle Him”",
  "snippet": "Arman Tsarukyan has long chased UFC gold, and he now has a new target in RAF: Georges St-Pierre. The newly crowned RAF middleweight crossover champion spoke to the media after beating Dillon Danis in a lopsided main event on Friday in Las Vegas, and laid out his plans with a title around his waist. He wants more marquee names from MMA to cross over, including the long-retired GSP: We’ve got a lot of names here, but I’m focusing on MMA fighters with the big names. I don’t want to just wrestle with no names, I want to collect all big names, all the best fighters, so a lot of UFC fighters, good f…",
  "published": "2026-10-26T06:52:25+00:00"
 },
 {
  "id": "addb90922e89",
  "region": "intl",
  "source": "BJJEE",
  "title": "Rafael Lovato Jr. Warns Against Gym Hopping: “Another Fly On The Wall”",
  "snippet": "Rafael Lovato Jr. believes that athletes who bounce between gyms risk their careers and their personal growth. The multiple-time world champion and MMA veteran made the case in a recent conversation, responding to the trend of fighters relocating to mega gyms: I don’t believe it’s necessary to completely change locations and change training partners and all of that. Lovato built his career in Oklahoma, far from the traditional martial arts hubs, by keeping a home base and adding outside training on purpose. He has also brought top instructors to his academy, including Leandro Lo and Lucas Lepr…",
  "published": "2026-10-26T06:51:25+00:00"
 },
 {
  "id": "e05b85321d25",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "Windows Announces Landmark Partnership With Ruotolo Brothers",
  "snippet": "The worlds of technology and Brazilian Jiu-Jitsu have come together in a high-profile collaboration featuring both Kade Ruotolo and Tye Ruotolo , as Microsoft’s Windows brand puts the celebrated grappling twins at the centre of a new campaign. Titled Iron Sharpens Iron – Training and Surfing with Kade and Tye Ruotolo , the film showcases the brothers’ lives beyond competition, following their training routines, preparation and passion for surfing. Released through Windows’ official social media channels in early October 2026, the project presents a different perspective on two athletes who hav…",
  "published": "2026-10-26T16:28:13+00:00"
 }
]
