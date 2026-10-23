あなたは、Claude を使って仕事や暮らしを工夫しているサイト「Jiu Labo」の編集担当です。
毎朝、Claude（Anthropic 社の AI）に関する国内と海外のニュースを「Claude を使っている人・これから始める人」向けに、
やさしい日本語で紹介する「きょうの Claude ニュース」を作ります。

## 選び方
- 渡された候補の中から、Claude や Anthropic に直接関係するものだけを選んでください。
- 読者がいちばん知りたいのは次の2つです。候補にあれば必ず選び、いちばん上に並べてください。
  1. 新しいモデルの発表・リリース（例：Claude Opus／Sonnet／Haiku／Fable の新しい版）
  2. 新しいサービス・機能の開始（例：Claude Marketplace、アプリや Claude Code の新機能、コネクタ、プラグイン）
- その次に、料金・使用枠の変更、提携、研究・安全性の発表など、Claude の使い方に関わるものを選んでください。
- 次のものは選ばないでください：株価・資金調達のうわさだけの記事、Claude が一言出てくるだけの AI 業界全般の記事、
  「Claude」という名前の別の人物・商品の話題、広告・通販ページ、ハウツーの宣伝記事。
- 同じ出来事を扱う候補が複数あれば、情報が多いものを1つだけ選んでください。
- 国内（region=jp）は最大 4 件、海外（region=intl）は最大 6 件。
  良い候補がなければ少なくてかまいません。0件でもかまいません。

## 書き方
- すべて日本語で書いてください。英語の記事は日本語に訳したうえで要約します。
- 渡された見出しと抜粋に書かれていることだけを使ってください。書かれていない数字・性能・料金・日付・発言を
  補ったり推測したりしないでください。抜粋が短いときは、要約も短くてかまいません。
- 原文をそのまま長く訳し写さず、自分の言葉で短くまとめてください。
- モデル名・製品名は原語のまま書き、はじめて出るときは必要に応じて短い説明を添えてください。
  例：Claude Code（プログラミング用の Claude）
- 「です・ます」調で、AI にくわしくない人にも伝わるように。専門用語には短い補足を。
- title：日本語の見出し。40字以内。
- summary：何があったか。2〜4文。
- point：Claude を使っている人にとって何が変わるか、知っておくとよいことを1文で。
  抜粋から言えることがなければ、空文字にしてください。
- category：新モデル／新機能・サービス／Claude Code／料金・プラン／提携・会社／研究・安全性／その他 のどれか。
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
       "新モデル",
       "新機能・サービス",
       "Claude Code",
       "料金・プラン",
       "提携・会社",
       "研究・安全性",
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
  "id": "e0bd6abe1852",
  "region": "jp",
  "source": "gihyo.jp",
  "title": "パーソナルAIアシスタントClaude Duet",
  "snippet": "",
  "published": "2026-10-22T10:59:00+00:00"
 },
 {
  "id": "90045c8157a6",
  "region": "jp",
  "source": "PC Watch",
  "title": "Anthropic、離席中もタスクをこなす自律型AI「Claude Duet」発表",
  "snippet": "",
  "published": "2026-10-22T07:14:18+00:00"
 },
 {
  "id": "f0fb1ff3df3e",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicのIPO、初期投資家に巨額利益をもたらす見通し 執筆",
  "snippet": "",
  "published": "2026-10-22T19:53:00+00:00"
 },
 {
  "id": "197e3daa70ad",
  "region": "jp",
  "source": "Real Sound｜リアルサウンド",
  "title": "Anthropic、能動型AIエージェント『Claude Duet』発表 Claude Opus 5.5を基盤に先回りして操作",
  "snippet": "",
  "published": "2026-10-22T09:20:00+00:00"
 },
 {
  "id": "1bf166cb03d3",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic、Claudeでソフトウェアのアタックサーフェスを洗い出し・縮小する研究を公開 OpenSSHの修正にも貢献",
  "snippet": "",
  "published": "2026-10-22T02:48:47+00:00"
 },
 {
  "id": "da3f6c3e9d5a",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Anthropic、先回りしてユーザーを助ける秘書エージェント「Claude Duet」を発表（窓の杜）",
  "snippet": "",
  "published": "2026-10-22T06:00:00+00:00"
 },
 {
  "id": "a5d6f38867c2",
  "region": "jp",
  "source": "TradingView",
  "title": "AI市場の動揺で他社が延期、AnthropicのIPOは唯一",
  "snippet": "",
  "published": "2026-10-22T13:05:44+00:00"
 },
 {
  "id": "765105c3f1c1",
  "region": "jp",
  "source": "Moomoo",
  "title": "Google：Google CloudにおけるClaudeモデルのAnthropic管理型デプロイメントオプションの一般提供開始を発表",
  "snippet": "",
  "published": "2026-10-22T21:56:24+00:00"
 },
 {
  "id": "6432fa90053f",
  "region": "jp",
  "source": "Korben",
  "title": "Claude Duet:あなたが寝ている間も働くAnthropicのエージェント",
  "snippet": "",
  "published": "2026-10-22T13:16:54+00:00"
 },
 {
  "id": "c5d2001dacdc",
  "region": "jp",
  "source": "ASCII.jp",
  "title": "Anthropic「Claude Duet」発表 PCを閉じても仕事を続ける常駐型AIエージェント",
  "snippet": "",
  "published": "2026-10-22T06:11:38+00:00"
 },
 {
  "id": "dd26a1493912",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "OpenAIは、AnthropicのIPOを前に資金調達を加速させている。",
  "snippet": "",
  "published": "2026-10-22T09:28:41+00:00"
 },
 {
  "id": "2b483749a3cc",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic版常時稼働エージェント「Claude Duet」発表 Opus 5.5ベースで設計 Pro／Maxプランで提供（1/2 ページ）",
  "snippet": "",
  "published": "2026-10-22T01:09:23+00:00"
 },
 {
  "id": "f2a2c8796d4f",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Anthropic「Claude Duet」発表 PCを閉じても仕事を続ける常駐型AIエージェント (アスキー)",
  "snippet": "",
  "published": "2026-10-22T06:10:00+00:00"
 },
 {
  "id": "912f210af0c3",
  "region": "jp",
  "source": "ITmedia",
  "title": "本番コードのAI生成率99％ ソニー銀行は「勘定系開発にClaude Code適用」をどう実現？",
  "snippet": "",
  "published": "2026-10-21T23:00:00+00:00"
 },
 {
  "id": "39da2cec9cd7",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "米Anthropic、AIの稼働は人の6倍に 若手採用の割合は27%から9%に下がる（いけとも） - エキスパート",
  "snippet": "",
  "published": "2026-10-22T03:05:19+00:00"
 },
 {
  "id": "7d415a2ade6b",
  "region": "jp",
  "source": "合同会社ロケットボーイズ",
  "title": "Anthropic、機密AI企業Opaque Systemsの技術・人材を獲得―AIエージェントのセキュリティ強化へ",
  "snippet": "",
  "published": "2026-10-22T05:00:13+00:00"
 },
 {
  "id": "9c4e812aa22e",
  "region": "jp",
  "source": "Moomoo",
  "title": "米国のIPO市場が「麻痺」状態に陥る中、Anthropic社に現状打破の期待が高まる",
  "snippet": "",
  "published": "2026-10-22T16:40:17+00:00"
 },
 {
  "id": "21df15201068",
  "region": "jp",
  "source": "Iolite（アイオライト）",
  "title": "Anthropic、上場目論見書を23日にも公開か 11月上場へ最終段階",
  "snippet": "",
  "published": "2026-10-22T05:45:00+00:00"
 },
 {
  "id": "970b759fb12a",
  "region": "jp",
  "source": "Real Sound｜リアルサウンド",
  "title": "AIエージェント競争にアンソロピックが『Claude Duet』で殴り込み OpenAIの提携と買収も【AIニュース3選】",
  "snippet": "",
  "published": "2026-10-22T12:00:25+00:00"
 },
 {
  "id": "7a0d651ebbed",
  "region": "jp",
  "source": "OrcaRouter",
  "title": "Claude Duet vs Claude Code：同じモデル、2つの「完了」の捉え方",
  "snippet": "",
  "published": "2026-10-22T11:12:13+00:00"
 },
 {
  "id": "d25b77f9fe11",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "Anthropic社は、AI危機の中、保有株式の5％を慈善団体に寄付した。",
  "snippet": "",
  "published": "2026-10-22T03:29:36+00:00"
 },
 {
  "id": "4256e57e9050",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic版常時稼働エージェント「Claude Duet」発表 Opus 5.5ベースで設計 Pro／Maxプランで提供（2/2 ページ）",
  "snippet": "",
  "published": "2026-10-22T01:43:38+00:00"
 },
 {
  "id": "8afd5effec62",
  "region": "jp",
  "source": "窓の杜",
  "title": "Anthropic、先回りしてユーザーを助ける秘書エージェント「Claude Duet」を発表",
  "snippet": "",
  "published": "2026-10-22T05:40:00+00:00"
 },
 {
  "id": "d140a15880ab",
  "region": "jp",
  "source": "日経クロステック",
  "title": "Anthropic「物理AI版MCP」を米量子QuEraが実証、エラーの復旧成功率99％（2ページ目）",
  "snippet": "",
  "published": "2026-10-21T20:00:00+00:00"
 },
 {
  "id": "1683ea885ce9",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Railwayの情報漏えい：盗まれたAnthropicとOpenAIのAPIキーがモデル蒸留のブラックマーケットを形成、Theo Browne氏が指摘",
  "snippet": "",
  "published": "2026-10-22T05:08:00+00:00"
 },
 {
  "id": "23886969ff46",
  "region": "intl",
  "source": "Anthropic",
  "title": "LLMs are making formal software verification feasible at a much larger scale",
  "snippet": "",
  "published": "2026-10-22T21:58:06+00:00"
 },
 {
  "id": "520ab7b7f05d",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic IPO stands alone as AI market jitters sideline others",
  "snippet": "",
  "published": "2026-10-22T16:29:48+00:00"
 },
 {
  "id": "b7c1f2900200",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic IPO to Drive Blockbuster Gains for Iconiq, Spark, GIC",
  "snippet": "",
  "published": "2026-10-22T19:34:03+00:00"
 },
 {
  "id": "3464747e27ed",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Claude Duet app is Anthropic’s bet on agents",
  "snippet": "",
  "published": "2026-10-22T13:53:26+00:00"
 },
 {
  "id": "574dbe9d4a3b",
  "region": "intl",
  "source": "Billboard",
  "title": "Reservoir Sues Suno & Anthropic in Latest Lawsuits Over AI Music: ‘Meant to Replace the Artists’",
  "snippet": "",
  "published": "2026-10-22T18:10:53+00:00"
 },
 {
  "id": "41b9c7113438",
  "region": "intl",
  "source": "The Motley Fool",
  "title": "Anthropic IPO: Here's What a $5,000 Investment Could Be Worth in 5 Years",
  "snippet": "",
  "published": "2026-10-22T11:20:00+00:00"
 },
 {
  "id": "47ce16c7608b",
  "region": "intl",
  "source": "Bloomberg Law News",
  "title": "Anthropic’s Ambitions in Legal Technology Get a Reality Check",
  "snippet": "",
  "published": "2026-10-22T09:01:00+00:00"
 },
 {
  "id": "cf32d8eb0557",
  "region": "intl",
  "source": "Barron's",
  "title": "How Anthropic’s Claude Duet Differs From Meta Muse in the AI Agent Race",
  "snippet": "",
  "published": "2026-10-22T17:25:00+00:00"
 },
 {
  "id": "554e3125c8b6",
  "region": "intl",
  "source": "The American Bazaar",
  "title": "Anthropic’s new AI agent Claude Duet can work while users are away",
  "snippet": "",
  "published": "2026-10-22T22:48:43+00:00"
 },
 {
  "id": "089dc7ccd0de",
  "region": "intl",
  "source": "CNET",
  "title": "Anthropic Introduces Claude Duet: A New Agentic AI App for Professionals",
  "snippet": "",
  "published": "2026-10-22T21:19:09+00:00"
 },
 {
  "id": "d412edc07b3a",
  "region": "intl",
  "source": "Google Cloud",
  "title": "Expanding Claude availability and deployment choice on Google Cloud",
  "snippet": "",
  "published": "2026-10-22T21:19:39+00:00"
 },
 {
  "id": "4a7e6e51e261",
  "region": "intl",
  "source": "CNBC",
  "title": "Alex Kantrowitz: Google, Anthropic, OpenAI will be looking for ways to fund the backbone of AI",
  "snippet": "",
  "published": "2026-10-22T19:14:27+00:00"
 },
 {
  "id": "d24c772af648",
  "region": "intl",
  "source": "TechTarget",
  "title": "Anthropic rolls out Claude Duet, but enterprises aren’t ready",
  "snippet": "",
  "published": "2026-10-22T17:38:48+00:00"
 },
 {
  "id": "13459daf06f9",
  "region": "intl",
  "source": "R&D World",
  "title": "Anthropic's Claude Duet joins the race for always-on agents",
  "snippet": "",
  "published": "2026-10-22T20:21:19+00:00"
 },
 {
  "id": "6bf4fb62d782",
  "region": "intl",
  "source": "EdTech Innovation Hub",
  "title": "Anthropic details AI progress and safety gaps in 2026 report | ETIH EdTech News",
  "snippet": "",
  "published": "2026-10-23T00:15:16+00:00"
 },
 {
  "id": "883cd2f36aa4",
  "region": "intl",
  "source": "Anthropic",
  "title": "Open call for guest investigators in the life sciences",
  "snippet": "",
  "published": "2026-10-22T22:03:06+00:00"
 },
 {
  "id": "aed0122f8e43",
  "region": "intl",
  "source": "Bloomberg Law News",
  "title": "Anthropic Sued Over Training Claude AI Model on Protected Music",
  "snippet": "",
  "published": "2026-10-22T17:29:00+00:00"
 },
 {
  "id": "db50b3d62c1a",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic, OpenAI, Musk Pledge Donations Amid AI Backlash",
  "snippet": "",
  "published": "2026-10-22T20:01:25+00:00"
 },
 {
  "id": "2f777a0b6480",
  "region": "intl",
  "source": "Reuters",
  "title": "NEWSLETTER: Why Anthropic is turning away some users",
  "snippet": "",
  "published": "2026-10-22T17:52:55+00:00"
 },
 {
  "id": "bb18d7c237ab",
  "region": "intl",
  "source": "EdTech Innovation Hub",
  "title": "Anthropic unveils Claude Duet, an AI agent for everyday work | ETIH EdTech News",
  "snippet": "",
  "published": "2026-10-22T23:07:35+00:00"
 },
 {
  "id": "b102a10a956f",
  "region": "intl",
  "source": "Business Insider",
  "title": "Anthropic's top engineer reveals just how far her team has gone with AI coding",
  "snippet": "",
  "published": "2026-10-22T09:00:00+00:00"
 },
 {
  "id": "87c300e0d264",
  "region": "intl",
  "source": "Gerben IP",
  "title": "Anthropic’s ‘CLAUDE MYTHOS’ Trademark Application Denied by USPTO",
  "snippet": "",
  "published": "2026-10-22T20:05:46+00:00"
 },
 {
  "id": "46ba6fc6bf52",
  "region": "intl",
  "source": "The Verge",
  "title": "OpenAI, Anthropic, and Nvidia had record lobbying quarters",
  "snippet": "",
  "published": "2026-10-22T15:50:30+00:00"
 },
 {
  "id": "5d4c50d15ee9",
  "region": "intl",
  "source": "CBS News",
  "title": "Anthropic's proposed AI safety bill only allows government to block models under extreme conditions",
  "snippet": "",
  "published": "2026-10-22T21:39:00+00:00"
 },
 {
  "id": "445ddb49d2f8",
  "region": "intl",
  "source": "Seeking Alpha",
  "title": "Anthropic Is The Riskiest IPO Of 2026 (Private:ANTHRO)",
  "snippet": "",
  "published": "2026-10-22T22:32:55+00:00"
 },
 {
  "id": "d0c7c3932d4e",
  "region": "intl",
  "source": "Anthropic",
  "title": "Donating Agent Skills to the Agentic AI Foundation",
  "snippet": "",
  "published": "2026-10-22T18:25:44+00:00"
 },
 {
  "id": "6cbdb4a99f73",
  "region": "intl",
  "source": "Anthropic",
  "title": "2026 Public Benefit Report",
  "snippet": "",
  "published": "2026-10-21T19:18:30+00:00"
 },
 {
  "id": "270931bcc9f5",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Platform is now available on Google Cloud",
  "snippet": "",
  "published": "2026-10-22T21:22:20+00:00"
 },
 {
  "id": "5bb4c470f658",
  "region": "intl",
  "source": "claude.com",
  "title": "Introducing Claude Duet",
  "snippet": "",
  "published": "2026-10-21T19:15:08+00:00"
 },
 {
  "id": "c4eb9c637f8c",
  "region": "intl",
  "source": "claude.com",
  "title": "Building agents: When to fold subagents into your main agent loop",
  "snippet": "",
  "published": "2026-10-22T16:22:28+00:00"
 },
 {
  "id": "8cdc0e0642f5",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "How to use Link by Stripe with Claude Duet",
  "snippet": "",
  "published": "2026-10-21T18:46:03+00:00"
 },
 {
  "id": "ed7dcdab1e53",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Get started with skill and plugin scanning",
  "snippet": "",
  "published": "2026-10-21T21:46:24+00:00"
 },
 {
  "id": "be641fa6b946",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Elimina profilo utente",
  "snippet": "",
  "published": "2026-10-21T17:12:27+00:00"
 },
 {
  "id": "0ae205b0f122",
  "region": "intl",
  "source": "claude.com",
  "title": "HCLTech becomes a Global Premier Partner for Claude",
  "snippet": "",
  "published": "2026-10-21T19:23:33+00:00"
 },
 {
  "id": "7450e817a909",
  "region": "intl",
  "source": "claude.com",
  "title": "Redesigning Claude Code on desktop for parallel agents",
  "snippet": "",
  "published": "2026-10-22T02:23:06+00:00"
 },
 {
  "id": "16ac22315f58",
  "region": "intl",
  "source": "claude.com",
  "title": "How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace",
  "snippet": "",
  "published": "2026-10-21T18:56:15+00:00"
 },
 {
  "id": "889f6951d821",
  "region": "intl",
  "source": "claude.com",
  "title": "Agents and products",
  "snippet": "",
  "published": "2026-10-22T08:27:45+00:00"
 },
 {
  "id": "27e26a3a5827",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Security is now in public beta",
  "snippet": "",
  "published": "2026-10-21T18:31:22+00:00"
 },
 {
  "id": "471f2f29e42e",
  "region": "intl",
  "source": "claude.com",
  "title": "Loop engineering: Getting started with loops",
  "snippet": "",
  "published": "2026-10-22T00:38:09+00:00"
 },
 {
  "id": "24ab87281c81",
  "region": "intl",
  "source": "claude.com",
  "title": "YMCA South Australia Claude case study",
  "snippet": "",
  "published": "2026-10-22T00:41:40+00:00"
 },
 {
  "id": "98bda4a5a7af",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Claude Cowork and chat are one Claude",
  "snippet": "",
  "published": "2026-10-22T20:00:50+00:00"
 },
 {
  "id": "193ef4e1c1d8",
  "region": "intl",
  "source": "claude.com",
  "title": "Ship Code Faster with Claude Code on Vertex AI",
  "snippet": "",
  "published": "2026-10-22T00:21:08+00:00"
 },
 {
  "id": "327f330c4070",
  "region": "intl",
  "source": "claude.com",
  "title": "PwC Claude Code case study",
  "snippet": "",
  "published": "2026-10-21T18:21:06+00:00"
 },
 {
  "id": "a85b4fb986ac",
  "region": "intl",
  "source": "claude.com",
  "title": "Kindora Claude Code case study",
  "snippet": "",
  "published": "2026-10-22T01:42:44+00:00"
 },
 {
  "id": "3634aca7c9f6",
  "region": "intl",
  "source": "claude.com",
  "title": "Mutiny Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-22T03:59:30+00:00"
 },
 {
  "id": "0cfd6aa14051",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Notas de lançamento",
  "snippet": "",
  "published": "2026-10-22T09:09:42+00:00"
 },
 {
  "id": "29ee8635ed74",
  "region": "intl",
  "source": "claude.com",
  "title": "Leadfeeder",
  "snippet": "",
  "published": "2026-10-22T11:36:11+00:00"
 },
 {
  "id": "580de51838a9",
  "region": "intl",
  "source": "claude.com",
  "title": "Yoodli Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-21T18:56:28+00:00"
 },
 {
  "id": "08be190c224b",
  "region": "intl",
  "source": "claude.com",
  "title": "Customer stories",
  "snippet": "",
  "published": "2026-10-22T09:28:47+00:00"
 },
 {
  "id": "096ef5bb63a3",
  "region": "intl",
  "source": "claude.com",
  "title": "Anything Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-22T04:21:54+00:00"
 },
 {
  "id": "d85b259ea5bc",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.309",
  "snippet": "What's changed Fixed sandboxed Bash commands on macOS and Linux running the shell's startup files outside the sandbox before each command Fixed macOS sandbox denyWrite glob patterns not applying at a path's real location when the pattern's folder is reached through a symlink Fixed sandboxed commands and auto-accepted edits being able to modify the MCP config file passed with --mcp-config Fixed a disabled MCP server being reconnected by a later permission prompt in print and SDK sessions Fixed the Bash permission check trusting a variable set by a command whose redirect can fail to open Fixed B…",
  "published": "2026-10-22T22:18:57+00:00"
 },
 {
  "id": "831ab4bfc776",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.308",
  "snippet": "What's changed Bug fixes and reliability improvements",
  "published": "2026-10-22T04:34:55+00:00"
 }
]
