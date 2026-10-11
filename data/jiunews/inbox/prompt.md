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
  "id": "f11fd9f242e3",
  "region": "jp",
  "source": "CAMPFIRE (キャンプファイヤー)",
  "title": "水戸にブラジリアン柔術ジムを！工事費高騰にも負けたくない！支援をお願いします",
  "snippet": "",
  "published": "2026-10-10T15:45:00+00:00"
 },
 {
  "id": "45434b83ecf4",
  "region": "jp",
  "source": "愛媛新聞",
  "title": "スポーツの秋！ブラジリアン柔術で運動不足解消！",
  "snippet": "",
  "published": "2026-10-10T12:13:11+00:00"
 },
 {
  "id": "dfa01ef4a800",
  "region": "jp",
  "source": "山陽新聞",
  "title": "柔術大会『キン肉マン杯2026』8月開催決定 ゆでたまご嶋田「キッズから大人まで。白帯から黒帯まで誰でも出場できます」",
  "snippet": "",
  "published": "2026-10-10T08:06:11+00:00"
 },
 {
  "id": "ed17fefe184a",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "玉木宏 １０２歳まで「俳優＆柔術」の生涯現役を宣言「やっていればギネスにも載れるかな」長寿家系の血筋も明かす",
  "snippet": "",
  "published": "2026-10-10T06:12:55+00:00"
 },
 {
  "id": "b4a0005df430",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "玉木宏、祖父は108歳まで生きたと告白 役者・柔術で“生涯現役”を宣言「100歳は越えるかなと勝手に思っている」",
  "snippet": "",
  "published": "2026-10-10T05:57:00+00:00"
 },
 {
  "id": "1243787b9212",
  "region": "jp",
  "source": "四国新聞",
  "title": "柔術全国大会Ｖ、市長に喜び報告 坂出・道場所属の前田選手｜四国新聞WEB朝刊",
  "snippet": "",
  "published": "2026-10-09T12:36:02+00:00"
 },
 {
  "id": "380dcf2791db",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【ROMAN】バーリトゥードで関根“シュレック”秀樹vs.台湾の大魔王、「組技VT」で白木大輔vs.ボグダノフ、リオ五輪グレコ井上智裕vs.アジアカデ柔道優勝の西願寺哲平、ウ...",
  "snippet": "",
  "published": "2026-10-10T05:10:00+00:00"
 },
 {
  "id": "0ca8283e39b9",
  "region": "jp",
  "source": "UQライフ",
  "title": "玉木宏、祖父は102歳まで生きたと告白 役者・柔術で“生涯現役”を宣言「100歳は越えるかなと勝手に思っている」",
  "snippet": "",
  "published": "2026-10-10T06:07:00+00:00"
 },
 {
  "id": "1d018f2a41d2",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "玉木宏、祖父は102歳まで生きたと告白 役者・柔術で“生涯現役”を宣言「100歳は越えるかなと勝手に思っている」 (ENCOUNT)",
  "snippet": "",
  "published": "2026-10-10T05:57:20+00:00"
 },
 {
  "id": "b168a10c4c3a",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "玉木宏 祖父は１０２歳、曽祖父は１０８歳まで生きた長寿一家だった！ 「生涯現役で頑張りたい」",
  "snippet": "",
  "published": "2026-10-10T06:28:00+00:00"
 },
 {
  "id": "ecb4614f9b1e",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ROMAN】バーリトゥードで関根“シュレック”秀樹vs.台湾の大魔王。「組技VT」で白木アマゾン大輔vs.ボグダノフ、リオ五輪グレコ井上智裕vs.アジアカデ柔道優勝の西願寺哲平も！（ゴング格闘技）",
  "snippet": "",
  "published": "2026-10-10T06:17:55+00:00"
 },
 {
  "id": "8dea59ce9b0b",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "“18歳の超新星”虹咲カリナ、メイド服姿を初解禁 カラフルなビキニ姿も披露（オリコン）",
  "snippet": "",
  "published": "2026-10-10T02:05:27+00:00"
 },
 {
  "id": "45bc6a3d17e9",
  "region": "jp",
  "source": "Infoseek",
  "title": "玉木宏「生涯現役」宣言！目標は102歳 大往生の家系明かす「ギネスにも載れるかな」",
  "snippet": "",
  "published": "2026-10-10T07:37:04+00:00"
 },
 {
  "id": "78b4d95e6162",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "玉木宏「生涯現役」宣言！目標は102歳 大往生の家系明かす「ギネスにも載れるかな」（スポニチアネックス）",
  "snippet": "",
  "published": "2026-10-10T07:33:32+00:00"
 },
 {
  "id": "df0294689c2b",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "玉木宏「人によって心は豊かになるんだと感じさせてくれる映画」声優を務めたアニメ映画「どこよりも遠い場所にいる君へ」に手応え",
  "snippet": "",
  "published": "2026-10-10T06:46:00+00:00"
 },
 {
  "id": "66e321b3afd0",
  "region": "jp",
  "source": "日刊スポーツ",
  "title": "玉木宏「『埋めるぞ！』なんて言わない」長寿家系についても告白「100歳は超えるかな…」",
  "snippet": "",
  "published": "2026-10-10T06:49:30+00:00"
 },
 {
  "id": "64e7dd0fe6a4",
  "region": "jp",
  "source": "스타뉴스",
  "title": "\"叩きのめす\"と宣戦布告→\"熱く戦おう\"··· UFC アランvsダンカン「大激突」",
  "snippet": "",
  "published": "2026-10-10T05:41:11+00:00"
 },
 {
  "id": "0490357df75f",
  "region": "jp",
  "source": "T COM（アットティーコム）",
  "title": "“18歳の超新星”虹咲カリナ、メイド服姿を初解禁 カラフルなビキニ姿も披露",
  "snippet": "",
  "published": "2026-10-10T02:05:00+00:00"
 },
 {
  "id": "046fb6d18d66",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "【画像】玉木宏 １０２歳まで「俳優＆柔術」の生涯現役を宣言「やっていればギネスにも載れるかな」長寿家系の血筋も明かす",
  "snippet": "",
  "published": "2026-10-10T06:12:00+00:00"
 },
 {
  "id": "900238f4e219",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "【RIZIN】11・８千葉大会チケット販売開始、王者・神龍誠VSララミーフライ級王座戦など",
  "snippet": "",
  "published": "2026-10-09T15:14:00+00:00"
 },
 {
  "id": "318754ec3527",
  "region": "intl",
  "source": "YouTube",
  "title": "I Tried My BJJ Against an Aikido Master",
  "snippet": "",
  "published": "2026-10-10T15:00:07+00:00"
 },
 {
  "id": "c75510a421a9",
  "region": "intl",
  "source": "UFCESPANOL.com",
  "title": "UFC BJJ 12 Results",
  "snippet": "",
  "published": "2026-10-09T20:21:38+00:00"
 },
 {
  "id": "982c6d71033c",
  "region": "intl",
  "source": "Tehachapi News",
  "title": "Tehachapi Chamber celebrates grand opening",
  "snippet": "",
  "published": "2026-10-09T22:46:57+00:00"
 },
 {
  "id": "63487e586267",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - M/W",
  "snippet": "",
  "published": "2026-10-09T23:10:17+00:00"
 },
 {
  "id": "00480ebaa180",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Marisa Celeste Mercier vs Rachel Noelle Lohr 2026 World Master IBJJF Jiu-Jitsu Championship",
  "snippet": "",
  "published": "2026-10-10T20:05:50+00:00"
 },
 {
  "id": "6edd5fa731f5",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Rodrigo Ribeiro vs Lucas Laet 2026 BJJ Stars 19",
  "snippet": "",
  "published": "2026-10-10T01:39:31+00:00"
 },
 {
  "id": "dc2e88cb0faf",
  "region": "intl",
  "source": "Combat Press",
  "title": "Dana White’s Contender Series Season 10, Week 10 Preview & Predictions",
  "snippet": "",
  "published": "2026-10-09T15:59:00+00:00"
 },
 {
  "id": "cf20a5ed0387",
  "region": "intl",
  "source": "EssentiallySports",
  "title": "Mikey Musumeci Vacates UFC BJJ Title to Focus on MMA Debut",
  "snippet": "",
  "published": "2026-10-10T06:32:00+00:00"
 },
 {
  "id": "d88c21b4109a",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Mikey Musumeci Vacates UFC BJJ Title To Prioritize MMA Training",
  "snippet": "",
  "published": "2026-10-10T02:21:42+00:00"
 },
 {
  "id": "fdc281eda005",
  "region": "intl",
  "source": "BJJDOC",
  "title": "50-Year-Old John Danaher Black Belt Details His Advice for Training Every Day Despite Injuries",
  "snippet": "",
  "published": "2026-10-10T10:44:26+00:00"
 },
 {
  "id": "cdda1250a145",
  "region": "intl",
  "source": "BJJEE",
  "title": "Draculino: “The Technical Level Of BJJ Nowadays Compared To My Time Is Infinitely Better Now”",
  "snippet": "Draculino has watched Brazilian Jiu-Jitsu grow from its grassroots days in Barra da Tijuca into a technical, global sport. On The Resilient Show, he compared the old school with the modern game and gave today’s athletes full credit: The technical level of Jiu-Jitsu people nowadays compared to my time is infinitely better now. I’m not going to be one of those guys: “Oh, in my time everybody was better now.” It’s not such a thing. It’s progress. The real difference, in his view, is not technical – it is philosophical: What changed now, a little bit more than anything, is the philosophy. The phil…",
  "published": "2026-10-10T09:45:52+00:00"
 },
 {
  "id": "45f1615caddc",
  "region": "intl",
  "source": "BJJEE",
  "title": "FloGrappling GM Ben Kovacs Says UFC BJJ Is Losing Money: “Doesn’t Math Out”",
  "snippet": "FloGrappling general manager Ben Kovacs says the economics of professional grappling rarely add up, and that UFC BJJ is a prime example. He laid out the case on The Ageless Warrior Lab with host Dave Meyer, starting with the live show: I think we need to shorten the events. People just don’t care about 99.999% of Jiu-Jitsu. They only care about certain matchups and high-stakes things. He named F2W as one of the few promotions that pencils out: It’s a lot, and everybody’s selling their own tickets… He has very controlled venue costs. He gets people to sell the tickets for him. He doesn’t offer…",
  "published": "2026-10-10T09:36:54+00:00"
 }
]
