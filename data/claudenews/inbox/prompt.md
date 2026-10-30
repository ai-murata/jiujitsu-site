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
  "id": "18d6767b9ccc",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "AnthropicがAIの訓練のために海賊版書籍を使用していた中にスタンフォード大学教授の書籍も含まれていたと主張して教授らは和解から離脱し訴訟を提起",
  "snippet": "",
  "published": "2026-10-29T10:22:00+00:00"
 },
 {
  "id": "c13e8b04a694",
  "region": "jp",
  "source": "AIsmiley",
  "title": "Claude Codeとは？できること・料金・使い方を徹底解説",
  "snippet": "",
  "published": "2026-10-29T12:24:32+00:00"
 },
 {
  "id": "fade302efc27",
  "region": "jp",
  "source": "キーマンズネット",
  "title": "「このPC、感染してない？」Claude Code、Codexなどに聞ける無料スキル GitHubで公開",
  "snippet": "",
  "published": "2026-10-29T22:00:00+00:00"
 },
 {
  "id": "c77692fb34ac",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "AnthropicはIPOに先立ち、AI機能の強化に数千億ドルを投じる計画だ。",
  "snippet": "",
  "published": "2026-10-30T01:35:46+00:00"
 },
 {
  "id": "b3990633c1d0",
  "region": "jp",
  "source": "www.korit.jp",
  "title": "企業価値2700兆ウォンのAnthropic「サムスン電子・SKハイニックスが半導体を供給しなければAIは止まる」",
  "snippet": "",
  "published": "2026-10-30T00:29:29+00:00"
 },
 {
  "id": "116dd44a6d4f",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicがQ3のSpaceX収益の3分の1超を占める――Bloomberg報道 執筆",
  "snippet": "",
  "published": "2026-10-30T01:14:00+00:00"
 },
 {
  "id": "a14afe8467d6",
  "region": "jp",
  "source": "日本経済新聞",
  "title": "Why you shouldn't bother reading the Anthropic IPO filing",
  "snippet": "",
  "published": "2026-10-29T15:00:00+00:00"
 },
 {
  "id": "e794f861a1fe",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Anthropic、Claudeのスマートレポートを発表 業務外チャットも集計",
  "snippet": "",
  "published": "2026-10-29T17:04:44+00:00"
 },
 {
  "id": "ee844d71d227",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "「大空頭」本人が発砲：Anthropicの目論見書、財務報告が「6月で止まる」、2兆ドル評価に疑義",
  "snippet": "",
  "published": "2026-10-29T20:55:00+00:00"
 },
 {
  "id": "a6138e45ea02",
  "region": "jp",
  "source": "shiritomo",
  "title": "「永久に見つけられない・直せない問題ってあるんですよ」——Claude CodeとCodexを使い分ける”サンドイッチ方式”",
  "snippet": "",
  "published": "2026-10-29T22:35:20+00:00"
 },
 {
  "id": "c0b93c6cef11",
  "region": "jp",
  "source": "Moomoo",
  "title": "アルファベットはAnthropicの株式14%を保有",
  "snippet": "",
  "published": "2026-10-29T16:26:27+00:00"
 },
 {
  "id": "fe6b66208c13",
  "region": "jp",
  "source": "Business Insider Japan",
  "title": "「人間のコーディング作業は、もはや存在しない」…アンソロピック幹部エンジニアが、自身のチームではすべてClaudeが書いていることを明かす",
  "snippet": "",
  "published": "2026-10-29T10:00:00+00:00"
 },
 {
  "id": "cde399ae2acf",
  "region": "jp",
  "source": "AIsmiley",
  "title": "Claude Code Web版の完全ガイド：ブラウザだけで始めるAI自動コーディング",
  "snippet": "",
  "published": "2026-10-29T17:42:27+00:00"
 },
 {
  "id": "f2fdb0579340",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "iPhoneの削除済み写真とClaude Code、400万回表示のバイラル投稿は根拠薄弱と判明",
  "snippet": "",
  "published": "2026-10-29T18:06:45+00:00"
 },
 {
  "id": "c81761d9c581",
  "region": "jp",
  "source": "AIsmiley",
  "title": "【2026年最新】Claude（クロード）のアップデートまとめ！新機能や使い方を解説",
  "snippet": "",
  "published": "2026-10-29T19:35:53+00:00"
 },
 {
  "id": "02f689315140",
  "region": "jp",
  "source": "CNET Japan",
  "title": "「ダウンロード」フォルダに「AI指示書」（.md）を置かないで--CodexやClaude Codeを操る攻撃",
  "snippet": "",
  "published": "2026-10-29T08:45:00+00:00"
 },
 {
  "id": "8b4c014423d3",
  "region": "jp",
  "source": "Business Insider Japan",
  "title": "個人投資家が購入できる、アンソロピック株の規模が見えてきた",
  "snippet": "",
  "published": "2026-10-29T03:50:00+00:00"
 },
 {
  "id": "b1be73a839d8",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Franklin Templeton CEO on SpaceX, Anthropic and the Market｜Sourcery",
  "snippet": "",
  "published": "2026-10-29T18:19:57+00:00"
 },
 {
  "id": "1fc1da561556",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "GitHub、Claude Codeに2点差の「半額」AI投入…「Copilot Fusion」の仕組みとは？（ビジネス＋IT）",
  "snippet": "",
  "published": "2026-10-28T17:30:06+00:00"
 },
 {
  "id": "7ac434a9798d",
  "region": "jp",
  "source": "PR TIMES",
  "title": "【お役立ち資料を無料公開】DAIJOBUが社内で毎日使う「Claude Code 業務効率化アイデア20選」を公開",
  "snippet": "",
  "published": "2026-10-29T23:00:01+00:00"
 },
 {
  "id": "ac66f1dfd605",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "時価総額2,680兆ウォン規模のAnthropic IPO、韓国証券大手8社が相次ぎ不参加…個人の公募申込は事実上不可能に",
  "snippet": "",
  "published": "2026-10-29T08:25:00+00:00"
 },
 {
  "id": "7539fd6abfcf",
  "region": "jp",
  "source": "ニコニコニュース",
  "title": "AIチェックツール「トラスクエタ」に、Anthropic社のAI「Claude」を搭載",
  "snippet": "",
  "published": "2026-10-29T12:00:27+00:00"
 },
 {
  "id": "4cb2f11dd309",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、2兆ドル評価でIPOに挑むも豪州投資責任者「やや無理がある」と直言",
  "snippet": "",
  "published": "2026-10-29T07:56:00+00:00"
 },
 {
  "id": "264017c50255",
  "region": "jp",
  "source": "Reuters",
  "title": "AI Weekly: Anthropic IPO nears, President Trump's ban on AI term",
  "snippet": "",
  "published": "2026-10-29T10:32:06+00:00"
 },
 {
  "id": "689dc29aa4df",
  "region": "jp",
  "source": "remio",
  "title": "Claude Code Utah Pilot：10機関の開発者34人が時間短縮を報告",
  "snippet": "",
  "published": "2026-10-29T03:47:37+00:00"
 },
 {
  "id": "3e9c42624863",
  "region": "intl",
  "source": "Mashable",
  "title": "Claude's new smart reports tell bosses when workers are 'off-topic'",
  "snippet": "",
  "published": "2026-10-30T00:11:48+00:00"
 },
 {
  "id": "0acc559d3226",
  "region": "intl",
  "source": "Understanding AI | Timothy B. Lee",
  "title": "Anthropic’s financials are surprisingly strong",
  "snippet": "",
  "published": "2026-10-29T19:10:41+00:00"
 },
 {
  "id": "e1da055728f2",
  "region": "intl",
  "source": "The Information",
  "title": "Nvidia Moves to Backstop a Cloud Provider’s $45 Billion Anthropic Project",
  "snippet": "",
  "published": "2026-10-29T22:40:00+00:00"
 },
 {
  "id": "935573d2c6d3",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Banks Shelve Bond Sale for Anthropic-Tied Texas Data Center",
  "snippet": "",
  "published": "2026-10-29T13:51:24+00:00"
 },
 {
  "id": "9284c53c5c4f",
  "region": "intl",
  "source": "Forbes",
  "title": "Anthropic Launched A Consulting Arm. 5 Ways The Industry Has To Change",
  "snippet": "",
  "published": "2026-10-29T15:30:00+00:00"
 },
 {
  "id": "9db765453751",
  "region": "intl",
  "source": "Fortune",
  "title": "Anthropic spent $2.75 million guarding Dario Amodei last year—more than 4 times his salary",
  "snippet": "",
  "published": "2026-10-29T08:04:00+00:00"
 },
 {
  "id": "15c42a85d246",
  "region": "intl",
  "source": "NYU Stern Center for Business & Human Rights",
  "title": "Enterprise AI with a Consumer Funnel: What Anthropic’s S-1 Reveals About the AI IPO Era",
  "snippet": "",
  "published": "2026-10-29T21:56:52+00:00"
 },
 {
  "id": "4a0a759c59fd",
  "region": "intl",
  "source": "Dark Reading",
  "title": "Anthropic-Themed Phishing Emails Bypass Top Security Tools",
  "snippet": "",
  "published": "2026-10-29T21:53:25+00:00"
 },
 {
  "id": "ff3d3b393dfa",
  "region": "intl",
  "source": "ETF Database",
  "title": "Anthropic Plans IPO: Direxion Single-Stock ETF to Follow",
  "snippet": "",
  "published": "2026-10-29T21:22:30+00:00"
 },
 {
  "id": "883edec00279",
  "region": "intl",
  "source": "Reuters",
  "title": "Breakingviews - COMMENTARY: Anthropic’s spending is worryingly anthropocentric",
  "snippet": "",
  "published": "2026-10-29T19:10:23+00:00"
 },
 {
  "id": "d0f8e27af932",
  "region": "intl",
  "source": "KQED",
  "title": "Real Estate, Climate and Wild Parties? Here’s How Anthropic’s IPO Could Affect the Bay Area",
  "snippet": "",
  "published": "2026-10-29T18:10:20+00:00"
 },
 {
  "id": "31c06dcf53a7",
  "region": "intl",
  "source": "The Verge",
  "title": "Can Anthropic really become a $10 trillion company?",
  "snippet": "",
  "published": "2026-10-29T14:00:00+00:00"
 },
 {
  "id": "a34ddbb9a1c0",
  "region": "intl",
  "source": "24/7 Wall St.",
  "title": "Claude AI Prices Chainlink, Stellar and Hedera for 2028. Which Gains the Most?",
  "snippet": "",
  "published": "2026-10-30T01:43:18+00:00"
 },
 {
  "id": "8b86ca00c36e",
  "region": "intl",
  "source": "The Motley Fool",
  "title": "Anthropic IPO: How to Buy Shares and What to Expect on Day 1",
  "snippet": "",
  "published": "2026-10-29T23:24:30+00:00"
 },
 {
  "id": "72fd70296c50",
  "region": "intl",
  "source": "CIO Dive",
  "title": "Tech Bytes: Big banks unite to back Anthropic’s compute buildout",
  "snippet": "",
  "published": "2026-10-29T20:34:22+00:00"
 },
 {
  "id": "9172711be2ad",
  "region": "intl",
  "source": "Forbes",
  "title": "Anthropic Bought A One-Person Biotech That Ran A Drug Program With Claude",
  "snippet": "",
  "published": "2026-10-29T14:41:57+00:00"
 },
 {
  "id": "7849b91e20a5",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic’s IPO filing left these key questions unanswered",
  "snippet": "",
  "published": "2026-10-29T09:00:00+00:00"
 },
 {
  "id": "1adf6e98a0b1",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "SpaceX’s Largest Revenue Source Is a Finite Deal With Anthropic",
  "snippet": "",
  "published": "2026-10-29T19:19:12+00:00"
 },
 {
  "id": "010890475e04",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic IPO May Spark AI Rally as Short Bets on Tech Pile Up",
  "snippet": "",
  "published": "2026-10-29T11:52:40+00:00"
 },
 {
  "id": "78352643a438",
  "region": "intl",
  "source": "The Verge",
  "title": "Anthropic’s business plan: Build God or die trying",
  "snippet": "",
  "published": "2026-10-29T13:30:00+00:00"
 },
 {
  "id": "2a64fecfc9ae",
  "region": "intl",
  "source": "Business Insider",
  "title": "VC Insider: Anthropic mints record gains in record time",
  "snippet": "",
  "published": "2026-10-29T18:21:00+00:00"
 },
 {
  "id": "cba6537fb526",
  "region": "intl",
  "source": "New York Post",
  "title": "San Francisco’s luxury dealers are salivating at Anthropic IPO, bracing for ‘tidal wave’ of cash to hit their coffers",
  "snippet": "",
  "published": "2026-10-29T22:10:00+00:00"
 },
 {
  "id": "0bf5ea7e815b",
  "region": "intl",
  "source": "EdTech Innovation Hub",
  "title": "Anthropic AI fluency courses reach 1.1m users | ETIH EdTech News",
  "snippet": "",
  "published": "2026-10-30T00:21:06+00:00"
 },
 {
  "id": "315979bc76d7",
  "region": "intl",
  "source": "Reuters",
  "title": "Breakingviews - COMMENTARY: Artificial intelligence reaches its Napster moment",
  "snippet": "",
  "published": "2026-10-29T22:00:25+00:00"
 },
 {
  "id": "b5ddf4b966d0",
  "region": "intl",
  "source": "Inc.com",
  "title": "The Dark Side of the Anthropic IPO: What Happens After You Become an Overnight Multimillionaire",
  "snippet": "",
  "published": "2026-10-29T08:11:25+00:00"
 },
 {
  "id": "d62612f78ae5",
  "region": "intl",
  "source": "claude.com",
  "title": "IDC brings Quanta into Claude and adopts Claude across the company",
  "snippet": "",
  "published": "2026-10-28T17:11:13+00:00"
 },
 {
  "id": "527315cee87c",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Cyber Verification Program | Claude Help Center",
  "snippet": "",
  "published": "2026-10-29T22:47:41+00:00"
 },
 {
  "id": "0e5eaa74c7c5",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Manage plugins, skills, and connectors from one Plugins page",
  "snippet": "",
  "published": "2026-10-28T15:30:58+00:00"
 },
 {
  "id": "c8e643ca5867",
  "region": "intl",
  "source": "claude.com",
  "title": "Intuit QuickBooks Labs connector",
  "snippet": "",
  "published": "2026-10-30T00:47:07+00:00"
 },
 {
  "id": "2dc900b3c4b3",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for the legal industry",
  "snippet": "",
  "published": "2026-10-28T17:02:21+00:00"
 },
 {
  "id": "9c8b4dba6a40",
  "region": "intl",
  "source": "claude.com",
  "title": "Bringing Salesforce into Claude",
  "snippet": "",
  "published": "2026-10-28T21:22:04+00:00"
 },
 {
  "id": "65aa96ef60ed",
  "region": "intl",
  "source": "claude.com",
  "title": "Bringing Claude Code and Claude Cowork to government",
  "snippet": "",
  "published": "2026-10-29T23:22:11+00:00"
 },
 {
  "id": "0f8d24311558",
  "region": "intl",
  "source": "claude.com",
  "title": "Clio connector",
  "snippet": "",
  "published": "2026-10-29T00:38:03+00:00"
 },
 {
  "id": "63aa8c591539",
  "region": "intl",
  "source": "claude.com",
  "title": "Tomorrow.io Weather MCP App connector",
  "snippet": "",
  "published": "2026-10-29T07:52:04+00:00"
 },
 {
  "id": "a43b256075c8",
  "region": "intl",
  "source": "claude.com",
  "title": "BiggerPockets connector",
  "snippet": "",
  "published": "2026-10-28T22:59:10+00:00"
 },
 {
  "id": "d2d5df1c8418",
  "region": "intl",
  "source": "assets.claude.com",
  "title": "Alignment Risk Update: Claude Mythos Preview (Redacted, April 10)",
  "snippet": "",
  "published": "2026-10-28T23:44:50+00:00"
 },
 {
  "id": "c904939ee4dd",
  "region": "intl",
  "source": "claude.com",
  "title": "Introducing the Claude Platform on AWS",
  "snippet": "",
  "published": "2026-10-29T04:07:16+00:00"
 },
 {
  "id": "b6630622d1ea",
  "region": "intl",
  "source": "claude.com",
  "title": "Build plugins for Claude with the directory submission portal",
  "snippet": "",
  "published": "2026-10-29T07:46:26+00:00"
 },
 {
  "id": "809b7c64ea21",
  "region": "intl",
  "source": "claude.com",
  "title": "Building an AI-native revenue organization",
  "snippet": "",
  "published": "2026-10-28T20:23:32+00:00"
 },
 {
  "id": "0bbed20f3d61",
  "region": "intl",
  "source": "claude.com",
  "title": "EasyPost connector",
  "snippet": "",
  "published": "2026-10-28T15:53:15+00:00"
 },
 {
  "id": "4e3763af26d4",
  "region": "intl",
  "source": "claude.com",
  "title": "Mapbox MCP connector",
  "snippet": "",
  "published": "2026-10-29T17:06:40+00:00"
 },
 {
  "id": "83cf94598e44",
  "region": "intl",
  "source": "claude.com",
  "title": "New analytics and cost controls are available for Claude Enterprise.",
  "snippet": "",
  "published": "2026-10-29T00:42:59+00:00"
 },
 {
  "id": "c87c8fef0086",
  "region": "intl",
  "source": "claude.com",
  "title": "Working at the frontier: How Balyasny Asset Management evaluates and governs Claude Fable 5",
  "snippet": "",
  "published": "2026-10-28T18:42:19+00:00"
 },
 {
  "id": "a453c08066a2",
  "region": "intl",
  "source": "claude.com",
  "title": "The startup lifecycle, rebooted for 2026",
  "snippet": "",
  "published": "2026-10-28T20:45:56+00:00"
 },
 {
  "id": "8a76a7f66375",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Tool use with the Messages API",
  "snippet": "",
  "published": "2026-10-29T18:36:07+00:00"
 },
 {
  "id": "6b4e24c12fa7",
  "region": "intl",
  "source": "claude.com",
  "title": "Smart reports, surveys, and pooled group budgets for Claude Enterprise",
  "snippet": "",
  "published": "2026-10-28T18:22:48+00:00"
 },
 {
  "id": "8b360ec037e9",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Create surveys for your organization | Claude Help Center",
  "snippet": "",
  "published": "2026-10-28T17:49:38+00:00"
 },
 {
  "id": "c035a921a747",
  "region": "intl",
  "source": "partnerhub.claude.com",
  "title": "Directory Optum",
  "snippet": "",
  "published": "2026-10-28T19:50:14+00:00"
 },
 {
  "id": "d44b79b8f250",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Claude for Nonprofits: Data handling and your AI use policy",
  "snippet": "",
  "published": "2026-10-29T00:48:07+00:00"
 },
 {
  "id": "ee24f2da5fdd",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Course quiz · Tool use with the Messages API",
  "snippet": "",
  "published": "2026-10-29T18:55:19+00:00"
 },
 {
  "id": "d820d0beaa38",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.314",
  "snippet": "What's changed Added permissions.blockWritesOutsideWorkingDirectories : Write, Edit and NotebookEdit refuse paths outside the working directories in every permission mode Added an optional groups list to Claude apps gateway upstreams: only developers in the listed IdP groups are sent to that upstream, on failover too Added guardrail_trace to Claude apps gateway Bedrock upstreams, to log which Amazon Bedrock guardrail filter fired on a request, without the matched text Added idle compaction to VS Code and Claude Desktop's Code tab: a 200K+ token conversation left idle is summarized, and the sum…",
  "published": "2026-10-30T01:06:26+00:00"
 }
]
