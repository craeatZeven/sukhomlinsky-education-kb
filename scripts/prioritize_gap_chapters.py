# -*- coding: utf-8 -*-
"""缺口章优先级：用可测代理剔除「不值得成卡」的章。

判据（都可机检，不靠印象）：
  1) 非正文：章名含 注释/前言/序/目录/附录/编后/译后/版权/书名/目 次
  2) 他人评述：章开头 3 个 unit 内出现「著」类署名行（例：「阿·泽韦林著」）
  3) 论断密度低：含 我认为/应该/必须/不能/正是/意味着/首先/教育者 等词的 unit 占比 < 15%
     —— 这类章几乎全是课程描述、设备清单、叙事，成卡价值低
其余按「未被引用的 unit 数 × 论断密度」排序。
"""
import sqlite3, io, json, os, re, collections
# 2026-10-01：原来写死 D:\Git\sukhomlinsky-education-kb，仓库搬到 D:\Work 后整脚本报
# 「unable to open database file」（会被误判成"数据库丢了"）。改成从 __file__ 推，搬目录不再失效。
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
c = sqlite3.connect(os.path.join(ROOT, "local_working_copy", "fulltext", "corpus.db")); c.row_factory = sqlite3.Row
loc = [json.loads(x) for x in io.open(os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl"), encoding="utf-8") if x.strip()]
ALIAS = {"xuan-ji-zh-vol1":"选集（五卷本）第1卷","xuan-ji-zh-vol2":"选集(五卷本)第2卷","xuan-ji-zh-vol3":"选集（五卷本）第3卷",
         "xuan-ji-zh-vol4":"选集(五卷本)第4卷","xuan-ji-zh-vol5":"选集（五卷本）第5卷","zuo-ren-de-gu-shi-zh":"做人的故事",
         "gei-jiao-shi-de-jian-yi-zh":"给教师的建议","ba-xin-xian-gei-hai-zi-zh":"ba-xin-xian-gei-hai-zi-zh"}
cited = collections.defaultdict(set)
for r in loc:
    if r.get("unit"): cited[str(r.get("book"))].add(r["unit"])
NONCONTENT = re.compile(r"注释|前 ?言|目录|目 ?次|附录|编后|译后|版权|书名|扉页|序 ?言|出版说明")
# **实测不可成卡的章**（不是靠印象，是子代理逐 unit 数过之后回报的）。
# 判据：该章绝大多数 unit 是图窗说明 / 陈列清单 / 标语牌文字，作者本人的论断句极少。
# 放进这里，是为了让后续批次**不再把配额浪费在这些章上**。
NOT_CARDABLE = {
    "校舍内部陈设的教育作用":
        "260 unit 里 225 个 <90 字（主体是图窗说明/陈列清单/标语牌）；≥90 字的 35 个里 32 个是叙事/清单/标语，"
        "真论断仅 2 条（2026-09-27 子代理实测，该批实出 2 张、拒绝凑数）",
    "苏联杰出的教育家": "他人评述（署名行「阿·泽韦林著」）",
}
CLAIM = re.compile(r"我认为|我坚信|我深信|应该|必须|不能|正是|意味着|首先|教育者|教师应")
AUTHORSIGN = re.compile(r"著$|著[，,。]|（著）|编著")
rows = []
for slug, book in ALIAS.items():
    hit = cited.get(slug, set())
    us = list(c.execute("SELECT unit_id, section, text FROM units WHERE book=? ORDER BY unit_id", (book,)))
    by = collections.defaultdict(list)
    for u in us:
        by[u["section"] or "（无节名）"].append(u)
    for sec, lst in by.items():
        if len(lst) < 30: continue
        h = sum(1 for u in lst if u["unit_id"] in hit)
        if h > max(1, len(lst)//20): continue
        reason = NOT_CARDABLE.get(sec)
        if reason:
            rows.append((len(lst) - h, 0.0, book, sec, len(lst), h, "实测不可成卡：" + reason[:28]))
            continue
        if NONCONTENT.search(sec): reason = "非正文"
        else:
            head = [re.sub(r"\s+","",u["text"] or "") for u in lst[:3]]
            if any(len(x) < 24 and AUTHORSIGN.search(x) for x in head): reason = "他人评述（署名行）"
        tot = len(lst)
        dens = sum(1 for u in lst if CLAIM.search(re.sub(r"\s+","",u["text"] or ""))) / float(tot)
        if not reason and dens < 0.15: reason = "论断密度低（%.0f%%）" % (dens*100)
        rows.append((tot - h, dens, book, sec, tot, h, reason))
good = [r for r in rows if not r[6]]
bad = [r for r in rows if r[6]]
good.sort(key=lambda r: -r[0]*r[1])

# --- 排除「已产卡」的章（2026-10-02 加）---
# 问题：优先级表包含已产过卡的章（如 vol1《(4)集体和个人的精神生活》缺口 108 但其实已有卡），
# 规格段只能每次自己再筛，结果就是连续多批落到同一本书上（实测连续 3 批《给教师的建议》）。
# 做法：从 card-locators.jsonl 取「已产卡的 (book, section)」，直接从清单里去掉，让 Top 列表 = 真正还没做的。
# 2026-10-08 修正（子代理实测指出）：locators 里的 book 多为 slug（如 xuan-ji-zh-vol2），
# 而清单行的 book 是 ALIAS 解析后的全名（如 选集(五卷本)第2卷）——直接比**永不相等**，
# 于是「剔除已产卡章」完全失效（旧卡所在章一个都剔不掉）。比较前必须归一化。
def _norm_book(b):
    b = str(b)
    for _slug, _full in ALIAS.items():
        if b == _slug or b == _full:
            return _full
    return b


CARDED = set()
for _r in loc:
    if _r.get("section"):
        CARDED.add((_norm_book(_r.get("book")), str(_r.get("section"))))
_done = [r for r in good if (r[2], r[3]) in CARDED]
good = [r for r in good if (r[2], r[3]) not in CARDED]
print("=== 已产卡过滤：剔除 %d 个已产过卡的章，剩 %d 个真·待补章" % (len(_done), len(good)))
print()
# --- 选章轮换约束（2026-10-02 加，用户要求）---
# 问题：按优先级纯排序会「偏食」——实测连续 4 批都在做《给教师的建议》。
# 做法：看最近几批规格用的哪本书；若最近 2 批同书，就把「换一本、且优先级最高」的章提到最前。
# 生效方式：规格段每次都读本脚本的输出，所以约束自动作用于它的选章，不必改卡 prompt（卡执行后已冻结）。
SPEC_DIR = os.path.join(ROOT, "local_working_copy", "subagent-specs")
def _recent_books(n=4):
    items = []
    for sub in ("_landed", "_void"):
        d = os.path.join(SPEC_DIR, sub)
        if not os.path.isdir(d): continue
        for fn in os.listdir(d):
            if fn.endswith(".json"):
                p = os.path.join(d, fn)
                items.append((os.path.getmtime(p), p))
    items.sort(reverse=True)
    out = []
    for _, p in items[:n]:
        try:
            it = json.load(io.open(p, encoding="utf-8"))
            if isinstance(it, list) and it: out.append(str(it[0].get("book")))
        except Exception: pass
    return out
# ---- 2026-10-17：主题均衡排序（薄主题优先）----
# 起因：原排序是「缺口 × 论断密度」，结果全落在已经很厚的主题上；
# 实测 love-education 803 张 ↔ health-first 107 张，差距 7.5 倍。
# 做法：按「该章已有卡的主题」给章加权，主题越薄权重越高（开方，避免过度倾斜）。
def _topic_balance():
    import collections as _c
    tp_counts = _c.Counter()
    chap_tp = _c.defaultdict(_c.Counter)
    topics_of = {}
    cards_dir = os.path.join(ROOT, "cards")
    if os.path.isdir(cards_dir):
        for fn in os.listdir(cards_dir):
            if not (fn.startswith("sk-") and fn.endswith(".md")): continue
            m0 = re.match(r"(sk-\d+)", fn)
            if not m0: continue
            try:
                t = io.open(os.path.join(cards_dir, fn), encoding="utf-8", errors="replace").read()
            except Exception: continue
            m = re.search(r"^topics:\s*$([\s\S]{0,400}?)(?=^[a-z_]+:|\Z)", t, re.M)
            tps = re.findall(r"^\s*-\s*(\S+)", m.group(1), re.M) if m else []
            topics_of[m0.group(1)] = tps
            for x in tps: tp_counts[x] += 1
    locp = os.path.join(ROOT, "local_working_copy", "fulltext", "card-locators.jsonl")
    if os.path.exists(locp):
        for l in io.open(locp, encoding="utf-8"):
            if not l.strip(): continue
            try: rr = json.loads(l)
            except Exception: continue
            for x in topics_of.get(str(rr.get("card")), []):
                chap_tp[(str(rr.get("book")), str(rr.get("section")))][x] += 1
    if not tp_counts: return {}, chap_tp
    mx = max(tp_counts.values())
    return {t: (mx / max(c, 1)) ** 0.5 for t, c in tp_counts.items()}, chap_tp


_tw, _ctp = _topic_balance()
if _tw:
    def _bw(row):
        base = float(row[0]) * float(row[1])
        ct = _ctp.get((row[2], row[3]))
        if not ct: return base
        best = max(ct.items(), key=lambda x: x[1])[0]
        return base * _tw.get(best, 1.0)
    good.sort(key=lambda r: -_bw(r))
    _thin = sorted(_tw, key=lambda k: _tw[k])[:3]
    print("=== 主题均衡排序已启用（薄主题加权 %s…）" % " / ".join(_thin))
    print()


_rb = _recent_books()
_b, _streak = None, 0
for _x in _rb:
    if _b is None: _b, _streak = _x, 1
    elif _x == _b: _streak += 1
    else: break
_switched = ""
if _streak >= 2:
    for _i, _row in enumerate(good):
        if _row[2] != _b:
            good.insert(0, good.pop(_i)); _switched = _row[2] + " / " + _row[3]; break
print("=== 轮换约束：最近 %d 批的书 = %s" % (len(_rb), "｜".join(x[:14] for x in _rb)))
if _streak >= 2:
    print("   连续 %d 批同一本（%s）→ 本轮把「换书且优先级最高」的章提到最前" % (_streak, _b[:16]))
    print("   ★ 本轮建议：%s" % _switched)
else:
    print("   未触发（最近连续同书 %d 批 < 2）→ 仍按优先级排序" % _streak)
print()
print("可补章（值得成卡）：%d｜不值得：%d｜合计 %d" % (len(good), len(bad), len(rows)))
print()

# ---- 2026-10-17：输出「薄主题 -> 建议章」----
# 实测：已产卡过滤后剩余可补章只有 2 个（且不可用），Top 列表基本为空，
# 规格段于是自己乱选章（结果反复落在很厚的主题上）。所以必须把建议直接打出来。
if _tw and _ctp:
    print("=== ★ 本轮建议：按主题均衡补短板（薄主题 → 该主题料最集中的章）")
    _thin_topics = sorted(_tw, key=lambda k: -_tw[k])[:3]
    for _t in _thin_topics:
        # 2026-10-20 修正：只按该主题卡数排序会把「主题只占少数」的章也推出来
        # （实测：vol3《我们怎样学习读和写》被推给 health-first，但该章是识字教学，
        #  105 unit 里 0 条健康证据，连续两批都被子代理判定为 0 张）。
        # 修法：要求该主题至少占该章卡片的 1/3，且该章至少 2 张该主题的卡。
        _cands = []
        for _k in _ctp:
            _n_t = _ctp[_k].get(_t, 0)
            _n_all = sum(_ctp[_k].values())
            if _n_t >= 2 and _n_all > 0 and (_n_t / float(_n_all)) >= 0.34:
                _cands.append((_k[0], _k[1], _n_t, _n_all))
        _cands.sort(key=lambda x: (-x[2], x[3]))
        _hit = []
        for (_b2, _s2, _n2, _a2) in _cands:
            _hit.append("%s《%s》(此主题 %d/%d 卡)" % (_b2[:16], _s2[:26], _n2, _a2))
            if len(_hit) >= 2: break
        print("  主题 %-26s → %s" % (_t, " ｜ ".join(_hit) if _hit else "(该主题暂无已定位的章)"))
    print("  提示：从上面这些章里选「还没取尽的段落」，每主题至多 6 张。")
    print()

print("=== 优先级 Top 24（缺口 × 论断密度）")
for gap, dens, book, sec, tot, h, _ in good[:24]:
    print("   缺口 %4d｜密度 %3.0f%%｜%-20s 《%s》" % (gap, dens*100, book[:20], sec[:34]))
print()
print("=== 剔除示例（前 12）")
for gap, dens, book, sec, tot, h, why in bad[:12]:
    print("   缺口 %4d｜%-28s｜%s" % (gap, sec[:28], why))

# ---- 2026-10-17：自动收口条件 ----
# 目的：让规格段**自己到点停**，不必靠人盯。任一条件满足即在输出末尾打印「不建议再产卡」。
#   ① 12 主题全部 >= 150（主题入口基本不空）
#   ② 连续 5 批产出 <= 1 张（长尾枯竭）
_tcnt = {}
_cdir = os.path.join(ROOT, "cards")
if os.path.isdir(_cdir):
    for _fn in os.listdir(_cdir):
        if not (_fn.startswith("sk-") and _fn.endswith(".md")): continue
        try:
            _tt = io.open(os.path.join(_cdir, _fn), encoding="utf-8", errors="replace").read()
        except Exception:
            continue
        _mm = re.search(r"^topics:\s*$([\s\S]{0,400}?)(?=^[a-z_]+:|\Z)", _tt, re.M)
        for _x in (re.findall(r"^\s*-\s*(\S+)", _mm.group(1), re.M) if _mm else []):
            _tcnt[_x] = _tcnt.get(_x, 0) + 1
_thin2 = dict((k, v) for k, v in _tcnt.items() if v < 150)
_stop = []
if _tcnt and not _thin2:
    _stop.append("12 主题全部 >=150")
_ys = []
for _sub in ("_landed",):
    _dd = os.path.join(SPEC_DIR, _sub)
    if os.path.isdir(_dd):
        for _fn in os.listdir(_dd):
            if _fn.endswith(".json"):
                _pp = os.path.join(_dd, _fn)
                _ys.append((os.path.getmtime(_pp), _pp))
_ys.sort(reverse=True)
_yc = []
for _mt, _pp in _ys[:5]:
    try:
        _it = json.load(io.open(_pp, encoding="utf-8"))
        _yc.append(len(_it) if isinstance(_it, list) else 0)
    except Exception:
        _yc.append(0)
if len(_yc) >= 5 and all(c <= 1 for c in _yc):
    _stop.append("最近 5 批产出均 <=1 张（长尾枯竭）")
print("=== 收口检查（2026-10-17 加）")
if _thin2:
    print("   薄主题（<150）：%s" % " ｜ ".join("%s %d" % (k, v) for k, v in sorted(_thin2.items(), key=lambda x: x[1])))
else:
    print("   12 主题已全部 >=150")
if _stop:
    print()
    print("   ★★ 已达收口条件：%s" % "；".join(_stop))
    print("   → 本轮【不建议再产卡】。请转做收尾：人核引文 / 封库 / 使用侧。")
else:
    print("   未达收口条件 → 继续产出（优先补上面的薄主题）")
