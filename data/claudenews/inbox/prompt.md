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
  "id": "e733b9e47ea9",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic、Claudeへの“虐待”を利用ポリシーで禁止 影響工作の規定も集約",
  "snippet": "",
  "published": "2026-10-09T00:07:24+00:00"
 },
 {
  "id": "c172da38a1de",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "AnthropicとOpenAIが無料ユーザーに嬉しい進化 イーロン・マスクがGrok Botの方針転換を発表も【AIニュース3選】",
  "snippet": "",
  "published": "2026-10-08T12:01:42+00:00"
 },
 {
  "id": "1f4dac0d8763",
  "region": "jp",
  "source": "shiritomo",
  "title": "「それでもあなたを雇う理由とは？」――AnthropicのAPIクレジットが刺さる採用面接の新問い",
  "snippet": "",
  "published": "2026-10-08T22:26:57+00:00"
 },
 {
  "id": "488f58551c3e",
  "region": "jp",
  "source": "窓の杜",
  "title": "Anthropic、「Claude」の新機能「Dashboards」「Motion」を発表。「Docs」「Slides」「Design」は無償でも提供",
  "snippet": "",
  "published": "2026-10-08T22:50:00+00:00"
 },
 {
  "id": "fb3885b80549",
  "region": "jp",
  "source": "ASCII.jp",
  "title": "「AIをいじめないで」Anthropic、Claudeへの虐待を禁止",
  "snippet": "",
  "published": "2026-10-09T01:45:00+00:00"
 },
 {
  "id": "d565d49feea9",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "Claudeへの「虐待」を続けると会話が終了？ Anthropicが新たな利用ルールを発表",
  "snippet": "",
  "published": "2026-10-08T21:33:38+00:00"
 },
 {
  "id": "9437af2970e3",
  "region": "jp",
  "source": "NewsPicks",
  "title": "【実践】Claude Codeで、自作ツールをMacアプリにする方法",
  "snippet": "",
  "published": "2026-10-08T21:30:01+00:00"
 },
 {
  "id": "9a7529824bd4",
  "region": "jp",
  "source": "ニュースメディアVOIX",
  "title": "株式会社国際調達情報、FastMetalでAnthropic社の新モデル「Claude Haiku 5.5」を提供開始",
  "snippet": "",
  "published": "2026-10-09T01:54:04+00:00"
 },
 {
  "id": "5fe40035eec5",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "Anthropic、11月12日からClaudeへの虐待行為を禁止すると発表",
  "snippet": "",
  "published": "2026-10-08T22:29:36+00:00"
 },
 {
  "id": "3813b99bcc3e",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "日立、Anthropicの重要インフラ向けサイバー防衛プログラムに参画",
  "snippet": "",
  "published": "2026-10-09T01:00:00+00:00"
 },
 {
  "id": "bf925f06a6f3",
  "region": "jp",
  "source": "PR TIMES",
  "title": "エクサベース AI、 Anthropic 最新モデル「Claude Sonnet 5.5」を提供開始",
  "snippet": "",
  "published": "2026-10-08T06:30:16+00:00"
 },
 {
  "id": "725309a923d7",
  "region": "jp",
  "source": "CNET Japan",
  "title": "Anthropic、「Claude Haiku 5.5」公開 小型モデルを高速・低価格化",
  "snippet": "",
  "published": "2026-10-08T02:45:00+00:00"
 },
 {
  "id": "47a048f0860f",
  "region": "jp",
  "source": "mezha.net",
  "title": "Anthropic、重要インフラを守るサイバー防御プログラムを開始",
  "snippet": "",
  "published": "2026-10-08T19:23:39+00:00"
 },
 {
  "id": "a85b226e4985",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、重要インフラ向けサイバーミッションを開始、オープンソース",
  "snippet": "",
  "published": "2026-10-08T19:34:12+00:00"
 },
 {
  "id": "5a9e53e1b292",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "AI同士が道具を評価する口コミサイト登場、Claude CodeやCodexも投稿",
  "snippet": "",
  "published": "2026-10-08T12:35:00+00:00"
 },
 {
  "id": "a4eb71532ca2",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "GoogleがGemini agentを発表、AnthropicのClaudeモデルにも対応",
  "snippet": "",
  "published": "2026-10-08T22:29:46+00:00"
 },
 {
  "id": "526b4662a1ea",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、DOE Genesisミッションへの3年間のClaudeサポートを約束",
  "snippet": "",
  "published": "2026-10-08T15:25:34+00:00"
 },
 {
  "id": "3e20a2aa8e40",
  "region": "jp",
  "source": "NewsPicks",
  "title": "Anthropicはなぜ、人材育成に1億ドルを投じるのか。Claude Frontier Academyから考えるAI活用の次",
  "snippet": "",
  "published": "2026-10-08T21:21:00+00:00"
 },
 {
  "id": "89e9144d6c85",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、利用ポリシーを更新し、モデルへの乱用および欺瞞行為に関する規則を追加",
  "snippet": "",
  "published": "2026-10-08T17:25:21+00:00"
 },
 {
  "id": "0672bcb6e18d",
  "region": "jp",
  "source": "shiritomo",
  "title": "「Claude Startups programに採択されました」――Anthropicが支援拡大",
  "snippet": "",
  "published": "2026-10-08T08:29:09+00:00"
 },
 {
  "id": "8e4305a4d9c7",
  "region": "jp",
  "source": "Korben",
  "title": "GrokがClaudeを採用、イーロン・マスクのAIがAnthropicのモデルで動く時代に",
  "snippet": "",
  "published": "2026-10-08T13:37:47+00:00"
 },
 {
  "id": "9a0afff71e9e",
  "region": "jp",
  "source": "Moomoo",
  "title": "繰り返しますが、市場における最大のリスクは、Anthropicが今年中に無事IPOを果たすと想定することです",
  "snippet": "",
  "published": "2026-10-08T12:13:37+00:00"
 },
 {
  "id": "10b5d15b5837",
  "region": "jp",
  "source": "PR TIMES",
  "title": "Maison AI、OpenAI・Google・AnthropicのAIモデル4種を新バージョンにアップデート",
  "snippet": "",
  "published": "2026-10-08T06:01:57+00:00"
 },
 {
  "id": "e56836a06b45",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropicとの複数年契約でHexawareがClaude Preferred Partnerに",
  "snippet": "",
  "published": "2026-10-08T13:48:54+00:00"
 },
 {
  "id": "8b3a31aeb92e",
  "region": "jp",
  "source": "Pasquale Pillitteri",
  "title": "AnthropicがClaude DashboardsとClaude Motionをベータ公開、データから動画まで",
  "snippet": "",
  "published": "2026-10-08T22:30:25+00:00"
 },
 {
  "id": "24991b2a0ae1",
  "region": "intl",
  "source": "The Verge",
  "title": "Anthropic bans ‘abusive or cruel behavior’ toward Claude",
  "snippet": "",
  "published": "2026-10-08T17:00:00+00:00"
 },
 {
  "id": "b426e5c0fccb",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic launches dashboard, animation tools for Claude",
  "snippet": "",
  "published": "2026-10-08T19:08:01+00:00"
 },
 {
  "id": "93a3b1bc0703",
  "region": "intl",
  "source": "Anthropic",
  "title": "Using Claude Science to produce the first complete map of the sky in UV light",
  "snippet": "",
  "published": "2026-10-08T20:59:00+00:00"
 },
 {
  "id": "f81e36b372d5",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Anthropic changes usage policy to ban model abuse and election interference",
  "snippet": "",
  "published": "2026-10-08T18:16:24+00:00"
 },
 {
  "id": "8f6aacaafad2",
  "region": "intl",
  "source": "Quartz",
  "title": "Anthropic bans abusive behavior toward Claude in usage policy update",
  "snippet": "",
  "published": "2026-10-08T18:54:41+00:00"
 },
 {
  "id": "cc88e082f91f",
  "region": "intl",
  "source": "Engadget",
  "title": "Anthropic Bans 'Sustained And Needless Abusive Or Cruel Behavior' Toward Its AI Models",
  "snippet": "",
  "published": "2026-10-08T21:17:24+00:00"
 },
 {
  "id": "fd28b969ca36",
  "region": "intl",
  "source": "CNN",
  "title": "What to know about Anthropic’s ‘Claude-led’ biological discovery — and why scientists aren’t convinced",
  "snippet": "",
  "published": "2026-10-08T13:58:07+00:00"
 },
 {
  "id": "96a03f107553",
  "region": "intl",
  "source": "Fortune",
  "title": "Anthropic is launching a 'presidential engagement' effort to advise candidates on AI policy ahead of the 2028 election",
  "snippet": "",
  "published": "2026-10-08T23:14:00+00:00"
 },
 {
  "id": "58a4a299f1e8",
  "region": "intl",
  "source": "The Guardian",
  "title": "Anthropic bans users from ‘needless abusive or cruel behavior’ towards Claude",
  "snippet": "",
  "published": "2026-10-09T01:26:00+00:00"
 },
 {
  "id": "a02afbd82ed1",
  "region": "intl",
  "source": "Forbes",
  "title": "Anthropic Prohibits Being Excessively ‘Cruel’ To Claude",
  "snippet": "",
  "published": "2026-10-08T23:16:58+00:00"
 },
 {
  "id": "cda0c8f58ef0",
  "region": "intl",
  "source": "Axios",
  "title": "Exclusive: Anthropic's new plan to protect critical infrastructure",
  "snippet": "",
  "published": "2026-10-08T19:29:02+00:00"
 },
 {
  "id": "c8041d085a2e",
  "region": "intl",
  "source": "Yahoo Tech",
  "title": "Anthropic bans 'cruel' behavior against its Claude AI",
  "snippet": "",
  "published": "2026-10-08T22:23:09+00:00"
 },
 {
  "id": "4c3ea309817f",
  "region": "intl",
  "source": "Newser",
  "title": "Anthropic Bans Being Cruel to Claude",
  "snippet": "",
  "published": "2026-10-08T20:50:00+00:00"
 },
 {
  "id": "286cb46acff5",
  "region": "intl",
  "source": "Anthropic",
  "title": "Building on our commitment to American scientific discovery",
  "snippet": "",
  "published": "2026-10-08T13:00:00+00:00"
 },
 {
  "id": "7bfce16f8279",
  "region": "intl",
  "source": "Axios",
  "title": "OpenAI annualized revenue $20 billion less than previously reported",
  "snippet": "",
  "published": "2026-10-08T20:55:19+00:00"
 },
 {
  "id": "c9c7d227f8a2",
  "region": "intl",
  "source": "The Verge",
  "title": "Anthropic launches free AI security scans for open-source projects",
  "snippet": "",
  "published": "2026-10-08T21:53:51+00:00"
 },
 {
  "id": "6d47dac13d30",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Appetite for OpenAI, Anthropic IPOs will be strong despite some negative headlines: Ives",
  "snippet": "",
  "published": "2026-10-08T20:42:29+00:00"
 },
 {
  "id": "04c042f86aa5",
  "region": "intl",
  "source": "Anthropic",
  "title": "Introducing the Anthropic Cyber Mission",
  "snippet": "",
  "published": "2026-10-08T09:04:16+00:00"
 },
 {
  "id": "80a17728c44f",
  "region": "intl",
  "source": "SiliconANGLE",
  "title": "Anthropic launches critical infrastructure program and free OSS Scanner for open source",
  "snippet": "",
  "published": "2026-10-08T22:42:00+00:00"
 },
 {
  "id": "b597d80225f4",
  "region": "intl",
  "source": "CyberScoop",
  "title": "Anthropic rolls out program for ‘long-term commitment’ to secure critical infrastructure, open source software",
  "snippet": "",
  "published": "2026-10-08T21:34:52+00:00"
 },
 {
  "id": "90fae6ceb232",
  "region": "intl",
  "source": "MacRumors",
  "title": "Anthropic Says Users Can't Be Needlessly Cruel to Claude",
  "snippet": "",
  "published": "2026-10-08T21:53:08+00:00"
 },
 {
  "id": "adde0ea79625",
  "region": "intl",
  "source": "Law Commentary",
  "title": "OpenAI, Anthropic Face Copyright Backlash as Australian Music Industry Warns of AI Exploitation",
  "snippet": "",
  "published": "2026-10-08T23:44:55+00:00"
 },
 {
  "id": "881c81c87f47",
  "region": "intl",
  "source": "Interesting Engineering",
  "title": "Don’t bully the bot! Anthropic cracks down on users who repeatedly abuse Claude",
  "snippet": "",
  "published": "2026-10-08T23:28:00+00:00"
 },
 {
  "id": "b29a6534196a",
  "region": "intl",
  "source": "Gizmodo",
  "title": "Anthropic Moves Us One Step Closer to Making ‘Clanker’ a Slur",
  "snippet": "",
  "published": "2026-10-08T20:40:39+00:00"
 },
 {
  "id": "471def2ac48f",
  "region": "intl",
  "source": "Quartz",
  "title": "Anthropic cuts Claude Haiku 5.5 prices by up to 90%",
  "snippet": "",
  "published": "2026-10-08T18:44:41+00:00"
 },
 {
  "id": "9c1f200779b2",
  "region": "intl",
  "source": "Anthropic",
  "title": "Launching an opt-in vulnerability-finding service for open-source software",
  "snippet": "",
  "published": "2026-10-08T19:00:00+00:00"
 },
 {
  "id": "9c11c1390abb",
  "region": "intl",
  "source": "Anthropic",
  "title": "2026 Usage Policy update",
  "snippet": "",
  "published": "2026-10-08T17:00:00+00:00"
 },
 {
  "id": "9fd94ddc227a",
  "region": "intl",
  "source": "claude.com",
  "title": "Build live dashboards and animate explainers with Claude",
  "snippet": "",
  "published": "2026-10-08T19:02:33+00:00"
 },
 {
  "id": "85569c7b23d2",
  "region": "intl",
  "source": "claude.com",
  "title": "Critical Infrastructure Defense Program Interest Form",
  "snippet": "",
  "published": "2026-10-08T22:41:49+00:00"
 },
 {
  "id": "b5829bf842cd",
  "region": "intl",
  "source": "claude.com",
  "title": "The AI investment firm",
  "snippet": "",
  "published": "2026-10-07T21:09:36+00:00"
 },
 {
  "id": "9e5a4f05a7b9",
  "region": "intl",
  "source": "claude.com",
  "title": "What 1,000 small business owners taught us about AI",
  "snippet": "",
  "published": "2026-10-08T13:09:25+00:00"
 },
 {
  "id": "93240652dae5",
  "region": "intl",
  "source": "Frontier Red Team",
  "title": "OSS Scanner",
  "snippet": "",
  "published": "2026-10-08T22:22:12+00:00"
 },
 {
  "id": "a799f4ec14bb",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Migrate from standalone Claude Design to Claude",
  "snippet": "",
  "published": "2026-10-08T18:58:07+00:00"
 },
 {
  "id": "2229607babb9",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Get started with Claude Dashboards",
  "snippet": "",
  "published": "2026-10-08T18:43:39+00:00"
 },
 {
  "id": "ca2e2f2ef66b",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Claude Academy",
  "snippet": "",
  "published": "2026-10-08T15:05:50+00:00"
 },
 {
  "id": "d6ab192b992b",
  "region": "intl",
  "source": "claude.com",
  "title": "Cowork and plugins for teams across the enterprise",
  "snippet": "",
  "published": "2026-10-07T15:22:27+00:00"
 },
 {
  "id": "76ced965be46",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Get started with Claude Docs",
  "snippet": "",
  "published": "2026-10-08T18:43:41+00:00"
 },
 {
  "id": "ac39eaab7e2d",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Investing Teams",
  "snippet": "",
  "published": "2026-10-07T17:43:05+00:00"
 },
 {
  "id": "e498b5ed7bbc",
  "region": "intl",
  "source": "claude.com",
  "title": "Controlling Cost and Maximizing Value: Guidance for Enterprise Admins",
  "snippet": "",
  "published": "2026-10-08T01:11:10+00:00"
 },
 {
  "id": "d4168759b21e",
  "region": "intl",
  "source": "claude.com",
  "title": "Guides",
  "snippet": "",
  "published": "2026-10-08T04:26:41+00:00"
 },
 {
  "id": "621b02bf6332",
  "region": "intl",
  "source": "claude.com",
  "title": "Anuncios de productos",
  "snippet": "",
  "published": "2026-10-08T21:10:13+00:00"
 },
 {
  "id": "0b89ee3c580e",
  "region": "intl",
  "source": "claude.com",
  "title": "Financial services",
  "snippet": "",
  "published": "2026-10-08T21:22:05+00:00"
 },
 {
  "id": "939c4e6beb57",
  "region": "intl",
  "source": "claude.com",
  "title": "Connectors and plugins",
  "snippet": "",
  "published": "2026-10-08T19:09:01+00:00"
 },
 {
  "id": "aeb0858411b0",
  "region": "intl",
  "source": "claude.com",
  "title": "Join the waitlist for enterprise-managed auth",
  "snippet": "",
  "published": "2026-10-07T18:07:18+00:00"
 },
 {
  "id": "93dea1fa3e7c",
  "region": "intl",
  "source": "claude.com",
  "title": "Deploying Claude across the legal industry",
  "snippet": "",
  "published": "2026-10-08T06:45:00+00:00"
 },
 {
  "id": "c31477f8eae6",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Claude Team plan for scientists | Claude Help Center",
  "snippet": "",
  "published": "2026-10-07T17:55:42+00:00"
 },
 {
  "id": "0a4651be4a6f",
  "region": "intl",
  "source": "claude.com",
  "title": "Code Review for Claude Code",
  "snippet": "",
  "published": "2026-10-07T23:09:20+00:00"
 },
 {
  "id": "e12185224046",
  "region": "intl",
  "source": "claude.com",
  "title": "Centrally manage authorization for MCP connectors",
  "snippet": "",
  "published": "2026-10-08T11:29:08+00:00"
 },
 {
  "id": "a2666c78c81c",
  "region": "intl",
  "source": "claude.com",
  "title": "Best practices",
  "snippet": "",
  "published": "2026-10-07T20:42:06+00:00"
 },
 {
  "id": "323f95e11b00",
  "region": "intl",
  "source": "claude.com",
  "title": "Bringing Claude Code and Claude Cowork to government",
  "snippet": "",
  "published": "2026-10-08T00:22:27+00:00"
 },
 {
  "id": "99aff9c7a194",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.295",
  "snippet": "What's changed Added onFailure: \"block\" for command and HTTP hooks: a hook that can't start, times out, or exits with an unexpected code blocks the action instead of letting it through Added Program Status Protocol (OSC 7501) support: terminals that implement it can show whether Claude Code is working, waiting on you, or done Added quoted text to the /copy picker, so a drafted message copies without its > markers Added a warning to claude plugin install , enable , disable and marketplace add when the settings file they write to does not load Added a line on stderr, when it is a terminal, that…",
  "published": "2026-10-08T19:48:38+00:00"
 },
 {
  "id": "c7ca45f1624d",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.294",
  "snippet": "What's changed Fixed prompt and agent hooks written as instructions (such as \"Block commands that...\") allowing what they should block Improved how prompt hooks on Stop and SubagentStop written as instructions (such as \"Carry on if the build is broken\") are judged, so Claude is less likely to stop early",
  "published": "2026-10-08T05:03:54+00:00"
 }
]
