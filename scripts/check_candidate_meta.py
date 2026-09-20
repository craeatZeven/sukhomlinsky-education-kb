# -*- coding: utf-8 -*-
"""候选卡 frontmatter 完整性体检。

为什么需要它
------------
写批量修卡脚本时，正则写错一个括号就会**静默毁掉字段**。实测过一次：
    re.sub(r"^origin: (.+)$", lambda m: m.group(1) + chr(10) + "ocr_fixes: ...", t)
括号写在了冒号后面，于是替换结果里 `origin: ` 前缀整个没了 —— 卡片还能读、
闸门也照过，因为没人检查「键还在不在」。4 张卡这么坏的。

体检项：
  1. 必备键是否都在；
  2. value 里有没有「没有键名的裸行」（丢前缀的字段就长这样）；
  3. 已知留空是允许的（primary/topics 缺失按项目约定另行登记），所以只报不判死。

用法：
    D:\\python\\python.exe scripts/check_candidate_meta.py
    D:\\python\\python.exe scripts/check_candidate_meta.py --dir <目录>
退出码：0 = 无「丢键名的裸行」；1 = 有。
"""
import argparse, glob, io, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAND_ROOT = os.path.join(ROOT, "local_working_copy", "card-candidates")
NEED = ["status", "type", "title", "source", "primary", "topics", "ref", "origin", "todo"]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", default=None)
    args = ap.parse_args()
    dirs = [args.dir] if args.dir else sorted(
        d for d in glob.glob(os.path.join(CAND_ROOT, "*")) if os.path.isdir(d))
    missing, orphan, total = {}, [], 0
    for d in dirs:
        for f in sorted(glob.glob(os.path.join(d, "cand-*.md"))):
            total += 1
            cid = "%s/%s" % (os.path.basename(d), os.path.basename(f)[:-3])
            t = io.open(f, encoding="utf-8").read()
            if t.count("---") < 2:
                orphan.append((cid, "没有 frontmatter 分隔线"))
                continue
            fm = t.split("---", 2)[1]
            keys = set(re.findall(r"^([A-Za-z_]+):", fm, re.M))
            for k in NEED:
                if k not in keys:
                    missing.setdefault(k, []).append(cid)
            for ln in fm.split(chr(10)):
                s = ln.strip()
                if s and not re.match(r"^[A-Za-z_]+:", s) and not s.startswith(("-", "[")):
                    orphan.append((cid, s[:40]))
    print("体检候选卡：%d 张" % total)
    for k in NEED:
        if missing.get(k):
            print("  缺字段 %-9s %d 张：%s" % (k, len(missing[k]), missing[k][:8]))
    print("★ 丢了键名的裸行（字段前缀被破坏）：%d 处" % len(orphan))
    for cid, s in orphan:
        print("     ! %s  %s" % (cid, s))
    print("结论：%s" % ("PASS" if not orphan else "FAIL"))
    return 1 if orphan else 0


if __name__ == "__main__":
    sys.exit(main())