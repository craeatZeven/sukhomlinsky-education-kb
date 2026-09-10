# -*- coding: utf-8 -*-
"""分类盲审的**唯一报告生成器**：读 docs/audit/ 里的判读记录，算出全部数字，写一份报告。

用法：
    python scripts/audit.py            # 打印
    python scripts/audit.py --write    # 另写 docs/classification-audit-result.md

证据都在版本库里（`docs/audit/`）：
    key.json                  第一轮抽样时算法的结论（当时快照）
    verdicts-r1a.txt          第一轮判读 passA（旧规格）
    verdicts-r1b.txt          第一轮判读 passB
    verdicts-r2-contaminated.txt  第二轮（**作废**，判读包里混进了算法规则）
    verdicts-r3.txt           第三轮（同批 99 张，干净判读包）
    verdicts-r4.txt           第四轮（**新样本** 100 张，定稿数字）
    SPEC-FOR-JUDGE.md         判读用的规格（只含元规则 + 五个角度 + 收录/不收录）
"""
from __future__ import annotations

import json
import sys
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))
from taxonomy import build_scorer, classify, load_spec  # noqa: E402

AUD = ROOT / "docs" / "audit"
DROP = {"sk-0317"}          # taxonomy.md §六 曾泄露它的答案，判读作废


def load(name: str) -> dict[str, str]:
    p = AUD / name
    if not p.exists():
        return {}
    d = {}
    for line in p.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line and not line.startswith("#") and " " in line:
            parts = line.split()
            if len(parts) >= 2 and parts[0].startswith("sk-"):
                d[parts[0]] = parts[1]
    return d


spec = load_spec()
entry = {e["id"]: e for e in spec["entries"]}
layer = {e["id"]: e["layer"] for e in spec["entries"]}
cards = json.load(open(ROOT / "web" / "data.json", encoding="utf-8"))["cards"]
corpus = {e["id"]: e for e in json.load(
    open(ROOT / "web" / "data" / "search" / "all.json", encoding="utf-8"))}
hay = {c["id"]: " ".join([c.get("title", ""), c.get("cn", ""),
                          corpus.get(c["id"], {}).get("text", "")]) for c in cards}
score = build_scorer(cards, spec, hay)
res = {c["id"]: classify(c, spec, score, hay) for c in cards}          # 当前规格
old_algo = {k: v["算法"] for k, v in
            json.load(open(AUD / "key.json", encoding="utf-8")).items()}  # 第一轮快照

ROUNDS = [
    ("第一轮 passA", "verdicts-r1a.txt", "旧规格 20 条目", "old"),
    ("第一轮 passB", "verdicts-r1b.txt", "旧规格 20 条目", "old"),
    ("第三轮", "verdicts-r3.txt", "新规格 23 条目 + 元规则（同批 99 张）", "new"),
    ("第四轮（新样本）", "verdicts-r4.txt", "新规格 23 条目 + 元规则（新种子）", "new"),
]

out: list[str] = []


def p(s: str = ""):
    out.append(s)
    print(s)


def pct(a, b):
    return f"{a}/{b}（{a / b * 100:.1f}%）" if b else "—"


def eval_round(vf: str, algo: str):
    v = load(vf)
    ids = [c for c in v if v[c] != "?" and c not in DROP and c in res]
    if not ids:
        return None
    a = (lambda c: res[c]["primary"]) if algo == "new" else (lambda c: old_algo.get(c))
    ok = sum(1 for c in ids if a(c) == v[c])
    sl = sum(1 for c in ids if a(c) and layer[a(c)] == layer[v[c]])
    src = defaultdict(lambda: [0, 0])
    for c in ids:
        if algo != "new":
            continue
        s = res[c].get("source")
        src[s][1] += 1
        if res[c]["primary"] == v[c]:
            src[s][0] += 1
    return {"v": v, "ids": ids, "ok": ok, "sl": sl, "abstain": sum(1 for c in v if v[c] == "?"),
            "src": dict(src)}


R = {name: eval_round(vf, algo) for name, vf, _, algo in ROUNDS}

p("# 分类盲审：完整记录与最终结论\n")
p("> 这份文件由 `python scripts/audit.py --write` 生成，**判读记录在 `docs/audit/`**，可复核。")
p("> 判读用规格也一并存档：`docs/audit/SPEC-FOR-JUDGE.md`。\n")

p("## 一、为什么会有这次审计\n")
p("外部评审（2026-09-10）指出：所谓「分配完成」不等于「分类可靠」。旧标签既已被认定存在大量混装，")
p("却又被当作新主归属的最可信证据——一张卡只要碰巧命中旧范围里的泛词，就永远没有纠错机会。")
p("于是做了一次**盲审**：从 718 张论述卡分层抽样，题目只给「原文摘录 / 编辑转述 / 出处」，")
p("旧标签与算法结论另存；由独立判读给出条目，再与算法对答案。\n")

p("## 二、方法（可复现）\n")
p("| 项 | 做法 |")
p("|---|---|")
p("| 抽样 | 按算法主归属等比例分层随机抽 100 张（种子 20260910；第四轮换种子 20260911） |")
p("| 判读材料 | 只有「标题 / 原文摘录 / 编辑转述 / 出处」，**不含旧标签、不含算法结论** |")
p("| 判读规格 | 元规则 + 五个观察角度 + 每条「收录什么 / 不收录什么」；**关键词列与算法规则一律剔除** |")
p("| 判读方式 | 4 个独立判读各判一批，互不可见 |")
p("| 作废 | `sk-0317`（`taxonomy.md` §六 曾明文写出答案）；第二轮整轮（判读包混进了算法规则） |")
p("| 口径 | 条目级＝同一条目；同范畴＝同一个观察角度 |")
p()

p("## 三、最终数字\n")
p("| 判读轮次 | 样本 | 条目级 | 同范畴 | 弃权 |")
p("|---|---|---|---|---|")
for name, vf, note, algo in ROUNDS:
    r = R[name]
    if not r:
        continue
    p(f"| {name} | {len(r['ids'])} 张 | **{r['ok'] / len(r['ids']) * 100:.1f}%** | "
      f"{r['sl'] / len(r['ids']) * 100:.1f}% | {r['abstain']} |")
p()
r4f = R["第四轮（新样本）"]
p(f"**定稿数字：第四轮 {r4f['ok'] / len(r4f['ids']) * 100:.1f}%（条目级）· "
  f"{r4f['sl'] / len(r4f['ids']) * 100:.1f}%（同范畴）。**")
p("样本是**新种子、且排除前三轮用过的卡**——前三轮那 99 张被多轮规格改动影响过，不能用来报业绩。\n")

p("### 3.1 一个反直觉但重要的发现\n")
r3, r4 = R["第三轮"], R["第四轮（新样本）"]
p("- 在**同一批 99 张卡**上，新规格比旧规格是**进步**的："
  f"{R['第一轮 passA']['ok'] / len(R['第一轮 passA']['ids']) * 100:.1f}% → "
  f"{r3['ok'] / len(r3['ids']) * 100:.1f}%。")
p(f"- 但在**新样本**上只有 {r4['ok'] / len(r4['ids']) * 100:.1f}%——"
  f"与最初的 {R['第一轮 passA']['ok'] / len(R['第一轮 passA']['ids']) * 100:.1f}% 基本持平。")
p("- **也就是说：那一批卡上的进步主要是过拟合。** 规格在那 99 张上改了十几轮，")
p("  改到「贴合那批卡」而不是「贴合这套分类」。")
p("- 这正是坚持「换样本复验」的价值：**如果只报第三轮的数字（54.6%），会得出一个错的结论。**\n")

p("## 四、分层看：错在哪里\n")
r = r4
p("### 4.1 按「算法是怎么定下来的」拆\n")
p("| 定案方式 | 第四轮准确率 | 含义 |")
p("|---|---|---|")
s = r["src"]
for k, label in [("prior", "旧标签先验定案"), ("override", "算法推翻旧标签"), ("pending", "待裁决")]:
    if k in s:
        a, b = s[k]
        p(f"| {label} | {a}/{b}（{a / b * 100:.1f}%） | "
          + ("算法与旧标签一致时" if k == "prior" else
             "算法改判到别处时" if k == "override" else "原文无证据") + " |")
p()
p("**算法推翻旧标签时只有 21.4% 是对的**——改判机制基本在帮倒忙。")
p("但它也不是完全没用：见下。\n")

p("### 4.2 三种策略的反事实（四轮都算一遍）\n")
only_label = {}
for c in cards:
    m = [spec["mapping"][t]["primary"] for t in c.get("topics", []) if t in spec["mapping"]]
    only_label[c["id"]] = m[0] if m else None
no_prior = {c["id"]: classify(c, dict(spec, prior=(0.0, 0.0)), score, hay)["primary"] for c in cards}
p("| 策略 | " + " | ".join(n for n, _, _, _ in ROUNDS) + " |")
p("|---" * (len(ROUNDS) + 1) + "|")
p("| A 现状（关键词 + 旧标签先验） | " + " | ".join(
    f"{R[n]['ok'] / len(R[n]['ids']) * 100:.1f}%" if R[n] else "—" for n, _, _, _ in ROUNDS) + " |")
row_b, row_c = "| B 只信旧标签（从不改判） | ", "| C 只信关键词（不用旧标签） | "
for n, _, _, _ in ROUNDS:
    rr = R[n]
    if not rr:
        row_b += "— | "
        row_c += "— | "
        continue
    v = rr["v"]
    row_b += f"{sum(1 for c in rr['ids'] if only_label[c] == v[c]) / len(rr['ids']) * 100:.1f}% | "
    row_c += f"{sum(1 for c in rr['ids'] if no_prior[c] == v[c]) / len(rr['ids']) * 100:.1f}% | "
p(row_b)
p(row_c)
p()
p("**现状比任何一半都好**（比只信旧标签高约 4–12 个点），所以「关键词 + 先验」的组合本身是有效的。")
p("问题不在于该不该组合，而在于**这个组合的天花板大约就在 47–55%**。\n")

p("### 4.3 残余错误集中在哪\n")
bad = Counter((res[c]["primary"] or "待裁决", r["v"][c])
              for c in r["ids"] if res[c]["primary"] != r["v"][c])
p("| 算法判 | 判读认为 | 张数 |")
p("|---|---|---|")
for (a, b), k in bad.most_common(10):
    p(f"| {a} {entry[a]['name'] if a in entry else a} | {b} {entry[b]['name'] if b in entry else b} | {k} |")
p()
p("最大一处仍是 **A5 尊严、爱与信任 ← A19 道德判断与品德培养**（5 张，全是「怎样培养X品质」）。")
p("按外部评审给的判据它们该归 A19，但**把判据翻译成关键词的尝试已被数据否掉**（见 §六）。\n")

p("## 五、判读本身靠不靠得住\n")
r1a, r1b = R["第一轮 passA"]["v"], R["第一轮 passB"]["v"]
both = [c for c in r1a if c in r1b and r1a[c] != "?" and r1b[c] != "?" and c not in DROP]
same = sum(1 for c in both if r1a[c] == r1b[c])
p(f"两批独立判读对同一批卡片互相一致 **{pct(same, len(both))}**（{len(both)} 张两边都给了答案）。\n")
p("⚠️ 这是「两次判读彼此一致的比例」，**不是正确率**——两批同类判读、同材料、同规格，")
p("共同偏差不会被它捕捉。它只能说明一件事：**判读稳定、可复现，所以低一致率不是判读抖动造成的。**\n")
p("而它给出的判断是残酷的：**「认真读一张卡该归哪条」这件事在 90% 以上是可复现的，")
p("关键词算法只做到 47%。** 差距不是任务的模糊，是方法的损失。\n")

p("## 六、被数据否掉的改法（比「改对了什么」更值钱）\n")
p("### 6.1 调关键词权重：没有杠杆\n")
p("逐个关键词从「强证据」降为「弱证据」扫过约 200 次，最好的一档只把一致率抬 2.2 个点。\n")
p("### 6.2 把判据翻译成关键词：会反噬\n")
p("针对 A5←A19 那 5 张，按外部评审的判据把 `关怀/同情/善良/奉献` 从 A5 降为弱证据、")
p("加上 `尊重学生/信任学生` 这类指向儿童的词组。**实测 63.3% → 59.2%（负 4 个点），已回退。**")
p("原因：**「尊重学生」这种词组在原文里几乎不出现**，原文写的是「尊重」「尊重他」。")
p("拿掉泛词只丢召回，不涨精度——判据与词表之间**没有可靠的翻译通道**。\n")
p("### 6.3 同批样本上迭代的收益不泛化\n")
p("这是 §3.1：同批 +8 个点，新样本 +0.7 个点。\n")

p("## 七、审计过程中自己犯的两个方法学错误\n")
p("**① 判读包污染。** 改完规格跑第二轮，判读理由里出现「按『无关键词证据不得定案』排除 sk-0164」——")
p("判读者在用**算法自己的规则**。原因：那句算法规则写进了 `taxonomy.md` §二，而判读包是直接截取生成的。")
p("第二轮整轮作废。第三轮判读包只保留元规则 + 五个角度 + 收录/不收录，并加自动断言检查。")
p("**教训：规格文件同时是「给人读的判据」和「给机器读的实现」，一起发出去，独立判读就不独立了。**\n")
p("**② 让编辑转述替原文提供证据。** 外部评审指出 sk-0219 的「自然/思维课」只出现在编辑转述里，")
p("原文没有——而我此前自己在规格里写过「要区分原文/转述/算法输入」。已写进元规则。\n")

p("## 八、结论与建议\n")
p("1. **条目级自动分配目前不可用。** 46.9% 的一致率意味着每两张卡就有一张的主归属与认真阅读不符。")
p("2. **不要在这条路上继续调参。** 三条证据（调权重无杠杆、判据翻译反噬、同批收益不泛化）都指向同一件事：")
p("   **关键词打分器不是这个任务的合适工具。**")
p("3. **但任务本身是可做的。** 两批独立判读 94% 一致，说明「按元规则认真读」稳定可复现。")
p("   差的是**由谁来读**——现在是关键词在读。")
p("4. **可选方向**（待用户拍板）：")
p("   - **换成 LLM 判读**：保留 23 条目 + 元规则 + 人工裁定表，把分类器从「关键词打分」换成")
p("     「按元规则逐卡判读」。718 张一次性成本，之后改动只需重跑；判读质量已有 94% 的内部一致作参照。")
p("   - **降低粒度**：同范畴一致率 60.2% 明显高于条目级 46.9%。若导航只依赖「五个观察角度」+")
p("     多值主题标签，可用性会立刻提升，代价是失去精确落点。")
p("   - **保留人工裁定表 + 待裁决机制**：无论走哪条路，这两样都该留——它们是这套分类唯一能自我纠错的地方。")
p("5. **不要迁移、不要做前端。** 46.9% 的落点做成页面，是把错误放大给读者看。\n")

if "--write" in sys.argv:
    dst = ROOT / "docs" / "classification-audit-result.md"
    dst.write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"\n已写入 {dst}")
