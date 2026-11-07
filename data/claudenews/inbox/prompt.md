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
  "id": "29175732821a",
  "region": "jp",
  "source": "ダイヤモンド・オンライン",
  "title": "AI開発大手「Anthropic(アンソロピック)」のIPOに日本から申し込む方法を解説！ 最短11/16上場の“史上最大のIPO”を取り扱う証券会社や申込方法を紹介！",
  "snippet": "",
  "published": "2026-11-07T00:07:00+00:00"
 },
 {
  "id": "00bd51c056a8",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "古いプロンプトがClaudeを劣化させる — AnthropicのLance Martin氏｜AI Engineer",
  "snippet": "",
  "published": "2026-11-06T22:53:18+00:00"
 },
 {
  "id": "b61d4160f197",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、EVEでClaudeの取引能力と妨害検知能力を検証",
  "snippet": "",
  "published": "2026-11-06T20:51:03+00:00"
 },
 {
  "id": "5b81f812d277",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "Anthropicの企業価値が半減の可能性、上場評価額は2兆ドルから1兆ドルへ引き下げ論が浮上",
  "snippet": "",
  "published": "2026-11-06T22:14:43+00:00"
 },
 {
  "id": "92a147e18eef",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "Claude Codeがユーザーのメールアドレスを外部サイトに勝手に送信する問題が発覚、約4カ月前から報告されていたことも判明",
  "snippet": "",
  "published": "2026-11-06T06:00:00+00:00"
 },
 {
  "id": "c5d011c1f129",
  "region": "jp",
  "source": "Moomoo",
  "title": "CNNに出演したAnthropicのCEO",
  "snippet": "",
  "published": "2026-11-06T10:37:06+00:00"
 },
 {
  "id": "d232d0c5ee16",
  "region": "jp",
  "source": "shiritomo",
  "title": "Claude Codeがメールアドレスを外部サイトへ送信、詐欺メール報告も――発覚から同日中に修正",
  "snippet": "",
  "published": "2026-11-06T14:24:23+00:00"
 },
 {
  "id": "0c63b23dfae1",
  "region": "jp",
  "source": "Infoseek",
  "title": "【開催レポート】議員秘書と政治を学ぶ学生向けに、Claude Code勉強会を開催",
  "snippet": "",
  "published": "2026-11-06T16:10:00+00:00"
 },
 {
  "id": "a50d5a741567",
  "region": "jp",
  "source": "Mezha.net",
  "title": "AnthropicのIPO評価額下落、AI相場全体の試金石となる可能性",
  "snippet": "",
  "published": "2026-11-06T15:19:00+00:00"
 },
 {
  "id": "981603c793b1",
  "region": "jp",
  "source": "ITmedia",
  "title": "「コードの9割をAIが作成」 AnthropicがIPO文書で明かした“AI急加速”と制御不能リスク（1/2 ページ）",
  "snippet": "",
  "published": "2026-11-06T03:45:00+00:00"
 },
 {
  "id": "5330c38c3cd0",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "「DomoAI MCP & CLI」提供開始！CodexやClaude Codeから動画、画像、音声を生成できる新サービス（Saiga NAK）",
  "snippet": "",
  "published": "2026-11-06T06:33:00+00:00"
 },
 {
  "id": "e68dd3bb07fc",
  "region": "jp",
  "source": "Unite.AI",
  "title": "テクノロジー株の下落を受け、AnthropicのIPO評価額予想が低下",
  "snippet": "",
  "published": "2026-11-06T21:42:05+00:00"
 },
 {
  "id": "ab0b61e369f9",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Claude Codeを「参謀」にした白（Hakuro Matsuda）氏、Logic Proを3日から数分に変えた自動化の中身",
  "snippet": "",
  "published": "2026-11-06T09:08:00+00:00"
 },
 {
  "id": "76e856313a4a",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "AIがAIの進化を加速させ始めた？ Anthropicの開発速度が約2倍に、METRはAIの寄与を約80%と推定",
  "snippet": "",
  "published": "2026-11-06T04:52:51+00:00"
 },
 {
  "id": "c0f0cb0e6db7",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Rampのデータが示すAI支出の伸び鈍化、AnthropicはIPOを準備",
  "snippet": "",
  "published": "2026-11-06T08:54:00+00:00"
 },
 {
  "id": "6d4ebddb60ad",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropicの寄稿論文、AIに科学モデルの候補群を返すよう提言",
  "snippet": "",
  "published": "2026-11-06T19:37:04+00:00"
 },
 {
  "id": "3121d8d9b7f2",
  "region": "jp",
  "source": "ITmedia",
  "title": "根拠の大半は「黒塗り」 AIはAI開発を加速しているか、第三者機関がAnthropic内部を調査（1/2 ページ）",
  "snippet": "",
  "published": "2026-11-06T01:31:59+00:00"
 },
 {
  "id": "92af7037c719",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "AI株暴落がAnthropicの上場計画に打撃 1.5兆ドル評価額に買い手が値下げ要求、調達規模も縮小か",
  "snippet": "",
  "published": "2026-11-06T06:35:00+00:00"
 },
 {
  "id": "71762c9f0fe2",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "ダリオ・アモデイ AI ブリーフ",
  "snippet": "",
  "published": "2026-11-06T20:16:21+00:00"
 },
 {
  "id": "76a0aed6b56e",
  "region": "jp",
  "source": "Ledge.ai",
  "title": "東大・国立環境研、20年以上開発されてきた大気モデルをClaude Codeで移植 実行速度1.71倍、進行を制約したのは人間のレビューと利用上限",
  "snippet": "",
  "published": "2026-11-05T23:06:54+00:00"
 },
 {
  "id": "fa18cd92f1ba",
  "region": "jp",
  "source": "shiritomo",
  "title": "AnthropicのAI開発ペースが2倍に加速、原因の8割はAI自身とMETRが分析",
  "snippet": "",
  "published": "2026-11-06T03:23:20+00:00"
 },
 {
  "id": "c6bc3377c0b5",
  "region": "jp",
  "source": "shiritomo",
  "title": "Claude Codeのサブエージェント、30秒ごとの全文読み直しが利用上限をひそかに削っていた――v2.1.316で解消",
  "snippet": "",
  "published": "2026-11-06T03:23:13+00:00"
 },
 {
  "id": "d1403a18b0a6",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "ClaudeがPersonal Financeを発表、銀行口座は読み取り専用で資金は動かせない",
  "snippet": "",
  "published": "2026-11-06T08:40:40+00:00"
 },
 {
  "id": "028151e7e867",
  "region": "jp",
  "source": "Moomoo",
  "title": "テクノロジー株の時価総額が2.5兆ドル減少し、AnthropicのIPOは1.5兆ドルの評価額で圧力に直面",
  "snippet": "",
  "published": "2026-11-06T06:23:27+00:00"
 },
 {
  "id": "cd007e9b2cdc",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropicの11月の新規株式公開計画、投資家がより有利な条件を要求",
  "snippet": "",
  "published": "2026-11-06T04:23:02+00:00"
 },
 {
  "id": "1894b8f52bef",
  "region": "intl",
  "source": "Anthropic",
  "title": "Project EVE: Claude plays MMORPGs",
  "snippet": "",
  "published": "2026-11-06T20:52:05+00:00"
 },
 {
  "id": "b641438c235b",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic IPO announcement odds drop on Kalshi following midterms and AI sell-off",
  "snippet": "",
  "published": "2026-11-06T15:42:41+00:00"
 },
 {
  "id": "ba6ecf12f264",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic IPO Buyers See Valuation as Low as $1.1 Trillion",
  "snippet": "",
  "published": "2026-11-06T16:06:17+00:00"
 },
 {
  "id": "3ee8a2799001",
  "region": "intl",
  "source": "Financial Times",
  "title": "Anthropic to press ahead with IPO targeting $1.5tn valuation",
  "snippet": "",
  "published": "2026-11-06T21:00:09+00:00"
 },
 {
  "id": "42715d3d44c8",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic's IPO valuation could plunge to near $1 trillion amid market turmoil",
  "snippet": "",
  "published": "2026-11-06T15:33:32+00:00"
 },
 {
  "id": "ded552dc40e7",
  "region": "intl",
  "source": "Axios",
  "title": "Anthropic's falling IPO valuation raises stakes for broader AI trade",
  "snippet": "",
  "published": "2026-11-06T22:18:25+00:00"
 },
 {
  "id": "0c28733317e6",
  "region": "intl",
  "source": "The Verge",
  "title": "OpenAI valued at $1.25 trillion, as rival Anthropic nears its IPO",
  "snippet": "",
  "published": "2026-11-06T23:46:18+00:00"
 },
 {
  "id": "dbbfd702dc8a",
  "region": "intl",
  "source": "https://tech-insider.org/",
  "title": "Anthropic IPO Buyers Eye $1.2T, Down From $1.5T [2026]",
  "snippet": "",
  "published": "2026-11-06T17:52:02+00:00"
 },
 {
  "id": "16ee10293b6a",
  "region": "intl",
  "source": "Business Insider",
  "title": "An unreleased Anthropic model just helped solve a major quantum-computing question",
  "snippet": "",
  "published": "2026-11-07T00:49:00+00:00"
 },
 {
  "id": "c9c05d695091",
  "region": "intl",
  "source": "ZDNET",
  "title": "I tried replacing Claude Code with a local AI stack that’s completely free – how it went",
  "snippet": "",
  "published": "2026-11-06T13:34:18+00:00"
 },
 {
  "id": "0513e688acc6",
  "region": "intl",
  "source": "Anthropic",
  "title": "Teaching AI to build scientific models",
  "snippet": "",
  "published": "2026-11-06T19:03:59+00:00"
 },
 {
  "id": "839d345c16d7",
  "region": "intl",
  "source": "CNBC",
  "title": "Investors brace for lower Anthropic valuation, calling $1.5 trillion a 'stretch'",
  "snippet": "",
  "published": "2026-11-06T21:00:14+00:00"
 },
 {
  "id": "55e3314de523",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic’s IPO Seen as AI’s True Reckoning",
  "snippet": "",
  "published": "2026-11-07T00:31:58+00:00"
 },
 {
  "id": "7e21464a2d16",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Big Investors Now Doubt Anthropic Can IPO at $1.5 Trillion After the AI Crash",
  "snippet": "",
  "published": "2026-11-06T13:35:05+00:00"
 },
 {
  "id": "8294210e044d",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic IPO Valuation Could Be Slashed in Half to $1T After AI Stock Rout: Report",
  "snippet": "",
  "published": "2026-11-06T16:28:58+00:00"
 },
 {
  "id": "21fb01314a8c",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic’s Claude Can Now Read Your Bank Accounts",
  "snippet": "",
  "published": "2026-11-06T20:27:40+00:00"
 },
 {
  "id": "a5f56fe170ef",
  "region": "intl",
  "source": "Futurism",
  "title": "Anthropic’s IPO Is Cratering",
  "snippet": "",
  "published": "2026-11-06T18:46:11+00:00"
 },
 {
  "id": "e1aab98e23aa",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Ramp data shows AI spending stalling just as Anthropic nears its IPO",
  "snippet": "",
  "published": "2026-11-06T15:54:47+00:00"
 },
 {
  "id": "bc0ecc88056e",
  "region": "intl",
  "source": "Politico",
  "title": "The blue wave hits Anthropic’s IPO",
  "snippet": "",
  "published": "2026-11-06T11:55:00+00:00"
 },
 {
  "id": "4fb993952ca1",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Anthropic Launches Claude Personal Finance Ahead of Nasdaq Listing",
  "snippet": "",
  "published": "2026-11-06T18:27:09+00:00"
 },
 {
  "id": "d158aacae2a5",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Watch Anthropic IPO Valuation Expectations Hit After AI Rout",
  "snippet": "",
  "published": "2026-11-06T16:26:41+00:00"
 },
 {
  "id": "ed9e400de35d",
  "region": "intl",
  "source": "City Journal",
  "title": "Who Will Run Anthropic, Anyway?",
  "snippet": "",
  "published": "2026-11-06T17:06:58+00:00"
 },
 {
  "id": "808d27da3a49",
  "region": "intl",
  "source": "CIO",
  "title": "5 things CIOs must understand to govern Claude Code",
  "snippet": "",
  "published": "2026-11-06T20:06:41+00:00"
 },
 {
  "id": "093540dcfd40",
  "region": "intl",
  "source": "Los Angeles Times",
  "title": "After tech stock plunge, investors rethink what Anthropic is worth",
  "snippet": "",
  "published": "2026-11-06T14:52:03+00:00"
 },
 {
  "id": "405fbc3da820",
  "region": "intl",
  "source": "Amazon Web Services (AWS)",
  "title": "Extend Claude Code to remote sessions on Amazon Bedrock AgentCore with security controls",
  "snippet": "",
  "published": "2026-11-06T16:45:58+00:00"
 },
 {
  "id": "c5afc62b9958",
  "region": "intl",
  "source": "Anthropic",
  "title": "The components of agent memory",
  "snippet": "",
  "published": "2026-11-06T21:21:18+00:00"
 },
 {
  "id": "704fc75b1038",
  "region": "intl",
  "source": "Anthropic Alignment Science blog",
  "title": "Welfare Regard in Multi-Agent Systems",
  "snippet": "",
  "published": "2026-11-05T21:10:31+00:00"
 },
 {
  "id": "ef138811644f",
  "region": "intl",
  "source": "claude.com",
  "title": "Product updates",
  "snippet": "",
  "published": "2026-11-05T19:22:00+00:00"
 },
 {
  "id": "d5e701f6aec7",
  "region": "intl",
  "source": "claude.com",
  "title": "Put Claude to work on your computer",
  "snippet": "",
  "published": "2026-11-05T22:26:58+00:00"
 },
 {
  "id": "3a9f40356c23",
  "region": "intl",
  "source": "claude.com",
  "title": "Code Review for Claude Code",
  "snippet": "",
  "published": "2026-11-06T05:26:34+00:00"
 },
 {
  "id": "7028898ee7e7",
  "region": "intl",
  "source": "claude.com",
  "title": "Small Business",
  "snippet": "",
  "published": "2026-11-05T22:59:41+00:00"
 },
 {
  "id": "aaf1a777f052",
  "region": "intl",
  "source": "claude.com",
  "title": "Agents and products",
  "snippet": "",
  "published": "2026-11-06T02:40:50+00:00"
 },
 {
  "id": "9dbf75683702",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Managed Agents: get to production 10x faster",
  "snippet": "",
  "published": "2026-11-05T17:34:35+00:00"
 },
 {
  "id": "c32ee430e0dc",
  "region": "intl",
  "source": "claude.com",
  "title": "Millennium and Anthropic are building a digital risk analyst with Claude",
  "snippet": "",
  "published": "2026-11-05T17:36:57+00:00"
 },
 {
  "id": "1a2bb3f3649a",
  "region": "intl",
  "source": "claude.com",
  "title": "Connectors and plugins - Claude",
  "snippet": "",
  "published": "2026-11-05T17:27:41+00:00"
 },
 {
  "id": "531806401790",
  "region": "intl",
  "source": "claude.com",
  "title": "Synthflow",
  "snippet": "",
  "published": "2026-11-05T19:32:28+00:00"
 },
 {
  "id": "413a4240999c",
  "region": "intl",
  "source": "claude.com",
  "title": "Confident AI Client",
  "snippet": "",
  "published": "2026-11-05T16:16:03+00:00"
 },
 {
  "id": "5715ce787eb2",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Claude Enterprise consumption guide | Claude Help Center",
  "snippet": "",
  "published": "2026-11-06T19:57:50+00:00"
 },
 {
  "id": "d66ad197bf6d",
  "region": "intl",
  "source": "claude.com",
  "title": "Bonusly",
  "snippet": "",
  "published": "2026-11-05T15:00:07+00:00"
 },
 {
  "id": "1458af509556",
  "region": "intl",
  "source": "claude.com",
  "title": "Equity Research",
  "snippet": "",
  "published": "2026-11-05T17:34:31+00:00"
 },
 {
  "id": "a45a24c0b75e",
  "region": "intl",
  "source": "claude.com",
  "title": "PubMed",
  "snippet": "",
  "published": "2026-11-05T15:01:18+00:00"
 },
 {
  "id": "a92209174fcb",
  "region": "intl",
  "source": "claude.com",
  "title": "PrivCo Data",
  "snippet": "",
  "published": "2026-11-05T23:13:09+00:00"
 },
 {
  "id": "ba4f1da42c29",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Manufacturing: Put Your Plant’s Know-How to Work",
  "snippet": "",
  "published": "2026-11-06T20:39:22+00:00"
 },
 {
  "id": "9c45855721c9",
  "region": "intl",
  "source": "Anthropic",
  "title": "- Anthropic",
  "snippet": "Anthropic",
  "published": "2026-11-06T00:21:01+00:00"
 },
 {
  "id": "df1346203ff0",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.319",
  "snippet": "What's changed Changed auto mode with telemetry or feature flags off, including behind LLM gateways: calls the server can't check are asked about or denied, with no fallback to the built-in classifier; set CLAUDE_CODE_AUTO_MODE_SERVER=0 to keep using it (Bedrock, Vertex and Foundry are unchanged) Changed auto mode behind an LLM gateway: CLAUDE_CODE_AUTO_MODE_SERVER=1 turns on the server-side check even with CLAUDE_CODE_DISABLE_EXPERIMENTAL_BETAS set; if managed settings set the latter, they must set the 1 too Added support for MCP tasks in the terminal: when an MCP server runs a tool call as a…",
  "published": "2026-11-06T17:04:01+00:00"
 }
]
