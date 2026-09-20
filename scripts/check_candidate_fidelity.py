# -*- coding: utf-8 -*-
"""候选卡的「原文」与书全文的对账闸门。

为什么需要它
------------
候选卡的原文是用脚本从书全文里抠出来的，中间还叠了几层自动清理（去书眉、
去乱码前缀、修 OCR 单字）。这类清理**会悄悄吃掉正文**：本仓库踩过一次——
书眉正则把两端各多吃了几个字，删掉了正文里的「人」「观察自己」，而卡片照样
「看起来正常」。所以每张候选卡的原文必须能回到书全文里**逐字对上**。

对不上的地方分两类：
  * 书眉/版式串（「苏霍姆林斯基选集（五卷本）」之类）—— 剥掉后应该什么都不剩，正常；
  * 剥完还剩连续汉字 —— 就是**被吃掉的正文**，本脚本判 FAIL。

这个检查与写入脚本**不共用任何变换**：只认 corpus.db 里的原始文本，且只比汉字
（不比标点），所以「我修得对不对」不靠我自己那套规则背书。

用法
----
    D:\\python\\python.exe scripts/check_candidate_fidelity.py
    D:\\python\\python.exe scripts/check_candidate_fidelity.py --dir <目录>
    D:\\python\\python.exe scripts/check_candidate_fidelity.py --json <输出.json>

退出码：0 = 没发现被吃掉的正文；1 = 有。
「锚点找不到」（卡片抄的是选本而非选集）列为 WARN，不判 FAIL。
"""
import argparse, difflib, glob, io, json, os, re, sqlite3, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")
CAND_ROOT = os.path.join(ROOT, "local_working_copy", "card-candidates")

HEADS = [
    "苏霍姆林斯基选集五卷本", "苏霍姆林选集五卷本", "苏霍姆林斯基选集", "苏霍姆林选集",
    "公民的诞生", "帕夫雷什中学", "帕夫需什中学", "把心给了孩子们", "把心献给孩子",
    "快乐学校", "给教师的建议", "我的教育信条", "和青年校长的谈话",
    "苏霍姆林斯基", "霍姆林斯基", "姆林斯基", "苏雷姆杯斯基选集", "孫雀姆林亚基",
    "苏徂姆林斯", "苏霍", "选集", "五卷本",
]
CJK = re.compile(r"[\u4e00-\u9fff]")


def cjk_only(s):
    return "".join(CJK.findall(s))


def strip_heads(s):
    for h in sorted(HEADS, key=len, reverse=True):
        s = s.replace(h, "")
    return s


def load_corpus():
    if not os.path.exists(DB):
        sys.exit("找不到语料库：%s" % DB)
    conn = sqlite3.connect(DB)
    by_vol = {}
    for vol, txt in conn.execute(
            "SELECT volume, group_concat(text, char(10)) FROM units "
            "WHERE book LIKE '%选集%' GROUP BY volume"):
        by_vol[str(vol)] = cjk_only(txt)
    whole = cjk_only("\n".join(r[0] for r in conn.execute("SELECT text FROM units")))
    # 跨页拼接的卡片：书里那张页的书眉夹在句子中间，整段当然对不上。
    # 所以再备一份「把书眉从书里也剥掉」的副本 —— 两边都不含书眉，才谈得上逐字比对。
    return by_vol, whole, strip_heads(whole)


def read_origin(path):
    t = io.open(path, encoding="utf-8").read()
    # 取到下一个二级标题为止。原来写成 ([\s\S]+?)\s*$ —— 那是「一直到文件尾」，
    # 卡片一旦补了「中文转述/说明」小节，就会把整篇一起当成原文（本仓库踩过）。
    m = re.search(r"## 原文（[^）]*）[ \t]*\n+([\s\S]*?)(?=\n#{1,2}[ \t]|\s*$)", t)
    if not m:
        return None, None
    vol = (re.search(r"^source: xuan-ji-zh-vol(\d)", t, re.M) or [None, "?"])[1]
    return m.group(1), vol


def local_align(n, whole):
    """整段找不到时用中段 16 字种子定位做局域比对；返回 (相似度, 缺失段列表)。"""
    locs = []
    for frac in (0.33, 0.5, 0.15):
        i = int(len(n) * frac)
        seed = n[i:i + 16]
        if len(seed) < 16:
            continue
        locs = [m.start() for m in re.finditer(re.escape(seed), whole)][:5]
        if locs:
            break
    if not locs:
        return None, None
    best = None
    for L in locs:
        a, b = max(0, L - len(n) - 60), min(len(whole), L + len(n) + 60)
        seg = whole[a:b]
        r = difflib.SequenceMatcher(None, n, seg).ratio()
        if best is None or r > best[0]:
            best = (r, seg)
    r, seg = best
    missing = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, n, seg).get_opcodes():
        if tag in ("insert", "replace"):
            g = strip_heads(seg[j1:j2])
            if len(g) >= 2:
                missing.append(g)
    return r, missing


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None)
    ap.add_argument("--json", default=None)
    args = ap.parse_args()
    dirs = [args.dir] if args.dir else sorted(
        d for d in glob.glob(os.path.join(CAND_ROOT, "*")) if os.path.isdir(d))
    by_vol, whole, whole_clean = load_corpus()
    ok, warn, fail, total = 0, [], [], 0
    for d in dirs:
        for f in sorted(glob.glob(os.path.join(d, "cand-*.md"))):
            text, vol = read_origin(f)
            if text is None:
                continue
            total += 1
            cid = "%s/%s" % (os.path.basename(d), os.path.basename(f)[:-3])
            n = cjk_only(text)
            if not n:
                fail.append((cid, "正文为空"))
                continue
            if n in whole or n in whole_clean or n in by_vol.get(str(vol), ""):
                ok += 1
                continue
            r, missing = local_align(n, whole_clean)
            # 关键：相似度低时这段对齐是错位的（卡片抄的是选本、不在选集里），
            # 这种「缺字」是尺子自己的幻觉，不能拿去判人家的文本。
            if r is None or r < 0.90:
                warn.append((cid, "未能逐字对回选集（r=%s）—— 多半抄自选本原文，非删除"
                             % ("-" if r is None else "%.2f" % r)))
            elif missing:
                fail.append((cid, "r=%.2f 书里有而卡里缺：%s" % (r, "｜".join(missing)[:120])))
            else:
                ok += 1
    print("对账候选卡：%d 张" % total)
    print("  逐字对回书全文（含剥书眉后对上）：%d" % ok)
    print("  WARN（对不上，不判失败）：%d" % len(warn))
    for cid, why in warn:
        print("     - %s %s" % (cid, why))
    print("  FAIL（高相似度对齐下，书里有而卡里没有 = 被吃掉的正文）：%d" % len(fail))
    for cid, why in fail:
        print("     ! %s %s" % (cid, why))
    if args.json:
        io.open(args.json, "w", encoding="utf-8").write(json.dumps(
            {"ok": ok, "warn": [list(x) for x in warn],
             "fail": [list(x) for x in fail], "total": total},
            ensure_ascii=False, indent=1))
    print("结论：%s" % ("PASS" if not fail else "FAIL"))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())