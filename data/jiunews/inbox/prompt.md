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
  "id": "d4dbcd59931a",
  "region": "jp",
  "source": "eJudo",
  "title": "【連載】見る専👀Ayaの場外ケアシステム #075「嘉重春樺、世界選手権2連覇の秘訣は柔術に!? ／王者PSGやはり強い！テディ・リネールの出場はいかに…／ベデルのハネムーンは日本！花嫁姿で東京観光」",
  "snippet": "",
  "published": "2026-11-01T23:55:18+00:00"
 },
 {
  "id": "198ae02f3447",
  "region": "jp",
  "source": "au Webポータル",
  "title": "「最強の柔道家」木村政彦が顔面血だるまで沈んだ「力道山へのいけない挑発」／スポーツ界を揺るがせた「大問題発言」",
  "snippet": "",
  "published": "2026-11-03T00:45:00+00:00"
 },
 {
  "id": "4d61c31c0607",
  "region": "jp",
  "source": "Infoseek",
  "title": "「あらゆる面で優位に立つ」――ルーカス・ガブリエル、ONEファイトナイト49でマゴメド・マゴメドフの無敗記録を止めることを目指す",
  "snippet": "",
  "published": "2026-11-02T07:03:10+00:00"
 },
 {
  "id": "aad43b244bf0",
  "region": "jp",
  "source": "西日本新聞me",
  "title": "陸上の全国大会に出場する（右から）宇佐美さん、磯部さん、宮崎さんと浜田さん - 北九州の小6の3人、陸上全国大会へ 「アスリートリンク」所属 「表彰台目指す」 - 写真・画像(1/1)",
  "snippet": "",
  "published": "2026-11-01T21:17:55+00:00"
 },
 {
  "id": "64a0d27e88fb",
  "region": "jp",
  "source": "Infoseek",
  "title": "11月6日開催の「ザ・インナー・サークル37」の全対戦カードが発表",
  "snippet": "",
  "published": "2026-11-01T20:23:31+00:00"
 },
 {
  "id": "e352943786d8",
  "region": "jp",
  "source": "Infoseek",
  "title": "「とんでもない夜になりそうだ」――タイ・ルオトロ、『インナー・サークル37』でクリスチャン・リーと対戦し、歴史を刻む準備は万端",
  "snippet": "",
  "published": "2026-11-02T23:37:32+00:00"
 },
 {
  "id": "bdf1410a1fff",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "【ONE】山北渓人「SAMURAI 5」で長男誕生重なる運命の王座戦「獲らなきゃいけない」",
  "snippet": "",
  "published": "2026-11-02T06:57:00+00:00"
 },
 {
  "id": "6697aa2eae56",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "【ONE】山北渓人「獲らなきゃいけない」 家族のために負けられない世界タイトル戦！「弱みを見せない」",
  "snippet": "",
  "published": "2026-11-02T08:06:00+00:00"
 },
 {
  "id": "cab00e6035df",
  "region": "jp",
  "source": "Infoseek",
  "title": "「団結して懸命に努力する」――クリスチャン・リーが、ハワイの次世代ファイターたちの道を切り拓く",
  "snippet": "",
  "published": "2026-11-02T07:15:57+00:00"
 },
 {
  "id": "7eb588bb6059",
  "region": "jp",
  "source": "Infoseek",
  "title": "11月6日に『The Inner Circle 37』を視聴すべき、見逃せない3つの理由",
  "snippet": "",
  "published": "2026-11-02T09:09:30+00:00"
 },
 {
  "id": "3bfa0a9b9700",
  "region": "intl",
  "source": "Black Belt Magazine",
  "title": "Rolling in Rio: The Brazilian Jiu-Jitsu Experience",
  "snippet": "",
  "published": "2026-11-02T18:42:22+00:00"
 },
 {
  "id": "248c1bdfad8a",
  "region": "intl",
  "source": "WBIR",
  "title": "Bearden middle schooler wins Pan-American Jiu-Jitsu title",
  "snippet": "",
  "published": "2026-11-02T17:41:00+00:00"
 },
 {
  "id": "38e6f9527248",
  "region": "intl",
  "source": "BJJ Heroes",
  "title": "2026 IBJJF European No-Gi Championship Results",
  "snippet": "",
  "published": "2026-11-02T13:59:20+00:00"
 },
 {
  "id": "68eab525a0f4",
  "region": "intl",
  "source": "Nanaimo News Bulletin",
  "title": "Nanaimo jiu-jitsu academy ‘tops’ at Abu Dhabi Combat Club open on Mainland",
  "snippet": "",
  "published": "2026-11-02T13:51:03+00:00"
 },
 {
  "id": "8a1bae089117",
  "region": "intl",
  "source": "The Straits Times",
  "title": "Fencing, jiu-jitsu, chess among sports affected or scrapped at 2027 SEA Games",
  "snippet": "",
  "published": "2026-11-02T10:45:00+00:00"
 },
 {
  "id": "0b03cbd61795",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Dierley De Almeida Rodrigues vs Marcio Celio Lima De Oliveira 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-11-01T20:41:16+00:00"
 },
 {
  "id": "220ea25a8af1",
  "region": "intl",
  "source": "The Maine Campus",
  "title": "UMSG discusses Patch Hall hot water outage, grants recognition to four clubs",
  "snippet": "",
  "published": "2026-11-02T07:04:59+00:00"
 },
 {
  "id": "0a2a16bc33b8",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Dillon Danis dips on grappling match with Colby Covington, Raul Rosas Jr. steps in on three days notice",
  "snippet": "",
  "published": "2026-11-01T18:00:00+00:00"
 },
 {
  "id": "804fc7b77eda",
  "region": "intl",
  "source": "Forces News",
  "title": "Save the dates! Army and Navy Sports Awards to be broadcast LIVE",
  "snippet": "",
  "published": "2026-11-02T14:32:18+00:00"
 },
 {
  "id": "3b292237820d",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "Khabib Nurmagomedov Reveals His Father's Favorite Sport",
  "snippet": "",
  "published": "2026-11-02T02:18:51+00:00"
 },
 {
  "id": "793524251b4a",
  "region": "intl",
  "source": "Castanet Kamloops",
  "title": "Become part of StrongHER community through kickboxing, self-defence",
  "snippet": "",
  "published": "2026-11-02T07:40:02+00:00"
 },
 {
  "id": "4592266e5fc1",
  "region": "intl",
  "source": "Liverpool Echo",
  "title": "‘We're not trying to change the world, just South Road’",
  "snippet": "",
  "published": "2026-11-02T21:18:00+00:00"
 },
 {
  "id": "aef317ff8e30",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "James Gonzalez vs Jonathan Potts 2026 LIJJN Boo Jitsu Halloween Hangover",
  "snippet": "",
  "published": "2026-11-02T00:21:19+00:00"
 },
 {
  "id": "fa8c1703044c",
  "region": "intl",
  "source": "Gibraltar Chronicle",
  "title": "Stevens win British Veteran Championships 2026 in Scotland",
  "snippet": "",
  "published": "2026-11-02T11:18:13+00:00"
 },
 {
  "id": "d581b28b03b9",
  "region": "intl",
  "source": "BJJDOC",
  "title": "BJJ Historian Disputes Helio Gracie Was A Fascist Despite Being A Part Of Integralist Movement",
  "snippet": "",
  "published": "2026-11-02T08:19:02+00:00"
 },
 {
  "id": "b250a88f0925",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Chimaev and Masvidal Set for Submission-Only Match in Dubai",
  "snippet": "",
  "published": "2026-11-02T16:23:31+00:00"
 },
 {
  "id": "dc7ab7562e5e",
  "region": "intl",
  "source": "BJJDOC",
  "title": "ADCC Gold Medalist & UFC Veteran: \"Having The UFC On The White House Lawn Is Insulting To The Memory Of This Country\"",
  "snippet": "",
  "published": "2026-11-02T07:34:30+00:00"
 },
 {
  "id": "71f67d620407",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Khamzat Chimaev Faces Jorge Masvidal In December 4 ALF Grappling Main Event",
  "snippet": "",
  "published": "2026-11-02T20:42:50+00:00"
 },
 {
  "id": "b8707741f2cf",
  "region": "intl",
  "source": "GhanaWeb",
  "title": "Police Ladies thrash Immigration 4-0 to maintain perfect start to season",
  "snippet": "",
  "published": "2026-11-01T16:43:03+00:00"
 },
 {
  "id": "da16283c2778",
  "region": "intl",
  "source": "BJJEE",
  "title": "Gui Mendes Shares What He’d Do Differently Starting BJJ Over From White Belt",
  "snippet": "Brazilian Jiu-Jitsu world champion Gui Mendes says he would organize everything if he could begin again. In a recent video, he outlined a white belt plan built on structure, fundamentals and steady progress – as he sees disorganization as why many people walk away: If I could start Jiu-Jitsu over again, I would focus on organizing everything. It’s very hard to understand what you should prioritize and the things that are truly important. The biggest reason why people quit jiu-jitsu is because at some point it becomes overwhelming for them, especially in the beginning. If you focus on creating…",
  "published": "2026-11-02T11:43:12+00:00"
 },
 {
  "id": "3b0a6c0f9d2f",
  "region": "intl",
  "source": "BJJEE",
  "title": "Former Student Accuses BJJ Champion AJ Agazarm Of Grooming After September Arrest",
  "snippet": "A former student has accused AJ Agazarm, a decorated Brazilian Jiu-Jitsu champion and MMA fighter, of grooming. The allegation follows his September arrest on suspicion of residential burglary in Ventura County, California. No charges have been filed. According to Ventura County Sheriff’s Office records , Agazarm was taken into custody on September 22, 2026, at 5:45 p.m. and booked into the main jail that evening. He posted $50,000 bail and was released the next day. He is the lead instructor at Agazarmy Atascadero in San Luis Obispo County. The arrest stems from claims by his 24-year-old ex-g…",
  "published": "2026-11-02T07:56:04+00:00"
 }
]
