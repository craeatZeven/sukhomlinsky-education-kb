# -*- coding: utf-8 -*-
"""把 12 条待复核项做成**单文件 HTML 复核页**（T0 静态、零依赖、file:// 直接开）。

为什么不是 Markdown
------------------
Markdown 只能读，不能**记录判断**。复核这件事的关键动作是「逐条给结论」，
所以这一页要能做到：勾选 + 写备注 + 一键把结论复制回去。没有后端，
靠 localStorage 存状态、靠剪贴板导出。

设计走「档案层」（AGENTS.md §B）：内容区圆角 0-2px、零阴影、hairline 分隔、
列表一条只放三个信息、元信息等宽 12-13px；引文段用「阅读层」的左边线。

用法：
    D:\\python\\python.exe scripts/build_review_html.py
"""
import io, json, os, re, sqlite3, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))
from check_candidate_fidelity import (cjk_only, strip_heads, declared_pairs,  # noqa: E402
                                      revert_declared, read_origin, local_align, DB)
import audit_excerpt_starts as A  # noqa: E402

D = os.path.join(ROOT, "local_working_copy", "card-candidates", "jiao-yu-zhen-yan-2026-09-20")

# 每条要问的问题与可选项（人话，短）
ASK = {
    # ⚠️ 更正（2026-09-21）：这两条最初写成「用反推的 A19 / 见 primary_source」，
    #    但复核时发现卡里**根本没有 primary_source** —— 当初反推就失败了（选本的出处行有误），
    #    是我把前提记串了。改为按内容判定，判定依据写进卡片的 primary_source。
    "cand-019": ("条目归属当初推不出来（选本出处行有误）。按 SPEC-FOR-JUDGE 按内容判定：本条讲「怎么认识儿童」，属 A6 了解儿童。",
                 ["接受 A6 了解儿童（topics: child-study）", "改判 A5（规范教育者的态度与行为）", "待查纸本"]),
    "cand-192": ("条目归属当初推不出来（选本出处行有误）。按 SPEC-FOR-JUDGE 按内容判定：本条讲第一教育关系，属 A8 家庭与母亲。",
                 ["接受 A8 家庭与母亲（topics: family-school / love-education）", "我指定另一个条目（写在备注里）", "待查纸本"]),
    "cand-156": ("选集作「美一—乃是善良和热忱之母，」，校勘后作「美——乃是善良和热忱之母。」",
                 ["接受校勘后的写法", "改回选集原样（保留错字）", "待查纸本"]),
    "cand-010": ("书里有「关于教育道德的一封信」这几个字，卡里没有 —— 它是选集里那封信的标题，摘引时跳过了。",
                 ["接受（标题不进引文）", "把标题也写进引文", "待查纸本"]),
    "cand-087": ("书作「不使：-本坏书」，校勘后作「不使一本坏书」；对齐边界正好落在这处改动的缝上。",
                 ["接受（差额由我的校勘解释）", "改回选集原样", "待查纸本"]),
    "cand-093": ("书作「创造的：一切」「白已」，校勘后作「创造的一切」「自己」；边界落在两处改动的缝上。",
                 ["接受（差额由我的校勘解释）", "改回选集原样", "待查纸本"]),
    "cand-201": ("书作「…培养真正的人|养人…」，按声明剔掉分隔符时还带掉一个「养」。",
                 ["接受（那个「养」是书里的重复字，不该留）", "把「养」补回引文", "待查纸本"]),
    "cand-042": ("卡片抄的是《教育箴言》的措辞（选本对原句做过节缩），在选集里对不上 —— 不算验过。",
                 ["接受（引文按选本措辞，标注来源即可）", "改成选集原句", "待查纸本"]),
    "cand-154": ("全句一句；选集作「美是入的道德财富的源泉。」，「入」是 OCR 错字，卡片作「人」。",
                 ["接受（人）", "改回选集原样（入）", "待查纸本"]),
    "cand-173": ("卡片抄的是《教育箴言》的措辞；校勘过「一个入→一个人」。",
                 ["接受", "改成选集原句", "待查纸本"]),
    "cand-032": ("卡片从「…正是这种错误所致」处起引，起点前还挂着 15 字（「而学校教育发生的许多灾难，正是」）。",
                 ["接受这个摘引起点", "向前补到句首", "待查纸本"]),
}
# 2026-09-21 人工已决（全取第一个选项）—— 让这一页变成**记录**，不只是问卷
DECIDED = {
    "cand-019": "接受 A6 了解儿童",
    "cand-192": "接受 A8 家庭与母亲",
    "cand-156": "接受校勘后的写法",
    "cand-010": "接受：标题不进引文",
    "cand-087": "接受：差额由校勘解释",
    "cand-093": "接受：差额由校勘解释",
    "cand-201": "接受：重复字不留",
    "cand-042": "接受：引文按选本措辞",
    "cand-154": "接受：人",
    "cand-173": "接受：引文按选本措辞",
    "cand-032": "接受这个摘引起点",
}
KIND_ORDER = ["字段缺失", "对不上选集（WARN）", "书里有而卡里没有（GAP）",
              "只在选本里对上（自证）", "起点需人工判断（长悬挂）", "起点定位不到"]


def gather():
    fid = json.load(io.open(os.path.join(D, "fidelity.json"), encoding="utf-8"))
    sta = json.load(io.open(os.path.join(D, "start-audit.json"), encoding="utf-8"))
    items, seen = [], {}

    def add(cid, kind, why):
        c = cid.split("/")[-1]
        if (c, kind) in seen:
            return
        seen[(c, kind)] = True
        items.append({"id": c, "kind": kind, "why": why})

    for cid, why in fid.get("fail", []):
        add(cid, "删掉正文（FAIL）", why)
    for cid, why in fid.get("warn", []):
        add(cid, "对不上选集（WARN）", why)
    for cid, why in fid.get("gap", []):
        add(cid, "书里有而卡里没有（GAP）", why)
    for cid, why in fid.get("circular", []):
        add(cid, "只在选本里对上（自证）", why)
    for cid, dl, cut in sta.get("manual", []):
        add(cid, "起点需人工判断（长悬挂）", "起点前还挂着 %d 字：…%s" % (dl, cut))
    for cid in sta.get("unlocated", []):
        add(cid, "起点定位不到", "卡文开头 20 字在选集里找不到")
    # 字段缺失
    for f in sorted(os.listdir(D)):
        if not f.startswith("cand-") or not f.endswith(".md"):
            continue
        t = io.open(os.path.join(D, f), encoding="utf-8").read()
        fm = t.split("---", 2)[1]
        miss = [k for k in ("primary", "topics") if not re.search(r"^%s:" % k, fm, re.M)]
        if miss:
            add(f[:-3], "字段缺失", "缺 " + "、".join(miss))

    # 组装证据
    conn = sqlite3.connect(DB)
    HAY = {}
    for v in ("1", "2", "3", "4", "5"):
        pat = "%第" + v + "卷%"
        for row in conn.execute("SELECT DISTINCT volume FROM units WHERE book LIKE ? AND volume LIKE ?",
                                ("%选集%", pat)):
            hayp, idx = A.build_hay(conn, "WHERE book LIKE '%选集%' AND volume = '" + row[0] + "'")
            HAY[v] = (hayp, "".join(hayp[i] for i in idx))
    out = []
    for it in items:
        p = os.path.join(D, it["id"] + ".md")
        t = io.open(p, encoding="utf-8").read()
        fm = t.split("---", 2)[1]
        quote, vol = read_origin(p)
        it["quote"] = re.sub(r"\s+", "", quote)
        rec = []
        for k in ("ocr_fixes", "excerpt_note", "ocr_note", "truncated_note", "primary_source", "todo"):
            m = re.search(r"^%s: (.+)$" % k, fm, re.M)
            if m:
                rec.append({"k": k, "v": m.group(1)})
        it["record"] = rec
        it["short"] = (re.search(r'^title_short: "(.+)"$', fm, re.M) or [None, ""])[1]
        it["primary"] = (re.search(r"^primary: (\S+)", fm, re.M) or [None, "（缺）"])[1]
        it["ref"] = (re.search(r"^ref: (.+)$", fm, re.M) or [None, ""])[1]
        # 书里的对应文字
        book = ""
        if str(vol) in HAY:
            hayp, cjk = HAY[str(vol)]
            n = cjk_only(quote)
            n_rev = revert_declared(n, declared_pairs(t))
            r, missing, seg = local_align(n_rev, cjk, 0.90)
            if seg:
                k = cjk.find(seg)
                book = hayp[max(0, k - 40): k + len(seg) + 40] if k >= 0 else seg
                it["missing"] = missing or []
            else:
                it["missing"] = []
        it["book"] = book
        q = ASK.get(it["id"])
        it["ask"] = q[0] if q else "（这一类未预置问题 —— 照 why 判断即可）"
        it["options"] = q[1] if q else ["接受", "需修改（写在备注里）", "待查纸本"]
        it["decided"] = DECIDED.get(it["id"], "")
        out.append(it)
    out.sort(key=lambda x: (KIND_ORDER.index(x["kind"]) if x["kind"] in KIND_ORDER else 99, x["id"]))
    return out


CSS = """
:root{--paper:#f7f5f1;--ink:#1b1815;--sub:#6b645a;--line:#ddd7cc;--accent:#a84a22;--ok:#2f6b40}
*{box-sizing:border-box}
body{margin:0;background:var(--paper);color:var(--ink);
 font:16px/1.75 -apple-system,BlinkMacSystemFont,"Segoe UI","Noto Sans CJK SC","Microsoft YaHei",sans-serif}
header{padding:34px 28px 18px;border-bottom:1px solid var(--line)}
h1{margin:0 0 6px;font-size:22px;letter-spacing:.01em}
.sub{color:var(--sub);font-size:13px}
.bar{position:sticky;top:0;z-index:5;background:rgba(247,245,241,.94);
 backdrop-filter:blur(8px);border-bottom:1px solid var(--line);padding:10px 28px;
 display:flex;gap:14px;align-items:center;flex-wrap:wrap}
.bar b{font-variant-numeric:tabular-nums}
button{font:inherit;font-size:13px;padding:5px 12px;border:1px solid var(--line);
 background:#fff;color:var(--ink);border-radius:2px;cursor:pointer}
button:hover{border-color:var(--accent);color:var(--accent)}
button.primary{background:var(--accent);border-color:var(--accent);color:#fff}
button.primary:hover{color:#fff;opacity:.92}
main{max-width:960px;margin:0 auto;padding:8px 28px 80px}
.item{border-bottom:1px solid var(--line);padding:22px 0}
.head{display:flex;gap:12px;align-items:baseline;flex-wrap:wrap}
.cid{font:13px/1 ui-monospace,SFMono-Regular,Consolas,monospace;color:var(--sub);letter-spacing:.02em}
.kind{font-size:12px;letter-spacing:.04em;color:var(--accent);border:1px solid var(--line);
 padding:1px 7px;border-radius:2px;background:#fff}
.done .kind{color:var(--ok);border-color:var(--ok)}
h2{font-size:17px;margin:10px 0 2px}
p{margin:8px 0}
.quote{border-left:3px solid var(--line);padding:2px 30px 2px 18px;margin:12px 0;
 max-width:44em;color:#2a2521}
.book{font:13px/1.7 ui-monospace,SFMono-Regular,Consolas,monospace;color:var(--sub);
 white-space:pre-wrap;word-break:break-word}
mark{background:#f3e2c8;color:inherit;padding:0 2px}
.meta{font:12.5px/1.7 ui-monospace,SFMono-Regular,Consolas,monospace;color:var(--sub);
 white-space:pre-wrap;word-break:break-word}
.ask{margin:14px 0 6px;padding-left:12px;border-left:3px solid var(--accent)}
.opts{display:flex;flex-direction:column;gap:6px;margin:8px 0}
label.opt{display:flex;gap:9px;align-items:flex-start;font-size:14.5px;cursor:pointer}
textarea{width:100%;min-height:52px;font:14px/1.6 inherit;padding:7px 9px;border:1px solid var(--line);
 border-radius:2px;background:#fff;color:var(--ink);resize:vertical}
.detail{margin-top:10px}
summary{cursor:pointer;font-size:13px;color:var(--sub)}
.tip{background:#fff;border:1px solid var(--line);border-radius:2px;padding:12px 14px;margin:16px 0;
 font-size:14px}
code{font:13px/1.6 ui-monospace,SFMono-Regular,Consolas,monospace;background:#fff;
 border:1px solid var(--line);padding:1px 5px;border-radius:2px}
footer{color:var(--sub);font-size:12.5px;padding:20px 28px 40px;border-top:1px solid var(--line)}
"""

JS = """
const KEY='kb-review-12';
const state=JSON.parse(localStorage.getItem(KEY)||'{}');
function paint(){
  let done=0;
  document.querySelectorAll('.item').forEach(el=>{
    const id=el.dataset.id, s=state[id]||{};
    el.classList.toggle('done',!!s.choice);
    if(s.choice) done++;
    const ta=el.querySelector('textarea'); if(ta && ta.value!==(s.note||'')) ta.value=s.note||'';
    el.querySelectorAll('input[type=radio]').forEach(r=>{r.checked=(s.choice===r.value)});
  });
  document.getElementById('cnt').textContent=done;
}
function bind(){
  document.querySelectorAll('.item').forEach(el=>{
    const id=el.dataset.id;
    el.querySelectorAll('input[type=radio]').forEach(r=>r.addEventListener('change',()=>{
      state[id]=state[id]||{}; state[id].choice=r.value; save();}));
    const ta=el.querySelector('textarea');
    if(ta) ta.addEventListener('input',()=>{state[id]=state[id]||{}; state[id].note=ta.value; save();});
  });
}
function save(){localStorage.setItem(KEY,JSON.stringify(state));paint();}
function exportText(){
  const lines=['复核结论（12 条）—— 生成于 '+new Date().toLocaleString(),''];
  document.querySelectorAll('.item').forEach(el=>{
    const id=el.dataset.id, s=state[id]||{};
    lines.push(id+'  '+(s.choice?('【'+s.choice+'】'):'【未决】')+(s.note?('  备注：'+s.note):''));
  });
  const t=lines.join('\n');
  navigator.clipboard.writeText(t).then(()=>{
    const b=document.getElementById('cp'); b.textContent='已复制 ✓'; setTimeout(()=>b.textContent='复制结论',1600);
  }).catch(()=>{ window.prompt('手动复制：',t); });
}
"""


def esc(s):
    return (s or "").replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def main():
    items = gather()
    parts = ["<!DOCTYPE html>", '<html lang="zh-CN">', "<head>", '<meta charset="utf-8">',
             '<meta name="viewport" content="width=device-width,initial-scale=1">',
             "<title>候选卡复核清单 · 12 条</title>", "<style>" + CSS + "</style>", "</head>", "<body>",
             "<header>", "<h1>候选卡复核清单 · 12 条</h1>",
             '<div class="sub">《教育箴言》候选卡 202 张，其中 <b>190 张</b>已由三道闸门放行；'
             '另有 <b>12 条</b>机器判不了，已于 <b>2026-09-21 全部给出结论</b>（全取第一个选项），'
             '结论已写进各卡片的 <code>review_note</code>。'
             '其中「字段缺失」两条（cand-019/192）在处理后已补齐，故本页现在只列剩下的 10 条。'
             '本页保留作记录：每条都标了当时的问题与最终选择。</div>',
             "</header>",
             '<div class="bar"><span>已决 <b id="cnt">0</b> / %d</span>'
             '<button id="cp" class="primary" onclick="exportText()">复制结论</button>'
             '<button onclick="if(confirm(\'清空本页所有勾选与备注？\')){localStorage.removeItem(KEY);location.reload()}">清空</button>'
             "</div>" % len(items), "<main>"]
    for it in items:
        opts = "".join(
            '<label class="opt"><input type="radio" name="%s" value="%s"><span>%s</span></label>'
            % (it["id"], esc(o), esc(o)) for o in it["options"])
        rec = "\n".join("%s: %s" % (r["k"], r["v"]) for r in it["record"]) or "（这张卡没有修法/备注字段）"
        parts += ['<section class="item" data-id="%s">' % it["id"],
                  '<div class="head"><span class="cid">%s</span><span class="kind">%s</span>'
                  '<span class="sub">%s · %s</span></div>'
                  % (it["id"], esc(it["kind"]), esc(it["primary"]), esc(it["short"])),
                  "<h2>%s</h2>" % esc(it["why"]),
                  '<p class="sub">%s</p>' % esc(it["ref"]),
                  '<div class="quote">%s</div>' % esc(it["quote"])]
        if it.get("book"):
            parts.append('<details class="detail"><summary>书里对应的原文（对照用）</summary>'
                         '<p class="book">%s</p></details>' % esc(it["book"]))
        parts.append('<details class="detail"><summary>卡片自己的记录</summary><p class="meta">%s</p></details>'
                     % esc(rec))
        parts += ['<div class="ask">%s</div>' % esc(it["ask"])]
        if it.get("decided"):
            parts.append('<p class="sub">✅ 2026-09-21 已决：%s</p>' % esc(it["decided"]))
        parts += ['<div class="opts">%s</div>' % opts,
                  '<textarea placeholder="备注（可选）：写清你选的条目码、或要改成什么"></textarea>',
                  "</section>"]
    parts += ["</main>",
              '<footer>页面由 <code>scripts/build_review_html.py</code> 生成 · 结论存在本机 localStorage · '
              '不改动任何卡片文件</footer>',
              "<script>" + JS + "</script>", "</body>", "</html>"]
    out = os.path.join(D, "REVIEW.html")
    io.open(out, "w", encoding="utf-8", newline="\n").write("\n".join(parts))
    print("写好了：%s（%d 条 · %d KB）" % (out, len(items), os.path.getsize(out) // 1024))


if __name__ == "__main__":
    main()
