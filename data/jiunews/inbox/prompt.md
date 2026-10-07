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
  "id": "c875a4d13f27",
  "region": "jp",
  "source": "東愛知新聞社",
  "title": "ブラジリアン柔術の国際大会で大活躍 御津あおば高の平野レチシアさんが豊川市長へ表敬",
  "snippet": "",
  "published": "2026-10-07T00:00:19+00:00"
 },
 {
  "id": "144ad28ef30a",
  "region": "jp",
  "source": "大分県中津市",
  "title": "ブラジリアン柔術世界大会結果報告会が行われました",
  "snippet": "",
  "published": "2026-10-06T07:09:57+00:00"
 },
 {
  "id": "c9abce8cf5b1",
  "region": "jp",
  "source": "東日新聞",
  "title": "ブラジリアン柔術の国際大会で好成績",
  "snippet": "",
  "published": "2026-10-06T15:01:45+00:00"
 },
 {
  "id": "012a35dc0db0",
  "region": "jp",
  "source": "山陽新聞",
  "title": "【ひとフォーカス】ブラジリアン柔術で国際大会優勝の玉井大和さん 「世界に名を広めたい」",
  "snippet": "",
  "published": "2026-10-06T09:40:00+00:00"
 },
 {
  "id": "b48b4b98419d",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "【柔道女子78kg級】階級を変え、教師との二刀流で挑む初の公式戦！渡邊 聖未【アジア大会】",
  "snippet": "",
  "published": "2026-10-06T09:25:44+00:00"
 },
 {
  "id": "45bc3af6d1ab",
  "region": "jp",
  "source": "UFC.com",
  "title": "Renato Canuto Pre-Match Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-06T21:50:03+00:00"
 },
 {
  "id": "aca96c5ed35c",
  "region": "jp",
  "source": "中日新聞Web",
  "title": "体重57キロの小さな力士、でっかい目標 秋場所で初土俵の新道「強いことで有名になりたい」",
  "snippet": "",
  "published": "2026-10-06T09:29:16+00:00"
 },
 {
  "id": "ba39c5916fbe",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "LL・クール・J：8,000億ドル（約126.5兆円）のAIをめぐる問い——規律か、破壊か",
  "snippet": "",
  "published": "2026-10-06T18:08:00+00:00"
 },
 {
  "id": "c0e760faf824",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【Polaris】二冠制覇！ 高橋“SUBMISSION”雄己がEBIに続き、Polarisバンタム級王者に「間に合うのであればUFC BJJ王者マイキーと」",
  "snippet": "",
  "published": "2026-10-06T10:10:00+00:00"
 },
 {
  "id": "f05e8f4f974a",
  "region": "jp",
  "source": "YouTube",
  "title": "アジア競技大会 柔術、日本大敗。とても苦しいが知れて良かった、この10年の間違いと現実。",
  "snippet": "",
  "published": "2026-10-05T17:11:57+00:00"
 },
 {
  "id": "e69fae0138b1",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "【アジア大会 エピローグ】熱狂のトヨタアスリート",
  "snippet": "",
  "published": "2026-10-06T10:00:31+00:00"
 },
 {
  "id": "852b312fb74b",
  "region": "jp",
  "source": "UFC.com",
  "title": "Adele Fornarino Pre-Match Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-06T21:50:03+00:00"
 },
 {
  "id": "73cdc5d6d746",
  "region": "jp",
  "source": "YouTube",
  "title": "僕が柔術を始めた道場の先生に会ってきた",
  "snippet": "",
  "published": "2026-10-06T10:00:00+00:00"
 },
 {
  "id": "38ef74841cfa",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【Polaris】快挙、高橋“SUBMISSION”雄己が黒帯ノーギ世界王者のシェイ・モンタギューに判定勝ちでEBIに続き、バンタム級二冠王者に！ (ゴング格闘技)",
  "snippet": "",
  "published": "2026-10-06T10:37:08+00:00"
 },
 {
  "id": "06ee686c3ad2",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【RIZIN】死闘を制した荒東“怪獣キラー”英貴「時が来たら、仕事はします」×長谷川賢「“押し切っちまえ”が出来なかった」＆「『ファイトする』ということ」",
  "snippet": "",
  "published": "2026-10-06T06:10:00+00:00"
 },
 {
  "id": "2c2ad6d3170d",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "image-1791280197.jpg",
  "snippet": "",
  "published": "2026-10-06T10:26:57+00:00"
 },
 {
  "id": "a0bd8eac6ef8",
  "region": "jp",
  "source": "Howl.Link",
  "title": "三重で格闘技をするなら「𝐍★𝐓𝐑𝐔𝐒𝐓（エヌ・トラスト）」 (@n_trust_mma) on X",
  "snippet": "",
  "published": "2026-10-06T13:40:34+00:00"
 },
 {
  "id": "6c52126b3fb8",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 12: Moura vs Fornarino Results",
  "snippet": "",
  "published": "2026-10-06T22:42:22+00:00"
 },
 {
  "id": "0340f2b7f0c1",
  "region": "intl",
  "source": "Daily Freeman",
  "title": "Midtown Jiu Jitsu competitors earns medals at New Jersey event",
  "snippet": "",
  "published": "2026-10-06T20:30:37+00:00"
 },
 {
  "id": "f3e64dd5ac38",
  "region": "intl",
  "source": "Glenside Local",
  "title": "Berzin BJJ expands into newly renovated space in Wyncote Commons, announces scholarship",
  "snippet": "",
  "published": "2026-10-06T19:22:20+00:00"
 },
 {
  "id": "5dcd0d18b073",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Who Stole The Show At IBJJF No-Gi Pans?",
  "snippet": "",
  "published": "2026-10-06T18:07:31+00:00"
 },
 {
  "id": "1e6f88a72863",
  "region": "intl",
  "source": "UFC.com",
  "title": "Match By Match Preview | UFC BJJ 12: Moura vs Fornarino",
  "snippet": "",
  "published": "2026-10-06T21:45:27+00:00"
 },
 {
  "id": "8ca5b8319a78",
  "region": "intl",
  "source": "MMA Mania",
  "title": "Edson Barboza signs with new promotion less than two months after UFC retirement (and it’s not RAF)",
  "snippet": "",
  "published": "2026-10-06T17:11:05+00:00"
 },
 {
  "id": "7c88458d2b33",
  "region": "intl",
  "source": "UFC.com",
  "title": "Cassia Moura Pre-Match Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-06T22:32:24+00:00"
 },
 {
  "id": "53ded4b68577",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Diego \"Pato\" Oliveira",
  "snippet": "",
  "published": "2026-10-06T19:33:56+00:00"
 },
 {
  "id": "03f141a13a93",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Jeremiah Vance",
  "snippet": "",
  "published": "2026-10-06T05:33:19+00:00"
 },
 {
  "id": "622f6bcbac05",
  "region": "intl",
  "source": "EIN Presswire",
  "title": "New Jersey's Raymond Gramenzi wins IBJJF ‘s Jiu-Jitsu World Title in the Masters 7 Ultra-Heavyweight Division",
  "snippet": "",
  "published": "2026-10-05T18:25:00+00:00"
 },
 {
  "id": "2d68c6f2343f",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship - Videos",
  "snippet": "",
  "published": "2026-10-05T14:36:45+00:00"
 },
 {
  "id": "e1c78d1c84cf",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - Finals - M/W",
  "snippet": "",
  "published": "2026-10-06T05:25:00+00:00"
 },
 {
  "id": "2cc21a6c5ac9",
  "region": "intl",
  "source": "FloGrappling",
  "title": "CBJJE Pan-Am Jiu-Jitsu Championships",
  "snippet": "",
  "published": "2026-10-05T18:01:18+00:00"
 },
 {
  "id": "e2038bd8ab84",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - M/W",
  "snippet": "",
  "published": "2026-10-06T02:52:45+00:00"
 },
 {
  "id": "94d60a2800c3",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu Semi Finals - M/W",
  "snippet": "",
  "published": "2026-10-06T03:30:31+00:00"
 },
 {
  "id": "e78dee6ef966",
  "region": "intl",
  "source": "SunStar Publishing Inc.",
  "title": "Marc Lim proud of Asian Games run",
  "snippet": "",
  "published": "2026-10-05T16:31:16+00:00"
 },
 {
  "id": "cc8ea90da984",
  "region": "intl",
  "source": "97X",
  "title": "Ladies, This Women’s Self-Defense Class in Davenport Is Completely FREE",
  "snippet": "",
  "published": "2026-10-06T11:52:33+00:00"
 },
 {
  "id": "69f76f58b16e",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "Rider Zuchi Stripped Of IBJJF World Title And Suspended For 3 Years",
  "snippet": "",
  "published": "2026-10-06T22:08:16+00:00"
 },
 {
  "id": "a40f7892192f",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Even BJJ’s Top Stars Couldn’t Be Bothered To Stay And Watch Matches",
  "snippet": "",
  "published": "2026-10-05T13:50:52+00:00"
 },
 {
  "id": "3e3075b528c8",
  "region": "intl",
  "source": "BJJDOC",
  "title": "BJJ Black Belt Bruno Formiga Accused of SA And Harassment By Female Students",
  "snippet": "",
  "published": "2026-10-06T13:27:00+00:00"
 },
 {
  "id": "1c707fde29e4",
  "region": "intl",
  "source": "BJJDOC",
  "title": "WATCH: Councilman And BJJ Black Belt Takes Down A Massive Security Guard At A Fundraising Meeting",
  "snippet": "",
  "published": "2026-10-06T13:52:59+00:00"
 },
 {
  "id": "7089fc1c85a9",
  "region": "intl",
  "source": "FASTBREAK.com.ph",
  "title": "Jiu-jitsu artist Luigi Dy draws strength from family after Asian Games defeat",
  "snippet": "",
  "published": "2026-10-06T01:27:08+00:00"
 },
 {
  "id": "ad978eaff077",
  "region": "intl",
  "source": "BJJEE",
  "title": "Daniel Schuardt Reveals His Wife Made Him Choose Kingsway Over Craig Jones’ B Team",
  "snippet": "Daniel Schuardt picked Kingsway over B Team largely because his wife told him to. The Australian, an ADCC 2026 bronze medalist and the man behind the viral “Mussolini lock”, explained in a recent interview why he trained under John Danaher instead of with his longtime friend Craig Jones, and why the call strained that friendship. Schuardt’s then-girlfriend, now his wife, had looked at B Team’s social media and didn’t like what she saw: My wife was like: “I’m not sending you there to go and have a bunch of fun. I’m sending you there to go do work.” My lady saw all the stuff on like the B Team s…",
  "published": "2026-10-06T11:05:48+00:00"
 },
 {
  "id": "ee39eef9825f",
  "region": "intl",
  "source": "BJJEE",
  "title": "Jose Aldo & Marlon Vera Go to A Draw In Quito Grappling Match",
  "snippet": "Jose Aldo and Marlon Vera could not separate themselves in their submission-only grappling match at Hype on Sunday night in Quito, Ecuador. And, well, the 10-minute contest ended in a draw with no finish from either side. The event was a homecoming for Vera. It was his first competition in Ecuador since 2012, and the local crowd watched him take the initiative from the start. For the opening five minutes he chased a takedown, but Aldo planted himself in the corner and shut down every attempt. With half the match gone and nothing to show for it, Vera waved the former UFC champion out to the cen…",
  "published": "2026-10-06T10:47:42+00:00"
 }
]
