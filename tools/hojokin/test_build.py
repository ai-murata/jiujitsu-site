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


FIXTURE_RAW = json.loads(FIXTURE.read_text(encoding="utf-8"))


def items(enriched=True):
    """一覧APIの返りを模したもの。enriched=True で詳細APIの内容をかぶせる。"""
    rows = json.loads(json.dumps(FIXTURE_RAW["result"]))
    if enriched:
        build.enrich(rows, {"detail_interval_seconds": 0},
                     fetcher=FIXTURE_RAW["details"].get)
    return rows


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


class DetailTest(unittest.TestCase):
    """一覧APIは利用目的・業種・キャッチコピーを返さない。詳細APIで補う。"""

    def test_list_alone_has_no_purpose_or_industry(self):
        raw = items(enriched=False)
        self.assertEqual([], build.values(raw[0], "use_purpose"))
        self.assertEqual([], build.industry_values(raw[0]))

    def test_detail_fills_purpose_and_industry(self):
        rows = by_id(records()[0])
        self.assertIn("販路拡大・海外展開をしたい", rows["fx-jizokuka-001"]["purpose"])
        self.assertIn("生活関連サービス業、娯楽業", rows["fx-jizokuka-001"]["industry"])

    def test_industry_comes_from_the_detail_field(self):
        self.assertEqual(["製造業"], build.industry_values({"industry": "製造業"}))
        self.assertEqual([], build.industry_values({"title": "業種欄なし"}))

    def test_a_failed_detail_lookup_does_not_drop_the_item(self):
        rows = items(enriched=False)
        got = build.enrich(rows, {"detail_interval_seconds": 0}, fetcher=lambda _id: None)
        self.assertEqual(got, 0)
        self.assertEqual(len(rows), len(FIXTURE_RAW["result"]))

    def test_internal_code_is_never_shown(self):
        # name は S-00007152 のような内部コード。表に出してはいけない。
        self.assertEqual("", build.program_alias({"name": "S-00007152", "title": "何か"}))
        for r in records()[0]:
            self.assertNotRegex(r["alias"] or "x", r"^[A-Z]-?\d+$")

    def test_alias_is_shown_only_when_it_adds_something(self):
        long_title = "【経済産業省】ものづくり・商業・サービス生産性向上促進補助金（19次締切）"
        self.assertEqual("ものづくり補助金", build.program_alias(
            {"title": long_title, "institution_name": "ものづくり補助金"}))
        # タイトルに丸ごと含まれるなら情報が増えないので出さない
        self.assertEqual("", build.program_alias(
            {"title": "東京都商店街デジタル化推進事業費補助金",
             "institution_name": "商店街デジタル化推進事業費補助金"}))

    def test_a_longer_alias_is_a_data_error_and_is_dropped(self):
        # jGrants 側に、別制度の名前が institution_name に入っている件がある
        self.assertEqual("", build.program_alias(
            {"title": "「賃上げ環境整備補助金2026」",
             "institution_name": "【北海道】中小企業競争力強化促進事業（マーケティング支援事業）［2次募集］"}))

    def test_detail_page_url_is_preferred_over_the_guessed_one(self):
        rows = by_id(records()[0])
        self.assertEqual("https://www.jgrants-portal.go.jp/subsidy/fx-jizokuka-001",
                         rows["fx-jizokuka-001"]["url"])
        self.assertTrue(rows["fx-osaka-003"]["url"].endswith("fx-osaka-003"))


class HintTest(unittest.TestCase):
    """「使いどころ」は当たったときだけ出す。当たらなければ黙る。"""

    def setUp(self):
        self.rows = by_id(records()[0])

    def test_title_gives_the_grounded_hint(self):
        self.assertIn("空き店舗を道場に改装する費用に使えることが多い",
                      self.rows["fx-osaka-003"]["hints"])

    def test_purpose_only_supplements_a_grounded_hint(self):
        # 「持続化」でヒントが立ってはじめて、利用目的（販路拡大）の一言が後ろに付く
        hints = self.rows["fx-jizokuka-001"]["hints"]
        self.assertLess(hints.index("小規模な道場が最も使いやすい定番の補助金"),
                        hints.index("体験入会の集客、チラシやWeb広告に"))

    def test_purpose_alone_never_produces_a_hint(self):
        # 一覧に載るほとんどの補助金が「設備整備・IT導入をしたい」を持っているため、
        # これだけで書くと無関係な補助金に道場向けの文言が付いてしまう
        oil = {"title": "令和7年度_産油国石油精製技術等対策事業費補助金",
               "industry": "サービス業（他に分類されないもの）"}
        self.assertEqual([], build.use_hints(oil, CONFIG, ["設備整備・IT導入をしたい",
                                                          "新たな事業を行いたい"]))

    def test_generic_equipment_wording_is_not_treated_as_a_dojo_signal(self):
        gas = {"title": "【二次公募】令和８年度 天然ガス利用設備による強靱性向上対策事業費補助金",
               "industry": "サービス業（他に分類されないもの）"}
        self.assertEqual([], build.use_hints(gas, CONFIG, ["設備整備・IT導入をしたい"]))

    def test_out_of_industry_items_get_nothing_even_with_a_matching_word(self):
        construction = {"title": "スポーツ施設の建設促進事業", "industry": "建設業"}
        self.assertEqual([], build.use_hints(construction, CONFIG, []))

    def test_generic_subsidies_stay_silent(self):
        # デジタルツール導入・人材確保は、道場に限った話が何も言えないので黙る
        self.assertEqual([], self.rows["fx-tokyo-002"]["hints"])
        self.assertEqual([], self.rows["fx-hokkaido-006"]["hints"])

    def test_only_a_minority_of_items_get_a_hint(self):
        with_hints = [r for r in self.rows.values() if r["hints"]]
        self.assertLess(len(with_hints), len(self.rows))
        self.assertTrue(with_hints)

    def test_small_business_wording_is_not_repeated(self):
        # タイトルの「小規模事業者」と従業員数の両方が当たっても、同じ文が2度出ない
        item = {"title": "小規模事業者持続化補助金",
                "industry": "サービス業（他に分類されないもの）",
                "target_number_of_employees": "5名以下 / 20名以下"}
        hints = build.use_hints(item, CONFIG, [])
        self.assertEqual(len(hints), len(set(hints)))
        self.assertEqual(1, hints.count(CONFIG["small_business_hint"]))

    def test_hints_are_capped_so_the_card_stays_short(self):
        for r in self.rows.values():
            self.assertLessEqual(len(r["hints"]), 3)

    def test_nothing_is_invented_when_no_rule_matches(self):
        item = {"id": "x", "title": "何かの交付金", "target_number_of_employees": "300名以下",
                "industry": "サービス業（他に分類されないもの）"}
        self.assertEqual([], build.use_hints(item, CONFIG, []))

    def test_page_shows_the_hints(self):
        page = build.render_page(records()[0], CONFIG, NOW)
        self.assertIn("使いどころ", page)
        self.assertIn("道場向きのみ", page)


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
