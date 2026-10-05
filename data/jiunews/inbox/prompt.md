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
  "id": "1c3b16362d42",
  "region": "jp",
  "source": "アラブニュース",
  "title": "UAE、アジア競技大会の柔術で過去最高の5つの金メダルを獲得",
  "snippet": "",
  "published": "2026-10-04T18:49:55+00:00"
 },
 {
  "id": "b06e2ce29080",
  "region": "jp",
  "source": "スポニチ Sponichi Annex",
  "title": "玉木宏 意外な食生活語る 柔術参戦も「普段は全く節制はしていなくて」 1日の驚がく食事回数",
  "snippet": "",
  "published": "2026-10-04T09:48:00+00:00"
 },
 {
  "id": "57d57361a6da",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "玉木宏 意外な食生活語る 柔術参戦も「普段は全く節制はしていなくて」 1日の驚がく食事回数 (スポニチアネックス)",
  "snippet": "",
  "published": "2026-10-04T09:50:33+00:00"
 },
 {
  "id": "a55238eec994",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "函南町から格闘王兄弟に！ 小川龍乃丞・樟乃丞さんが柔術世界大会で優秀成績「将来は王者に」（静岡新聞DIGITAL）",
  "snippet": "",
  "published": "2026-10-04T00:00:00+00:00"
 },
 {
  "id": "72e709f2456d",
  "region": "jp",
  "source": "岐阜新聞デジタル",
  "title": "愛知・名古屋アジア大会 第１５日 柔術 吉永（パラエストラ岐阜）６３キロ級でベスト１６",
  "snippet": "",
  "published": "2026-10-03T20:00:00+00:00"
 },
 {
  "id": "77fb406d13aa",
  "region": "jp",
  "source": "47NEWS",
  "title": "函南町から格闘王兄弟に！ 小川龍乃丞・樟乃丞さんが柔術世界大会で優秀成績「将来は王者に」",
  "snippet": "",
  "published": "2026-10-04T00:00:00+00:00"
 },
 {
  "id": "e6ab1cfd4cf3",
  "region": "jp",
  "source": "アラブニュース",
  "title": "アル＝ダハミ、障害飛越で金メダルを獲得し、サウジアラビアがアジア大会を17個のメダルで締めくくる",
  "snippet": "",
  "published": "2026-10-04T18:51:45+00:00"
 },
 {
  "id": "7147d6c20caa",
  "region": "jp",
  "source": "スポニチ Sponichi Annex",
  "title": "玉木宏",
  "snippet": "",
  "published": "2026-10-04T10:03:26+00:00"
 },
 {
  "id": "45c3b06dfff7",
  "region": "jp",
  "source": "Infoseek",
  "title": "玉木宏 「毎日のように顔を合わせる」大人気俳優明かす 「ほぼ道場仲間という意識です」",
  "snippet": "",
  "published": "2026-10-04T10:21:36+00:00"
 },
 {
  "id": "ffc27530c6a7",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "玉木宏 意外な食生活語る 柔術参戦も「普段は全く節制はしていなくて」 1日の驚がく食事回数 (2026年10月4日掲載)",
  "snippet": "",
  "published": "2026-10-04T09:50:33+00:00"
 },
 {
  "id": "ef13be9171d0",
  "region": "jp",
  "source": "t.co",
  "title": "森本17号 (@morimoto_17) on X",
  "snippet": "",
  "published": "2026-10-03T12:08:06+00:00"
 },
 {
  "id": "9183512ebade",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Pierre-Olivier Leclerc vs Guilherme Rodrigues Fernandes 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T21:14:14+00:00"
 },
 {
  "id": "4a69d6175b2e",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Christian De La Fuente vs Ignacio Masis Barrientos 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:53:28+00:00"
 },
 {
  "id": "f6e61e857e5b",
  "region": "intl",
  "source": "flograppling.com",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T21:14:15+00:00"
 },
 {
  "id": "963988500368",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Madison Caorsi vs Jaden Nicholas Bunton 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:51:36+00:00"
 },
 {
  "id": "11c0fa0151e8",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Omar Sabha vs Brett W Oteri 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:49:35+00:00"
 },
 {
  "id": "0f263041e3cc",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Daniel J. Phoenix vs Jose Alfonso Hermoza 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:55:02+00:00"
 },
 {
  "id": "924b5ad846bd",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Robert DIon Forrest vs Phillip Todd Farley 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T18:07:19+00:00"
 },
 {
  "id": "38982b31334b",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Salvatore Burriesci vs Anthony Jay Siscoe 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T18:13:23+00:00"
 },
 {
  "id": "0457094953e1",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Madison Marie Taggart vs Jonesy Keen Jones 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:50:16+00:00"
 },
 {
  "id": "d1b9eed38a77",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Natan Chueng Freitas vs Pawel Kacper Jaworski 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:56:13+00:00"
 },
 {
  "id": "cd82ebbe130b",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T22:21:10+00:00"
 },
 {
  "id": "f10a52e9383e",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Replay: Mat 11 - 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship | Oct 3 @ 9 AM",
  "snippet": "",
  "published": "2026-10-04T02:03:28+00:00"
 },
 {
  "id": "7cf6a59ae4ec",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Daniel Fundora vs Victor Conde Dourado Guerra 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T17:59:34+00:00"
 },
 {
  "id": "8e7cbeea5942",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Charlotte L Wardrop vs Inga Boruch 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T17:59:37+00:00"
 },
 {
  "id": "76b1b9a0bdee",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Titus Krixus Ortiz vs Mikaael Ilias Wise 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T17:59:30+00:00"
 },
 {
  "id": "ce6d1bd33ec6",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Richard Anthony Foster vs Neil A. Franciotti 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T02:03:19+00:00"
 },
 {
  "id": "9fce702b3754",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Joseph Samuel Smith vs Samuel J Buhrman 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T02:03:30+00:00"
 },
 {
  "id": "c292b4d4223b",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Alexa Amber Rivera vs Chika Adaora Efobi 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T17:59:32+00:00"
 },
 {
  "id": "982bba3e9973",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Elmer Abraham Florian vs Gabriel Riccioppo Asenjo 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T17:59:28+00:00"
 },
 {
  "id": "6b879b3bff33",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Joshua Cole Spivey vs Neil A. Franciotti 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T02:03:12+00:00"
 },
 {
  "id": "a7f0c2ac0f5c",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Diego De Araujo Saraiva vs Suldbayar Damdin 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T19:58:47+00:00"
 },
 {
  "id": "c2e353d44bae",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Alex Micheal Kerwan vs Nathaniel Alexander Martinez 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T19:58:31+00:00"
 },
 {
  "id": "cf697413d8f6",
  "region": "intl",
  "source": "flograppling.com",
  "title": "Continue Watching",
  "snippet": "",
  "published": "2026-10-03T20:52:10+00:00"
 },
 {
  "id": "63ea6b25f88f",
  "region": "intl",
  "source": "Arab News",
  "title": "UAE tops Asian Games jiu-jitsu standings with record 5 golds",
  "snippet": "",
  "published": "2026-10-04T08:18:25+00:00"
 },
 {
  "id": "f2757621d820",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Aliya V. Appassova vs Valentina Javiera Larrondo Peña 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T13:33:06+00:00"
 },
 {
  "id": "7ba18dca77aa",
  "region": "intl",
  "source": "BJJEE",
  "title": "“We Detest You”- Ukrainian BJJ Black Belt Reveals the Real Reason Gordon Ryan’s Ukraine Seminar Was Shut Down",
  "snippet": "Was Gordon Ryan really kicked out of Ukraine? Ukrainian BJJ black belt Vlad Polyanskiy has revealed how the grappling superstar’s secret seminar sparked a backlash involving Ukrainian coaches, war veterans and Craig Jones. Speaking on the Grapplezilla Podcast , Vlad shared his account of the controversy surrounding Ryan’s visit to Ukraine shortly after ADCC, explaining why the American grappler’s previous statements about Ukraine and the Azov Brigade made his appearance so controversial. He also addressed the biggest question surrounding the incident: Was Ryan actually deported, or did he leav…",
  "published": "2026-10-04T13:14:39+00:00"
 },
 {
  "id": "3f0f0ab565f7",
  "region": "intl",
  "source": "BJJEE",
  "title": "Rickson Gracie Opens Up On Parkinson’s: “My Physicalities Are Fading Away”",
  "snippet": "Rickson Gracie discussed his ongoing battle with Parkinson’s disease in a recent appearance on The ROL Radio Podcast… Acknowledging that his physical condition continues to decline. Reflecting on a recent training session with his brother Royler, Gracie was honest about where he stands physically: Physically I feel like I’m fading away a little bit. So, I cannot keep up with him right now. He’s a monster. The 66-year-old, widely regarded as one of the greatest practitioners in Jiu-Jitsu history, explained how his diagnosis has reshaped his sense of purpose within the sport: With my physicaliti…",
  "published": "2026-10-04T07:24:37+00:00"
 },
 {
  "id": "c6fbe5dd3956",
  "region": "intl",
  "source": "BJJEE",
  "title": "Joe Rogan Says BJJ Coaches Don’t Need To Compete To Be Successful: “John Danaher Didn’t Do It”",
  "snippet": "A recent episode of the Joe Rogan Experience MMA Show focused on whether elite coaching requires elite competitive experience And the conversation centered on John Danaher, widely considered one of the greatest Jiu-Jitsu coaches ever despite never competing at a high level himself. Sean Sharaf, coming off his upset win over Gable Stevenson, opened up about the difficulty he had finding quality coaching throughout his career – describing years of bouncing between gyms and paying out of pocket for every private session, never receiving free coaching despite showing real potential. When the discu…",
  "published": "2026-10-04T07:12:50+00:00"
 },
 {
  "id": "475edbb179a9",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "BJJ Rankings Update – October 2026",
  "snippet": "The October 2026 update has been applied to the Jits Magazine BJJ Rankings and the full standings can be found here . It goes without saying that the no gi divisions have experienced a major shakeup, as September contained the most prestigious no gi grappling tournament in the sport. With ADCC 2026 coming to an end, there were 9 new champions crowned and each and every one of them had to beat multiple elite competitors in order to get there. That wasn’t all though, UFC BJJ 11 took place shortly after and that event also featured some of the best in the world that didn’t step on the mats at ADC…",
  "published": "2026-10-04T17:40:45+00:00"
 }
]
