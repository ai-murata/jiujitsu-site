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
  "id": "cbb9ae21356a",
  "region": "jp",
  "source": "株式会社エクサウィザーズ",
  "title": "Anthropicの巨額IPOに見る収益力の「今」と発明するAIという「未来」",
  "snippet": "",
  "published": "2026-10-28T00:44:30+00:00"
 },
 {
  "id": "fa098772a1f4",
  "region": "jp",
  "source": "WIRED.jp",
  "title": "AnthropicのIPO目論見書から見えてきた、急成長の実態とAIの未来",
  "snippet": "",
  "published": "2026-10-27T04:00:00+00:00"
 },
 {
  "id": "dda7d34e7ca2",
  "region": "jp",
  "source": "AIsmiley",
  "title": "Claude（クロード）とは？できること・料金・使い方を解説",
  "snippet": "",
  "published": "2026-10-27T10:23:22+00:00"
 },
 {
  "id": "f8e21f6df1f3",
  "region": "jp",
  "source": "Unite.AI",
  "title": "GSA、AnthropicとのOneGov契約を拡大し、Claudeを40％割引",
  "snippet": "",
  "published": "2026-10-27T22:40:13+00:00"
 },
 {
  "id": "bb65574d3d03",
  "region": "jp",
  "source": "ITmedia",
  "title": "IPO目論見書に「AIは人類の存亡リスク」「コードの9割はClaude製」 Anthropicが示した規格外の見立て（1/2 ページ）",
  "snippet": "",
  "published": "2026-10-27T11:30:12+00:00"
 },
 {
  "id": "49731a9d8fb2",
  "region": "jp",
  "source": "Moomoo",
  "title": "速報：AnthropicのIPO申請書提出がAI半導体銘柄を急騰",
  "snippet": "",
  "published": "2026-10-27T16:33:42+00:00"
 },
 {
  "id": "63874edbbd3d",
  "region": "jp",
  "source": "BeInCrypto",
  "title": "Anthropic、上場前にNVIDIAとApple合計上回る現金保有",
  "snippet": "",
  "published": "2026-10-27T22:00:00+00:00"
 },
 {
  "id": "1095a5942077",
  "region": "jp",
  "source": "Media Innovation",
  "title": "Anthropic、4～6月期に営業黒字化、上半期売上は前年の14倍 ナスダックに「ANT」で上場申請",
  "snippet": "",
  "published": "2026-10-27T11:14:34+00:00"
 },
 {
  "id": "32cac29f6556",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicがIPOの米国個人投資家向け販売でJPモルガンを起用 執筆",
  "snippet": "",
  "published": "2026-10-28T01:09:00+00:00"
 },
 {
  "id": "8b7daf8549af",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropicが史上最大のIPOを計画：AI企業、最大1兆7500億ドル評価を目指す",
  "snippet": "",
  "published": "2026-10-27T18:39:00+00:00"
 },
 {
  "id": "71961e24cd4b",
  "region": "jp",
  "source": "WIRED.jp",
  "title": "人類滅亡のリスクが競争力に？ AnthropicのIPO目論見書が示していること",
  "snippet": "",
  "published": "2026-10-27T08:00:00+00:00"
 },
 {
  "id": "9f5a7c6f8843",
  "region": "jp",
  "source": "AIsmiley",
  "title": "Claude Coworkとは？料金・使い方・何ができるかを解説",
  "snippet": "",
  "published": "2026-10-27T12:53:43+00:00"
 },
 {
  "id": "d7a71fb28160",
  "region": "jp",
  "source": "株式会社エクサウィザーズ",
  "title": "「自分より賢いAIをつくるAI」、2027年にも Anthropic上場書類に映る開発現場",
  "snippet": "",
  "published": "2026-10-27T08:41:14+00:00"
 },
 {
  "id": "0498a92ced11",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claudeを活用した創薬の初期段階での進展を報告",
  "snippet": "",
  "published": "2026-10-27T20:42:05+00:00"
 },
 {
  "id": "268d782f2ffa",
  "region": "jp",
  "source": "Moomoo",
  "title": "Anthropicの8,000億ドル規模のコンピューティング契約：需要が依然として不確定要因",
  "snippet": "",
  "published": "2026-10-27T14:00:30+00:00"
 },
 {
  "id": "ef9a2e3ec0bc",
  "region": "jp",
  "source": "AIsmiley",
  "title": "Claude Sonnet 5とは？性能・料金・Sonnet 4.6との違いを徹底解説",
  "snippet": "",
  "published": "2026-10-27T13:10:13+00:00"
 },
 {
  "id": "171d2153dc16",
  "region": "jp",
  "source": "Moomoo",
  "title": "AnthropicのIPO：AI巨人の成長、経済性、そしてソフトウェア業界の変革の内幕",
  "snippet": "",
  "published": "2026-10-27T15:18:48+00:00"
 },
 {
  "id": "f716d1e3118d",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropicの研究、判断を要する課題でアナリストがAIエージェントに判断を委ねる実態を明らかに",
  "snippet": "",
  "published": "2026-10-27T19:10:11+00:00"
 },
 {
  "id": "7f3f1c5d6202",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "AnthropicがIPO申請書を提出、異例の形でTSMCを名指しし先端半導体の台湾集中リスクを警告",
  "snippet": "",
  "published": "2026-10-27T18:31:00+00:00"
 },
 {
  "id": "05bdf626fa7c",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicのIPO、AI成長ストーリーへの市場の忍耐力を試す＝Firstrade 執筆",
  "snippet": "",
  "published": "2026-10-27T17:48:00+00:00"
 },
 {
  "id": "73b2b7305838",
  "region": "jp",
  "source": "Moomoo",
  "title": "TSMCのパッケージング価格が上昇、AnthropicがS-1を提出",
  "snippet": "",
  "published": "2026-10-27T12:38:07+00:00"
 },
 {
  "id": "baa6a676eb11",
  "region": "jp",
  "source": "株式会社エクサウィザーズ",
  "title": "【連載】PdMがAIを「自分専属の秘書」に（前編） ～Claude Codeで散らばる情報を一元化し、AIとマルチタスクをこなす日常へ～",
  "snippet": "",
  "published": "2026-10-27T04:33:46+00:00"
 },
 {
  "id": "57501f88401a",
  "region": "jp",
  "source": "BeInCrypto",
  "title": "クレイマー氏、Anthropic上場でこの大手銀を買い推奨",
  "snippet": "",
  "published": "2026-10-27T17:21:43+00:00"
 },
 {
  "id": "9dc630ed92f9",
  "region": "jp",
  "source": "Unite.AI",
  "title": "InvescoとAnthropic、Claude上でアドバイザー向けポートフォリオツールを連携",
  "snippet": "",
  "published": "2026-10-27T17:06:01+00:00"
 },
 {
  "id": "b35182575985",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicがIPO申請で保険の不備を警告、15億ドルの著作権和解を受け 執筆",
  "snippet": "",
  "published": "2026-10-27T16:52:00+00:00"
 },
 {
  "id": "851ab2c12c7c",
  "region": "intl",
  "source": "Anthropic",
  "title": "Early progress on accelerating drug development with Claude",
  "snippet": "",
  "published": "2026-10-27T20:20:53+00:00"
 },
 {
  "id": "9ca19d0dc977",
  "region": "intl",
  "source": "CBS News",
  "title": "Anthropic's IPO filing lists 93 pages of risks. What could possibly go wrong?",
  "snippet": "",
  "published": "2026-10-27T19:28:00+00:00"
 },
 {
  "id": "b2b88060f398",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic's IPO is risky business",
  "snippet": "",
  "published": "2026-10-27T11:00:01+00:00"
 },
 {
  "id": "83da2e1baec4",
  "region": "intl",
  "source": "WSJ",
  "title": "Exclusive | Broadcom CEO Intervened to Seal $63 Billion Anthropic Debt Deal",
  "snippet": "",
  "published": "2026-10-27T17:50:00+00:00"
 },
 {
  "id": "802081ed7311",
  "region": "intl",
  "source": "The New York Times",
  "title": "Who Stands to Gain From an Anthropic I.P.O.",
  "snippet": "",
  "published": "2026-10-27T19:17:28+00:00"
 },
 {
  "id": "eb847728465f",
  "region": "intl",
  "source": "Axios",
  "title": "Anthropic files for its IPO",
  "snippet": "",
  "published": "2026-10-27T11:34:27+00:00"
 },
 {
  "id": "f239787bc099",
  "region": "intl",
  "source": "PBS",
  "title": "Anthropic says risks for investors include blowback from runaway AI",
  "snippet": "",
  "published": "2026-10-27T18:28:55+00:00"
 },
 {
  "id": "d2d46e16192a",
  "region": "intl",
  "source": "AP News",
  "title": "Anthropic expands AI support for nonprofits as it files to sell shares to the public",
  "snippet": "",
  "published": "2026-10-27T17:10:56+00:00"
 },
 {
  "id": "b83d74a6aed1",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "When is the Anthropic IPO? SEC rules and SpaceX’s sprint point to Nov. 16-18",
  "snippet": "",
  "published": "2026-10-27T15:54:05+00:00"
 },
 {
  "id": "eb3e4612f707",
  "region": "intl",
  "source": "Business Insider",
  "title": "Nvidia's worst nightmare may be lurking inside Anthropic's IPO filing",
  "snippet": "",
  "published": "2026-10-27T20:31:00+00:00"
 },
 {
  "id": "ebdea15a4aad",
  "region": "intl",
  "source": "The Guardian",
  "title": "Four takeaways from Anthropic’s potentially record-breaking stock market filing",
  "snippet": "",
  "published": "2026-10-27T15:27:00+00:00"
 },
 {
  "id": "9f283278fce4",
  "region": "intl",
  "source": "ABC News - Breaking News, Latest News and Videos",
  "title": "Pentagon gives Anthropic ultimatum on AI technology: Sources",
  "snippet": "",
  "published": "2026-10-27T15:51:55+00:00"
 },
 {
  "id": "55d127c81982",
  "region": "intl",
  "source": "Anthropic",
  "title": "Expanding our partnership with GSA to bring Claude to all levels of government",
  "snippet": "",
  "published": "2026-10-27T22:23:13+00:00"
 },
 {
  "id": "cd6dd809ab0d",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic's IPO could be 'speculative fiction' or a 'generational moment' — investors are split",
  "snippet": "",
  "published": "2026-10-27T17:26:34+00:00"
 },
 {
  "id": "f77ef8d269c8",
  "region": "intl",
  "source": "WSJ",
  "title": "Anthropic’s ‘Adjusted’ Profit Exposes Wall Street’s Earnings Game",
  "snippet": "",
  "published": "2026-10-27T09:30:00+00:00"
 },
 {
  "id": "881bba48fd45",
  "region": "intl",
  "source": "Axios",
  "title": "Claude says Anthropic's IPO is a buy. ChatGPT disagrees",
  "snippet": "",
  "published": "2026-10-27T11:18:44+00:00"
 },
 {
  "id": "66f6e1e9018b",
  "region": "intl",
  "source": "Anthropic",
  "title": "How AI agents shape experts’ judgment calls",
  "snippet": "",
  "published": "2026-10-27T18:50:53+00:00"
 },
 {
  "id": "78033363c096",
  "region": "intl",
  "source": "CNBC",
  "title": "Chart: Anthropic's cash pile towers over nearly every U.S. company",
  "snippet": "",
  "published": "2026-10-27T21:12:55+00:00"
 },
 {
  "id": "a8e6873df252",
  "region": "intl",
  "source": "Barron's",
  "title": "Why Broadcom Is the Big Anthropic IPO Winner. The Stock Jumps on Buy Upgrade.",
  "snippet": "",
  "published": "2026-10-27T17:50:00+00:00"
 },
 {
  "id": "a3e037b1593a",
  "region": "intl",
  "source": "CNN",
  "title": "From bioweapons to blackmail, here’s what’s in Anthropic’s nearly 100-page list of risks, including ‘risks to humanity’",
  "snippet": "",
  "published": "2026-10-27T10:00:16+00:00"
 },
 {
  "id": "caf615d2c5f9",
  "region": "intl",
  "source": "ABC News - Breaking News, Latest News and Videos",
  "title": "Exclusive: Anthropic CEO calls for stronger regulation of AI",
  "snippet": "",
  "published": "2026-10-27T17:08:26+00:00"
 },
 {
  "id": "6938d58b8b30",
  "region": "intl",
  "source": "The New York Times",
  "title": "In Anthropic I.P.O., Goldman and Morgan Stanley Slug It Out for Top Bank",
  "snippet": "",
  "published": "2026-10-27T10:09:10+00:00"
 },
 {
  "id": "68403036b114",
  "region": "intl",
  "source": "R&D World",
  "title": "Anthropic acquires a one-person biotech that used Claude to coordinate 11 labs",
  "snippet": "",
  "published": "2026-10-27T23:10:01+00:00"
 },
 {
  "id": "033d61c3f3f9",
  "region": "intl",
  "source": "Politico",
  "title": "Anthropic to Newsom: Courts should have power to block risky AI",
  "snippet": "",
  "published": "2026-10-27T23:27:00+00:00"
 },
 {
  "id": "a3b948ddc24a",
  "region": "intl",
  "source": "Fortune",
  "title": "Anthropic’s S-1, by the numbers: A thriving business—with a $498 billion asterisk",
  "snippet": "",
  "published": "2026-10-27T08:00:00+00:00"
 },
 {
  "id": "d69697bc8857",
  "region": "intl",
  "source": "Anthropic",
  "title": "Discovering and exploiting vulnerabilities in critical, real-world software with Claude",
  "snippet": "",
  "published": "2026-10-27T18:20:51+00:00"
 },
 {
  "id": "97ce4c3b6489",
  "region": "intl",
  "source": "claude.com",
  "title": "Zero Trust for AI agents",
  "snippet": "",
  "published": "2026-10-27T23:23:12+00:00"
 },
 {
  "id": "4dc9df0be999",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Models, usage, and limits in Claude Code | Claude Help Center",
  "snippet": "",
  "published": "2026-10-27T16:58:58+00:00"
 },
 {
  "id": "ad10f6f67cfc",
  "region": "intl",
  "source": "Anthropic",
  "title": "Anthropic in London: AI and Science",
  "snippet": "",
  "published": "2026-10-27T23:14:30+00:00"
 },
 {
  "id": "ef70d6944d6d",
  "region": "intl",
  "source": "claude.com",
  "title": "Mid-Ohio Food Collective Claude case study | Claude by Anthropic",
  "snippet": "",
  "published": "2026-10-26T18:37:17+00:00"
 },
 {
  "id": "2a3412fb989a",
  "region": "intl",
  "source": "claude.com",
  "title": "Montgomery County Food Bank Claude case study | Claude by Anthropic",
  "snippet": "",
  "published": "2026-10-26T18:36:35+00:00"
 },
 {
  "id": "231988a190fa",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Claude Code user FAQ",
  "snippet": "",
  "published": "2026-10-27T03:52:57+00:00"
 },
 {
  "id": "e478f0ab1412",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Contract redlining",
  "snippet": "",
  "published": "2026-10-27T10:01:59+00:00"
 },
 {
  "id": "6ebd6fc69419",
  "region": "intl",
  "source": "assets.claude.com",
  "title": "Redacted Risk Report August 2026",
  "snippet": "",
  "published": "2026-10-27T02:01:24+00:00"
 },
 {
  "id": "3da546a7a663",
  "region": "intl",
  "source": "claude.com",
  "title": "Redesigning Claude Code on desktop for parallel agents",
  "snippet": "",
  "published": "2026-10-27T18:14:12+00:00"
 },
 {
  "id": "b4b7306e563f",
  "region": "intl",
  "source": "claude.com",
  "title": "Think through hard problems in voice mode",
  "snippet": "",
  "published": "2026-10-27T13:57:13+00:00"
 },
 {
  "id": "92e15f0483ed",
  "region": "intl",
  "source": "claude.com",
  "title": "Invesco for Advisors connector",
  "snippet": "",
  "published": "2026-10-27T07:47:22+00:00"
 },
 {
  "id": "ff440165ea7b",
  "region": "intl",
  "source": "claude.com",
  "title": "Nevis connector",
  "snippet": "",
  "published": "2026-10-27T06:29:40+00:00"
 },
 {
  "id": "62f385807688",
  "region": "intl",
  "source": "claude.com",
  "title": "CARE Claude Enterprise case study | Claude by Anthropic",
  "snippet": "",
  "published": "2026-10-26T18:31:36+00:00"
 },
 {
  "id": "cbac44b42ec9",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Enterprise",
  "snippet": "",
  "published": "2026-10-27T14:05:36+00:00"
 },
 {
  "id": "4b3e4e064c87",
  "region": "intl",
  "source": "claude.com",
  "title": "FINNY connector",
  "snippet": "",
  "published": "2026-10-27T07:47:22+00:00"
 },
 {
  "id": "8a4c84d1a3d1",
  "region": "intl",
  "source": "claude.com",
  "title": "LaunchDarkly",
  "snippet": "",
  "published": "2026-10-26T17:44:30+00:00"
 },
 {
  "id": "6217ed6188f2",
  "region": "intl",
  "source": "claude.com",
  "title": "Theysaid connector",
  "snippet": "",
  "published": "2026-10-27T14:27:01+00:00"
 },
 {
  "id": "66527347e145",
  "region": "intl",
  "source": "claude.com",
  "title": "AdisInsight connector",
  "snippet": "",
  "published": "2026-10-26T23:09:50+00:00"
 },
 {
  "id": "8ac97205d813",
  "region": "intl",
  "source": "claude.com",
  "title": "komoot connector",
  "snippet": "",
  "published": "2026-10-26T17:52:15+00:00"
 },
 {
  "id": "82a62611d350",
  "region": "intl",
  "source": "claude.com",
  "title": "J.P. Morgan Asset Management (55ip) connector",
  "snippet": "",
  "published": "2026-10-27T06:57:57+00:00"
 },
 {
  "id": "78e8771d40de",
  "region": "intl",
  "source": "claude.com",
  "title": "Ando",
  "snippet": "",
  "published": "2026-10-27T13:47:26+00:00"
 },
 {
  "id": "c4dbc1fda125",
  "region": "intl",
  "source": "claude.com",
  "title": "Zero risk isn't the job: a CISO's guide to agentic AI",
  "snippet": "",
  "published": "2026-10-27T15:34:56+00:00"
 },
 {
  "id": "5449a73edb7e",
  "region": "intl",
  "source": "claude.com",
  "title": "Build Agents with the Claude Platform on Google Cloud",
  "snippet": "",
  "published": "2026-10-27T19:06:55+00:00"
 },
 {
  "id": "ff8296c202dd",
  "region": "intl",
  "source": "claude.com",
  "title": "skill-creator",
  "snippet": "",
  "published": "2026-10-27T17:38:23+00:00"
 },
 {
  "id": "3fa83c67bd72",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.312",
  "snippet": "What's changed Added oidc.user_id_claim to the Claude apps gateway, to identify people by an id_token claim other than sub , such as Microsoft Entra ID's oid Added click to send: in fullscreen, clicking the \"to send now\" hint under a queued message sends it right away, as its key does Fixed managed settings and organization policy not being fetched for the rest of the session after signing in from the VS Code extension Fixed Claude overwriting a very large CLAUDE.md, rules file or @-included file in a subdirectory after seeing only its start; Write now asks Claude to read it all or edit in pla…",
  "published": "2026-10-27T20:24:20+00:00"
 }
]
