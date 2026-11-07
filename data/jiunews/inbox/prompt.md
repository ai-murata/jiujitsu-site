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
  "id": "f50700765861",
  "region": "jp",
  "source": "イーファイト",
  "title": "【パンクラス】菊入正行、平信一の“投げたら勝ち”に「何もさせない」！5年ぶり復帰へ闘志",
  "snippet": "",
  "published": "2026-11-06T11:39:23+00:00"
 },
 {
  "id": "bece100c140d",
  "region": "jp",
  "source": "イーファイト",
  "title": "【RIZIN】バンタム級サバイバルマッチ！鹿志村仁之介「絶対負けられない」太田忍「一方的にぶん殴る」",
  "snippet": "",
  "published": "2026-11-06T11:49:42+00:00"
 },
 {
  "id": "75cbe0521b37",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【ONE】王者クリスチャン・リーに挑戦するタイ・ルオトロ「MMAグラップリングは違う？ エイドリアンも同じことを言っていた。自信を持つのは良いことだが、妄想の域に達してしまい...",
  "snippet": "",
  "published": "2026-11-06T12:46:45+00:00"
 },
 {
  "id": "2f1bcddca6fb",
  "region": "jp",
  "source": "Infoseek",
  "title": "『インナー・サークル37』メインイベントの結果：タイ・ルオトロが第1ラウンドでクリスチャン・リーを破り、2種目王者となる",
  "snippet": "",
  "published": "2026-11-06T13:57:08+00:00"
 },
 {
  "id": "c464e38e11b8",
  "region": "jp",
  "source": "Mix Vale",
  "title": "柔術家のLucas Portela Fontana Gomes（32歳）、リオのティジュカでエレベーター内の女性を殴り逮捕",
  "snippet": "",
  "published": "2026-11-06T14:00:48+00:00"
 },
 {
  "id": "fd0353c3ccc8",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE】グラップリング王者タイ・ルオトロがMMA3戦目でライト級絶対王者クリスチャン・リーを左でダウン奪い、チョーク極めてベルト奪取！「1Rで終わらせるつもりだった」 (ゴング格闘技)",
  "snippet": "",
  "published": "2026-11-06T16:27:53+00:00"
 },
 {
  "id": "80676ef84c9b",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【ONE】タイ・ルオトロと対戦する二階級制覇王者クリスチャン・リー「プロセスを急ぐことはできない。5Rの王座戦の準備をするには、まったく異なるレベルの経験が必要。彼はまだ準備...",
  "snippet": "",
  "published": "2026-11-06T10:36:32+00:00"
 },
 {
  "id": "8462a8014ad4",
  "region": "jp",
  "source": "Infoseek",
  "title": "ONE Fight Night 49 計量および水分補給テストの結果",
  "snippet": "",
  "published": "2026-11-06T11:54:54+00:00"
 },
 {
  "id": "20b977a9e45f",
  "region": "jp",
  "source": "週刊ファイト",
  "title": "タイ・ルオトロ2種め獲得＆1500万円超ボーナス！日本2勝2敗 ONE FF ＆ TIC",
  "snippet": "",
  "published": "2026-11-07T00:46:45+00:00"
 },
 {
  "id": "b0105cd227b6",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "image-1793965570.jpg",
  "snippet": "",
  "published": "2026-11-06T12:17:46+00:00"
 },
 {
  "id": "4a6e6f880f79",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "image-1793874570.jpg",
  "snippet": "",
  "published": "2026-11-06T10:07:08+00:00"
 },
 {
  "id": "641fd2cb9525",
  "region": "jp",
  "source": "Infoseek",
  "title": "『ザ・インナー・サークル 37』および『ONE フライデー・ファイト 177』――全試合の結果とハイライト",
  "snippet": "",
  "published": "2026-11-06T03:18:26+00:00"
 },
 {
  "id": "ba67795a076c",
  "region": "intl",
  "source": "MMA Mania",
  "title": "BJJ star Tye Ruotolo shocks Christian Lee, wins MMA title in 3rd bout | Video",
  "snippet": "",
  "published": "2026-11-06T16:00:00+00:00"
 },
 {
  "id": "d159548c1d22",
  "region": "intl",
  "source": "MyMMANews",
  "title": "Over 10,000 athletes from 130 countries set to compete at 18th Abu Dhabi World Professional Jiu-Jitsu Championship",
  "snippet": "",
  "published": "2026-11-07T00:26:38+00:00"
 },
 {
  "id": "f0c5e9aa2160",
  "region": "intl",
  "source": "The Worcester Guardian",
  "title": "Worcester’s youngest jiu-jitsu competitors bring home team title",
  "snippet": "",
  "published": "2026-11-06T02:46:48+00:00"
 },
 {
  "id": "e6c5a4182eab",
  "region": "intl",
  "source": "WVLT",
  "title": "Bearden Middle School student crowned Pan American Jiu-Jitsu Champion",
  "snippet": "",
  "published": "2026-11-06T04:21:00+00:00"
 },
 {
  "id": "c7c9776d8209",
  "region": "intl",
  "source": "Sportsnet.ca",
  "title": "Will Suarez’s elite wrestling be too much for Jandiroba’s Brazilian jiu-jitsu?",
  "snippet": "",
  "published": "2026-11-06T10:04:00+00:00"
 },
 {
  "id": "882830812473",
  "region": "intl",
  "source": "auroradesio.it",
  "title": "Brazilian Jiu Jitsu Hoodies - Discover Traditional Clothing in Brazil Today",
  "snippet": "",
  "published": "2026-11-06T18:58:12+00:00"
 },
 {
  "id": "7c3f570cc624",
  "region": "intl",
  "source": "12News",
  "title": "Tapping out, not giving in: Veterans find better mental health on the mat in Mesa",
  "snippet": "",
  "published": "2026-11-05T15:02:00+00:00"
 },
 {
  "id": "95fba0713fb8",
  "region": "intl",
  "source": "Bendigo Advertiser",
  "title": "'Added 20 years to my life': Transformed Bendigo father targets world glory",
  "snippet": "",
  "published": "2026-11-06T23:42:23+00:00"
 },
 {
  "id": "8343821e6c07",
  "region": "intl",
  "source": "Big News Network.com",
  "title": "UAE Jiu-Jitsu Federation launches award honouring champions' families",
  "snippet": "",
  "published": "2026-11-06T18:54:00+00:00"
 },
 {
  "id": "94a3075928d6",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Garry Tonon Cautions BJJ Students: Stop Memorizing Random Moves",
  "snippet": "",
  "published": "2026-11-06T19:10:47+00:00"
 },
 {
  "id": "f67b83eec54d",
  "region": "intl",
  "source": "BJJDOC",
  "title": "FloGrappling General Manager Details How UFC BJJ Is Hurting The Sport",
  "snippet": "",
  "published": "2026-11-06T17:10:06+00:00"
 },
 {
  "id": "532c9cea9ded",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Tye Ruotolo: Jiu-Jitsu Is In A Weird ‘Fragmented’ Spot",
  "snippet": "",
  "published": "2026-11-06T12:03:07+00:00"
 },
 {
  "id": "d6e73932e525",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Islam Makhachev Dismisses BJJ During Sambo World Championship Press Conference",
  "snippet": "",
  "published": "2026-11-06T10:55:15+00:00"
 }
]
