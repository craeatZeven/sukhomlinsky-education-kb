# -*- coding: utf-8 -*-
"""卡片骨架闸门：每张卡必须有**内容块**，且四节齐全。

为什么补它（2026-09-22 实测）
--------------------------
我在批次 5 写 sk-1606 时，切片逻辑遇到「unit 原文断在句中」，结果把引文写成了**空**，
而 `validate_all` 的 13 道检查**全部放行** —— 空引文的卡能一路发到线上。
（同一次自查里另有 11 张卡被我误判为"空引文"，实际它们用 `## 编者概括/Summary`，
那是**契约允许**的转述卡形态 —— 所以判据要把两种形态都算上。）

判据
----
每张卡必须具备下列四节中的前三节 + 内容块：
  1. 内容块：`## 原文/Excerpt`（去空白后 ≥10 字）**或** `## 编者概括/Summary`（≥20 字）
  2. `## 中文转述/说明`（≥20 字）
  3. `## 教育场景/应用`（≥10 字）
  4. `## 出处核对`
两者都没有、或内容过短 → FAIL（这条正是我踩过的那个洞）。
"""
import io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
SEC = lambda t, n: (re.search(r"## %s[ \t]*\n+([\s\S]*?)(?=\n## |\s*$)" % re.escape(n), t) or [None, ""])[1]
def body(s):
    return re.sub(r"[\s>*#-]", "", s or "")


def main():
    problems, n_ex, n_sum = [], 0, 0
    for f in sorted(os.listdir(CARDS)):
        if not (f.startswith("sk-") and f.endswith(".md")):
            continue
        cid = f[:7]
        t = io.open(os.path.join(CARDS, f), encoding="utf-8").read()
        q = body(SEC(t, "原文/Excerpt"))
        s = body(SEC(t, "编者概括/Summary"))
        if len(q) >= 10:
            n_ex += 1
        elif len(s) >= 20:
            n_sum += 1
        else:
            problems.append("%s 没有内容块（原文/Excerpt 与 编者概括/Summary 都空或过短）" % cid)
        if len(body(SEC(t, "中文转述/说明"))) < 20:
            problems.append("%s 的中文转述/说明 过短或缺失" % cid)
        if len(body(SEC(t, "教育场景/应用"))) < 10:
            problems.append("%s 的教育场景/应用 过短或缺失" % cid)
        if "## 出处核对" not in t:
            problems.append("%s 缺 出处核对 节" % cid)
    print("卡片 %d｜原文块 %d · 编者概括块 %d" % (n_ex + n_sum, n_ex, n_sum))
    if problems:
        print("卡片骨架：**%d 处问题**" % len(problems))
        for p in problems[:15]:
            print("  ✗ " + p)
        return 1
    print("卡片骨架：全部齐备（四节 + 内容块）")
    return 0


if __name__ == "__main__":
    sys.exit(main())
