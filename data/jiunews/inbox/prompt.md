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
  "id": "f346f32aa7cc",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【PANCRASE】代役ヘニングも欠場で平信一が緊急参戦、菊入正行と対戦。岸田宙大欠場を受け、眞藤源太がBTTのダヴィ・チュンと対戦に＝11月8日（日）ニューピア",
  "snippet": "",
  "published": "2026-10-31T15:10:00+00:00"
 },
 {
  "id": "8d2b6dd2b5f9",
  "region": "jp",
  "source": "イーファイト",
  "title": "『ROMAN6』",
  "snippet": "",
  "published": "2026-10-31T15:06:06+00:00"
 },
 {
  "id": "ac06dc55a47f",
  "region": "jp",
  "source": "京都新聞デジタル",
  "title": "10月31日 大日本武徳会が解散 1946（昭和21）年",
  "snippet": "",
  "published": "2026-10-30T15:00:00+00:00"
 },
 {
  "id": "8a26a0bfc4be",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【RIZIN】失神KO負けのサバテロ戦を経て、五輪銀メダリスト太田忍との再起戦に挑む鹿志村仁之介、青木真也vs.朝倉未来戦から学んだグラップラーの戦い方「前に出る、下がらない」＝11月8日（日）千葉",
  "snippet": "",
  "published": "2026-10-31T06:22:00+00:00"
 },
 {
  "id": "23982c28372c",
  "region": "jp",
  "source": "イーファイト",
  "title": "平本蓮、クレベルの挑発に応戦、大晦日対決か！？ファン期待",
  "snippet": "",
  "published": "2026-10-30T13:57:22+00:00"
 },
 {
  "id": "cf51080b7ad6",
  "region": "jp",
  "source": "Howl.Link",
  "title": "ARTチャレンジ.6",
  "snippet": "",
  "published": "2026-10-31T02:42:39+00:00"
 },
 {
  "id": "0ed4f889bd69",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "肉塊のような奇妙な敵を薙ぎ倒すローグライク・ホードシューター『Neurospasm』配信！",
  "snippet": "",
  "published": "2026-10-31T07:05:00+00:00"
 },
 {
  "id": "fda35d25cc3c",
  "region": "intl",
  "source": "UFC.com",
  "title": "Liam Crelinsten Bowl Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-31T19:12:53+00:00"
 },
 {
  "id": "1ee28365f5fd",
  "region": "intl",
  "source": "Fightomic",
  "title": "Damien Anderson: UFC Record, BJJ Roots and Fighter Profile",
  "snippet": "",
  "published": "2026-10-31T13:37:20+00:00"
 },
 {
  "id": "5959a72b116d",
  "region": "intl",
  "source": "The Mountaineer",
  "title": "Gracie Waynesville Jiu Jitsu to host veterans fundraiser",
  "snippet": "",
  "published": "2026-10-31T04:15:00+00:00"
 },
 {
  "id": "0556661c8d0b",
  "region": "intl",
  "source": "Wicked Local",
  "title": "Optimus BJJ Explains Its Belt Rank and Attendance Card System",
  "snippet": "",
  "published": "2026-10-31T09:06:50+00:00"
 },
 {
  "id": "e9b66b230ded",
  "region": "intl",
  "source": "San Luis Obispo Tribune",
  "title": "World champion jiu-jitsu instructor from SLO County arrested after home burglary",
  "snippet": "",
  "published": "2026-10-30T18:10:06+00:00"
 },
 {
  "id": "f06098caeb45",
  "region": "intl",
  "source": "GMA Network",
  "title": "Jalen Fonacier captures vacant UFC BJJ title",
  "snippet": "",
  "published": "2026-10-31T01:11:08+00:00"
 },
 {
  "id": "8b17b0c77c80",
  "region": "intl",
  "source": "Kayo Sports",
  "title": "Watch Live",
  "snippet": "",
  "published": "2026-10-30T13:45:58+00:00"
 },
 {
  "id": "783900c8a704",
  "region": "intl",
  "source": "Livemint",
  "title": "UAE President light-heartedly offers flydubai hero Smit Machchhar jiu-jitsu lessons — All about the Japanese martial art",
  "snippet": "",
  "published": "2026-10-31T14:20:45+00:00"
 },
 {
  "id": "4f022942e625",
  "region": "intl",
  "source": "BJPenn.com",
  "title": "Kade Ruotolo turns Lionel Messi’s bodyguard into his newest jiu-jitsu student",
  "snippet": "",
  "published": "2026-10-30T20:00:03+00:00"
 },
 {
  "id": "499cacce838a",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Marcelo Garcia: I Got My Blue Belt And I Lost And I Got Put To Sleep In 20 Seconds",
  "snippet": "",
  "published": "2026-10-31T14:53:23+00:00"
 },
 {
  "id": "fbea78c65f76",
  "region": "intl",
  "source": "NewsBytes",
  "title": "UAE President invites injured flydubai pilot to jiu-jitsu training",
  "snippet": "",
  "published": "2026-10-31T15:02:35+00:00"
 },
 {
  "id": "c202176d2217",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Gui Mendez Shares Advice He’d Take “If He Were to Start Over From White Belt”",
  "snippet": "",
  "published": "2026-10-31T10:49:48+00:00"
 },
 {
  "id": "d977d80b7bfc",
  "region": "intl",
  "source": "FASTBREAK.com.ph",
  "title": "Jalen Fonacier makes history as first Pinoy UFC ‘BJJ’ champ",
  "snippet": "",
  "published": "2026-10-30T14:24:23+00:00"
 },
 {
  "id": "2113f4ec9786",
  "region": "intl",
  "source": "BJJEE",
  "title": "Gracie Barra Instructor D*es After Physical Altercation With His Brother",
  "snippet": "Brian DeMuro, a 47-year-old Brazilian Jiu-Jitsu black belt and owner of Gracie Barra Knightdale, died Sunday evening after a physical confrontation with his brother at his home in Johnston County, North Carolina. According to the Johnston County Sheriff’s Office , deputies were called to a residence on Sunny Dale Drive near Middlesex around 4:59 p.m. over an altercation between two brothers. DeMuro’s brother had come to visit their 77-year-old mother, who was staying with Brian. Investigators say a physical dispute broke out between the siblings. During it, authorities report, DeMuro tried to…",
  "published": "2026-10-31T19:04:26+00:00"
 },
 {
  "id": "2ca633713936",
  "region": "intl",
  "source": "BJJEE",
  "title": "Craig Jones Says The IBJJF Points System Rewards The Wrong Kind Of Control",
  "snippet": "Craig Jones argues that IBJJF scoring misreads what control means in grappling. In his Power Ride instructional, he says the system was built around positions assumed to be strong for ground and pound, yet those positions rarely produce finishes in modern MMA. His main criticism is that side control, mount and back control ignore where an opponent’s movement comes from: the legs. A bottom player who can plant their feet can bridge, hip escape and explode out, regardless of what the top player holds. Jones points to Khabib Nurmagomedov as evidence, noting that he stays on top of the legs from h…",
  "published": "2026-10-31T17:51:43+00:00"
 }
]
