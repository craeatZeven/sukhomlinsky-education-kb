# -*- coding: utf-8 -*-
"""定位层与卡片的一致性闸门。

为什么要有它（2026-09-21 的教训）
--------------------------------
这一轮修定位层时踩到两类**静默**错误，都是"没人会发现"的那种：
  ① 卡片上那行「- 定位：xuan-ji-zh-vol5 · 扫描件第 449 页」和定位数据
     （`local_working_copy/fulltext/card-locators.jsonl`）**各说各话** ——
     数据改了、卡上的字没改，页面上照样显示得有模有样。
  ② 有的卡**根本没有定位数据**，卡上却写着页码（或反过来：有数据、卡上说"无法定位"）。
  ③ 卡片正文里的 `[[sk-XXXX]]` 指向一张不存在的卡 —— 站点会渲染成死链。

规矩
----
1. 卡上的「扫描件第 N 页」必须与定位数据里的 page **一致**（数据在、页在、数相同）。
2. 卡上声称了页码但没有定位数据 → **FAIL**（凭空写页）。
3. 定位数据有 page、卡上却没写 → **WARN**（不算错，但要有理由）。
4. `[[sk-XXXX]]` 的目标卡必须存在。
5. 定位数据里的 `page` 若来自相邻单元推断，必须带 `page_inferred: true`（推断不能被当成观测）。

定位数据在 gitignored 的工作层里（REPO-POLICY：本地全文层不入库），
所以**缺文件时这步跳过并说明**，不让新克隆的仓库因为缺本地数据而失败。
"""
import io, json, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CARDS = os.path.join(ROOT, "cards")
LOC = os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl")
LOC_LINE = re.compile(r"^- 定位：(.+)$", re.M)
PAGE_IN_LINE = re.compile(r"扫描件第\s*(\d+)\s*页")
# ref（出处行）里也会写页码 —— **它和「- 定位：」行一样必须与数据对得上**。
# 2026-09-21 实测：202 张新卡的 ref 里写着「原出处《选集》第5卷 第423页（PDF 页序）」，
# 而 423 是选本引的**纸本**页（还指向文章起始页），实测扫描件是 449 —— 标签错、数也错，199 张。
REF_LINE = re.compile(r'^ref:\s*"(.*)"$', re.M)
REF_MISLABEL = re.compile(r"（PDF 页序）")

PROBLEMS, WARNS = [], []


def main():
    cards, loc_lines, links = {}, {}, []
    for f in sorted(os.listdir(CARDS)):
        if not (f.startswith("sk-") and f.endswith(".md")):
            continue
        cid = f[:7]
        t = io.open(os.path.join(CARDS, f), encoding="utf-8").read()
        cards[cid] = t
        m = LOC_LINE.search(t)
        if m:
            loc_lines[cid] = m.group(1)
        body = t.split("---", 2)[2]
        for ref in re.findall(r"\[\[(sk-\d{4})\]\]", body):
            links.append((cid, ref))

    # 规矩 4：双链必须有落点
    for a, b in links:
        if b not in cards:
            PROBLEMS.append("%s 的双链 [[%s]] 指向不存在的卡" % (a, b))

    if not os.path.exists(LOC):
        print("定位数据不在本地（%s）—— 跳过定位相关判据。" % os.path.relpath(LOC, ROOT))
        print("双链落点：检查 %d 处，问题 %d 处" % (len(links), len(PROBLEMS)))
        for p in PROBLEMS[:15]:
            print("  ✗ " + p)
        return 1 if PROBLEMS else 0

    rows = {}
    for ln in io.open(LOC, encoding="utf-8"):
        if ln.strip():
            d = json.loads(ln)
            rows[d["card"]] = d

    # 规矩 6：ref 里的页码声明也必须与数据一致；且不许用含糊的「（PDF 页序）」
    n_ref = 0
    for cid, t in cards.items():
        m = REF_LINE.search(t)
        if not m:
            continue
        ref = m.group(1)
        if REF_MISLABEL.search(ref):
            PROBLEMS.append("%s 的 ref 用了含糊的「（PDF 页序）」——页码只有两种合法标注："
                            "「扫描件第 N 页（1 基）」与「纸本第 N 页」" % cid)
        for num in PAGE_IN_LINE.findall(ref):
            n_ref += 1
            r = rows.get(cid)
            if not r or r.get("page") is None:
                PROBLEMS.append("%s 的 ref 声称扫描件第 %s 页，但定位数据没有页" % (cid, num))
            elif int(num) != r["page"]:
                PROBLEMS.append("%s 的 ref 写扫描件第 %s 页，定位数据是第 %s 页" % (cid, num, r["page"]))

    n_page, n_none = 0, 0
    for cid, line in loc_lines.items():
        r = rows.get(cid)
        claimed = PAGE_IN_LINE.search(line)
        if r and r.get("page") is not None:
            n_page += 1
            if claimed and int(claimed.group(1)) != r["page"]:
                PROBLEMS.append("%s 卡上写第 %s 页，定位数据是第 %s 页" % (cid, claimed.group(1), r["page"]))
            elif not claimed:
                WARNS.append("%s 有定位页 %s，卡上那行没写页" % (cid, r["page"]))
            if r.get("page_inferred") and "推断" not in line:
                PROBLEMS.append("%s 的页是**推断**出来的（page_inferred），卡上那行没写明" % cid)
        elif claimed:
            PROBLEMS.append("%s 卡上声称第 %s 页，但定位数据%s"
                            % (cid, claimed.group(1), "没有这一行" if not r else "没有 page"))
        else:
            n_none += 1

    # 推断页必须在数据里留痕（与卡上的字分开判：数据是源，卡是显示）
    for cid, r in rows.items():
        if r.get("page") is None and r.get("page_inferred"):
            PROBLEMS.append("%s 的定位 page 为空却标了 page_inferred" % cid)

    print("卡片 %d｜写了「- 定位：」的 %d（其中有页 %d · 无页 %d）｜定位数据 %d 条｜双链 %d 处｜ref 里的扫描件页声明 %d 处"
          % (len(cards), len(loc_lines), n_page, n_none, len(rows), len(links), n_ref))
    if PROBLEMS:
        print("定位一致性：**%d 处问题**" % len(PROBLEMS))
        for p in PROBLEMS[:20]:
            print("  ✗ " + p)
        if len(PROBLEMS) > 20:
            print("  … 另有 %d 处" % (len(PROBLEMS) - 20))
        return 1
    print("定位一致性：全部一致%s" % ("（另有 %d 处提示）" % len(WARNS) if WARNS else ""))
    for w in WARNS[:8]:
        print("  · " + w)
    return 0


if __name__ == "__main__":
    sys.exit(main())
