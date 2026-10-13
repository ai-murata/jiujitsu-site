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
  "id": "e682729b2391",
  "region": "jp",
  "source": "イーファイト",
  "title": "【ROMAN】関根“シュレック”秀樹が台湾の“大魔王”と激突！『ケンガンアシュラ』コラボで4試合が決定＝11.14東京",
  "snippet": "",
  "published": "2026-10-12T11:55:34+00:00"
 },
 {
  "id": "1f0683a48005",
  "region": "jp",
  "source": "efight.jp",
  "title": "何か付いてる？太もも鍛えるとこうなる！？吉成名高、V2戦へ凄すぎる筋肉",
  "snippet": "",
  "published": "2026-10-12T08:14:27+00:00"
 },
 {
  "id": "883750e2d162",
  "region": "jp",
  "source": "西日本新聞me",
  "title": "玖珠町役場を訪れた原田彩那さん - ［大分県］玖珠町の森中央小6年原田さん 「陸上全国V目指す」 県大会で県記録更新し出場へ - 写真・画像(1/1)",
  "snippet": "",
  "published": "2026-10-11T21:18:10+00:00"
 },
 {
  "id": "4e74b0f551b2",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "PFC】フライ級王者・中西テツオがバンタム級で青木大地に延長判定勝ち。二階級制覇へ。池田貴一がグラップリングフェザー級王者に＝『PFC.42",
  "snippet": "",
  "published": "2026-10-12T12:10:00+00:00"
 },
 {
  "id": "d133c8dabd69",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "image-1791780095.jpg",
  "snippet": "",
  "published": "2026-10-12T04:52:57+00:00"
 },
 {
  "id": "668945146b35",
  "region": "jp",
  "source": "イーファイト",
  "title": "『DEEP HAMAMATSU IMPACT 2026 2nd ROUND』",
  "snippet": "",
  "published": "2026-10-12T13:45:49+00:00"
 },
 {
  "id": "0cb4beef1977",
  "region": "jp",
  "source": "efight.jp",
  "title": "52歳・山本美憂、グラビアで鍛えた美脚！亡き弟KIDへの思い、ジム開設の夢も",
  "snippet": "",
  "published": "2026-10-12T03:16:03+00:00"
 },
 {
  "id": "2c0cf345cd29",
  "region": "jp",
  "source": "Howl.link",
  "title": "不遷流柔術 盛武館 (@fusenryu) on X",
  "snippet": "",
  "published": "2026-10-12T03:31:12+00:00"
 },
 {
  "id": "00e9a06fa552",
  "region": "jp",
  "source": "Mix Vale",
  "title": "柔術家Willian Kabuto選手が体重差40kgの相手から受けた禁止技で頸椎骨折し10時間の手術を経て在宅治療へ",
  "snippet": "",
  "published": "2026-10-12T02:27:32+00:00"
 },
 {
  "id": "96ac82b537e7",
  "region": "jp",
  "source": "Howl.link",
  "title": "20代で柔術を始めて食べていけるのか？",
  "snippet": "",
  "published": "2026-10-12T10:00:01+00:00"
 },
 {
  "id": "26bde73930a5",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "神龍誠vs.トニー・ララミーのフライ級タイトルマッチほか「abc presents RIZIN.55」ABEMA PPVにて全試合生中継決定",
  "snippet": "",
  "published": "2026-10-12T02:39:15+00:00"
 },
 {
  "id": "f3c8d0c13d98",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "eye-catch-1791809505.jpg",
  "snippet": "",
  "published": "2026-10-12T13:06:35+00:00"
 },
 {
  "id": "ba3909608c84",
  "region": "jp",
  "source": "Howl.link",
  "title": "Kanagawa Kickboxing Academy (@KKAcademy227) on X",
  "snippet": "",
  "published": "2026-10-12T00:53:17+00:00"
 },
 {
  "id": "d2871cc0d958",
  "region": "intl",
  "source": "FloGrappling",
  "title": "FloGrappling Streaming Schedule: Oct. 12--18, 2026",
  "snippet": "",
  "published": "2026-10-12T16:43:39+00:00"
 },
 {
  "id": "809c6226b623",
  "region": "intl",
  "source": "Richmond Register",
  "title": "10th Planet Jiu Jitsu Richmond earns top rankings at Fuji BJJ World Championships",
  "snippet": "",
  "published": "2026-10-12T01:32:00+00:00"
 },
 {
  "id": "f569e6c1b53e",
  "region": "intl",
  "source": "WUNC News",
  "title": "Rodrigo Amarante talks about new music, recording the \"Narcos\" theme and what Brazilian jiu-jitsu taught him",
  "snippet": "",
  "published": "2026-10-12T20:47:00+00:00"
 },
 {
  "id": "f9865b5a270f",
  "region": "intl",
  "source": "Benzinga",
  "title": "Mark Zuckerberg Once Wrote Fencing Sequences in Chemistry Class, Now He’s Into Jiu-Jitsu — Meta Flagged t",
  "snippet": "",
  "published": "2026-10-12T01:15:59+00:00"
 },
 {
  "id": "bbb3b49951f8",
  "region": "intl",
  "source": "Daily Kos",
  "title": "Talarico Eviscerates Paxton with Masterful Jiu-Jitsu Move while Addressing Mindless MAGA Rumors over his Mental Health [Updated]",
  "snippet": "",
  "published": "2026-10-12T04:04:39+00:00"
 },
 {
  "id": "18f81bc0e82a",
  "region": "intl",
  "source": "KKTV",
  "title": "Former El Paso County deputy now teaching life saving moves decades after she was kidnapped",
  "snippet": "",
  "published": "2026-10-12T00:32:00+00:00"
 },
 {
  "id": "b80690f00399",
  "region": "intl",
  "source": "FloGrappling",
  "title": "UIJJ ADRIATICO BJJ CUP",
  "snippet": "",
  "published": "2026-10-12T03:05:50+00:00"
 },
 {
  "id": "98ed1203da3f",
  "region": "intl",
  "source": "Northampton Chronicle and Echo",
  "title": "Northampton Schoolgirl Crowned European Jiu-Jitsu Champion for Second Year Running",
  "snippet": "",
  "published": "2026-10-12T16:28:00+00:00"
 },
 {
  "id": "7f033d91b4c1",
  "region": "intl",
  "source": "Richmond Register",
  "title": "'Other Mommy' tops the box office with $27.5M; 'The Social Reckoning' opens to $5.5M",
  "snippet": "",
  "published": "2026-10-11T16:28:36+00:00"
 },
 {
  "id": "03844d165a55",
  "region": "intl",
  "source": "Richmond Register",
  "title": "Photos of NFL action from London to Seattle in Week 5",
  "snippet": "",
  "published": "2026-10-12T04:01:12+00:00"
 },
 {
  "id": "a8bc9696679a",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 UIJJ BOLOGNA BJJ CHALLENGE",
  "snippet": "",
  "published": "2026-10-12T00:02:20+00:00"
 },
 {
  "id": "b3b5aa98ae74",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Thamara Ferreira",
  "snippet": "",
  "published": "2026-10-11T20:07:12+00:00"
 },
 {
  "id": "a3582cd16d25",
  "region": "intl",
  "source": "FloGrappling",
  "title": "PBJJF World Jiu-Jitsu Championships",
  "snippet": "",
  "published": "2026-10-12T18:20:29+00:00"
 },
 {
  "id": "3a33d213bea8",
  "region": "intl",
  "source": "Richmond Register",
  "title": "Iran calls latest US response to proposal insufficient, and other Mideast developments",
  "snippet": "",
  "published": "2026-10-11T22:23:20+00:00"
 },
 {
  "id": "898576c320ce",
  "region": "intl",
  "source": "Richmond Register",
  "title": "Isaias moves north into Appalachians and mid-Atlantic; Southern California battered by Rachel",
  "snippet": "",
  "published": "2026-10-12T01:26:39+00:00"
 },
 {
  "id": "e700ad3243c4",
  "region": "intl",
  "source": "Richmond Register",
  "title": "Pennsylvania shooter who killed 8 was family’s patriarch, father of toddler killed says",
  "snippet": "",
  "published": "2026-10-11T22:55:35+00:00"
 },
 {
  "id": "5595c6fd0a68",
  "region": "intl",
  "source": "Richmond Register",
  "title": "Georgia takes over at No. 1 in AP Top 25 with Notre Dame, Miami next; Oregon is out of the poll",
  "snippet": "",
  "published": "2026-10-11T18:00:38+00:00"
 },
 {
  "id": "9a2c9795f09a",
  "region": "intl",
  "source": "وكالة الأنباء السعودية",
  "title": "Abdullah Nada Wins Saudi Arabia's Third Gold at Nagoya Asian Games",
  "snippet": "",
  "published": "2026-10-11T16:01:51+00:00"
 },
 {
  "id": "0494aac5e3d8",
  "region": "intl",
  "source": "Nottinghamshire Police",
  "title": "Assistant Chief Officer Efe Eruero",
  "snippet": "",
  "published": "2026-10-12T22:55:33+00:00"
 },
 {
  "id": "0e127f531db4",
  "region": "intl",
  "source": "BJJDOC",
  "title": "BJJ Black Belt Slammed For Sending Smaller Female To The ER",
  "snippet": "",
  "published": "2026-10-12T17:03:21+00:00"
 },
 {
  "id": "bf6693703d73",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Prosecutor Who Trains Jiu-Jitsu Triggered Police Investigation Into Incident That Paralyzed Kabuto",
  "snippet": "",
  "published": "2026-10-12T09:21:19+00:00"
 },
 {
  "id": "ce46dc1631ae",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Lucas Kanard Credits John Danaher Training Session With Defeating ADCC Gold Medalist Matheus Diniz",
  "snippet": "",
  "published": "2026-10-12T08:20:56+00:00"
 },
 {
  "id": "8cd471236785",
  "region": "intl",
  "source": "Mix Vale",
  "title": "Willian Kabuto Masuda recovers at home while police investigate illegal jiu-jitsu slam",
  "snippet": "",
  "published": "2026-10-12T02:27:32+00:00"
 },
 {
  "id": "722fdf3e6f83",
  "region": "intl",
  "source": "BJJEE",
  "title": "Windows Signs Kade & Tye Ruotolo In What May Be One Of BJJ’s Biggest Sponsorship Deals Ever",
  "snippet": "Microsoft’s Windows brand has announced a sponsorship with Kade and Tye Ruotolo, a partnership that is likely among the largest the sport of Jiu-Jitsu has seen. Windows unveiled the news in an Instagram post presenting the deal as a collaboration between the brothers and the tech company. A short documentary-style video on YouTube followed, built around the personalities of both athletes. The Ruotolos made their names in Jiu-Jitsu before moving into MMA, and they remain closely tied to the grappling community. Their following comes from technical skill on the mat and charisma away from it, qua…",
  "published": "2026-10-12T09:56:13+00:00"
 },
 {
  "id": "4adfd72884a6",
  "region": "intl",
  "source": "BJJEE",
  "title": "Owen Livesey Says The Training Room Is Afraid Of John Danaher: “He’s Got A Temper”",
  "snippet": "UK judo champion and grappling coach Owen Livesey has given a rare inside account of John Danaher’s New Wave room in Texas, where he trained for two weeks a couple of years ago. Speaking on the Life At The Apex podcast, he said Danaher has a short fuse with the partner he uses to demonstrate technique. Livesey described the dynamic through a judo lens – the coach demonstrates on the same uke every session and does not tolerate mistakes: I was laughing my head off ’cause like, in judo as well, you’ll demonstrate on a partner and he uses the same lad all the time as his partner. And if the lad j…",
  "published": "2026-10-12T09:40:33+00:00"
 }
]
