#!/usr/bin/env python3
"""クラウド日記のオフラインテスト（ネットワーク不要）。

    python3 tools/nikki/test_build.py
"""

import json
import pathlib
import sys
import tempfile
import unittest
from datetime import datetime

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import build  # noqa: E402

CONFIG = build.load_config()


def commit(subject, time, files, author="Claude", body=""):
    return {"sha": "0" * 40, "author": author, "subject": subject, "body": body, "files": files,
            "date": datetime.fromisoformat(f"2026-09-29T{time}:00+09:00")}


COMMITS = [
    commit("トップページ：柔術ニュースを上に移動", "10:00", ["index.html"]),
    commit("chore(jiunews): 柔術ニュースを更新 (2026-09-29)", "06:50", ["jiunews/index.html"]),
    commit("chore(hojokin): 補助金一覧を更新", "06:31", ["hojokin/index.html"], author="github-actions[bot]"),
    commit("まみちゃん売上ノートを直す", "11:00", ["mami-b5d5e37cd655/index.html"]),
    commit("売上ノートの色を変える", "11:10", ["mami-b5d5e37cd655/index.html"]),
    commit("アイコンを変更", "12:00", ["favicon.ico", "staff/index.html"]),
    commit("前の日の作業", "23:59", ["index.html"]) | {"date": datetime.fromisoformat("2026-09-28T23:59:00+09:00")},
    commit("本文つき", "09:00", ["blog/index.html"], body="理由を書いた\n\nCo-Authored-By: Claude <x@example.com>"),
]

GOOD = {
    "date": "2026-09-29",
    "title": "柔術ニュースをいちばん上に",
    "lead": "今日はトップページの並びを変えました。",
    "items": [{"heading": "トップの並び替え", "text": "ニュースを上に移してもらいました。"}],
    "closing": "明日も続けます。",
}


class SelectTest(unittest.TestCase):
    def setUp(self):
        self.work, self.auto, self.skipped = build.select(COMMITS, "2026-09-29", CONFIG)

    def test_only_that_day_and_sorted(self):
        self.assertEqual([w["subject"] for w in self.work], ["本文つき", "トップページ：柔術ニュースを上に移動", "アイコンを変更"])

    def test_auto_commits_are_only_counted(self):
        self.assertEqual(len(self.auto), 2)
        names = {a["name"] for a in build.auto_summary(self.auto)}
        self.assertEqual(names, {"柔術ニュース", "補助金一覧"})

    def test_private_commits_are_dropped(self):
        self.assertEqual(self.skipped, 2, "非公開の言葉を含む／非公開ページだけを触ったコミットは外す")
        joined = json.dumps(self.work, ensure_ascii=False)
        self.assertNotIn("mami", joined)
        self.assertNotIn("staff/", joined, "公開と非公開の両方を触ったコミットは、非公開のファイル名を消す")

    def test_signature_lines_removed(self):
        self.assertEqual(self.work[0]["body"], "理由を書いた")

    def test_prompt_lists_work(self):
        auto = build.auto_summary(self.auto)
        p = build.build_prompt("2026-09-29", self.work, auto, CONFIG, "data/nikki/inbox")
        self.assertIn("トップページ：柔術ニュースを上に移動", p)
        self.assertIn("柔術ニュース 1件", p)
        self.assertIn("村田亜衣", p)


class EntryTest(unittest.TestCase):
    CANDS = {"date": "2026-09-29", "work": [], "auto": [{"name": "柔術ニュース", "count": 1}]}

    def test_good_result(self):
        e = build.to_entry(GOOD, self.CANDS, CONFIG)
        self.assertEqual(e["auto"], self.CANDS["auto"])

    def bad(self, **change):
        with self.assertRaises(ValueError):
            build.to_entry({**GOOD, **change}, self.CANDS, CONFIG)

    def test_rejects_private_words(self):
        self.bad(closing="まみちゃんのノートも直しました。")
        self.bad(items=[{"heading": "スタッフ用ページ", "text": "直した"}])

    def test_rejects_urls_and_hashes(self):
        self.bad(lead="https://example.com を見てね")
        self.bad(lead="コミット 72b8c6d0a1b2c3 を入れた")

    def test_rejects_missing_and_wrong_date(self):
        self.bad(date="2026-09-28")
        self.bad(items=[])
        self.bad(title="")
        self.bad(items=[GOOD["items"][0]] * (CONFIG["max_items"] + 1))


class RenderTest(unittest.TestCase):
    def test_apply_and_render_escapes(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = pathlib.Path(tmp)
            inbox = root / "inbox"
            inbox.mkdir()
            (inbox / "candidates.json").write_text(json.dumps(EntryTest.CANDS), encoding="utf-8")
            (inbox / "result.json").write_text(json.dumps({**GOOD, "title": "<script>x</script>"}), encoding="utf-8")
            build.apply(root, inbox, CONFIG)
            page = (root / "blog/nikki/2026-09-29/index.html").read_text(encoding="utf-8")
            self.assertNotIn("<script>x", page)
            self.assertIn("&lt;script&gt;", page)
            self.assertIn("柔術ニュース 1件", page)
            self.assertIn("/blog/nikki/2026-09-29/", (root / "blog/nikki/index.html").read_text(encoding="utf-8"))
            # 同じ日はもう集めない
            self.assertFalse(build.collect(build.REPO, root, root / "again", "2026-09-29", CONFIG))


if __name__ == "__main__":
    unittest.main(verbosity=2)
