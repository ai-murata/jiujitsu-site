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
  "id": "2baa2d223c8e",
  "region": "jp",
  "source": "Infoseek",
  "title": "ガリットチュウ福島、「ＯＮＥ ＳＡＭＵＲＡＩ ４」公開計量にオレンジ「ビキニ」で登場…竹浦正起とオープニングマッチで対戦…１０・１７有明アリーナ",
  "snippet": "",
  "published": "2026-10-16T22:45:00+00:00"
 },
 {
  "id": "8e9b185a43dd",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "トラン・ティ・カム・トゥは手に汗握る接戦を制し、世界空手選手権の決勝に進出した。",
  "snippet": "",
  "published": "2026-10-16T12:57:54+00:00"
 },
 {
  "id": "5e7164a94e7e",
  "region": "jp",
  "source": "スポニチ Sponichi Annex",
  "title": "【ONE】ガリットチュウ福島 計量・ハイドレーションテスト一発クリア！朝倉未来らの柔術コーチと対戦",
  "snippet": "",
  "published": "2026-10-16T01:27:00+00:00"
 },
 {
  "id": "bb6220cd7fe6",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "【開催レポート】クレベル・コイケ選手による特別柔術クラスを開催！渋谷アカデミーにて。ボンサイファミリーの絆を深める一日",
  "snippet": "",
  "published": "2026-10-15T17:30:33+00:00"
 },
 {
  "id": "1bbe6ddd2aa2",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE】ガリットチュウ福島 計量・ハイドレーションテスト一発クリア！朝倉未来らの柔術コーチと対戦 (スポニチアネックス)",
  "snippet": "",
  "published": "2026-10-16T01:28:19+00:00"
 },
 {
  "id": "23ea9628f715",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "アジアパラ大会はパラアーチェリー 篠原彩選手で熱狂しよう！",
  "snippet": "",
  "published": "2026-10-16T04:05:22+00:00"
 },
 {
  "id": "4bd517803066",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "アジアパラ大会はパラ水泳 アーニー・ガウィラン選手で熱狂しよう！",
  "snippet": "",
  "published": "2026-10-16T04:05:20+00:00"
 },
 {
  "id": "f47da47a82c1",
  "region": "jp",
  "source": "スポニチ Sponichi Annex",
  "title": "【ONE】ガリットチュウ福島 メガネ＆カツラ＆ビキニで登場！チャトリCEOも笑いこらえきれず!?",
  "snippet": "",
  "published": "2026-10-16T08:04:00+00:00"
 },
 {
  "id": "e940b7758792",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "アジアパラ大会はパラバドミントン 藤原大輔選手で熱狂しよう！",
  "snippet": "",
  "published": "2026-10-16T04:10:20+00:00"
 },
 {
  "id": "af2ea89ea73d",
  "region": "jp",
  "source": "efight.jp",
  "title": "【ONE】平田樹、鍛えた筋肉美で計量パス！対するラズワンも盛り上がる太もも",
  "snippet": "",
  "published": "2026-10-16T08:36:05+00:00"
 },
 {
  "id": "19023369616a",
  "region": "jp",
  "source": "スポニチ Sponichi Annex",
  "title": "【記事全文】【ONE】ガリットチュウ福島 メガネ＆カツラ＆ビキニで登場！チャトリCEOも笑い耐えられず！？",
  "snippet": "",
  "published": "2026-10-16T08:04:00+00:00"
 },
 {
  "id": "5ac4789b7d60",
  "region": "jp",
  "source": "Infoseek",
  "title": "【ONE】ガリットチュウ福島はハゲづら＆オレンジビキニで登場も竹浦正起にビキニ引っ張られ…",
  "snippet": "",
  "published": "2026-10-16T10:15:52+00:00"
 },
 {
  "id": "89173d44e9f5",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "アジアパラ大会はパラ陸上競技 石山大輝選手で熱狂しよう！",
  "snippet": "",
  "published": "2026-10-16T06:10:47+00:00"
 },
 {
  "id": "bf314b10ee04",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【ONE】『ONE SAMURAI 4』本計量速報＝安保瑠輝也がハイドレーションをパス出来ず再計量。野杁正明、吉成名高、秋元皓貴らは順調にパス",
  "snippet": "",
  "published": "2026-10-16T01:10:00+00:00"
 },
 {
  "id": "8e037629cfd2",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "【ONE】ガリットチュウ福島 計量・ハイドレーションテスト一発クリア！朝倉未来らの柔術コーチと対戦 (2026年10月16日掲載)",
  "snippet": "",
  "published": "2026-10-16T01:28:19+00:00"
 },
 {
  "id": "ae2caf009372",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "【画像】【ONE】ガリットチュウ福島 計量・ハイドレーションテスト一発クリア！朝倉未来らの柔術コーチと対戦",
  "snippet": "",
  "published": "2026-10-16T01:28:19+00:00"
 },
 {
  "id": "1b9a8c86c59a",
  "region": "jp",
  "source": "サンスポ",
  "title": "【ONE動画】ガリットチュウ福島善成、ビキニ姿で登場 JTTコーチ竹浦正起から〝洗礼〟浴びる 「ONE SAMURAI 4」公開計量＆フェイスオフ",
  "snippet": "",
  "published": "2026-10-16T13:22:15+00:00"
 },
 {
  "id": "ca3672a7f410",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "ガリットチュウ福島善成が前日計量クリア フェースオフでは芸人魂見せるも肉体に本気度",
  "snippet": "",
  "published": "2026-10-16T20:00:00+00:00"
 },
 {
  "id": "5b3bba6423b5",
  "region": "jp",
  "source": "Infoseek",
  "title": "【ONE】ガリットチュウ福島 メガネ＆カツラ＆オレンジビキニで登場！チャトリCEOも笑い耐えられず",
  "snippet": "",
  "published": "2026-10-16T08:09:44+00:00"
 },
 {
  "id": "fcbf05c3b412",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "オフロード車で雪に覆われた“文明崩壊後の世界”を生き抜くゲーム『AFTERZERO：ラストラン』が発表。ほかの生存者を",
  "snippet": "",
  "published": "2026-10-16T03:42:16+00:00"
 },
 {
  "id": "9165e1ae2ce8",
  "region": "jp",
  "source": "게임메카",
  "title": "終わりなき冬、生存ドライビング探索ゲーム『アフターゼロ』公開",
  "snippet": "",
  "published": "2026-10-16T02:55:12+00:00"
 },
 {
  "id": "155c1682dee2",
  "region": "jp",
  "source": "サンスポ",
  "title": "「ONE SAMURAI 4（ワン・サムライ）」 秋元皓貴が王座奪還へ挑む 野杁正明はフェザー級トーナメント準決勝",
  "snippet": "",
  "published": "2026-10-16T12:28:56+00:00"
 },
 {
  "id": "5a5a623b5c97",
  "region": "jp",
  "source": "Infoseek",
  "title": "安保瑠輝也ら３選手、「ハイドレーションテスト」失敗…再テストでキャッチウェートで対戦へ…「ＯＮＥ ＳＡＭＵＲＡＩ４」１０・１７有明アリーナ",
  "snippet": "",
  "published": "2026-10-16T06:30:00+00:00"
 },
 {
  "id": "1bbf9cf42d70",
  "region": "jp",
  "source": "Infoseek",
  "title": "【ONE SAMURAI 4】ガリットチュウ福島善成、白ブリーフ姿で計量に登場。芸人魂で一発クリア｜Infoseekニュース",
  "snippet": "",
  "published": "2026-10-16T03:22:35+00:00"
 },
 {
  "id": "cfc14dac1773",
  "region": "intl",
  "source": "The New York Times",
  "title": "These Older Brazilian Jiu-Jitsu Students Are Fighting the Clock",
  "snippet": "",
  "published": "2026-10-16T09:01:30+00:00"
 },
 {
  "id": "051c26826013",
  "region": "intl",
  "source": "MMA Mania",
  "title": "Celtics coach Joe Mazzulla: Getting BJJ blue belt felt the same as winning NBA title",
  "snippet": "",
  "published": "2026-10-16T16:30:00+00:00"
 },
 {
  "id": "03703410a988",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC Hosts Community Activations Across Los Angeles During UFC 331 Fight Week",
  "snippet": "",
  "published": "2026-10-16T17:19:04+00:00"
 },
 {
  "id": "5ee813b5ce17",
  "region": "intl",
  "source": "Cochrane Eagle",
  "title": "Legendary jiu-jitsu fighter visits with Cochrane school",
  "snippet": "",
  "published": "2026-10-16T19:30:00+00:00"
 },
 {
  "id": "36236950e31b",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu - W/M",
  "snippet": "",
  "published": "2026-10-16T20:26:00+00:00"
 },
 {
  "id": "7e9d9a5456da",
  "region": "intl",
  "source": "FloGrappling",
  "title": "PBJJF World Jiu-Jitsu Championships",
  "snippet": "",
  "published": "2026-10-16T15:43:21+00:00"
 },
 {
  "id": "0658a02f0735",
  "region": "intl",
  "source": "AKIpress News Agency",
  "title": "Kyrgyzstan's Ramis Abdyrashitov wins gold at Central Asian Jiu-Jitsu Championship",
  "snippet": "",
  "published": "2026-10-16T09:47:00+00:00"
 },
 {
  "id": "e6b0be23c264",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC Hosts Several Activations Across Philadelphia as part of UFC 330 Fight Week",
  "snippet": "",
  "published": "2026-10-16T16:53:09+00:00"
 },
 {
  "id": "dea7a791e19b",
  "region": "intl",
  "source": "colerainechronicle.co.uk",
  "title": "Mayor welcomes young wrestling and Brazilian Jiu-Jitsu champion",
  "snippet": "",
  "published": "2026-10-16T08:51:00+00:00"
 },
 {
  "id": "4d90f52d39d7",
  "region": "intl",
  "source": "NorthernIrelandWorld",
  "title": "Causeway Coast and Glens Mayor congratulates nine-year-old Brazilian Jiu-Jitsu world champion Leon",
  "snippet": "",
  "published": "2026-10-16T08:36:00+00:00"
 },
 {
  "id": "a35e9b287895",
  "region": "intl",
  "source": "BurgasMedia",
  "title": "Burgas student wins gold at jiu-jitsu tournament in Bosnia and Herzegovina",
  "snippet": "",
  "published": "2026-10-15T14:17:36+00:00"
 },
 {
  "id": "a2128fba9a26",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan Kids Jiu-Jitsu IBJJF Championship",
  "snippet": "",
  "published": "2026-10-15T17:00:00+00:00"
 },
 {
  "id": "fe82c6cc1fd5",
  "region": "intl",
  "source": "TOD",
  "title": "Jiu Jitsu Semi Finals - M/W",
  "snippet": "",
  "published": "2026-10-15T22:55:19+00:00"
 },
 {
  "id": "da43f3925057",
  "region": "intl",
  "source": "FloGrappling",
  "title": "GF Team",
  "snippet": "",
  "published": "2026-10-15T17:00:00+00:00"
 },
 {
  "id": "0c830dd8707f",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "James Paul Cima vs Tyler Cody Yazell 2026 Pan Jiu Jitsu IBJJF Championship",
  "snippet": "",
  "published": "2026-10-15T15:14:32+00:00"
 },
 {
  "id": "c0f91209e21f",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Levi Kurtovich",
  "snippet": "",
  "published": "2026-10-16T19:31:59+00:00"
 },
 {
  "id": "1facc63ffd85",
  "region": "intl",
  "source": "WIFR",
  "title": "Winnebago County Sheriff’s Office debuts upgraded training center",
  "snippet": "",
  "published": "2026-10-15T22:47:00+00:00"
 },
 {
  "id": "a12b859eefe2",
  "region": "intl",
  "source": "Combat Press",
  "title": "UFC Edmonton: Buckley vs. Malott Preview and Predictions",
  "snippet": "",
  "published": "2026-10-15T22:49:32+00:00"
 },
 {
  "id": "af87d1c27756",
  "region": "intl",
  "source": "Castanet",
  "title": "Vernon expert offering self-defence course for women",
  "snippet": "",
  "published": "2026-10-15T19:00:00+00:00"
 },
 {
  "id": "9d54edb5cade",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Kit Dale Premieres White Belt Comedy",
  "snippet": "",
  "published": "2026-10-16T10:10:42+00:00"
 },
 {
  "id": "cb66d9258c6e",
  "region": "intl",
  "source": "BJJDOC",
  "title": "UFC Veteran Kenny Florian Bans Shirtless Students Walking Around At His BJJ Dojo",
  "snippet": "",
  "published": "2026-10-16T13:40:41+00:00"
 },
 {
  "id": "ac5df7303863",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Bernardo Faria: Champions Can Be Bad Teachers Sometimes, Unable To Communicate Concepts",
  "snippet": "",
  "published": "2026-10-16T08:24:43+00:00"
 },
 {
  "id": "1170136ef082",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Gordon Ryan Claimed AI Finally Taught Him How To Cure His Staph Infection Problem Without Using Oral Antibiotics",
  "snippet": "",
  "published": "2026-10-16T13:06:40+00:00"
 },
 {
  "id": "7a76cb21c62b",
  "region": "intl",
  "source": "BJJEE",
  "title": "Judo Historian Says Gordon Ryan’s Behavior Would Not Be Tolerated In Judo",
  "snippet": "Judo historian Chadi argues that Gordon Ryan’s public conduct would not survive inside judo’s institutional culture. Speaking on a podcast, he said the sport weighs an athlete’s behavior outside competition heavily, so technical ability alone does not guarantee advancement through the ranks. He noted that modern judo federations watch athletes on and off the mat, social media included: If you’re picking brawls in competition when you go out and compete or on social media or your behavior or whatever it may be, that stuff of course affects a lot. Even now, the athletes that go on the world tour…",
  "published": "2026-10-16T09:04:28+00:00"
 },
 {
  "id": "25b471c11514",
  "region": "intl",
  "source": "BJJEE",
  "title": "John Hearn, The World’s Oldest Judo Teacher, Passes Away At 103",
  "snippet": "John “Jack” Hearn, known to generations of students in Cramlington simply as Mr. Hearn and nicknamed Judo Jack, has died at 103. His judo began by accident. Appendix surgery ended his cycling, and in 1951 he found judo, taking to it “like a duck to water”. In 1954 he and his brother Bob opened their own club, the start of a teaching career that ran more than seventy years. He coached generations of Northumberland families and liked to joke that former six-year-old students were now bringing their grandchildren. Sources state that Guinness World Records named him the world’s oldest judo instruc…",
  "published": "2026-10-16T08:56:15+00:00"
 }
]
