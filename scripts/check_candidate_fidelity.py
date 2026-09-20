# -*- coding: utf-8 -*-
"""候选卡的「原文」与书全文的对账闸门。

为什么需要它
------------
候选卡的原文是脚本从书全文里抠出来、又叠了几层自动清理（去书眉、去乱码前缀、
修 OCR 单字）的产物。这类清理**会悄悄吃掉正文**，而卡片读起来照样通顺：
本仓库踩过一次 —— 删书眉的正则两端越界，把「一个**人**」的「人」和后面的
「**观察自己**」一起删了，剩「如果不能引导一，思索自己的命运」，通读发现不了。

三个判决（分开是因为它们的证据强度不同）
----------------------------------------
  OK   原文在《选集》里逐字命中（剥书眉后命中也算）。
  GAP  与《选集》高度一致（相似度≥阈值），但书里有几处字卡里没有。
       **这不必然是「被吃掉的正文」** —— 《教育箴言》是选本，它对原句做过节缩，
       节缩出来的缺口和「被吃掉」长得一模一样。所以只报「待人工确认」。
  FAIL **记录过的删除**里，删掉的字在书里查得到（剥掉书眉词后仍余≥2 个汉字）。
       这一条证据最硬：卡片自己声明了删什么，而那段字确实存在于书里。

另外单列两类：
  WARN  与《选集》对不上（相似度低于阈值），无法判定。
  自证  只在《教育箴言》选本/译本里对上 —— 卡片本来就抄自选本，
        在这里对上说明不了任何事。这一类比 WARN 更弱，不是「通过」。

这个检查**不与被检查的写入脚本共用任何变换**：只认 corpus.db 的原始文本，
且只比汉字、不比标点。

用法
----
    D:\\python\\python.exe scripts/check_candidate_fidelity.py
    D:\\python\\python.exe scripts/check_candidate_fidelity.py --dir <目录>
    D:\\python\\python.exe scripts/check_candidate_fidelity.py --json <输出.json>
    D:\\python\\python.exe scripts/check_candidate_fidelity.py --gap-threshold 0.90

退出码：0 = 无删掉正文的证据；1 = 有。
"""
import argparse, difflib, glob, io, json, os, re, sqlite3, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")
CAND_ROOT = os.path.join(ROOT, "local_working_copy", "card-candidates")

HEADS = [
    "苏霍姆林斯基选集五卷本", "苏霍姆林选集五卷本", "苏霍姆林斯基选集", "苏霍姆林选集",
    "公民的诞生", "帕夫雷什中学", "帕夫需什中学", "把心给了孩子们", "把心献给孩子",
    "快乐学校", "给教师的建议", "和青年校长的谈话",
    # 书眉的 OCR 变体：实测「我的教育信条」在书里被 OCR 成「我的教育信急」，
    # 漏了它，跨页拼接的句子就会被误判成「对不上选集」。
    "我的教育信条", "我的教育信急", "我的教育信念",
    "苏霍姆林斯基", "霍姆林斯基", "姆林斯基", "苏雷姆杯斯基选集", "孫雀姆林亚基",
    "苏徂姆林斯", "苏霍", "选集", "五卷本",
    # 书眉的又一批 OCR 变体（基→墓、五→万 等，逐页不同）
    "苏霍姆林斯墓选集", "霍姆林斯墓选集", "姆林斯墓选集", "苏霍姆林斯墓",
    "苏霍姆林斯基选集万卷本", "办霍姆林斯基选集", "苏霍姆林斯墓迭集",
]
CJK = re.compile(r"[\u4e00-\u9fff]")
# 译者注不是正文。语料里它作为独立 unit 夹在句子中间（实测：一句跨页的话被
# ①尼古拉·基巴利契奇…②伊万·巴布什金… 两条注释劈开），照直拼接就永远对不上。
FOOTNOTE = re.compile(r"^[\u2460-\u2473]|译者$")


def cjk_only(s):
    return "".join(CJK.findall(s))


def strip_heads(s):
    for h in sorted(HEADS, key=len, reverse=True):
        s = s.replace(h, "")
    return s


def load_corpus():
    """返回 (按卷的选集文本, 选集全文, 非选集文本)，都是汉字串且已剥书眉。

    选集与非选集必须分开：候选卡的出处写的是《选集》第 N 卷，如果只在
    《教育箴言》选本里对上，那是拿卡片的来源验卡片，等于没验。
    """
    if not os.path.exists(DB):
        sys.exit("找不到语料库：%s" % DB)
    conn = sqlite3.connect(DB)

    def blob(where):
        rows = conn.execute("SELECT text FROM units " + where).fetchall()
        keep = [r[0] for r in rows if not FOOTNOTE.search(r[0].strip())]
        return strip_heads(cjk_only("\n".join(keep)))

    by_vol = {}
    for volname, txt in conn.execute(
            "SELECT volume, group_concat(text, char(10)) FROM units "
            "WHERE book LIKE '%选集%' GROUP BY volume"):
        # 注意：units.volume 列里存的是**书名**（「苏霍姆林斯基选集（五卷本）第4卷」），
        # 不是卷号。直接拿它当键、再用 ref 里的「第4卷」去查，永远查不到，
        # 于是每次都退回全书做错位对齐 —— 全表看起来「对不上」，其实是尺子没接上。
        m = re.search(r"第([0-9一二三四五])卷", str(volname))
        # 按行剔除译者注（这里拿到的是 group_concat 的结果）
        keep = [ln for ln in str(txt).split(chr(10)) if not FOOTNOTE.search(ln.strip())]
        by_vol[m.group(1) if m else str(volname)] = strip_heads(cjk_only(chr(10).join(keep)))
    return by_vol, blob("WHERE book LIKE '%选集%'"), blob("WHERE book NOT LIKE '%选集%'")


def read_origin(path):
    """取卡片正文里的「原文」小节，以及 source 里的卷号。"""
    t = io.open(path, encoding="utf-8").read()
    # 取到下一个标题为止。原来写成 ([\s\S]+?)\s*$ —— 那是「一直到文件尾」，
    # 卡片一旦补了「中文转述/说明」小节，整篇都会被当成原文（本仓库踩过）。
    m = re.search(r"## 原文（[^）]*）[ \t]*\n+([\s\S]*?)(?=\n#{1,2}[ \t]|\s*$)", t)
    if not m:
        return None, None
    vol = (re.search(r"^source: xuan-ji-zh-vol(\d)", t, re.M) or [None, "?"])[1]
    return m.group(1), vol


def local_align(n, hay, gap_threshold=0.90):
    """局域比对：多粒种子各自定位，取相似度最高的一次对齐。

    两个坑都踩过，所以这里写得别扭但必要：
    1. 只用一粒种子会定位错（种子里只要有一个 OCR 改过的字就找不到）；
    2. 窗口加宽衬边会把衬边算成不匹配 —— 加 60 字衬边时，连完美对齐的
       相似度都被压到 0.55，于是「书里有卡里没有」全是错位的幻觉。
       所以只留 2 字余量 + 小步平移取最优。
    """
    seeds = [(i, n[i:i + 16]) for i in range(0, max(1, len(n) - 16), 24)]
    seeds = [(i, s) for i, s in seeds if len(s) == 16]
    if not seeds:
        return None, None, None
    best = None
    seen = set()
    for i, s in seeds:
        for m in list(re.finditer(re.escape(s), hay))[:3]:
            base = m.start() - i   # 种子落点是「n 的第 i 个字」，故 n 起点约在 L-i
            for shift in (-6, -3, -1, 0, 1, 3, 6):
                s0 = max(0, base + shift)
                if s0 in seen:
                    continue
                seen.add(s0)
                seg = hay[max(0, s0 - 2):s0 + len(n) + 2]
                r = difflib.SequenceMatcher(None, n, seg).ratio()
                if best is None or r > best[0]:
                    best = (r, seg)
    if best is None:
        return None, None, None
    r, seg = best
    ops = difflib.SequenceMatcher(None, n, seg).get_opcodes()
    missing = []
    for k, (tag, i1, i2, j1, j2) in enumerate(ops):
        if tag not in ("insert", "replace"):
            continue
        # 窗口首尾的错位是尺子的边界效应（卡文常从句子中间起，或结束在句子中间），
        # 不是「卡里少了字」，所以只报严格内部的缺口。
        if k == 0 or k == len(ops) - 1:
            continue
        g = strip_heads(seg[j1:j2])
        if len(g) >= 2:
            missing.append(g)
    return r, missing, seg


def declared_pairs(text):
    """从 ocr_fixes 里取出「A→B」这类逐字修法（位置无关，所以可以反推回去）。

    「删…「X」」那类不行 —— 删掉的位置无从得知，无法反推。
    返回 [(改后, 改前)]，用于把卡片正文还原成书里的原样。
    """
    pairs = []
    for line in re.findall(r"^ocr_fixes: (.+)$", text, re.M):
        # 冒号与空白都要排除：否则「ocr_fixes: 教帅→教师」会把整段前缀当成「改后」
        for a, b in re.findall(r"([^\s；：:→（）()]+)→([^\s；：:→（）()]+)", line):
            if a and b and "删" not in a:
                pairs.append((a, b))
    return pairs


def revert_declared(n, pairs):
    """按声明的修法反推，还原成书里的样子。

    pairs 里的每一项是 (书里的原样, 我改成的新字) —— 记录写成「A→B」时
    A 是书/选集的错字，B 是我改对的字。所以反推要拿 B 换回 A（写反了会一个都命中不了）。
    """
    out = n
    for wrong, fixed in reversed(pairs):
        if fixed in out:
            out = out.replace(fixed, wrong)
    return out

def recorded_deletions(text):
    """从 ocr_fixes 里取出被删掉的串，以及该条是否已回补。

    只认「删……「X」」这种紧挨着的写法。带括号的不算 ——
    例如「一并删去（原句为「由此入手」）」是在**说明**原句，不是在声明删除，
    早先的正则把它当成了删除记录（假阳性）。
    同一条记录里写了「回补」的，视为已修回，单独计。
    """
    fixed, open_ = [], []
    for line in re.findall(r"^ocr_fixes: (.+)$", text, re.M):
        hits = re.findall(r"删[^「」（）()]*「([^」]+)」", line)
        (fixed if "回补" in line else open_).extend(hits)
    return fixed, open_


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None)
    ap.add_argument("--json", default=None)
    ap.add_argument("--gap-threshold", type=float, default=0.90)
    args = ap.parse_args()
    dirs = [args.dir] if args.dir else sorted(
        d for d in glob.glob(os.path.join(CAND_ROOT, "*")) if os.path.isdir(d))
    by_vol, xuanji, other = load_corpus()
    ok, gap, fail, warn, circular, total, repaired, reverted = 0, [], [], [], [], 0, 0, 0
    for d in dirs:
        for f in sorted(glob.glob(os.path.join(d, "cand-*.md"))):
            raw = io.open(f, encoding="utf-8").read()
            text, vol = read_origin(f)
            if text is None:
                continue
            total += 1
            cid = "%s/%s" % (os.path.basename(d), os.path.basename(f)[:-3])
            n = cjk_only(text)
            if not n:
                fail.append((cid, "正文为空"))
                continue
            # ① 记录过的删除：删掉的字在不在书里（剥掉书眉词后仍余汉字 = 删了正文）
            fixed_del, open_del = recorded_deletions(raw)
            repaired += len(fixed_del)
            for dstr in open_del:
                rest = strip_heads(cjk_only(dstr))
                if len(rest) >= 2 and rest in xuanji:
                    fail.append((cid, "删掉的字在书里查得到：「%s」（余「%s」）" % (dstr[:20], rest[:20])))
            # ② 逐字命中
            if n in by_vol.get(str(vol), "") or n in xuanji:
                ok += 1
                continue
            # ②b 把我声明过的逐字修法反推回去再验一次：
            #     还原后能逐字命中，说明「与书不一致」的部分**完全由声明解释**，
            #     那不是吃字，是修字。目标仍然是书，所以这不是自证。
            pairs = declared_pairs(raw)
            n_rev = revert_declared(n, pairs)
            if n_rev != n and (n_rev in by_vol.get(str(vol), "") or n_rev in xuanji):
                ok += 1
                reverted += 1
                continue
            # ③ 先跟《选集》对齐，再判「是不是只在选本里对上」——
            #    顺序反了会冤枉卡片：去标点后选集原文与选本常逐字相同。
            hay = by_vol.get(str(vol)) or xuanji
            r, missing, seg = local_align(n, hay, args.gap_threshold)
            if (r is None or r < args.gap_threshold) and hay is not xuanji:
                r2, m2, seg2 = local_align(n, xuanji, args.gap_threshold)
                if r2 is not None and (r is None or r2 > r):
                    r, missing, seg = r2, m2, seg2
            if r is not None and r >= args.gap_threshold:
                if missing:
                    gap.append((cid, "r=%.2f 书里有而卡里没有：%s"
                                % (r, "｜".join(missing)[:110])))
                else:
                    ok += 1
            elif n in other:
                circular.append((cid, "r=%s 只在非选集文本里对上（选本/译本），不算验过"
                                 % ("-" if r is None else "%.2f" % r)))
            else:
                warn.append((cid, "未能逐字对回选集（r=%s）"
                             % ("-" if r is None else "%.2f" % r)))
    print("对账候选卡：%d 张" % total)
    print("  OK   逐字对回《选集》（含剥书眉后对上）：%d" % ok)
    print("       其中靠「反推声明的 ocr_fixes 后命中」计入：%d" % reverted)
    print("  GAP  高度一致但书里有几处卡里没有（待人工确认，选本节缩也会有此现象）：%d" % len(gap))
    for cid, why in gap:
        print("     ? %s %s" % (cid, why))
    print("  WARN 对不上选集，无法判定：%d" % len(warn))
    for cid, why in warn:
        print("     - %s %s" % (cid, why))
    print("  自证 只在非选集文本里对上（不算验过）：%d" % len(circular))
    for cid, why in circular:
        print("     ~ %s %s" % (cid, why))
    print("  已回补 记录里声明删过、并已修回的字：%d 处" % repaired)
    print("  FAIL 有删掉正文的证据：%d" % len(fail))
    for cid, why in fail:
        print("     ! %s %s" % (cid, why))
    if args.json:
        io.open(args.json, "w", encoding="utf-8").write(json.dumps(
            {"ok": ok, "gap": [list(x) for x in gap], "warn": [list(x) for x in warn],
             "circular": [list(x) for x in circular], "fail": [list(x) for x in fail],
             "total": total}, ensure_ascii=False, indent=1))
    print("结论：%s" % ("PASS" if not fail else "FAIL"))
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())