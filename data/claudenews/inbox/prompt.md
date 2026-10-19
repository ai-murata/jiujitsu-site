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
  "id": "997fe6f53879",
  "region": "jp",
  "source": "日経クロステック",
  "title": "2位は「Claude Codeを使い3時間で開発、熊本地震で累計60万人が利用の掲示板サイト」20代以下の注目トップ10",
  "snippet": "",
  "published": "2026-10-18T20:00:00+00:00"
 },
 {
  "id": "168133879305",
  "region": "jp",
  "source": "shiritomo",
  "title": "「全部パクって大丈夫です」――Claude Codeの自動化リストが1500いいね集めた中身",
  "snippet": "",
  "published": "2026-10-18T22:34:42+00:00"
 },
 {
  "id": "a277d45a6608",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic、社内でAIエージェントの稼働時間が人間の6倍に 技術系初級職の採用比率は27％→9％に激減",
  "snippet": "",
  "published": "2026-10-18T23:02:13+00:00"
 },
 {
  "id": "ebdff9965887",
  "region": "jp",
  "source": "リアルサウンド",
  "title": "Anthropic、技術職の新規採用に占める若手が27％から9％に AI導入後の社内変化を報告",
  "snippet": "",
  "published": "2026-10-18T22:00:37+00:00"
 },
 {
  "id": "26cf32a8f149",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "AnthropicのClaude、量子回路の最良設計を更新──暗号解読に関わる計算も改善（NADA NEWS）",
  "snippet": "",
  "published": "2026-10-18T23:06:21+00:00"
 },
 {
  "id": "2fc22ba314bc",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "技術職採用の若手比率が27%から9%に、Anthropicの「AI稼働6倍」を読む",
  "snippet": "",
  "published": "2026-10-18T20:11:05+00:00"
 },
 {
  "id": "c276366e6a52",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "Anthropicが株式の5%を新たな公益ファンドに拠出 執筆",
  "snippet": "",
  "published": "2026-10-18T18:28:00+00:00"
 },
 {
  "id": "ce3a0d27a9f9",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、新設の公益基金に自社株の5％を拠出",
  "snippet": "",
  "published": "2026-10-18T18:27:58+00:00"
 },
 {
  "id": "bc88c8a3c696",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "Anthropic社は、AIトレーニングマニュアルの著作権侵害で15億ドルの損害賠償を求めて訴えられている。",
  "snippet": "",
  "published": "2026-10-18T17:29:20+00:00"
 },
 {
  "id": "aae6d449327b",
  "region": "jp",
  "source": "TradingView",
  "title": "Anthropic、新設の公益基金に5%の株式を拠出へ",
  "snippet": "",
  "published": "2026-10-18T19:12:23+00:00"
 },
 {
  "id": "79553d20ee35",
  "region": "jp",
  "source": "Mezha.net",
  "title": "Anthropic、株式の5%を「公益基金」に拠出へ",
  "snippet": "",
  "published": "2026-10-18T15:11:00+00:00"
 },
 {
  "id": "c0038678a89f",
  "region": "jp",
  "source": "Ledge.ai",
  "title": "Linux生みの親、Claude Codeでカーネル改善 特定の読み取りテストで約3倍の性能",
  "snippet": "",
  "published": "2026-10-18T03:03:36+00:00"
 },
 {
  "id": "2d2fdbd71ebc",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "【十字路】新たな起業機会がClaude CodeとCodexの周辺で生まれつつある｜Tregとの対談【動画ポッドキャスト】｜Koji杨远骋",
  "snippet": "",
  "published": "2026-10-18T16:08:24+00:00"
 },
 {
  "id": "ce88f0e5fd40",
  "region": "jp",
  "source": "Alpha Match Technology",
  "title": "Anthropicが中国AI企業をデータ窃取で非難：その深層を探る",
  "snippet": "",
  "published": "2026-10-18T04:26:40+00:00"
 },
 {
  "id": "ff7288cc6b44",
  "region": "jp",
  "source": "Martin Cid Magazine",
  "title": "Anthropic、若手技術職の採用比率が27%から9%に低下",
  "snippet": "",
  "published": "2026-10-18T14:11:10+00:00"
 },
 {
  "id": "9e5d79302e02",
  "region": "jp",
  "source": "財経新聞",
  "title": "Anthropic、METRの研究者6人に従業員相当のアクセス 承認不要で評価結果を公表",
  "snippet": "",
  "published": "2026-10-18T06:32:00+00:00"
 },
 {
  "id": "a0b05b3aeefb",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "Anthropic社は、AIトレーニング関連書籍の著作権料として15億ドルを支払った。",
  "snippet": "",
  "published": "2026-10-18T19:51:41+00:00"
 },
 {
  "id": "28ff2a15c8d0",
  "region": "jp",
  "source": "YouTube",
  "title": "Claude Codeのプロンプト完全入門 ― 良い指示の8要素・AIインタビュー・コンテキスト管理・公式ベストプラクティスをやさしく解説",
  "snippet": "",
  "published": "2026-10-18T08:45:16+00:00"
 },
 {
  "id": "cbd67f626119",
  "region": "jp",
  "source": "note",
  "title": "Anthropic社員が描く2030年――AI開発で人間に残る仕事は5％？｜Trans-N",
  "snippet": "",
  "published": "2026-10-18T03:43:54+00:00"
 },
 {
  "id": "7358785cb118",
  "region": "jp",
  "source": "YouTube",
  "title": "Claude Codeにゲームを作らせたら、頼み方だけでここまで変わった｜1行 vs プロンプト",
  "snippet": "",
  "published": "2026-10-18T13:22:36+00:00"
 },
 {
  "id": "e391257ed3c2",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "Anthropic社は、AIによるサイバーセキュリティリスクについて警告を発している。",
  "snippet": "",
  "published": "2026-10-18T03:24:35+00:00"
 },
 {
  "id": "78ca04b1322d",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "OpenCodeへの攻撃、OpenAI・Anthropic・GoogleのAPIキーが危険に",
  "snippet": "",
  "published": "2026-10-18T08:26:30+00:00"
 },
 {
  "id": "4cff3509c141",
  "region": "jp",
  "source": "VOI.ID",
  "title": "人道的ジュニア採用率が低下、従業員会議時間が20%増加",
  "snippet": "",
  "published": "2026-10-18T17:26:55+00:00"
 },
 {
  "id": "5383d29b0089",
  "region": "jp",
  "source": "教育家庭新聞",
  "title": "デジタルハリウッド大学、国内大学初のAnthropic「Claude」全学導入へ",
  "snippet": "",
  "published": "2026-10-18T01:01:51+00:00"
 },
 {
  "id": "dc0796de7c5d",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、米議会に「AI安全法案」を提案…政府制裁の中での自救策",
  "snippet": "",
  "published": "2026-10-18T02:35:00+00:00"
 },
 {
  "id": "d24b6906593a",
  "region": "intl",
  "source": "Anthropic",
  "title": "Investing in the public benefit",
  "snippet": "",
  "published": "2026-10-18T16:49:35+00:00"
 },
 {
  "id": "12c42c1c875e",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic to commit 5% stake to new public benefit fund",
  "snippet": "",
  "published": "2026-10-18T19:11:37+00:00"
 },
 {
  "id": "382f73c16b19",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic commits 5% of shares to new public benefit fund that could address AI job disruption",
  "snippet": "",
  "published": "2026-10-18T22:55:48+00:00"
 },
 {
  "id": "7f0f9d52b1b5",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic Plans to Shift Some Shares Into New ‘Public Good’ Fund",
  "snippet": "",
  "published": "2026-10-18T19:56:36+00:00"
 },
 {
  "id": "10906829a5e7",
  "region": "intl",
  "source": "WSJ",
  "title": "Anthropic to Commit 5% of Its Shares to New ‘Public Benefit’ Fund",
  "snippet": "",
  "published": "2026-10-18T23:23:00+00:00"
 },
 {
  "id": "5b7c72137e5e",
  "region": "intl",
  "source": "The Guardian",
  "title": "What are self-replicating ‘AI worms’, and why is Anthropic worried about them?",
  "snippet": "",
  "published": "2026-10-18T13:30:00+00:00"
 },
 {
  "id": "a673ee4aacad",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Anthropic says it’s committing 5% of its shares to a ‘public benefit fund’",
  "snippet": "",
  "published": "2026-10-18T20:37:40+00:00"
 },
 {
  "id": "3675f3773946",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic to Shift Some Shares Into New ‘Public Good’ Fund",
  "snippet": "",
  "published": "2026-10-18T19:56:36+00:00"
 },
 {
  "id": "8442731f0698",
  "region": "intl",
  "source": "XDA",
  "title": "I made Claude Code build a map of my files, and it cut search times by 96%",
  "snippet": "",
  "published": "2026-10-18T20:00:19+00:00"
 },
 {
  "id": "dff523936db0",
  "region": "intl",
  "source": "KTVN",
  "title": "Anthropic commits 5% of its stock to a new 'public benefit' fund | National News | 2news.com",
  "snippet": "",
  "published": "2026-10-18T23:29:41+00:00"
 },
 {
  "id": "b586f790a3ff",
  "region": "intl",
  "source": "Business Insider",
  "title": "Anthropic Commits Billions to a 'Public Benefit Fund'",
  "snippet": "",
  "published": "2026-10-18T18:46:00+00:00"
 },
 {
  "id": "d93ec92399a9",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Anthropic Co-Founder Predicts AI Will Bring US GDP to $44 Trillion",
  "snippet": "",
  "published": "2026-10-18T22:28:28+00:00"
 },
 {
  "id": "764ec59d5ad9",
  "region": "intl",
  "source": "shattered.io",
  "title": "Anthropic's $1B AI Safety Bill Threshold [2026]",
  "snippet": "",
  "published": "2026-10-18T23:10:26+00:00"
 },
 {
  "id": "c487848238d5",
  "region": "intl",
  "source": "CT Insider",
  "title": "Anthropic commits 5% of its stock to a new 'public benefit' fund",
  "snippet": "",
  "published": "2026-10-18T23:41:41+00:00"
 },
 {
  "id": "8f74ac9c36e4",
  "region": "intl",
  "source": "Seeking Alpha",
  "title": "Anthropic plans to set aside 5% of shares for public benefit fund before IPO (ANTHRO:Private)",
  "snippet": "",
  "published": "2026-10-18T18:49:41+00:00"
 },
 {
  "id": "1dc329108f90",
  "region": "intl",
  "source": "EdTech Innovation Hub",
  "title": "Anthropic rebuilds its coding infrastructure as daily changes pass 30,000",
  "snippet": "",
  "published": "2026-10-18T23:06:29+00:00"
 },
 {
  "id": "691611551e73",
  "region": "intl",
  "source": "Investing.com",
  "title": "Anthropic commits 5% of shares to new public benefit fund",
  "snippet": "",
  "published": "2026-10-18T18:37:02+00:00"
 },
 {
  "id": "857ca3e039ee",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Meta Says Claude AI Tool Triggered No Kings Instagram Suspension",
  "snippet": "",
  "published": "2026-10-18T23:59:54+00:00"
 },
 {
  "id": "62f9a107c216",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic Pledges $48 Billion in Stock Before Its IPO: What Does It Mean for Buyers?",
  "snippet": "",
  "published": "2026-10-18T19:01:32+00:00"
 },
 {
  "id": "e4bfb74a5752",
  "region": "intl",
  "source": "NBC News",
  "title": "Anthropic wants outside input on Claude’s values. But who gets the final say?",
  "snippet": "",
  "published": "2026-10-18T09:30:40+00:00"
 },
 {
  "id": "d32880d000db",
  "region": "intl",
  "source": "Crowdfund Insider",
  "title": "Anthropic Proposes Congress Bill Mirroring Claude’s Internal Safety Policies",
  "snippet": "",
  "published": "2026-10-18T20:15:31+00:00"
 },
 {
  "id": "3cb586621dcf",
  "region": "intl",
  "source": "The Tech Buzz",
  "title": "Anthropic Commits 5% Equity Stake to Public Benefit Fund",
  "snippet": "",
  "published": "2026-10-18T21:06:00+00:00"
 },
 {
  "id": "7a9e7d6ae5fe",
  "region": "intl",
  "source": "Punchbowl News",
  "title": "Anthropic, the safety movement and the left",
  "snippet": "",
  "published": "2026-10-18T22:11:49+00:00"
 },
 {
  "id": "37b71ce1e051",
  "region": "intl",
  "source": "Anadolu Ajansı",
  "title": "Anthropic pledges 5% of shares to new public benefit fund",
  "snippet": "",
  "published": "2026-10-18T20:11:11+00:00"
 },
 {
  "id": "7c03295c9619",
  "region": "intl",
  "source": "https://tech-insider.org/",
  "title": "Anthropic Commits 5% Stake to New Public Benefit Fund [2026]",
  "snippet": "",
  "published": "2026-10-18T19:36:03+00:00"
 },
 {
  "id": "67bdeaba7446",
  "region": "intl",
  "source": "claude.com",
  "title": "Projects redesigned: from folder to conversation",
  "snippet": "",
  "published": "2026-10-17T13:25:02+00:00"
 },
 {
  "id": "f7185bfbbaac",
  "region": "intl",
  "source": "claude.com",
  "title": "Best practices and tips",
  "snippet": "",
  "published": "2026-10-17T21:29:32+00:00"
 },
 {
  "id": "6832b3fed11c",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for the legal industry",
  "snippet": "",
  "published": "2026-10-18T01:07:30+00:00"
 },
 {
  "id": "ecac9532856e",
  "region": "intl",
  "source": "claude.com",
  "title": "Connectors and plugins - Claude",
  "snippet": "",
  "published": "2026-10-17T13:37:57+00:00"
 },
 {
  "id": "f1ee16162861",
  "region": "intl",
  "source": "claude.com",
  "title": "Building commerce agents with Claude",
  "snippet": "",
  "published": "2026-10-18T11:46:49+00:00"
 },
 {
  "id": "09f5b4403ffe",
  "region": "intl",
  "source": "claude.com",
  "title": "Epic Systems Claude Code case study",
  "snippet": "",
  "published": "2026-10-18T01:13:02+00:00"
 },
 {
  "id": "00c95f6a3b8c",
  "region": "intl",
  "source": "claude.com",
  "title": "Miro Claude Cowork case study",
  "snippet": "",
  "published": "2026-10-17T17:05:43+00:00"
 },
 {
  "id": "7316043ba18c",
  "region": "intl",
  "source": "claude.com",
  "title": "Inference hooks: inline data loss prevention for Claude Enterprise",
  "snippet": "",
  "published": "2026-10-17T23:46:47+00:00"
 },
 {
  "id": "221c41929568",
  "region": "intl",
  "source": "claude.com",
  "title": "Popular use cases",
  "snippet": "",
  "published": "2026-10-17T21:24:56+00:00"
 },
 {
  "id": "1f0674d80c1c",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude support for Apple's Foundation Models framework",
  "snippet": "",
  "published": "2026-10-17T12:59:11+00:00"
 },
 {
  "id": "3912165c419f",
  "region": "intl",
  "source": "claude.com",
  "title": "How to ship and scale agents with Claude Managed Agents",
  "snippet": "",
  "published": "2026-10-17T18:16:53+00:00"
 },
 {
  "id": "0fecfb0ac576",
  "region": "intl",
  "source": "claude.com",
  "title": "Running auto mode in production",
  "snippet": "",
  "published": "2026-10-17T18:03:34+00:00"
 },
 {
  "id": "8a1a8b60bd8a",
  "region": "intl",
  "source": "claude.com",
  "title": "Building agents that reach production systems with MCP",
  "snippet": "",
  "published": "2026-10-17T21:28:20+00:00"
 },
 {
  "id": "70617be2c9a8",
  "region": "intl",
  "source": "claude.com",
  "title": "Scaling AI Across the Portfolio: Anthropic and AWS for Private Equity",
  "snippet": "",
  "published": "2026-10-18T00:29:05+00:00"
 },
 {
  "id": "333cc188e1b3",
  "region": "intl",
  "source": "claude.com",
  "title": "Inside Claude for Financial Advisors",
  "snippet": "",
  "published": "2026-10-17T20:16:05+00:00"
 },
 {
  "id": "d4dc99d45f74",
  "region": "intl",
  "source": "claude.com",
  "title": "Making Claude Cowork ready for enterprise",
  "snippet": "",
  "published": "2026-10-18T13:40:57+00:00"
 },
 {
  "id": "816d6a1642f8",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Claude Haiku 5.5 系統提示",
  "snippet": "",
  "published": "2026-10-17T22:01:56+00:00"
 },
 {
  "id": "9859a15ec899",
  "region": "intl",
  "source": "claude.com",
  "title": "Building an AI-native revenue organization",
  "snippet": "",
  "published": "2026-10-18T11:52:12+00:00"
 },
 {
  "id": "6f1f44e54df8",
  "region": "intl",
  "source": "claude.com",
  "title": "Chainguard",
  "snippet": "",
  "published": "2026-10-17T13:11:31+00:00"
 },
 {
  "id": "8e1308747c3c",
  "region": "intl",
  "source": "claude.com",
  "title": "Close connector",
  "snippet": "",
  "published": "2026-10-18T05:02:17+00:00"
 },
 {
  "id": "b76a8ab70ecd",
  "region": "intl",
  "source": "claude.com",
  "title": "Mastering Async Agents: Production Insights from Cognition Labs",
  "snippet": "",
  "published": "2026-10-17T15:14:12+00:00"
 },
 {
  "id": "01c584638aec",
  "region": "intl",
  "source": "claude.com",
  "title": "From 0 to 1: How Zingage Built AI-Powered Home Care on Claude",
  "snippet": "",
  "published": "2026-10-17T18:16:54+00:00"
 },
 {
  "id": "8d2665606e21",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude, der KI-Assistent, der Ihre Arbeit macht",
  "snippet": "",
  "published": "2026-10-17T14:54:02+00:00"
 },
 {
  "id": "3e3f6bade86a",
  "region": "intl",
  "source": "claude.com",
  "title": "The startup lifecycle, rebooted for 2026",
  "snippet": "",
  "published": "2026-10-18T12:23:04+00:00"
 },
 {
  "id": "92095d0757c5",
  "region": "intl",
  "source": "claude.com",
  "title": "Vital Care Finder connector",
  "snippet": "",
  "published": "2026-10-18T19:02:36+00:00"
 },
 {
  "id": "13d5315f5175",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.303",
  "snippet": "What's changed Bug fixes and reliability improvements",
  "published": "2026-10-18T22:26:54+00:00"
 }
]
