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
  "id": "f075c0c40969",
  "region": "jp",
  "source": "TBS NEWS DIG",
  "title": "世界大会で3位【 玉木宏 】ブラジリアン柔術 岡田准一も祝福「凄いよ。世界の猛者たち相手に」「イケおじではダントツ優勝だろ」",
  "snippet": "",
  "published": "2026-10-12T18:53:21+00:00"
 },
 {
  "id": "fd6c7ecd6926",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "「ガリットチュウ福島×竹浦正起」マッチメイク「理由」…「ＯＮＥ」チャトリＣＥＯが会見で明かす「一回は躊躇…ファンが求めるものを考慮」…１０・１７有明アリーナ",
  "snippet": "",
  "published": "2026-10-13T10:21:00+00:00"
 },
 {
  "id": "68439f2e465a",
  "region": "jp",
  "source": "YouTube",
  "title": "夏季柔術甲子園2026&第９回全日本 day.1 / MAT 5",
  "snippet": "",
  "published": "2026-10-12T14:27:25+00:00"
 },
 {
  "id": "bb9fc8426391",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "【ONE】ガリットチュウ福島が電撃参戦！グラップリングマッチにチャトリCEO「最初は躊躇した」",
  "snippet": "",
  "published": "2026-10-13T09:58:00+00:00"
 },
 {
  "id": "ff921dd1dcda",
  "region": "jp",
  "source": "スポニチ Sponichi Annex",
  "title": "【記事全文】【ONE】ガリットチュウ福島が電撃参戦！グラップリングマッチにチャトリCEO「最初は躊躇した」",
  "snippet": "",
  "published": "2026-10-13T09:52:00+00:00"
 },
 {
  "id": "b3c1dc9dbe09",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【RIZIN甲子園】勝ち残った12名とは？「第1回トーナメント合格者」11名＋1名が「“理不尽”合宿ステージ」で4名脱落、8名が10月17日（土）「準決勝トーナメント」へ",
  "snippet": "",
  "published": "2026-10-13T03:10:00+00:00"
 },
 {
  "id": "56737aa2fc00",
  "region": "jp",
  "source": "MMAPLANET",
  "title": "【PFL2026#14】カモーシェにアベンジ=最初で最後のPFL世界女子フライ級王座決定戦、ジェナ・ビショップ「日本のファンが試合を見ている姿を見るのが大好き」",
  "snippet": "",
  "published": "2026-10-13T12:53:56+00:00"
 },
 {
  "id": "13ac137ea936",
  "region": "jp",
  "source": "Howl.link",
  "title": "大正時代の沢田健と代田文誌（未発表原稿）｜Nobuyoshi Matsuki",
  "snippet": "",
  "published": "2026-10-13T08:09:32+00:00"
 },
 {
  "id": "a0c4ef10af84",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE】ガリットチュウ福島が電撃参戦！グラップリングマッチにチャトリCEO「最初は躊躇した」（スポニチアネックス）",
  "snippet": "",
  "published": "2026-10-13T09:58:28+00:00"
 },
 {
  "id": "b58d2f603c8f",
  "region": "jp",
  "source": "4Gamer.net",
  "title": "画像ギャラリー No.004 | 3つの武器を切り替えて斬り，グラップリングフックで飛び回る。チリのチームが作るアクションRPG「Atemporal Silentium」［BGS2026］",
  "snippet": "",
  "published": "2026-10-13T09:30:22+00:00"
 },
 {
  "id": "3ac773a4e99e",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "“最強芸人”４９歳ガリットチュウ福島の電撃参戦、ＯＮＥチャトリＣＥＯが言及「一回は躊躇しました」（デイリースポーツ）",
  "snippet": "",
  "published": "2026-10-13T09:29:38+00:00"
 },
 {
  "id": "5a04840b2a26",
  "region": "jp",
  "source": "4Gamer.net",
  "title": "3つの武器を切り替えて斬り，グラップリングフックで飛び回る。チリのチームが作るアクションRPG「Atemporal Silentium」［BGS2026］",
  "snippet": "",
  "published": "2026-10-13T09:04:39+00:00"
 },
 {
  "id": "de808e707232",
  "region": "intl",
  "source": "The Columbus Dispatch",
  "title": "Optimus BJJ Helps Parents Compare Kids Martial Arts Options",
  "snippet": "",
  "published": "2026-10-13T23:07:38+00:00"
 },
 {
  "id": "5dbca06dc9ff",
  "region": "intl",
  "source": "FloGrappling",
  "title": "How to Watch: 2026 BJJ Stars 20 | Grappling",
  "snippet": "",
  "published": "2026-10-13T17:49:36+00:00"
 },
 {
  "id": "6f4bb99b5072",
  "region": "intl",
  "source": "journal-news.net",
  "title": "Freya Jiu Jitsu celebrates grand opening",
  "snippet": "",
  "published": "2026-10-13T17:08:00+00:00"
 },
 {
  "id": "07e36f911d70",
  "region": "intl",
  "source": "WCNC",
  "title": "Love Your Local: Why Brazilian jiu-jitsu is booming in Charlotte",
  "snippet": "",
  "published": "2026-10-13T11:57:00+00:00"
 },
 {
  "id": "0da6dd7f3636",
  "region": "intl",
  "source": "WBONTV",
  "title": "10th Planet Jiu Jitsu Richmond Earns Top Rankings at Fuji BJJ World Championships",
  "snippet": "",
  "published": "2026-10-13T14:49:43+00:00"
 },
 {
  "id": "72b5c7557732",
  "region": "intl",
  "source": "somerset-kentucky.com",
  "title": "Camp hosted by Insight Brazilian Jiu Jitsu offered fun training style",
  "snippet": "",
  "published": "2026-10-13T17:00:00+00:00"
 },
 {
  "id": "74e34582d0f5",
  "region": "intl",
  "source": "MyMMANews",
  "title": "UFC BJJ 12 and the Rise of Submission-Only Betting Markets",
  "snippet": "",
  "published": "2026-10-13T11:11:26+00:00"
 },
 {
  "id": "635f839bf562",
  "region": "intl",
  "source": "AKIpress News Agency",
  "title": "Kyrgyz athlete wins three championship belts at World Grappling and BJJ Championship in U.S.",
  "snippet": "",
  "published": "2026-10-13T08:52:00+00:00"
 },
 {
  "id": "25e563ae6fff",
  "region": "intl",
  "source": "Telegraph and Argus",
  "title": "Bradford boys bring back European gold medals after wonderful weekend in Lisbon",
  "snippet": "",
  "published": "2026-10-13T23:21:00+00:00"
 },
 {
  "id": "b2ab09f7a574",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Michael Martinez",
  "snippet": "",
  "published": "2026-10-13T05:33:18+00:00"
 },
 {
  "id": "9402e3df09ed",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Mark Zuckerberg Once Wrote Fencing Sequences in Chemistry Class, Now He’s Into Jiu-Jitsu — Meta Flagged the Danger, His Answer: ‘High Risk = High Reward’",
  "snippet": "",
  "published": "2026-10-13T18:00:09+00:00"
 },
 {
  "id": "ff2c22fcf8ae",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Drafting The Top 10 Submissions Of 2026 (So Far) | The FloGrappling Show (Ep 108)",
  "snippet": "",
  "published": "2026-10-13T17:04:02+00:00"
 },
 {
  "id": "74c637f283a7",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Tony Way",
  "snippet": "",
  "published": "2026-10-12T17:57:41+00:00"
 },
 {
  "id": "14a56e13bc62",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Ross Nicholls",
  "snippet": "",
  "published": "2026-10-13T11:37:32+00:00"
 },
 {
  "id": "cbf55da7c667",
  "region": "intl",
  "source": "Yukon News",
  "title": "Black belt lineage brings martial arts history to Whitehorse mats",
  "snippet": "",
  "published": "2026-10-13T22:34:38+00:00"
 },
 {
  "id": "540faee7877e",
  "region": "intl",
  "source": "Legacy | Obituary",
  "title": "Benjamin Ben \"Ben\" Brotherton Obituary (2026) - Red House, WV - Gatens-Harding Funeral Home",
  "snippet": "",
  "published": "2026-10-13T00:26:46+00:00"
 },
 {
  "id": "9c07af8a718c",
  "region": "intl",
  "source": "Nanyang Technological University - NTU Singapore",
  "title": "A Winning Gesture: Noah Lim Shows Sportsmanship at Asian Games",
  "snippet": "",
  "published": "2026-10-13T13:26:18+00:00"
 },
 {
  "id": "9af25a8385c6",
  "region": "intl",
  "source": "Thames Valley Police",
  "title": "Martial arts club owner jailed for rape in Reading",
  "snippet": "",
  "published": "2026-10-13T13:39:00+00:00"
 },
 {
  "id": "cc1ddbc4bdd5",
  "region": "intl",
  "source": "vijesti.me",
  "title": "UP: Montenegrin police officers win nine medals at the European Police and Fire Games",
  "snippet": "",
  "published": "2026-10-13T15:38:26+00:00"
 },
 {
  "id": "b112136ca2ba",
  "region": "intl",
  "source": "Rediff",
  "title": "India Shines With Yogasana And Mallakhamb At BRICS Traditional Games",
  "snippet": "",
  "published": "2026-10-13T06:22:37+00:00"
 },
 {
  "id": "9eeda931150b",
  "region": "intl",
  "source": "Reading Chronicle",
  "title": "Man, 44, who raped woman will conducting Jiu-Jitsu class is jailed",
  "snippet": "",
  "published": "2026-10-13T14:07:04+00:00"
 },
 {
  "id": "8d439abf2258",
  "region": "intl",
  "source": "The Assam Tribune",
  "title": "India’s yogasana draws praise from China, South Africa at BRICS Games",
  "snippet": "",
  "published": "2026-10-13T09:47:07+00:00"
 },
 {
  "id": "d603d2076aee",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Former El Paso County Deputy Turned To Jiu Jitsu And Teaches Self Defense Decades After She Was Kidnapped",
  "snippet": "",
  "published": "2026-10-13T17:44:56+00:00"
 },
 {
  "id": "da0445254981",
  "region": "intl",
  "source": "BJJDOC",
  "title": "WATCH: Guy Uses BJJ To Disarm Thief",
  "snippet": "",
  "published": "2026-10-13T12:13:01+00:00"
 },
 {
  "id": "3d3921f02bf7",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Josh Barnett Breaks Down Why Mighty Mouse Is Wrong To Want Heel Hooks Banned From MMA",
  "snippet": "",
  "published": "2026-10-13T19:50:07+00:00"
 },
 {
  "id": "c3b622cfc74a",
  "region": "intl",
  "source": "BJJEE",
  "title": "Brian Glick Explains How He Trains Every Day In His 50s Despite Injuries",
  "snippet": "Longtime John Danaher student Brian Glick trains every day in his 50s, on a body carrying nearly 25 years of wear. In a recent interview he described a mix of lingering injuries and age-related arthritis, including a meniscus he tore on the day he received his purple belt about 18 years ago: It healed, it’s pretty good, but it’s still there. I have some arthritis… I’ve got pretty bad shoulders now. They’re not terrible, but if I get into particular positions it’s done. Like, it’s over. Like I can’t even be at that range of motion anymore. So you have these limitations and you just work around…",
  "published": "2026-10-13T14:39:48+00:00"
 },
 {
  "id": "a1ca4460d5be",
  "region": "intl",
  "source": "BJJEE",
  "title": "Teddy Riner Explains Why He Turned Down UFC: “It’s Not In My DNA”",
  "snippet": "Judo heavyweight Teddy Riner has spoken about a rumored multi-million dollar UFC offer to compete in the cage. Riner, whose career is so dominant that he is regularly mentioned among France’s greatest athletes, addressed it in an Original Version interview tied to his signing with PSG Judo at Parc des Princes. Asked why he said no, he left little room for doubt: It’s not actually that I refused – because it’s not in my DNA. I am in a sport that suits me. I am happy practicing this sport. Tomorrow, the minute I go and change hats and go into MMA, it’s a whole family that turns its back on me. I…",
  "published": "2026-10-13T04:58:35+00:00"
 }
]
