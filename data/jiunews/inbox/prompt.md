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
  "id": "4ae94e7ba9de",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "開会式生中継！日本初開催のアジアパラが開幕！【アジアパラ大会】",
  "snippet": "",
  "published": "2026-10-18T03:19:44+00:00"
 },
 {
  "id": "84e8b9af1878",
  "region": "jp",
  "source": "스타뉴스",
  "title": "無敗の新星？ 私に会わなかったじゃない「ユ・スヨン、コーバンチェックにサブミッション勝ち「次の相手が誰でも構わない」 [UFC]",
  "snippet": "",
  "published": "2026-10-18T07:41:22+00:00"
 },
 {
  "id": "c864aa86a743",
  "region": "jp",
  "source": "Infoseek",
  "title": "「極真王者が落とされた」16歳MMAファイター、極真王者から“悶絶”タップ「何このフィニッシュ」まさかの結末に騒然",
  "snippet": "",
  "published": "2026-10-17T11:51:00+00:00"
 },
 {
  "id": "9921e073d1ab",
  "region": "jp",
  "source": "YouTube",
  "title": "イキナリ手甲返しの真の姿は、ココにアリ…即行で極めに行く相対稽古は、ホージョードージョーの専売特許だ(笑)骨法グラップリング19 Part 8",
  "snippet": "",
  "published": "2026-10-18T10:36:29+00:00"
 },
 {
  "id": "d7e1fbdda46b",
  "region": "intl",
  "source": "The Mosh Network",
  "title": "Ozzy Osbourne Estate Teams With Half Sumo For Official Jiu-Jitsu Gear And Streetwear Collection",
  "snippet": "",
  "published": "2026-10-18T21:32:44+00:00"
 },
 {
  "id": "f4f91ef4a25d",
  "region": "intl",
  "source": "Daily Advocate",
  "title": "Local Jiu-Jitsu team brings home seven medals from World Championship",
  "snippet": "",
  "published": "2026-10-18T13:00:00+00:00"
 },
 {
  "id": "8a026049add7",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Elia Zanichelli vs Michael Roy 2026 UIJJ TRIESTE BJJ CHALLENGE",
  "snippet": "",
  "published": "2026-10-18T14:36:01+00:00"
 },
 {
  "id": "4f0693667b21",
  "region": "intl",
  "source": "Energeticcity",
  "title": "October Youth Athlete of the Month displays passion and poise on jiu-jitsu mats",
  "snippet": "",
  "published": "2026-10-18T15:16:31+00:00"
 },
 {
  "id": "54956d6dac4e",
  "region": "intl",
  "source": "Kuwait Times",
  "title": "Nine gold medals for Jiu-Jitsu Champions at AJP Championship",
  "snippet": "",
  "published": "2026-10-18T17:38:15+00:00"
 },
 {
  "id": "8e323e7ad415",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "Commando Group finishes runner-up at Abu Dhabi Grand Slam Jiu-Jitsu in Shanghai",
  "snippet": "",
  "published": "2026-10-18T18:06:52+00:00"
 },
 {
  "id": "16cee567693d",
  "region": "intl",
  "source": "مكتب أبوظبي الإعلامي",
  "title": "Zayed bin Mohamed bin Zayed attends conclusion of 3rd Khaled bin Mohamed bin Zayed Jiu-Jitsu Championship",
  "snippet": "",
  "published": "2026-10-18T18:24:28+00:00"
 },
 {
  "id": "387a39c558cb",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Sofia Camillucci vs Silvia Calabretta 2026 UIJJ TRIESTE BJJ CHALLENGE",
  "snippet": "",
  "published": "2026-10-18T09:20:12+00:00"
 },
 {
  "id": "9ff050ead5b5",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Continue Watching",
  "snippet": "",
  "published": "2026-10-18T07:24:12+00:00"
 },
 {
  "id": "2382408baf0e",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - M/W",
  "snippet": "",
  "published": "2026-10-18T00:14:49+00:00"
 },
 {
  "id": "fa79445886f8",
  "region": "intl",
  "source": "Arab Times Kuwait News",
  "title": "Kuwaiti jiu-jitsu stars strike gold at AJP Championship in Doha",
  "snippet": "",
  "published": "2026-10-18T17:45:14+00:00"
 },
 {
  "id": "4e8bd9141f43",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "China tops standings on opening day of Abu Dhabi Grand Slam Jiu-Jitsu in Shanghai",
  "snippet": "",
  "published": "2026-10-17T18:39:53+00:00"
 },
 {
  "id": "8b6b142e81ad",
  "region": "intl",
  "source": "스타뉴스",
  "title": "\"Invincible Rising Star? You Just Haven't Faced Me Yet\": Yoo Soo-yeong Defeats Cody Corbanek via Submission, \"It Doesn't Matter Who My Next Opponent Is\" [UFC]",
  "snippet": "",
  "published": "2026-10-18T07:41:22+00:00"
 },
 {
  "id": "d0bd20208457",
  "region": "intl",
  "source": "Muscat Daily",
  "title": "Sur siblings secure double gold at international championship",
  "snippet": "",
  "published": "2026-10-18T15:27:38+00:00"
 },
 {
  "id": "fb4bf9b0ca4b",
  "region": "intl",
  "source": "BJJEE",
  "title": "Ralph Gracie On The Melqui Galvão Case: “The Law Has To Be Severe”",
  "snippet": "Ralph Gracie addressed the Melqui Galvão situation – and, asked about se*ual assault allegations in martial arts, he placed the responsibility on instructors and gym owners. Here is what the Gracie had to say: We, professors, gym owners, we’re responsible for the physical and mental [wellbeing] of them in the academy. Of any person, a woman, a child. He described the instructor’s role as a position of trust, and one that demands strict consequences when it is abused: The professor is the guy who is responsible, and (if) the professor is the guy who is doing what he is doing – my friend, the la…",
  "published": "2026-10-18T10:26:02+00:00"
 },
 {
  "id": "036ad3b3ef1e",
  "region": "intl",
  "source": "BJJEE",
  "title": "Henry Cejudo Says Khabib Nurmagomedov & Other Sambo Athletes Couldn’t Make It In Wrestling",
  "snippet": "Henry Cejudo has taken aim at the standing of sambo in Dagestan, claiming that athletes who compete in it do so because they fell short in wrestling. The Olympic gold medalist and former two-division UFC champion made the case on the Double Coverage Podcast, asked about the wave of champions coming out of Russia’s combat sports system. He named Khabib Nurmagomedov among those he had in mind, while saying he respects them: People who do sambo can’t do wrestling. Like they can’t make it in wrestling. Like Khabib and all these dudes, like I love them, but I know like wrestling’s king in Dagestan.…",
  "published": "2026-10-18T10:10:17+00:00"
 }
]
