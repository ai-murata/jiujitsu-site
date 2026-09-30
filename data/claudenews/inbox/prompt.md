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
  "id": "aeb0a46bb641",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "【2026年最新】Claude Code勢に迫る？ 激変したCopilot、仕事が回る“7つ”の新機能（ビジネス＋IT）",
  "snippet": "",
  "published": "2026-09-29T22:20:06+00:00"
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
  "id": "da4af6f1f0db",
  "region": "jp",
  "source": "Reuters",
  "title": "The 'alarming' safety warning in the Anthropic IPO filing",
  "snippet": "",
  "published": "2026-09-29T23:48:45+00:00"
 },
 {
  "id": "70e1829fbb77",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "AnthropicのIPO目論見書が「人類存亡リスク」に言及、現行AIの危険はどこまで確認されたか",
  "snippet": "",
  "published": "2026-09-29T21:33:01+00:00"
 },
 {
  "id": "25114075e9e0",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claude.ai、Code、Cowork、API全体でのサービス障害を報告",
  "snippet": "",
  "published": "2026-09-29T15:16:06+00:00"
 },
 {
  "id": "70a7bd0e7f53",
  "region": "jp",
  "source": "gihyo.jp",
  "title": "スキルに新コマンド「build-eval」",
  "snippet": "",
  "published": "2026-09-29T10:32:00+00:00"
 },
 {
  "id": "12b421a315c8",
  "region": "jp",
  "source": "Межа. Новини України.",
  "title": "Anthropicは2025年売上の47％をAmazonとGoogle経由で得て、巨大ITへの依存を深めた",
  "snippet": "",
  "published": "2026-09-29T21:45:50+00:00"
 },
 {
  "id": "adfd9928dcd9",
  "region": "jp",
  "source": "Moomoo",
  "title": "速報：Anthropicの届出で420億ドルの損失判明、AMDがWorld Labsを買収",
  "snippet": "",
  "published": "2026-09-29T14:03:45+00:00"
 },
 {
  "id": "13db6df2c2bf",
  "region": "jp",
  "source": "SHIFT AI",
  "title": "【2026年最新】Claude Codeセミナー・講座おすすめ17選！種類別の選び方も徹底解説",
  "snippet": "",
  "published": "2026-09-29T04:23:07+00:00"
 },
 {
  "id": "83f8689dbfd4",
  "region": "jp",
  "source": "jp.beincrypto.com",
  "title": "AnthropicのIPO申請、AIが人類に脅威と警告",
  "snippet": "",
  "published": "2026-09-29T14:07:48+00:00"
 },
 {
  "id": "0e64947e639d",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic CPOマイク・クリーガー氏：「正しいAIプロダクトの形を誰もまだ知らない」",
  "snippet": "",
  "published": "2026-09-29T13:08:00+00:00"
 },
 {
  "id": "1e4695bf2c00",
  "region": "jp",
  "source": "itmedia.co.jp",
  "title": "Anthropic、IPO目論見書でAIによる「人類存亡リスク」を警告 海外報道",
  "snippet": "",
  "published": "2026-09-29T10:18:11+00:00"
 },
 {
  "id": "ab2865db3532",
  "region": "jp",
  "source": "Межа. Новини України.",
  "title": "Anthropic、自律型AIエージェントの法的責任リスクを警告",
  "snippet": "",
  "published": "2026-09-29T18:16:23+00:00"
 },
 {
  "id": "cdb4e8692b73",
  "region": "jp",
  "source": "SHIFT AI",
  "title": "Claude Codeの本おすすめ9選！初心者に合う1冊の選び方",
  "snippet": "",
  "published": "2026-09-29T09:29:57+00:00"
 },
 {
  "id": "85567827541b",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "Anthropic、売上46億ドルで純損失420億ドル その裏に5,180億ドルの巨額契約",
  "snippet": "",
  "published": "2026-09-29T10:56:40+00:00"
 },
 {
  "id": "5fd413b37f49",
  "region": "jp",
  "source": "TechTargetジャパン",
  "title": "GPU偏重に迫る転換点 AnthropicがAkamaiにCPUインフラ託す理由：GPU一極集中から分散型CPU基盤への転換",
  "snippet": "",
  "published": "2026-09-29T20:00:00+00:00"
 },
 {
  "id": "6823d4ca8b63",
  "region": "jp",
  "source": "itmedia.co.jp",
  "title": "Anthropic、「Claude Sonnet 5.5」公開 料金据え置きで30％以上高速化、タスク当たりコスト最大3割減",
  "snippet": "",
  "published": "2026-09-28T21:55:33+00:00"
 },
 {
  "id": "b561ccd4c8fc",
  "region": "jp",
  "source": "クラウド Watch",
  "title": "NSSOLがAnthropicと協業、AIエージェント連携やレガシーシステム刷新などを推進へ",
  "snippet": "",
  "published": "2026-09-29T04:27:00+00:00"
 },
 {
  "id": "bea36a6899b1",
  "region": "jp",
  "source": "jp.beincrypto.com",
  "title": "AnthropicのIPOに関する8つの疑問点",
  "snippet": "",
  "published": "2026-09-29T18:06:38+00:00"
 },
 {
  "id": "0816aad2102b",
  "region": "jp",
  "source": "Reuters",
  "title": "アンソロピックＩＰＯ目論見書、壮大なＡＩ構想もコスト増浮き彫り",
  "snippet": "",
  "published": "2026-09-29T00:30:00+00:00"
 },
 {
  "id": "d2f04630a396",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "米株価指数先物はまちまち、半導体株が反発。AnthropicのIPO申請で巨額損失が明らかに",
  "snippet": "",
  "published": "2026-09-29T13:25:00+00:00"
 },
 {
  "id": "c83f1dff65c4",
  "region": "jp",
  "source": "株式会社エクサウィザーズ",
  "title": "エクサベース AI、 Anthropic最新モデル「Claude Opus 5.5」を提供開始 ～長時間の自律的なタスク遂行と、これまでで最も高い安全性評価を両立",
  "snippet": "",
  "published": "2026-09-28T23:35:55+00:00"
 },
 {
  "id": "5aff97db9ddf",
  "region": "jp",
  "source": "日本経済新聞",
  "title": "アンソロピックIPO書類「強力なAI、人類存亡のリスク」 ロイター報道",
  "snippet": "",
  "published": "2026-09-29T02:46:05+00:00"
 },
 {
  "id": "689ac58006e2",
  "region": "jp",
  "source": "ビジネス+IT",
  "title": "AIが作った資料、そのまま出してない？Claude Codeで「AI部下」に検品させる神ワザ7選 連載：きょうから使える生成AI仕事術",
  "snippet": "",
  "published": "2026-09-28T21:10:00+00:00"
 },
 {
  "id": "d22b2a4a75f2",
  "region": "jp",
  "source": "Moomoo",
  "title": "Anthropicの2兆ドル規模IPOの可能性を探る",
  "snippet": "",
  "published": "2026-09-29T07:00:00+00:00"
 },
 {
  "id": "c79c379ee257",
  "region": "intl",
  "source": "Reuters",
  "title": "EXCLUSIVE: Anthropic IPO prospectus lays bare deep dependence on Big Tech partners",
  "snippet": "",
  "published": "2026-09-29T21:52:24+00:00"
 },
 {
  "id": "7ee1dbbeec83",
  "region": "intl",
  "source": "The New York Times",
  "title": "Is Claude Conscious? Inside Anthropic’s Quest to Instill Morality Into Its A.I. Models",
  "snippet": "",
  "published": "2026-09-30T00:09:48+00:00"
 },
 {
  "id": "6bec62ce7919",
  "region": "intl",
  "source": "Anthropic",
  "title": "What Do You Want from AI?",
  "snippet": "",
  "published": "2026-09-29T16:39:00+00:00"
 },
 {
  "id": "7a36ad9ca701",
  "region": "intl",
  "source": "finance.yahoo.com",
  "title": "Anthropic IPO: What investors should know about costs, risks after leaked prospectus",
  "snippet": "",
  "published": "2026-09-29T16:47:31+00:00"
 },
 {
  "id": "eba0a23427e1",
  "region": "intl",
  "source": "Mashable",
  "title": "Anthropic launches Claude Opus 5.5: Benchmarks, pricing, safety",
  "snippet": "",
  "published": "2026-09-29T20:12:06+00:00"
 },
 {
  "id": "bc0fa0266610",
  "region": "intl",
  "source": "CNN",
  "title": "Anthropic says its AI models pose ‘existential risk to humanity’ in leaked IPO filing: report",
  "snippet": "",
  "published": "2026-09-29T14:37:34+00:00"
 },
 {
  "id": "3eb6d145f0f5",
  "region": "intl",
  "source": "inc.com",
  "title": "A Quarter of Anthropic's Revenue Comes From 2 Customers. Experts Say the Real Test Comes Next",
  "snippet": "",
  "published": "2026-09-29T16:15:49+00:00"
 },
 {
  "id": "a6b3a75abc69",
  "region": "intl",
  "source": "theguardian.com",
  "title": "Anthropic ‘warns of existential AI risks to humanity’ in IPO document",
  "snippet": "",
  "published": "2026-09-29T12:16:00+00:00"
 },
 {
  "id": "e74a9534f5b0",
  "region": "intl",
  "source": "Gizmodo",
  "title": "Leaked Anthropic IPO Prospectus Gives Wall Street an Early Look at How AI Could Go Off the Rails",
  "snippet": "",
  "published": "2026-09-29T17:00:29+00:00"
 },
 {
  "id": "f74745b2c6f4",
  "region": "intl",
  "source": "Reuters",
  "title": "EXCLUSIVE: Anthropic warns AI may pose 'existential risks to humanity' in IPO filing",
  "snippet": "",
  "published": "2026-09-29T17:04:59+00:00"
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
  "id": "ee928c6a4bcd",
  "region": "intl",
  "source": "finance.yahoo.com",
  "title": "Anthropic’s S-1 Is Here. The $518 Billion Commitment Is the Real Story.",
  "snippet": "",
  "published": "2026-09-29T16:57:31+00:00"
 },
 {
  "id": "e70b89633f54",
  "region": "intl",
  "source": "The New York Times",
  "title": "What’s In Anthropic’s I.P.O. Filing",
  "snippet": "",
  "published": "2026-09-29T11:58:36+00:00"
 },
 {
  "id": "ecd668897575",
  "region": "intl",
  "source": "theguardian.com",
  "title": "As AI models go rogue, do you still trust OpenAI and Anthropic to stop them? I don’t and neither should you",
  "snippet": "",
  "published": "2026-09-29T16:32:00+00:00"
 },
 {
  "id": "e93dcefebda3",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic's $518 billion AI buildout hinges largely on deals that cannot be canceled, filing shows",
  "snippet": "",
  "published": "2026-09-29T16:48:56+00:00"
 },
 {
  "id": "31232a545b93",
  "region": "intl",
  "source": "finance.yahoo.com",
  "title": "Anthropic IPO leaks — here are 2 big hot takes",
  "snippet": "",
  "published": "2026-09-29T14:53:45+00:00"
 },
 {
  "id": "79337459cf8f",
  "region": "intl",
  "source": "Reuters",
  "title": "EXCLUSIVE: Anthropic says rogue AI agents pose uncertain legal risk for the company",
  "snippet": "",
  "published": "2026-09-29T17:16:36+00:00"
 },
 {
  "id": "e4ee0142c30f",
  "region": "intl",
  "source": "finance.yahoo.com",
  "title": "Anthropic Reportedly Generated $4.6 Billion in Revenue and Lost $42 Billion in 2025. Will This Impact Its Targeted $2 Trillion Valuation?",
  "snippet": "",
  "published": "2026-09-29T14:37:01+00:00"
 },
 {
  "id": "ebb1b4ffb076",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic's IPO prospectus sharpens focus on AI valuations",
  "snippet": "",
  "published": "2026-09-29T14:15:53+00:00"
 },
 {
  "id": "fd7d8d19d8ef",
  "region": "intl",
  "source": "Reuters",
  "title": "Trump, AI CEOs sign voluntary safety pact, back data center expansion",
  "snippet": "",
  "published": "2026-09-29T22:45:58+00:00"
 },
 {
  "id": "8d08bfd06570",
  "region": "intl",
  "source": "fortune.com",
  "title": "Anthropic’s leaked IPO prospectus details steep losses, rapid growth, and a fear that AI could end humanity",
  "snippet": "",
  "published": "2026-09-29T10:03:00+00:00"
 },
 {
  "id": "aa6eb781d65b",
  "region": "intl",
  "source": "Investor's Business Daily",
  "title": "Anthropic IPO Filing Shows Fast Growth, Big Losses and 'Catastrophic Risk' Warning: Report",
  "snippet": "",
  "published": "2026-09-29T13:50:00+00:00"
 },
 {
  "id": "bf7bd4adac19",
  "region": "intl",
  "source": "The Next Web",
  "title": "Claude is down as Anthropic investigates errors across its services",
  "snippet": "",
  "published": "2026-09-29T17:34:38+00:00"
 },
 {
  "id": "c3490ab34d66",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "ExodusPoint Joins Hedge Funds Partnering With Anthropic Over AI",
  "snippet": "",
  "published": "2026-09-29T13:09:22+00:00"
 },
 {
  "id": "9d7c913545a6",
  "region": "intl",
  "source": "Reuters",
  "title": "Breakingviews - COMMENTARY: Anthropic’s $2 trln goal is AI’s biggest moonshot",
  "snippet": "",
  "published": "2026-09-29T19:08:01+00:00"
 },
 {
  "id": "6096e6b78172",
  "region": "intl",
  "source": "Anthropic",
  "title": "Introducing Claude Sonnet 5.5",
  "snippet": "",
  "published": "2026-09-28T22:47:04+00:00"
 },
 {
  "id": "bd6e02d9333e",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Prompting Claude Sonnet 5.5",
  "snippet": "",
  "published": "2026-09-28T18:01:55+00:00"
 },
 {
  "id": "dfa6fdcebcc6",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Claude Sonnet 5.5",
  "snippet": "",
  "published": "2026-09-28T17:59:48+00:00"
 },
 {
  "id": "e2148b46b050",
  "region": "intl",
  "source": "Anthropic",
  "title": "Claude Sonnet 5.5 System Card",
  "snippet": "",
  "published": "2026-09-28T18:06:05+00:00"
 },
 {
  "id": "d30ca3f5cca3",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Migrating to Claude Sonnet 5.5",
  "snippet": "",
  "published": "2026-09-28T18:01:46+00:00"
 },
 {
  "id": "15da86502fbc",
  "region": "intl",
  "source": "claude.com",
  "title": "Giving companies more control over their AI agents, with NVIDIA",
  "snippet": "",
  "published": "2026-09-28T21:02:46+00:00"
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
  "id": "c86e0fbd3806",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Capabilities",
  "snippet": "",
  "published": "2026-09-28T16:15:01+00:00"
 },
 {
  "id": "50649cb48912",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Why Claude switched models in your conversation with Sonnet 5.5",
  "snippet": "",
  "published": "2026-09-28T18:02:18+00:00"
 },
 {
  "id": "6d3aad834d55",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Real-time cyber safeguards on Claude Opus and Sonnet",
  "snippet": "",
  "published": "2026-09-28T19:21:59+00:00"
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
  "published": "2026-09-29T19:04:22+00:00"
 },
 {
  "id": "310df9abad1c",
  "region": "intl",
  "source": "support.claude.com",
  "title": "How Claude marks AI-generated content | Claude Help Center",
  "snippet": "",
  "published": "2026-09-28T18:34:34+00:00"
 },
 {
  "id": "7ac985bcdef7",
  "region": "intl",
  "source": "Claude Platform",
  "title": "What's new in Claude Sonnet 5.5",
  "snippet": "",
  "published": "2026-09-28T18:00:08+00:00"
 },
 {
  "id": "f26ba77aff5c",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Plugins: Encode your team's expertise · Introduction to Claude Cowork",
  "snippet": "",
  "published": "2026-09-29T14:28:24+00:00"
 },
 {
  "id": "9ccbbcf4e1a3",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "- academy.claude.com",
  "snippet": "academy.claude.com",
  "published": "2026-09-29T22:11:58+00:00"
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
  "id": "897b6d00b9d7",
  "region": "intl",
  "source": "Anthropic",
  "title": "Claude Sonnet 5",
  "snippet": "",
  "published": "2026-09-28T18:00:12+00:00"
 },
 {
  "id": "d9da138975c5",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Claude Sonnet 5.5 system prompts",
  "snippet": "",
  "published": "2026-09-28T19:14:18+00:00"
 },
 {
  "id": "2a011c7f7ffa",
  "region": "intl",
  "source": "Anthropic",
  "title": "Policy on the AI Exponential",
  "snippet": "",
  "published": "2026-09-28T14:00:06+00:00"
 },
 {
  "id": "006a7a871bca",
  "region": "intl",
  "source": "Anthropic",
  "title": "- Anthropic",
  "snippet": "Anthropic",
  "published": "2026-09-29T15:54:04+00:00"
 },
 {
  "id": "dcdfed08d1ca",
  "region": "intl",
  "source": "support.claude.com",
  "title": "Preserved thinking: changing how the Messages API handles thinking blocks to protect against distillation",
  "snippet": "",
  "published": "2026-09-28T18:36:28+00:00"
 },
 {
  "id": "a3dbb26ac21b",
  "region": "intl",
  "source": "claude.com",
  "title": "Apply to the Anthropic VC partner program",
  "snippet": "",
  "published": "2026-09-29T03:24:50+00:00"
 },
 {
  "id": "46b30df39c5b",
  "region": "intl",
  "source": "claude.com",
  "title": "Replit Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-09-28T21:11:05+00:00"
 },
 {
  "id": "cad569c6c442",
  "region": "intl",
  "source": "claude.com",
  "title": "Productivity",
  "snippet": "",
  "published": "2026-09-29T03:46:23+00:00"
 },
 {
  "id": "d906990043d7",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.285",
  "snippet": "What's changed Added CLAUDE_CODE_DISABLE_WEB_FETCH environment variable to turn off the WebFetch tool Added claude --desktop to open the Claude desktop app on the current directory, or on a session with --continue / --resume <id> Added claude plugin configure <plugin> to show a plugin's options and which are unset, or save new values read from stdin with --values-stdin Added <server>.<key>=<value> to claude plugin install --config , so a bundled .mcpb MCP server's own settings can be set at install time and it starts without visiting /plugin → Configure Added allowedProviders managed setting t…",
  "published": "2026-09-29T19:27:30+00:00"
 },
 {
  "id": "00e36c8cef2e",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.284",
  "snippet": "What's changed Added Claude Sonnet 5.5 ( claude-sonnet-5-5 ), now the default Sonnet model on the Anthropic API — 1M context, $2/$10 per Mtok with $0.20/Mtok cache reads Added a \"Yes, but ask again next time\" answer to auto mode's prompt before a read outside the working directories, so you can allow that one read and still be asked about later ones Added dollar amounts to the Claude apps gateway spend limit in /usage and the status line (for example \"$271.40 / $500.00 spent this month\") when the gateway runs this version or later; the status line's rate_limits.spend_limit also gains used_usd…",
  "published": "2026-09-28T18:02:03+00:00"
 }
]
