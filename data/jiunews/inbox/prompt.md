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
  "id": "f3f73cc9008f",
  "region": "jp",
  "source": "full-count.jp",
  "title": "球団幹部の「神経を逆なでした」 実況アナが契約終了…地元紙が指摘した“背景”",
  "snippet": "",
  "published": "2026-10-27T22:26:00+00:00"
 },
 {
  "id": "c2255e8e9040",
  "region": "jp",
  "source": "efight.jp",
  "title": "井上尚弥と対戦期待のエスピノサ、週末の相手交代に”想定外の強豪”右フックの名手に｢負ける可能性ある｣＝11.1",
  "snippet": "",
  "published": "2026-10-28T04:04:11+00:00"
 },
 {
  "id": "e1e7bd4de006",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【PANCRASE】RIZIN帰りのISAOがONE帰りの後藤亮と対戦。新居すぐるが3年3カ月ぶり復帰で井村塁とグラップラー対決、髙城光弘vs.山口怜臣、3連勝・白井誠司vs.山本歩夢、カマチョvs.菅歩夢など9カード追加＝12月20日（日）",
  "snippet": "",
  "published": "2026-10-28T10:10:00+00:00"
 },
 {
  "id": "4feda8a1782c",
  "region": "jp",
  "source": "Unisba Media",
  "title": "【ONE 試合映像】与座優貴、22cmの身長差をものともせず猛攻！長身王者ナビル・アナンに無念の判定負け『ONE SAMURAI 4』リング映像 Stub Hub (DagEVwDmwG)",
  "snippet": "",
  "published": "2026-10-28T17:41:30+00:00"
 },
 {
  "id": "8d29005725db",
  "region": "jp",
  "source": "Unisba Media",
  "title": "🔥🥋【衝撃】ウルフアロン、ザックに惜敗も大激闘！「一番強いレスラーになる」G1初出場で見せた“怪物級”の実力に会場騒然😱🔥 Ncis (z2xHBAtKQg)",
  "snippet": "",
  "published": "2026-10-27T20:30:41+00:00"
 },
 {
  "id": "ddddf7661772",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 13: Tackett vs Rodriguez Results",
  "snippet": "",
  "published": "2026-10-28T21:38:09+00:00"
 },
 {
  "id": "b355d46b593d",
  "region": "intl",
  "source": "FloGrappling",
  "title": "MARIA LUIZA RODRIGUES DE C. L. vs SINEAD HOPE GOLDING 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-10-28T20:29:23+00:00"
 },
 {
  "id": "369543f5bcef",
  "region": "intl",
  "source": "UFC.com",
  "title": "Match By Match Preview | UFC BJJ 13: Tackett vs Rodriguez",
  "snippet": "",
  "published": "2026-10-27T18:50:16+00:00"
 },
 {
  "id": "cd1c271a4bc5",
  "region": "intl",
  "source": "alphavilleearredores.com.br",
  "title": "RVCA SPORTS Men's DPMX SHOYOROLL Jiu Jitsu Gi alphavilleearredores.com.br",
  "snippet": "",
  "published": "2026-10-28T10:37:48+00:00"
 },
 {
  "id": "64aad17bc317",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Callie Marie Nelson vs Maria Luiza Rodrigues De C. L. S 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-10-28T20:29:17+00:00"
 },
 {
  "id": "28d7b315c7b6",
  "region": "intl",
  "source": "UFC.com",
  "title": "Jasmine Rocha Pre-Match Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-28T07:19:18+00:00"
 },
 {
  "id": "4f0aa52f83a5",
  "region": "intl",
  "source": "FloGrappling",
  "title": "GF Team",
  "snippet": "",
  "published": "2026-10-28T22:39:31+00:00"
 },
 {
  "id": "df6df2aa4265",
  "region": "intl",
  "source": "UFC.com",
  "title": "William Tackett Pre-Match Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-27T19:19:13+00:00"
 },
 {
  "id": "38164c0473ca",
  "region": "intl",
  "source": "boxingnews.com",
  "title": "UFC BJJ 13: Tackett vs Rodriguez — Full Card, Start Time & How to Watch",
  "snippet": "",
  "published": "2026-10-28T12:53:57+00:00"
 },
 {
  "id": "8d56f0f96fa1",
  "region": "intl",
  "source": "Demócrata",
  "title": "Mallorca BJJ & Yoga Festival presents its ninth edition in Andratx",
  "snippet": "",
  "published": "2026-10-28T11:06:49+00:00"
 },
 {
  "id": "352641de392f",
  "region": "intl",
  "source": "boxingnews.com",
  "title": "How to watch UFC BJJ 13: Tackett vs Rodriguez: time, channel and live stream",
  "snippet": "",
  "published": "2026-10-28T12:54:00+00:00"
 },
 {
  "id": "65078fa58058",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Chris Haueter: Originally You Weren’t Allowed To Train No-Gi Until You Were A Purple Belt",
  "snippet": "",
  "published": "2026-10-28T16:11:12+00:00"
 },
 {
  "id": "cf23630ec26c",
  "region": "intl",
  "source": "BJJEE",
  "title": "Travis Stevens: “Combat Athletes Need Around 6-7% Body Fat To Cushion Throws”",
  "snippet": "Olympic silver medalist Travis Stevens says chasing the leanest possible physique works against judo players. On a podcast, he argued that body fat acts as protection for athletes who get thrown repeatedly: When athletes get really lean, like I see a lot of athletes work towards like the 1%, 2% body fat as like a, I’m ready to go… But in combat sports, you really want that to be around like 6 or 7%, because we need the cushioning in our body to handle the impact. His view came from managing his own weight. Between the 2012 London Olympics and the 2016 Rio Olympics, his walking weight rose from…",
  "published": "2026-10-28T07:24:50+00:00"
 },
 {
  "id": "c80968e4a487",
  "region": "intl",
  "source": "BJJEE",
  "title": "Kade Ruotolo Books MMA Return After Eight-Month ACL Recovery",
  "snippet": "Kade Ruotolo will return to MMA against Ok Rae Yoon at ONE FN 50 on Friday, December 18! It will be his first fight after an eight-month recovery from a torn ACL that required surgical reconstruction, an injury he suffered while training for an MMA bout. He called it the toughest stretch of his athletic life, and the toll was mental as well as physical: This was for sure the gnarliest injury I can say that I’ve had in my life and the most time off the mats, the most time out the water, most time of everything… Obviously anytime you go through those down times, mentally it’s tough on the mind,…",
  "published": "2026-10-28T07:17:16+00:00"
 }
]
