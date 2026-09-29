#!/usr/bin/env python3
"""tools/search/build.py のテスト（ネットワーク不要）。

  python3 tools/search/test_build.py
"""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import build  # noqa: E402


class ParseTest(unittest.TestCase):
    def test_text_skips_scripts_nav_footer(self):
        p = build.parse(
            "<title>ページ</title><meta name='description' content='説明'>"
            "<nav>もくじ</nav><h1>見出し</h1><p>本文<br>つづき</p>"
            "<script>var x='秘密';</script><style>.a{}</style><footer>運営</footer>"
        )
        self.assertEqual(p.title, "ページ")
        self.assertEqual(p.description, "説明")
        self.assertEqual(p.headings, ["見出し"])
        text = p.text()
        self.assertIn("本文", text)
        self.assertIn("つづき", text)
        for hidden in ("もくじ", "秘密", "運営", ".a{}"):
            self.assertNotIn(hidden, text)

    def test_ruby_reading_is_dropped(self):
        p = build.parse("<p><ruby>AI<rt>亜衣</rt></ruby>が運用</p>")
        self.assertEqual(p.text(), "AIが運用")

    def test_noindex_and_redirect(self):
        self.assertTrue(build.parse('<meta name="robots" content="noindex,nofollow">').noindex)
        self.assertTrue(build.parse('<meta http-equiv="refresh" content="0; url=/x/">').redirect)
        self.assertFalse(build.parse("<p>ふつう</p>").noindex)

    def test_js_data(self):
        src = 'x\nconst DATA = [{"name":"道場A","pref":"北海道"}];\ny'
        self.assertEqual(build.js_data(src), [{"name": "道場A", "pref": "北海道"}])
        self.assertEqual(build.js_data("no data"), [])


class SiteTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.index = build.build_index()
        cls.urls = {p["url"] for p in cls.index["pages"]}

    def test_public_pages_are_indexed(self):
        for url in ("/", "/blog/", "/dojo/", "/hojokin/", "/company/"):
            self.assertIn(url, self.urls)

    def test_private_pages_are_not_indexed(self):
        for url in ("/staff/", "/handbook/", "/taikai/", "/search/", "/_shot.html"):
            self.assertNotIn(url, self.urls)
        for url in self.urls:
            self.assertFalse(url.startswith(("/mami-", "/secondo-")), url)

    def test_every_page_has_title(self):
        for p in self.index["pages"]:
            self.assertTrue(p["title"], p["url"])

    def test_dojo_items(self):
        dojo = next(p for p in self.index["pages"] if p["url"] == "/dojo/")
        self.assertGreater(len(dojo.get("items", [])), 100)

    def test_index_is_up_to_date(self):
        current = build.OUT.read_text(encoding="utf-8") if build.OUT.exists() else ""
        self.assertEqual(build.dump(self.index), current,
                         "search/index.json が古いです。python3 tools/search/build.py を実行してください")


if __name__ == "__main__":
    unittest.main()
