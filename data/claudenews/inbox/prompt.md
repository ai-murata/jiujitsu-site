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
  "id": "9a1754a954cc",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic、独自の“創薬活動”に着手 社員1人のバイオ企業を買収、小児難病の治療薬研究を進める",
  "snippet": "",
  "published": "2026-10-28T04:07:50+00:00"
 },
 {
  "id": "0913285fc336",
  "region": "jp",
  "source": "IDNFinancials",
  "title": "AIを誰が制御するのか？Anthropicは創業者承継の方法を準備",
  "snippet": "",
  "published": "2026-10-28T23:40:00+00:00"
 },
 {
  "id": "deb928e6e066",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "GitHub、Claude Codeに2点差の「半額」AI投入…「Copilot Fusion」の仕組みとは？（ビジネス＋IT）",
  "snippet": "",
  "published": "2026-10-28T17:30:06+00:00"
 },
 {
  "id": "45461225f155",
  "region": "jp",
  "source": "ビジネス+IT",
  "title": "GitHub、Claude Codeに2点差の「半額」AI投入…「Copilot Fusion」の仕組みとは？",
  "snippet": "",
  "published": "2026-10-28T17:16:00+00:00"
 },
 {
  "id": "14bcbb50b985",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "OpenAIとAnthropicが2026年夏から秋にかけてLLM料金を相次いで値下げした理由とは？",
  "snippet": "",
  "published": "2026-10-28T21:00:00+00:00"
 },
 {
  "id": "8d2f723694db",
  "region": "jp",
  "source": "innovaTopia",
  "title": "Anthropic、自社で創薬に着手 正社員1人のMithril Medicineを買収し小児の筋ジストロフィー治療薬を研究",
  "snippet": "",
  "published": "2026-10-29T00:10:44+00:00"
 },
 {
  "id": "82fff4c603eb",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claude Enterpriseにスマートレポート、アンケート、共同予算を追加",
  "snippet": "",
  "published": "2026-10-28T19:41:13+00:00"
 },
 {
  "id": "26d74a017946",
  "region": "jp",
  "source": "CNET Japan",
  "title": "Anthropic、1人社長の創薬企業を買収 「Claude」で小児難病の治療研究",
  "snippet": "",
  "published": "2026-10-28T08:40:00+00:00"
 },
 {
  "id": "512f32bd8c4f",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropicのエンジニア責任者、コーディング面接を廃止：Claudeが問題を解けるため、採用はポートフォリオ重視へ",
  "snippet": "",
  "published": "2026-10-28T18:32:00+00:00"
 },
 {
  "id": "b2ce889e7436",
  "region": "jp",
  "source": "SOC Prime",
  "title": "Claude.aiの悪用によるClickFixマルウェアの配信",
  "snippet": "",
  "published": "2026-10-28T14:52:34+00:00"
 },
 {
  "id": "1b5a7fd83a6f",
  "region": "jp",
  "source": "TradingView",
  "title": "Anthropic社、リスクAIモデルの使用差し止め求める",
  "snippet": "",
  "published": "2026-10-28T16:06:18+00:00"
 },
 {
  "id": "68c60f46cd57",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "アンソロピック、AI推奨に専門家の86％が追従する実験を公表 Claude Codeで統計分析（ビジネス＋IT）",
  "snippet": "",
  "published": "2026-10-28T11:30:06+00:00"
 },
 {
  "id": "de61b2e5d18b",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "Anthropicが筋ジストロフィー治療薬開発のMithril Medicine買収を発表、生命科学分野で独自の創薬活動を開始",
  "snippet": "",
  "published": "2026-10-28T09:00:00+00:00"
 },
 {
  "id": "39324165b69c",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Anthropic、Claude Enterprise向けの追跡ツール3種類を一般提供",
  "snippet": "",
  "published": "2026-10-28T11:22:00+00:00"
 },
 {
  "id": "0fbaabcb8e08",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicがIPO株式をRetailBook経由で英国の個人投資家に提供へ 執筆",
  "snippet": "",
  "published": "2026-10-28T17:40:00+00:00"
 },
 {
  "id": "62e13410b101",
  "region": "jp",
  "source": "AIsmiley",
  "title": "Anthropic、ナスダック上場へ。IPOに向け米国証券取引委員会へ登録届出書を提出",
  "snippet": "",
  "published": "2026-10-28T03:43:07+00:00"
 },
 {
  "id": "fb8b2bdf8b94",
  "region": "jp",
  "source": "Moomoo",
  "title": "OpenAI対Anthropic――5つのETFが明かすAIブームの真相",
  "snippet": "",
  "published": "2026-10-28T09:51:06+00:00"
 },
 {
  "id": "394941c29afd",
  "region": "jp",
  "source": "CNET Japan",
  "title": "AI学習でマドンナらの楽曲を不正利用か--AnthropicとSuno、計約530億円の訴訟に直面",
  "snippet": "",
  "published": "2026-10-28T01:20:00+00:00"
 },
 {
  "id": "1ca24a80c9f2",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "Googleが世界一高性能なAI「Gemini 4 Carbon」を発表、ついにOpenAIやAnthropicの最先端モデルを超える",
  "snippet": "",
  "published": "2026-10-29T01:41:00+00:00"
 },
 {
  "id": "6cb3e43e9a38",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "Claude Mythos 5がGitHubに悪意あるコードを送り込み偽アカウントで開発者に圧力をかけた問題の原因をAnthropicが分析",
  "snippet": "",
  "published": "2026-10-28T11:00:00+00:00"
 },
 {
  "id": "3c63d89ba472",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "「エルヴィス・プレスリーの曲がAI学習に無断使用された」と60億円超の損害賠償をAnthropicに求める訴訟が提起される",
  "snippet": "",
  "published": "2026-10-28T07:20:00+00:00"
 },
 {
  "id": "b2d42c78d910",
  "region": "jp",
  "source": "日経クロステック",
  "title": "Anthropicが上場目論見書を公開、従業員1人当たり売上高は10億円超",
  "snippet": "",
  "published": "2026-10-28T02:40:00+00:00"
 },
 {
  "id": "b6ac40f1d956",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropicを支える数字｜The Plain Bagel",
  "snippet": "",
  "published": "2026-10-28T15:50:09+00:00"
 },
 {
  "id": "aeb06ecd4fb4",
  "region": "jp",
  "source": "디지털투데이",
  "title": "Anthropic、企業向けAI支出の可視化ツール公開",
  "snippet": "",
  "published": "2026-10-28T20:45:16+00:00"
 },
 {
  "id": "049a82d4dffd",
  "region": "jp",
  "source": "Korben",
  "title": "AnthropicがMithrilを買収、Claudeで回す「たった一人のバイオ企業」",
  "snippet": "",
  "published": "2026-10-28T17:59:09+00:00"
 },
 {
  "id": "f18ed45fb705",
  "region": "intl",
  "source": "Aswath Damodaran | Substack",
  "title": "TheAnthropic IPO Arrives: My (but not the) Anthropic Valuation!",
  "snippet": "",
  "published": "2026-10-28T18:19:59+00:00"
 },
 {
  "id": "d9a2dddf3793",
  "region": "intl",
  "source": "Reuters",
  "title": "Prediction market bets set the tone for Anthropic's much-awaited IPO",
  "snippet": "",
  "published": "2026-10-28T19:32:07+00:00"
 },
 {
  "id": "dfd3864101f9",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic filed to go public—what retail investors should weigh before its IPO",
  "snippet": "",
  "published": "2026-10-28T19:11:25+00:00"
 },
 {
  "id": "9a8982d92d7a",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Anthropic just launched tools to show companies what their AI spending is buying",
  "snippet": "",
  "published": "2026-10-28T19:19:58+00:00"
 },
 {
  "id": "1ee79686caa7",
  "region": "intl",
  "source": "Anthropic",
  "title": "AI for Science expands to foundations and research institutions",
  "snippet": "",
  "published": "2026-10-28T20:14:19+00:00"
 },
 {
  "id": "ff9a70819a97",
  "region": "intl",
  "source": "Bloomberg",
  "title": "Anthropic Is Spending Millions to Protect Dario Amodei and Employees",
  "snippet": "",
  "published": "2026-10-28T16:47:36+00:00"
 },
 {
  "id": "f60e076ddc84",
  "region": "intl",
  "source": "XDA",
  "title": "I tested the 3 Claude Code alternatives the internet keeps talking about, and only one let me down",
  "snippet": "",
  "published": "2026-10-28T23:00:21+00:00"
 },
 {
  "id": "a04e5d603351",
  "region": "intl",
  "source": "The Washington Post",
  "title": "Opinion | Anthropic’s plan to protect humanity has a flaw",
  "snippet": "",
  "published": "2026-10-29T00:20:28+00:00"
 },
 {
  "id": "0edfd5de6b82",
  "region": "intl",
  "source": "The Register",
  "title": "Anthropic engineer declares the coding interview dead",
  "snippet": "",
  "published": "2026-10-28T20:22:56+00:00"
 },
 {
  "id": "488610f4a3d8",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "What Robinhood's CFO found interesting about Anthropic's IPO prospectus",
  "snippet": "",
  "published": "2026-10-28T22:39:10+00:00"
 },
 {
  "id": "12ef90359b79",
  "region": "intl",
  "source": "The Hacker News",
  "title": "Anthropic's Unreleased AI Model Chains Flaws Into Working Chrome, Safari, Windows and Linux Exploits",
  "snippet": "",
  "published": "2026-10-28T08:15:00+00:00"
 },
 {
  "id": "98b195d3e586",
  "region": "intl",
  "source": "The Profile | Polina Pompliano",
  "title": "Anthropic Bought Mithril, a One-Man Biotech Startup Built by an Anonymous X User",
  "snippet": "",
  "published": "2026-10-28T14:58:02+00:00"
 },
 {
  "id": "077dbdc75a7b",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic IPO filing warns some risks may be uninsurable. AI coverage will be issue for every company",
  "snippet": "",
  "published": "2026-10-28T13:45:36+00:00"
 },
 {
  "id": "e8c61706efad",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic unveils additional Claude tools for lawyers",
  "snippet": "",
  "published": "2026-10-28T16:43:56+00:00"
 },
 {
  "id": "c6488297e44f",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic’s public benefit structure creates unusual risks for IPO investors",
  "snippet": "",
  "published": "2026-10-28T21:48:17+00:00"
 },
 {
  "id": "1b72bc164baa",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic tells California governor courts should be able to block risky AI models",
  "snippet": "",
  "published": "2026-10-28T19:04:22+00:00"
 },
 {
  "id": "0191be1176cf",
  "region": "intl",
  "source": "Reuters",
  "title": "NEWSLETTER: Should you invest in Anthropic? Five takeaways from its S-1",
  "snippet": "",
  "published": "2026-10-28T21:16:00+00:00"
 },
 {
  "id": "49f6e8633a88",
  "region": "intl",
  "source": "Business Insider",
  "title": "Anthropic manager says the 'coding interview is dead' — here's his advice for junior developers",
  "snippet": "",
  "published": "2026-10-28T11:56:00+00:00"
 },
 {
  "id": "092990ed20f5",
  "region": "intl",
  "source": "Spectrum News",
  "title": "Sen. Elizabeth Warren asks Anthropic CEO to address ex­is­tential risks before IPO",
  "snippet": "",
  "published": "2026-10-28T16:59:00+00:00"
 },
 {
  "id": "afbd041e13e3",
  "region": "intl",
  "source": "Quartz",
  "title": "Anthropic acquires one-person biotech Mithril, starts drug programs",
  "snippet": "",
  "published": "2026-10-28T12:50:39+00:00"
 },
 {
  "id": "9372455f0150",
  "region": "intl",
  "source": "The Daily Northwestern",
  "title": "Hosseini: Anthropic’s molecular biology lab shows why AI-directed research needs oversight",
  "snippet": "",
  "published": "2026-10-28T23:55:58+00:00"
 },
 {
  "id": "35b7e9bb9cc8",
  "region": "intl",
  "source": "Artificial Lawyer",
  "title": "Anthropic Increases Legal Vertical Push With ‘Artifacts’",
  "snippet": "",
  "published": "2026-10-28T15:17:39+00:00"
 },
 {
  "id": "3e24159ae79f",
  "region": "intl",
  "source": "Gizmodo",
  "title": "Expert Judgement Can Be Easily Hacked by AI, Anthropic Study Finds",
  "snippet": "",
  "published": "2026-10-28T22:00:50+00:00"
 },
 {
  "id": "90aa0da65708",
  "region": "intl",
  "source": "Bloomberg",
  "title": "Four Unanswered Questions From Anthropic’s IPO Filing",
  "snippet": "",
  "published": "2026-10-28T20:35:08+00:00"
 },
 {
  "id": "f6092a50ebd9",
  "region": "intl",
  "source": "ExecutiveGov",
  "title": "GSA Expands Anthropic OneGov Deal With 40-Percent Claude Token Discount",
  "snippet": "",
  "published": "2026-10-28T21:24:49+00:00"
 },
 {
  "id": "a2eee3452827",
  "region": "intl",
  "source": "claude.com",
  "title": "Introducing artifacts for legal work",
  "snippet": "",
  "published": "2026-10-28T15:30:27+00:00"
 },
 {
  "id": "4ed6186b41c7",
  "region": "intl",
  "source": "claude.com",
  "title": "Smart reports, surveys, and pooled group budgets for Claude Enterprise",
  "snippet": "",
  "published": "2026-10-28T18:01:48+00:00"
 },
 {
  "id": "dcd720a06911",
  "region": "intl",
  "source": "claude.com",
  "title": "Changelog",
  "snippet": "",
  "published": "2026-10-28T01:50:09+00:00"
 },
 {
  "id": "5654d1097793",
  "region": "intl",
  "source": "claude.com",
  "title": "How CodeRabbit, Power Digital, and ThoughtSpot scale with Snowflake and Vercel on Claude Marketplace",
  "snippet": "",
  "published": "2026-10-27T16:00:37+00:00"
 },
 {
  "id": "a225e1a1d91b",
  "region": "intl",
  "source": "claude.com",
  "title": "The founder's playbook: Building an AI-native startup",
  "snippet": "",
  "published": "2026-10-27T15:06:56+00:00"
 },
 {
  "id": "ad24e0d260fd",
  "region": "intl",
  "source": "claude.com",
  "title": "New connectors in Claude for everyday life",
  "snippet": "",
  "published": "2026-10-27T18:57:50+00:00"
 },
 {
  "id": "2d3f65e7b237",
  "region": "intl",
  "source": "claude.com",
  "title": "How Anthropic's cybersecurity team built a threat detection platform with Claude Code",
  "snippet": "",
  "published": "2026-10-28T07:55:56+00:00"
 },
 {
  "id": "310df9abad1c",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "How Claude marks AI-generated content | Claude Help Center",
  "snippet": "",
  "published": "2026-10-28T18:53:26+00:00"
 },
 {
  "id": "35e4a74b423c",
  "region": "intl",
  "source": "claude.com",
  "title": "Wonder connector",
  "snippet": "",
  "published": "2026-10-28T15:48:07+00:00"
 },
 {
  "id": "1f2bdd9f61bf",
  "region": "intl",
  "source": "claude.com",
  "title": "Schwab Advisor Services connector",
  "snippet": "",
  "published": "2026-10-28T06:26:58+00:00"
 },
 {
  "id": "4436218be571",
  "region": "intl",
  "source": "claude.com",
  "title": "Saily connector",
  "snippet": "",
  "published": "2026-10-27T16:49:27+00:00"
 },
 {
  "id": "2135952d415e",
  "region": "intl",
  "source": "claude.com",
  "title": "Embat connector",
  "snippet": "",
  "published": "2026-10-27T18:40:23+00:00"
 },
 {
  "id": "753034add793",
  "region": "intl",
  "source": "claude.com",
  "title": "IDC brings Quanta into Claude and adopts Claude across the company",
  "snippet": "",
  "published": "2026-10-28T17:46:57+00:00"
 },
 {
  "id": "14d47de0ce4b",
  "region": "intl",
  "source": "assets.claude.com",
  "title": "Usage Policy",
  "snippet": "",
  "published": "2026-10-28T07:15:05+00:00"
 },
 {
  "id": "f436b5e1ac0d",
  "region": "intl",
  "source": "claude.com",
  "title": "BillingMart connector",
  "snippet": "",
  "published": "2026-10-27T23:48:46+00:00"
 },
 {
  "id": "c1788ea72c9e",
  "region": "intl",
  "source": "assets.claude.com",
  "title": "Supported Regions Policy",
  "snippet": "",
  "published": "2026-10-28T06:45:00+00:00"
 },
 {
  "id": "9e05847693ad",
  "region": "intl",
  "source": "Anthropic",
  "title": "- Anthropic",
  "snippet": "Anthropic",
  "published": "2026-10-27T20:36:30+00:00"
 }
]
