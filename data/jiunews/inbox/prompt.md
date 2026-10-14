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
  "id": "445962e7470d",
  "region": "jp",
  "source": "アラブニュース",
  "title": "アブダビでのハリード・ビン・モハメッド・ビン・ザイード柔術選手権でシーズンタイトルがかかる",
  "snippet": "",
  "published": "2026-10-14T11:21:52+00:00"
 },
 {
  "id": "64899a9c96f7",
  "region": "jp",
  "source": "sakhaparliament.ru",
  "title": "日本最大のブランド希少！柔術着 grips AMAZONA 女性用その他",
  "snippet": "",
  "published": "2026-10-14T10:13:19+00:00"
 },
 {
  "id": "14191205a084",
  "region": "jp",
  "source": "BOUTREVIEW",
  "title": "PFC 10.11 札幌PODアリーナ（結果）：フライ級王者 中西テツオ、バンタム級ランカーの青木大地に延長判定勝ち。池田貴一がグラップリング・フェザー級王者に。藏田圭介改め藏田家工房、13年ぶり試合で判定勝ち",
  "snippet": "",
  "published": "2026-10-14T12:04:09+00:00"
 },
 {
  "id": "cbb1bdefa653",
  "region": "jp",
  "source": "MMOEXP",
  "title": "ARC Raiders最新アップデート徹底解説！PvEモード期間限定テスト開始、Frozen Trail後の変更点と不具合修正まとめ",
  "snippet": "",
  "published": "2026-10-14T05:16:50+00:00"
 },
 {
  "id": "bb6c6646db0a",
  "region": "intl",
  "source": "EastBayRI.com",
  "title": "Bristol student wins Jiu-Jitsu gold",
  "snippet": "",
  "published": "2026-10-14T16:00:03+00:00"
 },
 {
  "id": "a6a0fed80a72",
  "region": "intl",
  "source": "Theprp.com",
  "title": "Official Ozzy Osbourne Jiu-Jitsu Gear & Streetwear Coming Via Half Sumo",
  "snippet": "",
  "published": "2026-10-14T20:39:15+00:00"
 },
 {
  "id": "8882748f0df0",
  "region": "intl",
  "source": "BLABBERMOUTH.NET",
  "title": "OZZY OSBOURNE And HALF SUMO Launch First Official OZZY Jiu-Jitsu Collection",
  "snippet": "",
  "published": "2026-10-14T16:57:46+00:00"
 },
 {
  "id": "d5ebca18bf4c",
  "region": "intl",
  "source": "WFIW",
  "title": "ELEVATION JIU JITSU TO HOLD GRAND OPENING AND RIBBON CUTTING SATURDAY",
  "snippet": "",
  "published": "2026-10-14T11:03:06+00:00"
 },
 {
  "id": "6589bf0a3b93",
  "region": "intl",
  "source": "Lohud",
  "title": "Optimus BJJ Helps Parents Compare Kids Martial Arts Options",
  "snippet": "",
  "published": "2026-10-14T04:33:10+00:00"
 },
 {
  "id": "01af44816ade",
  "region": "intl",
  "source": "San Diego Union-Tribune",
  "title": "Young Poway athlete wins eighth jiu-jitsu gold medal",
  "snippet": "",
  "published": "2026-10-14T01:26:50+00:00"
 },
 {
  "id": "b6a61a5132e2",
  "region": "intl",
  "source": "Arab News",
  "title": "Season title on the line at Khaled bin Mohamed bin Zayed Jiu-Jitsu Championship in Abu Dhabi",
  "snippet": "",
  "published": "2026-10-14T05:52:22+00:00"
 },
 {
  "id": "f1655722f88c",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Lucas Norat",
  "snippet": "",
  "published": "2026-10-14T16:55:11+00:00"
 },
 {
  "id": "44a8cf154be4",
  "region": "intl",
  "source": "Metal Injection",
  "title": "Half Sumo Launches First Ever Ozzy Osbourne Jiu-Jitsu Collection",
  "snippet": "",
  "published": "2026-10-13T19:11:18+00:00"
 },
 {
  "id": "f88a19ed6aa4",
  "region": "intl",
  "source": "헤럴드경제",
  "title": "'Yoo Jiu-jitsu' Yoo Su-young targets third UFC win, vows to prove Korean fighters' worth",
  "snippet": "",
  "published": "2026-10-14T03:09:33+00:00"
 },
 {
  "id": "3f14dbc153e0",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Lucas Gualberto Gomes Nascimento",
  "snippet": "",
  "published": "2026-10-13T21:50:38+00:00"
 },
 {
  "id": "1fa6d33658c3",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "Abu Dhabi Jiu-Jitsu Pro organises 9 championships across three continents in just three days",
  "snippet": "",
  "published": "2026-10-14T11:41:12+00:00"
 },
 {
  "id": "6bc7acf113d6",
  "region": "intl",
  "source": "www.wam.ae",
  "title": "UAE Jiu-Jitsu Federation announces championship final round, awards ceremony",
  "snippet": "",
  "published": "2026-10-14T05:52:24+00:00"
 },
 {
  "id": "8b5d769b0eb1",
  "region": "intl",
  "source": "Turkmenportal.com",
  "title": "Turkmen athletes won 16 medals at the World Jiu-Jitsu Championships in Antalya",
  "snippet": "",
  "published": "2026-10-14T04:12:52+00:00"
 },
 {
  "id": "df492fd03234",
  "region": "intl",
  "source": "Chaoszine",
  "title": "Half Sumo releases first official Ozzy Osbourne martial arts apparel line",
  "snippet": "",
  "published": "2026-10-14T18:40:31+00:00"
 },
 {
  "id": "c76d756a840b",
  "region": "intl",
  "source": "Legacy | Obituary",
  "title": "Benjamin Brotherton Obituary (2026) - Poca, WV - Charleston Gazette-Mail",
  "snippet": "",
  "published": "2026-10-14T00:58:09+00:00"
 },
 {
  "id": "f2d942200621",
  "region": "intl",
  "source": "BJJDOC",
  "title": "80 Year Old Awarded BJJ Black Belt",
  "snippet": "",
  "published": "2026-10-14T20:47:41+00:00"
 },
 {
  "id": "09bce7f7ee95",
  "region": "intl",
  "source": "BJJDOC",
  "title": "BJJ Gym Owner Jailed For SA Committed During Private Lesson",
  "snippet": "",
  "published": "2026-10-14T14:41:30+00:00"
 },
 {
  "id": "b589513d6adf",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Dima Murovanni Explains How ADCC 2026 Changed The Trajectory Jiu-Jitsu Is On",
  "snippet": "",
  "published": "2026-10-14T07:24:35+00:00"
 },
 {
  "id": "3cdc2a739609",
  "region": "intl",
  "source": "BJJDOC",
  "title": "MMA Analyst Gives His Honest Take On Mikey Musumeci MMA Transition",
  "snippet": "",
  "published": "2026-10-14T11:16:38+00:00"
 },
 {
  "id": "fd90c7633014",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Keith Krikorian Comes Out Against Banning Students From Dating Each Other: It's a Little Bit Culty",
  "snippet": "",
  "published": "2026-10-14T18:18:38+00:00"
 },
 {
  "id": "7d0aed852f96",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Nolan Stuart Returns To Defend IBJJF Crown Heavyweight Title",
  "snippet": "",
  "published": "2026-10-14T13:58:48+00:00"
 },
 {
  "id": "22ed01f63c3d",
  "region": "intl",
  "source": "Haberler.com",
  "title": "'Tarzan' wrestled a 6-meter-long giant python: I really had a very close call.",
  "snippet": "",
  "published": "2026-10-14T10:52:40+00:00"
 },
 {
  "id": "8ebc7037f0b2",
  "region": "intl",
  "source": "BJJEE",
  "title": "Demetrious Johnson Says He Would Ban Heel Hooks In MMA: “Can Ruin Someone’s Career”",
  "snippet": "Demetrious Johnson wants oblique kicks banned from MMA, and he says heel hooks should go with them. The MMA legend made his case in a sit-down with Ariel Helwani, comparing the two techniques as similarly risky. Josh Barnett was among those who pushed back on that comparison. Asked whether oblique kicks should be outlawed, Johnson answered plainly: I think so… Because it can ruin somebody’s career… I would ban heel hooks too. He said he avoids both moves himself because he always has another way to finish: I don’t do heel hooks and I don’t do oblique kicks, because there’s another way I can ta…",
  "published": "2026-10-14T21:51:03+00:00"
 },
 {
  "id": "85f5428320c9",
  "region": "intl",
  "source": "BJJEE",
  "title": "Judo Champion Kayla Harrison Reveals She Has Five Herniated Discs: “Couldn’t Lift My Arm”",
  "snippet": "UFC champion Kayla Harrison has detailed the neck surgery that threatened her preparation for her November 14 fight with Amanda Nunes. On a recent podcast, she said she learned she had five herniated discs only after she was on the operating table, having expected a different procedure: It was rough at the beginning… I went 10 years without having surgery (and) in the last four years I’ve had four surgeries back to back – and this one was the most serious. And I kind of was just, like, am I ever going to be okay again? It got to the point where I was questioning if I was ever going to feel lik…",
  "published": "2026-10-14T21:46:47+00:00"
 }
]
