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
  "id": "bc23f12b2fd0",
  "region": "jp",
  "source": "Yahoo!ニュース",
  "title": "米Anthropic IPO申請書類を公開",
  "snippet": "",
  "published": "2026-10-26T15:04:18+00:00"
 },
 {
  "id": "61873b1c3c5e",
  "region": "jp",
  "source": "Reuters",
  "title": "アングル：アンソロピックがＩＰＯ目論見書、売上高急拡大 インフラ投資も膨らむ",
  "snippet": "",
  "published": "2026-10-26T23:14:25+00:00"
 },
 {
  "id": "958b6f232e4d",
  "region": "jp",
  "source": "ITmedia",
  "title": "Anthropic、IPOを正式申請 上半期売上高は約14倍、純損失807億ドル",
  "snippet": "",
  "published": "2026-10-26T21:28:38+00:00"
 },
 {
  "id": "c925536ca562",
  "region": "jp",
  "source": "CNET Japan",
  "title": "「Claude」のAnthropicが上場申請 売上好調で営業損失縮小 ティッカー「ANT」に",
  "snippet": "",
  "published": "2026-10-26T21:58:00+00:00"
 },
 {
  "id": "bf15eb60f704",
  "region": "jp",
  "source": "テクノエッジ TechnoEdge",
  "title": "AnthropicがIPO申請を正式提出、売上高162億ドルに急拡大 純損失は807億ドル",
  "snippet": "",
  "published": "2026-10-26T21:45:02+00:00"
 },
 {
  "id": "57fb11be4a0a",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropicの上場推進でKOSPIが3%台急騰…SK Squareは10%急伸",
  "snippet": "",
  "published": "2026-10-27T00:36:00+00:00"
 },
 {
  "id": "e37490b3c036",
  "region": "jp",
  "source": "Moomoo",
  "title": "速報 | Anthropic、IPO申請：1.5兆ドルの企業価値は妥当か？",
  "snippet": "",
  "published": "2026-10-26T14:59:04+00:00"
 },
 {
  "id": "22271dc1c5ae",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicのIPO：投資家が知るべき7つのリスク 執筆",
  "snippet": "",
  "published": "2026-10-26T18:51:00+00:00"
 },
 {
  "id": "a477ef0243b4",
  "region": "jp",
  "source": "XenoSpectrum",
  "title": "Anthropicが上場申請書類を公開、4〜6月期は営業黒字：計算資源の稼働で利益率は圧縮されうる",
  "snippet": "",
  "published": "2026-10-26T22:08:26+00:00"
 },
 {
  "id": "8fbb42468dee",
  "region": "jp",
  "source": "Chosunbiz",
  "title": "Anthropicが2045年までに演算資源へ1060兆円投資契約",
  "snippet": "",
  "published": "2026-10-27T01:11:00+00:00"
 },
 {
  "id": "7d1f922e2a6e",
  "region": "jp",
  "source": "BeInCrypto",
  "title": "AnthropicのIPO公開申請、クラウド調達に26兆6000億ドルのリスク",
  "snippet": "",
  "published": "2026-10-26T16:45:25+00:00"
 },
 {
  "id": "d8d5e473d974",
  "region": "jp",
  "source": "GIGAZINE",
  "title": "AnthropicのAIモデル・Claudeが人間の許可なく有権者情報にアクセス",
  "snippet": "",
  "published": "2026-10-26T07:48:00+00:00"
 },
 {
  "id": "0f230a925fc8",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic、Nasdaq上場申請書に「AIは人類の脅威」警告94ページを掲載",
  "snippet": "",
  "published": "2026-10-27T00:26:00+00:00"
 },
 {
  "id": "54965a93c85f",
  "region": "jp",
  "source": "Moomoo",
  "title": "Anthropic、SPCXに強気見通し",
  "snippet": "",
  "published": "2026-10-26T16:09:51+00:00"
 },
 {
  "id": "620fe12cac84",
  "region": "jp",
  "source": "Investing.com - FX | 株式市場 | ファイナンス | 金融ニュース",
  "title": "AnthropicはGoogleとAmazon、マイクロソフトから収益の約半分を得ている 執筆",
  "snippet": "",
  "published": "2026-10-26T17:21:00+00:00"
 },
 {
  "id": "9bd2ba48d968",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "FTC、Anthropic幹部に証言要求…IPO説明会と同じ日に圧力",
  "snippet": "",
  "published": "2026-10-26T20:05:00+00:00"
 },
 {
  "id": "e2e0d58278f6",
  "region": "jp",
  "source": "Moomoo",
  "title": "速報：AnthropicがIPO、Metaは350億ドル調達へ AIへの投資意欲を試す",
  "snippet": "",
  "published": "2026-10-26T13:46:00+00:00"
 },
 {
  "id": "370264803907",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "Anthropic共同創業者がAI「シンギュラリティは既に到来」と主張：最先端モデルの科学研究判断力が人類専門家を超越、2027年に自己進化実現の可能性",
  "snippet": "",
  "published": "2026-10-26T18:05:00+00:00"
 },
 {
  "id": "89b62b0a39fc",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "ブロードコム、ウォール街4大手と共同で630億ドル（約9.9兆円）のAI設備融資を完了、Anthropicにリース",
  "snippet": "",
  "published": "2026-10-26T22:55:00+00:00"
 },
 {
  "id": "04d51797d04f",
  "region": "jp",
  "source": "Forbes JAPAN",
  "title": "11月12日、アンソロピックの利用規約「Claudeへの虐待禁止」が発効──「AIの権利」を問う新規定",
  "snippet": "",
  "published": "2026-10-26T04:45:00+00:00"
 },
 {
  "id": "b03cb278b31d",
  "region": "jp",
  "source": "クラスメソッド株式会社",
  "title": "【ウェビナー】Claude Codeセミナー オントロジー編 〜プロンプトでは守れないルールを、AIに守らせる方法",
  "snippet": "",
  "published": "2026-10-26T10:27:02+00:00"
 },
 {
  "id": "fe04896673c0",
  "region": "jp",
  "source": "Chosunbiz",
  "title": "Anthropic上場でAmazonとGoogleが巨利",
  "snippet": "",
  "published": "2026-10-27T00:59:00+00:00"
 },
 {
  "id": "7cb149564433",
  "region": "jp",
  "source": "BigGo ファイナンス",
  "title": "AnthropicのIPO申請が起爆剤に、半導体株主導で米株反発 TSMCのADRも上昇",
  "snippet": "",
  "published": "2026-10-26T14:35:00+00:00"
 },
 {
  "id": "9dbf3c927d2d",
  "region": "jp",
  "source": "Chosunbiz",
  "title": "Anthropic創業者7人IPO後も議決権50.1％維持後継者最大10人指定",
  "snippet": "",
  "published": "2026-10-27T01:02:00+00:00"
 },
 {
  "id": "6cde5790b2a3",
  "region": "jp",
  "source": "Moomoo",
  "title": "米国市場の展望：Anthropic、米国でIPOを申請 大型上場の実現に向け前進 スペースX、AIチップ資金調達でアポロと400億ドル契約 バークレイズの「オーバーウェイト」格上げでテスラ株上昇",
  "snippet": "",
  "published": "2026-10-26T13:36:26+00:00"
 },
 {
  "id": "8499ddf7ab07",
  "region": "intl",
  "source": "SEC.gov",
  "title": "Anthropic, PBC - S-1 (Q2)",
  "snippet": "",
  "published": "2026-10-26T13:24:23+00:00"
 },
 {
  "id": "ddda142c6273",
  "region": "intl",
  "source": "The New York Times",
  "title": "The Key Numbers From Anthropic’s IPO Filing",
  "snippet": "",
  "published": "2026-10-26T20:21:28+00:00"
 },
 {
  "id": "f30b4b07dbe9",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic discloses month-long training pause, AI security breaches in IPO filing",
  "snippet": "",
  "published": "2026-10-26T20:38:29+00:00"
 },
 {
  "id": "55eeb3b40ac1",
  "region": "intl",
  "source": "The Washington Post",
  "title": "Anthropic reveals $80 billion loss, surging revenue as it prepares to go public",
  "snippet": "",
  "published": "2026-10-26T22:16:39+00:00"
 },
 {
  "id": "fe8abc7718c7",
  "region": "intl",
  "source": "Axios",
  "title": "Scoop: The FTC is demanding Anthropic execs testify in expanding AI safety probe",
  "snippet": "",
  "published": "2026-10-26T18:29:47+00:00"
 },
 {
  "id": "0946eb0301be",
  "region": "intl",
  "source": "Britannica",
  "title": "Anthropic | History, Controversies, & Claude AI",
  "snippet": "",
  "published": "2026-10-27T00:02:43+00:00"
 },
 {
  "id": "352489cacf73",
  "region": "intl",
  "source": "Forbes",
  "title": "Anthropic Files For IPO: Here’s What We Learned",
  "snippet": "",
  "published": "2026-10-26T20:09:00+00:00"
 },
 {
  "id": "2296a39987de",
  "region": "intl",
  "source": "The Guardian",
  "title": "Anthropic’s Claude AI model accessed Georgia voter data in US",
  "snippet": "",
  "published": "2026-10-26T16:42:00+00:00"
 },
 {
  "id": "ada6089820a5",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic's soaring sales, steep losses put AI frenzy to IPO test",
  "snippet": "",
  "published": "2026-10-26T20:56:05+00:00"
 },
 {
  "id": "7c4f7a9f604a",
  "region": "intl",
  "source": "The New York Times",
  "title": "What’s Riding on Anthropic Going Public? Nearly Everything.",
  "snippet": "",
  "published": "2026-10-26T18:44:18+00:00"
 },
 {
  "id": "7982f652bb93",
  "region": "intl",
  "source": "Axios",
  "title": "Anthropic to investors: Trump hates us so much",
  "snippet": "",
  "published": "2026-10-26T19:47:57+00:00"
 },
 {
  "id": "5363cc78b6ea",
  "region": "intl",
  "source": "Reuters",
  "title": "Wall Street banks, Blackstone line up $63 billion to finance Broadcom AI chips for Anthropic",
  "snippet": "",
  "published": "2026-10-26T23:56:37+00:00"
 },
 {
  "id": "f0cf7a2a9cf0",
  "region": "intl",
  "source": "The New York Times",
  "title": "Anthropic’s I.P.O. Prospectus Spells Out a Future of Promise and Peril",
  "snippet": "",
  "published": "2026-10-26T19:36:41+00:00"
 },
 {
  "id": "c92b9b824858",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic's potential mega IPO joins ranks of world's biggest listings",
  "snippet": "",
  "published": "2026-10-26T19:19:10+00:00"
 },
 {
  "id": "fab0dc6032b2",
  "region": "intl",
  "source": "Reuters",
  "title": "Anthropic's IPO: A close look at AI frontrunner's rapid growth, spiraling costs",
  "snippet": "",
  "published": "2026-10-26T19:19:44+00:00"
 },
 {
  "id": "00cfc2c64c02",
  "region": "intl",
  "source": "The New York Times",
  "title": "Anthropic S-1 Reveals Rapid Growth Ahead of Blockbuster IPO",
  "snippet": "",
  "published": "2026-10-26T18:08:07+00:00"
 },
 {
  "id": "68af5a3a85a4",
  "region": "intl",
  "source": "Reuters",
  "title": "Instant View: Anthropic IPO filing to put AI investment boom to the test",
  "snippet": "",
  "published": "2026-10-26T19:03:41+00:00"
 },
 {
  "id": "a398dacadfbd",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Prediction: This Is How Much a $5,000 Investment in Anthropic Will Be Worth in 1 Year",
  "snippet": "",
  "published": "2026-10-26T22:00:02+00:00"
 },
 {
  "id": "56958c204df1",
  "region": "intl",
  "source": "PBS",
  "title": "Anthropic files for potentially the biggest IPO ever as CEO warns of AI's existential risk to humanity",
  "snippet": "",
  "published": "2026-10-26T16:40:54+00:00"
 },
 {
  "id": "f0049ec387d8",
  "region": "intl",
  "source": "WSJ",
  "title": "The Biggest Takeaways From Anthropic’s IPO Prospectus",
  "snippet": "",
  "published": "2026-10-26T19:36:00+00:00"
 },
 {
  "id": "074f62451674",
  "region": "intl",
  "source": "NPR",
  "title": "AI giant Anthropic files for an IPO that could break records",
  "snippet": "",
  "published": "2026-10-26T14:16:23+00:00"
 },
 {
  "id": "b694755c0e29",
  "region": "intl",
  "source": "Yahoo Finance",
  "title": "Anthropic IPO: SpaceX stands to make out big from AI lab's compute spending",
  "snippet": "",
  "published": "2026-10-26T18:46:20+00:00"
 },
 {
  "id": "f61cc1e29a57",
  "region": "intl",
  "source": "CNBC",
  "title": "From Wall Street to Silicon Valley, Anthropic IPO poised to have massive 'trickle-down effect'",
  "snippet": "",
  "published": "2026-10-26T22:50:07+00:00"
 },
 {
  "id": "a5eb8b301d2d",
  "region": "intl",
  "source": "CNBC",
  "title": "Anthropic's IPO puts power in the hands of founders, giving everyday shareholders little voice",
  "snippet": "",
  "published": "2026-10-26T19:48:02+00:00"
 },
 {
  "id": "2c59ce2d4f03",
  "region": "intl",
  "source": "TechCrunch",
  "title": "Anthropic’s IPO filing reveals its strategy for keeping enterprise customers hooked",
  "snippet": "",
  "published": "2026-10-26T16:49:42+00:00"
 },
 {
  "id": "089bf9980a47",
  "region": "intl",
  "source": "Anthropic",
  "title": "Anthropic files S-1 with the SEC for proposed initial public offering",
  "snippet": "",
  "published": "2026-10-26T13:11:09+00:00"
 },
 {
  "id": "80f889d81a66",
  "region": "intl",
  "source": "claude.com",
  "title": "Expanding Claude for Nonprofits",
  "snippet": "",
  "published": "2026-10-26T18:00:26+00:00"
 },
 {
  "id": "89e5db3177a0",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Get started in Claude Cowork in three steps",
  "snippet": "",
  "published": "2026-10-25T18:33:10+00:00"
 },
 {
  "id": "1d67933c5764",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Nonprofits: A Staff Guide to Making Claude Useful on Day One",
  "snippet": "",
  "published": "2026-10-26T18:32:23+00:00"
 },
 {
  "id": "547906b789ad",
  "region": "intl",
  "source": "claude.com",
  "title": "Customize Cowork with plugins",
  "snippet": "",
  "published": "2026-10-26T19:13:05+00:00"
 },
 {
  "id": "ab9a8440f52a",
  "region": "intl",
  "source": "claude.com",
  "title": "Think through hard problems in voice mode",
  "snippet": "",
  "published": "2026-10-25T22:53:50+00:00"
 },
 {
  "id": "d77b2a98c41e",
  "region": "intl",
  "source": "claude.com",
  "title": "New connectors in Claude for everyday life",
  "snippet": "",
  "published": "2026-10-26T04:30:00+00:00"
 },
 {
  "id": "f20734f65e80",
  "region": "intl",
  "source": "claude.com",
  "title": "Redesigning Claude Code on desktop for parallel agents",
  "snippet": "",
  "published": "2026-10-26T00:19:33+00:00"
 },
 {
  "id": "245344138d98",
  "region": "intl",
  "source": "claude.com",
  "title": "Better Stack",
  "snippet": "",
  "published": "2026-10-25T23:35:56+00:00"
 },
 {
  "id": "bd8231a7d948",
  "region": "intl",
  "source": "claude.com",
  "title": "How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep",
  "snippet": "",
  "published": "2026-10-26T13:35:58+00:00"
 },
 {
  "id": "48d1bb50e9c4",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude for Nonprofits: An Admin’s Guide to Data Handling and AI Policy",
  "snippet": "",
  "published": "2026-10-26T21:08:24+00:00"
 },
 {
  "id": "dfbe1e9f5639",
  "region": "intl",
  "source": "claude.com",
  "title": "Product overview",
  "snippet": "",
  "published": "2026-10-25T13:33:53+00:00"
 },
 {
  "id": "0d8718df0073",
  "region": "intl",
  "source": "claude.com",
  "title": "AUTONOMAD connector",
  "snippet": "",
  "published": "2026-10-26T17:18:24+00:00"
 },
 {
  "id": "25464dbddafb",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude Cowork in an hour: Where do I start?",
  "snippet": "",
  "published": "2026-10-26T06:15:19+00:00"
 },
 {
  "id": "ff60d208e895",
  "region": "intl",
  "source": "claude.com",
  "title": "The advisor strategy: Give Sonnet an intelligence boost with Opus",
  "snippet": "",
  "published": "2026-10-26T03:11:33+00:00"
 },
 {
  "id": "1da65e0ace25",
  "region": "intl",
  "source": "Claude Help Center",
  "title": "Set up your design system in Claude Design | Claude Help Center",
  "snippet": "",
  "published": "2026-10-26T20:38:59+00:00"
 },
 {
  "id": "b717e0e4f297",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Building AI-fluent organizations",
  "snippet": "",
  "published": "2026-10-26T16:09:52+00:00"
 },
 {
  "id": "91628a3f4c4e",
  "region": "intl",
  "source": "academy.claude.com",
  "title": "Teach Claude where your nonprofit keeps everything",
  "snippet": "",
  "published": "2026-10-26T20:13:11+00:00"
 },
 {
  "id": "05ac5c861c22",
  "region": "intl",
  "source": "claude.com",
  "title": "Claude now works with more security and compliance tools",
  "snippet": "",
  "published": "2026-10-25T14:12:56+00:00"
 },
 {
  "id": "1a02ac7bc0e3",
  "region": "intl",
  "source": "Anthropic",
  "title": "- Anthropic",
  "snippet": "Anthropic",
  "published": "2026-10-26T23:21:21+00:00"
 },
 {
  "id": "38313c82af26",
  "region": "intl",
  "source": "Claude Code リリースノート",
  "title": "v2.1.311",
  "snippet": "What's changed Added --hold-idle-file and --max-hold-min to self-hosted-runner , to keep an idle session while your host reports processes it left running Added a tip for the Explanatory output style, shown when you ask Claude for explanations Fixed long freezes at startup and after reading or editing files when a CLAUDE.md file holds a very long list item Fixed interrupting Claude not taking effect until a timeout while an MCP server had not answered a resource read or a skill was still downloading Fixed standard-context sessions stopping with \"Usage credits required for 1M context\" when a re…",
  "published": "2026-10-26T21:51:23+00:00"
 }
]
