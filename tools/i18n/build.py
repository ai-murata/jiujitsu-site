#!/usr/bin/env python3
"""日本語のページから英語・韓国語・ポルトガル語のページを作る。

  python3 tools/i18n/build.py todo <作業フォルダ>    # まだ訳がない文を <作業フォルダ>/todo/<言語>/ に書き出す
  python3 tools/i18n/build.py absorb <作業フォルダ>  # <作業フォルダ>/done/<言語>/ の訳を data/i18n/<言語>.json に取り込む
  python3 tools/i18n/build.py build                  # /en/ /ko/ /pt/ のページを作り、日本語ページに言語の目印を入れる
  python3 tools/i18n/build.py check                  # 訳もれ・タグのくい違い・日本語の残りを一覧にする（問題があれば終了コード 1）

ページの見た目は日本語版をそのまま使い、文章だけを差し替える。訳は「日本語の文 → 訳文」の
対応表（data/i18n/<言語>.json）で持つので、日本語を直したページは build すれば自動で作り直され、
直した文だけが訳もれとして check に出る。ネットワークは使わない。
"""
import json
import posixpath
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TM_DIR = ROOT / "data" / "i18n"
SITE = "https://jiujitsu.co.jp"
LANGS = {"en": "en", "ko": "ko", "pt": "pt-BR"}  # フォルダ名 → html の lang

MAIN_PAGES = [
    "index.html", "company/index.html", "hajimete/index.html", "kenkyu/index.html",
    "goroku/index.html", "toriatsukai/index.html", "data/index.html", "claudecode/index.html",
    "tournament/index.html", "irai/index.html", "claude-nyumon/index.html",
]
# 訳さないが、訳したトップから日本語版のまま案内するページ
KEEP_LINKS = {"/dojo/", "/textbook/"}

JA = re.compile(r"[぀-ヿ㐀-鿿ｦ-ﾟ、。「」『』【】・〜]")
JA_STRICT = re.compile(r"[぀-ヿ㐀-鿿]")

VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
RAW = {"script", "style"}
INLINE = {
    "a", "abbr", "b", "bdi", "bdo", "br", "cite", "code", "data", "del", "dfn", "em", "i", "img", "ins",
    "kbd", "mark", "q", "rp", "rt", "ruby", "s", "samp", "small", "span", "strong", "sub", "sup", "time",
    "u", "var", "wbr",
}
OPAQUE = {"svg", "textarea", "select", "noscript", "template"}  # 中身に立ち入らない
IMPLIED_CLOSE = {"p": {"p"}, "li": {"li"}, "dt": {"dt", "dd"}, "dd": {"dt", "dd"}, "tr": {"tr", "td", "th"},
                 "td": {"td", "th"}, "th": {"td", "th"}}
TEXT_ATTRS = ("alt", "title", "aria-label", "placeholder")
META_NAMES = {"description", "og:title", "og:description", "twitter:title", "twitter:description"}

TOKEN = re.compile(r"<!--.*?-->|<!doctype[^>]*>|</?[a-zA-Z][a-zA-Z0-9-]*(?:\"[^\"]*\"|'[^']*'|[^'\">])*>", re.S | re.I)
ATTR = re.compile(r"""([a-zA-Z_:][-a-zA-Z0-9_:.]*)(\s*=\s*)("[^"]*"|'[^']*')""")
JS_TOKEN = re.compile(
    r"""//[^\n]*|/\*.*?\*/|"(?:\\.|[^"\\\n])*"|'(?:\\.|[^'\\\n])*'|`(?:\\.|[^`\\])*`""", re.S)


class Node:
    def __init__(self, tag, start, end_open):
        self.tag, self.start, self.end_open = tag, start, end_open
        self.end = None
        self.children = []


def parse(src):
    """ページを木の形に読む。元の文字位置を覚えておき、差し替えは位置で行う。"""
    root = Node("#root", 0, 0)
    stack = [root]
    pos = 0
    while True:
        m = TOKEN.search(src, pos)
        text_end = m.start() if m else len(src)
        if text_end > pos:
            n = Node("#text", pos, text_end)
            n.end = text_end
            stack[-1].children.append(n)
        if not m:
            break
        pos = m.end()
        raw = m.group(0)
        if raw.startswith("<!"):
            n = Node("#comment", m.start(), pos)
            n.end = pos
            stack[-1].children.append(n)
            continue
        name = re.match(r"</?([a-zA-Z][a-zA-Z0-9-]*)", raw).group(1).lower()
        if raw.startswith("</"):
            if any(s.tag == name for s in stack[1:]):
                while True:
                    s = stack.pop()
                    s.end = pos if s.tag == name else m.start()
                    if s.tag == name:
                        break
            continue
        closes = IMPLIED_CLOSE.get(name)
        if closes:
            while len(stack) > 1 and stack[-1].tag in closes:
                stack.pop().end = m.start()
        n = Node(name, m.start(), pos)
        stack[-1].children.append(n)
        if name in VOID or raw.endswith("/>"):
            n.end = pos
        elif name in RAW or name in OPAQUE:
            close = re.compile(r"</%s\s*>" % name, re.I).search(src, pos)
            pos = close.end() if close else len(src)
            n.end = pos
        else:
            stack.append(n)
    while len(stack) > 1:
        stack.pop().end = len(src)
    root.end = len(src)
    return root


def has_block(node):
    return any(c.tag not in ("#text", "#comment") and (c.tag not in INLINE or has_block(c)) for c in node.children)


def attr_edits(src, node, out):
    raw = src[node.start:node.end_open]
    attrs = {a.group(1).lower(): a for a in ATTR.finditer(raw)}
    targets = [attrs[k] for k in TEXT_ATTRS if k in attrs]
    if node.tag == "meta" and "content" in attrs:
        key = attrs.get("name") or attrs.get("property")
        if key and key.group(3)[1:-1].lower() in META_NAMES:
            targets.append(attrs["content"])
    for a in targets:
        value = a.group(3)[1:-1]
        if JA.search(value):
            s = node.start + a.start(3) + 1
            out.append((s, s + len(value), value, "attr"))


def script_edits(src, node, out):
    body_start, body_end = node.end_open, src.rfind("</", node.end_open, node.end)
    if "src=" in src[node.start:node.end_open]:
        return
    for m in JS_TOKEN.finditer(src, body_start, body_end):
        tok = m.group(0)
        if tok[0] in "\"'`" and JA.search(tok):
            out.append((m.start() + 1, m.end() - 1, tok[1:-1], tok[0]))


def segments(src):
    """訳す文の一覧を (始まり, 終わり, 元の文) で返す。文の中のリンクや太字はタグごと1文として扱う。"""
    out = []

    def flush(run):
        if not run:
            return
        s, e = run[0].start, run[-1].end
        while s < e and src[s].isspace():
            s += 1
        while e > s and src[e - 1].isspace():
            e -= 1
        text = src[s:e]
        if JA.search(re.sub(r"<[^>]*>", "", text)):
            out.append((s, e, text, "html"))
        else:
            for n in run:
                walk_attrs(n)

    def walk_attrs(n):
        if n.tag.startswith("#"):
            return
        attr_edits(src, n, out)
        for c in n.children:
            walk_attrs(c)

    def walk(node):
        run = []
        for c in node.children:
            if c.tag == "#comment":
                if run:
                    flush(run)
                    run = []
            elif c.tag == "#text" or (c.tag in INLINE and not has_block(c)):
                run.append(c)
            else:
                flush(run)
                run = []
                if c.tag == "script":
                    script_edits(src, c, out)
                elif c.tag not in RAW and c.tag not in OPAQUE:
                    attr_edits(src, c, out)
                    walk(c)
                elif c.tag == "style":
                    pass
        flush(run)

    walk(parse(src))
    return sorted(out)


def blog_pages():
    pages = []
    for p in sorted((ROOT / "blog").glob("**/index.html")):
        rel = p.relative_to(ROOT).as_posix()
        if rel != "blog/nikki/index.html" and rel not in pages:
            pages.append(rel)
    return pages


def all_pages():
    return MAIN_PAGES + [p for p in blog_pages() if not is_blog_excluded(p)]


def is_blog_excluded(rel):
    return "noindex" in (ROOT / rel).read_text(encoding="utf-8")[:4000]


def route(rel):
    return "/" + rel[: -len("index.html")]


def routes():
    return {route(p) for p in all_pages()}


def cut(src, start_pat, end_pat):
    m = re.search(start_pat, src, re.S)
    if not m:
        return src
    e = re.compile(end_pat, re.S).search(src, m.end())
    return src[: m.start()] + src[e.end():] if e else src


def prune_home(src, known):
    """トップから、毎朝変わる欄と外国語版のないページへの案内を外す。"""
    src = cut(src, r"<!-- news:start -->", r"<!-- news:end -->")
    src = cut(src, r'<section class="dailynews"', r"</section>")
    src = cut(src, r'<form class="hsearch', r"</form>")

    def card(m):
        href = re.search(r'href="([^"#?]*)', m.group(0)).group(1)
        if not href.startswith("/") or href in known or href in KEEP_LINKS:
            return m.group(0)
        return ""

    src = re.sub(r'[ \t]*<a class="card[^>]*>.*?</a>\n?', card, src, flags=re.S)
    # カードがなくなった分類は、見出しとメニューも外す
    labels = list(re.finditer(r'[ \t]*<p class="cat-label" id="(cat-[a-z]+)">.*?</p>\n', src))
    for i, m in reversed(list(enumerate(labels))):
        tail = src[m.end(): labels[i + 1].start() if i + 1 < len(labels) else len(src)]
        if 'class="card' not in tail.split('<section', 1)[0]:
            src = src[: m.start()] + src[m.end():]
            src = re.sub(r'[ \t]*<a href="#%s">.*?</a>\n' % m.group(1), "", src)
    src = re.sub(r'[ \t]*<a href="#cat-news">.*?</a>\n', "", src)
    n = [0]

    def renumber(m):
        n[0] += 1
        return "%s%02d ・%s" % (m.group(1), n[0], m.group(2))

    return re.sub(r'(<p class="eyebrow">)\d+ ・( [A-Z])', renumber, src)


def prune_blog_list(src, known):
    def item(m):
        href = re.search(r'href="([^"#?]*)', m.group(0))
        return m.group(0) if not href or href.group(1) in known else ""

    return re.sub(r'[ \t]*<li(?: class="[^"]*")?>.*?</li>\n?', item, src, flags=re.S)


def source(rel, known):
    src = (ROOT / rel).read_text(encoding="utf-8")
    src = re.sub(r"<!-- i18n:start -->.*?<!-- i18n:end -->\n?", "", src, flags=re.S)
    if rel == "index.html":
        return prune_home(src, known)
    if rel == "blog/index.html":
        return prune_blog_list(src, known)
    return src


def fix_url(url, base_dir, lang, known):
    """リンク先を、言語版があれば言語版へ、相対パスは日本語版のファイルを指す絶対パスへ直す。"""
    if not url or url.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return url
    full = url.startswith(SITE + "/") or url == SITE
    if full:
        url = url[len(SITE):] or "/"
    elif re.match(r"[a-z]+:|//", url):
        return url
    m = re.match(r"([^?#]*)(.*)", url, re.S)
    path, rest = m.group(1), m.group(2)
    if not path.startswith("/"):
        keep_slash = path.endswith("/") or path == ""
        path = posixpath.normpath(posixpath.join(base_dir, path))
        if keep_slash and not path.endswith("/"):
            path += "/"
    if path.endswith("/index.html"):
        path = path[: -len("index.html")]
    if path in known:
        path = "/" + lang + path
    if path == "/textbook/" and rest == "":
        rest = "?lang=" + lang
    return (SITE if full else "") + path + rest


def rewrite_links(html, rel, lang, known):
    base_dir = "/" + posixpath.dirname(rel)

    def tag(m):
        raw = m.group(0)
        if raw.startswith(("</", "<!")):
            return raw
        is_og = re.search(r'property="og:(url|image)"', raw)

        def attr(a):
            name = a.group(1).lower()
            if name in ("href", "src", "action", "poster") or (name == "content" and is_og):
                q = a.group(3)[0]
                return a.group(1) + a.group(2) + q + fix_url(a.group(3)[1:-1], base_dir, lang, known) + q
            return a.group(0)

        return ATTR.sub(attr, raw)

    # プログラムの中の文字列は触らない
    parts = re.split(r"(<script\b.*?</script>)", html, flags=re.S | re.I)
    return "".join(p if i % 2 else TOKEN.sub(tag, p) for i, p in enumerate(parts))


def add_locale_css(html):
    """長い単語がはみ出さないように、外国語版にだけ足す調整。"""
    css = ("<style id=\"i18n-fix\">body{overflow-wrap:break-word}"
           "html:lang(ko) body{word-break:keep-all}"
           "@media (max-width:640px){table{max-width:100%}td,th{overflow-wrap:anywhere;min-width:0}}</style>\n")
    return html.replace("</head>", css + "</head>", 1) if "</head>" in html else html.replace("<title>", css + "<title>", 1)


def head_block(rel, current):
    path = route(rel)
    links = ['<link rel="alternate" hreflang="ja" href="%s%s">' % (SITE, path)]
    for folder, code in LANGS.items():
        links.append('<link rel="alternate" hreflang="%s" href="%s/%s%s">' % (code, SITE, folder, path))
    links.append('<link rel="alternate" hreflang="x-default" href="%s%s">' % (SITE, path))
    url = SITE + path if current == "ja" else "%s/%s%s" % (SITE, current, path)
    links.append('<link rel="canonical" href="%s">' % url)
    links.append('<script src="/assets/langs.js" defer></script>')
    return "<!-- i18n:start -->\n" + "\n".join(links) + "\n<!-- i18n:end -->\n"


def put_head(html, block):
    html = re.sub(r"<!-- i18n:start -->.*?<!-- i18n:end -->\n?", "", html, flags=re.S)
    html = re.sub(r'<link rel="canonical"[^>]*>\n?', "", html)
    return html.replace("<title>", block + "<title>", 1)


def load_tm(lang):
    p = TM_DIR / (lang + ".json")
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def save_tm(lang, tm):
    TM_DIR.mkdir(parents=True, exist_ok=True)
    text = json.dumps(dict(sorted(tm.items())), ensure_ascii=False, indent=0)
    (TM_DIR / (lang + ".json")).write_text(text + "\n", encoding="utf-8")


def slug(rel):
    return route(rel).strip("/").replace("/", "__") or "home"


def cmd_todo(work):
    known = routes()
    for lang in LANGS:
        tm = load_tm(lang)
        seen = set()
        out_dir = work / "todo" / lang
        out_dir.mkdir(parents=True, exist_ok=True)
        total = 0
        for rel in all_pages():
            items = []
            for _, _, text, _ in segments(source(rel, known)):
                if text not in tm and text not in seen:
                    seen.add(text)
                    items.append(text)
            if items:
                data = {str(i): t for i, t in enumerate(items, 1)}
                (out_dir / (slug(rel) + ".json")).write_text(
                    json.dumps(data, ensure_ascii=False, indent=0), encoding="utf-8")
                total += len(items)
        print(lang, "未訳", total, "文")


def cmd_absorb(work):
    for lang in LANGS:
        tm = load_tm(lang)
        added = 0
        for done in sorted((work / "done" / lang).glob("*.json")):
            todo = json.loads((work / "todo" / lang / done.name).read_text(encoding="utf-8"))
            trans = json.loads(done.read_text(encoding="utf-8"))
            for k, ja in todo.items():
                if str(trans.get(k, "")).strip():
                    tm[ja] = trans[k]
                    added += 1
                else:
                    print("訳なし", lang, done.name, k)
        save_tm(lang, tm)
        print(lang, "取り込み", added, "文 / 計", len(tm))


def escape(text, kind):
    if kind == "attr":
        return text.replace('"', "&quot;")
    if kind in ("'", '"', "`"):  # プログラムの中の文字列
        return re.sub(r"(?<!\\)" + kind, "\\" + kind, text)
    return text


def translate(src, tm, missing):
    parts, pos = [], 0
    for s, e, text, kind in segments(src):
        if s < pos:
            continue
        parts.append(src[pos:s])
        if text in tm:
            parts.append(escape(tm[text], kind))
        else:
            missing.append(text)
            parts.append(text)
        pos = e
    parts.append(src[pos:])
    return "".join(parts)


def cmd_build():
    known = routes()
    pages = all_pages()
    report = 0
    for lang, code in LANGS.items():
        tm = load_tm(lang)
        missing = []
        for rel in pages:
            html = translate(source(rel, known), tm, missing)
            html = rewrite_links(html, rel, lang, known)
            html = html.replace("get('/blog/')", "get('/%s/blog/')" % lang)
            html = re.sub(r'<html lang="ja"', '<html lang="%s"' % code, html, count=1)
            html = put_head(add_locale_css(html), head_block(rel, lang))
            out = ROOT / lang / rel
            out.parent.mkdir(parents=True, exist_ok=True)
            out.write_text(html, encoding="utf-8")
        report += len(missing)
        print(lang, len(pages), "ページ / 訳もれ", len(missing), "文")
    for rel in pages:
        p = ROOT / rel
        src = p.read_text(encoding="utf-8")
        new = put_head(src, head_block(rel, "ja"))
        if new != src:
            p.write_text(new, encoding="utf-8")
    return report


def tag_list(text):
    return sorted(m.group(0).split()[0].rstrip(">").lower() for m in re.finditer(r"</?[a-zA-Z][^>]*>", text)
                  if not m.group(0).lower().startswith(("<rt", "</rt", "<ruby", "</ruby", "<rp", "</rp")))


def hrefs(text):
    return [h.split("?")[0] if h.startswith("mailto:") else h for h in re.findall(r'href="([^"]*)"', text)]


def visible_text(html):
    html = re.sub(r"<(style|script|svg)\b.*?</\1>", " ", html, flags=re.S | re.I)
    html = re.sub(r"<!--.*?-->", " ", html, flags=re.S)
    return re.sub(r"<[^>]*>", "\n", html)


def cmd_check():
    known = routes()
    problems = 0
    for lang in LANGS:
        tm = load_tm(lang)
        for rel in all_pages():
            for _, _, text, _ in segments(source(rel, known)):
                if text not in tm:
                    print("訳もれ", lang, rel, text[:60].replace("\n", " "))
                    problems += 1
                elif tag_list(text) != tag_list(tm[text]):
                    print("タグ違い", lang, rel, text[:60].replace("\n", " "))
                    problems += 1
                elif hrefs(text) != hrefs(tm[text]):
                    print("リンク違い", lang, rel, text[:60].replace("\n", " "))
                    problems += 1
            out = ROOT / lang / rel
            if out.exists():
                for line in visible_text(out.read_text(encoding="utf-8")).splitlines():
                    if JA_STRICT.search(line):
                        print("日本語の残り", lang, rel, line.strip()[:60])
                        problems += 1
    print("問題", problems, "件")
    return problems


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "todo":
        cmd_todo(Path(sys.argv[2]))
    elif cmd == "absorb":
        cmd_absorb(Path(sys.argv[2]))
    elif cmd == "build":
        cmd_build()
    elif cmd == "check":
        sys.exit(1 if cmd_check() else 0)
    else:
        print(__doc__)
        sys.exit(2)


if __name__ == "__main__":
    main()
