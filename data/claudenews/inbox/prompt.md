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
  "id": "e3baa477611b",
  "region": "jp",
  "source": "日経クロステック",
  "title": "Claude Codeを相棒に記者が月2kg減量、個人向けエージェントの可能性",
  "snippet": "",
  "published": "2026-11-04T20:00:00+00:00"
 },
 {
  "id": "aff735fde7bc",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "AnthropicのAI「Claude」が生命科学の40年来の謎に挑む、96個のタンパク質が作る巨大構造を解明",
  "snippet": "",
  "published": "2026-11-05T01:10:20+00:00"
 },
 {
  "id": "74e3aa4138ac",
  "region": "jp",
  "source": "合同会社ロケットボーイズ",
  "title": "AIコードエディタCursorのマーケットプレイス「Claude Code」拡張機能に悪性コード混入、最大5,000ユーザーに影響の可能性 SSHバックドア設置狙う|セキュリティニュースのセキュリティ対策Lab",
  "snippet": "",
  "published": "2026-11-04T21:00:03+00:00"
 },
 {
  "id": "21beb91f347f",
  "region": "jp",
  "source": "ｄメニューニュース",
  "title": "Claude Codeを装う悪意ある拡張機能がCursorで配布、SSHバックドア設置を試みる",
  "snippet": "",
  "published": "2026-11-05T01:05:00+00:00"
 },
 {
  "id": "43a7a995359a",
  "region": "jp",
  "source": "ICT教育ニュース",
  "title": "DAIJOBU、議員秘書と政治を学ぶ学生向けにClaude Code勉強会を開催",
  "snippet": "",
  "published": "2026-11-05T01:25:52+00:00"
 },
 {
  "id": "11b3c9303b6f",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Claudeのエンジニアが警告：AIによるコード代筆が「理解負債」を生む、マージ前にテストを",
  "snippet": "",
  "published": "2026-11-05T00:56:00+00:00"
 },
 {
  "id": "4767b2fd85ac",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、Claudeを活用して細菌とファージのタンパク質がボールトを形成することを示す",
  "snippet": "",
  "published": "2026-11-04T20:12:05+00:00"
 },
 {
  "id": "a03f2076f3e5",
  "region": "jp",
  "source": "Infoseek",
  "title": "Hajimari、Anthropic社の「Claude Partner Network」に参画。『TUKURUS』でAIを活かした開発・内製化を支援",
  "snippet": "",
  "published": "2026-11-05T01:15:43+00:00"
 },
 {
  "id": "90de4fc8c7b5",
  "region": "jp",
  "source": "shiritomo",
  "title": "「金曜日が最後の日でした」――Claude Code製品リードが退社表明、IPO目前のAnthropicで3人目",
  "snippet": "",
  "published": "2026-11-04T08:36:42+00:00"
 },
 {
  "id": "9a0484391960",
  "region": "jp",
  "source": "Business Insider Japan",
  "title": "アンソロピックIPO、参加すべきか見送るべきか？ 日本の証券会社でも案内開始",
  "snippet": "",
  "published": "2026-11-04T08:10:00+00:00"
 },
 {
  "id": "7bb32c8266be",
  "region": "jp",
  "source": "Unite.AI",
  "title": "Anthropic、パートナーエージェントと製品を加えてClaude Marketplaceを拡充",
  "snippet": "",
  "published": "2026-11-04T19:30:01+00:00"
 },
 {
  "id": "5df7fc6e8af9",
  "region": "jp",
  "source": "shiritomo",
  "title": "20万トークン未満は対象外――Claude Code、キャッシュ切れ54分前に会話を自動要約",
  "snippet": "",
  "published": "2026-11-04T08:36:54+00:00"
 },
 {
  "id": "a17447231187",
  "region": "jp",
  "source": "The Japan Times Alpha Online",
  "title": "Anthropic commits 5% of its stock to a new ‘public benefit’ fund",
  "snippet": "",
  "published": "2026-11-04T14:18:22+00:00"
 },
 {
  "id": "cd0a5d2f1e31",
  "region": "jp",
  "source": "Gizmodo",
  "title": "PCの乗っ取りを狙うClaude Code拡張、発見される。削除だけでは対策不十分",
  "snippet": "",
  "published": "2026-11-04T10:00:00+00:00"
 },
 {
  "id": "e3a9b791520b",
  "region": "jp",
  "source": "Moomoo",
  "title": "Anthropicの収益は氷山の一角に過ぎない。",
  "snippet": "",
  "published": "2026-11-04T13:48:37+00:00"
 },
 {
  "id": "420b669b451a",
  "region": "jp",
  "source": "Unite.AI",
  "title": "TeraWulf、Anthropicのケンタッキー州AIキャンパスでGoogleの保証を確保",
  "snippet": "",
  "published": "2026-11-04T16:17:02+00:00"
 },
 {
  "id": "3b9370650de3",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "Anthropic 、「Claude Code」によるゲームの複製を制限",
  "snippet": "",
  "published": "2026-11-04T01:05:00+00:00"
 },
 {
  "id": "00ac4b06bec0",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic、AIの応答が「本当にそのモデルによるものか」を暗号技術で証明する「FlashProve」を公開",
  "snippet": "",
  "published": "2026-11-04T01:40:15+00:00"
 },
 {
  "id": "d9f471282104",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、「AIすり替え」を暴く検証技術を公開…重みを秘匿したまま出所を証明",
  "snippet": "",
  "published": "2026-11-04T08:45:00+00:00"
 },
 {
  "id": "c8e726c7ba1e",
  "region": "jp",
  "source": "Korben",
  "title": "RevolutがClaude Codeを中国製AIに乗り換え、コストを10分の1に削減",
  "snippet": "",
  "published": "2026-11-04T09:39:50+00:00"
 },
 {
  "id": "e4f0a3d90e17",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "人間原理とAI開発競争の背後にある課題。",
  "snippet": "",
  "published": "2026-11-04T15:52:44+00:00"
 },
 {
  "id": "3a84e763ea14",
  "region": "jp",
  "source": "合同会社ロケットボーイズ",
  "title": "Anthropic、Claude Coworkの仮想マシン内にEDRセンサーを導入可能に CrowdStrikeなど7社に対応、AIエージェントの実行状況を監視|セキュリティニュースのセキュリティ対策Lab",
  "snippet": "",
  "published": "2026-11-04T07:00:27+00:00"
 },
 {
  "id": "d27ae422e172",
  "region": "jp",
  "source": "Vietnam.vn",
  "title": "雰囲気を変えた人がちょうど去ったところだ。",
  "snippet": "",
  "published": "2026-11-04T11:13:01+00:00"
 },
 {
  "id": "ca32ce685899",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Apple TV 4KでNintendo Switchゲームがネイティブ動作、AI支援のオープンソースプロジェクト",
  "snippet": "",
  "published": "2026-11-04T17:35:00+00:00"
 },
 {
  "id": "6f2ea6c4bda7",
  "region": "jp",
  "source": "OrcaRouter",
  "title": "Claudy Day：3つのclaude.aiの欠陥が連鎖する仕組み",
  "snippet": "",
  "published": "2026-11-04T10:59:22+00:00"
 },
 {
  "id": "4db192e7a60a",
  "region": "intl",
  "source": "Business Insider",
  "title": "A top Anthropic product leader has been poached by OpenAI",
  "snippet": "",
  "published": "2026-11-05T00:57:00+00:00"
 },
 {
  "id": "46631757ee0c",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Should You Buy Anthropic's IPO on Day 1?",
  "snippet": "",
  "published": "2026-11-04T19:29:00+00:00"
 },
 {
  "id": "70eb9ddfcb77",
  "region": "intl",
  "source": "Courthouse News",
  "title": "Music publishers suffer setback in copyright case against Anthropic",
  "snippet": "",
  "published": "2026-11-04T22:56:45+00:00"
 },
 {
  "id": "68da0472c35a",
  "region": "intl",
  "source": "Fortune",
  "title": "Dario Amodei wants 'a country of geniuses in a data center.' Realizing that vision requires risky financial mechanics, Anthropic's IPO filing shows",
  "snippet": "",
  "published": "2026-11-04T11:22:00+00:00"
 },
 {
  "id": "f6e8ff5b5502",
  "region": "intl",
  "source": "Reuters",
  "title": "TeraWulf gets credit backstop from Google for Anthropic data-center project",
  "snippet": "",
  "published": "2026-11-04T14:11:15+00:00"
 },
 {
  "id": "af9a8a7eb778",
  "region": "intl",
  "source": "ADWEEK",
  "title": "Anthropic Strikes Its First Licensing Deal, With the AP, for Election Coverage",
  "snippet": "",
  "published": "2026-11-05T00:00:00+00:00"
 },
 {
  "id": "806c353ca46c",
  "region": "intl",
  "source": "The New Stack",
  "title": "Anthropic found a way to prove which AI model answered you — but there’s a costly catch",
  "snippet": "",
  "published": "2026-11-04T22:51:08+00:00"
 },
 {
  "id": "fbdb83ed48e0",
  "region": "intl",
  "source": "PYMNTS.com",
  "title": "Anthropic Develops Tools to Confirm AI Models’ Identities",
  "snippet": "",
  "published": "2026-11-04T20:34:50+00:00"
 },
 {
  "id": "371e35bf861a",
  "region": "intl",
  "source": "Forbes",
  "title": "Are We Ready For A World Without Managers? Anthropic’s Vision Of The Future",
  "snippet": "",
  "published": "2026-11-04T23:09:59+00:00"
 },
 {
  "id": "4397e1644658",
  "region": "intl",
  "source": "XDA",
  "title": "I let Claude Code debloat my 4-year-old Windows laptop, and it found 30 GB of junk I never needed",
  "snippet": "",
  "published": "2026-11-05T00:01:00+00:00"
 },
 {
  "id": "caff822d439d",
  "region": "intl",
  "source": "Crain's Chicago Business",
  "title": "Opinion: Anthropic’s stark warning makes the case for taking AI out of Silicon Valley’s hands",
  "snippet": "",
  "published": "2026-11-04T17:06:49+00:00"
 },
 {
  "id": "81134101b956",
  "region": "intl",
  "source": "TradingView",
  "title": "Cat Wu, Former Head Of Product For Claude Code At Anthropic, Joins OpenAI To Lead Product Management For Core Products - X Post",
  "snippet": "",
  "published": "2026-11-05T01:13:00+00:00"
 },
 {
  "id": "54bedd8372d1",
  "region": "intl",
  "source": "Cassandra Unchained | Michael Burry",
  "title": "Anthropic’s Amended Prospectus Form S-1/A: 3rd Quarter Results & More Questions",
  "snippet": "",
  "published": "2026-11-04T20:50:33+00:00"
 },
 {
  "id": "0384ac58ce97",
  "region": "intl",
  "source": "The Decoder",
  "title": "Anthropic's text watermark is easy to bypass on several older Claude models",
  "snippet": "",
  "published": "2026-11-04T19:07:53+00:00"
 },
 {
  "id": "18f57f8ecb6f",
  "region": "intl",
  "source": "Interesting Engineering",
  "title": "Anthropic maps world’s first 3D bacterial vault with 96 copies of one protein",
  "snippet": "",
  "published": "2026-11-04T23:25:00+00:00"
 },
 {
  "id": "f51f591b6149",
  "region": "intl",
  "source": "Morningstar",
  "title": "Anthropic: After the IPO, Who Controls the Company?",
  "snippet": "",
  "published": "2026-11-04T21:32:42+00:00"
 },
 {
  "id": "ac61a549fe74",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "One Wall Street Analyst Says This Stock Is the Best Way to Invest in Anthropic and OpenAI. He's Right.",
  "snippet": "",
  "published": "2026-11-04T15:30:00+00:00"
 },
 {
  "id": "d1683dc0f667",
  "region": "intl",
  "source": "Georgetown University",
  "title": "SpaceX Executives, Anthropic Have Pledged Billions in Stock to the Public. What’s the Catch?",
  "snippet": "",
  "published": "2026-11-04T14:50:10+00:00"
 },
 {
  "id": "6782c5a763be",
  "region": "intl",
  "source": "Newcomer | Substack",
  "title": "Latest Fundraising Efforts Show OpenAI & Anthropic on Divergent Paths",
  "snippet": "",
  "published": "2026-11-04T21:15:13+00:00"
 },
 {
  "id": "a07258b1a634",
  "region": "intl",
  "source": "Unite.AI",
  "title": "Anthropic Uses Claude to Show Bacterial and Phage Proteins Form Vaults",
  "snippet": "",
  "published": "2026-11-04T20:12:05+00:00"
 },
 {
  "id": "a06b03026c79",
  "region": "intl",
  "source": "Unite.AI",
  "title": "Anthropic Expands Claude Marketplace with Partner Agents and Products",
  "snippet": "",
  "published": "2026-11-04T19:30:01+00:00"
 },
 {
  "id": "3471671368a7",
  "region": "intl",
  "source": "ABC News - Breaking News, Latest News and Videos",
  "title": "Judge appears skeptical of Pentagon arguments in legal fight over Anthropic 'supply chain risk' designation",
  "snippet": "",
  "published": "2026-11-03T22:03:13+00:00"
 },
 {
  "id": "8e19a23c1409",
  "region": "intl",
  "source": "Unite.AI",
  "title": "TeraWulf Lines Up Google Backstop for Anthropic’s Kentucky AI Campus",
  "snippet": "",
  "published": "2026-11-04T16:17:02+00:00"
 },
 {
  "id": "745d90bc8083",
  "region": "intl",
  "source": "Barchart.com",
  "title": "SpaceX Stock Can Get a Lift From the Anthropic IPO, but SPCX Remains Unappealing",
  "snippet": "",
  "published": "2026-11-04T19:12:11+00:00"
 },
 {
  "id": "011821b5ca37",
  "region": "intl",
  "source": "HackerNoon",
  "title": "My Claude Code Workflow: Lessons From Rebuilding a Website in Two Days",
  "snippet": "",
  "published": "2026-11-04T08:05:06+00:00"
 },
 {
  "id": "e2e27efb0d2a",
  "region": "intl",
  "source": "Anthropic",
  "title": "Investigating vault particles with Claude",
  "snippet": "",
  "published": "2026-11-04T22:02:45+00:00"
 },
 {
  "id": "7b59f6402c31",
  "region": "intl",
  "source": "claude.com",
  "title": "New agents and products for security, productivity, and creative work on Claude Marketplace",
  "snippet": "",
  "published": "2026-11-04T20:11:35+00:00"
 },
 {
  "id": "d2401c41e764",
  "region": "intl",
  "source": "assets.claude.com",
  "title": "FlashProve: an open-source library for provable inference",
  "snippet": "",
  "published": "2026-11-03T22:11:53+00:00"
 },
 {
  "id": "96fd34fa62db",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Cyber Verification Program Security Requirements | Claude Help Center",
  "snippet": "",
  "published": "2026-11-03T17:32:44+00:00"
 },
 {
  "id": "d8c8552250ec",
  "region": "intl",
  "source": "Anthropic",
  "title": "The Briefing: Work at the Frontier Livestream",
  "snippet": "",
  "published": "2026-11-04T15:41:58+00:00"
 },
 {
  "id": "f4e085a70e12",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "How do Anthropic-hosted browsers identify themselves when they browse the web on a user's behalf?",
  "snippet": "",
  "published": "2026-11-04T22:04:37+00:00"
 },
 {
  "id": "8698f17c16e3",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Security is now in public beta",
  "snippet": "",
  "published": "2026-11-04T21:09:42+00:00"
 },
 {
  "id": "f01daff41833",
  "region": "intl",
  "source": "claude.com",
  "title": "1M context is now generally available for Opus 4.6 and Sonnet 4.6",
  "snippet": "",
  "published": "2026-11-04T12:53:13+00:00"
 },
 {
  "id": "4343621fff02",
  "region": "intl",
  "source": "claude.com",
  "title": "Toffu connector",
  "snippet": "",
  "published": "2026-11-04T22:55:37+00:00"
 },
 {
  "id": "ff9ecde6445e",
  "region": "intl",
  "source": "claude.com",
  "title": "Dext connector",
  "snippet": "",
  "published": "2026-11-04T19:41:27+00:00"
 },
 {
  "id": "69a50b30188d",
  "region": "intl",
  "source": "claude.com",
  "title": "Flipsnack connector",
  "snippet": "",
  "published": "2026-11-04T14:15:35+00:00"
 },
 {
  "id": "e5aef58b0126",
  "region": "intl",
  "source": "claude.com",
  "title": "Zoom Agentic Search",
  "snippet": "",
  "published": "2026-11-03T17:38:59+00:00"
 },
 {
  "id": "729ca86f80c5",
  "region": "intl",
  "source": "claude.com",
  "title": "Onfire connector",
  "snippet": "",
  "published": "2026-11-04T05:27:11+00:00"
 },
 {
  "id": "def0f1cadf03",
  "region": "intl",
  "source": "claude.com",
  "title": "Squarespace connector",
  "snippet": "",
  "published": "2026-11-04T01:54:25+00:00"
 },
 {
  "id": "546cde617ea2",
  "region": "intl",
  "source": "claude.com",
  "title": "Code Review for Claude Code",
  "snippet": "",
  "published": "2026-11-04T17:24:50+00:00"
 },
 {
  "id": "cba9febf78bf",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Claude Academy",
  "snippet": "",
  "published": "2026-11-04T01:52:18+00:00"
 },
 {
  "id": "8eece859034f",
  "region": "intl",
  "source": "claude.com",
  "title": "Configuration changelog",
  "snippet": "",
  "published": "2026-11-04T10:03:38+00:00"
 },
 {
  "id": "533a8304430f",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Introduction to evals",
  "snippet": "",
  "published": "2026-11-03T22:23:43+00:00"
 },
 {
  "id": "bfe2db4d00f8",
  "region": "intl",
  "source": "Anthropic",
  "title": "- Anthropic",
  "snippet": "Anthropic",
  "published": "2026-11-03T23:23:21+00:00"
 }
]
