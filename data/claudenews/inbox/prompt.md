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
  "id": "0dbc2c9bff75",
  "region": "jp",
  "source": "キーマンズネット",
  "title": "「Claude」3倍高速化の裏で、Anthropic開発者が「あえてしなかったこと」：899th Lap",
  "snippet": "",
  "published": "2026-10-01T22:00:00+00:00"
 },
 {
  "id": "e2212a12c1b4",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "「Claude Codeがすごい」と言う人が見分けていないもの（尾藤克之） - エキスパート",
  "snippet": "",
  "published": "2026-10-01T21:40:28+00:00"
 },
 {
  "id": "988f9f970e2b",
  "region": "jp",
  "source": "Digital PR Platform",
  "title": "freeeのテックカンファレンス「freee 技術の日 2026」にて、AnthropicとAWSの登壇が決定",
  "snippet": "",
  "published": "2026-10-01T19:02:47+00:00"
 },
 {
  "id": "a70fa144b8ef",
  "region": "jp",
  "source": "TradingKey",
  "title": "アンスロピックIPO：Claudeの開発元について知っておくべき重要な情報",
  "snippet": "",
  "published": "2026-10-01T13:53:58+00:00"
 },
 {
  "id": "78a4d7bb21f8",
  "region": "jp",
  "source": "rocket-boys.co.jp",
  "title": "AIエージェントが勝手にハッキングしたら誰が責任を負う？Anthropicが法的リスクを警告、OpenAIはHugging Face侵害で提訴",
  "snippet": "",
  "published": "2026-10-01T21:30:28+00:00"
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
  "id": "9f1a6bbf93fb",
  "region": "jp",
  "source": "TIKR.com",
  "title": "Billionaire Investor Predicts 50% Haircut to Anthropic IPO Price: “$1 Trillion or Less”",
  "snippet": "",
  "published": "2026-10-01T17:24:35+00:00"
 },
 {
  "id": "7f86a8e2a4e9",
  "region": "jp",
  "source": "Investing.com 日本",
  "title": "AnthropicがサンクスギビングホリデーまでにIPOをターゲット 執筆",
  "snippet": "",
  "published": "2026-10-01T17:40:00+00:00"
 },
 {
  "id": "b525cc3dffb3",
  "region": "jp",
  "source": "PR TIMES",
  "title": "Anthropic・OpenAI投資家と明治安田生命のAI責任者が登壇日本の大手企業が「AX」で勝つ条件を議論する完全オフレコの経営者向け特別セッションを10月6日に開催",
  "snippet": "",
  "published": "2026-10-01T06:00:02+00:00"
 },
 {
  "id": "e76762f40e0f",
  "region": "jp",
  "source": "moomoo.com",
  "title": "ブロードコム、Anthropicに420億ドルをベット：ASIC物語の新たな章か？",
  "snippet": "",
  "published": "2026-10-02T00:08:18+00:00"
 },
 {
  "id": "5665bceeb612",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "米国は、AI関係者による一連の事件を受け、OpenAIとAnthropicに対する捜査を開始した。",
  "snippet": "",
  "published": "2026-10-01T13:16:34+00:00"
 },
 {
  "id": "54eaeaebb828",
  "region": "jp",
  "source": "日経クロステック（xTECH）",
  "title": "Claude Codeの「ごまかし」に直面 マネージド版と併用で乗り切る",
  "snippet": "",
  "published": "2026-09-30T22:02:00+00:00"
 },
 {
  "id": "6224c79a52fa",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "Anthropicの営業チームはClaudeの自動返信で成約件数を2.5倍にした",
  "snippet": "",
  "published": "2026-10-01T02:40:00+00:00"
 },
 {
  "id": "cae26303a132",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "世界有数の金融機関がClaudeを全社展開、2027年に技術者の過半数がClaude Code利用へ（ビジネス＋IT）",
  "snippet": "",
  "published": "2026-10-01T10:05:06+00:00"
 },
 {
  "id": "ae258b729e14",
  "region": "jp",
  "source": "TradingKey",
  "title": "アンソロピックの2026年IPO：投資家が答えを求める5つの疑問",
  "snippet": "",
  "published": "2026-10-01T14:37:06+00:00"
 },
 {
  "id": "34ceb9c03561",
  "region": "jp",
  "source": "ITmedia",
  "title": "米連邦取引委がAI大手の調査開始 AnthropicやOpenAIなど、暴走や悪用の懸念",
  "snippet": "",
  "published": "2026-10-01T07:01:45+00:00"
 },
 {
  "id": "d85e718362f4",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Claude Codeは、コードを書かない人こそ使える。散らかったフォルダもWindowsのエラーも「頼むだけ」で片づいた",
  "snippet": "",
  "published": "2026-10-01T05:01:02+00:00"
 },
 {
  "id": "2eeb4c814ea7",
  "region": "jp",
  "source": "Chosunbiz",
  "title": "Anthropicが11月中旬IPO目指す 時価総額最大2兆ドル見込む - CHOSUNBIZ",
  "snippet": "",
  "published": "2026-10-02T01:12:00+00:00"
 },
 {
  "id": "eebe057e9bfa",
  "region": "jp",
  "source": "디지털투데이",
  "title": "Anthropic、米連邦機関向け「Claude for Government」を正式提供",
  "snippet": "",
  "published": "2026-10-01T23:48:52+00:00"
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
  "id": "c7e92cd3a1e6",
  "region": "jp",
  "source": "ゴリミー",
  "title": "Claudeの会社、11月にも上場へ。評価額は最大2兆ドル",
  "snippet": "",
  "published": "2026-10-01T21:39:17+00:00"
 },
 {
  "id": "ed992549d905",
  "region": "jp",
  "source": "newspicks.com",
  "title": "あなたのClaude Codeが微妙なのは、プロンプトのせいじゃない",
  "snippet": "",
  "published": "2026-09-30T21:30:13+00:00"
 },
 {
  "id": "be60b24179c7",
  "region": "jp",
  "source": "財経新聞",
  "title": "NVIDIA、Anthropic向けAI基盤2.6GWを開示 Rubin世代の売上機会は1GW当たり400億ドル",
  "snippet": "",
  "published": "2026-10-01T08:03:00+00:00"
 },
 {
  "id": "9b4d0e0f87ce",
  "region": "jp",
  "source": "moomoo.com",
  "title": "【速報】ブロードコムはAnthropicに対し、自社AIチップのリース資金として最大420億ドルを融資する",
  "snippet": "",
  "published": "2026-10-01T11:09:55+00:00"
 },
 {
  "id": "0e5487f7aae3",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "2兆ドルIPOを目指すAnthropic、その裏で抱える5,180億ドルの巨額AI契約",
  "snippet": "",
  "published": "2026-10-01T03:20:06+00:00"
 },
 {
  "id": "002c70a07e0f",
  "region": "intl",
  "source": "Reuters",
  "title": "EXCLUSIVE: Broadcom to lend Anthropic up to $42 billion to lease its chips, filing says",
  "snippet": "",
  "published": "2026-10-01T21:50:00+00:00"
 },
 {
  "id": "0d21e0d77af7",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic reportedly looking to IPO as early as mid-November",
  "snippet": "",
  "published": "2026-10-01T20:18:53+00:00"
 },
 {
  "id": "4498fdf7edba",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic Targets Mega-IPO Before Thanksgiving Holiday",
  "snippet": "",
  "published": "2026-10-01T21:04:14+00:00"
 },
 {
  "id": "7f19a7edefe8",
  "region": "intl",
  "source": "Anthropic",
  "title": "Claude-shaped science",
  "snippet": "",
  "published": "2026-10-01T14:02:00+00:00"
 },
 {
  "id": "2185a3c4db34",
  "region": "intl",
  "source": "Barron's",
  "title": "Broadcom Stock Rises. Anthropic and Broadcom Are Becoming More Intertwined.",
  "snippet": "",
  "published": "2026-10-01T19:13:00+00:00"
 },
 {
  "id": "34b679ae232f",
  "region": "intl",
  "source": "CNBC",
  "title": "Broadcom to lend Anthropic up to $42 billion to lease its chips, filing says",
  "snippet": "",
  "published": "2026-10-01T12:20:57+00:00"
 },
 {
  "id": "24b743f25bf1",
  "region": "intl",
  "source": "theguardian.com",
  "title": "Anthropic pushes for opt-out model for Australian content as ABC warns of ‘cannibalisation’ of news",
  "snippet": "",
  "published": "2026-10-01T21:53:00+00:00"
 },
 {
  "id": "c47ef16433b4",
  "region": "intl",
  "source": "San Francisco Chronicle",
  "title": "Exclusive: Anthropic eyeing Mission District industrial space as AI company moves beyond the office",
  "snippet": "",
  "published": "2026-10-01T23:47:53+00:00"
 },
 {
  "id": "0946eb0301be",
  "region": "intl",
  "source": "Britannica",
  "title": "Anthropic | History, Controversies, & Claude AI",
  "snippet": "",
  "published": "2026-10-01T07:05:41+00:00"
 },
 {
  "id": "d0bfdde67dd3",
  "region": "intl",
  "source": "Broadband Breakfast",
  "title": "FTC Opens Probe of AI Giants Anthropic, OpenAI Over Consumer Risks",
  "snippet": "",
  "published": "2026-10-01T23:39:34+00:00"
 },
 {
  "id": "95f90a0c4d57",
  "region": "intl",
  "source": "The Hill",
  "title": "FTC launches probe into OpenAI, Anthropic over model consumer risks",
  "snippet": "",
  "published": "2026-10-01T19:32:00+00:00"
 },
 {
  "id": "95269bafa25a",
  "region": "intl",
  "source": "SiliconANGLE",
  "title": "Report: Anthropic targets pre-Thanksgiving IPO launch, despite warning of AI's 'existential risks'",
  "snippet": "",
  "published": "2026-10-01T23:43:00+00:00"
 },
 {
  "id": "b737560ef869",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Barclays Accelerates AI Rollout With Anthropic’s Claude Code",
  "snippet": "",
  "published": "2026-10-01T14:44:07+00:00"
 },
 {
  "id": "b8f0059e8f6f",
  "region": "intl",
  "source": "ExecutiveBiz",
  "title": "Anthropic Announces General Availability of Claude for Government",
  "snippet": "",
  "published": "2026-10-01T15:29:31+00:00"
 },
 {
  "id": "151993a637ab",
  "region": "intl",
  "source": "Seton Hall University",
  "title": "Artificial Intelligence Researcher Resigns from AI Developer Anthropic Amid Safety Concerns for the Future of Development in the Industry",
  "snippet": "",
  "published": "2026-10-01T19:15:22+00:00"
 },
 {
  "id": "a66d1c996546",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic Is Said to Plan Pre-IPO Investor Day as Listing Nears",
  "snippet": "",
  "published": "2026-10-01T20:14:03+00:00"
 },
 {
  "id": "99bdaced7e4f",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Broadcom to lend Anthropic up to $42 billion to lease chips, in latest circular investing deal",
  "snippet": "",
  "published": "2026-10-01T14:37:32+00:00"
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
  "id": "d17c553c130c",
  "region": "intl",
  "source": "Barron's",
  "title": "Anthropic IPO to Come Before Thanksgiving, Report Says. Why the Timing Matters.",
  "snippet": "",
  "published": "2026-10-01T19:01:00+00:00"
 },
 {
  "id": "2d5af9f9c9bc",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Watch Anthropic Said to Target Mega-IPO Before Thanksgiving Holiday",
  "snippet": "",
  "published": "2026-10-02T00:00:00+00:00"
 },
 {
  "id": "6a4c0705c77c",
  "region": "intl",
  "source": "New York Post",
  "title": "Anthropic plans blockbuster IPO before Thanksgiving despite its warnings of 'existential risks to humanity': report",
  "snippet": "",
  "published": "2026-10-01T19:07:00+00:00"
 },
 {
  "id": "f6a4738a29b0",
  "region": "intl",
  "source": "observer.com",
  "title": "Dario Amodei’s $518 Billion Bet Gives AI’s Infrastructure Leaders the Upper Hand",
  "snippet": "",
  "published": "2026-10-01T22:52:30+00:00"
 },
 {
  "id": "9fd73e82391c",
  "region": "intl",
  "source": "Florida International University",
  "title": "Will Claude's new AI \"watermark\" keep us all honest?",
  "snippet": "",
  "published": "2026-10-01T20:54:04+00:00"
 },
 {
  "id": "13d79f861496",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic CEO Dario Amodei is warning about AI risks the wrong way: Meta's former CTO",
  "snippet": "",
  "published": "2026-10-01T15:48:38+00:00"
 },
 {
  "id": "3ff4d0613ef3",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Anthropic Targets Pre-Thanksgiving IPO at $2 Trillion Valuation",
  "snippet": "",
  "published": "2026-10-01T23:25:05+00:00"
 },
 {
  "id": "e1c975732d4f",
  "region": "intl",
  "source": "claude.com",
  "title": "Customize Claude Code with mods in TypeScript | Claude by Anthropic",
  "snippet": "",
  "published": "2026-10-01T18:03:32+00:00"
 },
 {
  "id": "8f94d082d77a",
  "region": "intl",
  "source": "Anthropic",
  "title": "Barclays scales Claude to upgrade operations and improve client experience",
  "snippet": "",
  "published": "2026-10-01T15:19:00+00:00"
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
  "id": "bd6e02d9333e",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Prompting Claude Sonnet 5.5",
  "snippet": "",
  "published": "2026-10-02T01:16:14+00:00"
 },
 {
  "id": "6093cfce68e8",
  "region": "intl",
  "source": "Anthropic",
  "title": "Building with the Claude 5.5 Family: Choosing the Right Model and Getting More from Every Token",
  "snippet": "",
  "published": "2026-10-01T16:00:00+00:00"
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
  "id": "d30ca3f5cca3",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Migrating to Claude Sonnet 5.5",
  "snippet": "",
  "published": "2026-10-02T00:58:08+00:00"
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
  "id": "cdbfeef20de6",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Get started with Claude Compliance API integrations | Claude Help Center",
  "snippet": "",
  "published": "2026-09-30T16:26:00+00:00"
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
  "id": "c86e87c31950",
  "region": "intl",
  "source": "claude.com",
  "title": "Mods overview",
  "snippet": "",
  "published": "2026-10-01T18:05:50+00:00"
 },
 {
  "id": "d25d419395ac",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Artifact usage promotion | Claude Help Center",
  "snippet": "",
  "published": "2026-10-01T18:00:20+00:00"
 },
 {
  "id": "9ccbbcf4e1a3",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "- academy.claude.com",
  "snippet": "academy.claude.com",
  "published": "2026-10-01T23:55:48+00:00"
 },
 {
  "id": "006a7a871bca",
  "region": "intl",
  "source": "Anthropic",
  "title": "- Anthropic",
  "snippet": "Anthropic",
  "published": "2026-10-01T14:17:13+00:00"
 },
 {
  "id": "acde9aa72587",
  "region": "intl",
  "source": "claude.com",
  "title": "Agents and products",
  "snippet": "",
  "published": "2026-10-01T03:47:36+00:00"
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
  "id": "2a23e1fd26cf",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Model availability in Claude for Government",
  "snippet": "",
  "published": "2026-09-30T19:18:06+00:00"
 },
 {
  "id": "12a316156dee",
  "region": "intl",
  "source": "support.claude.com",
  "title": "SSO login | Claude Help Center",
  "snippet": "",
  "published": "2026-09-30T19:16:06+00:00"
 },
 {
  "id": "1583cf6b1c65",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Get started with Claude for Government",
  "snippet": "",
  "published": "2026-09-30T19:15:18+00:00"
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
  "id": "0b371eed8ad5",
  "region": "intl",
  "source": "claude.com",
  "title": "How does a badge-maker shorten lead times but keep an old-world process alive?",
  "snippet": "",
  "published": "2026-09-30T21:18:27+00:00"
 },
 {
  "id": "634a2190939e",
  "region": "intl",
  "source": "claude.com",
  "title": "Syracuse University Claude Enterprise case study",
  "snippet": "",
  "published": "2026-09-30T15:02:06+00:00"
 },
 {
  "id": "ad3b1b751e6a",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Manage plugins for your organization",
  "snippet": "",
  "published": "2026-09-30T16:54:01+00:00"
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
  "id": "d896475d827e",
  "region": "intl",
  "source": "claude.com",
  "title": "Fitch Solutions connector",
  "snippet": "",
  "published": "2026-10-01T00:03:41+00:00"
 },
 {
  "id": "287cb9c6426f",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.287",
  "snippet": "What's changed Added Claude Mods: plugins may now modify deeper behavior Added You should know, a built-in mod where a side agent watches your back and flags things you or Claude might miss. Turn it on with /plugin enable cc-plugin-you-should-know@builtin (for first-party sessions with telemetry on) Added an n:<text> filter to the agents view that matches session names and tasks; a filter now shows matches in collapsed sections and Enter opens the first match Added prompt_text to the OpenTelemetry user_prompt event, a copy of prompt for backends that nest dotted keys; drop or mask it wherever…",
  "published": "2026-10-01T18:43:19+00:00"
 },
 {
  "id": "efce1daa2ff1",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.286",
  "snippet": "What's changed Added a count such as \"2 of 5\" to the permission prompt when several permission requests stack up Added mouse support for the \"N more\" rows of lists in fullscreen mode: click one to jump to that end of the list, with hover and pressed states Fixed several Claude Code processes and IDE extensions each opening a login browser when gcpAuthRefresh or awsAuthRefresh credentials expire Fixed claude --resume and --continue sometimes losing every turn after a batch of parallel tool calls when the earlier session crashed or was killed Fixed API 400 errors after a tool or hook returned an…",
  "published": "2026-09-30T19:10:13+00:00"
 }
]
