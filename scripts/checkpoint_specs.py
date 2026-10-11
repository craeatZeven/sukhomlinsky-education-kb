# -*- coding: utf-8 -*-
"""规格段落卡检查点（A 模式）——把 docs/content-growth-loop.md §十二 的流程固化下来。

用法：D:\python\python.exe scripts/checkpoint_specs.py [--land]
  不带 --land：只审计（dry-run + 字数），报告哪些可落、哪些要作废。
  带 --land：审计通过的批次按 §十二 五步落地（重分配 id -> 查重 -> apply -> rebuild -> validate
            -> commit -> push -> 线上验收 -> 归档）。

设计原则：**审计失败即阻断**（绝不出现"审计崩了但照落"）。
"""
import io, json, os, re, subprocess, sys, time, urllib.request

W = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PY = r"D:\python\python.exe"
GIT = r"D:\Dev\Git\cmd\git.exe"
S = os.path.join(W, "local_working_copy", "subagent-specs")
LOC = os.path.join(W, "local_working_copy", "fulltext", "card-locators.jsonl")
TOOL = os.path.join(W, "scripts", "new_cards_from_spec.py")
LAND = "--land" in sys.argv


def sh(args, cwd=W):
    r = subprocess.run(args, cwd=cwd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    return r.returncode, (r.stdout or "") + (r.stderr or "")


def max_id():
    mx = 0
    for n in os.listdir(os.path.join(W, "cards")):
        m = re.match(r"^sk-(\d+)(?:-.*)?\.md$", n)
        if m:
            mx = max(mx, int(m.group(1)))
    return mx


def carded():
    out = set()
    for ln in io.open(LOC, encoding="utf-8"):
        if ln.strip():
            d = json.loads(ln)
            if d.get("section"):
                out.add((str(d.get("book")), str(d.get("section"))))
    return out


def move_to(sub, *paths):
    d = os.path.join(S, sub)
    os.makedirs(d, exist_ok=True)
    for p in paths:
        if os.path.exists(p):
            os.replace(p, os.path.join(d, os.path.basename(p)))


def try_push(tries=3):
    """推送（带重试）。返回 (成功?, 未推送提交数, 最后错误)。"""
    err = ""
    for _ in range(tries):
        code, out = sh([GIT, "push"])
        if code == 0:
            break
        err = out.strip().splitlines()[-1][:160] if out.strip() else "push 失败"
        time.sleep(10)
    code, out = sh([GIT, "log", "--oneline", "origin/master..HEAD"])
    n = len([l for l in out.splitlines() if l.strip()])
    return (n == 0), n, err


def quote_bad_items(specpath):
    """返回与已有卡片 Excerpt 有 12 字窗重叠的条目 id 列表（空 = 干净）。
    用 marker 定位 unit、按 quote_from/quote_to 切片（与产卡工具同一套算法）。"""
    import sqlite3
    try:
        items = json.load(io.open(specpath, encoding="utf-8"))
    except Exception:
        return -1
    old = []
    cd = os.path.join(W, "cards")
    for fn in os.listdir(cd):
        if fn.endswith(".md"):
            for ln in io.open(os.path.join(cd, fn), encoding="utf-8", errors="replace"):
                if ln.startswith(">"):
                    old.append(ln)
    oldtext = re.sub(r"\s+", "", "".join(old))
    oldset = set(oldtext[i:i + 12] for i in range(max(0, len(oldtext) - 11)))
    conn = sqlite3.connect(os.path.join(W, "local_working_copy", "fulltext", "corpus.db"))
    conn.row_factory = sqlite3.Row
    bad = []
    for it in items:
        hits = list(conn.execute("SELECT text FROM units WHERE book=? AND text LIKE ?",
                                 (it.get("book"), "%" + str(it.get("marker")) + "%")))
        if len(hits) != 1:
            return -1
        t = re.sub(r"\s+", "", hits[0]["text"] or "")
        # 2026-10-10 修：规格里 quote_from/quote_to 可能是 **null**（不是缺失），
        # 直接 .find(None) 会 TypeError。这里对齐产卡工具的判空逻辑：
        # 无 quote_from -> 整 unit 就是引文；有 quote_from 但找不到 quote_to -> 视为不可判（-1）。
        qf = str(it.get("quote_from") or "")
        qt = str(it.get("quote_to") or "")
        if qf:
            i = t.find(qf)
            j = t.find(qt, i) if qt else -1
            if i < 0 or j < 0:
                return -1
            q = t[i:j + len(qt)]
        else:
            q = t
        sh = set(q[k:k + 12] for k in range(max(0, len(q) - 11)))
        if sh & oldset:
            bad.append(str(it.get("id")))
    return bad


def main():
    # 0) 先补推：上轮可能因网络失败留下未推送提交（实测 2026-10-03 TLS 断链）
    ok, n, err = try_push()
    if n:
        print("!! 仍有 %d 个未推送提交（push 失败：%s）" % (n, err))
        print("   -> 本地提交安全，但线上未更新。**请检查代理/VPN**（到 github.com 的 TLS 不通）。")
    elif ok:
        print("(无未推送提交或已补推成功)")
    pend = sorted([f for f in os.listdir(S) if f.endswith(".json") and f.startswith("batch")])
    print("待处理规格：%d 个" % len(pend))
    if not pend:
        print("无新规格 -> 本轮不落卡")
        return 0
    CARDED = carded()
    ready, void, dup = [], [], 0
    for fn in pend:
        p = os.path.join(S, fn)
        code, out = sh([PY, TOOL, os.path.relpath(p, W)])
        lens = [int(x) for x in re.findall(r"｜(\d+) 字｜", out)]
        bad = [n for n in lens if n < 90 or n > 250]
        items = []
        try:
            data = json.load(io.open(p, encoding="utf-8"))
            if isinstance(data, list): items = data
        except Exception:
            pass
        key = (str(items[0].get("book")), str(items[0].get("section"))) if items else ("", "")
        print("  %-58s exit=%d 条=%d 越界=%d" % (fn[:58], code, len(lens), len(bad)))
        if code != 0 or bad or not lens:
            note = os.path.join(S, "_void", fn + ".VOID.md")
            os.makedirs(os.path.join(S, "_void"), exist_ok=True)
            io.open(note, "w", encoding="utf-8", newline="\n").write(
                "# 作废（检查点自动判定）\n\ndry-run exit=%d｜字数越界 %s\n\n%s\n" % (code, bad, out.strip()[-800:]))
            void.append(fn)
            continue
        # 章级【只警告】。2026-10-08 起不再拦截：§十四 实测章级缺口已耗尽
        # （134 个值得成卡的章里 132 个都有卡），长尾全在已产卡的章里 —— 章级拦截会把唯一的价值来源挡掉。
        if key in CARDED:
            print("     （提示：该章已有卡；按 §十四 不拦截，改看引文级重叠）")
        # 引文级查重（**真正的门**）：新引文与已有卡片 Excerpt 的 12 字窗不得重叠
        bad_ids = quote_bad_items(p)
        if bad_ids:
            # 逐条剔（2026-10-11）：长尾期整批退会白丢好卡；剔掉重叠条目，>=3 条仍落
            keep = [x for x in items if str(x.get("id")) not in bad_ids]
            print("     -> 引文级重叠 %d 条（%s）；逐条剔除后剩 %d 条" % (len(bad_ids), ",".join(bad_ids), len(keep)))
            if len(keep) < 3:
                print("        剩余不足 3 条，本批不落")
                # 只有"整批退"才归档到 _void（2026-10-10 补）：否则同一批每轮都会被重审一次
                os.makedirs(os.path.join(S, "_void"), exist_ok=True)
                with io.open(os.path.join(S, "_void", fn + ".VOID.md"), "w", encoding="utf-8", newline=chr(10)) as fh:
                    fh.write("# 引文级查重未过（自动）" + chr(10) + chr(10) +
                             "重叠条目 %d 条（%s）；逐条剔除后不足 3 条 -> 本批不落。" % (len(bad_ids), ",".join(bad_ids)) + chr(10))
                move_to("_void", p)
                dup += 1
                continue
            io.open(p, "w", encoding="utf-8", newline=chr(10)).write(json.dumps(keep, ensure_ascii=False, indent=1))
            items = keep
        ready.append((fn, p, items))
    if not LAND:
        print("\n审计结论：可落 %d｜作废 %d｜章节重复 %d（未加 --land，不改仓库）" % (len(ready), len(void), dup))
        return 0
    if not ready:
        print("\n无可落批次。")
        return 0
    # --- 落地：先统一重分配 id（避免跨批撞车，见 §十一）---
    nxt = max_id() + 1
    first_ids = []
    for fn, p, items in ready:
        for it in items:
            it["id"] = "sk-%d" % nxt
            nxt += 1
        io.open(p, "w", encoding="utf-8", newline="\n").write(json.dumps(items, ensure_ascii=False, indent=1))
        first_ids.append((fn, len(items)))
    print("\n重分配 id 后开始落卡，共 %d 张" % sum(n for _, n in first_ids))
    for fn, p, items in ready:
        code, out = sh([PY, TOOL, os.path.relpath(p, W), "--apply"])
        print("  apply %s -> exit=%d" % (fn[:40], code))
        if code != 0:
            print("  **apply 失败，中止**：" + out[-300:])
            return 1
    code, out = sh([PY, os.path.join(W, "scripts", "rebuild_index.py")])
    print("  rebuild: " + out.strip().splitlines()[-1][:80] if out.strip() else "  rebuild: ?")
    code, out = sh([PY, os.path.join(W, "scripts", "validate_all.py")])
    tail = [l for l in out.strip().splitlines() if l.strip()][-2:]
    print("  validate_all: " + " / ".join(t.strip()[:40] for t in tail))
    if "ALL OK" not in out:
        print("  **validate_all 未通过，中止（未提交）**")
        return 1
    msg = "落卡 %d 张（规格段检查点自动落）：审计通过" % sum(n for _, n in first_ids)
    sh([GIT, "add", "cards/", "classification.json", "INDEX.md", "web/", "docs/"])
    code, out = sh([GIT, "-c", "i18n.commitEncoding=utf-8", "commit", "-q", "-m", msg])
    code, out = sh([GIT, "log", "--oneline", "-1"])
    print("  提交：" + out.strip()[:90])
    ok, n, err = try_push()
    if not ok:
        print("  **PUSH FAILED**：未推送 %d 个提交｜%s" % (n, err))
        print("  本地提交已生成（不会丢），但**线上未更新**；下次检查点会自动补推。")
    else:
        print("  push ok")
    for fn, p, items in ready:
        move_to("_landed", p, p.replace(".json", ".NOTE.md"))
    print("  已归档 _landed/")
    # 线上验收
    time.sleep(110)
    base = "https://craeatzeven.github.io/sukhomlinsky-education-kb/web/data/"
    live = None
    for _ in range(3):
        try:
            ids = json.loads(urllib.request.urlopen(base + "ids.json", timeout=40).read().decode("utf-8"))
            live = len(ids)
            break
        except Exception as e:
            err = str(e)[:90]
            time.sleep(12)
    if live is None:
        print("  **线上验收失败**（网络）：%s —— 与推送失败同源，**不是站点问题**。" % err)
        return 1
    print("  线上 ids：%d" % live)
    local = len([f for f in os.listdir(os.path.join(W, "cards")) if re.match(r"^sk-.*\.md$", f)])
    print("  本地卡数：%d｜一致：%s" % (local, live == local))
    return 0 if live == local else 1


if __name__ == "__main__":
    sys.exit(main())