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
  "id": "cb105a08acd0",
  "region": "jp",
  "source": "マイナビニュース",
  "title": "Anthropic、能動型AIエージェント「Claude Duet」発表 Meta「Muse」と競合",
  "snippet": "",
  "published": "2026-10-21T23:02:04+00:00"
 },
 {
  "id": "3f6571e0dd5b",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "テレビ所有者がClaude Codeで広告と追跡ソフトを除去",
  "snippet": "",
  "published": "2026-10-21T18:19:00+00:00"
 },
 {
  "id": "9f810faaff0f",
  "region": "jp",
  "source": "ビジネス+IT",
  "title": "米Anthropic、2026年上半期の売上高は約163億ドルに急増も、807億ドルの巨額赤字計上",
  "snippet": "",
  "published": "2026-10-21T10:00:00+00:00"
 },
 {
  "id": "a82e3a06b062",
  "region": "jp",
  "source": "innovaTopia",
  "title": "Anthropic「Claude Duet」公開、自分から連絡し送信や支払いは承認制のAIエージェント",
  "snippet": "",
  "published": "2026-10-21T22:15:18+00:00"
 },
 {
  "id": "6176b2560b37",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "Anthropic社による、AIに「餌を与える」ための書籍収集キャンペーン。",
  "snippet": "",
  "published": "2026-10-21T23:36:46+00:00"
 },
 {
  "id": "ab699cf5914b",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、米国のProおよびMaxユーザー向けにClaude Duetのリサーチプレビューを開始",
  "snippet": "",
  "published": "2026-10-21T19:28:50+00:00"
 },
 {
  "id": "d0ec9d046226",
  "region": "jp",
  "source": "TradingView",
  "title": "Anthropic、AIエージェントアプリ「Claude Duet」を発表",
  "snippet": "",
  "published": "2026-10-21T20:17:51+00:00"
 },
 {
  "id": "5858019945a1",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "Claudeが「指示待ち」から自律行動へ：Anthropic、新AIエージェント「Duet」を発表",
  "snippet": "",
  "published": "2026-10-21T20:46:34+00:00"
 },
 {
  "id": "be88c9899460",
  "region": "jp",
  "source": "Ledge.ai",
  "title": "Anthropic、METRの6人に「社員並み」の社内アクセス AIの独立評価を拡充、公表には機密情報の制限も",
  "snippet": "",
  "published": "2026-10-21T13:03:06+00:00"
 },
 {
  "id": "489ef3fefebb",
  "region": "jp",
  "source": "remio",
  "title": "Claude Code v2.1.304、権限に関する判断をより明確に",
  "snippet": "",
  "published": "2026-10-21T14:58:42+00:00"
 },
 {
  "id": "094846df5942",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "米Anthropic、2026年上半期の売上高は約163億ドルに急増も、807億ドルの巨額赤字計上 (ビジネス＋IT)",
  "snippet": "",
  "published": "2026-10-21T12:05:06+00:00"
 },
 {
  "id": "3e081500ed2b",
  "region": "jp",
  "source": "日経クロステック",
  "title": "Anthropic「物理AI版MCP」を米量子QuEraが実証、エラーの復旧成功率99％",
  "snippet": "",
  "published": "2026-10-21T20:00:00+00:00"
 },
 {
  "id": "40e835e29481",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claude Securityに継続スキャンと修正追跡機能を追加",
  "snippet": "",
  "published": "2026-10-21T18:04:18+00:00"
 },
 {
  "id": "36c3da760404",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic上期淨損失800億ドル超、IPO目論見書がAI競争のコストを露呈",
  "snippet": "",
  "published": "2026-10-21T18:21:00+00:00"
 },
 {
  "id": "a7a6a91186f0",
  "region": "jp",
  "source": "ビジネス+IT",
  "title": "OpenAIがAI創薬スタートアップ買収、AnthropicやGoogleとの競争激化",
  "snippet": "",
  "published": "2026-10-21T08:00:00+00:00"
 },
 {
  "id": "3f75b9950683",
  "region": "jp",
  "source": "remio",
  "title": "Claude Code v2.1.305、サンドボックスとのトレードオフを伴うLinux互換性を追加",
  "snippet": "",
  "published": "2026-10-21T17:18:11+00:00"
 },
 {
  "id": "babbf7c3c177",
  "region": "jp",
  "source": "TradingView",
  "title": "Anthropicと音楽出版社、AI学習訴訟で主要議論へ",
  "snippet": "",
  "published": "2026-10-21T14:44:00+00:00"
 },
 {
  "id": "76de7a4248eb",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Glean、Claude Code、Cursor、Codex向けのヘッドレスエージェント構築機能を追加",
  "snippet": "",
  "published": "2026-10-21T15:33:34+00:00"
 },
 {
  "id": "ced32054223c",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Anthropic、ChatGPT DotsやMeta Museに対抗する「Claude Duet」を発表",
  "snippet": "",
  "published": "2026-10-21T13:43:00+00:00"
 },
 {
  "id": "2c0a40077483",
  "region": "jp",
  "source": "CodeZine",
  "title": "Anthropic、ハッカソン「Built with Claude: Japan 2026」を開催、参加者にMax 5x PlanとAPIクレジットを提供",
  "snippet": "",
  "published": "2026-10-21T04:30:00+00:00"
 },
 {
  "id": "c1fc0b57c913",
  "region": "jp",
  "source": "GameBusiness.jp",
  "title": "「Claude」Anthropic、日本向け初のオンラインハッカソン開催！眠っていたアイデアを「Claude Code」で形に、未経験者も参加可能",
  "snippet": "",
  "published": "2026-10-21T04:13:51+00:00"
 },
 {
  "id": "2274a70618ae",
  "region": "jp",
  "source": "remio",
  "title": "Claude Codeによる暗号資産マイナー発見が、より大きなセキュリティ上の逆説を浮き彫りに",
  "snippet": "",
  "published": "2026-10-21T09:49:24+00:00"
 },
 {
  "id": "f190805efb42",
  "region": "jp",
  "source": "NOVAIST",
  "title": "Anthropic、ClaudeがNIST楕円曲線5種のシード生成法を解明 1997年の時刻が手掛かり",
  "snippet": "",
  "published": "2026-10-21T11:02:27+00:00"
 },
 {
  "id": "d9d743e7bca5",
  "region": "jp",
  "source": "BeInCrypto",
  "title": "サトシのビットコイン設計に誤りか クロードのNSA発見で議論",
  "snippet": "",
  "published": "2026-10-21T14:00:00+00:00"
 },
 {
  "id": "90a1c9ce6840",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Anthropic、ハーバード大学の元科学部長を監督機関に迎える",
  "snippet": "",
  "published": "2026-10-21T12:19:00+00:00"
 },
 {
  "id": "29513dd24179",
  "region": "intl",
  "source": "The New York Times",
  "title": "Anthropic Joins the A.I. Agent Race With Claude Duet",
  "snippet": "",
  "published": "2026-10-21T22:45:12+00:00"
 },
 {
  "id": "eabcc68ce22a",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic unveils Claude Duet AI agent app",
  "snippet": "",
  "published": "2026-10-21T20:25:35+00:00"
 },
 {
  "id": "ad23456bcbd6",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic announces preview of Claude Duet, a personal AI agent to take on Muse, Dots",
  "snippet": "",
  "published": "2026-10-21T21:42:54+00:00"
 },
 {
  "id": "705d3445b65a",
  "region": "intl",
  "source": "The Verge",
  "title": "Anthropic takes on Muse with Claude Duet, its new AI agent",
  "snippet": "",
  "published": "2026-10-21T19:53:20+00:00"
 },
 {
  "id": "e8e71f0dd389",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic to publicly file for IPO as early as Friday, sources say",
  "snippet": "",
  "published": "2026-10-21T13:53:43+00:00"
 },
 {
  "id": "6e6bacec4509",
  "region": "intl",
  "source": "Mashable",
  "title": "Anthropic’s AI safety bill would pause AI models if 50+ people could die",
  "snippet": "",
  "published": "2026-10-21T23:53:38+00:00"
 },
 {
  "id": "21f312ed2d50",
  "region": "intl",
  "source": "Axios",
  "title": "Why Anthropic can't afford to delay its IPO",
  "snippet": "",
  "published": "2026-10-21T09:27:42+00:00"
 },
 {
  "id": "cd1e7ab7cc87",
  "region": "intl",
  "source": "Fortune",
  "title": "Anthropic’s S-1 leaks (again)—here’s a look at the massive losses on the income statement",
  "snippet": "",
  "published": "2026-10-21T10:40:00+00:00"
 },
 {
  "id": "72fe1e2ef885",
  "region": "intl",
  "source": "Engadget",
  "title": "Claude Duet Is Anthropic's Answer To Meta Muse And OpenAI Dots",
  "snippet": "",
  "published": "2026-10-21T21:03:19+00:00"
 },
 {
  "id": "d76be378318f",
  "region": "intl",
  "source": "DefenseScoop",
  "title": "Former U.S. officials urge D.C. Circuit to reconsider decision in Anthropic-Pentagon fight",
  "snippet": "",
  "published": "2026-10-21T22:28:48+00:00"
 },
 {
  "id": "b3fc135b0d7b",
  "region": "intl",
  "source": "9to5Mac",
  "title": "Anthropic takes on ChatGPT Dots and Meta Muse with Claude Duet",
  "snippet": "",
  "published": "2026-10-21T19:39:00+00:00"
 },
 {
  "id": "c21f3eee513a",
  "region": "intl",
  "source": "Politico",
  "title": "Why Anthropic’s draft bill sets $1 billion threshold for AI risk",
  "snippet": "",
  "published": "2026-10-21T09:00:00+00:00"
 },
 {
  "id": "0393a9739fde",
  "region": "intl",
  "source": "9to5Google",
  "title": "Claude Duet is Anthropic’s proactive AI agent answer to Muse and OpenAI’s Dots [Video]",
  "snippet": "",
  "published": "2026-10-21T20:45:00+00:00"
 },
 {
  "id": "05e2774a24a1",
  "region": "intl",
  "source": "Business Insider",
  "title": "Anthropic launches Claude Duet, its answer to Meta and OpenAI's personal agents",
  "snippet": "",
  "published": "2026-10-21T20:29:00+00:00"
 },
 {
  "id": "54e5f68f17d6",
  "region": "intl",
  "source": "MacRumors",
  "title": "Anthropic Launches Claude Duet, a Proactive AI Agent",
  "snippet": "",
  "published": "2026-10-21T20:52:59+00:00"
 },
 {
  "id": "99c09c3d485a",
  "region": "intl",
  "source": "WSJ",
  "title": "SpaceX, Anthropic and Nvidia Help Snap Tech Stocks Out of Their Recent Malaise",
  "snippet": "",
  "published": "2026-10-21T21:36:00+00:00"
 },
 {
  "id": "0fef6036545a",
  "region": "intl",
  "source": "The Harvard Crimson",
  "title": "Former Harvard AI Adviser Joins Anthropic Oversight Trust Weeks After Stepping Down",
  "snippet": "",
  "published": "2026-10-21T19:59:25+00:00"
 },
 {
  "id": "a0b834548a17",
  "region": "intl",
  "source": "Al Jazeera",
  "title": "Anthropic posts $80bn loss in first half of 2026: WSJ",
  "snippet": "",
  "published": "2026-10-21T05:52:53+00:00"
 },
 {
  "id": "51eb44695674",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic, music publishers square off on 'fair use' defense in AI copyright case",
  "snippet": "",
  "published": "2026-10-21T21:17:07+00:00"
 },
 {
  "id": "d62ee162cf6d",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic adds former Harvard science dean to oversight body",
  "snippet": "",
  "published": "2026-10-21T17:49:45+00:00"
 },
 {
  "id": "de6a9742e08d",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic appoints physicist Christopher Stubbs to its Long-Term Benefit Trust",
  "snippet": "",
  "published": "2026-10-21T18:09:52+00:00"
 },
 {
  "id": "c43160b617f1",
  "region": "intl",
  "source": "Gizmodo",
  "title": "Anthropic’s New Agent Has No Cute Mascot, and You Probably Can’t Try It Yet",
  "snippet": "",
  "published": "2026-10-21T23:54:17+00:00"
 },
 {
  "id": "970a999f42cb",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Anthropic Accounting Charge Drives 80% Net Loss",
  "snippet": "",
  "published": "2026-10-21T20:15:11+00:00"
 },
 {
  "id": "aa3730b565c9",
  "region": "intl",
  "source": "ExecutiveGov",
  "title": "HHS Plans Sole-Source Anthropic Claude Contract Ahead of Enterprise AI BPA",
  "snippet": "",
  "published": "2026-10-21T21:28:14+00:00"
 },
 {
  "id": "ec9a66048b24",
  "region": "intl",
  "source": "Anadolu Ajansı",
  "title": "Anthropic launches Claude Duet AI agent to rival Meta's Muse, OpenAI's Dots",
  "snippet": "",
  "published": "2026-10-21T21:08:33+00:00"
 },
 {
  "id": "4e178f932325",
  "region": "intl",
  "source": "Anthropic",
  "title": "Charter",
  "snippet": "",
  "published": "2026-10-21T18:03:18+00:00"
 },
 {
  "id": "192b52b4ee7c",
  "region": "intl",
  "source": "Anthropic",
  "title": "Physicist Christopher Stubbs joins Anthropic's Long-Term Benefit Trust",
  "snippet": "",
  "published": "2026-10-21T17:25:01+00:00"
 },
 {
  "id": "881fcae7083d",
  "region": "intl",
  "source": "claude.com",
  "title": "Introducing Claude Duet",
  "snippet": "",
  "published": "2026-10-21T19:05:29+00:00"
 },
 {
  "id": "ffca147fe4b5",
  "region": "intl",
  "source": "Anthropic",
  "title": "Anthropic 2026 Public Benefit Report Taking stock of our progress toward our charter",
  "snippet": "",
  "published": "2026-10-21T18:54:02+00:00"
 },
 {
  "id": "72e6bbc7947e",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Security now scans continuously and tracks fixes",
  "snippet": "",
  "published": "2026-10-21T17:37:00+00:00"
 },
 {
  "id": "3a8a1d77259c",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Get started with Claude Duet",
  "snippet": "",
  "published": "2026-10-21T19:37:37+00:00"
 },
 {
  "id": "2031fa886c5c",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Migrating to API version 2026-10-21",
  "snippet": "",
  "published": "2026-10-21T17:53:02+00:00"
 },
 {
  "id": "c91a96312fda",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Get started with smart reports",
  "snippet": "",
  "published": "2026-10-20T22:43:17+00:00"
 },
 {
  "id": "4f40620b51f8",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Profil Pengguna",
  "snippet": "",
  "published": "2026-10-21T17:48:31+00:00"
 },
 {
  "id": "1e568e5fd777",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Profili utente",
  "snippet": "",
  "published": "2026-10-21T03:18:02+00:00"
 },
 {
  "id": "14e58bd0ff6b",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Perfis de usuário",
  "snippet": "",
  "published": "2026-10-21T01:00:31+00:00"
 },
 {
  "id": "7bbd633e459d",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Perfiles de usuario",
  "snippet": "",
  "published": "2026-10-21T04:38:34+00:00"
 },
 {
  "id": "01265b66b1ab",
  "region": "intl",
  "source": "claude.com",
  "title": "HCLTech becomes a Global Premier Partner for Claude",
  "snippet": "",
  "published": "2026-10-21T19:51:37+00:00"
 },
 {
  "id": "3edddc144c1f",
  "region": "intl",
  "source": "claude.com",
  "title": "Projects redesigned: from folder to conversation",
  "snippet": "",
  "published": "2026-10-21T15:32:42+00:00"
 },
 {
  "id": "dadc8e59bffc",
  "region": "intl",
  "source": "claude.com",
  "title": "Measuring AI Fluency at Your Organization",
  "snippet": "",
  "published": "2026-10-20T21:09:33+00:00"
 },
 {
  "id": "6e1247c72968",
  "region": "intl",
  "source": "claude.com",
  "title": "Attention Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-20T21:15:17+00:00"
 },
 {
  "id": "e7bed70560cc",
  "region": "intl",
  "source": "claude.com",
  "title": "Bubble Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-20T22:47:35+00:00"
 },
 {
  "id": "bea4e2859baf",
  "region": "intl",
  "source": "claude.com",
  "title": "Zingage Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-21T22:03:14+00:00"
 },
 {
  "id": "4984964c2b2b",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Science AMA: How to accelerate scientific discovery",
  "snippet": "",
  "published": "2026-10-20T21:09:31+00:00"
 },
 {
  "id": "2cf383d87cfa",
  "region": "intl",
  "source": "claude.com",
  "title": "Scaling AI Across the Portfolio: Anthropic and AWS for Private Equity",
  "snippet": "",
  "published": "2026-10-21T13:05:24+00:00"
 },
 {
  "id": "98a77e0a7e07",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude builds interactive visuals right in your conversation",
  "snippet": "",
  "published": "2026-10-20T18:43:35+00:00"
 },
 {
  "id": "1a58e798ba9b",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude on AWS",
  "snippet": "",
  "published": "2026-10-21T01:13:16+00:00"
 },
 {
  "id": "59bd045f32e7",
  "region": "intl",
  "source": "claude.com",
  "title": "Working with Claude Fable 5 in Claude Cowork",
  "snippet": "",
  "published": "2026-10-21T17:22:09+00:00"
 },
 {
  "id": "5da502b804de",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Enterprise plan",
  "snippet": "",
  "published": "2026-10-21T02:26:48+00:00"
 },
 {
  "id": "bff50b546104",
  "region": "intl",
  "source": "claude.com",
  "title": "Adspirer Social Ads connector",
  "snippet": "",
  "published": "2026-10-21T00:59:37+00:00"
 },
 {
  "id": "2a7200426574",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.307",
  "snippet": "What's changed Added /claude-api api-version to move Claude API code to API version 2026-10-21 Added the claude_code.safety_event OpenTelemetry event for each tool call a permission rule, auto mode, a safety check, a hook or the sandbox stopped, prompted or sent back Fixed requests failing with a model-not-found error when CLAUDE_CODE_DISABLE_1M_CONTEXT is set and the model is an alias with the [1m] suffix, such as opus[1m] Fixed the prompt-caching-scope beta header being sent behind custom ANTHROPIC_BASE_URL gateways and on Foundry, where it has no effect Fixed MCP servers showing \"needs auth…",
  "published": "2026-10-21T22:17:02+00:00"
 },
 {
  "id": "e35546215de1",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.306",
  "snippet": "What's changed Fixed claude -p inside cloud sessions reporting \"Not logged in\" when started without the session's environment variables Fixed an API error being replaced by \"prompt is too long\", and an unneeded compaction, in sessions with many MCP tools",
  "published": "2026-10-21T03:16:31+00:00"
 }
]
