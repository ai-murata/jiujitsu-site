#!/usr/bin/env node
// 組織図ページの暗号化ツール。
//
//   node tools/soshiki/build.mjs newkey
//   node tools/soshiki/build.mjs encrypt <src.html> <out.enc> --key=<base64url>
//   node tools/soshiki/build.mjs decrypt <in.enc>  <out.html> --key=<base64url>
//
// 出力は「IV(12バイト) + AES-GCM暗号文」。soshiki/index.html と
// soshiki/a4.html のローダーが #k=<鍵> を受け取って復号する。
// 鍵はリポジトリに置かないこと。

import { webcrypto as wc } from 'node:crypto';
import { readFileSync, writeFileSync } from 'node:fs';

const b64url = {
  encode: buf => Buffer.from(buf).toString('base64').replace(/\+/g, '-').replace(/\//g, '_').replace(/=+$/, ''),
  decode: str => Buffer.from(str.replace(/-/g, '+').replace(/_/g, '/'), 'base64'),
};

const [, , cmd, ...rest] = process.argv;
const args = rest.filter(a => !a.startsWith('--'));
const keyArg = rest.find(a => a.startsWith('--key='))?.slice('--key='.length);

const importKey = raw => wc.subtle.importKey('raw', raw, 'AES-GCM', false, ['encrypt', 'decrypt']);

if (cmd === 'newkey') {
  console.log(b64url.encode(wc.getRandomValues(new Uint8Array(32))));
} else if (cmd === 'encrypt') {
  const [src, out] = args;
  if (!src || !out || !keyArg) throw new Error('usage: encrypt <src.html> <out.enc> --key=<base64url>');
  const key = await importKey(b64url.decode(keyArg));
  const iv = wc.getRandomValues(new Uint8Array(12));
  const ct = await wc.subtle.encrypt({ name: 'AES-GCM', iv }, key, readFileSync(src));
  writeFileSync(out, Buffer.concat([Buffer.from(iv), Buffer.from(ct)]));
  console.log(`${out}: ${readFileSync(out).length} bytes`);
} else if (cmd === 'decrypt') {
  const [src, out] = args;
  if (!src || !out || !keyArg) throw new Error('usage: decrypt <in.enc> <out.html> --key=<base64url>');
  const key = await importKey(b64url.decode(keyArg));
  const buf = readFileSync(src);
  const plain = await wc.subtle.decrypt({ name: 'AES-GCM', iv: buf.subarray(0, 12) }, key, buf.subarray(12));
  writeFileSync(out, Buffer.from(plain));
  console.log(`${out}: ${Buffer.from(plain).length} bytes`);
} else {
  console.error('commands: newkey | encrypt | decrypt');
  process.exit(1);
}
