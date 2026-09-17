#!/usr/bin/env python3
"""tools/hojokin/build.py のオフラインテスト。ネットワークにはアクセスしない。"""

import json
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest
from datetime import datetime, timedelta

sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))

import build  # noqa: E402

HERE = pathlib.Path(__file__).resolve().parent
CONFIG = json.loads((HERE / "config.json").read_text(encoding="utf-8"))
FIXTURE = HERE / "fixtures" / "sample.json"
NOW = datetime(2099, 6, 1, 9, 0, tzinfo=build.JST)


def items():
    return json.loads(FIXTURE.read_text(encoding="utf-8"))["result"]


def records():
    return build.to_records(items(), CONFIG, NOW)


def by_id(rows):
    return {r["id"]: r for r in rows}


class AreaTest(unittest.TestCase):
    def test_nationwide_covers_every_prefecture(self):
        prefs, nationwide = build.expand_areas(["全国"])
        self.assertTrue(nationwide)
        self.assertEqual(len(prefs), 47)

    def test_region_expands_to_its_members(self):
        prefs, nationwide = build.expand_areas(["近畿地方"])
        self.assertFalse(nationwide)
        self.assertIn("大阪府", prefs)
        self.assertNotIn("東京都", prefs)

    def test_koshinetsu_belongs_to_kanto_region(self):
        prefs, _ = build.expand_areas(["関東・甲信越地方"])
        for pref in ("東京都", "新潟県", "山梨県", "長野県"):
            self.assertIn(pref, prefs)
        self.assertNotIn("静岡県", prefs)

    def test_prefecture_and_region_together_are_merged(self):
        prefs, _ = build.expand_areas(["東京都", "関東・甲信越地方"])
        self.assertIn("東京都", prefs)
        self.assertIn("群馬県", prefs)

    def test_missing_area_is_treated_as_nationwide(self):
        prefs, nationwide = build.expand_areas([])
        self.assertTrue(nationwide)
        self.assertEqual(len(prefs), 47)

    def test_every_prefecture_is_covered_exactly_once(self):
        self.assertEqual(len(build.PREFECTURES), 47)
        self.assertEqual(len(set(build.PREFECTURES)), 47)


class RecordTest(unittest.TestCase):
    def setUp(self):
        self.rows, self.dropped = records()
        self.ids = [r["id"] for r in self.rows]

    def test_keeps_every_region_not_just_tokyo(self):
        for sid in ("fx-jizokuka-001", "fx-tokyo-002", "fx-osaka-003",
                    "fx-kansai-004", "fx-hokkaido-006"):
            self.assertIn(sid, self.ids)

    def test_drops_closed_large_and_out_of_industry(self):
        self.assertNotIn("fx-closed-009", self.ids)
        self.assertNotIn("fx-large-008", self.ids)
        self.assertNotIn("fx-nogyo-007", self.ids)
        self.assertEqual(self.dropped, {"従業員規模外": 1, "業種違い": 1, "募集終了": 1})

    def test_prefecture_lookup_is_usable_by_the_page(self):
        rows = by_id(self.rows)
        self.assertIn("大阪府", rows["fx-osaka-003"]["prefs"])
        self.assertNotIn("東京都", rows["fx-osaka-003"]["prefs"])
        self.assertIn("北海道", rows["fx-hokkaido-006"]["prefs"])
        self.assertEqual(len(rows["fx-jizokuka-001"]["prefs"]), 47)

    def test_days_left_is_computed_from_now(self):
        rows = by_id(self.rows)
        self.assertEqual(rows["fx-sports-005"]["days"], 60)  # 6/1 -> 7/31

    def test_sorted_by_deadline_by_default(self):
        days = [r["days"] for r in self.rows]
        self.assertEqual(days, sorted(days))

    def test_dojo_relevant_entry_scores_above_generic_one(self):
        rows = by_id(self.rows)
        self.assertGreater(rows["fx-sports-005"]["score"], rows["fx-noarea-010"]["score"])


class PageTest(unittest.TestCase):
    def setUp(self):
        rows, _ = records()
        self.rows = rows
        self.page = build.render_page(rows, CONFIG, NOW)

    def test_data_is_embedded_and_parsable(self):
        match = re.search(r"const DATA = (\[.*?\]);\n", self.page, re.S)
        self.assertIsNotNone(match)
        data = json.loads(match.group(1).replace("\\u003c", "<"))
        self.assertEqual(len(data), len(self.rows))

    def test_script_tag_cannot_be_broken_by_data(self):
        row = {"id": "x", "title": "</script><script>alert(1)</script>", "org": "", "catch": "",
               "max": None, "start": "", "end": "", "days": None, "areas": [], "prefs": [],
               "nationwide": True, "emp": [], "purpose": [], "industry": [], "score": 0, "url": "#"}
        page = build.render_page([row], CONFIG, NOW)
        self.assertNotIn("</script><script>alert(1)", page)
        self.assertIn("\\u003c/script", page)

    def test_all_47_prefectures_are_selectable(self):
        for pref in ("北海道", "東京都", "大阪府", "沖縄県"):
            self.assertIn(f'<option value="{pref}">', self.page)

    def test_credits_jgrants_as_source(self):
        self.assertIn("Jグランツ", self.page)
        self.assertIn("公募要領の原文で確認", self.page)

    def test_links_back_to_the_site(self):
        self.assertIn('href="/"', self.page)

    def test_css_braces_survived_templating(self):
        self.assertIn("--gold: #a3801a;", self.page)
        self.assertIn("box-sizing: border-box;", self.page)
        self.assertNotIn("{{", self.page)

    def test_warns_when_some_keywords_failed(self):
        page = build.render_page(self.rows, CONFIG, NOW, errors=["boom"])
        self.assertIn("取得に失敗", page)
        self.assertNotIn("取得に失敗", self.page)


class CollectTest(unittest.TestCase):
    def test_merges_by_id(self):
        def fake(keyword):
            return [{"id": "dup", "title": "重複"}, {"id": keyword, "title": keyword}]
        cfg = dict(CONFIG, keywords=["A", "B"], request_interval_seconds=0)
        rows, errors = build.collect(cfg, fetcher=fake)
        self.assertEqual(errors, [])
        self.assertEqual(len(rows), 3)

    def test_one_failure_does_not_abort(self):
        def flaky(keyword):
            if keyword == "A":
                raise RuntimeError("jGrants API 取得失敗 (keyword=A)")
            return [{"id": "ok"}]
        cfg = dict(CONFIG, keywords=["A", "B"], request_interval_seconds=0)
        rows, errors = build.collect(cfg, fetcher=flaky)
        self.assertEqual([r["id"] for r in rows], ["ok"])
        self.assertEqual(len(errors), 1)


class CliTest(unittest.TestCase):
    def test_fixture_run_writes_the_page(self):
        with tempfile.TemporaryDirectory() as tmp:
            out = pathlib.Path(tmp) / "hojokin" / "index.html"
            rc = subprocess.call([
                sys.executable, str(HERE / "build.py"),
                "--fixture", str(FIXTURE), "--out", str(out),
            ], stderr=subprocess.DEVNULL)
            self.assertEqual(rc, 0)
            page = out.read_text(encoding="utf-8")
            self.assertIn("<title>道場が使える補助金", page)
            self.assertIn("小規模事業者持続化補助金", page)


if __name__ == "__main__":
    unittest.main(verbosity=2)
