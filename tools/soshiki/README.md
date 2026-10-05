# 組織図ページの暗号化

`/soshiki/` は鍵付きリンクでしか開けないようにしてあります。`/staff/` と同じ方式です。

- `soshiki/index.html` … 詳細版のローダー（`data.enc` を復号）
- `soshiki/a4.html` … A4・1枚版のローダー（`a4.enc` を復号）
- 中身は AES-GCM（256bit）で暗号化。ファイルの先頭12バイトがIV。
- 鍵は URL のフラグメント `#k=<鍵>` で渡します。フラグメントはサーバーに送信されません。
- **鍵はこのリポジトリに置かないこと。** 共有した相手だけが開けます。

## 中身を直すとき

```sh
# 1. 復号して元のHTMLを取り出す
node tools/soshiki/build.mjs decrypt soshiki/data.enc /tmp/index.html --key=<鍵>
node tools/soshiki/build.mjs decrypt soshiki/a4.enc   /tmp/a4.html   --key=<鍵>

# 2. /tmp/index.html, /tmp/a4.html を編集する
#    （詳細版からA4版へのリンクには #k=<鍵> を付けたままにしておくこと）

# 3. 暗号化して戻す
node tools/soshiki/build.mjs encrypt /tmp/index.html soshiki/data.enc --key=<鍵>
node tools/soshiki/build.mjs encrypt /tmp/a4.html   soshiki/a4.enc   --key=<鍵>
```

平文のHTMLをリポジトリに置いたままコミットしないこと。履歴に残ると、
リポジトリが公開なので誰でも読めてしまいます。

鍵を変えるときは `node tools/soshiki/build.mjs newkey` で作り直し、
両方のファイルを新しい鍵で暗号化し直してください。
