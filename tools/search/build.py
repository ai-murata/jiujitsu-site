#!/usr/bin/env python3
"""サイト内の HTML を読んで、検索用の索引 search/index.json を作る。

  python3 tools/search/build.py          # search/index.json を作り直す
  python3 tools/search/build.py --check  # 作り直しが必要かどうかだけ見る（必要なら終了コード 1）

ネットワークは使わない。載せないページ：
  - <meta name="robots" content="noindex"> があるページ（スタッフ用・非公開のページ）
  - <meta http-equiv="refresh"> で別のページへ飛ばすだけのページ
  - 名前が _ で始まるファイル・フォルダ、search/ 自身
"""
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "search" / "index.json"
MAX_TEXT = 12000  # 1ページあたりの本文の上限（文字数）。索引を軽く保つため

SKIP_TAGS = {"script", "style", "noscript", "template", "svg", "head", "nav", "footer", "button", "select", "rt"}
BLOCK_TAGS = {
    "p", "div", "section", "article", "main", "header", "li", "ul", "ol", "dl", "dt", "dd",
    "h1", "h2", "h3", "h4", "h5", "h6", "tr", "td", "th", "table", "br", "blockquote", "figcaption",
}
VOID_TAGS = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.description = ""
        self.noindex = False
        self.redirect = False
        self.headings = []
        self._skip = []  # 読み飛ばし中のタグの積み上げ
        self._in_title = False
        self._heading = None
        self._parts = []

    def handle_starttag(self, tag, attrs):
        a = {k: (v or "") for k, v in attrs}
        if tag == "meta":
            name = a.get("name", "").lower()
            if name == "robots" and "noindex" in a.get("content", "").lower():
                self.noindex = True
            elif name == "description":
                self.description = a.get("content", "").strip()
            elif a.get("http-equiv", "").lower() == "refresh":
                self.redirect = True
            return
        if tag == "title":
            self._in_title = True
            return
        if tag in VOID_TAGS:
            if tag == "br":
                self._parts.append("\n")
            return
        if self._skip or tag in SKIP_TAGS or "hidden" in a or a.get("aria-hidden") == "true":
            self._skip.append(tag)
            return
        if tag in BLOCK_TAGS:
            self._parts.append("\n")
        if tag in ("h1", "h2", "h3"):
            self._heading = []

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title = False
            return
        if self._skip:
            # 閉じ忘れがあっても崩れないよう、同じタグまで巻き戻す
            if tag in self._skip:
                while self._skip and self._skip.pop() != tag:
                    pass
            return
        if tag in ("h1", "h2", "h3") and self._heading is not None:
            h = squash("".join(self._heading))
            if h:
                self.headings.append(h)
            self._heading = None
        if tag in BLOCK_TAGS:
            self._parts.append("\n")

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if self._skip:
            return
        self._parts.append(data)
        if self._heading is not None:
            self._heading.append(data)

    def text(self):
        lines = (squash(line) for line in "".join(self._parts).split("\n"))
        return " ".join(line for line in lines if line)


def squash(s):
    return re.sub(r"\s+", " ", s).strip()


def page_url(path):
    rel = path.relative_to(ROOT).as_posix()
    if rel == "index.html":
        return "/"
    if rel.endswith("/index.html"):
        return "/" + rel[: -len("index.html")]
    return "/" + rel


def candidates():
    for path in sorted(ROOT.rglob("*.html")):
        parts = path.relative_to(ROOT).parts
        if any(p.startswith((".", "_")) for p in parts):
            continue
        if parts[0] in ("search", "tools", "node_modules"):
            continue
        yield path


def parse(source):
    p = PageParser()
    p.feed(source)
    p.close()
    return p


def js_data(source):
    """ページに埋め込まれた `const DATA = [...]` を読む（道場ガイド・補助金のように JS で描くページ用）。"""
    m = re.search(r"^const DATA\s*=\s*(\[.*\]);\s*$", source, re.M)
    return json.loads(m.group(1)) if m else []


def join(*parts):
    return " · ".join(squash(str(p)) for p in parts if p)


def items_dojo(source):
    # 1道場を1件として出す。q はページ側の検索窓に入れる言葉（/dojo/?q=…）
    return [
        {"t": d["name"], "s": join(d.get("pref"), d.get("addr"), d.get("instructor") and f"指導 {d['instructor']}",
                                   d.get("name_en") if d.get("name_en") != d["name"] else ""),
         "q": d["name"]}
        for d in js_data(source) if d.get("name")
    ]


def items_hojokin(source):
    return [
        {"t": d["title"], "s": join(d.get("alias"), d.get("catch"), "・".join(d.get("prefs") or [])[:60]),
         "q": d["title"]}
        for d in js_data(source) if d.get("title")
    ]


# JS で中身を描くページは、埋め込みデータから1件ずつ拾う
ITEM_EXTRACTORS = {"/dojo/": items_dojo, "/hojokin/": items_hojokin}


def build_index():
    pages = []
    for path in candidates():
        source = path.read_text(encoding="utf-8", errors="replace")
        p = parse(source)
        if p.noindex or p.redirect:
            continue
        url = page_url(path)
        text = p.text()
        if len(text) > MAX_TEXT:
            text = text[:MAX_TEXT]
        page = {
            "url": url,
            "title": squash(p.title) or url,
            "description": p.description,
            "headings": p.headings[:40],
            "text": text,
        }
        if url in ITEM_EXTRACTORS:
            page["items"] = ITEM_EXTRACTORS[url](source)
        pages.append(page)
    pages.sort(key=lambda e: e["url"])
    return {"pages": pages}


def dump(index):
    return json.dumps(index, ensure_ascii=False, separators=(",", ":")) + "\n"


def main(argv):
    body = dump(build_index())
    current = OUT.read_text(encoding="utf-8") if OUT.exists() else ""
    if "--check" in argv:
        if body != current:
            print("search/index.json が古くなっています。python3 tools/search/build.py を実行してください。")
            return 1
        print("search/index.json は最新です")
        return 0
    if body == current:
        print("search/index.json：変更なし")
        return 0
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(body, encoding="utf-8")
    n = len(json.loads(body)["pages"])
    print(f"search/index.json を作り直しました（{n} ページ, {len(body.encode()) // 1024} KB）")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
