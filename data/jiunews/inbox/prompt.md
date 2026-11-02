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
  "id": "47ddca51be23",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【UFC】190cmの新鋭ノーラン、柔術黒帯モイカノをKO！ピンチから逆転で6連勝（イーファイト）",
  "snippet": "",
  "published": "2026-11-01T10:05:20+00:00"
 },
 {
  "id": "6b6460cf9b64",
  "region": "jp",
  "source": "efight.jp",
  "title": "【UFC】190cmの新鋭ノーラン、柔術黒帯モイカノをKO！ピンチから逆転で6連勝",
  "snippet": "",
  "published": "2026-11-01T09:58:17+00:00"
 },
 {
  "id": "17dce0045785",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【パンクラス】元王者・菊入正行、緊急参戦の平信一と激突！眞藤源太はブラジルの新鋭と対戦＝11.8（イーファイト）",
  "snippet": "",
  "published": "2026-11-01T07:49:14+00:00"
 },
 {
  "id": "3964ff42a642",
  "region": "intl",
  "source": "NanaimoNewsNOW",
  "title": "Island Top Team clean up at Canadian Open Brazilian jiu jitsu event",
  "snippet": "",
  "published": "2026-11-01T12:34:14+00:00"
 },
 {
  "id": "a5d926851bc2",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "Victor Hugo and Devhonte Johnson Ready for ONE Debuts",
  "snippet": "",
  "published": "2026-11-01T17:23:21+00:00"
 },
 {
  "id": "2e030a66d3b7",
  "region": "intl",
  "source": "BJJEE",
  "title": "Marcelo Garcia Recalls Being Choked Out In 20 Seconds At His First Worlds",
  "snippet": "Marcelo Garcia, a multiple-time ADCC and World champion, did not have a smooth start. On The North South Project podcast, he described the loss at his first World Championship that shaped how he handles setbacks. Garcia fell for Jiu-Jitsu within a week. In his small town, classes ran three times a week, and he marked training days on a calendar: I was already, like, I can’t wait to the next day and there was no class next day because there was only three class a week… During the weekend, I was, like, I can’t believe it’s a weekend. So I have to wait two more days now until the next class. At 1…",
  "published": "2026-11-01T15:20:41+00:00"
 },
 {
  "id": "3ba4c9a01a9f",
  "region": "intl",
  "source": "BJJEE",
  "title": "MMA Fighter Asks Dana White For A $100K Bonus To Help Pay For His Wedding After UFC Debut Win",
  "snippet": "Joe Kropschot submitted Nick Klein with an inverted triangle at UFC Vegas 123, then used his post-fight interview to ask Dana White for money. The 31-year-old is getting married five days after his Octagon debut, and he made his pitch to Daniel Cormier on camera: Man, it feels great to get the finish. I need the extra money. I’m getting married five days after this with my fiancée. We’ve been together since I was 16. So maybe an extra 100K bonus would help a lot with that. He is not the first fighter to ask White for help with a wedding. After beating Bryce Mitchell, Jean Silva suggested White…",
  "published": "2026-11-01T15:11:04+00:00"
 }
]
