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
  "id": "6995f7dea5ad",
  "region": "jp",
  "source": "TVer",
  "title": "熊本DEデニスのルーツ巡り！絶品カレー＆柔術で大波乱！衝撃デニ怖話も",
  "snippet": "",
  "published": "2026-10-20T16:21:41+00:00"
 },
 {
  "id": "1852418770b4",
  "region": "jp",
  "source": "Infoseek",
  "title": "石井慧が現役復帰を決断！元ＰＦＬ王者との対戦で「手応えつかんだ」２年ぶりＭＭＡは〝最終章〟",
  "snippet": "",
  "published": "2026-10-20T20:02:18+00:00"
 },
 {
  "id": "d5f83ea397f4",
  "region": "jp",
  "source": "KAB 熊本朝日放送",
  "title": "カラシコンボ » 2026年10月20日（火）熊本DEデニスのルーツ巡り！絶品カレー＆柔術で大波乱！衝撃デニ怖話も",
  "snippet": "",
  "published": "2026-10-20T02:56:27+00:00"
 },
 {
  "id": "7f43974fb6e4",
  "region": "jp",
  "source": "efight.jp",
  "title": "現役警官が元受刑者に素手ボクシングで失神KO勝利！「合法的にブチのめせる」＝海外",
  "snippet": "",
  "published": "2026-10-20T08:08:15+00:00"
 },
 {
  "id": "396ea05c3e85",
  "region": "jp",
  "source": "efight.jp",
  "title": "ぱんちゃん璃奈、割れた腹筋と”分厚い”広背筋に成長！今週23日に再起なるか「ムエタイ技術で挑む」",
  "snippet": "",
  "published": "2026-10-20T03:19:41+00:00"
 },
 {
  "id": "0ebc0154f793",
  "region": "jp",
  "source": "ブラジル日報",
  "title": "商議所＝伝説の柔道家・前田光世の半生描く＝大友啓史監督『コンデコマ』始動＝日伯米合作のアクション超大作",
  "snippet": "",
  "published": "2026-10-19T21:57:24+00:00"
 },
 {
  "id": "87c3512886f8",
  "region": "jp",
  "source": "YouTube",
  "title": "ONE SAMURAI4を観て感じた色々な事",
  "snippet": "",
  "published": "2026-10-19T12:39:32+00:00"
 },
 {
  "id": "cfc7d3586418",
  "region": "jp",
  "source": "イーファイト",
  "title": "【パンクラス】3大タイトル戦が決定！神谷大智は日本に王座奪還となるか",
  "snippet": "",
  "published": "2026-10-20T07:03:32+00:00"
 },
 {
  "id": "655db358d649",
  "region": "jp",
  "source": "Mogura VR",
  "title": "2D登山ゲーム『Mount Lomyst』、MyDearestのゲームレーベル「BACHI BACHI GAMES」がパブリッシング担当に",
  "snippet": "",
  "published": "2026-10-20T03:02:35+00:00"
 },
 {
  "id": "9ce7a5f3ccd6",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "この登山ゲーム、ジャンプができない!?BitSummitで「ファミ通賞」など2冠の『Mount",
  "snippet": "",
  "published": "2026-10-20T12:48:29+00:00"
 },
 {
  "id": "91fca2e126bb",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "【RIZIN】「甲子園」決勝カードが決定 大みそかで日本一の高校生を目指し対戦",
  "snippet": "",
  "published": "2026-10-20T07:30:30+00:00"
 },
 {
  "id": "2d84f060d114",
  "region": "jp",
  "source": "神ゲー攻略",
  "title": "【ヴァルヘイム】硫黄の入手方法と使い道【Valheim】",
  "snippet": "",
  "published": "2026-10-20T08:16:00+00:00"
 },
 {
  "id": "04b74b47896f",
  "region": "jp",
  "source": "Dellows News",
  "title": "ONE SAMURAI 4追加カード発表 福島善成対竹浦正起が決定",
  "snippet": "",
  "published": "2026-10-19T22:35:57+00:00"
 },
 {
  "id": "206f88ee64e2",
  "region": "intl",
  "source": "DVIDS",
  "title": "Building Strength and Discipline Through Jiu-Jitsu [Image 1 of 5]",
  "snippet": "",
  "published": "2026-10-20T14:05:00+00:00"
 },
 {
  "id": "f39d43c9579f",
  "region": "intl",
  "source": "Williams-Grand Canyon News",
  "title": "Route 66 Jiu Jitsu wins Southwest Classic, claims No. 1 ranking",
  "snippet": "",
  "published": "2026-10-20T16:05:00+00:00"
 },
 {
  "id": "7142af5b778e",
  "region": "intl",
  "source": "Arab News",
  "title": "Baniyas and Sharjah Self-Defence retain titles at Khaled bin Mohamed bin Zayed Jiu-Jitsu Championship",
  "snippet": "",
  "published": "2026-10-20T08:08:41+00:00"
 },
 {
  "id": "2807b8da94fe",
  "region": "intl",
  "source": "MyMMANews",
  "title": "Best Martial Arts for MMA in 2026: Wrestling, BJJ, Boxing and More",
  "snippet": "",
  "published": "2026-10-20T15:38:13+00:00"
 },
 {
  "id": "a9983e3501e5",
  "region": "intl",
  "source": "Magzter",
  "title": "Baniyas, Sharjah Self-Defence Club retain jiu-jitsu championship titles | Gulf Today - newspaper",
  "snippet": "",
  "published": "2026-10-20T04:36:56+00:00"
 },
 {
  "id": "d080c038674e",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Omar French",
  "snippet": "",
  "published": "2026-10-19T23:11:45+00:00"
 },
 {
  "id": "a434e404c31d",
  "region": "intl",
  "source": "PressReader",
  "title": "Sur siblings secure double gold at internatio­nal championsh­ip",
  "snippet": "",
  "published": "2026-10-19T16:36:42+00:00"
 },
 {
  "id": "9b4244ad6442",
  "region": "intl",
  "source": "Daily Press",
  "title": "Suffolk’s Landon Jones earns chance to compete for WBC Muay Thai national championship",
  "snippet": "",
  "published": "2026-10-20T22:11:50+00:00"
 },
 {
  "id": "15c54a6ce5f8",
  "region": "intl",
  "source": "Bold Journey Magazine",
  "title": "Meet Bryan Medina",
  "snippet": "",
  "published": "2026-10-20T04:00:35+00:00"
 },
 {
  "id": "40e8203acf76",
  "region": "intl",
  "source": "FloGrappling",
  "title": "How Kit Dale Brought 'WHITE BELT' The Movie To Life | The FloGrappling Show (Ep 109)",
  "snippet": "",
  "published": "2026-10-20T19:40:47+00:00"
 },
 {
  "id": "cb2623d1eee3",
  "region": "intl",
  "source": "FloGrappling",
  "title": "The Top 10 Leg Locks From The 2026 ADCC World Championship",
  "snippet": "",
  "published": "2026-10-20T21:57:06+00:00"
 },
 {
  "id": "f7c64145cdce",
  "region": "intl",
  "source": "Yahoo Sports",
  "title": "Brutal slam becomes knockout of the year contender",
  "snippet": "",
  "published": "2026-10-19T19:29:44+00:00"
 },
 {
  "id": "0febddc2b407",
  "region": "intl",
  "source": "Sherdog",
  "title": "Glover Teixeira: 3-0 UFC finisher Yousri Belgaroui is evolving on ground",
  "snippet": "",
  "published": "2026-10-20T01:52:22+00:00"
 },
 {
  "id": "bb829de63ae2",
  "region": "intl",
  "source": "MMA Fighting",
  "title": "Charles Oliveira: If the BMF belt is about rock ‘em sock ‘em robots, ‘take it somewhere else’",
  "snippet": "",
  "published": "2026-10-19T15:00:00+00:00"
 },
 {
  "id": "fbb771d4ca67",
  "region": "intl",
  "source": "Fightomic",
  "title": "Katlyn Cerminara Profile: UFC Record, Bio and Latest Fight",
  "snippet": "",
  "published": "2026-10-19T22:55:28+00:00"
 },
 {
  "id": "d1535766a35e",
  "region": "intl",
  "source": "inkl",
  "title": "Controversial UFC champion declares: ‘Take the belt, it’s not for me’",
  "snippet": "",
  "published": "2026-10-19T21:58:51+00:00"
 },
 {
  "id": "b76dafd7144e",
  "region": "intl",
  "source": "Sharjah24",
  "title": "Kalba Women’s Sports Club wins Abu Dhabi Junior Judo title",
  "snippet": "",
  "published": "2026-10-19T17:20:07+00:00"
 },
 {
  "id": "1953e93b939b",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Legendary Brazilian Paulo Filho Can't Promote BJJ Black Belts Due To Federation Requirements",
  "snippet": "",
  "published": "2026-10-20T15:42:00+00:00"
 },
 {
  "id": "0b13f42442e0",
  "region": "intl",
  "source": "BJJDOC",
  "title": "WATCH: 14 Year Old Girl Immobilizes Burglar Using Jiu Jitsu, Restrains Him For 15 Minutes Waiting For Police",
  "snippet": "",
  "published": "2026-10-20T15:24:05+00:00"
 },
 {
  "id": "38247d745884",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Keith Krikorian: Treating Someone Differently Because They’re A Lower Belt Is Wrong",
  "snippet": "",
  "published": "2026-10-20T07:38:54+00:00"
 },
 {
  "id": "7e6e9c3640b3",
  "region": "intl",
  "source": "BJJDOC",
  "title": "Judo Olympic Silver Medalist Travis Stevens: Salad Isn't Helping You Win, Get A Cheeseburger",
  "snippet": "",
  "published": "2026-10-20T08:29:44+00:00"
 },
 {
  "id": "13deecb7b1d5",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Vetoraci Twins Enter Different Divisions At IBJJF Crown",
  "snippet": "",
  "published": "2026-10-20T00:54:10+00:00"
 },
 {
  "id": "a5d0ae58f938",
  "region": "intl",
  "source": "MiddleEasy",
  "title": "Javier Mendez Says Cain Velasquez Is In Talks To Compete In RAF",
  "snippet": "",
  "published": "2026-10-20T00:54:10+00:00"
 },
 {
  "id": "232928b507c7",
  "region": "intl",
  "source": "FightBook MMA",
  "title": "How MMA Reinvented Itself In The Modern Era",
  "snippet": "",
  "published": "2026-10-19T23:47:45+00:00"
 },
 {
  "id": "5874995379a9",
  "region": "intl",
  "source": "SuaraGarut.ID",
  "title": "Charles Oliveira Defends His MMA Style Ahead of UFC 335",
  "snippet": "",
  "published": "2026-10-19T19:00:00+00:00"
 },
 {
  "id": "e2ac94d0616b",
  "region": "intl",
  "source": "BJJEE",
  "title": "Megaton Dias On Training With Rickson Gracie: “I Couldn’t Do Anything”",
  "snippet": "Wellington “Megaton” Dias holds 20 world titles – but the coral belt still remembers being completely shut down by two of the sport’s most celebrated names. In a recent video, Dias looked back on training with Rickson Gracie: I trained with Rickson, bro… I couldn’t do anything. He had a lot of muscle. You’re just going to do something without him letting you do it. The admission comes weeks after he made history at the IBJJF World Master Championship in Las Vegas, where he won his 20th world title in early September. He competed in the Master 7 division and arrived with momentum, having alread…",
  "published": "2026-10-20T06:41:40+00:00"
 },
 {
  "id": "b8057162e836",
  "region": "intl",
  "source": "BJJEE",
  "title": "(WATCH) UFC Edmonton Video Shows Police Officer Suplexing Fan",
  "snippet": "A video of a crowd brawl at Saturday’s UFC event in Edmonton is spreading on social media, and it appears to show a police officer throwing a fan with a suplex. The event took place at Rogers Place in Edmonton, Alberta. The clip allegedly captures an altercation involving fans, arena security and Edmonton police officers. In it, an officer appears to grab a person from behind and throw them backward, and the person lands hard on the ground. The impact seems to leave the person stiff. The footage also suggests the person may have been tasered afterward, but what happens next is hard to make out…",
  "published": "2026-10-20T06:35:19+00:00"
 }
]
