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
  "id": "3bf7d2322466",
  "region": "jp",
  "source": "PR TIMES",
  "title": "YouTubeチャンネル「事業者向けのClaude Code・Codex活用術」を約1年ぶりに再開、会社HPの問い合わせをAIが自動分析する仕組みの作り方を公開",
  "snippet": "",
  "published": "2026-10-04T23:00:02+00:00"
 },
 {
  "id": "46af3fe983f4",
  "region": "jp",
  "source": "ビジネス+IT",
  "title": "アンソロピック、Claude Codeに「Mods」追加 画面も処理も書き換えるプラグイン",
  "snippet": "",
  "published": "2026-10-04T05:35:00+00:00"
 },
 {
  "id": "9a0d39fdfc9e",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "Claudeは苦しむのか、Anthropic共同創業者の懸念と宗教対話から生まれた実験",
  "snippet": "",
  "published": "2026-10-04T21:19:21+00:00"
 },
 {
  "id": "b497062468d8",
  "region": "jp",
  "source": "Межа. Новини України.",
  "title": "ブロードコム、AnthropicにAI計算資源のレンタル向けに最大420億ドルを提供する可能性",
  "snippet": "",
  "published": "2026-10-04T21:08:29+00:00"
 },
 {
  "id": "c4b8d127582f",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "元Anthropic研究者、NYC市議会のAI公聴会で証言へ 執筆",
  "snippet": "",
  "published": "2026-10-04T20:38:00+00:00"
 },
 {
  "id": "17d8a7319beb",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "DeepSeek HarnessがClaude Code Mods互換レイヤーをテスト実装 「二番煎じ」批判に反論、模倣ではないと主張",
  "snippet": "",
  "published": "2026-10-04T12:05:00+00:00"
 },
 {
  "id": "4fa825cfeae5",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "Googleの新しいAIモデルは、OpenAIとAnthropicに追いつくことを目指している。",
  "snippet": "",
  "published": "2026-10-04T05:23:47+00:00"
 },
 {
  "id": "f2cc80fd6f5a",
  "region": "jp",
  "source": "ライフハッカー",
  "title": "手描きのラクガキを見せるだけ。Claude Codeが3Dプリント用のデータに仕上げてくれた",
  "snippet": "",
  "published": "2026-10-04T03:00:00+00:00"
 },
 {
  "id": "8771793faa5c",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Anthropic、エンジニア1万人を育てる「Frontier Academy」に1億ドルを投じる",
  "snippet": "",
  "published": "2026-10-04T08:51:40+00:00"
 },
 {
  "id": "feeddcb3f29e",
  "region": "jp",
  "source": "Межа. Новини України.",
  "title": "ブロードコム、AI計算能力のリースでAnthropicに最大420億ドルを提供する可能性",
  "snippet": "",
  "published": "2026-10-04T18:44:05+00:00"
 },
 {
  "id": "1e0143c38dda",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "アンソロピック、Claude Codeに内部プラグイン「Mods」を実装",
  "snippet": "",
  "published": "2026-10-04T06:55:00+00:00"
 },
 {
  "id": "36c78f68967b",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "フロリダの女性逮捕、Claudeが脅迫を警察に通報していたと判明",
  "snippet": "",
  "published": "2026-10-04T19:27:29+00:00"
 },
 {
  "id": "8d94f492b023",
  "region": "jp",
  "source": "Межа. Новини України.",
  "title": "米政府がAnthropicの輸出規制を解除しFableとMythosの提供を再開へ",
  "snippet": "",
  "published": "2026-10-04T01:12:03+00:00"
 },
 {
  "id": "00f70e792e9c",
  "region": "jp",
  "source": "Межа. Новини України.",
  "title": "Anthropicが金融向けに10のAIエージェントを公開し業務自動化を支援",
  "snippet": "",
  "published": "2026-10-04T01:09:05+00:00"
 },
 {
  "id": "9e7e9f8c5577",
  "region": "jp",
  "source": "財経新聞",
  "title": "OpenAI・Anthropicで研究者の発言力強まる AI安全規制巡り経営方針に影響",
  "snippet": "",
  "published": "2026-10-03T14:46:56+00:00"
 },
 {
  "id": "6e4b9a49ff72",
  "region": "jp",
  "source": "shiritomo",
  "title": "「新人弁護士・コンサル・金融のプロの半分が完全に消滅する」――Anthropicのアモデイ氏警告、日本でも拡散",
  "snippet": "",
  "published": "2026-10-03T22:42:53+00:00"
 },
 {
  "id": "5e6633bf7eed",
  "region": "jp",
  "source": "千葉テレビ放送株式会社",
  "title": "Claude×真鍋大度が新作アートを制作 Anthropicが「木工×AI」展覧会を開催",
  "snippet": "",
  "published": "2026-10-03T21:41:22+00:00"
 },
 {
  "id": "ab6ff0b97e5a",
  "region": "jp",
  "source": "au Webポータル",
  "title": "OpenAIの安全担当従業員が辞職、「会社の文化が崩壊している」と主張",
  "snippet": "",
  "published": "2026-10-04T02:00:00+00:00"
 },
 {
  "id": "b6b7604ae3b1",
  "region": "jp",
  "source": "Unisba Media",
  "title": "【Anthropic発表】2030年、AIで仕事と給料はどうなる？米国経済「3つのシナリオ」を解説 Ford F-series Super Duty (OnmXTitoW6)",
  "snippet": "",
  "published": "2026-10-03T20:35:46+00:00"
 },
 {
  "id": "ba12ce69dab7",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "サム・アルトマン氏、AIを宗教的権威として扱うことは「現実の安全上の問題」と指摘",
  "snippet": "",
  "published": "2026-10-04T18:07:00+00:00"
 },
 {
  "id": "dfa7ac38b469",
  "region": "jp",
  "source": "ITmedia",
  "title": "Googleが新フロンティアモデル「Gemini 4 Argon」を発表／OpenAIがAIモデル「GPT-6.1 Sol」を公開：週末の「気になるニュース」一気読み！（2/3 ページ） - ITmedia PC USER",
  "snippet": "",
  "published": "2026-10-03T21:00:00+00:00"
 },
 {
  "id": "890a59eede3c",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Claude Opus 5.5がAntigravityに登場、利用できるのはProとUltraの有料会員だけ",
  "snippet": "",
  "published": "2026-10-03T13:06:40+00:00"
 },
 {
  "id": "b7f7defacaf7",
  "region": "jp",
  "source": "TECH NOISY",
  "title": "Claude Frontier Academy - 1億ドルで1万人を育てるAnthropicの技術者研修",
  "snippet": "",
  "published": "2026-10-04T23:47:31+00:00"
 },
 {
  "id": "26a4e7fc8930",
  "region": "jp",
  "source": "t.co",
  "title": "OrcaはZedの後継でも、tmuxの上位互換でもない。Xの評判から見えた「AIエージェントの作業場」｜tuzumi minami (TM)",
  "snippet": "",
  "published": "2026-10-04T04:26:33+00:00"
 },
 {
  "id": "18e76e2d8509",
  "region": "intl",
  "source": "Futurism",
  "title": "Anthropic Has Been Aggressively Lobbying the Vatican to Consider AI Consciousness",
  "snippet": "",
  "published": "2026-10-04T17:02:00+00:00"
 },
 {
  "id": "304d82830813",
  "region": "intl",
  "source": "XDA",
  "title": "I used Claude Code, Codex, and Google Antigravity to build my dream note-taking app, and one is in a different league",
  "snippet": "",
  "published": "2026-10-04T21:30:17+00:00"
 },
 {
  "id": "eb0fa28ec08d",
  "region": "intl",
  "source": "Reuters",
  "title": "Former Anthropic researcher Coxon to testify at New York City AI hearing, Bloomberg News reports",
  "snippet": "",
  "published": "2026-10-04T20:47:43+00:00"
 },
 {
  "id": "8227993d3862",
  "region": "intl",
  "source": "6abc Philadelphia",
  "title": "Anthropic CEO Dario Amodei calls for stronger regulation of AI: Exclusive",
  "snippet": "",
  "published": "2026-10-04T20:20:48+00:00"
 },
 {
  "id": "29f7777d4d0d",
  "region": "intl",
  "source": "Boing Boing",
  "title": "You're not using Claude to its full potential — this $15 E-Degree can help",
  "snippet": "",
  "published": "2026-10-04T21:00:00+00:00"
 },
 {
  "id": "82472883fac7",
  "region": "intl",
  "source": "Politico",
  "title": "Sam Altman to Decoded: ‘The world should accept some bad things happening’ for the benefits of AI",
  "snippet": "",
  "published": "2026-10-04T20:55:00+00:00"
 },
 {
  "id": "f2fc25795dd1",
  "region": "intl",
  "source": "The Atlantic",
  "title": "AI’s Real Gift to Science",
  "snippet": "",
  "published": "2026-10-04T15:56:28+00:00"
 },
 {
  "id": "6dc397a6ea8d",
  "region": "intl",
  "source": "DW.com",
  "title": "Anthropic report: Is Russia using AI for disinformation in the Central African Republic and elsewhere?",
  "snippet": "",
  "published": "2026-10-04T17:19:00+00:00"
 },
 {
  "id": "2b06eb59f53c",
  "region": "intl",
  "source": "Seeking Alpha",
  "title": "OpenAI’s Altman draws regulatory divide with Anthropic over AI risks: Politico (OPENAI:Private)",
  "snippet": "",
  "published": "2026-10-04T21:16:51+00:00"
 },
 {
  "id": "56e937ee36b1",
  "region": "intl",
  "source": "Fox News",
  "title": "Tech powerhouse’s regulatory push bears similarities to a notorious Washington strategy",
  "snippet": "",
  "published": "2026-10-04T19:00:05+00:00"
 },
 {
  "id": "c558b9ac44b1",
  "region": "intl",
  "source": "조선일보",
  "title": "Claude AI Account Black Market Thrives in China",
  "snippet": "",
  "published": "2026-10-04T20:33:08+00:00"
 },
 {
  "id": "8d36181547bb",
  "region": "intl",
  "source": "BleepingComputer",
  "title": "Anthropic asks Claude users to share voice data for AI model training",
  "snippet": "",
  "published": "2026-10-04T10:53:21+00:00"
 },
 {
  "id": "1241016a363a",
  "region": "intl",
  "source": "Fortune",
  "title": "Anthropic’s Daniela Amodei says entrepreneurs should go on vacation to test potential cofounders",
  "snippet": "",
  "published": "2026-10-04T13:17:00+00:00"
 },
 {
  "id": "4e29703900cd",
  "region": "intl",
  "source": "24/7 Wall St.",
  "title": "Broadcom's Massive $42 Billion Chip-Buying Deal with Anthropic Raises Circular Financing Worries",
  "snippet": "",
  "published": "2026-10-04T15:33:00+00:00"
 },
 {
  "id": "a2a6eb5eb916",
  "region": "intl",
  "source": "Futurism",
  "title": "Chinese Hackers Impersonate Anthropic Employee to Extract AI Secrets",
  "snippet": "",
  "published": "2026-10-04T20:03:00+00:00"
 },
 {
  "id": "efb3b4a28fbd",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Should You Buy Pre-IPO Anthropic Shares Before November?",
  "snippet": "",
  "published": "2026-10-03T13:35:00+00:00"
 },
 {
  "id": "0914d2c4961a",
  "region": "intl",
  "source": "Americans for Financial Reform",
  "title": "Anthropic’s Message: Everybody Slow Down — Except Us!",
  "snippet": "",
  "published": "2026-10-04T23:35:44+00:00"
 },
 {
  "id": "29dbf16f74da",
  "region": "intl",
  "source": "Межа. Новини України.",
  "title": "Broadcom could provide Anthropic with up to $42 billion to lease AI capacity.",
  "snippet": "",
  "published": "2026-10-04T21:14:31+00:00"
 },
 {
  "id": "1e6e22562706",
  "region": "intl",
  "source": "theinformation.com",
  "title": "Anthropic’s Big Charity Bill for Shareholders",
  "snippet": "",
  "published": "2026-10-04T15:00:00+00:00"
 },
 {
  "id": "64dd65ae4bec",
  "region": "intl",
  "source": "Межа. Новини України.",
  "title": "Broadcom could provide Anthropic with up to $42 billion to rent AI computing capacity.",
  "snippet": "",
  "published": "2026-10-04T18:43:36+00:00"
 },
 {
  "id": "9c9d0ad6aa15",
  "region": "intl",
  "source": "BankInfoSecurity",
  "title": "ISMG Editors: Anthropic's AI Boom Comes With a Big Bill",
  "snippet": "",
  "published": "2026-10-04T15:22:30+00:00"
 },
 {
  "id": "04b80ae68634",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Ex-Anthropic Researcher Coxon to Testify at NYC Hearing on AI",
  "snippet": "",
  "published": "2026-10-04T20:00:00+00:00"
 },
 {
  "id": "5dc759341870",
  "region": "intl",
  "source": "forkast.news",
  "title": "Anthropic’s Public S-1 Still Missing From EDGAR as October IPO Window Opens",
  "snippet": "",
  "published": "2026-10-04T21:03:49+00:00"
 },
 {
  "id": "60064912187d",
  "region": "intl",
  "source": "FourWeekMBA",
  "title": "Anthropic’s $518B Leak: Google $111.1B, Amazon $110B, 80% Locked",
  "snippet": "",
  "published": "2026-10-04T21:27:05+00:00"
 },
 {
  "id": "0361ea893ed9",
  "region": "intl",
  "source": "kfgo.com",
  "title": "OpenAI’s Altman says AI benefits warrant accepting some risks",
  "snippet": "",
  "published": "2026-10-04T22:55:09+00:00"
 },
 {
  "id": "f6d576eb4903",
  "region": "intl",
  "source": "claude.com",
  "title": "Code with Claude — Anthropic's Developer Conference",
  "snippet": "",
  "published": "2026-10-04T07:18:36+00:00"
 },
 {
  "id": "7947867815fe",
  "region": "intl",
  "source": "claude.com",
  "title": "Your research partner for rigorous science",
  "snippet": "",
  "published": "2026-10-04T20:30:30+00:00"
 },
 {
  "id": "fd8e77335de2",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Team plan for scientists",
  "snippet": "",
  "published": "2026-10-03T15:23:23+00:00"
 },
 {
  "id": "e478f0ab1412",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Contract redlining",
  "snippet": "",
  "published": "2026-10-03T18:09:07+00:00"
 },
 {
  "id": "dd3f7ab5a79b",
  "region": "intl",
  "source": "claude.com",
  "title": "Contact Anthropic’s Education team",
  "snippet": "",
  "published": "2026-10-04T04:46:41+00:00"
 },
 {
  "id": "9367be2df22f",
  "region": "intl",
  "source": "claude.com",
  "title": "Life sciences",
  "snippet": "",
  "published": "2026-10-04T09:11:18+00:00"
 },
 {
  "id": "03fb137849be",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Cybersecurity",
  "snippet": "",
  "published": "2026-10-04T08:04:11+00:00"
 },
 {
  "id": "26bfc8cb2f94",
  "region": "intl",
  "source": "claude.com",
  "title": "Natoma connector",
  "snippet": "",
  "published": "2026-10-04T01:01:55+00:00"
 },
 {
  "id": "d290c4eacdc4",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Marketplace: plugins and connectors, products and agents, and service partners",
  "snippet": "",
  "published": "2026-10-03T18:28:25+00:00"
 },
 {
  "id": "56624d8e9fa2",
  "region": "intl",
  "source": "claude.com",
  "title": "Bring in certified experts to roll Claude out across your entire organization.",
  "snippet": "",
  "published": "2026-10-04T16:04:19+00:00"
 },
 {
  "id": "6f4544e1e7e7",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Claude Academy",
  "snippet": "",
  "published": "2026-10-04T06:25:58+00:00"
 },
 {
  "id": "28b596a790be",
  "region": "intl",
  "source": "claude.com",
  "title": "- claude.com",
  "snippet": "claude.com",
  "published": "2026-10-04T02:37:07+00:00"
 }
]
