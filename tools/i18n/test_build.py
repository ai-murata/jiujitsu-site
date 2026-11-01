#!/usr/bin/env python3
"""tools/i18n/build.py のテスト（ネットワーク不要）。

  python3 tools/i18n/test_build.py
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402

KNOWN = {"/", "/blog/", "/blog/a/"}


def test_segments_keep_inline_tags_together():
    src = '<p>こんにちは<b>世界</b>です</p><p>English only</p>'
    assert [s[2] for s in build.segments(src)] == ['こんにちは<b>世界</b>です']


def test_block_inside_link_is_split():
    src = '<a class="card" href="/x/"><h2>見出し</h2><p>説明</p></a>'
    assert [s[2] for s in build.segments(src)] == ['見出し', '説明']


def test_attribute_and_script_text():
    src = '<img alt="写真"><script>var a = "こんにちは"; // コメント</script>'
    assert [(s[2], s[3]) for s in build.segments(src)] == [("写真", "attr"), ("こんにちは", '"')]


def test_translate_escapes_quotes():
    src = "<script>var a = 'はい';</script><img alt=\"写真\">"
    out = build.translate(src, {"はい": "Don't", "写真": 'a "photo"'}, [])
    assert "'Don\\'t'" in out and 'alt="a &quot;photo&quot;"' in out


def test_links():
    assert build.fix_url("/blog/a/", "/blog", "en", KNOWN) == "/en/blog/a/"
    assert build.fix_url("img.png", "/blog/a", "en", KNOWN) == "/blog/a/img.png"
    assert build.fix_url("/dojo/", "/", "ko", KNOWN) == "/dojo/"
    assert build.fix_url("/textbook/", "/", "pt", KNOWN) == "/textbook/?lang=pt"
    assert build.fix_url("https://jiujitsu.co.jp/blog/a/", "/", "en", KNOWN) == "https://jiujitsu.co.jp/en/blog/a/"
    assert build.fix_url("https://example.com/", "/", "en", KNOWN) == "https://example.com/"


def test_links_in_scripts_are_left_alone():
    html = """<script>x = '<a href="' + url + '">';</script><a href="/blog/a/">a</a>"""
    out = build.rewrite_links(html, "index.html", "en", KNOWN)
    assert """'<a href="' + url + '">'""" in out and 'href="/en/blog/a/"' in out


def main():
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
    print("OK")


if __name__ == "__main__":
    main()
