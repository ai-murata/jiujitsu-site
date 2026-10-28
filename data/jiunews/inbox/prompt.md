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
  "id": "cc0a36118afb",
  "region": "jp",
  "source": "毎日新聞",
  "title": "柔術大会で世界一 津曲寛卓さん（11） 体格差へっちゃら「次もVを」 五條市長に報告 ／奈良",
  "snippet": "",
  "published": "2026-10-26T20:03:11+00:00"
 },
 {
  "id": "1d8a6f9258d2",
  "region": "jp",
  "source": "UFC.com",
  "title": "Jasmine Rocha Pre-Match Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-27T19:54:10+00:00"
 },
 {
  "id": "d482abf6a207",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "2026年アジア室内・武道競技大会が、予想外の延期となった。",
  "snippet": "",
  "published": "2026-10-27T08:42:10+00:00"
 },
 {
  "id": "c84b9232a98e",
  "region": "jp",
  "source": "UFC.com",
  "title": "Kleber Barboza Pre-Match Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-27T19:54:10+00:00"
 },
 {
  "id": "e443daf0e5e2",
  "region": "jp",
  "source": "UFC.com",
  "title": "Jay Rodriguez Pre-Match Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-27T18:56:05+00:00"
 },
 {
  "id": "31f8de33024c",
  "region": "jp",
  "source": "UFC.com",
  "title": "William Tackett Pre-Match Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-27T18:56:05+00:00"
 },
 {
  "id": "8d0a1d6e8fe6",
  "region": "jp",
  "source": "efight.jp",
  "title": "レフェリー、パウンド止める際に選手のヒザ直撃！脚がぐにゃり…勝者が絶叫し転倒「残酷すぎる」",
  "snippet": "",
  "published": "2026-10-27T02:30:41+00:00"
 },
 {
  "id": "e64bc2006a32",
  "region": "jp",
  "source": "TRILL【トリル】",
  "title": "「毎日のように顔を合わせる」玉木宏が“芸能界で仲のいい人物”と明かした【ストイック俳優】とは？",
  "snippet": "",
  "published": "2026-10-27T21:35:00+00:00"
 },
 {
  "id": "8b3f325a512a",
  "region": "jp",
  "source": "arcraiders.nexon.com",
  "title": "ライブアップデート 2.3.0 | アークレイダース",
  "snippet": "",
  "published": "2026-10-27T10:32:45+00:00"
 },
 {
  "id": "4404bebecdd7",
  "region": "jp",
  "source": "Number Web",
  "title": "「プロレスも学生生活も青春です」高校3年生の女子プロレスラー・心希が明かす「友達はみんな受験」「体育祭翌日に両国大会」高校最後の夏を追った（橋本宗洋）",
  "snippet": "",
  "published": "2026-10-27T04:43:15+00:00"
 },
 {
  "id": "67f29701e1e7",
  "region": "intl",
  "source": "Daily Freeman",
  "title": "Martial Arts: Midtown Jiu Jitsu competitors star at ADCC New Jersey Open",
  "snippet": "",
  "published": "2026-10-27T19:27:54+00:00"
 },
 {
  "id": "2c9a4c4800b3",
  "region": "intl",
  "source": "Erie News Now",
  "title": "814 Matters: Jaroslav “Yoda” Botka (Good Karma Jiu-Jitsu Academy)",
  "snippet": "",
  "published": "2026-10-27T17:14:00+00:00"
 },
 {
  "id": "b23542a37b8f",
  "region": "intl",
  "source": "MMA Mania",
  "title": "UFC BJJ 13 live stream, results, video highlights | New champ to take Musumeci’s belt",
  "snippet": "",
  "published": "2026-10-27T08:30:00+00:00"
 },
 {
  "id": "2618ebe3d3db",
  "region": "intl",
  "source": "Cleveland.com",
  "title": "This sport rising in popularity in US and abroad",
  "snippet": "",
  "published": "2026-10-26T15:43:00+00:00"
 },
 {
  "id": "27b8d3086809",
  "region": "intl",
  "source": "theherald.co.za",
  "title": "Eastern Cape champion Shahla-Zeynib Jogee aims to empower women through jiu-jitsu",
  "snippet": "",
  "published": "2026-10-27T07:24:55+00:00"
 },
 {
  "id": "25f01868ea3a",
  "region": "intl",
  "source": "boxingnews.com",
  "title": "UFC BJJ 13 Crowns New Champ After Musumeci Vacates",
  "snippet": "",
  "published": "2026-10-27T08:30:42+00:00"
 },
 {
  "id": "80c2e7fcd97c",
  "region": "intl",
  "source": "UFC.com",
  "title": "Match By Match Preview | UFC BJJ 13: Tackett vs Rodriguez",
  "snippet": "",
  "published": "2026-10-27T18:50:16+00:00"
 },
 {
  "id": "53096436182c",
  "region": "intl",
  "source": "Telegraph and Argus",
  "title": "Bradford club claim European glory as inexperience overcome in style",
  "snippet": "",
  "published": "2026-10-28T00:15:00+00:00"
 },
 {
  "id": "cae5a79b0148",
  "region": "intl",
  "source": "Turkmenportal.com",
  "title": "Turkmen athletes won 16 medals at the World Jiu-Jitsu Championships in Antalya",
  "snippet": "",
  "published": "2026-10-27T02:58:02+00:00"
 },
 {
  "id": "abb686dd7a5c",
  "region": "intl",
  "source": "Townsville Bulletin",
  "title": "Vote now: Gympie’s top 20 martial arts instructors revealed",
  "snippet": "",
  "published": "2026-10-27T01:22:07+00:00"
 },
 {
  "id": "f81f49c020fb",
  "region": "intl",
  "source": "BJJDOC",
  "title": "UFC’s Casey O’Neil Credits Gi Training With Pulling Off Viral Submission",
  "snippet": "",
  "published": "2026-10-27T17:54:31+00:00"
 },
 {
  "id": "3afbd79010ec",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Two Vacant Belts Headline UFC BJJ 13 in Las Vegas",
  "snippet": "",
  "published": "2026-10-27T16:08:26+00:00"
 },
 {
  "id": "38287e80c2ac",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "Windows Announces Landmark Partnership With Ruotolo Brothers",
  "snippet": "",
  "published": "2026-10-26T16:34:35+00:00"
 },
 {
  "id": "5af9a373d504",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "IBJJF Crown Brackets Set For November 8 In Long Beach",
  "snippet": "",
  "published": "2026-10-27T23:15:00+00:00"
 },
 {
  "id": "ba7e048af47d",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Sam Nagai Wants An Aggressive Crown Return After Two Major Finals",
  "snippet": "",
  "published": "2026-10-27T15:24:05+00:00"
 },
 {
  "id": "e91fff47c494",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Ademir Barreto Trusts Adaptability Before IBJJF Crown Featherweight Challenge",
  "snippet": "",
  "published": "2026-10-27T16:13:09+00:00"
 },
 {
  "id": "1782d25527f8",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Arman Tsarukyan To Defend RAF Title Against Anthony Pettis On November 28",
  "snippet": "",
  "published": "2026-10-27T23:23:14+00:00"
 },
 {
  "id": "6d148bc24e33",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Geno Petriashvili Faces Yonger Bastida In RAF Heavyweight Title Eliminator",
  "snippet": "",
  "published": "2026-10-27T02:13:53+00:00"
 },
 {
  "id": "af4824b163b0",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Arman Tsarukyan Faces Neiman Gracie In RAF Abu Dhabi Co-Main Event",
  "snippet": "",
  "published": "2026-10-27T02:13:53+00:00"
 },
 {
  "id": "fad19bf790eb",
  "region": "intl",
  "source": "LatestLY",
  "title": "Jayden Jain: Indian MMA Fighter's US Debut Will Stun You!",
  "snippet": "",
  "published": "2026-10-27T05:35:14+00:00"
 },
 {
  "id": "b779dba43ad6",
  "region": "intl",
  "source": "OneArabia",
  "title": "Jayden Jain's US Debut: A Masterclass in First-Round Submission",
  "snippet": "",
  "published": "2026-10-27T05:12:21+00:00"
 },
 {
  "id": "026292f87e60",
  "region": "intl",
  "source": "BJJEE",
  "title": "Gavin Corbe Shares How He Won ADCC Silver On Coffee, Candy & Almost No Preparation",
  "snippet": "Gavin Corbe’s ADCC silver medal surprised many people, and how he got there surprised them more. The 26-year-old shared that his preparation looks nothing like his rivals’. Plus, his invitation came late. His brother DeAndre was training in San Diego for the event while Gavin stayed home running their gym, Black Box: I just gave up on the idea that I was going to get invited because all the spots were getting taken up… I’m going to jump in there. I’ll regret it more if I didn’t take it. He entered without strength and conditioning work and at a weight that was not where it needed to be: My dai…",
  "published": "2026-10-27T09:58:10+00:00"
 },
 {
  "id": "67a592dc6b7b",
  "region": "intl",
  "source": "BJJEE",
  "title": "Kurt Angle Explains How He Won Olympic Gold With A Broken Neck",
  "snippet": "Kurt Angle, the 1996 Olympic gold medalist, has told the full story of how he competed and won with a broken neck – ignoring medical advice to chase his lifelong goal. He broke his neck in the first round of the Olympic trials at the U.S. Open and still won the tournament before seeing a doctor: I broke my neck at the U.S. Open, the first round of the Olympic trials… I ended up winning the U.S. Open and I went home the next day and I went to my doctor and he took an MRI on my neck… “You have four broken vertebrae and two sticks directly into your spinal cord and you’re going to have a really b…",
  "published": "2026-10-27T09:47:31+00:00"
 }
]
