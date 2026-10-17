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
  "id": "8d5c9c890eb3",
  "region": "jp",
  "source": "窓の杜",
  "title": "「Claude」Anthropicが開発したAIモデル／AIチャットボット",
  "snippet": "",
  "published": "2026-10-17T15:05:00+00:00"
 },
 {
  "id": "452b801c134e",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、Claudeが25年来のNSA暗号シード謎を30分で解明と発表",
  "snippet": "",
  "published": "2026-10-17T18:05:00+00:00"
 },
 {
  "id": "ad210a0b95e5",
  "region": "jp",
  "source": "shiritomo",
  "title": "Claude Codeの「コードレビュー」が一般提供開始、6〜10分で終わる仕組みの中身",
  "snippet": "",
  "published": "2026-10-17T08:25:26+00:00"
 },
 {
  "id": "30271fca6457",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "AnthropicがClaude Mythos 5設計の量子回路を公開、効率は最大39倍",
  "snippet": "",
  "published": "2026-10-17T18:55:26+00:00"
 },
 {
  "id": "8e997f88e977",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Anthropic、従業員の若手比率が低下し、会議に費やす時間が増えたと報告",
  "snippet": "",
  "published": "2026-10-17T14:37:00+00:00"
 },
 {
  "id": "db552ab7b2b1",
  "region": "jp",
  "source": "Ledge.ai",
  "title": "Anthropic共同創業者、AIによる後継AIの開発が可能になる時期を2027年と予測 東大講演で「50％以上」",
  "snippet": "",
  "published": "2026-10-17T02:55:25+00:00"
 },
 {
  "id": "c1e7e3b42824",
  "region": "jp",
  "source": "CoinDesk",
  "title": "「これは本物の発見だ」：クロードがNSAの25年間の数字の謎を解明",
  "snippet": "",
  "published": "2026-10-17T06:39:48+00:00"
 },
 {
  "id": "42fad7de5666",
  "region": "jp",
  "source": "財経新聞",
  "title": "米FTC、OpenAIとAnthropicに民事調査要求 AIの安全対策や利用者向け説明を調査",
  "snippet": "",
  "published": "2026-10-17T07:50:00+00:00"
 },
 {
  "id": "41eb0a4ddcb3",
  "region": "jp",
  "source": "QUANTUM BUSINESS MAGAZINE -",
  "title": "ハーバード大学、Anthropic、QuEraがLLMを活用し、リソースコストを最大9,100倍削減する量子回路を発見",
  "snippet": "",
  "published": "2026-10-17T13:10:14+00:00"
 },
 {
  "id": "4ac37bd45fa0",
  "region": "jp",
  "source": "YouTube",
  "title": "【Anthropic・OpenAI朝刊】2026-10-18（日） AI安全法案の草案／カナダ初のDC契約",
  "snippet": "",
  "published": "2026-10-17T19:09:39+00:00"
 },
 {
  "id": "2cbd6b1680d1",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "Anthropic社は、米国における危険なAIモデルの使用を停止させる仕組みを提案している。",
  "snippet": "",
  "published": "2026-10-17T06:44:39+00:00"
 },
 {
  "id": "a27c98b952ea",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic共同創業者、AIで米GDPが2030年に44.4兆ドルへ拡大もと発言",
  "snippet": "",
  "published": "2026-10-17T18:16:00+00:00"
 },
 {
  "id": "e0cd4aa5841e",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "ReplitがAnthropicとの決別を発表、だが「決別」には異論も",
  "snippet": "",
  "published": "2026-10-17T13:05:44+00:00"
 },
 {
  "id": "50d533450ba6",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic内部データが明かすAIの衝撃：初級技術職の採用が激減、AIエージェントの労働時間は社員の6倍に",
  "snippet": "",
  "published": "2026-10-17T07:25:00+00:00"
 },
 {
  "id": "7f201cfcf1d1",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Claudeが楕円曲線ECDSAの起源を解明、NSAのシードはタイムスタンプだった",
  "snippet": "",
  "published": "2026-10-17T18:47:22+00:00"
 },
 {
  "id": "e9107f1eef88",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropicが量子計算のブレークスルーを発表：Claudeが自律設計した回路、人間の最適解より効率17倍",
  "snippet": "",
  "published": "2026-10-17T03:55:00+00:00"
 },
 {
  "id": "547e242815cb",
  "region": "jp",
  "source": "au Webポータル",
  "title": "すべてのAIコーディングエージェントのコストを閲覧・検索・追跡しローカルで動作する「AgentsView」、Claude Code・Codex・Cursor・Copilot・Geminiなど60種類以上のエージェントを自動検出し全文検索も可能",
  "snippet": "",
  "published": "2026-10-17T09:00:00+00:00"
 },
 {
  "id": "913c27041fe7",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "AnthropicがClaude Codeのgzip圧縮とクラウドセッション高速化を発表",
  "snippet": "",
  "published": "2026-10-17T07:56:33+00:00"
 },
 {
  "id": "266739fa8229",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "米Anthropic、極端なケースに限定したAIモデル停止権限を政府に付与する法案草案を作成",
  "snippet": "",
  "published": "2026-10-17T00:25:00+00:00"
 },
 {
  "id": "5c1a9b9069ed",
  "region": "jp",
  "source": "財経新聞",
  "title": "[写真]米FTC、OpenAIとAnthropicに民事調査要求 AIの安全対策や利用者向け説明を調査",
  "snippet": "",
  "published": "2026-10-17T07:50:00+00:00"
 },
 {
  "id": "cc9c640e242f",
  "region": "jp",
  "source": "Reuters",
  "title": "Anthropic IPO timing, price is major factor for stocks now, says CIO",
  "snippet": "",
  "published": "2026-10-16T22:18:43+00:00"
 },
 {
  "id": "13cfab4f653b",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "CoreWeave株急落、AIトレードの亀裂、Anthropic IPOの危険信号、ビル・ゲイツの終末論",
  "snippet": "",
  "published": "2026-10-17T02:03:14+00:00"
 },
 {
  "id": "217728c7e426",
  "region": "jp",
  "source": "Chosunbiz",
  "title": "Anthropicが韓国作家作品無断学習で和解金150億ドル支払う - CHOSUNBIZ",
  "snippet": "",
  "published": "2026-10-17T01:46:00+00:00"
 },
 {
  "id": "ce22bb0c4ed1",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicがカナダでEverWindと初のデータセンター契約を締結、EverWindは100億カナダドル超の投資を計画 執筆",
  "snippet": "",
  "published": "2026-10-17T00:06:00+00:00"
 },
 {
  "id": "a26919a84c7f",
  "region": "jp",
  "source": "Moomoo",
  "title": "【速報】Anthropic、市監査官と協議開始 AI安全・統治懸念でIPO延期要請",
  "snippet": "",
  "published": "2026-10-16T14:19:23+00:00"
 },
 {
  "id": "a110e6288b4c",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Replit makes OpenAI its default over Anthropic, CEO says",
  "snippet": "",
  "published": "2026-10-17T18:48:08+00:00"
 },
 {
  "id": "a8a7e02194ca",
  "region": "intl",
  "source": "Fortune",
  "title": "Anthropic’s Dario Amodei is steering a possible $2 trillion IPO—but he says up to 40% of his time goes to making sure company culture is good",
  "snippet": "",
  "published": "2026-10-17T13:28:00+00:00"
 },
 {
  "id": "723623052971",
  "region": "intl",
  "source": "Mother Jones",
  "title": "Anthropic’s AI Safety Bill Has an Alarming Threshold for Government Action",
  "snippet": "",
  "published": "2026-10-17T19:25:21+00:00"
 },
 {
  "id": "af51c30e8235",
  "region": "intl",
  "source": "CNBC",
  "title": "AI rapidly improving, could vastly boost U.S. GDP, Anthropic's Clark tells policymakers",
  "snippet": "",
  "published": "2026-10-17T23:04:00+00:00"
 },
 {
  "id": "c34caf926428",
  "region": "intl",
  "source": "Business Insider",
  "title": "AI was supposed to spare gardeners. Anthropic's robot research has me thinking about pulling weeds.",
  "snippet": "",
  "published": "2026-10-17T14:00:00+00:00"
 },
 {
  "id": "ad621b2c6572",
  "region": "intl",
  "source": "CoinDesk",
  "title": "‘Wow, it’s a real discovery’: Claude cracks a 25-year NSA number mystery",
  "snippet": "",
  "published": "2026-10-17T06:39:48+00:00"
 },
 {
  "id": "ab0f8af8c9ea",
  "region": "intl",
  "source": "The Next Web",
  "title": "Robots and AI could reach 80% of work but rarely cheaply, Anthropic says",
  "snippet": "",
  "published": "2026-10-17T18:18:22+00:00"
 },
 {
  "id": "002bb1d55152",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic offers Blackstone double-digit yield in chip-financing deal, FT reports",
  "snippet": "",
  "published": "2026-10-17T01:01:00+00:00"
 },
 {
  "id": "e07f88793747",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Anthropic says its workforce has become less junior and is spending more time in meetings",
  "snippet": "",
  "published": "2026-10-17T20:21:19+00:00"
 },
 {
  "id": "7a5445549048",
  "region": "intl",
  "source": "The Times of India",
  "title": "Some Accenture employees spent $1,000 a month on Anthropic’s Claude AI, company will now centrally fund $",
  "snippet": "",
  "published": "2026-10-17T08:12:00+00:00"
 },
 {
  "id": "64f8d6a84294",
  "region": "intl",
  "source": "Startup Fortune",
  "title": "OpenCode breach exposes stored OpenAI and Anthropic keys, prompts urgent key rotation",
  "snippet": "",
  "published": "2026-10-17T18:57:21+00:00"
 },
 {
  "id": "cacd964e2c2f",
  "region": "intl",
  "source": "The Quantum Insider",
  "title": "Anthropic’s Claude Designs Leaner Quantum Circuits, Reducing Resources Needed for Key Calculations",
  "snippet": "",
  "published": "2026-10-17T08:12:06+00:00"
 },
 {
  "id": "1af16ca32cfa",
  "region": "intl",
  "source": "Seeking Alpha",
  "title": "Anthropic co-founder Clark projects U.S. GDP to hit $44T by 2030 thanks to AI",
  "snippet": "",
  "published": "2026-10-17T12:03:55+00:00"
 },
 {
  "id": "eb1d2f9292ce",
  "region": "intl",
  "source": "Mezha.net",
  "title": "Anthropic says its workforce is less junior and employees spend more time in meetings",
  "snippet": "",
  "published": "2026-10-17T20:54:22+00:00"
 },
 {
  "id": "94c1995dbd83",
  "region": "intl",
  "source": "Quantum Zeitgeist",
  "title": "Anthropic's Claude Improves Quantum Optimization Designs",
  "snippet": "",
  "published": "2026-10-17T15:28:19+00:00"
 },
 {
  "id": "22dfd915ac79",
  "region": "intl",
  "source": "Startup Fortune",
  "title": "Anthropic's Jack Clark Tells the IMF AI Could Push US GDP to $44 Trillion",
  "snippet": "",
  "published": "2026-10-17T13:55:25+00:00"
 },
 {
  "id": "3f09240927aa",
  "region": "intl",
  "source": "Financial Times",
  "title": "Anthropic offers Blackstone double-digit yield in latest chip financing",
  "snippet": "",
  "published": "2026-10-17T00:47:25+00:00"
 },
 {
  "id": "cde9cf616e71",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic Wants an IPO. New York City Wants It to Slow Down.",
  "snippet": "",
  "published": "2026-10-17T12:02:00+00:00"
 },
 {
  "id": "b5bbf5af3022",
  "region": "intl",
  "source": "TestingCatalog AI News",
  "title": "Anthropic prepares to release Claude Fable 5.5 next week",
  "snippet": "",
  "published": "2026-10-17T12:57:51+00:00"
 },
 {
  "id": "2b32f529103f",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Some Anthropic Investors Now See a $1.5 Trillion IPO, Not $2 Trillion",
  "snippet": "",
  "published": "2026-10-16T12:24:07+00:00"
 },
 {
  "id": "e6cb02d78b66",
  "region": "intl",
  "source": "How-To Geek",
  "title": "OpenCode Go is the half-priced Claude Code replacement that I can't stop recommending to techy friends",
  "snippet": "",
  "published": "2026-10-17T11:00:17+00:00"
 },
 {
  "id": "c9634539a3ae",
  "region": "intl",
  "source": "Law Commentary",
  "title": "Anthropic Quietly Pushes AI Safety Bill That Would Limit Government Power to Block Dangerous Models",
  "snippet": "",
  "published": "2026-10-17T02:44:47+00:00"
 },
 {
  "id": "302bbe53a277",
  "region": "intl",
  "source": "Futurism",
  "title": "Investors Disturbed by Anthropic’s Financial Data",
  "snippet": "",
  "published": "2026-10-17T10:50:00+00:00"
 },
 {
  "id": "3ac55f27f0ae",
  "region": "intl",
  "source": "The Next Web",
  "title": "‘AI must remain under human direction’: EU puts the AI Act to the test",
  "snippet": "",
  "published": "2026-10-17T13:26:16+00:00"
 },
 {
  "id": "4eb8e8857c10",
  "region": "intl",
  "source": "Briefs Finance",
  "title": "Anthropic floats bill to let U.S. block risky AI models",
  "snippet": "",
  "published": "2026-10-17T15:42:43+00:00"
 },
 {
  "id": "0fa79364222b",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Daftar Message Batch",
  "snippet": "",
  "published": "2026-10-17T04:43:31+00:00"
 },
 {
  "id": "bfa08d196505",
  "region": "intl",
  "source": "claude.com",
  "title": "Going deeper",
  "snippet": "",
  "published": "2026-10-17T01:08:37+00:00"
 },
 {
  "id": "08f4da2ba2c1",
  "region": "intl",
  "source": "claude.com",
  "title": "Building commerce agents with Claude",
  "snippet": "",
  "published": "2026-10-16T14:33:49+00:00"
 },
 {
  "id": "318588b45685",
  "region": "intl",
  "source": "claude.com",
  "title": "Centrally manage authorization for MCP connectors",
  "snippet": "",
  "published": "2026-10-16T12:40:01+00:00"
 },
 {
  "id": "06faf135c70b",
  "region": "intl",
  "source": "claude.com",
  "title": "Bringing Claude Code and Claude Cowork to government",
  "snippet": "",
  "published": "2026-10-17T11:26:15+00:00"
 },
 {
  "id": "9af0f1d6f067",
  "region": "intl",
  "source": "claude.com",
  "title": "How Anthropic's finance team uses Claude to shape the narrative behind the numbers",
  "snippet": "",
  "published": "2026-10-17T04:37:29+00:00"
 },
 {
  "id": "6bec5fe491e5",
  "region": "intl",
  "source": "claude.com",
  "title": "Introducing routines in Claude Code",
  "snippet": "",
  "published": "2026-10-17T02:04:03+00:00"
 },
 {
  "id": "cb715adf0142",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Use Claude Security",
  "snippet": "",
  "published": "2026-10-16T17:25:30+00:00"
 },
 {
  "id": "ef237904dce8",
  "region": "intl",
  "source": "claude.com",
  "title": "Lovable Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-17T04:35:46+00:00"
 },
 {
  "id": "034889de3d4d",
  "region": "intl",
  "source": "claude.com",
  "title": "Subtext connector",
  "snippet": "",
  "published": "2026-10-17T07:46:35+00:00"
 },
 {
  "id": "d1964a80d027",
  "region": "intl",
  "source": "claude.com",
  "title": "Vambe Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-17T08:02:37+00:00"
 },
 {
  "id": "d4595df3aeee",
  "region": "intl",
  "source": "claude.com",
  "title": "The evolution of agentic surfaces: building with Claude Managed Agents",
  "snippet": "",
  "published": "2026-10-17T09:56:15+00:00"
 },
 {
  "id": "6bfa1d1e62bd",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Code",
  "snippet": "",
  "published": "2026-10-16T13:23:42+00:00"
 },
 {
  "id": "b7ba1ec0e393",
  "region": "intl",
  "source": "claude.com",
  "title": "Expo",
  "snippet": "",
  "published": "2026-10-16T12:59:24+00:00"
 },
 {
  "id": "1109ce09aeb4",
  "region": "intl",
  "source": "claude.com",
  "title": "item connector",
  "snippet": "",
  "published": "2026-10-17T02:57:34+00:00"
 },
 {
  "id": "a29062dae978",
  "region": "intl",
  "source": "claude.com",
  "title": "Building an AI-native revenue organization",
  "snippet": "",
  "published": "2026-10-16T13:00:19+00:00"
 },
 {
  "id": "6841843bf179",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Financial Advisors: Your Cowork Security and Compliance Questions, Answered",
  "snippet": "",
  "published": "2026-10-16T19:49:34+00:00"
 },
 {
  "id": "6436c72d3c24",
  "region": "intl",
  "source": "claude.com",
  "title": "Shopify connector",
  "snippet": "",
  "published": "2026-10-16T13:31:41+00:00"
 },
 {
  "id": "0ae7735e0918",
  "region": "intl",
  "source": "claude.com",
  "title": "Inside Claude for Financial Advisors",
  "snippet": "",
  "published": "2026-10-16T15:10:40+00:00"
 },
 {
  "id": "15578e9b265e",
  "region": "intl",
  "source": "claude.com",
  "title": "Apollo.io connector",
  "snippet": "",
  "published": "2026-10-16T15:07:41+00:00"
 },
 {
  "id": "0c77200383c2",
  "region": "intl",
  "source": "claude.com",
  "title": "MindMeister",
  "snippet": "",
  "published": "2026-10-16T12:31:47+00:00"
 },
 {
  "id": "d436f54c56c1",
  "region": "intl",
  "source": "Anthropic",
  "title": "Appendix to “The AI Expectations Gap”",
  "snippet": "",
  "published": "2026-10-16T21:16:42+00:00"
 },
 {
  "id": "ff28c763d42c",
  "region": "intl",
  "source": "claude.com",
  "title": "Greenhouse connector",
  "snippet": "",
  "published": "2026-10-17T00:49:23+00:00"
 },
 {
  "id": "09d087ce1381",
  "region": "intl",
  "source": "claude.com",
  "title": "Articles",
  "snippet": "",
  "published": "2026-10-16T22:26:03+00:00"
 },
 {
  "id": "94801ee1696f",
  "region": "intl",
  "source": "claude.com",
  "title": "Introducing the Claude Platform on AWS",
  "snippet": "",
  "published": "2026-10-16T12:40:14+00:00"
 }
]
