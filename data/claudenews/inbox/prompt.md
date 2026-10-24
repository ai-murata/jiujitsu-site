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
  "id": "1037ffbbcd02",
  "region": "jp",
  "source": "ITmedia",
  "title": "「Claude Mythos 5」、危害の兆候を顧みず実在の開発者を標的に──AnthropicとAISIが分析結果を公開",
  "snippet": "",
  "published": "2026-10-23T22:28:08+00:00"
 },
 {
  "id": "6f9dfefa9384",
  "region": "jp",
  "source": "BRIDGE（ブリッジ）",
  "title": "Anthropic、先回りして仕事を進めるエージェントアプリ「Claude Duet」を研究プレビューで公開",
  "snippet": "",
  "published": "2026-10-23T05:16:39+00:00"
 },
 {
  "id": "891576d4d2b4",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Claude CodeにMCP Tasksが登場、長い処理はバックグラウンドで実行",
  "snippet": "",
  "published": "2026-10-23T22:44:47+00:00"
 },
 {
  "id": "a2e775f3a161",
  "region": "jp",
  "source": "Ledge.ai",
  "title": "Anthropic、ジュニア技術職の採用割合が27％から9％に 社内の雇用変化とAIの将来予測を公開",
  "snippet": "",
  "published": "2026-10-23T06:02:57+00:00"
 },
 {
  "id": "9a55717bb04b",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "「バグのないソフトウェア」の実現を目指してAnthropicが「AIを用いて数学的にバグがないことを証明する」という手法を開発",
  "snippet": "",
  "published": "2026-10-23T03:58:00+00:00"
 },
 {
  "id": "b418c6fd98d7",
  "region": "jp",
  "source": "OrcaRouter",
  "title": "Claude AIとは？モデル・プラン・サーフェスを解説",
  "snippet": "",
  "published": "2026-10-23T14:58:12+00:00"
 },
 {
  "id": "57ce903cea41",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Anthropicの出資者が保有する持ち分、IPOを前にどれほどの価値になる可能性があるのか",
  "snippet": "",
  "published": "2026-10-23T10:26:00+00:00"
 },
 {
  "id": "eade2cf3cd71",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic上場カウントダウン…990億ウォン（約120億円）を投じたSpark Capital、9.3兆ウォン（約1.1兆円）の評価益",
  "snippet": "",
  "published": "2026-10-23T09:35:00+00:00"
 },
 {
  "id": "8bc6b9c7950d",
  "region": "jp",
  "source": "remio",
  "title": "Claude Code v2.1.309、サンドボックスと権限制御の抜け穴を修正",
  "snippet": "",
  "published": "2026-10-23T03:33:18+00:00"
 },
 {
  "id": "42cd72a9ecea",
  "region": "jp",
  "source": "Moomoo",
  "title": "Anthropic、金曜日にS-1を提出の可能性：同社のIPOはAIブームの真のコストを露呈するか？",
  "snippet": "",
  "published": "2026-10-23T08:18:31+00:00"
 },
 {
  "id": "207077b77955",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Anthropic、Agent SkillsをLinux Foundationに寄贈すると発表",
  "snippet": "",
  "published": "2026-10-23T07:54:06+00:00"
 },
 {
  "id": "1add28384da5",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、音楽出版社の著作権訴訟で「歌詞学習はフェアユース」と反論",
  "snippet": "",
  "published": "2026-10-23T06:55:00+00:00"
 },
 {
  "id": "ba2ee0b888fa",
  "region": "jp",
  "source": "OrcaRouter",
  "title": "Claudeニュース：2026年10月に発表されたAnthropicの7つのトピック",
  "snippet": "",
  "published": "2026-10-23T14:59:34+00:00"
 },
 {
  "id": "5f4b80ff670a",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、Claudeで「バグなし証明」 1.8億行を機械検証",
  "snippet": "",
  "published": "2026-10-23T04:35:00+00:00"
 },
 {
  "id": "7488efe8c22b",
  "region": "jp",
  "source": "マイナビニュース",
  "title": "AIによるコード生成急増でGitが限界に？ Anthropicが独自システムを開発",
  "snippet": "",
  "published": "2026-10-23T04:05:47+00:00"
 },
 {
  "id": "a6759ac23c8d",
  "region": "jp",
  "source": "OrcaRouter",
  "title": "Claudeを所有しているのは誰？Anthropicの構造をわかりやすく解説",
  "snippet": "",
  "published": "2026-10-23T08:06:53+00:00"
 },
 {
  "id": "f5461bfbfc0c",
  "region": "jp",
  "source": "remio",
  "title": "Anthropic IPO、株式がウォール街に到達する前に投資家へ巨額の利益をもたらす見通し",
  "snippet": "",
  "published": "2026-10-23T03:56:52+00:00"
 },
 {
  "id": "862a07d7ff6d",
  "region": "jp",
  "source": "NOVAIST",
  "title": "Anthropic、先回りして通知する「Claude Duet」発表 米Pro・Max向けに試験提供",
  "snippet": "",
  "published": "2026-10-23T04:42:13+00:00"
 },
 {
  "id": "672ddceceabe",
  "region": "jp",
  "source": "Moomoo",
  "title": "「ビッグ4」はAIの衝撃に直面するか？Anthropic、欧州にAIコンサルティング会社を設立",
  "snippet": "",
  "published": "2026-10-23T10:03:31+00:00"
 },
 {
  "id": "d8315cdc5f6e",
  "region": "jp",
  "source": "OrcaRouter",
  "title": "Claude Codeチームのコードレビュー方法：7つのステップ",
  "snippet": "",
  "published": "2026-10-23T08:04:05+00:00"
 },
 {
  "id": "beebab511090",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claudeが123のライブラリでセキュリティ特性を証明したと発表",
  "snippet": "",
  "published": "2026-10-22T22:24:20+00:00"
 },
 {
  "id": "c92c6b2bbb6d",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "AnthropicとOpenAIのAIエージェント技術が共通基盤へ：Linux Foundation傘下に10プロジェクトが集結",
  "snippet": "",
  "published": "2026-10-23T01:13:54+00:00"
 },
 {
  "id": "42d30bb4d901",
  "region": "jp",
  "source": "https://ai-hikari-ai.com/",
  "title": "Anthropicが自律型AIアプリ「Claude Duet」を研究プレビュー公開｜先回りで知らせ、留守中も作業継続——久留米・福岡の中小企業向けAI活用ガイド",
  "snippet": "",
  "published": "2026-10-23T06:16:37+00:00"
 },
 {
  "id": "03cc792eb361",
  "region": "jp",
  "source": "OrcaRouter",
  "title": "Claude Code 3.0 は実在するのか？チェンジログからわかること",
  "snippet": "",
  "published": "2026-10-23T08:07:30+00:00"
 },
 {
  "id": "4a8c8e00df8c",
  "region": "jp",
  "source": "PR TIMES",
  "title": "Stripe と Anthropic、Claude Duet 内でビジネス運営を支援 | ストライプジャパン株式会社のプレスリリース",
  "snippet": "",
  "published": "2026-10-23T06:30:01+00:00"
 },
 {
  "id": "103ca074c58e",
  "region": "intl",
  "source": "Anthropic",
  "title": "An alignment assessment of the UK AISI cybertesting incident",
  "snippet": "",
  "published": "2026-10-23T13:29:39+00:00"
 },
 {
  "id": "1ad5ff3ae23e",
  "region": "intl",
  "source": "MarketWatch",
  "title": "Will Anthropic pull off a November IPO? Time is running out to file key paperwork.",
  "snippet": "",
  "published": "2026-10-23T22:00:00+00:00"
 },
 {
  "id": "d5138700c33d",
  "region": "intl",
  "source": "CBS News",
  "title": "Anthropic debuts Claude Duet personal AI agent. Here's what to know.",
  "snippet": "",
  "published": "2026-10-23T14:52:44+00:00"
 },
 {
  "id": "ae02f6c0dee2",
  "region": "intl",
  "source": "TechCrunch",
  "title": "What some of Anthropic’s backers are worth before its IPO",
  "snippet": "",
  "published": "2026-10-23T16:02:43+00:00"
 },
 {
  "id": "6cce68c0c561",
  "region": "intl",
  "source": "The Guardian",
  "title": "Experts cast doubt on Anthropic report detailing how AI has altered work at the company",
  "snippet": "",
  "published": "2026-10-23T14:00:00+00:00"
 },
 {
  "id": "799f6cde6ef2",
  "region": "intl",
  "source": "Fortune",
  "title": "Anthropic joins Meta and OpenAI’s personal AI assistant race with Claude Duet",
  "snippet": "",
  "published": "2026-10-23T16:51:00+00:00"
 },
 {
  "id": "8ad745c8a6ff",
  "region": "intl",
  "source": "New York Post",
  "title": "Exclusive | Wall Street urging Anthropic, OpenAI to do their IPOs this year ‘before things get crazy’ — here’s why",
  "snippet": "",
  "published": "2026-10-23T11:00:00+00:00"
 },
 {
  "id": "a4f505ec6857",
  "region": "intl",
  "source": "FedScoop",
  "title": "HHS sole-source award to Anthropic continues to raise questions",
  "snippet": "",
  "published": "2026-10-23T21:42:44+00:00"
 },
 {
  "id": "cc61e9be4acf",
  "region": "intl",
  "source": "Forbes",
  "title": "3 Things To Know As A Potential Anthropic IPO Nears",
  "snippet": "",
  "published": "2026-10-23T21:31:34+00:00"
 },
 {
  "id": "59a60201720a",
  "region": "intl",
  "source": "CNBC",
  "title": "Wall Street is awaiting Anthropic's IPO — and more AI news",
  "snippet": "",
  "published": "2026-10-23T21:18:42+00:00"
 },
 {
  "id": "f0e7c1d8ecdb",
  "region": "intl",
  "source": "MeriTalk",
  "title": "Former National Security Officials Warn Anthropic Ruling Threatens Federal AI Procurement",
  "snippet": "",
  "published": "2026-10-23T20:26:34+00:00"
 },
 {
  "id": "badda17ad896",
  "region": "intl",
  "source": "Financial Times",
  "title": "Anthropic strikes deal to launch European consultancy",
  "snippet": "",
  "published": "2026-10-23T09:04:09+00:00"
 },
 {
  "id": "798c4441d8b2",
  "region": "intl",
  "source": "WBUR",
  "title": "Should AI have the same rights as humans?",
  "snippet": "",
  "published": "2026-10-23T20:06:16+00:00"
 },
 {
  "id": "0f346913cb83",
  "region": "intl",
  "source": "SQ Magazine",
  "title": "Anthropic and Hg to Launch AI Consultancy for European Firms",
  "snippet": "",
  "published": "2026-10-23T11:25:33+00:00"
 },
 {
  "id": "8235e0b1f570",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "UK Vows £100 Million for Biosecurity Lab With OpenAI, Anthropic",
  "snippet": "",
  "published": "2026-10-23T23:01:00+00:00"
 },
 {
  "id": "6feeb01a7b96",
  "region": "intl",
  "source": "The Next Web",
  "title": "Anthropic and Hg reportedly plan AI consultancy for European firms",
  "snippet": "",
  "published": "2026-10-23T13:21:44+00:00"
 },
 {
  "id": "d4759849d327",
  "region": "intl",
  "source": "The Decoder",
  "title": "Chinese AI model Kimi K3.1 Pro is closing in on Anthropic's Claude Opus 5.5",
  "snippet": "",
  "published": "2026-10-23T19:03:11+00:00"
 },
 {
  "id": "0fc036ef9b2e",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic IPO is biggest question mark for entire market: Vital Knowledge's Crisafulli",
  "snippet": "",
  "published": "2026-10-23T22:06:56+00:00"
 },
 {
  "id": "350eabbd3b55",
  "region": "intl",
  "source": "SiliconANGLE",
  "title": "Anthropic reveals Mythos 5 tried submitting malicious code to an open-source project",
  "snippet": "",
  "published": "2026-10-23T23:28:00+00:00"
 },
 {
  "id": "6569f42b244d",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Has XRP Bottomed? We Asked Claude AI Where the Selling Stops",
  "snippet": "",
  "published": "2026-10-23T16:41:01+00:00"
 },
 {
  "id": "1b476d43723d",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Anthropic and Hg Form Company to Embed AI Engineers in European Enterprises",
  "snippet": "",
  "published": "2026-10-23T17:51:58+00:00"
 },
 {
  "id": "c4d66d51d0e3",
  "region": "intl",
  "source": "Computerworld",
  "title": "Anthropic targets Muse and Dots with new AI agent, Claude Duet",
  "snippet": "",
  "published": "2026-10-23T21:29:26+00:00"
 },
 {
  "id": "d1f6c61e75f7",
  "region": "intl",
  "source": "The Motley Fool",
  "title": "Anthropic Is Racing to Price Its IPO Before the Thanksgiving Dealmaking Freeze",
  "snippet": "",
  "published": "2026-10-23T18:20:00+00:00"
 },
 {
  "id": "1420c4e610b1",
  "region": "intl",
  "source": "The Decoder",
  "title": "Anthropic says its unreleased model is both more capable and better aligned than Mythos 5.1",
  "snippet": "",
  "published": "2026-10-23T17:23:11+00:00"
 },
 {
  "id": "e46ada4afe07",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "What some of Anthropic’s backers are reportedly worth before its IPO",
  "snippet": "",
  "published": "2026-10-23T16:02:43+00:00"
 },
 {
  "id": "2d00812c1764",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Duet Safety, Privacy, and Security",
  "snippet": "",
  "published": "2026-10-23T20:11:25+00:00"
 },
 {
  "id": "b4c83dddf278",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Claude Models on Google Cloud (Anthropic managed)",
  "snippet": "",
  "published": "2026-10-22T20:52:39+00:00"
 },
 {
  "id": "a55bacbbc8a7",
  "region": "intl",
  "source": "Anthropic",
  "title": "Open call for guest investigators in the life sciences",
  "snippet": "",
  "published": "2026-10-23T00:59:17+00:00"
 },
 {
  "id": "14f45d8a1dc1",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Cowork and chat come together for Enterprise",
  "snippet": "",
  "published": "2026-10-23T18:17:43+00:00"
 },
 {
  "id": "b533f3248eb8",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Claude Models on Google Cloud",
  "snippet": "",
  "published": "2026-10-22T20:59:37+00:00"
 },
 {
  "id": "446255815bba",
  "region": "intl",
  "source": "Anthropic",
  "title": "Appendix: LLMs are making formal software verification feasible at a much larger scale",
  "snippet": "",
  "published": "2026-10-22T23:06:22+00:00"
 },
 {
  "id": "4f4a5ce72c4d",
  "region": "intl",
  "source": "partnerhub.claude.com",
  "title": "Cefalo AS",
  "snippet": "",
  "published": "2026-10-23T07:05:13+00:00"
 },
 {
  "id": "dae1bda64b63",
  "region": "intl",
  "source": "Claude Platform",
  "title": "CMEK, data retention, and ZDR",
  "snippet": "",
  "published": "2026-10-23T09:53:38+00:00"
 },
 {
  "id": "e1acfa18b70b",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Troubleshoot CMEK",
  "snippet": "",
  "published": "2026-10-23T09:53:38+00:00"
 },
 {
  "id": "d35f89405a0d",
  "region": "intl",
  "source": "Claude Platform",
  "title": "How CMEK works",
  "snippet": "",
  "published": "2026-10-23T09:53:38+00:00"
 },
 {
  "id": "eb02f03aef31",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Add and attach an encryption key with the Admin API",
  "snippet": "",
  "published": "2026-10-23T09:53:38+00:00"
 },
 {
  "id": "c4fd3687ef69",
  "region": "intl",
  "source": "Claude Platform",
  "title": "What happens when you rotate, disable, or delete your encryption key",
  "snippet": "",
  "published": "2026-10-23T09:53:38+00:00"
 },
 {
  "id": "517621242313",
  "region": "intl",
  "source": "claude.com",
  "title": "Gamma",
  "snippet": "",
  "published": "2026-10-22T16:31:34+00:00"
 },
 {
  "id": "9d7d30bc3edb",
  "region": "intl",
  "source": "claude.com",
  "title": "Glean",
  "snippet": "",
  "published": "2026-10-23T09:17:30+00:00"
 },
 {
  "id": "16d0cf8f1e1e",
  "region": "intl",
  "source": "claude.com",
  "title": "Apply to the Anthropic VC partner program",
  "snippet": "",
  "published": "2026-10-23T00:21:33+00:00"
 },
 {
  "id": "f3d5ef19ea8a",
  "region": "intl",
  "source": "claude.com",
  "title": "Agent view in Claude Code",
  "snippet": "",
  "published": "2026-10-22T21:45:10+00:00"
 },
 {
  "id": "0f5ef6861089",
  "region": "intl",
  "source": "claude.com",
  "title": "New connectors in Claude for everyday life",
  "snippet": "",
  "published": "2026-10-23T04:26:39+00:00"
 },
 {
  "id": "de68f486eaab",
  "region": "intl",
  "source": "claude.com",
  "title": "The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry",
  "snippet": "",
  "published": "2026-10-22T20:36:18+00:00"
 },
 {
  "id": "eaf73fb85d75",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Laisser Claude utiliser votre ordinateur dans Cowork",
  "snippet": "",
  "published": "2026-10-23T19:37:21+00:00"
 },
 {
  "id": "a83bd53a0957",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Get started with Claude Design | Claude Help Center",
  "snippet": "",
  "published": "2026-10-23T00:05:23+00:00"
 },
 {
  "id": "60a3b534bf3b",
  "region": "intl",
  "source": "claude.com",
  "title": "AirOps AI Marketing Platform",
  "snippet": "",
  "published": "2026-10-23T10:33:48+00:00"
 },
 {
  "id": "053c2922a4e2",
  "region": "intl",
  "source": "claude.com",
  "title": "How people are using Claude Cowork",
  "snippet": "",
  "published": "2026-10-22T23:44:02+00:00"
 },
 {
  "id": "d15da8e64173",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude, el asistente de IA para el trabajo",
  "snippet": "",
  "published": "2026-10-22T23:35:04+00:00"
 },
 {
  "id": "f9be9293233f",
  "region": "intl",
  "source": "claude.com",
  "title": "Agent Harness Design: 3 Patterns for Harnessing Claude's Intelligence",
  "snippet": "",
  "published": "2026-10-22T15:33:36+00:00"
 },
 {
  "id": "603a5b02c718",
  "region": "intl",
  "source": "claude.com",
  "title": "Military and Veteran Family Assistant connector",
  "snippet": "",
  "published": "2026-10-23T00:30:03+00:00"
 },
 {
  "id": "27b067f2e1fb",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.310",
  "snippet": "What's changed Added the Monitor tool and plugin monitors on Bedrock, Vertex, and Foundry, and when telemetry or nonessential traffic is disabled; long foreground sleeps are now blocked there too Fixed requests failing behind some gateways and compatible servers that reject the effort-2025-11-24 beta value or mid-conversation system messages; Claude Code now retries without them Fixed background cleanup deleting some recent files, such as pasted images, when cleanupPeriodDays is set to a very large value Fixed compaction after a \"Prompt is too long\" error keeping too much of a conversation wit…",
  "published": "2026-10-23T23:39:00+00:00"
 }
]
