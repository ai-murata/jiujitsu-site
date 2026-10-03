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
  "id": "5729f535c17c",
  "region": "jp",
  "source": "スポーツナビ",
  "title": "柔術男子77kg級の森戸新士が初戦で一本勝ちも無念の負傷棄権 自国開催の大舞台で魅せた誇り",
  "snippet": "",
  "published": "2026-10-03T07:05:00+00:00"
 },
 {
  "id": "ab336b64d99c",
  "region": "jp",
  "source": "アラブニュース",
  "title": "UAE、アジア大会で柔術メダル3つを獲得",
  "snippet": "",
  "published": "2026-10-03T17:19:44+00:00"
 },
 {
  "id": "17819c1636c0",
  "region": "jp",
  "source": "伊賀タウン情報 YOU",
  "title": "柔術世界大会でV 「もっと強く」48歳の宮川さん 伊賀",
  "snippet": "",
  "published": "2026-10-03T09:56:37+00:00"
 },
 {
  "id": "b1e62ea1398a",
  "region": "jp",
  "source": "中日新聞Web",
  "title": "柔術女子63キロ級2回戦、犬山市出身・吉永愛選手敗れる アジア大会",
  "snippet": "",
  "published": "2026-10-03T03:13:35+00:00"
 },
 {
  "id": "b99922b1899b",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "【柔術女子48kg級】日本柔術“初”のアジア大会 関節技に屈す【アジア大会】",
  "snippet": "",
  "published": "2026-10-03T08:27:28+00:00"
 },
 {
  "id": "9a0719f7eb9c",
  "region": "jp",
  "source": "読売新聞",
  "title": "柔術 女子52キロ級 試合結果・記録 アジア競技大会2026 愛知・名古屋",
  "snippet": "",
  "published": "2026-10-03T09:22:00+00:00"
 },
 {
  "id": "935fa1f20fcc",
  "region": "jp",
  "source": "中日新聞Web",
  "title": "10月3日 柔術",
  "snippet": "",
  "published": "2026-10-03T15:06:11+00:00"
 },
 {
  "id": "778835b53d34",
  "region": "jp",
  "source": "北海道新聞デジタル",
  "title": "書道パフォーマンスや柔術体験… お寺から 北広島盛り上げよう あすフェス 豚汁を無料提供",
  "snippet": "",
  "published": "2026-10-02T19:00:00+00:00"
 },
 {
  "id": "9b4a434c13b3",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "【セーリング女子 決勝】せらみさペア金メダル！セーリング49erFX級 史上初の快挙【アジア大会】",
  "snippet": "",
  "published": "2026-10-03T08:27:24+00:00"
 },
 {
  "id": "b98e96d6e260",
  "region": "jp",
  "source": "中日新聞Web",
  "title": "柔術女子63キロ級、犬山市出身の吉永愛選手敗れる 愛知・名古屋アジア大会",
  "snippet": "",
  "published": "2026-10-03T03:13:35+00:00"
 },
 {
  "id": "87f53b1ee69b",
  "region": "jp",
  "source": "YouTube",
  "title": "【FULL FIGHT】リリー・ホーベン vs 岡林香鈴 / SJJIF WORLD 2026 【ブラジリアン柔術】Lily Houben vs Karin Okabayashi",
  "snippet": "",
  "published": "2026-10-02T19:00:23+00:00"
 },
 {
  "id": "2b3bf5f25d49",
  "region": "jp",
  "source": "トヨタイムズスポーツ",
  "title": "【男子サッカー 準決勝】ピサノ選手も躍動！ PK戦までもつれる激闘【アジア大会】",
  "snippet": "",
  "published": "2026-10-03T07:54:25+00:00"
 },
 {
  "id": "b0d28e1e786b",
  "region": "jp",
  "source": "日刊スポーツ",
  "title": "【RIZIN】アラン“ヒロ”ヤマニハが計量超過の山本聖悟を返り討ち、大みそか大会出場熱望",
  "snippet": "",
  "published": "2026-10-03T07:13:07+00:00"
 },
 {
  "id": "236f649da389",
  "region": "jp",
  "source": "聯合ニュース",
  "title": "アジア大会14日目 韓国がアーチェリー・eスポーツ・セーリングで金メダル",
  "snippet": "",
  "published": "2026-10-03T01:20:38+00:00"
 },
 {
  "id": "06148140448a",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【RIZIN】“ボンサイ第4の男”40歳ヤマニハが圧巻一本勝ち！膝十字で山本聖悟を返り討ち、大晦日アピール（イーファイト）",
  "snippet": "",
  "published": "2026-10-03T07:19:51+00:00"
 },
 {
  "id": "992869531a3b",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "サンボのための場所を見つけよう",
  "snippet": "",
  "published": "2026-10-03T12:02:03+00:00"
 },
 {
  "id": "5df345b74164",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月3日のアジア競技大会のスケジュール：セパタクローでベトナムが3つ目の金メダルを獲得。",
  "snippet": "",
  "published": "2026-10-03T01:58:43+00:00"
 },
 {
  "id": "cfd0c4bf5aae",
  "region": "jp",
  "source": "サンスポ",
  "title": "【RIZIN】アラン“ヒロ”ヤマニハ が〝韓国ブラックコンバットの喧嘩番長〟山本聖悟を返り討ち 1回に膝十字で一本勝ち",
  "snippet": "",
  "published": "2026-10-03T06:41:41+00:00"
 },
 {
  "id": "9f35ae081a9f",
  "region": "jp",
  "source": "YouTube",
  "title": "キャッチレスリング 対 グレイシー柔術",
  "snippet": "",
  "published": "2026-10-03T08:00:09+00:00"
 },
 {
  "id": "a1e6ca8f6c9d",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "10月3日、第20回アジア競技大会におけるベトナムスポーツ代表団：セパタクローが優勝タイトルを防衛できるという期待。",
  "snippet": "",
  "published": "2026-10-03T01:29:57+00:00"
 },
 {
  "id": "1a4d9cb2cf57",
  "region": "jp",
  "source": "au Webポータル",
  "title": "アントニオ猪木の孫「猪木・アントニオ・尚登」がリングデビュー！",
  "snippet": "",
  "published": "2026-10-03T09:00:00+00:00"
 },
 {
  "id": "8caf368013c4",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "かまいたち濱家＆間宮祥太朗＆森本慎太郎、冠番組『濱太郎』開店 ゲストは玉木宏＆桐谷健太",
  "snippet": "",
  "published": "2026-10-02T21:00:19+00:00"
 },
 {
  "id": "3140772188dc",
  "region": "jp",
  "source": "Laodong.vn",
  "title": "チャン・タインは、ランニングマン・ベトナムでこれまでで最強の対戦相手と対戦したことを認めました。",
  "snippet": "",
  "published": "2026-10-03T03:02:58+00:00"
 },
 {
  "id": "9cd9d7b44369",
  "region": "jp",
  "source": "efight.jp",
  "title": "桃尻チャームポイントの宇佐美なお、HYROX挑戦に意欲！ヒップスラスト100kgの実力も",
  "snippet": "",
  "published": "2026-10-03T05:34:28+00:00"
 },
 {
  "id": "bd1e0ec7540e",
  "region": "jp",
  "source": "タイニュース・クロスボンバー",
  "title": "【名古屋アジア大会】柔術女子、タイ代表オラパー選手、大会史上初の金メダル！",
  "snippet": "",
  "published": "2026-10-03T18:57:37+00:00"
 },
 {
  "id": "4854b008edab",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE】2階級制覇クリスチャン・リー、無敗グラップリング世界王者ルオトロとV2戦！弟の敵討ちへ＝11.6（イーファイト）",
  "snippet": "",
  "published": "2026-10-03T01:09:40+00:00"
 },
 {
  "id": "4252e25f1696",
  "region": "jp",
  "source": "ONE Championship",
  "title": "【10/3 ONE Fight Night 48】エルドアンがエリオットをサブミッションで撃破、アルバレンガが石黒翔也を判定で下す",
  "snippet": "",
  "published": "2026-10-03T12:14:54+00:00"
 },
 {
  "id": "b2fa9209c174",
  "region": "jp",
  "source": "YouTube",
  "title": "【グラップリング】ジョシュ・バーネット“Bone to Bone” とは何か？ 痛みを与えるグラップリング・テクニック",
  "snippet": "",
  "published": "2026-10-02T12:42:40+00:00"
 },
 {
  "id": "d621d3e4bf28",
  "region": "jp",
  "source": "efight.jp",
  "title": "【ONE】2階級制覇クリスチャン・リー、無敗グラップリング世界王者ルオトロとV2戦！弟の敵討ちへ＝11.6",
  "snippet": "",
  "published": "2026-10-03T01:08:57+00:00"
 },
 {
  "id": "8da690a292a9",
  "region": "jp",
  "source": "efight.jp",
  "title": "【ONE】新星オスマノフ、1Rに3度ダウン奪う圧勝TKO！与座優貴とも対戦したウーリス沈め、本戦契約",
  "snippet": "",
  "published": "2026-10-03T02:02:33+00:00"
 },
 {
  "id": "442cfb37d5c0",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T22:03:49+00:00"
 },
 {
  "id": "fa358ec87ae0",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Ashley Jeslyn Soto vs Savanah B Torres 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T17:59:29+00:00"
 },
 {
  "id": "d430355dce99",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF No-Gi Championship Day 1 Winners",
  "snippet": "",
  "published": "2026-10-03T02:34:29+00:00"
 },
 {
  "id": "dedaf0690363",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Albert Chanbum Kim vs Zain Ul Haq 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T19:58:33+00:00"
 },
 {
  "id": "4e73d2e3e756",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship - Videos",
  "snippet": "",
  "published": "2026-10-03T19:00:40+00:00"
 },
 {
  "id": "6d9bb27190ac",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Kathryn Mary Egan vs Thaís Gomes Teixeira 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T19:59:23+00:00"
 },
 {
  "id": "6ac505c1cf31",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Grace Hunter Blanchette vs Emma Grace Artero 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T17:49:19+00:00"
 },
 {
  "id": "e4e76c656389",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Rochelle Lee Potter vs Vedha Clemente Toscano 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T16:35:33+00:00"
 },
 {
  "id": "7507116dcd65",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Gabriel Sonda Bevilacqua vs Rafael Reis Leite 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T16:35:32+00:00"
 },
 {
  "id": "e5f80a68c4b4",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Aliya V. Appassova vs Valentina Javiera Larrondo Peña 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-03T13:28:02+00:00"
 },
 {
  "id": "d67be2eccd21",
  "region": "intl",
  "source": "Combat Press",
  "title": "Ethan Crelinsten: From Montreal to a UFC BJJ Title Opportunity",
  "snippet": "",
  "published": "2026-10-03T23:28:35+00:00"
 },
 {
  "id": "1d3dafaa099f",
  "region": "intl",
  "source": "Combat Press",
  "title": "Gilbert Burns: Back to Jiu-Jitsu, With Another Title in Sight",
  "snippet": "",
  "published": "2026-10-03T15:03:43+00:00"
 },
 {
  "id": "37e12ffa2979",
  "region": "intl",
  "source": "facebook.com",
  "title": "ALL OUT SUPPORT FOR ALEX ❤️ Jiu jitsu athlete Alex Enriquez celebrates her 2026 #AsianGames silver medal with her fiancée and her mom, who flew all the way to Nagoya, Japan to watch her compete. #AichiNagoya2026 | via Paige Javier, ABS-CBN N",
  "snippet": "",
  "published": "2026-10-03T19:48:13+00:00"
 },
 {
  "id": "70dd314894af",
  "region": "intl",
  "source": "The Herald Journal",
  "title": "Asian Games Jiu-jitsu",
  "snippet": "",
  "published": "2026-10-03T07:21:06+00:00"
 },
 {
  "id": "c0faf1913c9e",
  "region": "intl",
  "source": "Qazinform",
  "title": "Kazakhstan’s Marian Zhuravleva wins bronze in jiu-jitsu at Asian Games",
  "snippet": "",
  "published": "2026-10-03T13:59:30+00:00"
 },
 {
  "id": "8e2a34f6920b",
  "region": "intl",
  "source": "アラブニュース",
  "title": "UAE claim 3 jiu-jitsu medals medals at Asian Games",
  "snippet": "",
  "published": "2026-10-03T17:19:38+00:00"
 },
 {
  "id": "771bcabce339",
  "region": "intl",
  "source": "Khaosod English",
  "title": "Thai jiu-jitsu athlete Orapa wins first Asian Games gold",
  "snippet": "",
  "published": "2026-10-03T05:38:43+00:00"
 },
 {
  "id": "6c4d4c3e091d",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Rainen Sky Cumberland vs Milla Sofia Mejia Pena 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T17:58:45+00:00"
 },
 {
  "id": "b7bcc1509ab5",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Kathryn Riley Irons vs Liubov Aleksandrovna Brown 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T17:58:45+00:00"
 },
 {
  "id": "60c128a574b0",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Continue Watching",
  "snippet": "",
  "published": "2026-10-02T23:14:24+00:00"
 },
 {
  "id": "64496ae09b93",
  "region": "intl",
  "source": "Sportscape Magazine",
  "title": "WATCH: Nate Diaz Playfully Gets Taken Down by a Group of Young BJJ Students",
  "snippet": "",
  "published": "2026-10-03T19:49:35+00:00"
 },
 {
  "id": "da176283975b",
  "region": "intl",
  "source": "facebook.com",
  "title": "PROUD OF YOU, ALEXANDRIA! 🥈🇵🇭 Filipina jiu-jitsu athlete Alexandria Luz Enriquez captures the silver medal in the women’s -63kg division after a close gold medal battle against Thailand’s Orapa Senatham at the 20th Asian Games in Aichi-Nagoya, Japa",
  "snippet": "",
  "published": "2026-10-03T06:10:58+00:00"
 },
 {
  "id": "d0f68b6a0c53",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Eduardo Henrique Dos Santos Silv vs Jorge Antonio Macías Arista 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-02T17:58:49+00:00"
 },
 {
  "id": "cc9be66ab003",
  "region": "intl",
  "source": "Qazinform",
  "title": "Kazakhstan claims silver in jiu-jitsu at 2026 Asian Games",
  "snippet": "",
  "published": "2026-10-03T06:34:34+00:00"
 },
 {
  "id": "fe6fc1e8ac68",
  "region": "intl",
  "source": "thenationalnews.com",
  "title": "UAE jiu-jitsu team's victorious campaign at Asian Games the 'start of a long journey'",
  "snippet": "",
  "published": "2026-10-03T10:07:36+00:00"
 },
 {
  "id": "ade96af2b965",
  "region": "intl",
  "source": "BJJEE",
  "title": "Xande Ribeiro Opens Up On The Daily Pain Behind His Decades-Long Career: “I Wake Up Every Day With Pain”",
  "snippet": "Xande Ribeiro has built one of the most enduring careers in Brazilian Jiu-Jitsu history, and his continued success at a high level has left many wondering what’s kept him going for so long. And, well, his answer isn’t particularly glamorous: I wake up every day with pain. Every day my shoulder hurts, every day my neck hurts, every day something hurts. I think this is something that we really have to deal with. Despite the constant discomfort, the 45-year-old champion credits much of his longevity to balance and self-awareness built over decades. From age 10 to 18, he trained five hours a day w…",
  "published": "2026-10-03T12:41:38+00:00"
 },
 {
  "id": "3a042bf3cd2f",
  "region": "intl",
  "source": "BJJEE",
  "title": "Helena Crevar On Becoming The Youngest ADCC Champion Ever: “99% Of My Training Is With Men”",
  "snippet": "At just 19, Helena Crevar has already made grappling history, becoming the youngest ADCC champion ever after capturing gold at 143 lbs (65kg) with three straight submissions… And in a recent interview on the FloGrappling Show, she opened up about her path to that moment and the significant role coach John Danaher has played in her development. Born and raised in Las Vegas to Serbian parents, Crevar started martial arts at three, trying Kajukenbo and even ballroom dance before discovering Jiu-Jitsu at eight. Her first class happened to be no-gi: I tried the Jiu-Jitsu class and I really liked it…",
  "published": "2026-10-03T12:29:42+00:00"
 },
 {
  "id": "ac3ae05b88f5",
  "region": "intl",
  "source": "BJJEE",
  "title": "Brendan Schaub Explains Why He Believes Mikey Musumeci Would Get “Annihilated” in the UFC",
  "snippet": "Former UFC heavyweight and Brazilian Jiu-Jitsu black belt Brendan Schaub has delivered a harsh assessment of Mikey Musumeci’s planned transition to MMA, arguing that even one of the greatest submission grapplers in the world could face serious problems against experienced UFC flyweights. Mikey Musumeci has spent years establishing himself as one of the most technically accomplished Brazilian Jiu-Jitsu competitors of his generation. The multiple-time world champion is famous for his extraordinary flexibility, intricate guard work, leg-lock attacks and ability to submit elite opponents. However,…",
  "published": "2026-10-03T12:25:53+00:00"
 }
]
