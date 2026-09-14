# -*- coding: utf-8 -*-
"""
离线影子分片（offline shims）—— 让 file:// 下也能用
=====================================================

问题（2026-09-14 实测）：
  kb.js 用 fetch() 按需读 data/ 的分片。而 file:// 页面的 origin 是 null，
  Chrome 会以 CORS 拒绝**所有** fetch —— 包括同目录的本地文件。
  于是"双击打开 index.html"这句 README 承诺，在检索页上是**假的**：
  search.html 在 file:// 下报「检索失败：Cannot read properties of null」。

修法的机制（已实测验证）：
  file:// 下 fetch 被拦，但 <script src> **不被拦**。
  所以给分片另存一份 .js 版本：
      window.KB_SHIM["search/all.json"] = [...];
  kb.js 在 file:// 下直接注入这个 <script> —— http 下行为完全不变。

覆盖范围（按 kb.js 实际请求过的路径来）：
  meta.json · index.json · ids.json · latest.json · map.json
  index/<slug>.json · search/<scope>.json · topic/<slug>.json
  entry/<code>.json · layer/<n>.json · facet/<code>.json
  单卡 cards/<id>.json —— 1386 个，**不逐个做影子**（会把工作区塞进一千多个文件），
  打成**一个** cards-all.js，只在打开卡片详情时才载入。

用法：
    $env:PYTHONIOENCODING='utf-8'
    D:\python\python.exe scripts\build_offline_shims.py
    ... --check     只报告，不写文件
"""

import argparse
import json
import sys
from pathlib import Path

WEB = Path(__file__).resolve().parent.parent / "web"
DATA = WEB / "data"

CARD_DIR = "cards"
CARD_BUNDLE = "cards-all.js"


def shards():
    """除 cards/ 与 data.json 之外的所有分片。"""
    out = []
    for p in sorted(DATA.rglob("*.json")):
        rel = p.relative_to(DATA).as_posix()
        if rel == "data.json":
            continue                      # 全库快照，浏览器不加载
        if rel.startswith(CARD_DIR + "/"):
            continue                      # 单卡走 cards-all.js
        out.append(rel)
    return out


def main():
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        pass
    ap = argparse.ArgumentParser(description="生成离线影子分片（.json.js）")
    ap.add_argument("--check", action="store_true", help="只报告，不写文件")
    args = ap.parse_args()

    total_out = 0
    written = 0
    print("")
    print("=" * 68)
    print("离线影子分片：" + str(DATA))
    print("=" * 68)
    print("")

    # ---- 单卡打包：1386 个卡片合成一个 cards-all.js ----
    card_dir = DATA / CARD_DIR
    cards = sorted(card_dir.glob("*.json")) if card_dir.is_dir() else []
    if args.check:
        print("  %-34s %5d 张（--check，未打包）" % (CARD_DIR + "/*.json", len(cards)))
    elif cards:
        parts = ["window.KB_SHIM_CARDS = window.KB_SHIM_CARDS || {};\n"]
        n = 0
        for cp in cards:
            raw = cp.read_text(encoding="utf-8").strip()
            if not raw:
                continue
            parts.append("window.KB_SHIM_CARDS[%s] = %s;\n" % (json.dumps(cp.stem), raw))
            n += 1
        bundle = DATA / CARD_BUNDLE
        bundle.write_text("".join(parts), encoding="utf-8")
        sz = bundle.stat().st_size
        total_out += sz
        written += 1
        print("  %-34s %5d 张 -> %8.1f KB" % (CARD_DIR + "/*.json（打包）", n, sz / 1024.0))

    # ---- 其余分片逐个生成 ----
    listed = shards()
    for rel in listed:
        src = DATA / rel
        dst = DATA / (rel + ".js")
        if args.check:
            print("  %-34s %s" % (rel, "影子已存在" if dst.exists() else "**缺影子**"))
            continue
        raw = src.read_text(encoding="utf-8")
        body = ("window.KB_SHIM = window.KB_SHIM || {};\n"
                "window.KB_SHIM[%s] = %s;\n" % (json.dumps(rel), raw.strip()))
        dst.write_text(body, encoding="utf-8")
        total_out += len(body.encode("utf-8"))
        written += 1
    if not args.check:
        print("  ... 另有 %d 个分片逐个生成（meta/index/search/topic/entry/layer/facet/index）"
              % len(listed))

    print("")
    print("-" * 68)
    if args.check:
        print("（--check 模式，未写文件）")
    else:
        print("共写 %d 个影子文件，合计 %.1f MB" % (written, total_out / 1024.0 / 1024.0))
        print("其中单卡是 1 个打包文件，其余是逐分片影子。")
    print("")
    print("提醒：影子是**生成物**，改了 data/ 里的 json 之后要重跑本脚本。")
    print("      已在 .gitignore 里（web/data/**/*.json.js）——可再生产，不进版本库。")
    sys.exit(0)


if __name__ == "__main__":
    main()
