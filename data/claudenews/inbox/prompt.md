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
  "id": "f77821e6f69c",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Claude Codeの使用上限がほぼ1日もつように。変えたのは「ファイルの読ませ方」だけ（ライフハッカー・ジャパン）",
  "snippet": "",
  "published": "2026-10-08T00:01:02+00:00"
 },
 {
  "id": "06c1cf8dadaf",
  "region": "jp",
  "source": "ライフハッカー",
  "title": "Claude Codeの使用上限がほぼ1日もつように。変えたのは「ファイルの読ませ方」だけ",
  "snippet": "",
  "published": "2026-10-08T01:20:01+00:00"
 },
 {
  "id": "b07092309daf",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic、「Claude Haiku 5.5」公開 「Haiku 4.5」から大幅性能向上で利用コスト約75％減",
  "snippet": "",
  "published": "2026-10-07T22:25:53+00:00"
 },
 {
  "id": "bd3485a2dadf",
  "region": "jp",
  "source": "BRIDGE（ブリッジ）",
  "title": "Anthropic、小型モデル「Claude Haiku 5.5」を公開——前モデル比コスト平均約75%削減",
  "snippet": "",
  "published": "2026-10-07T22:38:12+00:00"
 },
 {
  "id": "bba09025c02e",
  "region": "jp",
  "source": "合同会社ロケットボーイズ",
  "title": "Anthropic、Cyber Verification Programを拡張―Claude Mythos 5.1など高度なサイバー能力を3段階で提供",
  "snippet": "",
  "published": "2026-10-07T21:00:58+00:00"
 },
 {
  "id": "9668d4e37b7b",
  "region": "jp",
  "source": "Ledge.ai",
  "title": "Anthropic、ロボットは身体作業の74％を実行可能と推計 人間より安く担えるのは全労働時間の0.3％",
  "snippet": "",
  "published": "2026-10-08T01:06:49+00:00"
 },
 {
  "id": "be15702c59d8",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "Anthropic「Claude Haiku 5.5」発表 API料金最大90％減、性能も向上",
  "snippet": "",
  "published": "2026-10-07T23:04:00+00:00"
 },
 {
  "id": "03c95277d281",
  "region": "jp",
  "source": "株式会社マイナビ",
  "title": "Claude Codeのクラウド実行が正式版に 複数の開発作業を並行して実行",
  "snippet": "",
  "published": "2026-10-07T22:35:12+00:00"
 },
 {
  "id": "513fe237468a",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "Anthropic社は、最も強力なAIモデルのテストを拡大する。",
  "snippet": "",
  "published": "2026-10-08T00:17:34+00:00"
 },
 {
  "id": "5834dc58a3b9",
  "region": "jp",
  "source": "窓の杜",
  "title": "Anthropic、「Claude Haiku 5.5」を発表 ～1年ぶりの小型モデル、最速・最安を更新",
  "snippet": "",
  "published": "2026-10-07T20:05:00+00:00"
 },
 {
  "id": "db8c85ba3f8c",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、低コストAI向け「Haiku 5.5」発表 運用コスト75%削減",
  "snippet": "",
  "published": "2026-10-07T18:55:00+00:00"
 },
 {
  "id": "768f3be1bd37",
  "region": "jp",
  "source": "gihyo.jp",
  "title": "Anthropic、Cyber Verification Programを拡大 ——防御・侵入テストなどのセキュリティ業務向けにClaudeの利用制限を緩和",
  "snippet": "",
  "published": "2026-10-07T08:39:00+00:00"
 },
 {
  "id": "52d79852397b",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claude Sonnet 5.5 のキャッシュ読み取りコストを 50% 削減",
  "snippet": "",
  "published": "2026-10-07T19:44:53+00:00"
 },
 {
  "id": "0319184b5dd9",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic、「Claude Haiku 5.5」のAPI料金を「Haiku 4.5」の10分の1に 「Sonnet 5.5」のキャッシュ読み込み料金は半額に",
  "snippet": "",
  "published": "2026-10-07T23:20:36+00:00"
 },
 {
  "id": "8d5eb910d8b1",
  "region": "jp",
  "source": "Ledge.ai",
  "title": "生成AIを巡る問題が各所で噴出 国内の不正アクセス被害公表は最多ペース、日販子会社がAnthropicに書籍を無断販売",
  "snippet": "",
  "published": "2026-10-07T23:06:35+00:00"
 },
 {
  "id": "979c8df4defd",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claude Haiku 5.5 を発表、スモールモデル API の価格を引き下げ",
  "snippet": "",
  "published": "2026-10-07T18:32:37+00:00"
 },
 {
  "id": "fd42ba60f77b",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Anthropic、「Claude Haiku 5.5」を発表 ～1年ぶりの小型モデル、最速・最安を更新 (窓の杜)",
  "snippet": "",
  "published": "2026-10-07T21:05:26+00:00"
 },
 {
  "id": "1b5b20faca90",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "アクセンチュアとAnthropicがAIの安全性評価を行う「組み込み型評価者」チーム設立へ提携（Web担当者Forum）",
  "snippet": "",
  "published": "2026-10-07T06:01:13+00:00"
 },
 {
  "id": "59830214e91c",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic、セキュリティ専門家向け「Cyber Verification Program」を拡充 「Claude Mythos 5.1」も対象に",
  "snippet": "",
  "published": "2026-10-07T03:52:55+00:00"
 },
 {
  "id": "60833e64cc9c",
  "region": "jp",
  "source": "BRIDGE（ブリッジ）",
  "title": "Anthropic、サイバー認証プログラムを拡充——Claudeへのアクセスを3段階に",
  "snippet": "",
  "published": "2026-10-07T02:06:43+00:00"
 },
 {
  "id": "4a11eb4a2c79",
  "region": "jp",
  "source": "千葉テレビ放送株式会社",
  "title": "Anthropic、「Claude Haiku 5.5」を発表 ～1年ぶりの小型モデル、最速・最安を更新／高頻度・コスト重視の用途にピッタリ、「Opus」「Sonnet」の手足にも",
  "snippet": "",
  "published": "2026-10-07T20:19:25+00:00"
 },
 {
  "id": "5dc83e34d505",
  "region": "jp",
  "source": "디지털투데이",
  "title": "Anthropic、低価格モデル「Claude Haiku 5.5」発表 前世代比で運用コスト平均約75%減",
  "snippet": "",
  "published": "2026-10-07T23:20:32+00:00"
 },
 {
  "id": "0141abfe073c",
  "region": "jp",
  "source": "株式会社インプレス",
  "title": "Anthropic、「サイバー検証プログラム」を拡張 防御・レッドチームなど3階層でAIを活用",
  "snippet": "",
  "published": "2026-10-07T03:58:40+00:00"
 },
 {
  "id": "7f0ad45ebece",
  "region": "jp",
  "source": "窓の杜",
  "title": "Anthropic、「Claude for Google Workspace」アドオンをリリース",
  "snippet": "",
  "published": "2026-10-06T21:45:00+00:00"
 },
 {
  "id": "2607e11a14ec",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Anthropic、Claude Haiku 5.5を100万トークン0.10ドルで発表",
  "snippet": "",
  "published": "2026-10-07T21:17:08+00:00"
 },
 {
  "id": "dd6e8c6de49e",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic will be 'most ridiculous IPO' of year, analyst says",
  "snippet": "",
  "published": "2026-10-07T22:29:41+00:00"
 },
 {
  "id": "4188995afad7",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic launches third Claude 5.5 model, expanding AI lineup before planned IPO",
  "snippet": "",
  "published": "2026-10-07T18:07:44+00:00"
 },
 {
  "id": "58f83ddece9b",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic reveals Haiku 5.5 model as AI pricing war intensifies",
  "snippet": "",
  "published": "2026-10-07T18:00:00+00:00"
 },
 {
  "id": "adcb2edcbbca",
  "region": "intl",
  "source": "WSJ",
  "title": "The AI Price War Is Heating Up—and OpenAI Is Gaining Ground on Anthropic",
  "snippet": "",
  "published": "2026-10-08T00:00:00+00:00"
 },
 {
  "id": "1d4d3b2a1975",
  "region": "intl",
  "source": "MarkTechPost",
  "title": "Anthropic Releases Claude Haiku 5.5: A Small Model With 1M Context Priced at $0.10 per Million Input Tokens",
  "snippet": "",
  "published": "2026-10-07T20:38:30+00:00"
 },
 {
  "id": "18cd533c41ac",
  "region": "intl",
  "source": "The New Stack",
  "title": "Anthropic launches Haiku 5.5 at a much lower price",
  "snippet": "",
  "published": "2026-10-07T18:03:46+00:00"
 },
 {
  "id": "ede35b99cfa2",
  "region": "intl",
  "source": "SiliconANGLE",
  "title": "Anthropic releases Claude Haiku 5.5 small model and halves Sonnet 5.5 cache read prices",
  "snippet": "",
  "published": "2026-10-07T22:28:00+00:00"
 },
 {
  "id": "670ab88662ab",
  "region": "intl",
  "source": "South China Morning Post",
  "title": "‘China already has spies’ at US AI labs, claims ex-Anthropic researcher",
  "snippet": "",
  "published": "2026-10-07T23:39:15+00:00"
 },
 {
  "id": "be35b41c9039",
  "region": "intl",
  "source": "Business Insider",
  "title": "Claude Code's creator says he talks to AI like a coworker. Here are his 3 prompting tips.",
  "snippet": "",
  "published": "2026-10-07T16:02:00+00:00"
 },
 {
  "id": "9007e65475c3",
  "region": "intl",
  "source": "9to5Mac",
  "title": "Grok Bot just got a lot smarter thanks to Anthropic’s Claude",
  "snippet": "",
  "published": "2026-10-07T15:02:00+00:00"
 },
 {
  "id": "e775329ae3e2",
  "region": "intl",
  "source": "Dark Reading",
  "title": "Anthropic Gives Vetted Defenders Fewer Claude Guardrails",
  "snippet": "",
  "published": "2026-10-07T21:09:59+00:00"
 },
 {
  "id": "0aaadcbbfacf",
  "region": "intl",
  "source": "HackerNoon",
  "title": "Claude Code Finally Made Me an Engineer After 10 Years in Figma",
  "snippet": "",
  "published": "2026-10-07T22:56:01+00:00"
 },
 {
  "id": "6a46408cb6e9",
  "region": "intl",
  "source": "VentureBeat",
  "title": "Anthropic launches Claude Haiku 5.5 with 90% API price reduction, matching GPT-6 Luna",
  "snippet": "",
  "published": "2026-10-07T18:08:26+00:00"
 },
 {
  "id": "d4bfae0deddc",
  "region": "intl",
  "source": "Unite.AI",
  "title": "Anthropic Releases Claude Haiku 5.5, Cutting Small-Model API Prices",
  "snippet": "",
  "published": "2026-10-07T18:27:02+00:00"
 },
 {
  "id": "cf12b5c029a2",
  "region": "intl",
  "source": "The Business Journals",
  "title": "Data center eyed by Anthropic could break ground soon in Bastrop County",
  "snippet": "",
  "published": "2026-10-08T01:23:00+00:00"
 },
 {
  "id": "08e5e7498c91",
  "region": "intl",
  "source": "Legis1",
  "title": "Anthropic Dispute Highlights Gaps in Pentagon AI Oversight",
  "snippet": "",
  "published": "2026-10-07T16:52:33+00:00"
 },
 {
  "id": "4ab9c6c4090d",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic unveils a new, cheaper Haiku model",
  "snippet": "",
  "published": "2026-10-07T18:30:23+00:00"
 },
 {
  "id": "d9a7861ab2f3",
  "region": "intl",
  "source": "TechTarget",
  "title": "Anthropic opens cyber program applications, releases cheaper Haiku",
  "snippet": "",
  "published": "2026-10-07T22:31:06+00:00"
 },
 {
  "id": "24aa58b8770a",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "SpaceX Still Trades Above Its IPO Price. Could Anthropic Do the Same?",
  "snippet": "",
  "published": "2026-10-07T20:36:00+00:00"
 },
 {
  "id": "330216b8d166",
  "region": "intl",
  "source": "ExecutiveBiz",
  "title": "Anthropic Expands Cyber Verification Program With 3 Access Tiers",
  "snippet": "",
  "published": "2026-10-07T15:47:56+00:00"
 },
 {
  "id": "e4f5b265d2e0",
  "region": "intl",
  "source": "GovTech",
  "title": "How many states are paying more for AI from Anthropic than OpenAI?",
  "snippet": "",
  "published": "2026-10-07T19:51:42+00:00"
 },
 {
  "id": "2166bb5a0f19",
  "region": "intl",
  "source": "BankInfoSecurity",
  "title": "Anthropic Expands Access to Frontier Cyber AI Models",
  "snippet": "",
  "published": "2026-10-07T22:16:15+00:00"
 },
 {
  "id": "f7b8bac77551",
  "region": "intl",
  "source": "Investing.com",
  "title": "Anthropic expands AI model suite with low-cost, high-speed Haiku 5.5 launch",
  "snippet": "",
  "published": "2026-10-07T20:01:05+00:00"
 },
 {
  "id": "cb265e25f437",
  "region": "intl",
  "source": "The Real Deal",
  "title": "Anthropic shifts focus from office to R&D, eyes 100K sf of Mission District industrial",
  "snippet": "",
  "published": "2026-10-07T16:54:00+00:00"
 },
 {
  "id": "48bda31c1ce8",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Watch BofA Sees Strong Demand for OpenAI, Anthropic IPOs",
  "snippet": "",
  "published": "2026-10-07T18:08:43+00:00"
 },
 {
  "id": "c435919116b4",
  "region": "intl",
  "source": "Anthropic",
  "title": "Introducing Claude Haiku 5.5",
  "snippet": "",
  "published": "2026-10-07T18:06:12+00:00"
 },
 {
  "id": "bfb652ff6d82",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Monthly API credits for Max and Team plans | Claude Help Center",
  "snippet": "",
  "published": "2026-10-07T22:53:26+00:00"
 },
 {
  "id": "64fb5051a201",
  "region": "intl",
  "source": "Claude Platform",
  "title": "API credits for Max and Team plans",
  "snippet": "",
  "published": "2026-10-07T17:59:50+00:00"
 },
 {
  "id": "624f715fe806",
  "region": "intl",
  "source": "Claude Platform",
  "title": "What's new in Claude Haiku 5.5",
  "snippet": "",
  "published": "2026-10-07T17:55:52+00:00"
 },
 {
  "id": "2e5f2e69be4b",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Claude Haiku 5.5",
  "snippet": "",
  "published": "2026-10-07T17:55:52+00:00"
 },
 {
  "id": "f0a7e4144022",
  "region": "intl",
  "source": "claude.com",
  "title": "How Comcast and Booz Allen use Claude Mythos to find exploit chains and secure their codebases",
  "snippet": "",
  "published": "2026-10-06T19:54:40+00:00"
 },
 {
  "id": "b9c6c94921e1",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Prompting Claude Haiku 5.5",
  "snippet": "",
  "published": "2026-10-07T17:55:52+00:00"
 },
 {
  "id": "b86ccc99eaed",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Browser and computer use with the SDK toolsets",
  "snippet": "",
  "published": "2026-10-07T18:13:52+00:00"
 },
 {
  "id": "35ba0084f82c",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Release notes | Claude Help Center",
  "snippet": "",
  "published": "2026-10-08T00:05:50+00:00"
 },
 {
  "id": "38dad4139fcf",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Use the Claude Agent SDK with your Claude plan | Claude Help Center",
  "snippet": "",
  "published": "2026-10-07T22:33:28+00:00"
 },
 {
  "id": "810c58be7224",
  "region": "intl",
  "source": "claude.com",
  "title": "Foundations",
  "snippet": "",
  "published": "2026-10-07T10:58:09+00:00"
 },
 {
  "id": "30817be51e3e",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Claude Haiku 5.5 migration guide",
  "snippet": "",
  "published": "2026-10-07T17:55:52+00:00"
 },
 {
  "id": "3e625cec11c0",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Understanding your Pro or Max plan invoices",
  "snippet": "",
  "published": "2026-10-07T17:55:37+00:00"
 },
 {
  "id": "06d850a775b6",
  "region": "intl",
  "source": "Anthropic",
  "title": "Claude in Production: Executive Briefings",
  "snippet": "",
  "published": "2026-10-06T14:52:16+00:00"
 },
 {
  "id": "1ffc7c9ea979",
  "region": "intl",
  "source": "Anthropic",
  "title": "Virtual Claude Code Workshop",
  "snippet": "",
  "published": "2026-10-06T21:52:52+00:00"
 },
 {
  "id": "96210ee1ce89",
  "region": "intl",
  "source": "Anthropic",
  "title": "How to Roadmap With Decisions Rather Than Dates",
  "snippet": "",
  "published": "2026-10-06T16:18:30+00:00"
 },
 {
  "id": "9159493cc50d",
  "region": "intl",
  "source": "Anthropic",
  "title": "Claude Haiku 5.5 System Card",
  "snippet": "",
  "published": "2026-10-07T17:55:52+00:00"
 },
 {
  "id": "7cdb97819472",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Claude Haiku 5.5 system prompts",
  "snippet": "",
  "published": "2026-10-07T17:55:52+00:00"
 },
 {
  "id": "1e192f1c8df2",
  "region": "intl",
  "source": "claude.com",
  "title": "Auto mode is now the default in Claude Code for Pro, Max, and Team plans",
  "snippet": "",
  "published": "2026-10-06T15:33:19+00:00"
 },
 {
  "id": "0edf76ae63b3",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Managed Agents: get to production 10x faster",
  "snippet": "",
  "published": "2026-10-06T20:03:45+00:00"
 },
 {
  "id": "eda5b3ddc05f",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Security is now in public beta",
  "snippet": "",
  "published": "2026-10-06T15:07:48+00:00"
 },
 {
  "id": "8980416216d3",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude builds interactive visuals right in your conversation",
  "snippet": "",
  "published": "2026-10-06T18:33:26+00:00"
 },
 {
  "id": "01e97a8d716c",
  "region": "intl",
  "source": "claude.com",
  "title": "Salesforce in Claude",
  "snippet": "",
  "published": "2026-10-07T01:07:30+00:00"
 },
 {
  "id": "8164a9ffc76a",
  "region": "intl",
  "source": "claude.com",
  "title": "Connector observability and in-app directory submission",
  "snippet": "",
  "published": "2026-10-07T02:10:36+00:00"
 },
 {
  "id": "a62b1b90ed17",
  "region": "intl",
  "source": "claude.com",
  "title": "Bringing Claude Code and Claude Cowork to government",
  "snippet": "",
  "published": "2026-10-06T14:15:00+00:00"
 },
 {
  "id": "4250e365b896",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.293",
  "snippet": "What's changed Added Claude Haiku 5.5 ( claude-haiku-5-5 ), now the default Haiku model on the Anthropic API — 1M context, $0.10/$0.50 per Mtok ($0.50/$2.50 for prompts over 100K) Added agentType to the subagentStatusLine payload, so scripts can tell custom subagent types apart Added isDeferred to $.tool.register for mods: false lists the tool's schema in the prompt from the start instead of behind tool search Fixed Claude sometimes treating its own last actions before a context compaction as done after it, and retracting or redoing finished work Fixed a memory leak where an HTTP MCP connectio…",
  "published": "2026-10-07T18:10:20+00:00"
 }
]
