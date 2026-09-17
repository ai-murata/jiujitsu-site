#!/usr/bin/env python3
"""トップページのカード用サムネイル assets/hojokin.jpg を作る。

固定データで組み立てたページを撮るので、実データの中身には依存しない。ただし
「あと◯日」が荒唐無稽にならないよう、締切だけ実行日からの相対日数に差し替える。
カードは 4:3・object-position: top で表示されるため、絞り込みUIから下を 4:3 で切り取る。

    pip install playwright
    python3 tools/hojokin/make_thumb.py --out assets/hojokin.jpg
"""
import argparse
import json
import pathlib
import subprocess
import sys
import tempfile
from datetime import datetime, timedelta

HERE = pathlib.Path(__file__).resolve().parent
OFFSETS = [12, 34, 58, 81, 103, 126, 150, 172, 195, 217]  # 締切までの日数（見栄え用）


def realistic_fixture(dest):
    """サンプルの締切を実行日からの相対日数に置き換えた一時フィクスチャを作る。"""
    data = json.loads((HERE / "fixtures" / "sample.json").read_text(encoding="utf-8"))
    today = datetime.now()
    for i, item in enumerate(data["result"]):
        if not item.get("acceptance_end_datetime", "").startswith("2099"):
            continue  # 終了済みのサンプルはそのまま（除外されるべきもの）
        end = today + timedelta(days=OFFSETS[i % len(OFFSETS)])
        item["acceptance_end_datetime"] = end.strftime("%Y-%m-%dT17:00:00+09:00")
    dest.write_text(json.dumps(data, ensure_ascii=False), encoding="utf-8")
    return dest


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default="assets/hojokin.jpg")
    ap.add_argument("--chromium", default="", help="Playwright同梱以外のChromiumを使う場合のパス")
    args = ap.parse_args()

    from playwright.sync_api import sync_playwright

    with tempfile.TemporaryDirectory() as tmp:
        tmp = pathlib.Path(tmp)
        fixture = realistic_fixture(tmp / "thumb-fixture.json")
        page_path = tmp / "index.html"
        subprocess.check_call([
            sys.executable, str(HERE / "build.py"),
            "--fixture", str(fixture), "--out", str(page_path),
        ], stderr=subprocess.DEVNULL)

        out = pathlib.Path(args.out)
        out.parent.mkdir(parents=True, exist_ok=True)
        with sync_playwright() as p:
            launch = {"executable_path": args.chromium} if args.chromium else {}
            browser = p.chromium.launch(**launch)
            pg = browser.new_page(viewport={"width": 900, "height": 1400}, device_scale_factor=2)
            pg.goto(page_path.as_uri())
            pg.wait_for_timeout(1500)  # Webフォントの読み込み待ち
            top = pg.eval_on_selector(".controls", "e => e.getBoundingClientRect().top + window.scrollY")
            pg.screenshot(
                path=str(out), type="jpeg", quality=86, full_page=True,
                clip={"x": 0, "y": top - 16, "width": 900, "height": 675},
            )
            browser.close()
        print(f"{out} を書き出しました")


if __name__ == "__main__":
    main()
