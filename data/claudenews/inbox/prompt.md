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
  "id": "111560f1b1c2",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Anthropicが「AIに何を求めるか」調査を再開、インタビューは公開も選べる",
  "snippet": "",
  "published": "2026-10-06T19:08:39+00:00"
 },
 {
  "id": "a0414ef6474e",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Anthropic、「Claude for Google Workspace」アドオンをリリース（窓の杜）",
  "snippet": "",
  "published": "2026-10-06T22:05:00+00:00"
 },
 {
  "id": "309ed56dc7ee",
  "region": "jp",
  "source": "キーマンズネット",
  "title": "Claude Codeに「仕事を丸投げ」して事故らないための基本運用ルール",
  "snippet": "",
  "published": "2026-10-06T22:00:00+00:00"
 },
 {
  "id": "0728136eabdb",
  "region": "jp",
  "source": "Ledge.ai",
  "title": "Anthropicの自社活用事例、Claudeが購入相談を24時間対応 商談化率2倍超、営業は顧客との対話に集中",
  "snippet": "",
  "published": "2026-10-07T00:54:28+00:00"
 },
 {
  "id": "4a233fd16a0e",
  "region": "jp",
  "source": "マイナビニュース",
  "title": "OpenAIとAnthropic、AIサブスクの利用上限を見直し - 背景に推論コスト",
  "snippet": "",
  "published": "2026-10-07T00:30:12+00:00"
 },
 {
  "id": "138b5eb86d30",
  "region": "jp",
  "source": "PR TIMES",
  "title": "AIの使い方は「プロンプト」から「スキル」へ──OpenAI・Anthropic・Microsoftが相次ぎ対応する“AIスキル”を、ブラウザに貼るだけで試せる「スブリ」無料公開",
  "snippet": "",
  "published": "2026-10-07T01:00:02+00:00"
 },
 {
  "id": "6da7feb85c7e",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "Googleドキュメント・スプレッドシート・スライドにClaude統合 Anthropicがアドオン公開",
  "snippet": "",
  "published": "2026-10-06T23:48:00+00:00"
 },
 {
  "id": "8bfa0feddb2d",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、審査済みサイバー防衛担当者に最上位AIモデルへのアクセスを拡大",
  "snippet": "",
  "published": "2026-10-06T22:25:00+00:00"
 },
 {
  "id": "cb9c48f386d4",
  "region": "jp",
  "source": "innovaTopia",
  "title": "Anthropic、CVPを3段階に拡張しGlasswingと統合｜防御側にMythos 5.1も",
  "snippet": "",
  "published": "2026-10-07T00:35:19+00:00"
 },
 {
  "id": "263c333cea31",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Claude AI Assistant が Google Workspace にパブリックベータとして登場",
  "snippet": "",
  "published": "2026-10-06T20:06:43+00:00"
 },
 {
  "id": "a2c4252bac53",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "Claudeを日記として使用した女性がAnthropicに内容を通報されて逮捕される",
  "snippet": "",
  "published": "2026-10-06T02:40:00+00:00"
 },
 {
  "id": "d4c2306aa2ac",
  "region": "jp",
  "source": "Investing.com 日本",
  "title": "AnthropicがGoogle WorkspaceアプリにClaude統合機能を追加 執筆",
  "snippet": "",
  "published": "2026-10-06T18:08:00+00:00"
 },
 {
  "id": "477b3912b72e",
  "region": "jp",
  "source": "Chosunbiz",
  "title": "Anthropicがグラスウィング統合し3段階アクセス導入 - CHOSUNBIZ",
  "snippet": "",
  "published": "2026-10-07T00:49:00+00:00"
 },
 {
  "id": "a742155a19dc",
  "region": "jp",
  "source": "CREATIVE VILLAGE",
  "title": "【アーカイブ録画配信】Claude Codeって、私にも使える？ ～AIを仕事に活かしたい人のための超入門～",
  "snippet": "",
  "published": "2026-10-06T06:43:29+00:00"
 },
 {
  "id": "87819b22dd78",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropicがサイバー検証プログラムを3つのアクセスティアに拡大",
  "snippet": "",
  "published": "2026-10-06T19:16:17+00:00"
 },
 {
  "id": "093dacf06e82",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "アクセンチュアとAnthropicがAIの安全性評価を行う「組み込み型評価者」チーム設立へ提携",
  "snippet": "",
  "published": "2026-10-06T23:19:32+00:00"
 },
 {
  "id": "cdf7a08cea61",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claudeスタートアッププログラムを新たな創業者特典で拡大",
  "snippet": "",
  "published": "2026-10-06T16:41:33+00:00"
 },
 {
  "id": "9f9d8eb95186",
  "region": "jp",
  "source": "디지털투데이",
  "title": "Anthropic、スタートアップ支援拡充 Claude Teamを1年無償提供",
  "snippet": "",
  "published": "2026-10-06T21:31:48+00:00"
 },
 {
  "id": "c18905ca780e",
  "region": "jp",
  "source": "디지털투데이",
  "title": "Anthropic、サイバー検証制度を再編 全参加者に「Mythos」の限定提供を拡大",
  "snippet": "",
  "published": "2026-10-06T23:11:49+00:00"
 },
 {
  "id": "8cb9690c7c6c",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "ヒューバーマン氏：メタ、OpenAI、Anthropicはすべてバイオテック企業になる",
  "snippet": "",
  "published": "2026-10-06T13:08:00+00:00"
 },
 {
  "id": "60420d525525",
  "region": "jp",
  "source": "Reuters",
  "title": "Australia vs rogue AI agents: Anthropic says it's open to tougher laws",
  "snippet": "",
  "published": "2026-10-06T10:56:59+00:00"
 },
 {
  "id": "265f69b74455",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "OpenAIとAnthropicは、オーストラリアにおける厳格なインシデント報告法を支持しています。",
  "snippet": "",
  "published": "2026-10-06T12:18:48+00:00"
 },
 {
  "id": "ac4f1f72f9f6",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "米AI企業AnthropicのアモデイCEO、報酬1800万ドルはテック業界で中位水準—2兆ドルIPO目前",
  "snippet": "",
  "published": "2026-10-06T10:35:00+00:00"
 },
 {
  "id": "c50776101d8e",
  "region": "jp",
  "source": "PR TIMES",
  "title": "NEC、Anthropicおよび金融機関との連携プログラムにおいて第1回勉強会を開催",
  "snippet": "",
  "published": "2026-10-06T02:00:02+00:00"
 },
 {
  "id": "b739ff13fb6e",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Claude Startups、Anthropicが1年間のClaude Team無料提供と1,000ドル分のクレジットを発表",
  "snippet": "",
  "published": "2026-10-06T18:44:33+00:00"
 },
 {
  "id": "7bac2222620d",
  "region": "intl",
  "source": "Anthropic",
  "title": "Expanding the Cyber Verification Program",
  "snippet": "",
  "published": "2026-10-06T19:00:00+00:00"
 },
 {
  "id": "713dc795886d",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic opens its most powerful AI models to more security teams",
  "snippet": "",
  "published": "2026-10-06T20:37:46+00:00"
 },
 {
  "id": "8409fe50eb1b",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic expands Claude Startups program in bid to snag founders and fast-growing companies",
  "snippet": "",
  "published": "2026-10-06T16:00:28+00:00"
 },
 {
  "id": "c9d7416dd385",
  "region": "intl",
  "source": "New York Post",
  "title": "Here’s how much Anthropic CEO Dario Amodei and his sister made last year",
  "snippet": "",
  "published": "2026-10-06T21:12:45+00:00"
 },
 {
  "id": "a9f14232f5e7",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Anthropic is giving startups a free year of Claude Team and $1,000 in credits",
  "snippet": "",
  "published": "2026-10-06T16:00:00+00:00"
 },
 {
  "id": "26fae76d5693",
  "region": "intl",
  "source": "The New York Times",
  "title": "A New Open-Weight Challenger to Anthropic, Reflection, Emerges",
  "snippet": "",
  "published": "2026-10-06T12:04:55+00:00"
 },
 {
  "id": "f06ab8b3bc33",
  "region": "intl",
  "source": "The Register",
  "title": "Anthropic Claude subscription plan provides more value than OpenAI's, study says",
  "snippet": "",
  "published": "2026-10-06T21:11:38+00:00"
 },
 {
  "id": "1b7d4e0f60de",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "OpenAI and Anthropic Face Rising Price Pressure From Big AI Users",
  "snippet": "",
  "published": "2026-10-07T00:33:40+00:00"
 },
 {
  "id": "f6f0837f0348",
  "region": "intl",
  "source": "Business Insider",
  "title": "The Anthropic researcher whose resignation made waves last month says he was 'working to automate' himself",
  "snippet": "",
  "published": "2026-10-06T17:29:00+00:00"
 },
 {
  "id": "f0d21cdc9b98",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Anthropic Expands Discounts and Support for Founders",
  "snippet": "",
  "published": "2026-10-06T22:02:04+00:00"
 },
 {
  "id": "7be96bacfa21",
  "region": "intl",
  "source": "SiliconANGLE",
  "title": "Anthropic folds Project Glasswing into an expanded three-tier Cyber Verification Program",
  "snippet": "",
  "published": "2026-10-06T22:46:00+00:00"
 },
 {
  "id": "b4997f9b5429",
  "region": "intl",
  "source": "The San Francisco Standard",
  "title": "Landlord sues Physical Intelligence to clear space for Anthropic",
  "snippet": "",
  "published": "2026-10-06T19:36:37+00:00"
 },
 {
  "id": "8d0c71415533",
  "region": "intl",
  "source": "TheStreet",
  "title": "Meta and Microsoft just sent employees a memo about Anthropic",
  "snippet": "",
  "published": "2026-10-06T21:43:15+00:00"
 },
 {
  "id": "3583939fd21c",
  "region": "intl",
  "source": "The Motley Fool",
  "title": "Anthropic Could Beat OpenAI to Wall Street by Over a Year",
  "snippet": "",
  "published": "2026-10-06T20:12:00+00:00"
 },
 {
  "id": "2ef4794e7446",
  "region": "intl",
  "source": "Quartz",
  "title": "Anthropic expands cyber AI access program to more security firms",
  "snippet": "",
  "published": "2026-10-06T20:12:23+00:00"
 },
 {
  "id": "18346f093f62",
  "region": "intl",
  "source": "Reuters",
  "title": "EXCLUSIVE: Anthropic's Amodei made $18 million last year, middle of the tech CEO pack",
  "snippet": "",
  "published": "2026-10-06T13:46:00+00:00"
 },
 {
  "id": "40a96338860e",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic Expands Access to Latest AI Models for Cyber Firms",
  "snippet": "",
  "published": "2026-10-06T18:58:42+00:00"
 },
 {
  "id": "65fbd842bebf",
  "region": "intl",
  "source": "Quartz",
  "title": "Anthropic's IPO filing shows CEO Dario Amodei earned $18 million last year",
  "snippet": "",
  "published": "2026-10-06T13:05:44+00:00"
 },
 {
  "id": "16d934182e6a",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "JPMorgan CEO Dimon Says Anthropic’s Mythos Pushed Cyber Risk Up 10-Fold",
  "snippet": "",
  "published": "2026-10-06T13:41:39+00:00"
 },
 {
  "id": "ce78ff013132",
  "region": "intl",
  "source": "The Motley Fool",
  "title": "Anthropic Is Aiming for the Biggest IPO Ever -- Here's the Chip Stock to Buy Before It Lists",
  "snippet": "",
  "published": "2026-10-06T08:47:00+00:00"
 },
 {
  "id": "927a045802cd",
  "region": "intl",
  "source": "MeriTalk",
  "title": "DOD Halts Use of Anthropic AI After Court Upholds Supply Chain Risk Designation",
  "snippet": "",
  "published": "2026-10-06T20:17:49+00:00"
 },
 {
  "id": "b499e6dd58fb",
  "region": "intl",
  "source": "Benzinga",
  "title": "Anthropic Expands Claude Into Google Workspace With New AI Tools",
  "snippet": "",
  "published": "2026-10-06T21:24:45+00:00"
 },
 {
  "id": "4d42d58e70f7",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic Pushes Its IPO to November as Investors Eye a $2 Trillion Valuation",
  "snippet": "",
  "published": "2026-10-06T21:20:00+00:00"
 },
 {
  "id": "31a5a50409c8",
  "region": "intl",
  "source": "The Register",
  "title": "Anthropic reconfigures its cool kids security program",
  "snippet": "",
  "published": "2026-10-06T23:29:27+00:00"
 },
 {
  "id": "21f965358118",
  "region": "intl",
  "source": "Quartz",
  "title": "Anthropic expands Claude Startups program with credits and perks",
  "snippet": "",
  "published": "2026-10-06T16:35:48+00:00"
 },
 {
  "id": "f39f492e996a",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude now works with Google Docs, Sheets, and Slides",
  "snippet": "",
  "published": "2026-10-06T17:09:56+00:00"
 },
 {
  "id": "f51af5473d21",
  "region": "intl",
  "source": "claude.com",
  "title": "We’re expanding the Claude Startups program to help founders build",
  "snippet": "",
  "published": "2026-10-06T16:35:28+00:00"
 },
 {
  "id": "bd3489517465",
  "region": "intl",
  "source": "claude.com",
  "title": "The AI-native SDLC playbook",
  "snippet": "",
  "published": "2026-10-06T13:56:02+00:00"
 },
 {
  "id": "527315cee87c",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Cyber Verification Program | Claude Help Center",
  "snippet": "",
  "published": "2026-10-06T21:29:40+00:00"
 },
 {
  "id": "87bc45a6f8d0",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Sign in",
  "snippet": "",
  "published": "2026-10-06T16:13:18+00:00"
 },
 {
  "id": "20a91abe9147",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Assign a program to workspaces in Claude Console",
  "snippet": "",
  "published": "2026-10-06T18:54:51+00:00"
 },
 {
  "id": "52e36c96a349",
  "region": "intl",
  "source": "claude.com",
  "title": "Building your first workflow with Cowork",
  "snippet": "",
  "published": "2026-10-06T17:46:42+00:00"
 },
 {
  "id": "d60f63813c09",
  "region": "intl",
  "source": "claude.com",
  "title": "Projects redesigned: from folder to conversation",
  "snippet": "",
  "published": "2026-10-06T15:07:48+00:00"
 },
 {
  "id": "000a1c07889e",
  "region": "intl",
  "source": "code.claude.com",
  "title": "Create a Claude Code plugin",
  "snippet": "",
  "published": "2026-10-06T08:28:27+00:00"
 },
 {
  "id": "992b9c19f35e",
  "region": "intl",
  "source": "Anthropic",
  "title": "Ship Code Faster with Claude Code on Vertex AI",
  "snippet": "",
  "published": "2026-10-06T14:52:32+00:00"
 },
 {
  "id": "9bba6e19064c",
  "region": "intl",
  "source": "Anthropic",
  "title": "What We Shipped: Feature Updates, Tips, and Live Q&A with the Claude Code Team",
  "snippet": "",
  "published": "2026-10-06T13:51:15+00:00"
 },
 {
  "id": "b43aa9e1fc46",
  "region": "intl",
  "source": "Anthropic",
  "title": "Claude on Google Cloud: Monitoring and Securing Agents at Scale",
  "snippet": "",
  "published": "2026-10-06T16:51:44+00:00"
 },
 {
  "id": "96fd34fa62db",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Cyber Verification Program Security Requirements",
  "snippet": "",
  "published": "2026-10-06T18:54:52+00:00"
 },
 {
  "id": "9ec456bb92a9",
  "region": "intl",
  "source": "claude.com",
  "title": "Cowork and plugins for teams across the enterprise",
  "snippet": "",
  "published": "2026-10-06T14:27:03+00:00"
 },
 {
  "id": "af4060efadc6",
  "region": "intl",
  "source": "claude.com",
  "title": "Auto mode for Claude Code",
  "snippet": "",
  "published": "2026-10-06T14:34:06+00:00"
 },
 {
  "id": "1125f19bf1ba",
  "region": "intl",
  "source": "claude.com",
  "title": "Building Commerce Agents with Claude",
  "snippet": "",
  "published": "2026-10-06T15:37:45+00:00"
 },
 {
  "id": "27b6283a0ff1",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Government is now generally available",
  "snippet": "",
  "published": "2026-10-06T13:56:43+00:00"
 },
 {
  "id": "f5e50811470b",
  "region": "intl",
  "source": "Anthropic",
  "title": "How to control costs and show ROI for Claude Code on Google Cloud",
  "snippet": "",
  "published": "2026-10-06T13:52:16+00:00"
 },
 {
  "id": "ffafd970aaa9",
  "region": "intl",
  "source": "claude.com",
  "title": "Financial services",
  "snippet": "",
  "published": "2026-10-06T04:18:52+00:00"
 },
 {
  "id": "78f5536874e2",
  "region": "intl",
  "source": "claude.com",
  "title": "Connectors and plugins",
  "snippet": "",
  "published": "2026-10-06T10:35:03+00:00"
 },
 {
  "id": "e84174d622fa",
  "region": "intl",
  "source": "claude.com",
  "title": "Inside Claude for Financial Advisors",
  "snippet": "",
  "published": "2026-10-06T20:25:30+00:00"
 },
 {
  "id": "87ebabde2d13",
  "region": "intl",
  "source": "claude.com",
  "title": "Cowork and plugins for finance",
  "snippet": "",
  "published": "2026-10-06T18:22:30+00:00"
 },
 {
  "id": "66257c47dc9b",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Assign a program to custom roles on Enterprise plans",
  "snippet": "",
  "published": "2026-10-06T18:54:51+00:00"
 },
 {
  "id": "32b69cb2a5d3",
  "region": "intl",
  "source": "claude.com",
  "title": "Guides",
  "snippet": "",
  "published": "2026-10-06T13:30:38+00:00"
 },
 {
  "id": "165f5cf30fa6",
  "region": "intl",
  "source": "claude.com",
  "title": "Annonces produits",
  "snippet": "",
  "published": "2026-10-06T13:55:47+00:00"
 },
 {
  "id": "f465f4e38540",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.292",
  "snippet": "What's changed Added --marketplace <source> to claude plugin install : adds the marketplace if needed, under the same policy checks as claude plugin marketplace add , then installs the plugin from it Added an effort parameter to the Agent tool, so Claude runs a sub-agent at the effort level you ask for Added CLAUDE_CODE_OVERLOADED_RETRY_BASE_DELAY_MS environment variable to set a longer base delay for the backoff when retrying an overloaded (529) request Added prompt.autocomplete , an event a mod hooks to add its own rows to the prompt box's autocomplete list Added prompt caching to $.model.co…",
  "published": "2026-10-06T18:59:30+00:00"
 },
 {
  "id": "31ce016c9399",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.291",
  "snippet": "What's changed Fixed a regression in 2.1.290 where cloud sessions could drop answers to permission prompts Fixed a regression in 2.1.288 where the last messages of a session could be lost when quitting",
  "published": "2026-10-06T03:55:19+00:00"
 }
]
