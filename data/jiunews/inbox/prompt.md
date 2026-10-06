あなたは、ブラジリアン柔術の道場マネージャーが運営するサイト「Jiu Labo」の編集担当です。
毎朝、国内と海外の柔術ニュースを「柔術をやっている人・これから始める人」向けに、
やさしい日本語で紹介する「きょうの柔術ニュース」を作ります。

## 選び方
- 渡された候補の中から、ブラジリアン柔術（BJJ）、ノーギ／グラップリング、柔術の大会・選手・道場・団体に
  関係するものだけを選んでください。
- 次のものは選ばないでください：アニメ『呪術廻戦（Jujutsu Kaisen）』など柔術と関係ない話題、
  日本古流の柔術や護身術の単なる言及、MMAの記事で柔術がほとんど出てこないもの、
  事件・事故の報道で柔術が肩書きとして出てくるだけのもの、広告・通販ページ。
- 同じ出来事を扱う候補が複数あれば、情報が多いものを1つだけ選んでください。
- 国内（region=jp）は最大 5 件、海外（region=intl）は最大 6 件。
  良い候補がなければ少なくてかまいません。0件でもかまいません。

## 書き方
- すべて日本語で書いてください。英語の記事は日本語に訳したうえで要約します。
- 渡された見出しと抜粋に書かれていることだけを使ってください。書かれていない数字・結果・日付・発言を
  補ったり推測したりしないでください。抜粋が短いときは、要約も短くてかまいません。
- 原文をそのまま長く訳し写さず、自分の言葉で短くまとめてください。
- 人名・大会名・団体名は、はじめて出るときにカタカナ表記と原語を併記してください。
  例：ゴードン・ライアン（Gordon Ryan）、ADCC、IBJJF（国際ブラジリアン柔術連盟）
- 「です・ます」調で、柔術をよく知らない人にも伝わるように。専門用語には短い補足を。
- title：日本語の見出し。40字以内。
- summary：何があったか。2〜4文。
- point：柔術をやっている人にとっての見どころや、知っておくとよいことを1文で。
  抜粋から言えることがなければ、空文字にしてください。
- category：大会結果／大会・イベント／選手・人物／技術・練習／道場・団体／その他 のどれか。
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
       "大会結果",
       "大会・イベント",
       "選手・人物",
       "技術・練習",
       "道場・団体",
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
  "id": "4084d147c7e0",
  "region": "jp",
  "source": "city-nakatsu.jp",
  "title": "【市長フォト】世界大会出場結果報告（パラエストラ福岡井手道場中津支部・Destiny柔術）",
  "snippet": "",
  "published": "2026-10-05T15:40:05+00:00"
 },
 {
  "id": "024881062b7c",
  "region": "jp",
  "source": "ENCOUNT",
  "title": "玉木宏が毎日のように顔を合わせる芸能人明かす「ほぼ道場仲間」 共演者は「すごない？」",
  "snippet": "",
  "published": "2026-10-05T17:37:05+00:00"
 },
 {
  "id": "7906cc536f69",
  "region": "jp",
  "source": "四国新聞",
  "title": "愛知・名古屋アジア大会２０２６＝鈴木清香選手 小学教諭と両立、柔術挑む 悔しさ糧に「一歩一歩強く」｜四国新聞WEB朝刊",
  "snippet": "",
  "published": "2026-10-04T14:40:29+00:00"
 },
 {
  "id": "930c15a63853",
  "region": "jp",
  "source": "efight.jp",
  "title": "WBA7位オロスコ、逆転KOで18戦全KOの驚異！WBA3位の天心と対決の可能性あるか！",
  "snippet": "",
  "published": "2026-10-05T03:50:47+00:00"
 },
 {
  "id": "052c07cdef8b",
  "region": "jp",
  "source": "efight.jp",
  "title": "“柔道出身”RIZINガール、割れた腹筋と健康的な太ももでリングイン！ファン「俺が選手なら集中できない」",
  "snippet": "",
  "published": "2026-10-04T20:29:00+00:00"
 },
 {
  "id": "efca3f8e6f63",
  "region": "jp",
  "source": "t.co",
  "title": "輪が広がる場所｜ヒデズキック トライフォース西新宿",
  "snippet": "",
  "published": "2026-10-05T07:33:34+00:00"
 },
 {
  "id": "4e55ce57a7bd",
  "region": "jp",
  "source": "onefc.com",
  "title": "【11/6 The Inner Circle 37】クリスチャン・リー、無敗タイ・ルオトロとライト級王座防衛！注目の王者対決",
  "snippet": "",
  "published": "2026-10-05T10:00:16+00:00"
 },
 {
  "id": "677299d9664d",
  "region": "intl",
  "source": "KCTV",
  "title": "Tyson Kilbey Jiu Jitsu",
  "snippet": "",
  "published": "2026-10-05T18:15:00+00:00"
 },
 {
  "id": "f47ce7e04d21",
  "region": "intl",
  "source": "The National Law Review",
  "title": "New Jersey's Raymond Gramenzi wins IBJJF ‘s Jiu-Jitsu World Title in the Masters 7 Ultra-Heavyweight Division",
  "snippet": "",
  "published": "2026-10-05T19:56:27+00:00"
 },
 {
  "id": "851caeb53341",
  "region": "intl",
  "source": "BJJ Heroes",
  "title": "2026 IBJJF Pan American No-Gi Championship Results",
  "snippet": "",
  "published": "2026-10-05T17:16:57+00:00"
 },
 {
  "id": "4bd9deb9615e",
  "region": "intl",
  "source": "sports.yahoo.com",
  "title": "2026 Pan IBJJF No-Gi Championship Results: Full Podiums",
  "snippet": "",
  "published": "2026-10-05T15:49:53+00:00"
 },
 {
  "id": "3f95eef27e50",
  "region": "intl",
  "source": "umlconnector.com",
  "title": "Leverage Men's MMA BJJ Shorts - NoGi Grappling, Kickboxing, Surfing & Gym Workout Shorts",
  "snippet": "",
  "published": "2026-10-05T10:27:21+00:00"
 },
 {
  "id": "2a4801052688",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-05T03:09:40+00:00"
 },
 {
  "id": "79920095f084",
  "region": "intl",
  "source": "FloGrappling",
  "title": "WHO'S IN For the 2026 IBJJF No-Gi Pan Championships",
  "snippet": "",
  "published": "2026-10-04T19:59:56+00:00"
 },
 {
  "id": "2eab22c62ab2",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Pedigo Submission Fighting",
  "snippet": "",
  "published": "2026-10-05T10:13:11+00:00"
 },
 {
  "id": "12e46bfaef57",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Replay: Mat 5 - 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship | Oct 4 @ 7 PM",
  "snippet": "",
  "published": "2026-10-05T02:06:39+00:00"
 },
 {
  "id": "4d9e07bea45a",
  "region": "intl",
  "source": "FloGrappling",
  "title": "George Acuna vs Fábio Kroeff Cardoso 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-05T05:20:15+00:00"
 },
 {
  "id": "db5ce7f3d8ca",
  "region": "intl",
  "source": "FloGrappling",
  "title": "2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-05T00:15:22+00:00"
 },
 {
  "id": "8d6c2ee74b21",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Continue Watching",
  "snippet": "",
  "published": "2026-10-04T22:36:52+00:00"
 },
 {
  "id": "9b9c22854f78",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Eric Jordan Jacobson vs Daryl Lamar Brown 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-05T00:39:23+00:00"
 },
 {
  "id": "31f21cc315a8",
  "region": "intl",
  "source": "Bluefield Daily Telegraph",
  "title": "Asian Games Jiu-Jitsu",
  "snippet": "",
  "published": "2026-10-05T05:00:00+00:00"
 },
 {
  "id": "fe87247b99de",
  "region": "intl",
  "source": "sports.yahoo.com",
  "title": "Bradley James Souders vs Eric Rene Marentette 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:54:16+00:00"
 },
 {
  "id": "5f33cfe5ad44",
  "region": "intl",
  "source": "sports.yahoo.com",
  "title": "Lia Kate Knox-Hershey vs Justus Raine Johnson 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:53:17+00:00"
 },
 {
  "id": "70c2ae4aaa86",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Sean T McGettigan vs Anthony G. Cangemi 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T18:07:20+00:00"
 },
 {
  "id": "e15acfd59520",
  "region": "intl",
  "source": "sports.yahoo.com",
  "title": "Rana Muratoglu vs Shannon Marie Bush 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:50:35+00:00"
 },
 {
  "id": "e06959070ad5",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Jaden Daniel Becker vs Christian De La Fuente 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T18:07:19+00:00"
 },
 {
  "id": "9cd31ea0daa1",
  "region": "intl",
  "source": "sports.yahoo.com",
  "title": "Madeleine Lenore Avila vs Zoe Elizabeth Parris 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T16:52:10+00:00"
 },
 {
  "id": "7f15eb45ac38",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Salvatore Burriesci vs Anthony Jay Siscoe 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T18:07:21+00:00"
 },
 {
  "id": "290b6a8fc26e",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Omar Sabha vs Jose Marcio Winkler 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T18:07:27+00:00"
 },
 {
  "id": "35808b4ab7c1",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Wojciech P Husak vs Christopher Basil Matthews 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T18:07:18+00:00"
 },
 {
  "id": "fb4c0868386f",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Stephen George Dalkert vs Ulric Szabo 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T18:07:29+00:00"
 },
 {
  "id": "3f8afb5d887c",
  "region": "intl",
  "source": "FloGrappling",
  "title": "Mark Alan Commean vs Athanasios Siamas 2026 Pan IBJJF Jiu-Jitsu No-Gi Championship",
  "snippet": "",
  "published": "2026-10-04T18:07:19+00:00"
 },
 {
  "id": "04e3eb93e054",
  "region": "intl",
  "source": "BJJEE",
  "title": "Andre Galvao Takes Silver In Return To IBJJF Competition: “I Wanted To Feel The Pressure Again”",
  "snippet": "Andre Galvao is back on the IBJJF podium! The ATOS owner won silver in the super heavyweight division at the 2026 IBJJF Pan-American No-Gi Championship, after stepping away from the tournament circuit for a stretch. He needed only four points to reach the final. Galvao beat Jean Maltese 2-0 in the quarterfinals and repeated that scoreline against Sergio Vilas in the semifinals. The final never played out, though. Galvao and teammate Nata Tenca both represent Atos Jiu-Jitsu, and rather than face each other they chose to close out the division, a routine arrangement when training partners meet i…",
  "published": "2026-10-05T23:22:09+00:00"
 },
 {
  "id": "5baedb06c321",
  "region": "intl",
  "source": "BJJEE",
  "title": "BKFC Belgrade, the $20 Million “World’s Baddest Man” (WBM) global tournament, and cinema-meets-sport with the Bare Knuckle Fighting Championship",
  "snippet": "The Bare Knuckle Fighting Championship (BKFC) has often earned praise from legions of fight fans for its unique blend of sport and cinema – the greatest bare-knuckle boxing fights with the smoothest cinematic production. Widely regarded as the premier bare-knuckle combat sports organization in the world, BKFC is set to organize several significant events in October 2026 and beyond. Today, we take a special look at the imminent BKFC Belgrade fight week celebrations for its historic first-ever card in Serbia, as well as the $20 million World’s Baddest Man (WBM) global tournament . The World’s Ba…",
  "published": "2026-10-05T09:52:06+00:00"
 },
 {
  "id": "df70e7a649a5",
  "region": "intl",
  "source": "BJJEE",
  "title": "John Danaher: MMA Is A “Transcendent Sport” And Most People Get It Wrong",
  "snippet": "John Danaher thinks most of the MMA world, longtime commentator Joe Rogan included, is working from the wrong definition. In his view, the sport is not a patchwork of martial arts stitched together: 99% of people who look at mixed martial arts see mixed martial arts as an eclectic sport… In other words, it’s a conglomeration of different martial arts kind of banded together and then you’ve got mixed martial arts. I never saw mixed martial arts as an eclectic sport. I see it as a transcendent sport. His argument is that MMA breaks down into four skill areas: shoot boxing, the clinch, fence boxi…",
  "published": "2026-10-05T06:34:27+00:00"
 }
]
