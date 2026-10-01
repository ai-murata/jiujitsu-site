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
  "id": "54eaeaebb828",
  "region": "jp",
  "source": "日経クロステック（xTECH）",
  "title": "Claude Codeの「ごまかし」に直面 マネージド版と併用で乗り切る",
  "snippet": "",
  "published": "2026-09-30T22:02:00+00:00"
 },
 {
  "id": "45e05fc1291d",
  "region": "jp",
  "source": "newspicks.com",
  "title": "あなたのClaude Codeが微妙なのは、プロンプトのせいじゃない",
  "snippet": "",
  "published": "2026-09-30T21:30:13+00:00"
 },
 {
  "id": "ae82d35789ca",
  "region": "jp",
  "source": "株式会社エクサウィザーズ",
  "title": "Google、次世代「Gemini 4 Argon」を発表 OpenAI・Anthropicとの最先端モデル競争が再加速",
  "snippet": "",
  "published": "2026-09-30T22:28:35+00:00"
 },
 {
  "id": "3aa14c5cf3f6",
  "region": "jp",
  "source": "PC Watch",
  "title": "Mythos並みのサイバー攻撃能力を持つGLM-5.3にAnthropicが警鐘",
  "snippet": "",
  "published": "2026-09-30T05:46:31+00:00"
 },
 {
  "id": "576fbf9996b0",
  "region": "jp",
  "source": "株式会社マネーフォワード",
  "title": "「経理AI Forward – AIとともに経理をもっと前へ。 – 」に Anthropic Japan 合同会社 菅野 信 氏の登壇が決定",
  "snippet": "",
  "published": "2026-09-30T06:04:31+00:00"
 },
 {
  "id": "58a0b5cf15d6",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claude for Government をエージェンシー向けに一般提供",
  "snippet": "",
  "published": "2026-09-30T17:58:05+00:00"
 },
 {
  "id": "10b2640018ed",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "米コングがAIエージェント基盤「Volcano」、DBや認証を一体化 Claude Codeから本番へ（ビジネス＋IT）",
  "snippet": "",
  "published": "2026-09-30T21:06:50+00:00"
 },
 {
  "id": "dd57ff7b1650",
  "region": "jp",
  "source": "Gizmodo",
  "title": "Anthropic、驚異的なハイペースで日常使いに最適な新モデルを発表",
  "snippet": "",
  "published": "2026-10-01T01:00:00+00:00"
 },
 {
  "id": "7959873e18be",
  "region": "jp",
  "source": "sbbit.jp",
  "title": "米Anthropic「AIによる人類滅亡のリスク」投資家に向けIPO目論見書に記載",
  "snippet": "",
  "published": "2026-09-30T09:04:00+00:00"
 },
 {
  "id": "111560f1b1c2",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Anthropicが「AIに何を求めるか」調査を再開、インタビューは公開も選べる",
  "snippet": "",
  "published": "2026-09-30T20:16:19+00:00"
 },
 {
  "id": "922da09f4bac",
  "region": "jp",
  "source": "Межа. Новини України.",
  "title": "Anthropic、史上最大級の株式上場を目指す一方で人工知能の危険性を警告",
  "snippet": "",
  "published": "2026-09-30T21:38:04+00:00"
 },
 {
  "id": "f33640998060",
  "region": "jp",
  "source": "tradingview.com",
  "title": "AnthropicのIPOプレゼンテーションは、AIの将来性とリスクの両面に焦点を当てている",
  "snippet": "",
  "published": "2026-09-30T19:52:08+00:00"
 },
 {
  "id": "ab2ec600c2be",
  "region": "jp",
  "source": "about.gitlab.com",
  "title": "GitLabとClaude Code でスピードとコンプライアンスを両立する",
  "snippet": "",
  "published": "2026-09-30T03:26:53+00:00"
 },
 {
  "id": "711f26619bfd",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "Anthropic社は、AIによる深刻なリスクについて警告を発している。",
  "snippet": "",
  "published": "2026-09-30T13:12:14+00:00"
 },
 {
  "id": "8b267cd4ef48",
  "region": "jp",
  "source": "Moomoo",
  "title": "GraniteSharesの2倍レバレッジ・Anthropic ETF（AILおよびANS）",
  "snippet": "",
  "published": "2026-09-30T14:18:17+00:00"
 },
 {
  "id": "b38f1ad1cf62",
  "region": "jp",
  "source": "ITmedia",
  "title": "「Claude Code」の真価は併用にあり 4つのインターフェース使い分けとハイブリッド運用",
  "snippet": "",
  "published": "2026-09-29T20:00:00+00:00"
 },
 {
  "id": "980e13502031",
  "region": "jp",
  "source": "日経クロステック（xTECH）",
  "title": "生成AI＋「手足」＝AIエージェント 1年半前のClaude Code登場でブレーク",
  "snippet": "",
  "published": "2026-09-30T22:00:00+00:00"
 },
 {
  "id": "9230c8aef558",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "「人類存続に関わるリスク」AI開発企業Anthropicが自ら“警鐘” OpenAIは新モデル「GPT6.1アストラ」の公開中止【news23】",
  "snippet": "",
  "published": "2026-09-30T03:25:23+00:00"
 },
 {
  "id": "82c87aca2c32",
  "region": "jp",
  "source": "Межа. Новини України.",
  "title": "米連邦取引委員会がAnthropicやOpenAIを調査、AIエージェントの消費者リスクを検証",
  "snippet": "",
  "published": "2026-09-30T15:27:38+00:00"
 },
 {
  "id": "46d2755b4324",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "中国発AI「GLM-5.3」、Claude最上位モデルに迫る攻撃能力 Anthropicが警告",
  "snippet": "",
  "published": "2026-09-30T08:07:04+00:00"
 },
 {
  "id": "a61d5b01c87c",
  "region": "jp",
  "source": "sbbit.jp",
  "title": "【2026年最新】Claude Code勢に迫る？ 激変したCopilot、仕事が回る“7つ”の新機能",
  "snippet": "",
  "published": "2026-09-29T22:10:00+00:00"
 },
 {
  "id": "4c2aa23532d8",
  "region": "jp",
  "source": "디지털투데이",
  "title": "Anthropic、上場関連の投資説明書でAIエージェントの法的リスクに言及",
  "snippet": "",
  "published": "2026-09-30T22:57:04+00:00"
 },
 {
  "id": "a2862efac3af",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "米Anthropic「AIによる人類滅亡のリスク」投資家に向けIPO目論見書に記載 (ビジネス＋IT)",
  "snippet": "",
  "published": "2026-09-30T09:15:06+00:00"
 },
 {
  "id": "8a6afe5bc9cb",
  "region": "jp",
  "source": "yellow.com",
  "title": "グーグル、次世代モデル「Gemini 4 Argon」を発表 OpenAI・Anthropicをベンチマークで上回ったと主張",
  "snippet": "",
  "published": "2026-09-30T21:49:17+00:00"
 },
 {
  "id": "24891458d89d",
  "region": "jp",
  "source": "ASCII.jp",
  "title": "「誰でも入手できるAI」がサイバー攻撃を自律構築 Anthropicが「GLM-5.3」に警鐘",
  "snippet": "",
  "published": "2026-09-30T05:55:00+00:00"
 },
 {
  "id": "970ebef21f7c",
  "region": "intl",
  "source": "Reuters",
  "title": "FTC opens probe into AI giants including Anthropic and OpenAI",
  "snippet": "",
  "published": "2026-09-30T18:17:19+00:00"
 },
 {
  "id": "b96a6df26dab",
  "region": "intl",
  "source": "The New York Times",
  "title": "F.T.C. Investigates OpenAI and Anthropic Over Potential Consumer Harms",
  "snippet": "",
  "published": "2026-09-30T19:26:02+00:00"
 },
 {
  "id": "ef85ddc463d7",
  "region": "intl",
  "source": "finance.yahoo.com",
  "title": "Anthropic’s $11.6 Billion Quarter Just Changed How the Market Should Read the S-1",
  "snippet": "",
  "published": "2026-09-30T19:44:12+00:00"
 },
 {
  "id": "3682d0f6ba4d",
  "region": "intl",
  "source": "CNBC",
  "title": "Kalshi traders see high odds Anthropic's IPO is announced this year",
  "snippet": "",
  "published": "2026-09-30T17:19:57+00:00"
 },
 {
  "id": "48ea1735c49a",
  "region": "intl",
  "source": "The Guardian",
  "title": "US trade regulator opens investigation into AI giants including Anthropic and OpenAI",
  "snippet": "",
  "published": "2026-09-30T18:35:00+00:00"
 },
 {
  "id": "bdfa0be116df",
  "region": "intl",
  "source": "cbsnews.com",
  "title": "FTC investigating Anthropic, OpenAI and other companies over potential AI risks",
  "snippet": "",
  "published": "2026-09-30T15:07:00+00:00"
 },
 {
  "id": "e79fbf6b1deb",
  "region": "intl",
  "source": "Forbes",
  "title": "Google And Amazon Are The Reason For Anthropic’s Eye-Watering $42 Billion Loss",
  "snippet": "",
  "published": "2026-09-30T14:02:58+00:00"
 },
 {
  "id": "0ce56d65cae0",
  "region": "intl",
  "source": "WSJ",
  "title": "FTC Opens Investigation of Anthropic and OpenAI",
  "snippet": "",
  "published": "2026-09-30T17:29:00+00:00"
 },
 {
  "id": "be696999f061",
  "region": "intl",
  "source": "washingtonpost.com",
  "title": "FTC launches broad investigation into Anthropic, OpenAI",
  "snippet": "",
  "published": "2026-10-01T00:26:52+00:00"
 },
 {
  "id": "c6cda4af3133",
  "region": "intl",
  "source": "New York Post",
  "title": "Exclusive | FTC opens sweeping probe of Anthropic, OpenAI and other 'super intelligence' models",
  "snippet": "",
  "published": "2026-09-30T13:26:00+00:00"
 },
 {
  "id": "4c71ce6f4954",
  "region": "intl",
  "source": "ABC News - Breaking News, Latest News and Videos",
  "title": "FTC opens probe into safety of AI, including Anthropic and OpenAI",
  "snippet": "",
  "published": "2026-09-30T20:41:49+00:00"
 },
 {
  "id": "269daccde8a0",
  "region": "intl",
  "source": "Anthropic",
  "title": "Can we predict the jobs robots will do?",
  "snippet": "",
  "published": "2026-09-30T16:01:00+00:00"
 },
 {
  "id": "a10a15490ccd",
  "region": "intl",
  "source": "Axios",
  "title": "AI safety fears put OpenAI and Anthropic in the FTC's crosshairs",
  "snippet": "",
  "published": "2026-09-30T21:40:34+00:00"
 },
 {
  "id": "73e9ff9c9771",
  "region": "intl",
  "source": "Tom's Hardware",
  "title": "Anthropic claims popular Chinese AI model has Mythos-class hacking abilities",
  "snippet": "",
  "published": "2026-09-30T14:40:00+00:00"
 },
 {
  "id": "03b7da140a53",
  "region": "intl",
  "source": "CNBC",
  "title": "FTC is investigating OpenAI, Anthropic and other AI companies over product risks",
  "snippet": "",
  "published": "2026-09-30T15:27:47+00:00"
 },
 {
  "id": "743b4e14f5b9",
  "region": "intl",
  "source": "finance.yahoo.com",
  "title": "Billionaire Bill Ackman calls Anthropic “perhaps the greatest business story I've ever seen”",
  "snippet": "",
  "published": "2026-09-30T18:37:46+00:00"
 },
 {
  "id": "823b7c1b4fbe",
  "region": "intl",
  "source": "Reuters",
  "title": "EXCLUSIVE: Anthropic's IPO pitch embraces AI's promise and peril",
  "snippet": "",
  "published": "2026-09-30T19:52:00+00:00"
 },
 {
  "id": "85348af57714",
  "region": "intl",
  "source": "finance.yahoo.com",
  "title": "Anthropic IPO documents show there really is only one risk with AI",
  "snippet": "",
  "published": "2026-09-30T10:00:00+00:00"
 },
 {
  "id": "a98cfc6e0969",
  "region": "intl",
  "source": "Reuters",
  "title": "EXCLUSIVE: Anthropic's IPO prospectus shows sweeping AI vision, surging costs",
  "snippet": "",
  "published": "2026-09-30T01:16:47+00:00"
 },
 {
  "id": "79a02878e66d",
  "region": "intl",
  "source": "finance.yahoo.com",
  "title": "FTC reportedly looking into whether OpenAI, Anthropic violated consumer protection laws.",
  "snippet": "",
  "published": "2026-09-30T18:58:20+00:00"
 },
 {
  "id": "a91fa04d0d77",
  "region": "intl",
  "source": "XDA",
  "title": "I compared my Claude Code workflow to a beginner's, and some of my habits were making things worse",
  "snippet": "",
  "published": "2026-09-30T20:00:20+00:00"
 },
 {
  "id": "2c9bf6538024",
  "region": "intl",
  "source": "latimes.com",
  "title": "Anthropic says its AI models could manipulate, blackmail and harm humans",
  "snippet": "",
  "published": "2026-09-30T18:15:00+00:00"
 },
 {
  "id": "d3acd7e7b00f",
  "region": "intl",
  "source": "Reuters",
  "title": "NEWSLETTER: Inside Anthropic’s confidential S-1: a Q&A",
  "snippet": "",
  "published": "2026-09-30T22:25:09+00:00"
 },
 {
  "id": "65739aca37bf",
  "region": "intl",
  "source": "The Motley Fool",
  "title": "Anthropic Plans to Spend $518 Billion on Cloud and Data Centers. More Than $100 Billion Is Already Promised to Amazon.",
  "snippet": "",
  "published": "2026-10-01T00:43:28+00:00"
 },
 {
  "id": "f4a5583f763f",
  "region": "intl",
  "source": "New York Post",
  "title": "Anthropic co-founder Daniela Amodei and husband used stuffed-animal 'advisory council' for workplace conflicts: report",
  "snippet": "",
  "published": "2026-09-30T15:05:00+00:00"
 },
 {
  "id": "6bec62ce7919",
  "region": "intl",
  "source": "Anthropic",
  "title": "What do you want from AI?",
  "snippet": "",
  "published": "2026-09-29T16:39:00+00:00"
 },
 {
  "id": "eb144befd6f5",
  "region": "intl",
  "source": "Anthropic",
  "title": "GLM-5.3 and the spread of advanced cyber capabilities",
  "snippet": "",
  "published": "2026-09-29T15:46:00+00:00"
 },
 {
  "id": "6093cfce68e8",
  "region": "intl",
  "source": "Anthropic",
  "title": "Building with the Claude 5.5 Family: Choosing the Right Model and Getting More from Every Token",
  "snippet": "",
  "published": "2026-09-30T00:02:28+00:00"
 },
 {
  "id": "bd6e02d9333e",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Prompting Claude Sonnet 5.5",
  "snippet": "",
  "published": "2026-10-01T00:59:50+00:00"
 },
 {
  "id": "3141cb4fdf43",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Government is now generally available",
  "snippet": "",
  "published": "2026-09-30T17:34:15+00:00"
 },
 {
  "id": "d30ca3f5cca3",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Migrating to Claude Sonnet 5.5",
  "snippet": "",
  "published": "2026-10-01T00:50:30+00:00"
 },
 {
  "id": "cdbfeef20de6",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Get started with Claude Compliance API integrations | Claude Help Center",
  "snippet": "",
  "published": "2026-09-29T18:19:05+00:00"
 },
 {
  "id": "67c8d3272330",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Use Claude Cowork on web, desktop, and mobile | Claude Help Center",
  "snippet": "",
  "published": "2026-09-30T22:06:02+00:00"
 },
 {
  "id": "2788fc37f9b5",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Schedule recurring tasks in Claude Cowork | Claude Help Center",
  "snippet": "",
  "published": "2026-09-29T19:04:22+00:00"
 },
 {
  "id": "89e5db3177a0",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Get started in Claude Cowork in three steps",
  "snippet": "",
  "published": "2026-09-29T16:52:58+00:00"
 },
 {
  "id": "9ccbbcf4e1a3",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "- academy.claude.com",
  "snippet": "academy.claude.com",
  "published": "2026-09-30T22:25:21+00:00"
 },
 {
  "id": "9d72d5707bd7",
  "region": "intl",
  "source": "Anthropic",
  "title": "Claude in Microsoft Foundry: control the cost, prove the value",
  "snippet": "",
  "published": "2026-09-29T19:38:52+00:00"
 },
 {
  "id": "006a7a871bca",
  "region": "intl",
  "source": "Anthropic",
  "title": "- Anthropic",
  "snippet": "Anthropic",
  "published": "2026-09-30T14:00:43+00:00"
 },
 {
  "id": "c91a96312fda",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Get started with smart reports | Claude Help Center",
  "snippet": "",
  "published": "2026-09-29T22:25:44+00:00"
 },
 {
  "id": "88c2b983d4e4",
  "region": "intl",
  "source": "claude.com",
  "title": "How Anthropic's sales team rebuilt inbound with Claude Managed Agents",
  "snippet": "",
  "published": "2026-09-30T14:06:32+00:00"
 },
 {
  "id": "f5825f00ee38",
  "region": "intl",
  "source": "claude.com",
  "title": "Connectors and plugins - Claude",
  "snippet": "",
  "published": "2026-09-30T18:58:07+00:00"
 },
 {
  "id": "5ff1d1380674",
  "region": "intl",
  "source": "claude.com",
  "title": "Cyera",
  "snippet": "",
  "published": "2026-09-30T18:16:57+00:00"
 },
 {
  "id": "310df9abad1c",
  "region": "intl",
  "source": "support.claude.com",
  "title": "How Claude marks AI-generated content | Claude Help Center",
  "snippet": "",
  "published": "2026-10-01T00:01:14+00:00"
 },
 {
  "id": "a7188554c0a6",
  "region": "intl",
  "source": "claude.com",
  "title": "Box Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-09-30T14:39:29+00:00"
 },
 {
  "id": "71678365a80b",
  "region": "intl",
  "source": "claude.com",
  "title": "Partner waitlist",
  "snippet": "",
  "published": "2026-09-30T14:38:23+00:00"
 },
 {
  "id": "e2812381b10f",
  "region": "intl",
  "source": "claude.com",
  "title": "Factory",
  "snippet": "",
  "published": "2026-09-30T15:01:18+00:00"
 },
 {
  "id": "d8c8c316a5f5",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Marketplace",
  "snippet": "",
  "published": "2026-09-29T19:08:37+00:00"
 },
 {
  "id": "e906205e2ba5",
  "region": "intl",
  "source": "claude.com",
  "title": "Slack Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-09-30T02:36:56+00:00"
 },
 {
  "id": "d9aceddd3007",
  "region": "intl",
  "source": "claude.com",
  "title": "CodeRabbit",
  "snippet": "",
  "published": "2026-09-30T02:31:39+00:00"
 },
 {
  "id": "a5afe4bc0fad",
  "region": "intl",
  "source": "claude.com",
  "title": "monday.com",
  "snippet": "",
  "published": "2026-09-30T14:41:42+00:00"
 },
 {
  "id": "efce1daa2ff1",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.286",
  "snippet": "What's changed Added a count such as \"2 of 5\" to the permission prompt when several permission requests stack up Added mouse support for the \"N more\" rows of lists in fullscreen mode: click one to jump to that end of the list, with hover and pressed states Fixed several Claude Code processes and IDE extensions each opening a login browser when gcpAuthRefresh or awsAuthRefresh credentials expire Fixed claude --resume and --continue sometimes losing every turn after a batch of parallel tool calls when the earlier session crashed or was killed Fixed API 400 errors after a tool or hook returned an…",
  "published": "2026-09-30T19:10:13+00:00"
 },
 {
  "id": "d906990043d7",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.285",
  "snippet": "What's changed Added CLAUDE_CODE_DISABLE_WEB_FETCH environment variable to turn off the WebFetch tool Added claude --desktop to open the Claude desktop app on the current directory, or on a session with --continue / --resume <id> Added claude plugin configure <plugin> to show a plugin's options and which are unset, or save new values read from stdin with --values-stdin Added <server>.<key>=<value> to claude plugin install --config , so a bundled .mcpb MCP server's own settings can be set at install time and it starts without visiting /plugin → Configure Added allowedProviders managed setting t…",
  "published": "2026-09-29T19:27:30+00:00"
 }
]
