# -*- coding: utf-8 -*-
"""候选卡「正文起点」审计：起点有没有把上一句话的尾巴/半个词切掉。

为什么要单做这一项
------------------
第七批里连着撞见四张：063 脱「一」、064 脱「少」、065 脱「因此我要再三忠」、
067 脱「学」。它们**全都落在正文起始处**，不像 OCR 的形近替换，更像是
「提取窗口起点偏晚」——一类系统性截断。零星撞见一次修一次太慢，
所以把它做成一次全库扫描。

怎么判（判据只用书，不用卡自己那套规则）
----------------------------------------
1. 把卡文整段定位回《选集》（只比汉字）；
2. 看定位处**前面一个字符**是什么：
   * 句末标点 → 起点合法，悬挂 0，正常；
   * 不是句末标点 → 卡文是从句子中间开始的，量出「悬挂长度」
     = 往回数到上一个句末标点之间还有几个字符。
3. 分档：
   * dangle = 0       起点在句首 —— 正常
   * 1 ≤ dangle ≤ 12  多半是把该带的字切掉了 —— **可疑**
   * dangle > 12      多半是选本有意截取的从句 —— 需人工判断

注意：可疑不等于错。选本本来就允许从句子中间摘引。这份清单是**给人看的**，
列出被切掉的那几个字，由人决定补不补。

用法
----
    D:\\python\\python.exe scripts/audit_excerpt_starts.py
    D:\\python\\python.exe scripts/audit_excerpt_starts.py --dir <目录> --json <输出.json>
"""
import argparse, glob, io, json, os, re, sqlite3, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DB = os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")
CAND_ROOT = os.path.join(ROOT, "local_working_copy", "card-candidates")

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from check_candidate_fidelity import (CJK, cjk_only, strip_heads, FOOTNOTE,
                                      read_origin, HEADS,
                                      declared_pairs, revert_declared)  # noqa: E402

SENT_END = set("。！？!?…；;：:｡") | {"."}   # 句点也算句末（版本号/编号项会用到）
CLOSERS = set("」』“”‘’）】》〉〕］") | {chr(34), chr(39)}


def strip_heads_text(s):
    """只剥书眉串，保留标点。"""
    for h in sorted(HEADS, key=len, reverse=True):
        s = s.replace(h, "")
    return s


def build_hay(conn, where):
    """返回 (保留标点的正文串, 汉字在其中的下标表)。书眉与译者注先剔除。"""
    rows = conn.execute("SELECT text FROM units " + where).fetchall()
    keep = [r[0] for r in rows if not FOOTNOTE.search(r[0].strip())]
    s = re.sub(r"\s+", "", strip_heads_text("\n".join(keep)))
    idx = [i for i, ch in enumerate(s) if CJK.match(ch)]
    return s, idx


def locate(card_cjk, hay, idx):
    """把卡文定位回书里，返回 (起点下标, 用的偏移)。

    **只有 off=0 的定位才算数**：偏移找回来的是「卡文第 off 字在书里的位置」，
    再往前推 off 个字当起点 —— 可卡文与书在这几个字上本来就可能有差
    （例如我这轮把选集的 OCR 错字改对了），推出来的起点就是假的，
    对应的「悬挂」也就成了尺子的幻觉。宁可判「定位不到」。
    """
    cjk_hay = "".join(hay[i] for i in idx)
    seed = card_cjk[:20]
    if len(seed) < 12:
        return None, None
    k = cjk_hay.find(seed)
    if k >= 0:
        return idx[k], 0
    for off in (2, 4, 6, 8, 12, 16):
        s2 = card_cjk[off:off + 20]
        if len(s2) < 12:
            continue
        if cjk_hay.find(s2) >= 0:
            return None, off
    return None, None


def dangle(hay, pos):
    """从 pos 往回数到上一个句末标点，返回 (悬挂长度, 被切掉的那段字)。"""
    j = pos - 1
    while j >= 0 and hay[j] in CLOSERS:
        j -= 1
    if j < 0 or hay[j] in SENT_END:
        return 0, ""
    end = j
    while j >= 0 and hay[j] not in SENT_END and hay[j] not in CLOSERS:
        j -= 1
    return len(hay[j + 1:end + 1]), hay[j + 1:end + 1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None)
    ap.add_argument("--json", default=None)
    args = ap.parse_args()
    dirs = [args.dir] if args.dir else sorted(
        d for d in glob.glob(os.path.join(CAND_ROOT, "*")) if os.path.isdir(d))
    conn = sqlite3.connect(DB)
    hay_all, idx_all = build_hay(conn, "WHERE book LIKE '%选集%'")
    # 选本通道：候选卡来自《教育箴言》，选本对原句做过节缩 —— 开头若用选本措辞，
    # 在选集里当然对不上。分出来，人工就不必逐个去读。
    hay_zw, idx_zw = build_hay(conn, "WHERE book LIKE '%jiao-yu-zhen-yan%'")
    cjk_zw = "".join(hay_zw[i] for i in idx_zw)
    per_vol = {}
    for (volname,) in conn.execute(
            "SELECT DISTINCT volume FROM units WHERE book LIKE '%选集%'"):
        m = re.search(r"第([0-9一二三四五])卷", str(volname))
        if m:
            per_vol[m.group(1)] = build_hay(
                conn, "WHERE book LIKE '%%选集%%' AND volume = '%s'" % volname)
    clean, noted, suspect, manual, unlocated, shifted, explained_list, from_zw, total = [], [], [], [], [], [], [], [], 0
    for d in dirs:
        for f in sorted(glob.glob(os.path.join(d, "cand-*.md"))):
            raw = io.open(f, encoding="utf-8").read()
            text, vol = read_origin(f)
            if text is None:
                continue
            total += 1
            # 把所有声明行拼起来看 —— 只取第一条会漏：卡片里 ocr_fixes 常排在 excerpt_note 前面，
            # 而「起点相关」的判断要看的是后者（实测因此漏掉两张已声明的卡）。
            note_text = " ".join(m.group(1) for m in re.finditer(
                r"^(?:excerpt_note|ocr_note|ocr_fixes): (.+)$", raw, re.M))
            noted_flag = ("excerpt_note:" in raw) or bool(re.search(r"起点|句首", note_text))
            cid = "%s/%s" % (os.path.basename(d), os.path.basename(f)[:-3])
            n = cjk_only(text)
            hay, idx = per_vol.get(str(vol), (hay_all, idx_all))
            pos, off = locate(n, hay, idx)
            if pos is None:
                pos, off = locate(n, hay_all, idx_all)
            explained = False
            if pos is None or off:   # 完全找不到，或只在开头第 N 字之后才对上 —— 两条路都要试反推
                # 起点整段对不上时，先把声明过的逐字修法**反推回去**再试一次。
                # 卡片开头若改过字，反推后能对回书里 —— 那是「我改过」，不是「起点有问题」，
                # 不该占人工复核的位置（这一层归因之前，「定位不到」16 条里绝大多数是这类）。
                n_r = revert_declared(n, declared_pairs(raw))
                if n_r != n:
                    pos2, off2 = locate(n_r, hay, idx)
                    if pos2 is None:
                        pos2, off2 = locate(n_r, hay_all, idx_all)
                    if pos2 is not None and not off2:
                        # 反推后能在开头第 0 字对上 ⇒ 起点本身没问题，差额全由我声明的修字解释
                        explained, n, pos, off = True, n_r, pos2, off2
            if pos is None:
                # 最后两道归因：开头是不是用了选本的节缩措辞；或卡片自己声明过起点处理。
                # 声明必须是**起点相关**的（含「起点」或「句首」），不然随便一条备注就能豁免。
                if len(n) >= 20 and n[:20] in cjk_zw:
                    from_zw.append(cid)
                elif noted_flag and re.search(r"起点|句首", note_text):
                    noted.append((cid, 0, note_text[:48]))
                elif off:
                    shifted.append((cid, off))
                else:
                    unlocated.append(cid)
                continue
            if explained:
                explained_list.append(cid)
                continue
            dl, cut = dangle(hay, pos)
            if dl == 0:
                clean.append(cid)
            elif noted_flag:
                # 卡片已声明「起点为句中摘引（选本同）」——这是选本的选择，不是截断
                noted.append((cid, dl, cut))
            elif dl <= 12:
                suspect.append((cid, dl, cut))
            else:
                # 长悬挂（起点前还挂着 >12 字）：看**选本**是不是也从同一处起引。
                # 选本自己就从句子中间摘，那是编者的选择，不是提取截断 —— 归此类的自动出清。
                kz = cjk_zw.find(n[:16]) if len(n) >= 16 else -1
                if kz > 0 and hay_zw[idx_zw[kz] - 1] not in SENT_END:
                    from_zw.append(cid)
                else:
                    manual.append((cid, dl, cut[-24:]))
    print("审了候选卡：%d 张" % total)
    print("  起点在句首（正常）：%d" % len(clean))
    print("  ★ 可疑截断（悬挂 1~12 字）：%d" % len(suspect))
    for cid, dl, cut in suspect:
        print("     %s  悬挂 %d 字，被切掉：%s" % (cid, dl, cut))
    print("  已声明为句中摘引（excerpt_note，选本同）：%d" % len(noted))
    print("  长悬挂（选本有意摘引，需人工判断）：%d" % len(manual))
    for cid, dl, tail in manual:
        print("     %s  悬挂 %d 字  …%s" % (cid, dl, tail))
    print("  ★ 起点处改过字、反推后能对回书里（正常，不必人工看）：%d" % len(explained_list))
    print("  ★ 开头用选本节缩措辞（在选集里对不上属正常）：%d %s" % (len(from_zw), [c.split(chr(47))[-1] for c in from_zw][:12]))
    print("  起点对不上（卡文开头与书不一致，多为已修过 OCR 的卡）：%d" % len(shifted))
    for cid, off in shifted[:12]:
        print("     %s  开头第 %d 字才与书对上" % (cid, off))
    print("  定位不到：%d %s" % (len(unlocated), unlocated[:8]))
    if args.json:
        io.open(args.json, "w", encoding="utf-8").write(json.dumps(
            {"clean": len(clean), "noted": noted, "suspect": suspect, "manual": manual,
             "explained": explained_list, "from_anthology": from_zw,
             "shifted": shifted, "unlocated": unlocated,
             "total": total},
            ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()