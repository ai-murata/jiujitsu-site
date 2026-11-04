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
  "id": "fd12362e31e4",
  "region": "jp",
  "source": "ゴング格闘技",
  "title": "【PANCRASE】PFLから5年ぶりにPANCRASE参戦の菊入正行「嫁との付き合いから三年記念日の翌日にリリースの話が来て……」「日本でどれだけいいコンディションを作れる...",
  "snippet": "",
  "published": "2026-11-03T04:03:00+00:00"
 },
 {
  "id": "198ae02f3447",
  "region": "jp",
  "source": "au Webポータル",
  "title": "「最強の柔道家」木村政彦が顔面血だるまで沈んだ「力道山へのいけない挑発」／スポーツ界を揺るがせた「大問題発言」",
  "snippet": "",
  "published": "2026-11-03T00:45:00+00:00"
 },
 {
  "id": "87a9e2564e59",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "ベトナムのスポーツ界は、東南アジア競技大会の先を見据えている。",
  "snippet": "",
  "published": "2026-11-03T00:55:33+00:00"
 },
 {
  "id": "a6cf0700ea14",
  "region": "jp",
  "source": "Infoseek",
  "title": "「とんでもない夜になりそうだ」――タイ・ルオトロ、『インナー・サークル37』でクリスチャン・リーと対戦し、歴史を刻む準備は万端",
  "snippet": "",
  "published": "2026-11-02T23:37:32+00:00"
 },
 {
  "id": "881d9874106c",
  "region": "jp",
  "source": "Infoseek",
  "title": "「2Rで決着」――無敗のマグダレナ・チャバン、ONEファイトナイト49でのビクトリア・ソウザ戦をストップ勝ちと予想",
  "snippet": "",
  "published": "2026-11-03T02:01:02+00:00"
 },
 {
  "id": "4893854b894b",
  "region": "jp",
  "source": "efight.jp",
  "title": "車いすで首にコルセットを巻くツーウェイ。その横にはソン・ヤドン（＠kurabank）",
  "snippet": "",
  "published": "2026-11-03T09:17:30+00:00"
 },
 {
  "id": "65c63e5d7fa3",
  "region": "jp",
  "source": "Howl.Link",
  "title": "レターより 膝の音は問題あるの？ - SPINS of spinmaster | stand.fm",
  "snippet": "",
  "published": "2026-11-03T06:35:39+00:00"
 },
 {
  "id": "de1aa40bd672",
  "region": "jp",
  "source": "DAZN",
  "title": "コルビー・コビントン対ラウル・ロサスJr.をDAZNでライブ＆無料視聴する方法",
  "snippet": "",
  "published": "2026-11-03T11:11:15+00:00"
 },
 {
  "id": "6d889d30d0e3",
  "region": "jp",
  "source": "DAZN",
  "title": "ディロン・ダニス欠場でUFCスターがコルビー・コビントンの対戦相手に",
  "snippet": "",
  "published": "2026-11-03T10:23:57+00:00"
 },
 {
  "id": "57e9c336c865",
  "region": "jp",
  "source": "Infoseek",
  "title": "【ＤＤＴ】ザック・セイバーJr. 青木真也との一騎打ち制す「あれだけのグラップラーに勝てたのは重大な意味」",
  "snippet": "",
  "published": "2026-11-03T10:42:32+00:00"
 },
 {
  "id": "d7334c47037d",
  "region": "jp",
  "source": "Infoseek",
  "title": "『インナー・サークル 37』と『ONE ファイトナイト 49』を控えての3つの注目ポイント",
  "snippet": "",
  "published": "2026-11-03T10:20:13+00:00"
 },
 {
  "id": "40d46edd5e20",
  "region": "intl",
  "source": "NBC 6 South Florida",
  "title": "Person who assisted at Brazilian Jiu-Jitsu school in Coral Springs arrested, school says",
  "snippet": "",
  "published": "2026-11-03T22:09:51+00:00"
 },
 {
  "id": "030bfc9c3cfd",
  "region": "intl",
  "source": "UFC.com",
  "title": "UFC BJJ 14: Tackett vs Wojcik Fight Card",
  "snippet": "",
  "published": "2026-11-03T20:45:00+00:00"
 },
 {
  "id": "1508a3ac5fdd",
  "region": "intl",
  "source": "The Gabber Newspaper",
  "title": "From Park to Gym: Coach Brings Jiu-Jitsu to Gulfport",
  "snippet": "",
  "published": "2026-11-03T21:49:50+00:00"
 },
 {
  "id": "276def3d4718",
  "region": "intl",
  "source": "Statesman-Examiner",
  "title": "More Than Fighting",
  "snippet": "",
  "published": "2026-11-03T16:34:19+00:00"
 },
 {
  "id": "fb66026017b2",
  "region": "intl",
  "source": "Yahoo",
  "title": "Jiu Jitsu Meets Hardcore: A Band Rocks the Mats!",
  "snippet": "",
  "published": "2026-11-03T18:00:00+00:00"
 },
 {
  "id": "230beac8572c",
  "region": "intl",
  "source": "Revgear",
  "title": "Meet Robson Gracie Jr: The Next Generation of Gracie Jiu-Jitsu",
  "snippet": "",
  "published": "2026-11-03T08:00:00+00:00"
 },
 {
  "id": "38e6f9527248",
  "region": "intl",
  "source": "BJJ Heroes",
  "title": "2026 IBJJF European No-Gi Championship Results",
  "snippet": "",
  "published": "2026-11-02T13:59:20+00:00"
 },
 {
  "id": "1ef9a70ea258",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 CBJJ Brazilian Jiu-Jitsu Championship No-Gi - Videos",
  "snippet": "",
  "published": "2026-11-03T13:31:22+00:00"
 },
 {
  "id": "4d81ef0df017",
  "region": "intl",
  "source": "DVIDS",
  "title": "1st Battalion, 67th Armor Regiment combat medic earns gold medal at Fort Bliss BJJ Competition",
  "snippet": "",
  "published": "2026-11-02T23:11:00+00:00"
 },
 {
  "id": "248c1bdfad8a",
  "region": "intl",
  "source": "WBIR",
  "title": "Bearden middle schooler wins Pan-American Jiu-Jitsu title",
  "snippet": "",
  "published": "2026-11-02T17:41:00+00:00"
 },
 {
  "id": "337a31142f59",
  "region": "intl",
  "source": "Trinidad Guardian",
  "title": "Blackman wins gold at European Jiu-Jitsu Championships",
  "snippet": "",
  "published": "2026-11-03T16:54:40+00:00"
 },
 {
  "id": "2962288bdec4",
  "region": "intl",
  "source": "boxingnews.com",
  "title": "UFC BJJ 14: Tackett vs Wojcik — Full Card, Start Time & How to Watch",
  "snippet": "",
  "published": "2026-11-03T23:02:27+00:00"
 },
 {
  "id": "5b95b0c3506e",
  "region": "intl",
  "source": "Азия-Плюс",
  "title": "Tajikistan tops jiu-jitsu medal table in Tashkent with 35 golds",
  "snippet": "",
  "published": "2026-11-03T04:59:33+00:00"
 },
 {
  "id": "68eab525a0f4",
  "region": "intl",
  "source": "Nanaimo News Bulletin",
  "title": "Nanaimo jiu-jitsu academy ‘tops’ at Abu Dhabi Combat Club open on Mainland",
  "snippet": "",
  "published": "2026-11-02T13:51:03+00:00"
 },
 {
  "id": "094317dda2a4",
  "region": "intl",
  "source": "Ipswich Star",
  "title": "Ipswich boy, 11, wins European gold and now sets sights on world title",
  "snippet": "",
  "published": "2026-11-03T04:30:00+00:00"
 },
 {
  "id": "ba8e6b94387a",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Breaking Down The Brackets For IBJJF's The Crown On November 8th",
  "snippet": "",
  "published": "2026-11-03T17:27:42+00:00"
 },
 {
  "id": "4eeca2d3c725",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Cody Rhodes Admits He Almost Left WWE for MMA Before Brandi Rhodes Stepped In",
  "snippet": "",
  "published": "2026-11-03T14:29:40+00:00"
 },
 {
  "id": "e56373c87183",
  "region": "intl",
  "source": "City Lifestyle",
  "title": "8 Things Holistic Moms Are Doing This Cold and Flu Season",
  "snippet": "",
  "published": "2026-11-03T20:37:44+00:00"
 },
 {
  "id": "1a94c2523245",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Studio Chat With FloGrappling GM Ben Kovacs",
  "snippet": "",
  "published": "2026-11-03T01:26:13+00:00"
 },
 {
  "id": "da37d7ba7abd",
  "region": "intl",
  "source": "Combat Press",
  "title": "Grand Sumo: How to Watch the 2026 Kyushu Basho",
  "snippet": "",
  "published": "2026-11-03T20:59:00+00:00"
 },
 {
  "id": "804fc7b77eda",
  "region": "intl",
  "source": "Forces News",
  "title": "Save the dates! Army and Navy Sports Awards to be broadcast LIVE",
  "snippet": "",
  "published": "2026-11-02T14:32:18+00:00"
 },
 {
  "id": "20da638ff961",
  "region": "intl",
  "source": "Derry Now",
  "title": "Team Torres Derry prodigy Tyainon Cartin clinches major european title",
  "snippet": "",
  "published": "2026-11-03T12:00:00+00:00"
 },
 {
  "id": "4592266e5fc1",
  "region": "intl",
  "source": "Liverpool Echo",
  "title": "‘We're not trying to change the world, just South Road’",
  "snippet": "",
  "published": "2026-11-02T21:18:00+00:00"
 },
 {
  "id": "6d98a2958d14",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "UFC BJJ 13 Full Results And Highlights",
  "snippet": "",
  "published": "2026-11-03T12:44:28+00:00"
 },
 {
  "id": "1a49eae044ac",
  "region": "intl",
  "source": "BJJDOC",
  "title": "John Danaher Brown Belt Says Jiu-Jitsu Is ‘An Intellectual Pursuit First,’ Calls Out Hobbyists Who Won’t Study 20 Minutes A Day",
  "snippet": "",
  "published": "2026-11-03T13:18:45+00:00"
 },
 {
  "id": "10cf0300bd2a",
  "region": "intl",
  "source": "BJJEE",
  "title": "Russia Bans Its Wrestling National Team Members From Competing In RAF",
  "snippet": "Russia’s freestyle wrestling program has barred national team members from Real American Freestyle (RAF). Head coach Khadzhimurat Gatsalov announced that athletes who earn their spots at the Russian Championships will no longer be allowed to compete in the American promotion. The decision follows Russia’s showing at the World Championships in Astana, Kazakhstan, where the team won 14 medals, four of them gold. Gatsalov was unhappy with the preparation of three athletes who had fought in RAF – Ismail Khaniyev, Ibragim Kadiev and two-time Olympic champion Abdulrashid Sadulaev: Three guys, Khanie…",
  "published": "2026-11-03T09:43:16+00:00"
 },
 {
  "id": "05c5dddbe99c",
  "region": "intl",
  "source": "BJJEE",
  "title": "Robert Drysdale Calls UFC Event On White House Lawn “Insulting To The Memory Of This Country”",
  "snippet": "ADCC gold medalist and UFC veteran Robert Drysdale has strongly criticized the recent UFC event held on the White House lawn. The Brazilian Jiu-Jitsu legend and historian spoke on The Mat Minute podcast and framed the issue as one of American values, not of MMA itself: Having the UFC on the White House lawn, I think it’s insulting to the memory of this country. Personally, I think if any of the founding fathers were alive, they would have been losing their mind. They’re turning on their graves watching that. I love the UFC. It’s done a lot for me. I love the sport, MMA. I just don’t think that…",
  "published": "2026-11-03T09:25:52+00:00"
 },
 {
  "id": "e757719ca743",
  "region": "intl",
  "source": "Jits Magazine",
  "title": "Victor Hugo Opens Up About Potentially Retiring From ADCC",
  "snippet": "Victor Hugo capped off his ADCC journey with four submissions in four matches, explaining that injuries, business commitments and impending fatherhood helped shape his decision to step away from the prestigious tournament. Hugo has achieved the ultimate goal in submission grappling. After years of competing against the world’s best, the Brazilian heavyweight captured his first ADCC World Championship title in September 2026, submitting Josh Saunders in the +99kg final . In the aftermath of that victory, Hugo revealed that he does not expect to return for another edition of the tournament, brin…",
  "published": "2026-11-03T11:23:38+00:00"
 }
]
