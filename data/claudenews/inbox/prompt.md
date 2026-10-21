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
  "id": "a3195597c15a",
  "region": "jp",
  "source": "日本経済新聞",
  "title": "Claude Codeで被災者開発 熊本地震で60万人が利用した掲示板サイト",
  "snippet": "",
  "published": "2026-10-20T20:00:00+00:00"
 },
 {
  "id": "64a28d64912f",
  "region": "jp",
  "source": "ライフハッカー",
  "title": "Claude Codeの精度を上げるために、私がCLAUDE.mdで見直したこと",
  "snippet": "",
  "published": "2026-10-21T00:00:00+00:00"
 },
 {
  "id": "9a4a18c03991",
  "region": "jp",
  "source": "infoq.com",
  "title": "AnthropicがClaude封じ込め法を詳説、Web・Claude Code・Coworkに対して",
  "snippet": "",
  "published": "2026-10-20T07:31:37+00:00"
 },
 {
  "id": "e039a20fafd7",
  "region": "jp",
  "source": "AIsmiley",
  "title": "日立、Anthropicのサイバー防衛プログラムに参画。「Claude」活用しセキュリティ強化",
  "snippet": "",
  "published": "2026-10-20T08:55:06+00:00"
 },
 {
  "id": "d06243adf45f",
  "region": "jp",
  "source": "shiritomo",
  "title": "Anthropicの無料脆弱性診断「OSS Scanner」、11日でcurlなど77件検出",
  "snippet": "",
  "published": "2026-10-20T22:30:01+00:00"
 },
 {
  "id": "eb6059e893ee",
  "region": "jp",
  "source": "TradingView",
  "title": "Anthropicの公益基金と他の大規模慈善活動との比較",
  "snippet": "",
  "published": "2026-10-20T18:41:36+00:00"
 },
 {
  "id": "2f32e29601e3",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Anthropicの法案草案、壊滅的リスクを理由にAIモデルの公開を差し止め可能に",
  "snippet": "",
  "published": "2026-10-20T17:38:00+00:00"
 },
 {
  "id": "9618bf6faa9f",
  "region": "jp",
  "source": "Moomoo",
  "title": "Anthropic、史上最大規模のIPOを目指し準備中！将来の計算リソースへの支出は7,500億ドルに達する可能性",
  "snippet": "",
  "published": "2026-10-20T22:39:09+00:00"
 },
 {
  "id": "9dd2630c53b5",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropicの新モデルが露呈、明示されない目標も推論可能に、大規模モデル競争は「意図の読解」へ転換",
  "snippet": "",
  "published": "2026-10-20T18:19:00+00:00"
 },
 {
  "id": "0a8405bb847c",
  "region": "jp",
  "source": "innovaTopia",
  "title": "OpenAI、Anthropic上場前に300億ドル調達を急ぐと報道 企業価値1.4兆ドル超",
  "snippet": "",
  "published": "2026-10-20T23:03:06+00:00"
 },
 {
  "id": "537e85f028ad",
  "region": "jp",
  "source": "Morningstar",
  "title": "Here’s How Anthropic and OpenAI Are Building Economic Moats | モーニングスター",
  "snippet": "",
  "published": "2026-10-20T08:06:25+00:00"
 },
 {
  "id": "7222aa5c29cf",
  "region": "jp",
  "source": "Reuters",
  "title": "Why OpenAI is racing to raise funds ahead of Anthropic IPO",
  "snippet": "",
  "published": "2026-10-20T13:29:16+00:00"
 },
 {
  "id": "9bfdb5c82a60",
  "region": "jp",
  "source": "TIKR.com",
  "title": "Trump’s FTC Subpoenas OpenAI and Anthropic. Inside the $500 Billion Threat Faced by Microsoft, Amazon, and Google",
  "snippet": "",
  "published": "2026-10-20T18:22:30+00:00"
 },
 {
  "id": "c8e5fb48cab8",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicがNscaleと第2の数十億ドル規模の契約交渉中――CNBC 執筆",
  "snippet": "",
  "published": "2026-10-20T14:24:00+00:00"
 },
 {
  "id": "3574263aed0d",
  "region": "jp",
  "source": "Yellow.com",
  "title": "AnthropicのIPO目前、OpenAIが時価総額1.4兆ドル超えを狙い300億ドル調達へ加速",
  "snippet": "",
  "published": "2026-10-20T16:49:02+00:00"
 },
 {
  "id": "5c376025f047",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Anthropicのクラウド契約、複雑さ増す",
  "snippet": "",
  "published": "2026-10-20T16:00:00+00:00"
 },
 {
  "id": "64262826b209",
  "region": "jp",
  "source": "TradingView",
  "title": "Anthropic、26年上半期に800億ドル超の純損失＝WSJ報道",
  "snippet": "",
  "published": "2026-10-20T20:01:08+00:00"
 },
 {
  "id": "f3c616dd6089",
  "region": "jp",
  "source": "CodeZine",
  "title": "AnthropicやOpenAIらが登壇、GMO Flatt Securityがプロダクトセキュリティイベントを12月3日に開催",
  "snippet": "",
  "published": "2026-10-20T04:30:00+00:00"
 },
 {
  "id": "fb41c0ad905c",
  "region": "jp",
  "source": "remio",
  "title": "AnthropicのAI期待値調査、従業員と一般市民の間に52ポイントの隔たり",
  "snippet": "",
  "published": "2026-10-20T06:55:23+00:00"
 },
 {
  "id": "e49a4cbdd57b",
  "region": "jp",
  "source": "ニュースメディアVOIX",
  "title": "malna株式会社がAnthropic社の「Claude Partner Network」に参加しAI活用を加速する取り組み",
  "snippet": "",
  "published": "2026-10-20T05:24:59+00:00"
 },
 {
  "id": "3718b27caa54",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Anthropic、AIモデルの停止は被害10億ドル超か死者50人超に限る法案を提案",
  "snippet": "",
  "published": "2026-10-20T08:02:38+00:00"
 },
 {
  "id": "36c4e6e4b5f9",
  "region": "jp",
  "source": "ASCII.jp",
  "title": "GMO Flatt Security、Anthropic社・OpenAI社ら4社を招いたセキュリティイベント「Product Security Square #6」を12月3日に開催",
  "snippet": "",
  "published": "2026-10-20T08:37:30+00:00"
 },
 {
  "id": "e836bbb9ac05",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "近年最悪級のcurl脆弱性も発見 無料でClaude Mythosが検査する『OSS Scanner』、11日間で緊急・重要880件をAI判定",
  "snippet": "",
  "published": "2026-10-20T02:30:03+00:00"
 },
 {
  "id": "ab543154bdd6",
  "region": "jp",
  "source": "PR TIMES",
  "title": "「Claude Code実践講座」や企業の最新事例を紹介！下半期最大級*¹のDX・AX総合展「Japan DX ＆ AX Week【秋】」内で、オープンセミナー・カンファレンスを開催",
  "snippet": "",
  "published": "2026-10-20T01:50:01+00:00"
 },
 {
  "id": "c2ccdd62ccb3",
  "region": "jp",
  "source": "毎日新聞",
  "title": "プレスリリース：Anthropic社の「Claude Partner Network」に参画しました（PR TIMES）",
  "snippet": "",
  "published": "2026-10-20T00:22:37+00:00"
 },
 {
  "id": "25bbcf8ef0cc",
  "region": "intl",
  "source": "Anthropic",
  "title": "How Claude designed protein binders against scorpion neurotoxins",
  "snippet": "",
  "published": "2026-10-20T17:03:55+00:00"
 },
 {
  "id": "32cb40a89513",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic logged net loss of over $80 billion in first half of 2026, WSJ reports",
  "snippet": "",
  "published": "2026-10-20T22:14:51+00:00"
 },
 {
  "id": "7f15869bad49",
  "region": "intl",
  "source": "WSJ",
  "title": "Exclusive | Anthropic S-1 Shows Red-Hot Growth, Risks and Massive Computing Costs",
  "snippet": "",
  "published": "2026-10-20T19:30:00+00:00"
 },
 {
  "id": "1f4fe990ca19",
  "region": "intl",
  "source": "New York Post",
  "title": "Anthropic books colossal $81B loss, warns of data center backlash as Amodei siblings draw modest salaries",
  "snippet": "",
  "published": "2026-10-20T22:06:00+00:00"
 },
 {
  "id": "578ee2037df0",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic in talks with neocloud Nscale over second multibillion-dollar deal, source tells CNBC",
  "snippet": "",
  "published": "2026-10-20T14:12:38+00:00"
 },
 {
  "id": "6c0ca94034e3",
  "region": "intl",
  "source": "Investing.com",
  "title": "Anthropic revenue hits $16.3 billion as preliminary S-1 outlines IPO risks - WSJ",
  "snippet": "",
  "published": "2026-10-20T22:05:02+00:00"
 },
 {
  "id": "201673e4b92b",
  "region": "intl",
  "source": "The Motley Fool",
  "title": "Anthropic Is in Talks for Another $45 Billion AI Deal. Nvidia Could Be a Big Winner.",
  "snippet": "",
  "published": "2026-10-20T20:24:00+00:00"
 },
 {
  "id": "d417c130eede",
  "region": "intl",
  "source": "FedScoop",
  "title": "HHS to make sole-source award to Anthropic ahead of broader AI competition",
  "snippet": "",
  "published": "2026-10-20T23:12:13+00:00"
 },
 {
  "id": "ced92267ba03",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic Will Be The Last AI IPO Of 2026, As Industry Collapses",
  "snippet": "",
  "published": "2026-10-20T13:55:20+00:00"
 },
 {
  "id": "e2f967164c47",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Anthropic’s cloud partnerships are getting messy",
  "snippet": "",
  "published": "2026-10-20T21:25:22+00:00"
 },
 {
  "id": "0fa793efd596",
  "region": "intl",
  "source": "Barron's",
  "title": "Why Anthropic’s IPO Faces a Test That Goes Beyond Its Price Tag",
  "snippet": "",
  "published": "2026-10-20T20:12:00+00:00"
 },
 {
  "id": "45f62c8c1c25",
  "region": "intl",
  "source": "Gartner",
  "title": "First Take: Anthropic’s Claude Convergence Makes Shadow AI Harder to Contain",
  "snippet": "",
  "published": "2026-10-20T20:59:19+00:00"
 },
 {
  "id": "437d5ff72259",
  "region": "intl",
  "source": "South China Morning Post",
  "title": "Why Anthropic has a major China problem ahead of its blockbuster IPO",
  "snippet": "",
  "published": "2026-10-21T00:00:15+00:00"
 },
 {
  "id": "668c2eadedb7",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic May Spend $750 Billion on Computing Costs, Report Says",
  "snippet": "",
  "published": "2026-10-20T20:04:21+00:00"
 },
 {
  "id": "dc60b8edd3a2",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Anthropic pitches AI safety bill that may block a model if 50+ people could be killed",
  "snippet": "",
  "published": "2026-10-20T23:01:23+00:00"
 },
 {
  "id": "7493b4b44123",
  "region": "intl",
  "source": "The Motley Fool",
  "title": "Anthropic Is Targeting an IPO as Soon as Mid-November",
  "snippet": "",
  "published": "2026-10-21T00:17:44+00:00"
 },
 {
  "id": "85d412667f41",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Eric Schmidt reportedly owns about half as much of Anthropic as CEO Dario Amodei",
  "snippet": "",
  "published": "2026-10-20T17:55:12+00:00"
 },
 {
  "id": "1cbe0d9d8297",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic May Spend $750 Billion on Computing Costs, WSJ Reports",
  "snippet": "",
  "published": "2026-10-20T21:35:01+00:00"
 },
 {
  "id": "a92307f04fa0",
  "region": "intl",
  "source": "New York Post",
  "title": "Investors eagerly await key Anthropic filing to see blockbuster IPO will stoke demand",
  "snippet": "",
  "published": "2026-10-20T23:19:00+00:00"
 },
 {
  "id": "e3ef74bd562c",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Watch Nscale Anthropic in AI Computing Talks",
  "snippet": "",
  "published": "2026-10-20T20:30:37+00:00"
 },
 {
  "id": "69f645647c27",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic had $16.3 billion in revenue during first half of 2026: WSJ",
  "snippet": "",
  "published": "2026-10-20T19:54:00+00:00"
 },
 {
  "id": "dff34d99f184",
  "region": "intl",
  "source": "EdTech Innovation Hub",
  "title": "Anthropic pledges 5% of shares to public benefit fund | ETIH EdTech News",
  "snippet": "",
  "published": "2026-10-20T23:17:09+00:00"
 },
 {
  "id": "c51d697c324f",
  "region": "intl",
  "source": "Benzinga",
  "title": "Anthropic Lost $80 Billion in Six Months as AI Spending Soars, Draft IPO Filing Shows",
  "snippet": "",
  "published": "2026-10-20T21:52:39+00:00"
 },
 {
  "id": "f982978f5266",
  "region": "intl",
  "source": "Financial Times",
  "title": "Submit a question: Could Anthropic’s IPO be a turning point for AI?",
  "snippet": "",
  "published": "2026-10-20T20:57:44+00:00"
 },
 {
  "id": "1d6ef55a331d",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Market Chatter: Anthropic First-Half Revenue Hits $16.3 Billion",
  "snippet": "",
  "published": "2026-10-20T20:11:08+00:00"
 },
 {
  "id": "85cd0a17cb21",
  "region": "intl",
  "source": "Anthropic",
  "title": "Announcements",
  "snippet": "",
  "published": "2026-10-20T17:03:24+00:00"
 },
 {
  "id": "01572fe590cf",
  "region": "intl",
  "source": "Anthropic",
  "title": "De novo design of protein binders against scorpion toxins with Claude",
  "snippet": "",
  "published": "2026-10-20T14:40:42+00:00"
 },
 {
  "id": "9be6a40d86e1",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Claude for nonprofits",
  "snippet": "",
  "published": "2026-10-20T15:11:21+00:00"
 },
 {
  "id": "988c6f512dca",
  "region": "intl",
  "source": "Anthropic",
  "title": "Using Claude to reduce the attack surface of code",
  "snippet": "",
  "published": "2026-10-20T21:43:55+00:00"
 },
 {
  "id": "f31670bcd1b2",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Turn on data retention for a Workspace in a zero data retention organization",
  "snippet": "",
  "published": "2026-10-19T20:13:06+00:00"
 },
 {
  "id": "c69af5adc0a0",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Understanding your Claude API invoices",
  "snippet": "",
  "published": "2026-10-19T20:39:09+00:00"
 },
 {
  "id": "6b19084607b8",
  "region": "intl",
  "source": "claude.com",
  "title": "Asana Claude Managed Agents case study",
  "snippet": "",
  "published": "2026-10-20T20:49:50+00:00"
 },
 {
  "id": "eb62cc83d8b5",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Claude Design admin guide for Team and Enterprise plans",
  "snippet": "",
  "published": "2026-10-19T17:15:43+00:00"
 },
 {
  "id": "5e9eaf84e85c",
  "region": "intl",
  "source": "claude.com",
  "title": "The AI-native SDLC playbook",
  "snippet": "",
  "published": "2026-10-19T18:06:14+00:00"
 },
 {
  "id": "beaf29a53690",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Restrict verified-domain connectors to your Enterprise",
  "snippet": "",
  "published": "2026-10-20T22:11:56+00:00"
 },
 {
  "id": "0c8658ab7578",
  "region": "intl",
  "source": "claude.com",
  "title": "aws-agents",
  "snippet": "",
  "published": "2026-10-19T21:24:27+00:00"
 },
 {
  "id": "c805577f04c3",
  "region": "intl",
  "source": "claude.com",
  "title": "UKG Bryte connector",
  "snippet": "",
  "published": "2026-10-20T00:58:13+00:00"
 },
 {
  "id": "9584374ffbcd",
  "region": "intl",
  "source": "claude.com",
  "title": "Foreword - Claude for the legal industry",
  "snippet": "",
  "published": "2026-10-20T20:30:24+00:00"
 },
 {
  "id": "82e22fd5ed9c",
  "region": "intl",
  "source": "claude.com",
  "title": "Compliance API coverage extends to Claude Cowork and Claude Code",
  "snippet": "",
  "published": "2026-10-20T10:03:34+00:00"
 },
 {
  "id": "da1b00039207",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp",
  "snippet": "",
  "published": "2026-10-19T22:19:51+00:00"
 },
 {
  "id": "bf5d07fd8d91",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Find and join a Console organization",
  "snippet": "",
  "published": "2026-10-19T20:47:23+00:00"
 },
 {
  "id": "3c4088ce24be",
  "region": "intl",
  "source": "claude.com",
  "title": "AnythingMCP connector",
  "snippet": "",
  "published": "2026-10-20T01:34:36+00:00"
 },
 {
  "id": "407da76df55f",
  "region": "intl",
  "source": "Claude Platform",
  "title": "User Preferences",
  "snippet": "",
  "published": "2026-10-20T15:56:18+00:00"
 },
 {
  "id": "fb392d2731ea",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Refine Claude's work through memory and instructions · Introduction to Claude Tag",
  "snippet": "",
  "published": "2026-10-19T15:43:32+00:00"
 },
 {
  "id": "86e2c1518aa1",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Claude Academy",
  "snippet": "",
  "published": "2026-10-19T23:01:18+00:00"
 },
 {
  "id": "99b7c561b1a8",
  "region": "intl",
  "source": "Anthropic",
  "title": "- Anthropic",
  "snippet": "Anthropic",
  "published": "2026-10-20T22:08:14+00:00"
 },
 {
  "id": "d48a46ffc5b7",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.305",
  "snippet": "What's changed Added sandbox.allowNestedUserNamespaces so sandboxed commands on Linux can create user namespaces (Chromium, rootless podman); this lets them get around the sandbox's file protections Added CLAUDE_CODE_RETRY_WATCHDOG_USAGE_LIMIT_RECHECK_MS so unattended retry mode ( CLAUDE_CODE_RETRY_WATCHDOG ) notices a usage limit that was lifted before its reset Fixed every request failing on Vertex, Bedrock and other providers when the endpoint or a gateway rejects tool search, and behind gateways with ToolSearch disallowed or left out of --tools (a 2.1.304 regression): Claude Code now retri…",
  "published": "2026-10-20T20:46:50+00:00"
 }
]
