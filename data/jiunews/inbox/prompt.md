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
  "id": "e4a436806405",
  "region": "jp",
  "source": "efight.jp",
  "title": "こんな手があったか！後ろを向いた瞬間、相手がバッタリ！この技は一体何？",
  "snippet": "",
  "published": "2026-11-05T08:58:29+00:00"
 },
 {
  "id": "f6ecb6c70d2b",
  "region": "jp",
  "source": "MMAPLANET",
  "title": "【ONE TIC37】組み技世界一=タイ・ルオトロの挑戦を受けるクリスチャン・リー「殺気を込めたファイトで」",
  "snippet": "",
  "published": "2026-11-05T14:52:43+00:00"
 },
 {
  "id": "ab59f4cd7a53",
  "region": "jp",
  "source": "Infoseek",
  "title": "「ONE Fight Night 50」で、ディオゴ・レイスがベベト・オリベイラを相手に王座防衛戦に臨み、セリーナ・フローレスは森本加奈と対戦する",
  "snippet": "",
  "published": "2026-11-05T08:48:39+00:00"
 },
 {
  "id": "52429d7f9965",
  "region": "jp",
  "source": "Infoseek",
  "title": "「誰とでも決着をつける」――ヴィクトル・ヒューゴとデヴォンテ・ジョンソン、ONE Fight Night 49で3戦目となる対決に臨む",
  "snippet": "",
  "published": "2026-11-05T04:57:03+00:00"
 },
 {
  "id": "a8658c41fdbb",
  "region": "jp",
  "source": "Infoseek",
  "title": "リー対ルオトロ：THE INNER CIRCLE 37で開催されるONEライト級MMA世界タイトルマッチにおける勝利の4つの鍵",
  "snippet": "",
  "published": "2026-11-05T02:57:12+00:00"
 },
 {
  "id": "04c0739d03b9",
  "region": "jp",
  "source": "Infoseek",
  "title": "「すぐに決着がつく」――タイ・ルオトロ、クリスチャン・リーの復讐の戦いを短く終わらせたい",
  "snippet": "",
  "published": "2026-11-04T22:58:03+00:00"
 },
 {
  "id": "5caf41124c33",
  "region": "jp",
  "source": "Infoseek",
  "title": "「ONE Fight Night 49」で注目を集めそうな3つの試合",
  "snippet": "",
  "published": "2026-11-04T18:00:07+00:00"
 },
 {
  "id": "4df68ffc46f3",
  "region": "intl",
  "source": "WVLT",
  "title": "Bearden Middle School student crowned Pan American Jiu-Jitsu Champion",
  "snippet": "",
  "published": "2026-11-05T20:41:00+00:00"
 },
 {
  "id": "bc59e66a3dc2",
  "region": "intl",
  "source": "MMA Mania",
  "title": "2026 IBJJF Crown - Live video stream, results, BJJ brackets, highlights",
  "snippet": "",
  "published": "2026-11-05T09:30:00+00:00"
 },
 {
  "id": "8255878e01bb",
  "region": "intl",
  "source": "Queen Creek Tribune",
  "title": "Queen Creek girl, 9, scores jiu-jitsu championship",
  "snippet": "",
  "published": "2026-11-05T07:00:00+00:00"
 },
 {
  "id": "511ad42629b7",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "Relative Strength Martial Arts Looking to Cement Place",
  "snippet": "",
  "published": "2026-11-05T13:01:30+00:00"
 },
 {
  "id": "042337d4675f",
  "region": "intl",
  "source": "Fightful",
  "title": "Juicy Finau Returning To World Elite Sumo",
  "snippet": "",
  "published": "2026-11-06T00:46:23+00:00"
 },
 {
  "id": "d8eb7b60fbfe",
  "region": "intl",
  "source": "Kyabram Free Press",
  "title": "Todd submits to jiu-jitsu grind",
  "snippet": "",
  "published": "2026-11-05T22:24:32+00:00"
 },
 {
  "id": "1bb3706fa520",
  "region": "intl",
  "source": "Gulf News",
  "title": "Building champions at home: The role of family in Zamzam Al Hammadi's Jiu-Jitsu success",
  "snippet": "",
  "published": "2026-11-05T06:30:32+00:00"
 },
 {
  "id": "f07b055dc022",
  "region": "intl",
  "source": "NorthernIrelandWorld",
  "title": "Nine-year-old Broughshane brothers making waves in the world of combat sports",
  "snippet": "",
  "published": "2026-11-05T06:00:00+00:00"
 },
 {
  "id": "d201907ecbcb",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 CBJJE International BJJ Championships - Videos",
  "snippet": "",
  "published": "2026-11-04T15:58:16+00:00"
 },
 {
  "id": "b329766653a5",
  "region": "intl",
  "source": "Wrestling Headlines",
  "title": "Jimmy House Recalls Goldberg’s First-Match Pep Talk, Explains Why Wrestling Is Harder Than Jiu-Jitsu",
  "snippet": "",
  "published": "2026-11-05T22:33:06+00:00"
 },
 {
  "id": "ffadf532059e",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Gui Mendes: Blue Belt Is The Most Difficult And Frustrating Phase Of Jiu-jitsu",
  "snippet": "",
  "published": "2026-11-05T11:58:35+00:00"
 },
 {
  "id": "083c22e6e7e0",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Abu Dhabi World Pro Returns November 9–21, With Professionals Up Last",
  "snippet": "",
  "published": "2026-11-05T05:03:04+00:00"
 },
 {
  "id": "9359114d64b5",
  "region": "intl",
  "source": "BJJEE",
  "title": "Gui Mendes: “Blue Belt Is The Most Frustrating Stage Of Jiu-Jitsu”",
  "snippet": "World champion Gui Mendes says blue belt is the toughest period in a practitioner’s journey. His main point is that expectations change. White belts know they are beginners and expect little of themselves. But blue belts start judging their level and measuring themselves against peers: To me, the blue belt is probably the most difficult phase if you don’t have your thoughts well organized. It’s where you’re going to feel frustrated the most and you should understand that it’s very important for you to focus on yourself and avoid the comparisons. As a blue belt, you start having the expectation…",
  "published": "2026-11-05T15:00:07+00:00"
 },
 {
  "id": "0c0840f095e3",
  "region": "intl",
  "source": "BJJEE",
  "title": "Xande Ribeiro Warns That The Attention Economy Is Hurting Jiu-Jitsu",
  "snippet": "Seven-time world champion Xande Ribeiro says modern Jiu-Jitsu culture is producing a “huge identity crisis”. Specifically, he blamed social media, organizational pressure to entertain and an overemphasis on winning for steering the sport and its athletes the wrong way. He traced the problem to a change in values: At least for me, competition was very natural. It was more like let’s get the group together and defend the team. It wasn’t really something that we did as individuals. For me, Jiu-Jitsu was never about being the best, it was about being skilful. He sees attention as the new currency:…",
  "published": "2026-11-05T14:45:19+00:00"
 },
 {
  "id": "9c7d84376aa6",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "BJJ Rankings Update – November 2026",
  "snippet": "The November 2026 update has been applied to the Jits Magazine BJJ Rankings and the full standings can be found here . The biggest impact came from the latest event on the IBJJF no gi grand slam calendar, the IBJJF No Gi European Championship 2026 . Although this was one of the smaller major tournaments, it still featured several ranked competitors in multiple weight classes. A few other changes came from the fact that UFC BJJ hosted events at both the beginning and end of the month, and Polaris also put on their latest slte of superfights as well. The Jits Magazine BJJ Rankings also have thei…",
  "published": "2026-11-04T13:42:30+00:00"
 }
]
