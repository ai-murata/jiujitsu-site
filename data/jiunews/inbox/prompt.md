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
  "id": "e1c4739ab76f",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE】ガリットチュウ福島が電撃参戦！朝倉未来らの柔術コーチ務める国内最高峰グラップラーと激突（スポニチアネックス）",
  "snippet": "",
  "published": "2026-10-07T19:01:12+00:00"
 },
 {
  "id": "3d76cf434581",
  "region": "jp",
  "source": "北海道新聞デジタル",
  "title": "札日大高・高橋さん 世界大会Ｖ ブラジリアン柔術 競技歴1年半 「勝てる自信あった」",
  "snippet": "",
  "published": "2026-10-07T19:00:00+00:00"
 },
 {
  "id": "6f3bb99fa95d",
  "region": "jp",
  "source": "帝京大学",
  "title": "理工学部の学生が第27回全日本ブラジリアン柔術選手権において準優勝を果たしました",
  "snippet": "",
  "published": "2026-10-07T01:13:48+00:00"
 },
 {
  "id": "c54ad92b224d",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "「ガリットチュウ」福島、「ＯＮＥ ＳＡＭＵＲＡＩ ４」参戦「とんでもないオファーが来たなと思っております…１０・１７有明アリーナ",
  "snippet": "",
  "published": "2026-10-07T22:19:00+00:00"
 },
 {
  "id": "30c9a23950eb",
  "region": "jp",
  "source": "日刊スポーツ",
  "title": "【ONE】ガリットチュウ福島参戦決定！サブミッショングラップリングで黒帯柔術家の竹浦正起と",
  "snippet": "",
  "published": "2026-10-07T10:05:15+00:00"
 },
 {
  "id": "77a8ed2817b1",
  "region": "jp",
  "source": "オリコンニュース",
  "title": "ガリットチュウ福島『ONE』緊急参戦 “朝倉未来の柔術コーチ”竹浦正起とグラップリングマッチ",
  "snippet": "",
  "published": "2026-10-07T10:17:00+00:00"
 },
 {
  "id": "436ddf695083",
  "region": "jp",
  "source": "スポニチ Sponichi Annex",
  "title": "ガリットチュウ福島が朝倉未来などの柔術コーチを務める強豪とグラップリング対決！（C）ONE SAMURAI",
  "snippet": "",
  "published": "2026-10-07T15:35:06+00:00"
 },
 {
  "id": "f9ebd211127d",
  "region": "jp",
  "source": "西スポWEB OTTO!",
  "title": "パーキンソン病に苦しみ…〝400戦無敗の男〟ヒクソン・グレイシー、66歳の稽古姿に「病気に立ち向かう姿すらも神々しい」「これこそが柔術の真髄」の声",
  "snippet": "",
  "published": "2026-10-07T10:50:00+00:00"
 },
 {
  "id": "9b24685b7f09",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "【ONE】ガリットチュウ福島が電撃参戦！朝倉未来らの柔術コーチ務める国内最高峰グラップラーと激突",
  "snippet": "",
  "published": "2026-10-07T09:47:00+00:00"
 },
 {
  "id": "787a3cdf8de5",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "ガリットチュウ福島『ONE』緊急参戦 “朝倉未来の柔術コーチ”竹浦正起とグラップリングマッチ (オリコン)",
  "snippet": "",
  "published": "2026-10-07T10:17:08+00:00"
 },
 {
  "id": "4a40cafb9065",
  "region": "jp",
  "source": "オリコンニュース",
  "title": "画像・写真 | ガリットチュウ福島『ONE』緊急参戦 “朝倉未来の柔術コーチ”竹浦正起とグラップリングマッチ 1枚目",
  "snippet": "",
  "published": "2026-10-07T10:17:00+00:00"
 },
 {
  "id": "f488d6c50a0f",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "“最強芸人”４９歳ガリットチュウ福島、まさかの「ＯＮＥ」参戦が電撃決定 朝倉未来の柔術コーチ・竹浦正起とグラップリング対決「とんでもないオファー来た」",
  "snippet": "",
  "published": "2026-10-07T13:04:00+00:00"
 },
 {
  "id": "ef6992becce8",
  "region": "jp",
  "source": "BOUTREVIEW",
  "title": "ONE SAMURAI 10.17 有明アリーナ：柔術茶帯のガリットチュウ福島善成、朝倉兄弟の寝技コーチ・竹浦正起とグラップリングマッチ",
  "snippet": "",
  "published": "2026-10-07T10:27:51+00:00"
 },
 {
  "id": "c8850b4df3dd",
  "region": "jp",
  "source": "佐賀新聞",
  "title": "【写真・画像】ガリットチュウ福島『ONE』緊急参戦 “朝倉未来の柔術コーチ”竹浦正起とグラップリングマッチ | | オリコンニュース",
  "snippet": "",
  "published": "2026-10-07T10:17:00+00:00"
 },
 {
  "id": "c31a093521bb",
  "region": "jp",
  "source": "YouTube",
  "title": "【FULL FIGHT】松野保奈美 vs リアナ・ラズマン / SJJIF WORLD 2026 【ブラジリアン柔術】Honami Matsuno vs Liyana Razman",
  "snippet": "",
  "published": "2026-10-07T08:24:22+00:00"
 },
 {
  "id": "b4734d370ae6",
  "region": "jp",
  "source": "YouTube",
  "title": "2010年前後に起きた柔術界の産業革命 「モダン柔術」の潮流とは何だったのか！？",
  "snippet": "",
  "published": "2026-10-06T16:52:57+00:00"
 },
 {
  "id": "04d8f459abc9",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "ガリットチュウ福島『ONE』緊急参戦 “朝倉未来の柔術コーチ”竹浦正起とグラップリングマッチ (2026年10月7日掲載)",
  "snippet": "",
  "published": "2026-10-07T10:17:08+00:00"
 },
 {
  "id": "8a4206286320",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "【画像】【ONE】ガリットチュウ福島が電撃参戦！朝倉未来らの柔術コーチ務める国内最高峰グラップラーと激突",
  "snippet": "",
  "published": "2026-10-07T09:47:06+00:00"
 },
 {
  "id": "03a7be7e3b5b",
  "region": "jp",
  "source": "PR TIMES",
  "title": "「ONE SAMURAI 4」 追加対戦カードを発表！ONEライト級サブミッショングラップリング 福島善成 vs 竹浦正起",
  "snippet": "",
  "published": "2026-10-07T09:04:34+00:00"
 },
 {
  "id": "ca6d1b624564",
  "region": "jp",
  "source": "サンスポ",
  "title": "「ONE SAMURAI 4」ガリットチュウ福島善成が参戦！JTTコーチ竹浦正起とグラップリングマッチ",
  "snippet": "",
  "published": "2026-10-07T09:55:05+00:00"
 },
 {
  "id": "9ebd962513d6",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE】ガリットチュウ福島参戦決定！サブミッショングラップリングで黒帯柔術家の竹浦正起と (日刊スポーツ)",
  "snippet": "",
  "published": "2026-10-07T10:05:17+00:00"
 },
 {
  "id": "baf3c75f0a2a",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "“最強芸人”４９歳ガリットチュウ福島、まさかの「ＯＮＥ」参戦が電撃決定 朝倉未来の柔術コーチ・竹浦正起とグラップリング対決「とんでもないオファー来た」 (デイリースポーツ)",
  "snippet": "",
  "published": "2026-10-07T13:04:55+00:00"
 },
 {
  "id": "4ffff3dbdce5",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【ONE】磯嶋祥蔵vs.阿部光太、竹内クレイジーバスター悠vs.西山亮翔、グラップリングで竹浦正起vs.ガリットチュウ福島＝10月17日（土）『ONE SAMURAI 4』有...",
  "snippet": "",
  "published": "2026-10-07T12:10:00+00:00"
 },
 {
  "id": "f0e88026fbfb",
  "region": "jp",
  "source": "au Webポータル",
  "title": "“最強芸人”49歳ガリットチュウ福島、まさかの「ONE」参戦が電撃決定 朝倉未来の柔術コーチ・竹浦正起とグラップリング対決「とんでもないオファー来た」",
  "snippet": "",
  "published": "2026-10-07T13:03:00+00:00"
 },
 {
  "id": "8bbae2f3d653",
  "region": "jp",
  "source": "サンスポ",
  "title": "「ONE SAMURAI 4」ガリットチュウ福島善成が参戦！JTTコーチ竹浦正起とグラップリングマッチ（写真・画像 1/1）",
  "snippet": "",
  "published": "2026-10-07T09:55:05+00:00"
 },
 {
  "id": "0cb7b40ac1a3",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "“最強芸人”４９歳ガリットチュウ福島、まさかの「ＯＮＥ」参戦が電撃決定 朝倉未来の柔術コーチ・竹浦正起とグラップリング対決「とんでもないオファー来た」 (2026年10月7日掲載)",
  "snippet": "",
  "published": "2026-10-07T14:40:39+00:00"
 },
 {
  "id": "9bc2eb05e874",
  "region": "intl",
  "source": "Community Impact Newspaper",
  "title": "New Blitz Flow Brazilian Jiu Jitsu studio opens in Friendswood",
  "snippet": "",
  "published": "2026-10-07T20:03:11+00:00"
 },
 {
  "id": "595d7f396fcb",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Here's Why To Get A FloGrappling Subscription",
  "snippet": "",
  "published": "2026-10-07T09:00:04+00:00"
 },
 {
  "id": "babb101095f1",
  "region": "intl",
  "source": "MMA Sucka",
  "title": "Adele Fornarino Will Fight for Flyweight Title at UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-07T23:10:10+00:00"
 },
 {
  "id": "b170436ebacd",
  "region": "intl",
  "source": "MMA Mania",
  "title": "Best possible title bout? UFC BJJ 12: Moura vs. Fornarino live stream, results, highlights",
  "snippet": "",
  "published": "2026-10-07T08:30:00+00:00"
 },
 {
  "id": "a3c0cd67a024",
  "region": "intl",
  "source": "Bluefield Daily Telegraph",
  "title": "Asian Games Jiu-jitsu",
  "snippet": "",
  "published": "2026-10-07T05:00:00+00:00"
 },
 {
  "id": "9032e666bb95",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Luke Griffith Makes A Comeback With A Submission In The ADCC Finals | Submission Of The Month (September)",
  "snippet": "",
  "published": "2026-10-07T18:21:39+00:00"
 },
 {
  "id": "e2ab16eeec5e",
  "region": "intl",
  "source": "UFC.com",
  "title": "Renato Canuto Pre-Match Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-07T07:32:30+00:00"
 },
 {
  "id": "76780c54ba79",
  "region": "intl",
  "source": "FloGrappling",
  "title": "What Went Down At Polaris 39? | Full Polaris Recap",
  "snippet": "",
  "published": "2026-10-07T04:55:04+00:00"
 },
 {
  "id": "542242324638",
  "region": "intl",
  "source": "UFC.com",
  "title": "Adele Fornarino Pre-Match Interview | UFC BJJ 12",
  "snippet": "",
  "published": "2026-10-07T07:32:28+00:00"
 },
 {
  "id": "6cc9eca0bc7d",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Caleb Mcallister",
  "snippet": "",
  "published": "2026-10-07T05:38:01+00:00"
 },
 {
  "id": "f2384397f026",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Essential Jiu-Jitsu - Videos",
  "snippet": "",
  "published": "2026-10-06T19:10:42+00:00"
 },
 {
  "id": "5a8c3ecf6a7f",
  "region": "intl",
  "source": "NDTV Sports",
  "title": "Moura vs Fornarino For UFC BJJ 12: Full Fight Card, Date, Time, Live Stream Details",
  "snippet": "",
  "published": "2026-10-07T11:43:02+00:00"
 },
 {
  "id": "ed81d1a03c71",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Who Stole The Show At IBJJF No-Gi Pans?",
  "snippet": "",
  "published": "2026-10-06T16:55:33+00:00"
 },
 {
  "id": "86659c216335",
  "region": "intl",
  "source": "YouTube",
  "title": "Shotgun armbar & K Guard entrances | BJJ In-person Breakdown Series | #2",
  "snippet": "",
  "published": "2026-10-06T15:46:04+00:00"
 },
 {
  "id": "05e7628780ad",
  "region": "intl",
  "source": "openPR.com",
  "title": "Sydney's Premier BJJ Community Expands with Official Opening of Locals Jiu Jitsu Marrickville",
  "snippet": "",
  "published": "2026-10-07T09:24:04+00:00"
 },
 {
  "id": "0abac1bcdcfa",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Kabuto Issues Statement After He Was Paralyzed At A BJJ Competition",
  "snippet": "",
  "published": "2026-10-07T15:22:14+00:00"
 },
 {
  "id": "87c1e121d232",
  "region": "intl",
  "source": "Politiko Visayas",
  "title": "Cebu mayor honors local jiu-jitsu medalists",
  "snippet": "",
  "published": "2026-10-07T05:49:35+00:00"
 },
 {
  "id": "9cef38021d07",
  "region": "intl",
  "source": "BJJDOC",
  "title": "UFC BJJ Boss Says Musumeci Looking For 'Easy Matches' After Refusing To Pay For A Worthy Opponent For Him",
  "snippet": "",
  "published": "2026-10-07T09:57:22+00:00"
 },
 {
  "id": "9d3bda7709cc",
  "region": "intl",
  "source": "BJJEE",
  "title": "LL Cool J Discovers The Brutal Reality Of Starting Jiu-Jitsu: “Your Whole World Shatters”",
  "snippet": "Hip-hop icon and actor LL Cool J has joined the growing list of celebrities discovering just how humbling Brazilian Jiu-Jitsu can be. During a recent appearance on The Joe Rogan Experience , LL Cool J revealed that he has recently begun training Jiu-Jitsu in Brooklyn — and he’s learning under an instructor with one of the most respected lineages in the sport. His teacher is Brian Glick , a longtime Brazilian Jiu-Jitsu black belt under John Danaher and Renzo Gracie . Glick has spent decades within the Renzo Gracie lineage and is described as one of Danaher’s longest-running students. When Rogan…",
  "published": "2026-10-07T08:13:32+00:00"
 },
 {
  "id": "bc7c552bbd7e",
  "region": "intl",
  "source": "BJJEE",
  "title": "Rider Zuchi Stripped Of IBJJF World Title & Banned For Three Years",
  "snippet": "Rider Zuchi has lost the first world title of his career. The IBJJF has suspended the heavyweight for three years and wiped out his 2026 World Championship gold after an in-competition drug test came back positive. The sample was collected on May 31, 2026, at the IBJJF World Championship. It showed drostanolone, a drostanolone metabolite (3α-hydroxy-2α-methyl-5α-androstan-17-one) and 19-norandrosterone, a metabolite of nandrolone or other 19-norsteroids, all above the Minimum Reporting Level. USADA announced the sanction, and the IBJJF has since revised its results from the event. The heavywei…",
  "published": "2026-10-07T06:47:32+00:00"
 },
 {
  "id": "c71b5aa3ecc3",
  "region": "intl",
  "source": "BJJEE",
  "title": "Two Former Students Accuse BJJ Black Belt Bruno Formiga Of SA",
  "snippet": "Police in Rio de Janeiro are investigating sexual assault allegations from two former female students against Bruno Leonardo Reis de Souza, 42, a Brazilian Jiu-Jitsu black belt known as Bruno Formiga. He runs Escola Bruno Formiga de Jiu-Jítsu in Tijuca, and the cases remain under judicial confidentiality. The older complainant, now 26, told authorities that Formiga used training techniques and immobilizations to make unwanted physical contact. She also alleges that he assaulted her after she became intoxicated during a May 2025 team trip to São Paulo, and that he bought her emergency contracep…",
  "published": "2026-10-07T06:35:43+00:00"
 },
 {
  "id": "500ca65aa9c9",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "Rider Zuchi Stripped Of IBJJF World Title And Suspended For 3 Years",
  "snippet": "Veteran competitor Rider Zuchi has just been suspended from IBJJF competition for 3 years and stripped of the world title that he just won at the same time. Zuchi tested positive for drostanolone, drostanolone metabolite 3α-hydroxy-2α-methyl-5α-androstan-17-one, and 19-norandrosterone, a metabolite of nandrolone or other 19-norsteroids, detected at a concentration greater than the Minimum Reporting Level. This positive result came from an in-competition drug test conducted at the IBJJF World Championship 2026 on May 31, 2026. Zuchi won a gold medal in the heavyweight division at that event, bu…",
  "published": "2026-10-06T22:03:56+00:00"
 }
]
