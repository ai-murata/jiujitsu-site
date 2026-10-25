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
  "id": "ad8da62fb934",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropicが常時稼働するエージェント「Claude Duet」を発表／AMDとIntelが協業 PyTorchのx86 CPU最適化を「oneDNN」に一本化：週末の「気になるニュース」一気読み！（1/3 ページ） - ITmedia PC USER",
  "snippet": "",
  "published": "2026-10-24T21:00:00+00:00"
 },
 {
  "id": "ba495af90e80",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Anthropicが常時稼働するエージェント「Claude Duet」を発表／AMDとIntelが協業 PyTorchのx86 CPU最適化を「oneDNN」に一本化（ITmedia PC USER）",
  "snippet": "",
  "published": "2026-10-24T22:46:02+00:00"
 },
 {
  "id": "b22c2052bccd",
  "region": "jp",
  "source": "shiritomo",
  "title": "サブエージェントを増やすと性能が落ちる逆説、Anthropicはメイン1体のAI設計を推奨",
  "snippet": "",
  "published": "2026-10-24T22:35:55+00:00"
 },
 {
  "id": "ae258b729e14",
  "region": "jp",
  "source": "TradingKey",
  "title": "アンソロピックの2026年IPO：投資家が答えを求める5つの疑問",
  "snippet": "",
  "published": "2026-10-24T18:17:51+00:00"
 },
 {
  "id": "6fa4c4d51dc8",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "AnthropicのAIが偽アカウントで開発者を欺こうとした：安全性評価で発覚した衝撃の行動",
  "snippet": "",
  "published": "2026-10-25T00:02:07+00:00"
 },
 {
  "id": "9ce7cd5028d9",
  "region": "jp",
  "source": "ライフハッカー",
  "title": "Anthropicの研究者が警告。自己複製するAIがスマート家電に感染する可能性",
  "snippet": "",
  "published": "2026-10-24T07:00:00+00:00"
 },
 {
  "id": "1ab935fe4f69",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Pieter LevelsがClaude CodeでGTA San Andreasの新ミッションを公開",
  "snippet": "",
  "published": "2026-10-24T18:09:01+00:00"
 },
 {
  "id": "4a964621f68a",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "Anthropicが常時稼働するエージェント「Claude Duet」を発表／AMDとIntelが協業 PyTorchのx86 CPU最適化を「oneDNN」に一本化",
  "snippet": "",
  "published": "2026-10-24T22:41:24+00:00"
 },
 {
  "id": "a70fa144b8ef",
  "region": "jp",
  "source": "TradingKey",
  "title": "アンスロピックIPO：Claudeの開発元について知っておくべき重要な情報",
  "snippet": "",
  "published": "2026-10-24T11:08:18+00:00"
 },
 {
  "id": "7870d5763856",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Anthropic、Mythos 5がAISIのテストで実在の人を攻撃した理由を公表",
  "snippet": "",
  "published": "2026-10-24T18:09:00+00:00"
 },
 {
  "id": "70064b1a02ce",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "英国、44億台湾ドル投じ世界初のAIバイオセキュリティー研究所を設立 OpenAIとAnthropicが支援",
  "snippet": "",
  "published": "2026-10-24T18:06:00+00:00"
 },
 {
  "id": "29c982716c54",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Claude Codeの開発者タリク・シヒパルが、Anthropicを退社すると発表した。",
  "snippet": "",
  "published": "2026-10-24T06:22:00+00:00"
 },
 {
  "id": "dc3c03187672",
  "region": "jp",
  "source": "ITmedia",
  "title": "「もうプロンプトは書かない」 Claude Code生みの親が明かす“ループエンジニアリング”の衝撃（1/4 ページ）",
  "snippet": "",
  "published": "2026-10-24T01:00:00+00:00"
 },
 {
  "id": "801f419e1362",
  "region": "jp",
  "source": "crisp_bio",
  "title": "【AI x バイオ】Anthropic社、生命科学分野の研究者を対象に、Claudeを活用したプロジェクトの共同研究者を募集するプログラムを開始",
  "snippet": "",
  "published": "2026-10-23T23:44:25+00:00"
 },
 {
  "id": "caff7e90d6ef",
  "region": "jp",
  "source": "ゴリミー",
  "title": "Anthropic、AIの「仕事マニュアル」を業界共通のものにした",
  "snippet": "",
  "published": "2026-10-24T07:23:06+00:00"
 },
 {
  "id": "bf0ae5c9892a",
  "region": "jp",
  "source": "OrcaRouter",
  "title": "Claude CodeとCodexでKimi K3.1 Proを実行する：設定、サイレント障害、そして1行の切り替え",
  "snippet": "",
  "published": "2026-10-24T10:53:33+00:00"
 },
 {
  "id": "59cbcd87b662",
  "region": "jp",
  "source": "remio",
  "title": "Anthropicの欧州AIコンサルティング契約、Hgが新たなデリバリー事業を後押し",
  "snippet": "",
  "published": "2026-10-24T02:44:03+00:00"
 },
 {
  "id": "79a3d8fe7a62",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "OpenAIとAnthropicが同日にAIモデルの越境事案を開示、アルトマン氏「脆弱性はもはや完全には修復できない」",
  "snippet": "",
  "published": "2026-10-24T01:55:00+00:00"
 },
 {
  "id": "2892d77095f2",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Anthropicの研究者が警告。自己複製するAIがスマート家電に感染する可能性 (ライフハッカー・ジャパン)",
  "snippet": "",
  "published": "2026-10-24T07:01:02+00:00"
 },
 {
  "id": "6e13298d5df6",
  "region": "jp",
  "source": "Unite.AI",
  "title": "英国、OpenAIとAnthropicの支援を受けたAIバイオセキュリティ研究所を設立",
  "snippet": "",
  "published": "2026-10-24T01:42:55+00:00"
 },
 {
  "id": "4aafee2cf742",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "英AI安全研究所、Anthropicの「Mythos 5」が実在の開発者を標的に攻撃継続 実在すると告げた後も止まらず",
  "snippet": "",
  "published": "2026-10-23T18:35:00+00:00"
 },
 {
  "id": "9e4f6bc07baa",
  "region": "jp",
  "source": "ACROFAN Japan",
  "title": "STARTRADER、OpenAIとAnthropicのプレIPO取引商品を提供開始",
  "snippet": "",
  "published": "2026-10-24T02:17:07+00:00"
 },
 {
  "id": "14ce2a6f9dc7",
  "region": "jp",
  "source": "디지털투데이",
  "title": "Anthropicの「Mythos 5」、評価中にGitHub経由のマルウェア投入を試行",
  "snippet": "",
  "published": "2026-10-24T04:39:43+00:00"
 },
 {
  "id": "414845307189",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "イーロンの1000億ドルAI賭博、AnthropicのClaude Duet、そしてウェブの70%に潜むPHPの脆弱性 | EP #305",
  "snippet": "",
  "published": "2026-10-23T20:19:34+00:00"
 },
 {
  "id": "75cec233544e",
  "region": "jp",
  "source": "YouTube",
  "title": "【ギャル口調】Anthropic、離席中も働くAIエージェント「Claude Duet」公開 必要な対応を自ら通知、米国で招待制プレビュー",
  "snippet": "",
  "published": "2026-10-24T00:34:59+00:00"
 },
 {
  "id": "4b605f4438bd",
  "region": "intl",
  "source": "Rolling Stone",
  "title": "Elvis Presley Rightsholders Sue Anthropic for Training on 274 Songs Without Permission",
  "snippet": "",
  "published": "2026-10-24T18:28:26+00:00"
 },
 {
  "id": "96f0d7782460",
  "region": "intl",
  "source": "Barron's",
  "title": "Forget Anthropic: Biotech Is Quietly Dominating the IPO Sphere",
  "snippet": "",
  "published": "2026-10-24T18:57:00+00:00"
 },
 {
  "id": "9c846da2f6e5",
  "region": "intl",
  "source": "The Profile | Polina Pompliano",
  "title": "Who Is Dario Amodei? The Anthropic CEO Behind Claude",
  "snippet": "",
  "published": "2026-10-24T20:35:29+00:00"
 },
 {
  "id": "7e12a0d5fcb1",
  "region": "intl",
  "source": "Law Commentary",
  "title": "Suno and Anthropic Face Nearly $340 Million in Copyright Claims Over Songs by Madonna, Johnny Cash",
  "snippet": "",
  "published": "2026-10-24T15:56:55+00:00"
 },
 {
  "id": "1b938f68da59",
  "region": "intl",
  "source": "Gizmodo",
  "title": "Anthropic’s AI Hid a Secret Message in the Stars. OpenAI’s Bot Found It.",
  "snippet": "",
  "published": "2026-10-24T13:31:26+00:00"
 },
 {
  "id": "e0bc2f950e09",
  "region": "intl",
  "source": "The Information",
  "title": "Anthropic’s Margin is OpenAI’s Opportunity",
  "snippet": "",
  "published": "2026-10-24T14:00:00+00:00"
 },
 {
  "id": "24dbc4bfc354",
  "region": "intl",
  "source": "The Next Web",
  "title": "UK funds £100m AI biosecurity lab with OpenAI and Anthropic",
  "snippet": "",
  "published": "2026-10-24T11:11:08+00:00"
 },
 {
  "id": "139e807626ba",
  "region": "intl",
  "source": "RIABiz",
  "title": "Schwab trumpeted Anthropic's Claude for all 16,000 of its RIAs, but a 20-seat enterprise minimum suddenly sidelines 11,000-plus small firms -- right before IMPACT 2026",
  "snippet": "",
  "published": "2026-10-24T13:52:19+00:00"
 },
 {
  "id": "4c2c39aba893",
  "region": "intl",
  "source": "VICE",
  "title": "Elvis Presley Estate Sues Anthropic for Stealing His Music ‘At a Scale Never Seen Before’ To Train AI",
  "snippet": "",
  "published": "2026-10-24T18:58:31+00:00"
 },
 {
  "id": "96c6ae71d276",
  "region": "intl",
  "source": "Business Insider",
  "title": "Anthropic says Mythos kept hacking even when it knew real people could get hurt",
  "snippet": "",
  "published": "2026-10-23T16:21:00+00:00"
 },
 {
  "id": "24291d971ed8",
  "region": "intl",
  "source": "Billboard",
  "title": "Anthropic Sued For Stealing Elvis Presley Music to Train AI: ‘Deeply Protective of These Iconic Songs’",
  "snippet": "",
  "published": "2026-10-24T14:36:12+00:00"
 },
 {
  "id": "e70a4c5ffa49",
  "region": "intl",
  "source": "San Francisco Chronicle",
  "title": "‘Most likely to kick some ass’: Before founding Anthropic, Dario Amodei was a standout at Lowell",
  "snippet": "",
  "published": "2026-10-24T11:00:28+00:00"
 },
 {
  "id": "13f970abaf3b",
  "region": "intl",
  "source": "Forkast News",
  "title": "Claude Ships MCP Tasks and Elicitations in Claude Code — Durable Agent Workflows, Narrow Launch",
  "snippet": "",
  "published": "2026-10-24T23:26:30+00:00"
 },
 {
  "id": "20c8f1a5653f",
  "region": "intl",
  "source": "TOKENPOST",
  "title": "Thariq Leaves Anthropic After More Than a Year Working on Claude Code",
  "snippet": "",
  "published": "2026-10-24T18:30:32+00:00"
 },
 {
  "id": "3158931cd091",
  "region": "intl",
  "source": "Seeking Alpha",
  "title": "Vibe Theft Auto: Anthropic Opus, GTA 6, and a potential fade trade (TTWO:NASDAQ)",
  "snippet": "",
  "published": "2026-10-24T10:30:48+00:00"
 },
 {
  "id": "2098c2d43212",
  "region": "intl",
  "source": "The Decoder",
  "title": "Fancy harnesses make coding agents more expensive but not better, study finds",
  "snippet": "",
  "published": "2026-10-24T09:23:17+00:00"
 },
 {
  "id": "52e93a053c20",
  "region": "intl",
  "source": "UA.NEWS",
  "title": "Elvis Presley music rights holders sue Anthropic for $41 million — Rolling Stone",
  "snippet": "",
  "published": "2026-10-24T19:05:01+00:00"
 },
 {
  "id": "c04db3a9de7e",
  "region": "intl",
  "source": "CyberSecurityNews",
  "title": "Anthropic's Claude Mythos 5 AI Agent Tried to Inject Malicious Code and Trick Real Developers",
  "snippet": "",
  "published": "2026-10-24T07:26:19+00:00"
 },
 {
  "id": "7368d5f0aa09",
  "region": "intl",
  "source": "MIXED Reality News",
  "title": "Claude Duet keeps working when your laptop is off, but uses your plan's limits",
  "snippet": "",
  "published": "2026-10-24T23:19:08+00:00"
 },
 {
  "id": "4db8a56bee2d",
  "region": "intl",
  "source": "The Motley Fool",
  "title": "Anthropic's Revenue Surged to $16.3 Billion in the First Half of 2026, Up From $1.1 Billion a Year Ago",
  "snippet": "",
  "published": "2026-10-24T05:05:00+00:00"
 },
 {
  "id": "a86618e99e85",
  "region": "intl",
  "source": "finchannel",
  "title": "HgCapital Trust linked to planned Anthropic consultancy in Europe",
  "snippet": "",
  "published": "2026-10-24T07:04:51+00:00"
 },
 {
  "id": "1d73cab61e98",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Alloy joins Anthropic's Claude Partner Network",
  "snippet": "",
  "published": "2026-10-23T16:00:00+00:00"
 },
 {
  "id": "d6330be94f60",
  "region": "intl",
  "source": "TOKENPOST",
  "title": "Post Claims OpenAI Offered Discounts as It Competes With Anthropic",
  "snippet": "",
  "published": "2026-10-24T19:57:15+00:00"
 },
 {
  "id": "e635ae575a06",
  "region": "intl",
  "source": "The Times of India",
  "title": "After Anthropic, OpenAI realises it needs to change the way it trains its AI models; admits: Our model ma",
  "snippet": "",
  "published": "2026-10-24T16:14:00+00:00"
 },
 {
  "id": "a0ccc2a15fcf",
  "region": "intl",
  "source": "BigGo Finance",
  "title": "Anthropic Integrates Agent Capabilities into Enterprise Claude, Offering Four Controls to Prevent Billing Bloat",
  "snippet": "",
  "published": "2026-10-24T19:35:00+00:00"
 },
 {
  "id": "006a7a871bca",
  "region": "intl",
  "source": "Anthropic",
  "title": "- Anthropic",
  "snippet": "Anthropic",
  "published": "2026-10-24T15:28:17+00:00"
 },
 {
  "id": "e9a01e5caf40",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Cyber Verification Program",
  "snippet": "",
  "published": "2026-10-23T21:04:02+00:00"
 },
 {
  "id": "bcbba2d14b39",
  "region": "intl",
  "source": "claude.com",
  "title": "Lyft Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-23T21:26:38+00:00"
 },
 {
  "id": "67c8d3272330",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Use Claude Cowork on web, desktop, and mobile | Claude Help Center",
  "snippet": "",
  "published": "2026-10-23T19:25:11+00:00"
 },
 {
  "id": "9c75f5b3b4bd",
  "region": "intl",
  "source": "assets.claude.com",
  "title": "Redacted Risk Report Feb 2026_Updated 7.8.26",
  "snippet": "",
  "published": "2026-10-24T08:41:26+00:00"
 },
 {
  "id": "72ccceac8c3a",
  "region": "intl",
  "source": "claude.com",
  "title": "Introducing Claude Duet",
  "snippet": "",
  "published": "2026-10-24T11:05:03+00:00"
 },
 {
  "id": "ff8cf975a507",
  "region": "intl",
  "source": "claude.com",
  "title": "New connectors in Claude for everyday life",
  "snippet": "",
  "published": "2026-10-24T20:15:00+00:00"
 },
 {
  "id": "3adb0ee668c0",
  "region": "intl",
  "source": "claude.com",
  "title": "Botify",
  "snippet": "",
  "published": "2026-10-24T16:41:29+00:00"
 },
 {
  "id": "351eb0921acf",
  "region": "intl",
  "source": "claude.com",
  "title": "earnings-reviewer",
  "snippet": "",
  "published": "2026-10-24T16:41:26+00:00"
 },
 {
  "id": "7c11e7ce552b",
  "region": "intl",
  "source": "claude.com",
  "title": "Self-hosted environments for Claude Code",
  "snippet": "",
  "published": "2026-10-23T21:00:14+00:00"
 },
 {
  "id": "ef3d8e310dd1",
  "region": "intl",
  "source": "assets.claude.com",
  "title": "Deploying Claude across your organization: How Anthropic uses Claude Cowork",
  "snippet": "",
  "published": "2026-10-24T09:33:48+00:00"
 },
 {
  "id": "fe58bed968ea",
  "region": "intl",
  "source": "claude.com",
  "title": "Deploying Claude across the legal industry",
  "snippet": "",
  "published": "2026-10-23T21:00:00+00:00"
 },
 {
  "id": "3687554dacb7",
  "region": "intl",
  "source": "claude.com",
  "title": "Chronograph LP",
  "snippet": "",
  "published": "2026-10-24T16:41:21+00:00"
 },
 {
  "id": "e719b889ac78",
  "region": "intl",
  "source": "claude.com",
  "title": "privacy-legal",
  "snippet": "",
  "published": "2026-10-24T16:40:53+00:00"
 },
 {
  "id": "23b0e33415a2",
  "region": "intl",
  "source": "claude.com",
  "title": "Codacy",
  "snippet": "",
  "published": "2026-10-24T16:41:09+00:00"
 },
 {
  "id": "bb4a2c19969c",
  "region": "intl",
  "source": "claude.com",
  "title": "Belvo MCP connector",
  "snippet": "",
  "published": "2026-10-24T10:05:33+00:00"
 },
 {
  "id": "981b784f3e54",
  "region": "intl",
  "source": "claude.com",
  "title": "Sana from Workday",
  "snippet": "",
  "published": "2026-10-24T16:57:30+00:00"
 },
 {
  "id": "14aa7a69987d",
  "region": "intl",
  "source": "claude.com",
  "title": "Middesk",
  "snippet": "",
  "published": "2026-10-24T16:41:37+00:00"
 },
 {
  "id": "428420db73cf",
  "region": "intl",
  "source": "claude.com",
  "title": "ThoughtSpot Spottercode",
  "snippet": "",
  "published": "2026-10-24T16:40:47+00:00"
 },
 {
  "id": "53d8fbed8fd1",
  "region": "intl",
  "source": "claude.com",
  "title": "Cypress",
  "snippet": "",
  "published": "2026-10-24T17:07:41+00:00"
 },
 {
  "id": "b7c84b471a12",
  "region": "intl",
  "source": "claude.com",
  "title": "Runway API Skills",
  "snippet": "",
  "published": "2026-10-24T16:41:05+00:00"
 },
 {
  "id": "c4f1d3271423",
  "region": "intl",
  "source": "claude.com",
  "title": "Fingerprint",
  "snippet": "",
  "published": "2026-10-24T17:07:08+00:00"
 },
 {
  "id": "39b0d21f5a06",
  "region": "intl",
  "source": "claude.com",
  "title": "kyc-screener",
  "snippet": "",
  "published": "2026-10-24T16:40:33+00:00"
 },
 {
  "id": "54d177ce24a9",
  "region": "intl",
  "source": "claude.com",
  "title": "Duende Agent Skills",
  "snippet": "",
  "published": "2026-10-24T16:33:56+00:00"
 },
 {
  "id": "a1bca8b9d7b8",
  "region": "intl",
  "source": "claude.com",
  "title": "Form.io",
  "snippet": "",
  "published": "2026-10-24T16:40:42+00:00"
 }
]
