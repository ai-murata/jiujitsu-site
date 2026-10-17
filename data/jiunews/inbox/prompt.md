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
  "id": "fed6a667fd54",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "“最強芸人”４９歳ガリットチュウ福島、プロ格闘技「ＯＮＥ」参戦も一本負けで謝罪「ダメでした」朝倉未来の柔術コーチ・竹浦正起のヒールホールドでたまらずタップ（デイリースポーツ）",
  "snippet": "",
  "published": "2026-10-17T07:08:27+00:00"
 },
 {
  "id": "2392ad5cfd0e",
  "region": "jp",
  "source": "サンスポ",
  "title": "【ONE】朝倉未来の柔術コーチ・竹浦正起、ガリットチュウ・福島善成にヒールフックで一本勝ち ボーナス150万円を獲得",
  "snippet": "",
  "published": "2026-10-17T07:08:22+00:00"
 },
 {
  "id": "d0dfaa05c26c",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "【ONE】ガリットチュウ福島 大金星ならず…朝倉未来らのコーチを務める“格上”柔術家に一本負け",
  "snippet": "",
  "published": "2026-10-17T06:50:00+00:00"
 },
 {
  "id": "147294376568",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【ONE】吉成名高の“神技”さく裂KOで1500万円ボーナス！野杁正明がシアサラニを破りグレゴリアンとの決勝へ、ナビル・アナンが与座優貴に判定勝ち、平田樹がラズワンにリベンジ...",
  "snippet": "",
  "published": "2026-10-17T06:10:00+00:00"
 },
 {
  "id": "ccea0e5cac0a",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE】ガリットチュウ福島 無念一本負け「夢を与えようと…」朝倉未来の柔術コーチ相手に大金星ならず（スポニチアネックス）",
  "snippet": "",
  "published": "2026-10-17T06:49:55+00:00"
 },
 {
  "id": "102a5142fb33",
  "region": "jp",
  "source": "Infoseek",
  "title": "【ONE】手塚治虫コスプレで登場のガリットチュウ福島は竹浦正起のヒールフックで一本負け",
  "snippet": "",
  "published": "2026-10-17T07:41:07+00:00"
 },
 {
  "id": "9541488638e6",
  "region": "jp",
  "source": "サンスポ",
  "title": "【ONE】朝倉未来の柔術コーチ・竹浦正起、ガリットチュウ・福島善成にヒールフックで一本勝ち ボーナス150万円を獲得（写真・画像 1/1）",
  "snippet": "",
  "published": "2026-10-17T07:08:22+00:00"
 },
 {
  "id": "9dca67e9031d",
  "region": "jp",
  "source": "ラブすぽ",
  "title": "【開催レポート】クレベル・コイケ選手による特別柔術クラスを開催！渋谷アカデミーにて。ボンサイファミリーの絆を深める一日に",
  "snippet": "",
  "published": "2026-10-16T14:11:26+00:00"
 },
 {
  "id": "72689100abf3",
  "region": "jp",
  "source": "au Webポータル",
  "title": "ガリットチュウ福島、「ＯＮＥ ＳＡＭＵＲＡＩ ４」公開計量にオレンジ「ビキニ」で登場…竹浦正起とオープニングマッチで対戦…１０・１７有明アリーナ",
  "snippet": "",
  "published": "2026-10-16T22:45:00+00:00"
 },
 {
  "id": "2e3cc8984e7e",
  "region": "jp",
  "source": "efight.jp",
  "title": "【ONE】ガリットチュウ福島善成、寝技の強豪・竹浦正起に一本負け！最後はジョークで会場沸かす",
  "snippet": "",
  "published": "2026-10-17T07:17:59+00:00"
 },
 {
  "id": "f0ec05ccf5f3",
  "region": "jp",
  "source": "ニコニコチャンネル",
  "title": "夢を金で買う男? 長谷川秀樹の篤志家すぎる5年間を振り返る！：Dropkick",
  "snippet": "",
  "published": "2026-10-17T07:02:00+00:00"
 },
 {
  "id": "18e3a4382df1",
  "region": "jp",
  "source": "ENCOUNT",
  "title": "【ONE】電撃参戦のガリットチュウ・福島善成、無念の一本負け「40代、50代の皆様に少しでも夢を」 現役お笑い芸人の歴史的白星ならず",
  "snippet": "",
  "published": "2026-10-17T07:07:57+00:00"
 },
 {
  "id": "38b08e32f490",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【RIZIN甲子園】大晦日決勝は金子蒼空vs.松尾クリスチャンに！ 準決勝で金子が阿部に判定勝ち。松尾は横溝を極める。準々決勝4試合も「熱闘甲子園」に",
  "snippet": "",
  "published": "2026-10-17T07:10:00+00:00"
 },
 {
  "id": "bc763facf34d",
  "region": "jp",
  "source": "au Webポータル",
  "title": "【ONE】大舞台に“異例抜擢”も敗戦、ガリットチュウ・福島善成「寝れない日が続いた」 会見で明かした挑戦のワケ「今日が生涯一緊張」",
  "snippet": "",
  "published": "2026-10-17T08:22:00+00:00"
 },
 {
  "id": "1502a95ab559",
  "region": "jp",
  "source": "au Webポータル",
  "title": "“最強芸人”49歳ガリットチュウ福島、プロ格闘技「ONE」参戦も一本負けで謝罪「ダメでした」朝倉未来の柔術コーチ・竹浦正起のヒールホールドでたまらずタップ",
  "snippet": "",
  "published": "2026-10-17T07:07:00+00:00"
 },
 {
  "id": "d12c46fced64",
  "region": "jp",
  "source": "Howl.link",
  "title": "トライフォース柔術アカデミー 本部 (池袋) / Tri-force BJJ HQ (Ikebukuro) on Instagram: \"IBJJFパンパシフィック選手権2026🇦🇺 トライフォース公認アスリート 芝本幸司 🥇 鈴木和宏 🥇 篠田光宏 🥉 大黒喬士 🥉 応援ありがとうございました！\"",
  "snippet": "",
  "published": "2026-10-17T03:21:40+00:00"
 },
 {
  "id": "c847b8d7093f",
  "region": "jp",
  "source": "ライブドアニュース",
  "title": "【ONE】ガリットチュウ福島 無念一本負け「夢を与えようと…」朝倉未来の柔術コーチ相手に大金星ならず (2026年10月17日掲載)",
  "snippet": "",
  "published": "2026-10-17T06:49:55+00:00"
 },
 {
  "id": "7287de259ce5",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE】ガリットチュウ福島善成、寝技の強豪・竹浦正起に一本負け！最後はジョークで会場沸かす（イーファイト）",
  "snippet": "",
  "published": "2026-10-17T07:41:39+00:00"
 },
 {
  "id": "42f9b95c036b",
  "region": "jp",
  "source": "日テレNEWS NNN",
  "title": "ONE参戦ガリットチュウ福島 粘るも無念の一本負け 「40代、50代の人にちょっとでも夢を」 相手は貫禄勝ちにボーナス獲得…最後は「金ちょうだい」芸人魂も",
  "snippet": "",
  "published": "2026-10-17T08:23:00+00:00"
 },
 {
  "id": "0175341f98f2",
  "region": "jp",
  "source": "千葉テレビ放送株式会社",
  "title": "【ONE】電撃参戦のガリットチュウ・福島善成が無念の敗北 現役お笑い芸人の歴史的白星ならず…18歳下の黒帯実力者とグラップリングマッチ",
  "snippet": "",
  "published": "2026-10-17T06:52:21+00:00"
 },
 {
  "id": "6159b04a9df9",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "“最強芸人”４９歳ガリットチュウ福島、プロ格闘技「ＯＮＥ」参戦も一本負けで謝罪「ダメでした」朝倉未来の柔術コーチ・竹浦正起のヒールホールドでたまらずタップ",
  "snippet": "",
  "published": "2026-10-17T07:08:00+00:00"
 },
 {
  "id": "68ebaaf0a3d2",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【ONE】電撃参戦のガリットチュウ・福島善成、無念の一本負け「40代、50代の皆様に少しでも夢を」 現役お笑い芸人の歴史的白星ならず（ENCOUNT）",
  "snippet": "",
  "published": "2026-10-17T06:49:11+00:00"
 },
 {
  "id": "7f6eb5febfdf",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "ガリットチュウ福島善成、JTTコーチ竹浦正起に一本負け「生涯一緊張したかも」（サンケイスポーツ）",
  "snippet": "",
  "published": "2026-10-17T08:21:10+00:00"
 },
 {
  "id": "98abe9d5a369",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "ガリットチュウ福島、「ＯＮＥ」初参戦は一本負け…対戦相手「ボーナス」１５０万円ゲットに「僕にもお金ちょうだい」…１０・１７有明アリーナ",
  "snippet": "",
  "published": "2026-10-17T07:48:00+00:00"
 },
 {
  "id": "d5c10d006db7",
  "region": "jp",
  "source": "AGARA 紀伊民報",
  "title": "【ONE SAMURAI 4】ガリットチュウ福島、敗戦後は晴れやかな表情「リングに上がる人は本当に尊敬します」",
  "snippet": "",
  "published": "2026-10-17T07:50:00+00:00"
 },
 {
  "id": "5c53df395246",
  "region": "jp",
  "source": "AGARA 紀伊民報",
  "title": "【ONE SAMURAI 4】ガリットチュウ福島、ONE初参戦は無念の一本負け 敗戦後も芸人魂さく裂「チャトリ、俺にもお金ちょうだい」",
  "snippet": "",
  "published": "2026-10-17T07:33:00+00:00"
 },
 {
  "id": "c416a9d3c75f",
  "region": "jp",
  "source": "Infoseek",
  "title": "【ONE】ガリットチュウ福島「人生で一番緊張した」 無念の一本負け…入場でのコスプレの真相とは？",
  "snippet": "",
  "published": "2026-10-17T09:31:05+00:00"
 },
 {
  "id": "21ec7a79b210",
  "region": "jp",
  "source": "Howl.link",
  "title": "@まさか、立ち関節技の稽古がみんなとできるようになるとは…30年前には、想像できなかった(笑)手首取りからの立ち関節技打込み稽古 後編‼️骨法グラップリング19 Part 7 - YouTube",
  "snippet": "",
  "published": "2026-10-16T21:19:56+00:00"
 },
 {
  "id": "e1dc1f1d7ce5",
  "region": "intl",
  "source": "WhatNow",
  "title": "Gracie Barra Jiu-Jitsu Plans New Burlington Academy With Founding Memberships Starting at $99",
  "snippet": "",
  "published": "2026-10-16T20:11:03+00:00"
 },
 {
  "id": "4a54f193829a",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Valeriy.borkun vs Nick Sylla 2026 Fight to Win 328",
  "snippet": "",
  "published": "2026-10-16T23:25:39+00:00"
 },
 {
  "id": "3458d8f9aae3",
  "region": "intl",
  "source": "FloGrappling",
  "title": "WNO Unleashed",
  "snippet": "",
  "published": "2026-10-16T17:30:16+00:00"
 },
 {
  "id": "855a758200d3",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Sarah Vasquez vs Alonnie Stovall 2026 Fight to Win 328",
  "snippet": "",
  "published": "2026-10-17T00:55:32+00:00"
 },
 {
  "id": "f568aedd3892",
  "region": "intl",
  "source": "The Times of India",
  "title": "Who is Jaqueline Amorim? UFC strawweight star suspended for six months after failed drug tests",
  "snippet": "",
  "published": "2026-10-17T16:30:00+00:00"
 },
 {
  "id": "3e1658dbc4de",
  "region": "intl",
  "source": "vijesti.me",
  "title": "UP: PJP members win 19 medals at the European Police and Fire Games",
  "snippet": "",
  "published": "2026-10-17T08:50:17+00:00"
 },
 {
  "id": "68a354d4e7e8",
  "region": "intl",
  "source": "Big News Network.com",
  "title": "China tops standings on opening day of Abu Dhabi Grand Slam Jiu-Jitsu in Shanghai",
  "snippet": "",
  "published": "2026-10-17T18:39:00+00:00"
 },
 {
  "id": "e8461f5ca34c",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Fitness YouTuber Will Tennyson Did His First Ever BJJ class",
  "snippet": "",
  "published": "2026-10-17T21:19:17+00:00"
 },
 {
  "id": "4a2eaa7f13d9",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Boston Celtics Coach: Getting BJJ Blue Belt Felt The Same As Winning NBA Title",
  "snippet": "",
  "published": "2026-10-17T10:12:56+00:00"
 },
 {
  "id": "9e4b18956e5d",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Ralph Gracie on Melqui Galvao Trial: The Consequences Have To Be Severe",
  "snippet": "",
  "published": "2026-10-17T21:38:20+00:00"
 },
 {
  "id": "b8a5ebdeba3c",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Gracie Family Female Says Jiu-Jitsu “Saved My Life” While Summiting Mount Everest",
  "snippet": "",
  "published": "2026-10-17T07:44:57+00:00"
 },
 {
  "id": "d23f2ebee388",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Royce Gracie On Gracie Family’s Violent Reputation: “No, It’s People Being Disrespectful”",
  "snippet": "",
  "published": "2026-10-17T06:31:01+00:00"
 },
 {
  "id": "58d09a46f8c8",
  "region": "intl",
  "source": "BJJEE",
  "title": "Royce Gracie: “The Gracies Aren’t Violent – It’s The People Who Are Disrespectful”",
  "snippet": "Royce Gracie, who helped bring Brazilian Jiu-Jitsu to a global audience with his run through the early UFC tournaments, told Carlos Machado why he left California for Florida four years ago. The policies and culture were the problem, to be specific: (California is) too weak. People got too woke. It’s my right to sleep on your front yard. It’s like dude, it’s my house… So we had to move out cuz if not, we just couldn’t put up with that. His criticism widened to online behavior: It’s just a lot of people likes to talk because they hide behind the computer… There’s no accountability, man. People…",
  "published": "2026-10-17T17:20:13+00:00"
 },
 {
  "id": "d8422122bf22",
  "region": "intl",
  "source": "BJJEE",
  "title": "Cesalina Gracie Says Jiu-Jitsu “Saved My Life” On Everest Summit",
  "snippet": "Cesalina Gracie went to Mount Everest ready for altitude, cold, avalanches and the physical grind of climbing… But she did not expect her Jiu-Jitsu to matter because of the man running her expedition. She said the leader controlled her schedule, equipment and Sherpa assignment. When she pushed back on his comments and set a boundary, she said his treatment of her changed: He made some comments which is when I set a boundary with him… I told him don’t ever talk to me like this again. She described one incident in which he came into her tent, made a comment she would not repeat and put his hand…",
  "published": "2026-10-17T17:13:05+00:00"
 }
]
