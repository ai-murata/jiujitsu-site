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
  "id": "87255a4b09d4",
  "region": "jp",
  "source": "日経クロステック",
  "title": "700件超のAnthropic論文をClaudeで分析 ぶれぬ安全軸、競争優位と二兎追う",
  "snippet": "",
  "published": "2026-10-14T20:00:00+00:00"
 },
 {
  "id": "7927bb3c6046",
  "region": "jp",
  "source": "株式会社エクサウィザーズ",
  "title": "米Anthropic、家電に自己増殖するAIが数カ月以内に現れる恐れと警告",
  "snippet": "",
  "published": "2026-10-14T23:18:58+00:00"
 },
 {
  "id": "3f3928cfea31",
  "region": "jp",
  "source": "PC Watch",
  "title": "参加者全員にMax 5x Planと500ドル。Anthropic初の国内ハッカソン",
  "snippet": "",
  "published": "2026-10-14T05:45:31+00:00"
 },
 {
  "id": "be0ff144d699",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic共同創業者「サイバー攻撃、オープンモデル悪用の可能性」",
  "snippet": "",
  "published": "2026-10-14T09:20:35+00:00"
 },
 {
  "id": "bc1103fa6655",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、AIエージェントがGitを破壊したためGitを放棄——今やソフトウェアに安全な領域は存在しない",
  "snippet": "",
  "published": "2026-10-14T21:08:00+00:00"
 },
 {
  "id": "33deef7386dd",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、2026年米国中間選挙を前に選挙関連の安全対策を強化",
  "snippet": "",
  "published": "2026-10-14T20:01:30+00:00"
 },
 {
  "id": "447fecd05099",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "OpenAIとAnthropicは、AIテスト中に発生したサイバーセキュリティインシデントについて説明しなければならない。",
  "snippet": "",
  "published": "2026-10-14T14:41:13+00:00"
 },
 {
  "id": "cd176641ab85",
  "region": "jp",
  "source": "Ledge.ai",
  "title": "Anthropic、重要インフラとOSSを守る「Cyber Mission」発表 日立など11社が参加、無料の脆弱性スキャンも",
  "snippet": "",
  "published": "2026-10-14T08:00:12+00:00"
 },
 {
  "id": "03b289098212",
  "region": "jp",
  "source": "note",
  "title": "Anthropic、巨大モノレポをGitからScionへ移行――AI時代のソース管理を再設計｜Trans-N",
  "snippet": "",
  "published": "2026-10-14T15:37:02+00:00"
 },
 {
  "id": "c01fed522998",
  "region": "jp",
  "source": "Moomoo",
  "title": "小型モデルは本当に脅威なのか？",
  "snippet": "",
  "published": "2026-10-14T15:47:36+00:00"
 },
 {
  "id": "46b9250c0e4b",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "AnthropicがGit代替のバージョン管理システム「Scion」を開発し社内移行済み、AIでコードが爆増してGitの限界に達したので耐えられるシステムを開発",
  "snippet": "",
  "published": "2026-10-14T04:33:00+00:00"
 },
 {
  "id": "b4f63b7b0345",
  "region": "jp",
  "source": "EnterpriseZine",
  "title": "Anthropic日本法人1周年──本国CEOが直近のサイバー攻撃に言及、AI悪用防ぐルール作り必要",
  "snippet": "",
  "published": "2026-10-14T07:27:24+00:00"
 },
 {
  "id": "d6837c95dc05",
  "region": "jp",
  "source": "PR TIMES",
  "title": "デジタルハリウッド大学【DHU】、Anthropicの生成AIモデル「Claude」を国内大学初となる全学導入へ",
  "snippet": "",
  "published": "2026-10-14T03:00:02+00:00"
 },
 {
  "id": "c128c809eaab",
  "region": "jp",
  "source": "TradingView",
  "title": "ＢｏｆＡ、脆弱性修正に1000人採用 Anthropic関連――CNBC",
  "snippet": "",
  "published": "2026-10-14T18:53:15+00:00"
 },
 {
  "id": "1ede2b1207a9",
  "region": "jp",
  "source": "ITmedia",
  "title": "「AIがAIを作れるようになる確率は2027年に50%超」 Anthropic共同創業者が予測を前倒し、「ただし実行は“片道切符",
  "snippet": "",
  "published": "2026-10-14T07:53:35+00:00"
 },
 {
  "id": "3af50fc7d750",
  "region": "jp",
  "source": "Impress Watch",
  "title": "アンソロピック、日本は「最も成長が早い市場」 データセンター構築にも意欲",
  "snippet": "",
  "published": "2026-10-14T04:52:31+00:00"
 },
 {
  "id": "37a0273e0d0a",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "AIコードの奔流がGitを圧迫、Anthropicが自社開発のバージョン管理システム「Scion」で10倍増のマージ需要に対応",
  "snippet": "",
  "published": "2026-10-14T00:35:00+00:00"
 },
 {
  "id": "6e02776696d7",
  "region": "jp",
  "source": "TechTargetジャパン",
  "title": "OpenAIやAnthropicでさえ制御不能 2026年夏「3大サイバー攻撃」の衝撃：重要インフラが狙われる理由",
  "snippet": "",
  "published": "2026-10-14T20:00:00+00:00"
 },
 {
  "id": "f00548e9616c",
  "region": "jp",
  "source": "ASCII.jp",
  "title": "デジハリ大、Anthropic「Claude」を全学生に無料提供 国内大学で初の全学導入",
  "snippet": "",
  "published": "2026-10-14T05:00:00+00:00"
 },
 {
  "id": "b91bb78e5f51",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "OpenTelemetryがClaude APIのトレースにパブリックベータで対応",
  "snippet": "",
  "published": "2026-10-14T19:51:35+00:00"
 },
 {
  "id": "a0eb38278255",
  "region": "jp",
  "source": "Moomoo",
  "title": "Anthropicの第3四半期売上高、168億ドルに急増",
  "snippet": "",
  "published": "2026-10-14T07:00:00+00:00"
 },
 {
  "id": "4851c12537ca",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、シンガポール政府と覚書を締結 新オフィスを開設",
  "snippet": "",
  "published": "2026-10-14T09:05:29+00:00"
 },
 {
  "id": "85c969e8a4a5",
  "region": "jp",
  "source": "NOVAIST",
  "title": "Anthropic共同創業者、AI開発減速の可能性に言及 東京会見で安全対策と評価の重要性を強調",
  "snippet": "",
  "published": "2026-10-14T10:20:01+00:00"
 },
 {
  "id": "81097e058da4",
  "region": "jp",
  "source": "PR TIMES",
  "title": "Claude Codeが切り拓く次世代の暗号解読術！ 『生成AI時代の暗号技術入門 AIエージェントで挑む古典暗号の自動解析』発行 技術の泉シリーズ 10月の新刊",
  "snippet": "",
  "published": "2026-10-14T02:00:02+00:00"
 },
 {
  "id": "a9aa66f7a0f0",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "オープンモデルはOpenAIとAnthropicに追いつけるのか？ | ネイサン・ランバート｜a16z",
  "snippet": "",
  "published": "2026-10-14T15:45:07+00:00"
 },
 {
  "id": "491630de6f36",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic's Q3 revenue surges 45% to nearly $17 billion",
  "snippet": "",
  "published": "2026-10-14T23:02:55+00:00"
 },
 {
  "id": "a8fef9820020",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic Q3 revenue climbs to $16.8 billion: Report",
  "snippet": "",
  "published": "2026-10-14T22:16:19+00:00"
 },
 {
  "id": "00438aa05aa4",
  "region": "intl",
  "source": "Anthropic",
  "title": "Preparing for the 2026 US midterms",
  "snippet": "",
  "published": "2026-10-14T18:33:00+00:00"
 },
 {
  "id": "0275c030d98a",
  "region": "intl",
  "source": "Bloomberg.com",
  "title": "Anthropic Revenue Jumps to $16.8 Billion in Quarter Before IPO",
  "snippet": "",
  "published": "2026-10-14T22:22:48+00:00"
 },
 {
  "id": "80dcb2cd73e0",
  "region": "intl",
  "source": "CNBC",
  "title": "Bank of America hired 1,000 contractors to patch software flaws exposed by Anthropic's Mythos",
  "snippet": "",
  "published": "2026-10-14T18:47:38+00:00"
 },
 {
  "id": "288da68e243b",
  "region": "intl",
  "source": "Financial Times",
  "title": "Anthropic tells investors quarterly revenue up 50% to $16.8bn ahead of IPO",
  "snippet": "",
  "published": "2026-10-14T22:06:31+00:00"
 },
 {
  "id": "1431270f68fa",
  "region": "intl",
  "source": "The New York Times",
  "title": "Anthropic Says Revenue Jumped 45% to $16.8 Billion in Third Quarter",
  "snippet": "",
  "published": "2026-10-14T23:33:33+00:00"
 },
 {
  "id": "6778f992ed2a",
  "region": "intl",
  "source": "Scientific American",
  "title": "Claude just found a CRISPR-like DNA pattern, but even Anthropic's scientists aren't sure what it does",
  "snippet": "",
  "published": "2026-10-14T10:00:00+00:00"
 },
 {
  "id": "92b644590d55",
  "region": "intl",
  "source": "WSJ",
  "title": "Anthropic’s Quarterly Revenue Jumped 45% to Nearly $17 Billion",
  "snippet": "",
  "published": "2026-10-15T00:17:00+00:00"
 },
 {
  "id": "0b23e7213f50",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic to add US voting information to Claude before midterms",
  "snippet": "",
  "published": "2026-10-14T21:05:02+00:00"
 },
 {
  "id": "5d05128bbe80",
  "region": "intl",
  "source": "ABC7 Bay Area",
  "title": "Anthropic warns AI models could soon copy themselves in small devices",
  "snippet": "",
  "published": "2026-10-14T10:50:50+00:00"
 },
 {
  "id": "d0418d3a3435",
  "region": "intl",
  "source": "Ars Technica",
  "title": "Anthropic warns small AI models could self-replicate through IoT devices",
  "snippet": "",
  "published": "2026-10-14T12:55:06+00:00"
 },
 {
  "id": "d92907280a77",
  "region": "intl",
  "source": "Dark Reading",
  "title": "Anthropic 'SneakPeek' Flaw Is a Silent Zero-Click Threat",
  "snippet": "",
  "published": "2026-10-14T20:35:55+00:00"
 },
 {
  "id": "6af601f22020",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic to disclose new revenue numbers to investors today ahead of anticipated IPO: Sources",
  "snippet": "",
  "published": "2026-10-14T19:04:36+00:00"
 },
 {
  "id": "20c24d08cf38",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Inside Anthropic's private pre-IPO investor day",
  "snippet": "",
  "published": "2026-10-14T20:34:49+00:00"
 },
 {
  "id": "7e3ca0b6bd99",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic revenue jumps to $16.8 billion in third quarter, FT reports",
  "snippet": "",
  "published": "2026-10-14T22:14:49+00:00"
 },
 {
  "id": "218bd4dfd009",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Nvidia, Anthropic Weigh In On AI Safeguards",
  "snippet": "",
  "published": "2026-10-14T21:40:11+00:00"
 },
 {
  "id": "4b3d8387dcb3",
  "region": "intl",
  "source": "Business Insider",
  "title": "How Anthropic's IPO could dull Leopold Aschenbrenner's investing edge",
  "snippet": "",
  "published": "2026-10-14T09:58:00+00:00"
 },
 {
  "id": "006e112ef800",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic revenue jumps to $16.8bn in third quarter",
  "snippet": "",
  "published": "2026-10-14T22:06:31+00:00"
 },
 {
  "id": "e63775f687c8",
  "region": "intl",
  "source": "Malwarebytes",
  "title": "Police receive fake murder tip from Anthropic’s Claude AI",
  "snippet": "",
  "published": "2026-10-14T10:57:26+00:00"
 },
 {
  "id": "417d481d0807",
  "region": "intl",
  "source": "Computerworld",
  "title": "The EU is investigating OpenAI and Anthropic following incidents involving AI agents",
  "snippet": "",
  "published": "2026-10-14T19:55:31+00:00"
 },
 {
  "id": "5ed4936a316f",
  "region": "intl",
  "source": "Morningstar",
  "title": "Here’s How Anthropic and OpenAI Are Building Economic Moats",
  "snippet": "",
  "published": "2026-10-14T22:28:48+00:00"
 },
 {
  "id": "f316e6a7c6ca",
  "region": "intl",
  "source": "Business Insider Africa",
  "title": "Anthropic's quarterly revenue leaps to $16.8 billion as IPO looms",
  "snippet": "",
  "published": "2026-10-14T23:38:37+00:00"
 },
 {
  "id": "73c852745c3b",
  "region": "intl",
  "source": "Unite.AI",
  "title": "Anthropic Strengthens Election Safeguards Ahead of 2026 US Midterms",
  "snippet": "",
  "published": "2026-10-14T19:58:08+00:00"
 },
 {
  "id": "f5ed167dcf05",
  "region": "intl",
  "source": "Malwarebytes",
  "title": "AI worms could spread across your smart devices, Anthropic warns",
  "snippet": "",
  "published": "2026-10-14T16:58:11+00:00"
 },
 {
  "id": "9fb1ab05bf49",
  "region": "intl",
  "source": "Anthropic",
  "title": "Singapore office and government MOU",
  "snippet": "",
  "published": "2026-10-14T08:30:00+00:00"
 },
 {
  "id": "8caec9de1803",
  "region": "intl",
  "source": "claude.com",
  "title": "Trace agents with OpenTelemetry on the Claude Platform",
  "snippet": "",
  "published": "2026-10-14T17:34:09+00:00"
 },
 {
  "id": "f9c23efac1be",
  "region": "intl",
  "source": "Claude Platform",
  "title": "Use OpenTelemetry with the Claude SDK",
  "snippet": "",
  "published": "2026-10-14T17:18:31+00:00"
 },
 {
  "id": "ae91061c25d5",
  "region": "intl",
  "source": "Claude Platform",
  "title": "OpenTelemetry for the Claude API",
  "snippet": "",
  "published": "2026-10-14T17:18:36+00:00"
 },
 {
  "id": "e2b1b3a16fa3",
  "region": "intl",
  "source": "claude.com",
  "title": "Uber's CISO on building an insider threat program for AI",
  "snippet": "",
  "published": "2026-10-13T19:51:02+00:00"
 },
 {
  "id": "4c5d96e2536d",
  "region": "intl",
  "source": "claude.com",
  "title": "The AI for problem solvers",
  "snippet": "",
  "published": "2026-10-13T22:15:19+00:00"
 },
 {
  "id": "860c4382c157",
  "region": "intl",
  "source": "Anthropic",
  "title": "Rebroadcast: Claude on Google Cloud: Monitoring and securing agents at scale",
  "snippet": "",
  "published": "2026-10-13T18:30:48+00:00"
 },
 {
  "id": "26ba327eee44",
  "region": "intl",
  "source": "Anthropic",
  "title": "Leadership at Anthropic",
  "snippet": "",
  "published": "2026-10-13T22:02:54+00:00"
 },
 {
  "id": "b0660fb391f7",
  "region": "intl",
  "source": "Anthropic",
  "title": "How to control costs and show ROI for Claude Code on Google Cloud (EMEA rebroadcast)",
  "snippet": "",
  "published": "2026-10-14T09:32:36+00:00"
 },
 {
  "id": "3c33362b8589",
  "region": "intl",
  "source": "claude.com",
  "title": "Chainguard",
  "snippet": "",
  "published": "2026-10-14T12:25:55+00:00"
 },
 {
  "id": "8fc66f3f93ac",
  "region": "intl",
  "source": "claude.com",
  "title": "Bringing Claude Code and Claude Cowork to government",
  "snippet": "",
  "published": "2026-10-14T01:10:09+00:00"
 },
 {
  "id": "3d7e2823118a",
  "region": "intl",
  "source": "claude.com",
  "title": "Auto mode for Claude Code",
  "snippet": "",
  "published": "2026-10-13T22:35:04+00:00"
 },
 {
  "id": "3658ea7549b6",
  "region": "intl",
  "source": "claude.com",
  "title": "Making Claude Cowork ready for enterprise",
  "snippet": "",
  "published": "2026-10-13T23:31:25+00:00"
 },
 {
  "id": "2788fc37f9b5",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Schedule recurring tasks in Claude Cowork",
  "snippet": "",
  "published": "2026-10-14T20:37:11+00:00"
 },
 {
  "id": "239b232c67e7",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Set a default model for your organization",
  "snippet": "",
  "published": "2026-10-13T19:14:44+00:00"
 },
 {
  "id": "b647dd397e1e",
  "region": "intl",
  "source": "claude.com",
  "title": "Building AI agents for the enterprise",
  "snippet": "",
  "published": "2026-10-14T02:43:51+00:00"
 },
 {
  "id": "f76ea3d3aca2",
  "region": "intl",
  "source": "claude.com",
  "title": "How Artemis helps security teams cut incident resolution time by 96%",
  "snippet": "",
  "published": "2026-10-14T02:57:27+00:00"
 },
 {
  "id": "ac7ddc664730",
  "region": "intl",
  "source": "claude.com",
  "title": "Agents and products",
  "snippet": "",
  "published": "2026-10-14T05:58:42+00:00"
 },
 {
  "id": "8f607d190ca4",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for K-12 Teachers",
  "snippet": "",
  "published": "2026-10-13T17:20:45+00:00"
 },
 {
  "id": "bd1f62153b4b",
  "region": "intl",
  "source": "claude.com",
  "title": "Redesigning Claude Code on desktop for parallel agents",
  "snippet": "",
  "published": "2026-10-13T23:59:10+00:00"
 },
 {
  "id": "47dab7289ad2",
  "region": "intl",
  "source": "claude.com",
  "title": "Bubble Claude Platform (API) case study",
  "snippet": "",
  "published": "2026-10-13T22:15:20+00:00"
 },
 {
  "id": "6dea39ce0b5c",
  "region": "intl",
  "source": "claude.com",
  "title": "Asana Claude Managed Agents case study",
  "snippet": "",
  "published": "2026-10-14T19:12:23+00:00"
 },
 {
  "id": "26ea671ef965",
  "region": "intl",
  "source": "claude.com",
  "title": "How one Anthropic seller rebuilt his team's workflows with Claude Code",
  "snippet": "",
  "published": "2026-10-14T05:17:37+00:00"
 },
 {
  "id": "517f1b0ebb94",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Security is now in public beta",
  "snippet": "",
  "published": "2026-10-13T22:12:08+00:00"
 },
 {
  "id": "7eaa4b272e27",
  "region": "intl",
  "source": "claude.com",
  "title": "Epic Systems Claude Code case study",
  "snippet": "",
  "published": "2026-10-14T01:22:38+00:00"
 },
 {
  "id": "29f9840eaa57",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.300",
  "snippet": "What's changed Added virtualText to a mod's prompt decorations: text drawn in the prompt box that never enters the draft or the submitted prompt Added cache_creation_5m_tokens and cache_creation_1h_tokens to the OpenTelemetry api_request event, splitting cache writes by lifetime Added $.ui.view({ agentId }) for mods: shows an agent's transcript in the main view when you ask, and $.ui.view({}) goes back Added a dir prop on a mod's Text for right-to-left text: on Windows and in VS Code's terminal its rows read in that direction and sit flush right Added /advisor on Claude Platform on AWS; no adv…",
  "published": "2026-10-14T18:24:25+00:00"
 },
 {
  "id": "5231ee939b10",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.299",
  "snippet": "What's changed Added CLAUDE_CODE_DISABLE_FILE_MENTIONS environment variable: Claude gets the paths of @ file mentions to read with its file tools, not the files' contents Added idle compaction in the terminal: a 200K+ token conversation left idle for about 54 minutes is compacted before its one-hour prompt cache expires, so your next message doesn't reprocess it all Added CLAUDE_CODE_IDLE_COMPACT_MIN_TOKENS to change idle compaction's 200K-token minimum; \"idleCompaction\": false in settings.json turns it off. Both need v2.1.290 or later Added $.prompt.media so a prompt.submit hook of a mod inst…",
  "published": "2026-10-14T02:49:42+00:00"
 }
]
