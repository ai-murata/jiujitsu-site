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
  "id": "5d44935f414a",
  "region": "jp",
  "source": "WEBザテレビジョン",
  "title": "＜刃牙道＞テレビ番組に出演した武蔵がキャスターを気絶させ、警視庁は身柄の拘束に動く…第18話あらすじ＆先行カット公開",
  "snippet": "",
  "published": "2026-10-30T10:35:12+00:00"
 },
 {
  "id": "99748f4a21b7",
  "region": "jp",
  "source": "UFC.com",
  "title": "William Tackett Bowl Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-30T03:31:13+00:00"
 },
 {
  "id": "2d537155a365",
  "region": "jp",
  "source": "UFC.com",
  "title": "Jasmine Rocha Bowl Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-30T02:18:10+00:00"
 },
 {
  "id": "d83714e2823e",
  "region": "jp",
  "source": "UFC.com",
  "title": "Nick Rodriguez Bowl Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-30T02:18:10+00:00"
 },
 {
  "id": "3f6f9d920d73",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "【パラ水泳 バタフライ】南井瑛翔２つ目の金｜トゥ・ウェイソンは銅で雪辱を誓う【アジア大会】",
  "snippet": "",
  "published": "2026-10-29T22:32:14+00:00"
 },
 {
  "id": "631f8b36da07",
  "region": "jp",
  "source": "UFC.com",
  "title": "Ffion Davies Bowl Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-30T02:18:10+00:00"
 },
 {
  "id": "6e142aca255a",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "平本蓮、クレベルの挑発に応戦、大晦日対決か！？ファン期待（イーファイト）",
  "snippet": "",
  "published": "2026-10-30T13:55:22+00:00"
 },
 {
  "id": "ba635974049d",
  "region": "jp",
  "source": "MMAPLANET",
  "title": "【UFN292】ハサノフ戦へ、ジャンポール・レバスノヤニ「MMAを戦うには、ベガスに住むのが一番」",
  "snippet": "",
  "published": "2026-10-30T15:07:17+00:00"
 },
 {
  "id": "49c0f91b71fe",
  "region": "jp",
  "source": "au Webポータル",
  "title": "森下文化センターで「漢字あそびフェス」 親子で楽しむ体験企画25種",
  "snippet": "",
  "published": "2026-10-30T14:45:46+00:00"
 },
 {
  "id": "e2fabe11c97e",
  "region": "jp",
  "source": "UFC.com",
  "title": "Liam Crelinsten Bowl Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-30T01:32:53+00:00"
 },
 {
  "id": "c51b4187f547",
  "region": "jp",
  "source": "UFC.com",
  "title": "ジョー・クロプスコット",
  "snippet": "",
  "published": "2026-10-30T15:24:24+00:00"
 },
 {
  "id": "88d4499f7e27",
  "region": "jp",
  "source": "UFC.com",
  "title": "Jalen Fonacier Bowl Interview | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-30T03:31:13+00:00"
 },
 {
  "id": "a706f62bc00b",
  "region": "jp",
  "source": "Howl.Link",
  "title": "Cタケ(40) (@crusher_take) on X",
  "snippet": "",
  "published": "2026-10-30T12:23:45+00:00"
 },
 {
  "id": "891765e14a36",
  "region": "intl",
  "source": "The Des Moines Register",
  "title": "Optimus BJJ Explains Its Belt Rank and Attendance Card System",
  "snippet": "",
  "published": "2026-10-30T23:57:16+00:00"
 },
 {
  "id": "2c456d1e1040",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "UFC BJJ 13 Packs Up a Submission Carnage Thursday Night",
  "snippet": "",
  "published": "2026-10-31T00:23:49+00:00"
 },
 {
  "id": "f73007bfd0a7",
  "region": "intl",
  "source": "San Luis Obispo Tribune",
  "title": "World champion jiu-jitsu instructor from SLO County arrested after home burglary",
  "snippet": "",
  "published": "2026-10-30T18:10:00+00:00"
 },
 {
  "id": "bd82bfeb7dbc",
  "region": "intl",
  "source": "lakeandsumterstyle.com",
  "title": "Young Jiu-Jitsu Athlete Jozlynn Brunson Finds Strength and Confidence",
  "snippet": "",
  "published": "2026-10-30T01:51:19+00:00"
 },
 {
  "id": "b8bad2423266",
  "region": "intl",
  "source": "FloGrappling",
  "title": "SUPERCUT: Every Submission From The 2026 ADCC World Championship",
  "snippet": "",
  "published": "2026-10-30T22:42:47+00:00"
 },
 {
  "id": "cca406936e2b",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "UFC BJJ 13: Jasmine Rocha Secures Lightning-Fast Armbar",
  "snippet": "",
  "published": "2026-10-31T00:23:44+00:00"
 },
 {
  "id": "4ce4228dc485",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Breno Rodrigues vs Hiram Costa Santanna 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-10-30T12:32:33+00:00"
 },
 {
  "id": "afa79575bd00",
  "region": "intl",
  "source": "MMA Mania",
  "title": "Musumeci’s belt goes to Filipino champ, UFC BJJ changes rules after Nicky Rod controversy | UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-30T05:16:00+00:00"
 },
 {
  "id": "fa73a97269cd",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "Ffion Davies Strangles Jaine Fragoso In UFC BJJ First Round",
  "snippet": "",
  "published": "2026-10-30T18:58:45+00:00"
 },
 {
  "id": "1b581170b13d",
  "region": "intl",
  "source": "FloGrappling",
  "title": "GF Team",
  "snippet": "",
  "published": "2026-10-30T14:43:33+00:00"
 },
 {
  "id": "2f9bbe74cc8b",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 13: Tackett vs Rodriguez Results",
  "snippet": "",
  "published": "2026-10-30T02:14:00+00:00"
 },
 {
  "id": "1f0f18a10bae",
  "region": "intl",
  "source": "FloGrappling",
  "title": "John Patrick Collins vs Stefan Dimitrov 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-10-29T22:42:05+00:00"
 },
 {
  "id": "3d1202ae5c68",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Julien Nicolas Doublet vs Raymond Birchall 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-10-30T00:12:06+00:00"
 },
 {
  "id": "532fbd4e9caa",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Marina Anna Gerszewska vs Ilaria Giacomini 2026 IBJJF European NoGi",
  "snippet": "",
  "published": "2026-10-29T16:13:39+00:00"
 },
 {
  "id": "aa19654aeaaf",
  "region": "intl",
  "source": "Kayo Sports",
  "title": "Watch Ufc brazilian jiu-jitsu Live",
  "snippet": "",
  "published": "2026-10-30T03:43:24+00:00"
 },
 {
  "id": "7f33fb48e782",
  "region": "intl",
  "source": "boxingnews.com",
  "title": "Musumeci's Belt Goes To Filipino Teammate After Controversial UFC BJJ 13",
  "snippet": "",
  "published": "2026-10-30T06:00:45+00:00"
 },
 {
  "id": "6f31ff5bdbe3",
  "region": "intl",
  "source": "BJPenn.com",
  "title": "Kade Ruotolo turns Lionel Messi’s bodyguard into his newest jiu-jitsu student",
  "snippet": "",
  "published": "2026-10-30T20:00:03+00:00"
 },
 {
  "id": "9e84a47426f4",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Andrew Tackett Defends UFC BJJ Title Against Chris Wojcik On December 3",
  "snippet": "",
  "published": "2026-10-30T07:17:34+00:00"
 },
 {
  "id": "7f23719e3b29",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "William Tackett Submits Jay Rodriguez In 86 Seconds To Win UFC BJJ Title (Highlights)",
  "snippet": "",
  "published": "2026-10-30T08:30:56+00:00"
 },
 {
  "id": "e47ad554ea85",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Gracie Barra BJJ Black Belt Lost His Life Following Scuffle With His Brother",
  "snippet": "",
  "published": "2026-10-30T14:12:04+00:00"
 },
 {
  "id": "6fbdbdc74710",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Jasmine Rocha Submits Karen Antunes In 38 Seconds At UFC BJJ 13 (Highlights)",
  "snippet": "",
  "published": "2026-10-30T04:32:34+00:00"
 },
 {
  "id": "7104e1b32f53",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Tristan Sainz Submits David Weintraub In UFC BJJ Debut At 19 (Highlights)",
  "snippet": "",
  "published": "2026-10-30T04:32:34+00:00"
 },
 {
  "id": "33d3045b2374",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Liam Crelinsten Heel Hooks Seilkhan Bolatbek At UFC BJJ 13 (Highlights)",
  "snippet": "",
  "published": "2026-10-30T04:32:34+00:00"
 },
 {
  "id": "85696de583c2",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Nick Rodriguez Submits Nata Tenca In Third Round At UFC BJJ 13 (Highlights)",
  "snippet": "",
  "published": "2026-10-30T02:54:24+00:00"
 },
 {
  "id": "55d641956cd0",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Ffion Davies Submits Jaine Fragoso In First Round At UFC BJJ 13 (Highlights)",
  "snippet": "",
  "published": "2026-10-30T02:32:20+00:00"
 },
 {
  "id": "5df758b14e06",
  "region": "intl",
  "source": "BJJEE",
  "title": "Ryan Hall: “BJJ Coaches Bury Students In Tiny Details Before They Know The Fundamentals”",
  "snippet": "Ryan Hall has little patience for Jiu-Jitsu coaches who flood students with technical minutiae while skipping what matters most. Hall argues that some instructors use an endless list of details to look knowledgeable, which leaves students unsure which parts of a technique carry the weight. His objection is not to details themselves, but it is to coaches who fail to rank them. He likened the problem to Maslow’s hierarchy of needs, where there is no point discussing higher-level ideas while basic problems remain unsolved: In my experience, a lot of coaches and a lot of people, particularly guys…",
  "published": "2026-10-30T10:55:57+00:00"
 },
 {
  "id": "78c13d7e00e7",
  "region": "intl",
  "source": "BJJEE",
  "title": "Beatrice Jin: “Being Too Nice In Training Holds You & Your Partner Back”",
  "snippet": "Black belt competitor and coach Beatrice Jin says a common problem in Jiu-Jitsu is not lack of technique or strength – it is holding back, out of fear of looking aggressive or like a bad training partner. Her main distinction is between technique and application. Most Jiu-Jitsu techniques have a legitimate purpose, and a hard crossface is not wrong if the partner can tap or bail before getting hurt. What crosses the line is using size or strength to overwhelm someone with no time to protect themselves. Jin put it this way: There is no such thing as mean techniques, only mean applications… A lo…",
  "published": "2026-10-30T10:47:56+00:00"
 }
]
