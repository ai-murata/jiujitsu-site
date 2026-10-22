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
  "id": "96d86518e7fd",
  "region": "jp",
  "source": "奈良新聞デジタル",
  "title": "奈良県五條市長らに世界一報告 IBJJF柔術コンキッズ出場の津曲(五條東小6年)",
  "snippet": "",
  "published": "2026-10-21T21:00:00+00:00"
 },
 {
  "id": "a7983386cb24",
  "region": "jp",
  "source": "神戸新聞",
  "title": "伊丹のブラジリアン柔術家・田中さん、世界大会優勝を報告 弟子の西山さんは全国V 市役所訪問|阪神",
  "snippet": "",
  "published": "2026-10-21T20:10:00+00:00"
 },
 {
  "id": "c7b7328dd23b",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "総合格闘家のロー・ティ・フンは、柔術の競技に出場することを選んだ。",
  "snippet": "",
  "published": "2026-10-21T11:07:16+00:00"
 },
 {
  "id": "ff5b6abc7f6f",
  "region": "jp",
  "source": "TBS NEWS DIG",
  "title": "【選手一覧】柔術 丹羽飛龍・吉永愛など 日本代表選手 【アジア大会2026】",
  "snippet": "",
  "published": "2026-10-20T22:29:00+00:00"
 },
 {
  "id": "66ad4440094e",
  "region": "jp",
  "source": "Laodong.vn",
  "title": "「MMA先生」ロー・ティ・フンが2026年全国体育大会で柔術を披露",
  "snippet": "",
  "published": "2026-10-21T11:40:31+00:00"
 },
 {
  "id": "67f23fafa4a9",
  "region": "jp",
  "source": "매일경제",
  "title": "「柔術」ユ·スヨンが2026年10月、カナダアルバータ州エドモントンのロジャースプレイスでUFCファイトナイト291開幕戦バンタム級試合勝利後喜んでいる。 UFC通算戦績は3勝1敗となった。 写真=TKO",
  "snippet": "",
  "published": "2026-10-21T12:57:15+00:00"
 },
 {
  "id": "f3d29f033f5b",
  "region": "jp",
  "source": "イーファイト",
  "title": "一本負けのはずが…抗議で続行させ、なんと逆転KO勝ち！世界で物議",
  "snippet": "",
  "published": "2026-10-21T10:54:28+00:00"
 },
 {
  "id": "bb38f56cb10a",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "日本が男子団体世界選手権で3連覇を達成した。",
  "snippet": "",
  "published": "2026-10-21T05:48:22+00:00"
 },
 {
  "id": "4b543acfbe7b",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "【パラパワーリフティング 男子49kg級 決勝】42歳、まだ終わらない。レジェンドがつかんだ銀",
  "snippet": "",
  "published": "2026-10-21T04:58:10+00:00"
 },
 {
  "id": "bf38f47415d5",
  "region": "jp",
  "source": "efight.jp",
  "title": "バックチョーク入った！と思ったら空中バックドロップで返され失神KO負け！前代未聞の衝撃シーン",
  "snippet": "",
  "published": "2026-10-21T03:54:22+00:00"
 },
 {
  "id": "200b58a16f2a",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "石井慧が現役復帰を決断！元ＰＦＬ王者との対戦で「手応えつかんだ」２年ぶりＭＭＡは〝最終章〟",
  "snippet": "",
  "published": "2026-10-20T20:00:02+00:00"
 },
 {
  "id": "2a7718630095",
  "region": "jp",
  "source": "Howl.link",
  "title": "青帯はブルーになりやすいから青なんだ - SPINS of spinmaster | stand.fm",
  "snippet": "",
  "published": "2026-10-21T22:31:13+00:00"
 },
 {
  "id": "d072f50f01a4",
  "region": "jp",
  "source": "Howl.link",
  "title": "表敬訪問と整体師について思うこと - SPINS of spinmaster | stand.fm",
  "snippet": "",
  "published": "2026-10-21T10:41:01+00:00"
 },
 {
  "id": "418ef6b8a314",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "「ONE SAMURAI 5」 の追加対戦カード4試合を発表！ONEストロー級総合格闘技 和田竜光 vs",
  "snippet": "",
  "published": "2026-10-21T17:51:22+00:00"
 },
 {
  "id": "6a5eadc1396e",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "この登山ゲーム、ジャンプができない!?BitSummitで「ファミ通賞」など2冠の『Mount",
  "snippet": "",
  "published": "2026-10-20T12:48:29+00:00"
 },
 {
  "id": "bde93cf893ab",
  "region": "jp",
  "source": "Howl.link",
  "title": "TAMURA☆GENE☆(HEAT-UP) (@tamgeneHU) on X",
  "snippet": "",
  "published": "2026-10-21T11:28:21+00:00"
 },
 {
  "id": "cb56ea833f8b",
  "region": "intl",
  "source": "FloGrappling",
  "title": "How to Watch: 2027 European Jiu-Jitsu IBJJF Championship | Grappling",
  "snippet": "",
  "published": "2026-10-21T20:53:01+00:00"
 },
 {
  "id": "4c55b0b7c7eb",
  "region": "intl",
  "source": "11Alive.com",
  "title": "5-year-old who beat brain tumor shows toughness through Jiu jitsu",
  "snippet": "",
  "published": "2026-10-21T21:22:00+00:00"
 },
 {
  "id": "e78f1d94ad6f",
  "region": "intl",
  "source": "umlconnector.com",
  "title": "Venum Brazilian Jiu Jitsu Belt – 100% Cotton, Embroidered, Durable BJJ Belt (A1-A4 Sizes)",
  "snippet": "",
  "published": "2026-10-21T17:38:37+00:00"
 },
 {
  "id": "2e8dc504f40d",
  "region": "intl",
  "source": "Consultancy-me.com",
  "title": "Saudi Jiu-Jitsu federation celebrates historic performance at 2026 Asian Games",
  "snippet": "",
  "published": "2026-10-21T12:07:15+00:00"
 },
 {
  "id": "2448f25a3713",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Garry Tonon To Compete In Jiu-Jitsu At Polaris 40",
  "snippet": "",
  "published": "2026-10-21T19:20:49+00:00"
 },
 {
  "id": "4bc3b6e5c1b7",
  "region": "intl",
  "source": "The Times of India",
  "title": "Renzo Gracie’s net worth 2026: Exploring the MMA legend’s career, business ventures, family legacy and mo",
  "snippet": "",
  "published": "2026-10-21T17:00:00+00:00"
 },
 {
  "id": "f81c5d3ca0fd",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "Abu Dhabi Jiu-Jitsu Pro organises three championships in Romania, South Africa, Russia",
  "snippet": "",
  "published": "2026-10-21T10:22:17+00:00"
 },
 {
  "id": "2f60a2eaf87a",
  "region": "intl",
  "source": "The Virginian-Pilot",
  "title": "Suffolk’s Landon Jones earns chance to compete for WBC Muay Thai national championship",
  "snippet": "",
  "published": "2026-10-20T22:11:24+00:00"
 },
 {
  "id": "8c8264b77933",
  "region": "intl",
  "source": "Manx Radio",
  "title": "Jiu-Jitsu: Island youngster claims another medal",
  "snippet": "",
  "published": "2026-10-21T14:26:00+00:00"
 },
 {
  "id": "833e5371e497",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - W/M",
  "snippet": "",
  "published": "2026-10-20T17:38:05+00:00"
 },
 {
  "id": "74a13b391cf4",
  "region": "intl",
  "source": "Neos Kosmos",
  "title": "Ilias Boursinos claims double gold at Pan Pacific Jiu-Jitsu Championships",
  "snippet": "",
  "published": "2026-10-21T03:07:49+00:00"
 },
 {
  "id": "b5c7c38221c4",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "ACBJJ 23 announces two exciting new matchups for Nov. 13",
  "snippet": "",
  "published": "2026-10-21T22:48:38+00:00"
 },
 {
  "id": "8f7b6ec1efdb",
  "region": "intl",
  "source": "FloWrestling",
  "title": "Vincent Palombo",
  "snippet": "",
  "published": "2026-10-21T12:42:42+00:00"
 },
 {
  "id": "194433ed08e0",
  "region": "intl",
  "source": "FloWrestling",
  "title": "Daniel Mata",
  "snippet": "",
  "published": "2026-10-21T14:41:34+00:00"
 },
 {
  "id": "74c70318b168",
  "region": "intl",
  "source": "FloWrestling",
  "title": "Joseph Ivancich",
  "snippet": "",
  "published": "2026-10-21T05:02:09+00:00"
 },
 {
  "id": "3ea435ae36c1",
  "region": "intl",
  "source": "Western Cape Government",
  "title": "Cara du Plessis is embracing challenges on and off the field",
  "snippet": "",
  "published": "2026-10-21T11:09:40+00:00"
 },
 {
  "id": "c4e12e829717",
  "region": "intl",
  "source": "Combat Press",
  "title": "UFC 333: Volkanovski vs. Evloev Preview and Predictions",
  "snippet": "",
  "published": "2026-10-21T17:37:13+00:00"
 },
 {
  "id": "c3aacb49499e",
  "region": "intl",
  "source": "thepress.net",
  "title": "Merab Dvalishvili looks to make history in trilogy bout with Petr Yan at UFC 333: 'Age is just a number'",
  "snippet": "",
  "published": "2026-10-21T18:03:32+00:00"
 },
 {
  "id": "d92a9ee1246b",
  "region": "intl",
  "source": "vijesti.me",
  "title": "Members of the Special Police Unit won 19 medals at the European Police and Firefighters Games",
  "snippet": "",
  "published": "2026-10-21T08:12:13+00:00"
 },
 {
  "id": "aea16ac18452",
  "region": "intl",
  "source": "Sportskeeda",
  "title": "\"His jiu-jitsu is top-notch\"- Islam Makhachev's coach guarantees not to underestimate Carlos Prates",
  "snippet": "",
  "published": "2026-10-21T12:30:00+00:00"
 },
 {
  "id": "2d2afced0abf",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Renato Canuto Wins UFC BJJ 12 Lightweight Title Against Ethan Crelinsten",
  "snippet": "",
  "published": "2026-10-21T16:57:04+00:00"
 },
 {
  "id": "598e33dfca6a",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Gordon Ryan Self Financed Appearance In White Belt Jiu Jitsu Movie",
  "snippet": "",
  "published": "2026-10-21T07:51:14+00:00"
 },
 {
  "id": "60f2e10d1272",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Joe Rogan Is In Awe Of Marcelo Garcia’s Jiu Jitsu",
  "snippet": "",
  "published": "2026-10-21T06:53:06+00:00"
 },
 {
  "id": "8a5211912342",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Roger Gracie Reveals The Biggest Lie In Modern BJJ",
  "snippet": "",
  "published": "2026-10-21T07:49:34+00:00"
 },
 {
  "id": "6531e87ec35b",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Gianni Grippo: Gi Athletes Have Better Guards",
  "snippet": "",
  "published": "2026-10-21T09:48:46+00:00"
 },
 {
  "id": "7e5c690a0e29",
  "region": "intl",
  "source": "BJJEE",
  "title": "Keith Krikorian Says Treating Lower Belts Worse Is Wrong: “My Rank Doesn’t Matter”",
  "snippet": "ADCC star Keith Krikorian says Jiu-Jitsu gyms undercut the values martial arts claim to hold when higher ranks look down on lower ones. He made the case on the Jits and Giggles podcast, comparing it to wider society: I just think in general it’s silly that we live in a kind of a world where rich people think they can treat poor people poorly… Like we kind of have this inverted triangle kind of thing, you know? It was maybe a regular pyramid actually but where you know from top down, the elites look down on the people below them – and I think that’s it should be the opposite. In practice, he sa…",
  "published": "2026-10-21T10:28:34+00:00"
 },
 {
  "id": "b650adc271a1",
  "region": "intl",
  "source": "BJJEE",
  "title": "Gianni Grippo: “No-Gi People’s Guard Retention Isn’t As Strong…”",
  "snippet": "Gianni Grippo argues that Jiu-Jitsu athletes with strong gi foundations develop superior guard retention. Grippo spent around 10 years at Renzo Gracie’s academy, training gi and no-gi equally before leaning toward the gi. He moved to Marcelo Garcia’s academy in 2013, where the focus covered both. But, after the pandemic changed how he trained, he was pulled toward no-gi. After two months of no-gi preparation for a single event, he realized his preference had changed, and he began telling teammates he was still preparing for competitions so he could keep training without the gi. Even so, he str…",
  "published": "2026-10-21T10:22:25+00:00"
 }
]
