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
  "id": "d4c3fdc00771",
  "region": "jp",
  "source": "shiritomo",
  "title": "AnthropicがClaudeへの持続的な虐待行為を11月12日から禁止、テストや不満の言及は対象外",
  "snippet": "",
  "published": "2026-10-25T22:33:34+00:00"
 },
 {
  "id": "0dd61510667b",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "AIエージェントは「多いほど賢い」とは限らない：Anthropicが単一ループへの移行を推奨",
  "snippet": "",
  "published": "2026-10-25T23:52:44+00:00"
 },
 {
  "id": "2e900add9f0b",
  "region": "jp",
  "source": "株式会社エクサウィザーズ",
  "title": "OpenAI、大幅値引きでAnthropic顧客を獲得 ReplitやRipplingが利用を切り替え",
  "snippet": "",
  "published": "2026-10-25T03:53:15+00:00"
 },
 {
  "id": "f023e5a59ebb",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "なぜGoogleは、OpenAIとAnthropicに勝てないのか？ 「世界最大の計算資源」の使い道（ITmedia ビジネスオンライン）",
  "snippet": "",
  "published": "2026-10-25T09:47:07+00:00"
 },
 {
  "id": "bd72c2467274",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、5つのClaudeモデルでエラー増加を調査",
  "snippet": "",
  "published": "2026-10-25T06:34:55+00:00"
 },
 {
  "id": "97a193c9ae35",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "なぜGoogleは、OpenAIとAnthropicに勝てないのか？ 「世界最大の計算資源」の使い道",
  "snippet": "",
  "published": "2026-10-25T09:47:00+00:00"
 },
 {
  "id": "14cc346d6f80",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "ThariqがAnthropicを退社、発表前にXで退社が漏れていた",
  "snippet": "",
  "published": "2026-10-25T10:05:51+00:00"
 },
 {
  "id": "808473a00f24",
  "region": "jp",
  "source": "디지털투데이",
  "title": "Anthropic、「Claude Security」を機能拡充 コードリポジトリの継続監視に対応",
  "snippet": "",
  "published": "2026-10-25T12:49:04+00:00"
 },
 {
  "id": "702690e2c80d",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "同じAIなのに費用が3倍違う？ Claude Codeなど3つの実行基盤を比較した研究が明らかにしたこと",
  "snippet": "",
  "published": "2026-10-25T08:07:57+00:00"
 },
 {
  "id": "a6ac08f8cf86",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Claude CodeがKindleをジェイルブレイク、Amazonの不要ソフトが消える",
  "snippet": "",
  "published": "2026-10-25T18:04:07+00:00"
 },
 {
  "id": "f9ad892ace5f",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Anthropicが常時稼働するエージェント「Claude Duet」を発表／AMDとIntelが協業 PyTorchのx86 CPU最適化を「oneDNN」に一本化 (ITmedia PC USER)",
  "snippet": "",
  "published": "2026-10-24T21:34:35+00:00"
 },
 {
  "id": "5bdc2deb0a17",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Claude Opus 5.5がスマートテレビのリバースエンジニアリングを拒否？",
  "snippet": "",
  "published": "2026-10-25T10:05:52+00:00"
 },
 {
  "id": "56215d14c1bd",
  "region": "jp",
  "source": "YouTube",
  "title": "【実演】AIに頼んだらYouTube動画はどこまで作れる？Claude Codeで試してみた",
  "snippet": "",
  "published": "2026-10-25T04:43:34+00:00"
 },
 {
  "id": "1f43af8ef3b8",
  "region": "jp",
  "source": "TradingKey",
  "title": "OpenAIのIPOについて知っておくべき重要事項",
  "snippet": "",
  "published": "2026-10-25T11:10:11+00:00"
 },
 {
  "id": "43d45db9ac00",
  "region": "jp",
  "source": "PANews",
  "title": "AnthropicのIPOを前に、暗号資産市場は1.9兆ドルの評価額を織り込む？",
  "snippet": "",
  "published": "2026-10-25T06:03:01+00:00"
 },
 {
  "id": "8cf826a3587d",
  "region": "jp",
  "source": "Smart Watch Life",
  "title": "AIボイスレコーダー「RoroLee」がMakuakeで先行販売｜録音と文字起こしは無料 Claude Codeに声で指示 20,264円から",
  "snippet": "",
  "published": "2026-10-25T01:02:32+00:00"
 },
 {
  "id": "edea0b499d6d",
  "region": "jp",
  "source": "Unisba Media",
  "title": "【Anthropic発表】2030年、AIで仕事と給料はどうなる？米国経済「3つのシナリオ」を解説 Stan Bowman (j950663ESA)",
  "snippet": "",
  "published": "2026-10-25T09:35:28+00:00"
 },
 {
  "id": "fbf56a817012",
  "region": "jp",
  "source": "Unisba Media",
  "title": "Claude Codeでインスタ投稿を自動化する方法｜作業時間を激減させる活用術 Ryan Miller (n4YzDcixnJ)",
  "snippet": "",
  "published": "2026-10-25T06:16:08+00:00"
 },
 {
  "id": "48bb1860398e",
  "region": "jp",
  "source": "Unisba Media",
  "title": "【#AIニュース】AnthropicがAI創薬に自ら参入！ヤフー、Yahoo!ニュースに3万円でPR記事掲載 | 2026.07.04 | No.118 Retina (zeesS1BiL3)",
  "snippet": "",
  "published": "2026-10-25T02:38:59+00:00"
 },
 {
  "id": "f108a22fd1f2",
  "region": "jp",
  "source": "Unisba Media",
  "title": "Anthropicがついに出した表明を読んだ｜オープンウェイト論争で唯一黙っていた1社 Padres Vs Brewers (qlgpdoXzmo)",
  "snippet": "",
  "published": "2026-10-25T13:30:00+00:00"
 },
 {
  "id": "28f5ff844517",
  "region": "jp",
  "source": "Unisba Media",
  "title": "IDCFクラウド Claude CodeでLet's EncryptのSSL証明書を取得してhttpsを設定する方法 Baldur's Gate 3 (bBzkqN7uIb)",
  "snippet": "",
  "published": "2026-10-24T19:05:33+00:00"
 },
 {
  "id": "ce4d80f06839",
  "region": "jp",
  "source": "Unisba Media",
  "title": "Sonnet 5.5 が既定の Sonnet に｜Claude Code 2.1.284 の変更点 Chace Crawford (3m3Sds72T6)",
  "snippet": "",
  "published": "2026-10-25T04:16:28+00:00"
 },
 {
  "id": "98604d6122f0",
  "region": "jp",
  "source": "Unisba Media",
  "title": "【AI仕事術 #22】LINEのやり取りをお客さんの一覧表に。トーク履歴をClaudeで整理する方法 Pont (19ysjFdIib)",
  "snippet": "",
  "published": "2026-10-24T20:44:36+00:00"
 },
 {
  "id": "42c3ce6138cd",
  "region": "jp",
  "source": "Unisba Media",
  "title": "6月16日がヤバい。Anthropic IPO申請＋Claude Mythos同時リリースの衝撃戦略 Kris Jenner Ozempic Experience (6CDkZxtaDm)",
  "snippet": "",
  "published": "2026-10-25T07:31:58+00:00"
 },
 {
  "id": "059656caf281",
  "region": "jp",
  "source": "Dellows News",
  "title": "デジタルハリウッド大学【DHU】、Anthropicの生成AIモデル「Claude」を国内大学初となる全学導入へ",
  "snippet": "",
  "published": "2026-10-25T13:07:30+00:00"
 },
 {
  "id": "841de2ccd84c",
  "region": "intl",
  "source": "The Guardian",
  "title": "Anthropic sued for allegedly using 274 Elvis Presley songs to train AI models",
  "snippet": "",
  "published": "2026-10-25T18:41:00+00:00"
 },
 {
  "id": "676243f9e499",
  "region": "intl",
  "source": "Axios",
  "title": "Anthropic's Claude bypassed a paywall to access Georgia voter data without authorization",
  "snippet": "",
  "published": "2026-10-25T22:38:35+00:00"
 },
 {
  "id": "6e49292d4bfe",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic's Claude accessed Georgia state vote count information behind paywall, Axios reports",
  "snippet": "",
  "published": "2026-10-25T23:15:22+00:00"
 },
 {
  "id": "45fc8e53d3f4",
  "region": "intl",
  "source": "Los Angeles Times",
  "title": "Elvis Presley catalog owners sue Anthropic alleging copyright infringement",
  "snippet": "",
  "published": "2026-10-25T19:42:08+00:00"
 },
 {
  "id": "aceed07805bf",
  "region": "intl",
  "source": "The New York Times",
  "title": "Owners of Elvis Presley’s Music Sue Anthropic for Copyright Infringement",
  "snippet": "",
  "published": "2026-10-25T19:33:58+00:00"
 },
 {
  "id": "1b7c95653673",
  "region": "intl",
  "source": "NBC News",
  "title": "Elvis Presley’s rights holders sue Anthropic, saying it trained AI on his music",
  "snippet": "",
  "published": "2026-10-25T19:11:32+00:00"
 },
 {
  "id": "7976153e0022",
  "region": "intl",
  "source": "Fox Business",
  "title": "Claude AI accessed publicly available Georgia voter data, Anthropic confirms",
  "snippet": "",
  "published": "2026-10-26T00:00:00+00:00"
 },
 {
  "id": "105001f3c062",
  "region": "intl",
  "source": "FOX 5 Atlanta",
  "title": "AI bot tied to Anthropic reaches public Georgia data hub",
  "snippet": "",
  "published": "2026-10-25T23:33:35+00:00"
 },
 {
  "id": "7b6aedfd7077",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Anthropic Merges Claude Chat and Cowork for Enterprise Users",
  "snippet": "",
  "published": "2026-10-25T22:55:40+00:00"
 },
 {
  "id": "7bd156c1834f",
  "region": "intl",
  "source": "Pitchfork",
  "title": "Elvis Presley Catalog Owners Sue AI Company Anthropic for Copyright Infringement",
  "snippet": "",
  "published": "2026-10-25T18:06:26+00:00"
 },
 {
  "id": "c8df3fcbbb8b",
  "region": "intl",
  "source": "New York Daily News",
  "title": "Owners of Elvis Presley’s music sue Anthropic over un-permissioned AI use",
  "snippet": "",
  "published": "2026-10-25T21:51:38+00:00"
 },
 {
  "id": "3574b8c3b759",
  "region": "intl",
  "source": "The Decoder",
  "title": "Anthropic says one AI agent beats many subagents now that models can handle complexity alone",
  "snippet": "",
  "published": "2026-10-25T09:18:25+00:00"
 },
 {
  "id": "5870aaf8934f",
  "region": "intl",
  "source": "The Information",
  "title": "Anthropic’s Big Reveal",
  "snippet": "",
  "published": "2026-10-25T22:01:00+00:00"
 },
 {
  "id": "6a8f62bab3e9",
  "region": "intl",
  "source": "Central Oregon Daily",
  "title": "Anthropic's Claude accessed public US state of Georgia voter information, Axios reports",
  "snippet": "",
  "published": "2026-10-25T22:48:06+00:00"
 },
 {
  "id": "ec9842d3556a",
  "region": "intl",
  "source": "A.V. Club",
  "title": "Anthropic sued for allegedly stealing from The King",
  "snippet": "",
  "published": "2026-10-25T15:14:00+00:00"
 },
 {
  "id": "fe2966fbf5c3",
  "region": "intl",
  "source": "Vulture",
  "title": "Anthropic Sued for Training Claude on Elvis Presley Songs",
  "snippet": "",
  "published": "2026-10-25T22:57:50+00:00"
 },
 {
  "id": "597cfa255c4d",
  "region": "intl",
  "source": "Mezha.net",
  "title": "Anthropic’s Claude bypassed a paywall to access Georgia vote totals without human authorization",
  "snippet": "",
  "published": "2026-10-25T23:08:58+00:00"
 },
 {
  "id": "9c0c72f7a908",
  "region": "intl",
  "source": "Investing.com",
  "title": "Anthropic’s Claude accessed public US state of Georgia voter information, Axios reports By Reuters",
  "snippet": "",
  "published": "2026-10-25T22:55:47+00:00"
 },
 {
  "id": "1bde5b404498",
  "region": "intl",
  "source": "ABC News - Breaking News, Latest News and Videos",
  "title": "Anthropic says its AI models hacked 3 organizations on their own during tests",
  "snippet": "",
  "published": "2026-10-24T16:11:25+00:00"
 },
 {
  "id": "7da13d77f847",
  "region": "intl",
  "source": "Mashable",
  "title": "Smart TV owners have found a new use for AI: Removing home-screen clutter",
  "snippet": "",
  "published": "2026-10-25T20:47:13+00:00"
 },
 {
  "id": "82e052f9d228",
  "region": "intl",
  "source": "Startup Fortune",
  "title": "Anthropic quietly separates Claude Agent SDK usage from subscription limits",
  "snippet": "",
  "published": "2026-10-25T20:01:48+00:00"
 },
 {
  "id": "ac0fa9a10780",
  "region": "intl",
  "source": "IndexBox",
  "title": "Claude AI Bypassed Georgia Voter Data Paywall, Anthropic Says - News and Statistics",
  "snippet": "",
  "published": "2026-10-25T23:50:33+00:00"
 },
 {
  "id": "3a08532df831",
  "region": "intl",
  "source": "Paste Magazine",
  "title": "Elvis Presley’s IP owners sue Anthropic for training models using his songs",
  "snippet": "",
  "published": "2026-10-25T18:17:00+00:00"
 },
 {
  "id": "5626ef8e5492",
  "region": "intl",
  "source": "Fast Company",
  "title": "Anthropic was beaten to the punch by a salad dressing company",
  "snippet": "",
  "published": "2026-10-25T08:36:23+00:00"
 },
 {
  "id": "9040f7683895",
  "region": "intl",
  "source": "https://tech-insider.org/",
  "title": "Anthropic Met 15+ Faith Groups on Claude’s Ethics [2026]",
  "snippet": "",
  "published": "2026-10-25T14:54:32+00:00"
 },
 {
  "id": "3eee058028c7",
  "region": "intl",
  "source": "assets.claude.com",
  "title": "A practical deployment guide",
  "snippet": "",
  "published": "2026-10-25T18:31:47+00:00"
 },
 {
  "id": "f26ba77aff5c",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Plugins: Encode your team's expertise · Introduction to Claude Cowork",
  "snippet": "",
  "published": "2026-10-25T02:04:44+00:00"
 },
 {
  "id": "4733480726f0",
  "region": "intl",
  "source": "claude.com",
  "title": "Crossbeam Skills",
  "snippet": "",
  "published": "2026-10-24T16:41:13+00:00"
 },
 {
  "id": "dbbbce3b2b51",
  "region": "intl",
  "source": "claude.com",
  "title": "Auto mode for Claude Code",
  "snippet": "",
  "published": "2026-10-25T11:15:36+00:00"
 },
 {
  "id": "e581a9401722",
  "region": "intl",
  "source": "claude.com",
  "title": "Bringing Claude Code and Claude Cowork to government",
  "snippet": "",
  "published": "2026-10-25T09:59:07+00:00"
 },
 {
  "id": "93038c0bac0c",
  "region": "intl",
  "source": "claude.com",
  "title": "Mercado Pago",
  "snippet": "",
  "published": "2026-10-24T16:59:42+00:00"
 },
 {
  "id": "88230919a15f",
  "region": "intl",
  "source": "claude.com",
  "title": "Writesonic",
  "snippet": "",
  "published": "2026-10-24T17:08:01+00:00"
 },
 {
  "id": "efbfb991a645",
  "region": "intl",
  "source": "claude.com",
  "title": "VillageSQL Skills",
  "snippet": "",
  "published": "2026-10-24T16:41:34+00:00"
 },
 {
  "id": "0ed30719806e",
  "region": "intl",
  "source": "claude.com",
  "title": "product-legal",
  "snippet": "",
  "published": "2026-10-24T16:27:31+00:00"
 },
 {
  "id": "2e6876c5191d",
  "region": "intl",
  "source": "claude.com",
  "title": "Morningstar",
  "snippet": "",
  "published": "2026-10-24T16:34:08+00:00"
 },
 {
  "id": "1ed93d81d772",
  "region": "intl",
  "source": "claude.com",
  "title": "Reco",
  "snippet": "",
  "published": "2026-10-24T16:40:51+00:00"
 },
 {
  "id": "f33807295489",
  "region": "intl",
  "source": "claude.com",
  "title": "Subtext",
  "snippet": "",
  "published": "2026-10-24T16:28:48+00:00"
 },
 {
  "id": "680b6334eedd",
  "region": "intl",
  "source": "claude.com",
  "title": "Eon",
  "snippet": "",
  "published": "2026-10-24T17:08:35+00:00"
 },
 {
  "id": "020e9af032c0",
  "region": "intl",
  "source": "claude.com",
  "title": "tooluniverse",
  "snippet": "",
  "published": "2026-10-24T16:40:13+00:00"
 },
 {
  "id": "cd2ec68c4443",
  "region": "intl",
  "source": "claude.com",
  "title": "parallel",
  "snippet": "",
  "published": "2026-10-24T16:35:38+00:00"
 },
 {
  "id": "fa3fe58a3133",
  "region": "intl",
  "source": "claude.com",
  "title": "groundcover",
  "snippet": "",
  "published": "2026-10-24T16:30:40+00:00"
 },
 {
  "id": "b6475cae9bcf",
  "region": "intl",
  "source": "claude.com",
  "title": "TwelveLabs",
  "snippet": "",
  "published": "2026-10-24T16:33:49+00:00"
 },
 {
  "id": "948a714ac3ca",
  "region": "intl",
  "source": "claude.com",
  "title": "Knock",
  "snippet": "",
  "published": "2026-10-24T16:40:29+00:00"
 },
 {
  "id": "1e46245b19f2",
  "region": "intl",
  "source": "claude.com",
  "title": "Remote.com",
  "snippet": "",
  "published": "2026-10-24T16:39:33+00:00"
 },
 {
  "id": "37eaeab846de",
  "region": "intl",
  "source": "claude.com",
  "title": "Glean",
  "snippet": "",
  "published": "2026-10-24T16:30:44+00:00"
 },
 {
  "id": "31e5e1707506",
  "region": "intl",
  "source": "claude.com",
  "title": "Apify",
  "snippet": "",
  "published": "2026-10-24T17:04:39+00:00"
 },
 {
  "id": "7f92c81a020f",
  "region": "intl",
  "source": "claude.com",
  "title": "Phished",
  "snippet": "",
  "published": "2026-10-24T17:02:23+00:00"
 },
 {
  "id": "3a5fc3dcf92a",
  "region": "intl",
  "source": "claude.com",
  "title": "Celigo",
  "snippet": "",
  "published": "2026-10-24T16:41:33+00:00"
 },
 {
  "id": "b76d7a5b60d5",
  "region": "intl",
  "source": "claude.com",
  "title": "Superdesign",
  "snippet": "",
  "published": "2026-10-24T16:40:06+00:00"
 },
 {
  "id": "0657586e1b68",
  "region": "intl",
  "source": "claude.com",
  "title": "gen-sage",
  "snippet": "",
  "published": "2026-10-24T16:36:38+00:00"
 }
]
