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
  "id": "333168c0d084",
  "region": "jp",
  "source": "アラブニュース",
  "title": "トップクラブがアブダビで柔術プレジデント杯を巡る戦い",
  "snippet": "",
  "published": "2026-10-23T13:35:06+00:00"
 },
 {
  "id": "8066c8a875ff",
  "region": "jp",
  "source": "YouTube",
  "title": "強い柔術家が“特注道着”に求めていること【スパイダーガーダー必見】 ＃毛利部慎佑 #木村天星",
  "snippet": "",
  "published": "2026-10-23T09:35:07+00:00"
 },
 {
  "id": "d8a317ca52b6",
  "region": "jp",
  "source": "WEBザテレビジョン",
  "title": "画像・写真 ＜刃牙道＞素手の格闘では持ち味を出せずにいた実戦柔術の使い手・本部以蔵が大舞台に臨む…第17話あらすじ＆先行カット公開(7/7)",
  "snippet": "",
  "published": "2026-10-23T15:14:10+00:00"
 },
 {
  "id": "8362abe4f9dc",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 13: Tackett vs Rodriguez airs live on Thursday, October 29th on UFC FIGHT PASS!",
  "snippet": "",
  "published": "2026-10-23T19:46:50+00:00"
 },
 {
  "id": "dc9c07e92e93",
  "region": "intl",
  "source": "New York Post",
  "title": "Exclusive | NYPD, FDNY and other service members to compete in city-first jiu-jitsu tourney",
  "snippet": "",
  "published": "2026-10-23T19:30:00+00:00"
 },
 {
  "id": "195483a85895",
  "region": "intl",
  "source": "Combat Press",
  "title": "Jay Rodriguez Looks to Turn the Tables on William Tackett at UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-23T16:59:00+00:00"
 },
 {
  "id": "41fcc2ead7a5",
  "region": "intl",
  "source": "Arab News",
  "title": "Top clubs chase Jiu-Jitsu President’s Cup title in Abu Dhabi",
  "snippet": "",
  "published": "2026-10-23T07:37:29+00:00"
 },
 {
  "id": "855117ff52e8",
  "region": "intl",
  "source": "Sherdog",
  "title": "Rousimar Palhares & Andre Galvao set for ADCC rematch with strikes",
  "snippet": "",
  "published": "2026-10-22T23:48:15+00:00"
 },
 {
  "id": "7aaee3dfd4da",
  "region": "intl",
  "source": "نادي النصر الثقافي الرياضي",
  "title": "Al Nasr Sports Games Company Honours Jiu-Jitsu and Cycling Champions",
  "snippet": "",
  "published": "2026-10-23T12:40:53+00:00"
 },
 {
  "id": "f6982d9c874f",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - M/W",
  "snippet": "",
  "published": "2026-10-22T18:48:47+00:00"
 },
 {
  "id": "d7603e892019",
  "region": "intl",
  "source": "Gulf Today",
  "title": "President receives UAE jiu-jitsu Asian Games medallists, says nation places great importance on sports sector",
  "snippet": "",
  "published": "2026-10-22T14:47:29+00:00"
 },
 {
  "id": "0d9834216cf2",
  "region": "intl",
  "source": "www.thenationalnews.com",
  "title": "UAE President receives UAE Jiu-Jitsu national team - in pictures",
  "snippet": "",
  "published": "2026-10-22T19:03:32+00:00"
 },
 {
  "id": "6fa29c120865",
  "region": "intl",
  "source": "Patch",
  "title": "Martial Arts School Moves To New Location In Malden",
  "snippet": "",
  "published": "2026-10-23T14:35:03+00:00"
 },
 {
  "id": "7bdd5fa5e586",
  "region": "intl",
  "source": "Mixtape Madness",
  "title": "Tinie Tempah: An MM Exclusive Interview",
  "snippet": "",
  "published": "2026-10-23T12:03:23+00:00"
 },
 {
  "id": "08ec8a1f29b8",
  "region": "intl",
  "source": "MyMMANews",
  "title": "Finishers Sub-Only Returns to the High Seas for USS Iowa Event Supporting Veterans",
  "snippet": "",
  "published": "2026-10-23T16:11:49+00:00"
 },
 {
  "id": "e9db0032062c",
  "region": "intl",
  "source": "Odessa American",
  "title": "GOOD NEWS: Bringing Home the Gold",
  "snippet": "",
  "published": "2026-10-22T14:57:31+00:00"
 },
 {
  "id": "b0d791bbac6c",
  "region": "intl",
  "source": "Kayo Sports",
  "title": "Watch Mixed martial arts Live",
  "snippet": "",
  "published": "2026-10-23T04:42:48+00:00"
 },
 {
  "id": "ca978ea35667",
  "region": "intl",
  "source": "Big News Network.com",
  "title": "Top clubs chase Jiu-Jitsu President's Cup title in Abu Dhabi on Saturday",
  "snippet": "",
  "published": "2026-10-23T13:25:00+00:00"
 },
 {
  "id": "609396a7a63e",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Jay Rodriguez Details Tackett’s Fast Start Before UFC BJJ 13 Rematch",
  "snippet": "",
  "published": "2026-10-23T23:23:04+00:00"
 },
 {
  "id": "6dbc2f933b5d",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Andre Galvao Vs Rousimar Palhares Will Feature ‘Combat Jiu Jitsu Rules’",
  "snippet": "",
  "published": "2026-10-23T16:11:54+00:00"
 },
 {
  "id": "42a356f8b57a",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Robert Whittaker Is A Big Believer In Gi Training For Learning Jiu-jitsu Because Gi Players Can Transition To No-gi, But It Is Much Harder To Go The Other Way",
  "snippet": "",
  "published": "2026-10-23T06:56:22+00:00"
 },
 {
  "id": "625c0e10763d",
  "region": "intl",
  "source": "BJJDOC",
  "title": "B Team’s Owen Jones Opens Up On Having To Confront Bad Training Partners",
  "snippet": "",
  "published": "2026-10-23T17:29:45+00:00"
 },
 {
  "id": "fe7d3b26d60b",
  "region": "intl",
  "source": "Travels Dubai",
  "title": "Abu Dhabi set for Jiu-Jitsu President’s Cup showdown",
  "snippet": "",
  "published": "2026-10-23T07:40:23+00:00"
 },
 {
  "id": "856086e5828c",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Bella Mir Says UFC Contract Predated Contender Series Appearance",
  "snippet": "",
  "published": "2026-10-23T03:07:37+00:00"
 },
 {
  "id": "de04d51d10d0",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Nicky Ryan Has Never Done An IBJJF Competition And Has No Plans To: You Could Never Make Money Competing For The IBJJF, Only The IBJJF Makes Money",
  "snippet": "",
  "published": "2026-10-23T11:08:51+00:00"
 },
 {
  "id": "0e436f5c1766",
  "region": "intl",
  "source": "BJJEE",
  "title": "Nicky Ryan Explains Why He Doesn’t Plan To Compete In The IBJJF – Ever",
  "snippet": "Nicky Ryan has never entered an IBJJF event and does not plan to. His reasoning is business-minded – as for competitors, he says, the financial model does not work: I’ve always been kind of against doing IBJJF. I’ve never done a single one of their events… I always thought it was f*cked that you could never make money competing for the IBJJF. Only the IBJJF makes money… Why go win this, pay to compete and make zero dollars? That organization makes so much money. No, I’d rather just do super matches or do ADCC. Competitors pay entry fees and receive no prize money for winning, a setup Ryan reje…",
  "published": "2026-10-23T11:55:25+00:00"
 },
 {
  "id": "fdb0ab2e5aee",
  "region": "intl",
  "source": "BJJEE",
  "title": "Robert Whittaker Explains Why Gi Training Is The Better Way To Learn Jiu-Jitsu",
  "snippet": "UFC star Robert Whittaker told Joe Rogan that the gi has a valuable place in learning Jiu-Jitsu, including for MMA. He argues that skills built in the gi carry over to no-gi much more readily than the other way around: If you want to learn Jiu-Jitsu, I’m a big believer in gi… Obviously it’s different, but a lot of gi guys can transition from gi to no-gi. It’s very hard the other way around. For Whittaker, the gi is more than a separate tradition. Its grips and slower pace make positioning and decision-making critical, especially for MMA: The great thing about the gi in terms of Jiu-Jitsu, espe…",
  "published": "2026-10-23T11:49:03+00:00"
 }
]
