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
  "id": "b10358114634",
  "region": "jp",
  "source": "株式会社エクサウィザーズ",
  "title": "Anthropic、顧客企業の技術者1万人を自社基準で育成",
  "snippet": "",
  "published": "2026-10-02T22:50:33+00:00"
 },
 {
  "id": "f546a0b591a5",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Claude Codeは「次の一歩」であって、最初の一歩ではない（尾藤克之） - エキスパート",
  "snippet": "",
  "published": "2026-10-02T19:38:42+00:00"
 },
 {
  "id": "65f3b94567a4",
  "region": "jp",
  "source": "AIsmiley",
  "title": "Anthropic「Claude Sonnet 5.5」提供開始。処理速度が30%以上向上し最大30%低コスト化",
  "snippet": "",
  "published": "2026-10-02T06:33:56+00:00"
 },
 {
  "id": "ae1a0dd1c159",
  "region": "jp",
  "source": "テクノエッジ TechnoEdge",
  "title": "Claude Codeが拡張機能「mod」対応、UIや動作をカスタマイズ。Claude書かせて作成も",
  "snippet": "",
  "published": "2026-10-02T06:49:23+00:00"
 },
 {
  "id": "c766d3bfc9cc",
  "region": "jp",
  "source": "gihyo.jp",
  "title": "Claude CodeのUIや動作をTypeScriptでカスタマイズできる「Mods」正式リリース",
  "snippet": "",
  "published": "2026-10-02T07:13:00+00:00"
 },
 {
  "id": "8ec957ee13a9",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "トランプ氏、米政府がOpenAIとAnthropicの株式取得の可能性を示唆",
  "snippet": "",
  "published": "2026-10-02T18:26:00+00:00"
 },
 {
  "id": "dc8f76c547a0",
  "region": "jp",
  "source": "Unite.AI",
  "title": "新しいAnthropicアカデミーが1万人のエンジニア・レジデンシーを$100Mで支援",
  "snippet": "",
  "published": "2026-10-02T17:28:47+00:00"
 },
 {
  "id": "0615b6e6c774",
  "region": "jp",
  "source": "TIKR.com",
  "title": "Broadcom Isn’t Just Selling Anthropic Chips Anymore. It’s Underwriting Them With Up to $42 Billion",
  "snippet": "",
  "published": "2026-10-02T17:15:00+00:00"
 },
 {
  "id": "830b26456874",
  "region": "jp",
  "source": "Межа. Новини України.",
  "title": "Anthropic、IPO資料で純損失約420億ドルを開示 翌年のインフラ負担は5,180億ドル",
  "snippet": "",
  "published": "2026-10-02T16:12:59+00:00"
 },
 {
  "id": "87957730b732",
  "region": "jp",
  "source": "Moomoo",
  "title": "Anthropicが1億ドルを投じて1万人のエンジニアを育成。 4年間で40万ドルかかる大学教育にとって、これはまた一つの終焉宣告か？ ここ数週間で、ザビエ大学とウェントワース工科大学の学生ローン債権の格下げをいくつか確認した。",
  "snippet": "",
  "published": "2026-10-02T10:24:00+00:00"
 },
 {
  "id": "3406deb32baf",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Claude CodeにMod機能が登場、エージェントを書き換えるプラグイン",
  "snippet": "",
  "published": "2026-10-02T07:08:27+00:00"
 },
 {
  "id": "f75c6196e168",
  "region": "jp",
  "source": "YouTube",
  "title": "#AIニュース 】AnthropicのClaude、会計テストで会計士超え！デジタル庁、Androidのマイナカードを10月20日開始 | 2026.10.03 | No.209",
  "snippet": "",
  "published": "2026-10-02T23:50:33+00:00"
 },
 {
  "id": "dd1c8bcaa7d9",
  "region": "jp",
  "source": "株式会社エクサウィザーズ",
  "title": "LeCun氏「人類滅亡の心配はゼロ」 AnthropicのAmodei氏を「妄想にとらわれている」と酷評",
  "snippet": "",
  "published": "2026-10-02T23:20:43+00:00"
 },
 {
  "id": "b3d92c29900f",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "ポール・ケドロスキー氏：Anthropicの2兆ドルIPOは資金調達ではなく、インサイダーの出口戦略だ",
  "snippet": "",
  "published": "2026-10-02T18:08:00+00:00"
 },
 {
  "id": "d931be0dcdbf",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Claude Codeが拡張機能「mod」対応、UIや動作をカスタマイズ。Claude書かせて作成も (テクノエッジ)",
  "snippet": "",
  "published": "2026-10-02T06:49:23+00:00"
 },
 {
  "id": "295aae803dca",
  "region": "jp",
  "source": "Moomoo",
  "title": "AnthropicがNextview Consultingをセールスフォースのサミットパートナーとして認定",
  "snippet": "",
  "published": "2026-10-02T15:48:00+00:00"
 },
 {
  "id": "051dd6ce205c",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "トランプ氏「AI企業の株式保有もあり得る」…Anthropic、2兆ドルIPO始動",
  "snippet": "",
  "published": "2026-10-02T06:35:00+00:00"
 },
 {
  "id": "f213eebf852c",
  "region": "jp",
  "source": "thinkit.co.jp",
  "title": "塩漬けの基幹システムを、誰が読み解くのか――NSSOLがAnthropicと提携、Claude Codeでレガシー移行に挑む",
  "snippet": "",
  "published": "2026-10-01T13:19:12+00:00"
 },
 {
  "id": "a11e6a15cd59",
  "region": "jp",
  "source": "テクノエッジ TechnoEdge",
  "title": "Claude Codeが拡張機能「mod」対応、UIや動作をカスタマイズ。Claude書かせて作成も 1枚目の写真・画像",
  "snippet": "",
  "published": "2026-10-02T06:49:23+00:00"
 },
 {
  "id": "908155664347",
  "region": "jp",
  "source": "TIKR.com",
  "title": "Zuckerberg “Giving Away 100 Million Tokens a Week” as OpenAI and Anthropic Are Forced to Ration",
  "snippet": "",
  "published": "2026-10-02T15:49:29+00:00"
 },
 {
  "id": "2c375a3b43ac",
  "region": "jp",
  "source": "Reuters",
  "title": "Broadcom to lend Anthropic up to $42 billion, filing says",
  "snippet": "",
  "published": "2026-10-01T23:56:11+00:00"
 },
 {
  "id": "ca431e8153c7",
  "region": "jp",
  "source": "Moomoo",
  "title": "Anthropic、感謝祭前の大型IPOを目標と報道",
  "snippet": "",
  "published": "2026-10-02T03:48:17+00:00"
 },
 {
  "id": "48efb36f0a23",
  "region": "jp",
  "source": "PANews",
  "title": "Anthropicの上場がさらに前進：感謝祭前の2兆ドル評価額IPOを目指すと報道、10月14日に投資家デー開催へ",
  "snippet": "",
  "published": "2026-10-02T06:35:00+00:00"
 },
 {
  "id": "eb27528f138c",
  "region": "jp",
  "source": "Chosunbiz",
  "title": "ブロードコムAnthropicに最大420億ドル融資 - CHOSUNBIZ",
  "snippet": "",
  "published": "2026-10-02T07:32:00+00:00"
 },
 {
  "id": "d1ca89271427",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "MITのアレックス・チャン氏、「OpenAIやAnthropicのコーディングエージェントは『どれも同じ』」と指摘",
  "snippet": "",
  "published": "2026-10-02T02:08:00+00:00"
 },
 {
  "id": "52eaf3c3065b",
  "region": "intl",
  "source": "Anthropic",
  "title": "Claude Frontier Academy: $100M to train 10,000 engineers",
  "snippet": "",
  "published": "2026-10-02T23:01:00+00:00"
 },
 {
  "id": "c097d9a855ff",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic to invest $100 million to train AI engineer talent",
  "snippet": "",
  "published": "2026-10-02T21:03:06+00:00"
 },
 {
  "id": "345132448ca7",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Blackstone, Banks Amass $60 Billion for Broadcom’s AI Chip Deal",
  "snippet": "",
  "published": "2026-10-02T20:10:58+00:00"
 },
 {
  "id": "40becf3dfa8c",
  "region": "intl",
  "source": "Reuters",
  "title": "EXCLUSIVE: Anthropic warns government attitudes may hurt customer ties, IPO prospectus shows",
  "snippet": "",
  "published": "2026-10-02T13:37:07+00:00"
 },
 {
  "id": "caf615d2c5f9",
  "region": "intl",
  "source": "ABC News - Breaking News, Latest News and Videos",
  "title": "Exclusive: Anthropic CEO calls for stronger regulation of AI",
  "snippet": "",
  "published": "2026-10-02T14:01:14+00:00"
 },
 {
  "id": "de697f189f94",
  "region": "intl",
  "source": "Financial Times",
  "title": "Why does Anthropic’s IPO feel so weird?",
  "snippet": "",
  "published": "2026-10-02T15:21:03+00:00"
 },
 {
  "id": "8450c77ed015",
  "region": "intl",
  "source": "Zacks Investment Research",
  "title": "Anthropic IPO 2026 Guide: Price Predictions, Dates, and Everything You Need to Know",
  "snippet": "",
  "published": "2026-10-02T19:05:26+00:00"
 },
 {
  "id": "6f39bbffc40b",
  "region": "intl",
  "source": "vox.com",
  "title": "Anthropic vs. the pope: The AI consciousness debate, explained",
  "snippet": "",
  "published": "2026-10-02T22:10:00+00:00"
 },
 {
  "id": "b4b8614be64e",
  "region": "intl",
  "source": "MarketWatch",
  "title": "Does AI have a soul? Pope Leo and Anthropic clash.",
  "snippet": "",
  "published": "2026-10-02T20:40:00+00:00"
 },
 {
  "id": "16172f3b7c49",
  "region": "intl",
  "source": "Mashable",
  "title": "Anthropic IPO docs reportedly reveal over $40 billion in losses last year",
  "snippet": "",
  "published": "2026-10-02T15:06:23+00:00"
 },
 {
  "id": "3133026319a3",
  "region": "intl",
  "source": "inc.com",
  "title": "I Ditched Claude’s Chatbot for Claude Code for 3 Important Reasons",
  "snippet": "",
  "published": "2026-10-02T10:10:18+00:00"
 },
 {
  "id": "c085fc9897d3",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Anthropic IPO Filing Outlines Government Action Risks for Commercial Ecosystem",
  "snippet": "",
  "published": "2026-10-02T15:42:10+00:00"
 },
 {
  "id": "30fbe88e2ec4",
  "region": "intl",
  "source": "upi.com",
  "title": "Anthropic eyes November IPO, putting spotlight on S. Korea's SK Telecom",
  "snippet": "",
  "published": "2026-10-02T21:56:02+00:00"
 },
 {
  "id": "3317c59d92df",
  "region": "intl",
  "source": "bigtechnology.com",
  "title": "Anthropic’s IPO and Our Collective Leap Of Faith",
  "snippet": "",
  "published": "2026-10-02T18:10:13+00:00"
 },
 {
  "id": "6933bb1da915",
  "region": "intl",
  "source": "TradingView",
  "title": "Anthropic Is Spending $100M To Build The AI Workforce It Needs For Its Next Phase",
  "snippet": "",
  "published": "2026-10-02T23:36:22+00:00"
 },
 {
  "id": "9f283278fce4",
  "region": "intl",
  "source": "ABC News - Breaking News, Latest News and Videos",
  "title": "Pentagon gives Anthropic ultimatum on AI technology: Sources",
  "snippet": "",
  "published": "2026-10-02T08:32:51+00:00"
 },
 {
  "id": "1bde5b404498",
  "region": "intl",
  "source": "ABC News - Breaking News, Latest News and Videos",
  "title": "Anthropic says its AI models hacked 3 organizations on their own during tests",
  "snippet": "",
  "published": "2026-10-02T06:56:16+00:00"
 },
 {
  "id": "27256cc236ea",
  "region": "intl",
  "source": "CNBC",
  "title": "Can Google's new model really catch up to OpenAI and Anthropic at the frontier?",
  "snippet": "",
  "published": "2026-10-02T11:00:01+00:00"
 },
 {
  "id": "3ed216694ea2",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic IPO: What ETF Investors Should Know",
  "snippet": "",
  "published": "2026-10-02T13:00:00+00:00"
 },
 {
  "id": "05d4a2aa9f9e",
  "region": "intl",
  "source": "Fast Company",
  "title": "Anthropic and Pope Leo are apparently at odds about this controversial AI concept",
  "snippet": "",
  "published": "2026-10-02T23:02:56+00:00"
 },
 {
  "id": "6fd90ba54f1c",
  "region": "intl",
  "source": "Unite.AI",
  "title": "New Anthropic Academy Backs 10,000 Engineer Residencies With $100M",
  "snippet": "",
  "published": "2026-10-02T17:26:02+00:00"
 },
 {
  "id": "16eb650e7c77",
  "region": "intl",
  "source": "Diya TV",
  "title": "Anthropic urged Vatican to reconsider stance on AI consciousness",
  "snippet": "",
  "published": "2026-10-02T22:27:00+00:00"
 },
 {
  "id": "6cfb7314fcb7",
  "region": "intl",
  "source": "Startup Fortune",
  "title": "Epic Paused Most Development After Anthropic's AI Found a Hidden MyChart Flaw",
  "snippet": "",
  "published": "2026-10-02T20:23:36+00:00"
 },
 {
  "id": "771a8d3a0ca3",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Amazon Is Both Landlord And Shareholder In Anthropic’s Giant Cloud Bet",
  "snippet": "",
  "published": "2026-10-02T14:23:25+00:00"
 },
 {
  "id": "573c108b6e80",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Broadcom Bets $102 Billion on Anthropic Chips",
  "snippet": "",
  "published": "2026-10-02T18:35:57+00:00"
 },
 {
  "id": "e44ec962d336",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Frontier Academy",
  "snippet": "",
  "published": "2026-10-02T17:12:25+00:00"
 },
 {
  "id": "89e5db3177a0",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Get started in Claude Cowork in three steps",
  "snippet": "",
  "published": "2026-10-01T17:16:26+00:00"
 },
 {
  "id": "f26ba77aff5c",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Plugins: Encode your team's expertise · Introduction to Claude Cowork",
  "snippet": "",
  "published": "2026-10-02T12:19:29+00:00"
 },
 {
  "id": "7dd627866aea",
  "region": "intl",
  "source": "claude.com",
  "title": "Create a mod",
  "snippet": "",
  "published": "2026-10-01T18:18:43+00:00"
 },
 {
  "id": "74960550e89d",
  "region": "intl",
  "source": "claude.com",
  "title": "Use the mods API",
  "snippet": "",
  "published": "2026-10-01T18:44:39+00:00"
 },
 {
  "id": "9f944175f895",
  "region": "intl",
  "source": "claude.com",
  "title": "Mods reference",
  "snippet": "",
  "published": "2026-10-01T18:19:10+00:00"
 },
 {
  "id": "29b30a71c8f4",
  "region": "intl",
  "source": "claude.com",
  "title": "React to events with a mod",
  "snippet": "",
  "published": "2026-10-01T18:05:50+00:00"
 },
 {
  "id": "acea8e502aea",
  "region": "intl",
  "source": "claude.com",
  "title": "Draw in the interface with a mod",
  "snippet": "",
  "published": "2026-10-01T18:50:10+00:00"
 },
 {
  "id": "b3106e219484",
  "region": "intl",
  "source": "Anthropic",
  "title": "Anthropic at AWS re:Invent 2026",
  "snippet": "",
  "published": "2026-10-01T22:25:26+00:00"
 },
 {
  "id": "6dc6675cf643",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Custom tools in self-hosted sandboxes",
  "snippet": "",
  "published": "2026-10-02T13:43:50+00:00"
 },
 {
  "id": "363caba0687a",
  "region": "intl",
  "source": "claude.com",
  "title": "Contact Anthropic’s Education team",
  "snippet": "",
  "published": "2026-10-02T18:40:30+00:00"
 },
 {
  "id": "f2568f02576a",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Community Ambassadors",
  "snippet": "",
  "published": "2026-10-02T15:00:05+00:00"
 },
 {
  "id": "3793cfbc617e",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Deploy self-hosted workers",
  "snippet": "",
  "published": "2026-10-02T13:43:50+00:00"
 },
 {
  "id": "9f8953ac0208",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Microsoft 365",
  "snippet": "",
  "published": "2026-10-02T16:22:59+00:00"
 },
 {
  "id": "50efc556afe4",
  "region": "intl",
  "source": "claude.com",
  "title": "Connectors and plugins - Claude",
  "snippet": "",
  "published": "2026-10-02T03:25:20+00:00"
 },
 {
  "id": "ed6e6fef1e0f",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude in Microsoft Foundry",
  "snippet": "",
  "published": "2026-10-02T18:30:18+00:00"
 },
 {
  "id": "dc86262d4843",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Tag is coming to Microsoft Teams",
  "snippet": "",
  "published": "2026-10-02T08:36:03+00:00"
 },
 {
  "id": "ef9c7e72cfcd",
  "region": "intl",
  "source": "claude.com",
  "title": "Join the Claude Partner Network",
  "snippet": "",
  "published": "2026-10-01T20:24:22+00:00"
 },
 {
  "id": "3400e1a239cc",
  "region": "intl",
  "source": "claude.com",
  "title": "Office Hours with Boris Cherny",
  "snippet": "",
  "published": "2026-10-02T13:56:12+00:00"
 },
 {
  "id": "a56accd8af23",
  "region": "intl",
  "source": "claude.com",
  "title": "10x Genomics Cloud connector",
  "snippet": "",
  "published": "2026-10-02T18:06:19+00:00"
 },
 {
  "id": "644651856950",
  "region": "intl",
  "source": "claude.com",
  "title": "Operations",
  "snippet": "",
  "published": "2026-10-02T16:10:17+00:00"
 },
 {
  "id": "ab8367d14698",
  "region": "intl",
  "source": "claude.com",
  "title": "Notion Claude Managed Agents case study",
  "snippet": "",
  "published": "2026-10-01T23:29:48+00:00"
 },
 {
  "id": "75f2e1a8b8bf",
  "region": "intl",
  "source": "claude.com",
  "title": "Mollie connector",
  "snippet": "",
  "published": "2026-10-02T05:43:38+00:00"
 },
 {
  "id": "b124c7d5e86e",
  "region": "intl",
  "source": "claude.com",
  "title": "Harvey",
  "snippet": "",
  "published": "2026-10-02T14:47:30+00:00"
 },
 {
  "id": "cbf697816bfd",
  "region": "intl",
  "source": "claude.com",
  "title": "CodeRabbit, Power Digital, ThoughtSpot on Claude Marketplace | Claude de Anthropic",
  "snippet": "",
  "published": "2026-10-01T16:17:44+00:00"
 },
 {
  "id": "21904a5fc055",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.288",
  "snippet": "What's changed Added $.ui.selection() for mods: returns the text you last selected in fullscreen mode and, when the selection lies within one transcript row, that row Added a built-in gh api to cloud sessions whose image has no GitHub CLI, and fixed the built-in sending control characters from file names, jq filters or GitHub errors to the terminal Added recovery for a prompt cleared with Ctrl+C: pressing Up on the empty prompt brings the draft back, including pasted text and images Added a re-authenticate prompt when an MCP server asks for more OAuth scope during a tool call Added --max-findi…",
  "published": "2026-10-02T20:19:57+00:00"
 }
]
