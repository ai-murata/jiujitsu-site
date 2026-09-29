#!/usr/bin/env python3
"""/jiunews/ のオフラインテスト（ネットワークも Claude API も使わない）。

    python3 tools/jiunews/test_build.py
"""

import json
import pathlib
import sys
import tempfile
import unittest
from datetime import datetime, timezone

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

FIX = HERE / "fixtures"
NOW = datetime(2026, 9, 28, 22, 0, tzinfo=timezone.utc)  # 2026-09-29 07:00 JST
FEEDS = {
    "ja": {"name": "Googleニュース（柔術）", "region": "jp"},
    "bjjee": {"name": "BJJEE", "region": "intl"},
    "atom": {"name": "Grappling", "region": "intl"},
}


def parse(fixture, feed):
    return build.parse_feed((FIX / fixture).read_bytes(), FEEDS[feed])


class ParseTest(unittest.TestCase):
    def test_google_news_source_and_title(self):
        items = parse("1-google-ja.xml", "ja")
        first = items[0]
        self.assertEqual(first["source"], "格闘技ニュース")
        self.assertEqual(first["title"], "全日本ブラジリアン柔術選手権、茶帯で17歳が初優勝")
        self.assertEqual(first["snippet"], "", "Googleニュースの description はタイトルの繰り返しなので捨てる")
        self.assertEqual(first["region"], "jp")

    def test_rss_snippet_strips_html_and_script(self):
        item = parse("2-bjjee.xml", "bjjee")[0]
        self.assertIn("return to competition", item["snippet"])
        self.assertNotIn("<", item["snippet"])
        self.assertNotIn("alert", item["snippet"])
        self.assertEqual(item["source"], "BJJEE")

    def test_leading_blank_lines_before_xml_declaration(self):
        data = b"\n\n  \n" + (FIX / "2-bjjee.xml").read_bytes()
        self.assertEqual(len(build.parse_feed(data, FEEDS["bjjee"])), 2)

    def test_atom_and_rejects_non_http_links(self):
        items = parse("3-atom.xml", "atom")
        self.assertEqual(len(items), 1, "javascript: のリンクは読まない")
        self.assertEqual(items[0]["link"], "https://grappling.example.com/ibjjf-rules-2027")
        self.assertTrue(items[0]["published"].startswith("2026-09-28T12:00"))


class CollectTest(unittest.TestCase):
    def config(self, hours=36):
        return {
            "feeds": [
                {"name": "a", "region": "jp", "url": "u1"},
                {"name": "b", "region": "intl", "url": "u2"},
                {"name": "broken", "region": "intl", "url": "u3"},
            ],
            "lookback_hours": hours,
        }

    def fetcher(self, url):
        return {
            "u1": (FIX / "1-google-ja.xml").read_bytes(),
            "u2": (FIX / "2-bjjee.xml").read_bytes(),
        }.get(url) or (_ for _ in ()).throw(RuntimeError("down"))

    def test_one_broken_feed_does_not_stop(self):
        cands, errors = build.collect(self.config(), NOW, {}, self.fetcher)
        self.assertEqual(len(errors), 1)
        self.assertEqual(len(cands), 5)

    def test_seen_and_old_are_dropped(self):
        seen = {build.item_id("https://www.bjjee.com/articles/gordon-ryan-return/", ""): "2026-09-28"}
        cands, _ = build.collect(self.config(hours=14), NOW, seen, self.fetcher)
        links = {c["link"] for c in cands}
        self.assertNotIn("https://www.bjjee.com/articles/gordon-ryan-return/", links)
        # 14時間前 = 2026-09-28 08:00 UTC。それより前の記事は落ちる
        self.assertNotIn("https://news.google.com/rss/articles/CCC333?oc=5", links)
        self.assertIn("https://news.google.com/rss/articles/AAA111?oc=5", links)


class EditionTest(unittest.TestCase):
    def setUp(self):
        self.cands = parse("1-google-ja.xml", "ja") + parse("2-bjjee.xml", "bjjee")
        self.config = {"max_items_jp": 1, "max_items_intl": 5}

    def test_unknown_ids_and_urls_from_model_are_ignored(self):
        gordon = next(c for c in self.cands if "Gordon" in c["title"])
        result = {
            "lead": "今日のニュースです。",
            "items": [
                {"id": "deadbeef0000", "category": "その他", "title": "でっち上げ", "summary": "x", "point": ""},
                {"id": gordon["id"], "category": "選手・人物", "title": "ゴードン・ライアンが復帰へ",
                 "summary": "復帰を表明しました。", "point": "", "link": "https://evil.example/"},
                {"id": gordon["id"], "category": "選手・人物", "title": "重複", "summary": "x", "point": ""},
            ],
        }
        ed = build.to_edition(result, self.cands, "2026-09-29", self.config, NOW)
        self.assertEqual(len(ed["items"]), 1)
        self.assertEqual(ed["items"][0]["link"], gordon["link"])
        self.assertEqual(ed["items"][0]["region"], "intl")
        self.assertEqual(ed["items"][0]["original_title"], gordon["title"])

    def test_region_limits_and_bad_category(self):
        jp = [c for c in self.cands if c["region"] == "jp"]
        result = {"lead": "l", "items": [
            {"id": c["id"], "category": "謎", "title": "t", "summary": "s", "point": ""} for c in jp
        ]}
        ed = build.to_edition(result, self.cands, "2026-09-29", self.config, NOW)
        self.assertEqual(len(ed["items"]), 1)
        self.assertEqual(ed["items"][0]["category"], "その他")

    def test_empty_result_has_no_lead(self):
        ed = build.to_edition({"lead": "何か", "items": []}, self.cands, "2026-09-29", self.config, NOW)
        self.assertEqual(ed["items"], [])
        self.assertEqual(ed["lead"], "")


class RenderTest(unittest.TestCase):
    def edition(self, date, title='<script>alert("x")</script>'):
        return {
            "date": date, "generated_at": "", "lead": "リード & まとめ",
            "items": [
                {"id": "a", "region": "jp", "category": "大会結果", "title": title, "summary": "要約",
                 "point": "見どころ", "source": "媒体<b>", "original_title": "", "link": "https://a.example/?x=1&y=2",
                 "published": ""},
                {"id": "b", "region": "intl", "category": "選手・人物", "title": "海外", "summary": "要約",
                 "point": "", "source": "BJJEE", "original_title": "Original", "link": "javascript:alert(1)",
                 "published": ""},
            ],
        }

    def test_render_escapes_and_links(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            build.write_edition(root, self.edition("2026-09-28", "昨日の見出し"))
            build.write_edition(root, self.edition("2026-09-29"))
            build.write_edition(root, {"date": "2026-09-27", "lead": "", "items": []})  # 空の号は出さない
            editions = build.render_all(root)
            self.assertEqual([e["date"] for e in editions], ["2026-09-29", "2026-09-28"])

            index = (root / "jiunews" / "index.html").read_text(encoding="utf-8")
            self.assertNotIn("<script>alert", index)
            self.assertIn("&lt;script&gt;", index)
            self.assertIn('href="https://a.example/?x=1&amp;y=2"', index)
            self.assertNotIn("javascript:alert", index)
            self.assertIn("海外のニュース（日本語訳）", index)
            self.assertIn("BJJEE（英語）", index)
            self.assertIn('href="/jiunews/2026-09-28/"', index, "過去の号への一覧")
            self.assertIn("AI（Claude）", index, "AI要約である旨の注記は消さない")

            day = (root / "jiunews" / "2026-09-28" / "index.html").read_text(encoding="utf-8")
            self.assertIn('href="/jiunews/2026-09-29/"', day)
            self.assertFalse((root / "jiunews" / "2026-09-27").exists())

    def test_render_empty(self):
        with tempfile.TemporaryDirectory() as tmp:
            build.render_all(pathlib.Path(tmp))
            index = (pathlib.Path(tmp) / "jiunews" / "index.html").read_text(encoding="utf-8")
            self.assertIn("準備中", index)


class EndToEndTest(unittest.TestCase):
    def test_fixture_run_with_fake_llm(self):
        with tempfile.TemporaryDirectory() as tmp:
            args = ["--root", tmp, "--fixture-dir", str(FIX), "--fake-llm", "--date", "2026-09-29"]
            self.assertEqual(build.main(args), 0)
            ed = json.loads((pathlib.Path(tmp) / "data/jiunews/editions/2026-09-29.json").read_text(encoding="utf-8"))
            self.assertTrue(ed["items"])
            seen = json.loads((pathlib.Path(tmp) / "data/jiunews/seen.json").read_text(encoding="utf-8"))["seen"]
            self.assertTrue(seen)
            # 同じ日にもう一度走らせても、号は作り直さない
            self.assertEqual(build.main(args), 0)

    def test_collect_then_apply(self):
        """ルーティン用の2段階：候補を書き出す → Claude が result.json を書く → 号にする。"""
        with tempfile.TemporaryDirectory() as tmp, tempfile.TemporaryDirectory() as work:
            base = ["--root", tmp, "--fixture-dir", str(FIX), "--date", "2026-09-29"]
            self.assertEqual(build.main(base + ["--collect-only", work]), 0)
            prompt = (pathlib.Path(work) / "prompt.md").read_text(encoding="utf-8")
            self.assertIn("result.json", prompt)
            self.assertIn('"additionalProperties": false', prompt)
            cands = json.loads((pathlib.Path(work) / "candidates.json").read_text(encoding="utf-8"))["candidates"]
            self.assertFalse((pathlib.Path(tmp) / "data/jiunews/editions").exists(), "書き出しだけでは号を作らない")

            pick = cands[0]
            result = {"lead": "今日のニュースです。", "items": [
                {"id": pick["id"], "category": "大会結果", "title": "見出し", "summary": "要約です。", "point": ""},
            ]}
            (pathlib.Path(work) / "result.json").write_text(json.dumps(result, ensure_ascii=False), encoding="utf-8")
            self.assertEqual(build.main(["--root", tmp, "--date", "2026-09-29", "--apply", work]), 0)
            ed = json.loads((pathlib.Path(tmp) / "data/jiunews/editions/2026-09-29.json").read_text(encoding="utf-8"))
            self.assertEqual([i["link"] for i in ed["items"]], [pick["link"]])
            self.assertTrue((pathlib.Path(tmp) / "jiunews/2026-09-29/index.html").exists())
            seen = json.loads((pathlib.Path(tmp) / "data/jiunews/seen.json").read_text(encoding="utf-8"))["seen"]
            self.assertEqual(len(seen), len(cands), "載せなかった候補も既出として覚える")

    def test_prompt_contains_candidates_and_schema_is_strict(self):
        cands = parse("2-bjjee.xml", "bjjee")
        system, user = build.build_prompt(cands, {"max_items_jp": 5, "max_items_intl": 6})
        self.assertIn("最大 6 件", system)
        self.assertIn(cands[0]["id"], user)
        self.assertFalse(build.OUTPUT_SCHEMA["additionalProperties"])
        self.assertFalse(build.OUTPUT_SCHEMA["properties"]["items"]["items"]["additionalProperties"])

    def test_config_is_valid(self):
        config = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
        regions = {f["region"] for f in config["feeds"]}
        self.assertEqual(regions, {"jp", "intl"})
        for f in config["feeds"]:
            self.assertTrue(f["url"].startswith("https://"), f["name"])


if __name__ == "__main__":
    unittest.main(verbosity=1)
