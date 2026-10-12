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
  "id": "a257d3b8f778",
  "region": "jp",
  "source": "山陽新聞",
  "title": "ガリットチュウ福島『ONE』緊急参戦 “朝倉未来の柔術コーチ”竹浦正起とグラップリングマッチ",
  "snippet": "",
  "published": "2026-10-12T00:02:48+00:00"
 },
 {
  "id": "803b91c41241",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "ブラジリアン柔術 世界大会で銀 桜台のジムの堀井さん〈伊勢原市〉",
  "snippet": "",
  "published": "2026-10-11T04:00:00+00:00"
 },
 {
  "id": "d53e42d0539a",
  "region": "jp",
  "source": "山陽新聞",
  "title": "【ひとフォーカス】ブラジリアン柔術で国際大会優勝の玉井大和さん 「世界に名を広めたい」",
  "snippet": "",
  "published": "2026-10-11T07:35:51+00:00"
 },
 {
  "id": "e6cd253ec3af",
  "region": "jp",
  "source": "Infoseek",
  "title": "【SSPW】10・21後楽園大会で船木＆高橋＆小河組が村上＆関根＆野村組と6人タッグで激突",
  "snippet": "",
  "published": "2026-10-11T11:11:38+00:00"
 },
 {
  "id": "d0a24cca48af",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "石橋陽彩、初号試写後の“ダブルレインボー”の奇跡を告白 玉木宏＆土屋神葉らの素顔が垣間見えるトークも＜どこよりも遠い場所にいる君へ＞（WEBザテレビジョン）",
  "snippet": "",
  "published": "2026-10-11T03:30:00+00:00"
 },
 {
  "id": "1c32ad3bec68",
  "region": "jp",
  "source": "Howl.link",
  "title": "前田まさき丨柔術白帯36歳 (@mmmsumo_bjj) on X",
  "snippet": "",
  "published": "2026-10-11T02:44:00+00:00"
 },
 {
  "id": "dda13ec9b523",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "ル・ヴァン・トゥアンはLC36でウズベキスタン人ファイターに敗れた。",
  "snippet": "",
  "published": "2026-10-11T06:28:58+00:00"
 },
 {
  "id": "b5f48b4f1ba3",
  "region": "jp",
  "source": "games.gg",
  "title": "ARC Raiders 2.0、グラップリングフック追加でSteam同接が急増",
  "snippet": "",
  "published": "2026-10-11T15:51:59+00:00"
 },
 {
  "id": "e9ea6c6e37a6",
  "region": "intl",
  "source": "Bloody Elbow",
  "title": "Popular BJJ black belt retires after losing sixth straight fight at UFC Vegas 122",
  "snippet": "",
  "published": "2026-10-11T02:00:00+00:00"
 },
 {
  "id": "92d3ca80ed88",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - M/W",
  "snippet": "",
  "published": "2026-10-11T08:57:11+00:00"
 },
 {
  "id": "925b05d75888",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Replay: Mat 5 - 2026 UIJJ ADRIATICO BJJ CUP | Oct 10 @ 7 PM",
  "snippet": "",
  "published": "2026-10-11T07:19:30+00:00"
 },
 {
  "id": "efebdc41d4ed",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 12 Results",
  "snippet": "",
  "published": "2026-10-11T01:11:48+00:00"
 },
 {
  "id": "467a838897ca",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - Finals - M/W",
  "snippet": "",
  "published": "2026-10-11T11:48:22+00:00"
 },
 {
  "id": "2fd66d39f220",
  "region": "intl",
  "source": "The New Indian Express",
  "title": "India, UAE troops sharpen mountain-warfare skills in Uttarakhand",
  "snippet": "",
  "published": "2026-10-11T15:29:01+00:00"
 },
 {
  "id": "bdffd5d1d7aa",
  "region": "intl",
  "source": "FloGrappling",
  "title": "BJJ",
  "snippet": "",
  "published": "2026-10-10T22:57:01+00:00"
 },
 {
  "id": "b5788aafbe96",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-10T18:38:26+00:00"
 },
 {
  "id": "2ad625f67874",
  "region": "intl",
  "source": "Belfast Live",
  "title": "How Co Antrim man turned heart attack recovery into judo black belt aged 57",
  "snippet": "",
  "published": "2026-10-11T16:32:00+00:00"
 },
 {
  "id": "32c069bc99aa",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Judo Gold Medalist Owen Livesay: Every Single Serious Judoka and Jiu Jitsu Guy Does Static Drills Daily",
  "snippet": "",
  "published": "2026-10-11T13:36:36+00:00"
 },
 {
  "id": "373665e38ab3",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Microsoft Announces Sponsorship Deal With Kade and Tye Ruotolo",
  "snippet": "",
  "published": "2026-10-11T09:10:28+00:00"
 },
 {
  "id": "1986323e4f00",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Teddy Riner Opens Up About His Refusal to Transition to MMA: ‘It’s Not in My DNA’",
  "snippet": "",
  "published": "2026-10-11T08:28:23+00:00"
 },
 {
  "id": "4e410b3ac84a",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Arman Tsarukyan Set to Wrestle Gracie Family Welterweight Champion",
  "snippet": "",
  "published": "2026-10-11T13:13:59+00:00"
 },
 {
  "id": "6cf5fd043b5e",
  "region": "intl",
  "source": "BJJDOC",
  "title": "John Danaher Has a Reputation for Having a Temper, Allegedly Slapping and Swearing at His Uke, According to a Visitor",
  "snippet": "",
  "published": "2026-10-11T08:42:57+00:00"
 },
 {
  "id": "7d39b8773a53",
  "region": "intl",
  "source": "Breitbart",
  "title": "HERO REMEMBERED: Texas Mourns Death of Texas Ranger Special Ops Sgt. Shelton After Valiant Cancer Battle",
  "snippet": "",
  "published": "2026-10-10T19:16:19+00:00"
 },
 {
  "id": "4ba7606905e2",
  "region": "intl",
  "source": "BJJEE",
  "title": "Judo Gold Medalist Owen Livesey Rejects The ‘Don’t Drill’ Movement: “I Don’t Agree With It”",
  "snippet": "Commonwealth Games judo gold medalist Owen Livesey has no patience for the idea that grapplers should stop drilling. Livesey trained judo full-time for eight years before moving into Jiu-Jitsu and grappling – and back in the day, he spent two weeks at John Danaher’s Renzo Gracie Academy alongside Gordon Ryan, Giancarlo Bodoni and other top competitors. Asked about training in a room of elite athletes, he raised the subject: You know, there’s this massive talk at the minute about you “shouldn’t drill”. I don’t agree with that at all. I think that’s just, like, people trying to put their own spi…",
  "published": "2026-10-11T14:53:07+00:00"
 },
 {
  "id": "320070a58899",
  "region": "intl",
  "source": "BJJEE",
  "title": "Arman Tsarukyan Set To Face Neiman Gracie At RAF Abu Dhabi",
  "snippet": "Real American Freestyle (RAF) announced that UFC lightweight contender Arman Tsarukyan will meet Neiman Gracie Stambowsky on November 14 at Etihad Arena on Yas Island, Abu Dhabi! Tsarukyan arrives with momentum in both worlds. In September at UFC 331 in Los Angeles, he stopped Mauricio Ruffy with first-round elbows, just short of the five-minute mark, strengthening his lightweight title case. In RAF he stands at 7-1, with his lone loss to Colby Covington at RAF 11. Tony Ferguson, Urijah Faber and Georgio Poullas are among the names he has faced there. Gracie brings family pedigree to the mix.…",
  "published": "2026-10-11T14:36:10+00:00"
 }
]
