# -*- coding: utf-8 -*-
"""常驻判据：分析页里的**每一条引文**必须能在对应卡片里找到，且出处节对得上。

## 为什么必须有它
第一篇分析写完时，我用一次性脚本把 37 条引文逐条回卡核对，**抓到 2 处真错**：
  · 把「转述段」的措辞标成了「原文」（[[sk-1172]]）
  · 引文里静默纠正了 OCR 错字（原文「儿董」「自已」「第次」，我写成正常字）
那个脚本当时躺在 `local_working_copy/`（gitignored）——**下次写分析就没有它了**。
分析页的全部价值都押在"引文可信"上，所以它必须变成仓库里的常驻判据。

## 它怎么工作（不需要人工维护清单）
分析页的写法本身带了机器可读的出处标注：
    > 「……引文……」（[[sk-1301]] 原文）
    「……引文……」（[[sk-1172]] 转述段）
所以脚本**从页面解析**引文 + 卡号 + 出处节，再回卡核对。以后新写的页面自动被查。

## 判据（每条都能失败）
  ① 引文（按 `……` 切段后）必须能在被引卡片的**该节**里逐字找到
  ② 标了「原文」的，不许只在「转述」里找到（这正是我犯过的错）
  ③ 找不到时**只有一种豁免**：页面显式申报了 OCR 录正（附近出现 "OCR"）——
     「允许按文意录正，但**必须申报**」，不许静默改字
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / 'wiki'
CARDS = ROOT / 'cards'
# 有引文的页面类型：概念页（分析）、对比页、归档问答
SCAN_DIRS = ['concepts', 'comparisons', 'queries']

SEC_LABEL = {          # 页面里写的出处 → 卡片里的小节
    '原文': ['原文/Excerpt', '编者概括'],
    '转述': ['中文转述/说明'],
    '场景': ['教育场景/应用'],
    '标题': ['__TITLE__'],
}
PROBLEMS: list[str] = []
STATS = {'quotes': 0, 'ok': 0, 'ocr': 0, 'nosection': 0}


def card_sections(text: str) -> dict[str, str]:
    out: dict[str, str] = {}
    body = re.sub(r'^---\n.*?\n---\n', '', text, count=1, flags=re.S)
    out['__TITLE__'] = '\n'.join(ln for ln in body.splitlines()
                                 if ln.startswith('# ') and not ln.startswith('## '))
    for name in ('原文/Excerpt', '中文转述/说明', '教育场景/应用', '编者概括'):
        m = re.search(rf'^## {re.escape(name)}\s*$', text, re.M)
        if m:
            s = m.end()
            nxt = re.search(r'^## ', text[s:], re.M)
            out[name] = t2 = text[s:s + nxt.start()] if nxt else text[s:]
    return out


def norm(s: str) -> str:
    """归一化后再比"逐字"。

    踩过的坑（判据自己制造假故障三次，都记在这儿）：
      · **引用块前缀 `>`**：页面里的长引文**换行后每行都有 `>`**（Markdown 引用块），
        而卡片里的原文没有 → 不去掉就永远匹配不上（第一版因此报了十几处假故障）
      · **引号变体**：页面写 `'积极思维的王国'`、卡片写 `“积极思维的王国”`；
        四种引号必须归一，否则"逐字"比的是标点差异不是文字差异
      · **markdown 强调**：`**相对**` 要去掉
    """
    s = s.replace('**', '').replace('*', '')
    s = re.sub(r'^[ \t]*>[ \t]?', '', s, flags=re.M)      # 去掉引用块前缀
    s = re.sub(r'\s+', '', s)
    # **所有引号变体归成同一个字符**：页面上我写 `'积极思维的王国'`、卡片里是
    # `“积极思维的王国”`——若把单引号归成 '、双引号归成 "，两者仍不相等，
    # 就变成"比的是标点差异而不是文字差异"（假故障）。逐字比较只该忽略引号的长相。
    for ch in '“”‘’「」『』"\'':
        s = s.replace(ch, '"')
    # 全角/半角括号也归一并统一：卡片里 OCR 常见半角 `(继而是少年、青年)`，
    # 我引用时写成全角 `（…）`——**内容一样，只是字形**。
    s = s.replace('（', '(').replace('）', ')')
    return s


def main() -> int:
    files = {p.stem.split('-')[0] + '-' + p.stem.split('-')[1]: p for p in CARDS.glob('sk-*.md')}
    pages = [p for d in SCAN_DIRS for p in sorted((WIKI / d).glob('*.md'))]
    if not pages:
        print('引文核对：没有可核对的页面')
        return 0

    for page in pages:
        raw = page.read_text(encoding='utf-8')
        rel = page.relative_to(ROOT).as_posix()
        # **约定**：分析页里 `「…」` = 引文（本判据核对这些），`"…"` = 强调或"假设的反例长什么样"。
        # 试过把 `"…"` 也纳入核对：结果假报多于真报——例如
        #   · 正文里的强调：`"应该"那一面的证据薄**：三因素里`
        #   · 描述反例形态：`有卡说"物质刺激应无条件禁止"`（这是**假设**，不是引文）
        # 与其把判据写得越来越绕去猜哪些是真引文，不如**定一个写作约定**：
        # 引文一律用 `「」`，判据只认这一种。覆盖率边界写进下面的汇总输出，不装作全查过。
        spans = [(m.start(), m.end(), m.group(1))
                 for m in re.finditer(r'「(.+?)」', raw, re.S)]
        for start, end, quote in sorted(spans):
            # 归属只在**本段之内**取。段的边界有三种，缺一不可：
            #   · 空行（普通段落）
            #   · 表格行 `\n|`（表格行之间没有空行，不切的话整张表算一段 →
            #     引文会串到**别的行**的卡号上。实测：§九的证伪表里
            #     「而不是全班一律去校办工厂做小板凳」被判给了下一行的 sk-0267）
            #   · 下一条引文 `「`（同一行里并排两条引文时）
            after = raw[end:end + 600]
            stops = [len(after)]
            for pat in (r'\n[ \t]*\n', r'\n[ \t]*\|', r'「'):
                s = re.search(pat, after)
                if s:
                    stops.append(s.start())
            tail = after[:min(stops)][:400]
            # 卡号可能在引文**后面**（`「引文」（[[sk-1301]] 原文）`），
            # 也可能在**前面**（表格与行内写法：`[[sk-1282]]「引文」`）。
            # 语义上应当取**离引文最近**的那一个——前两版分别只往后找、或只在往后找不到时才往前找，
            # 都会在 `[[sk-1282]]「甲」、[[sk-1302]]「乙」` 这种并排写法里判错。
            post_m = re.search(r'\[\[(sk-\d{4})\]\]', tail)
            before = raw[max(0, start - 120):start]
            stops2 = [len(before)]
            for pat in (r'\n[ \t]*\n', r'\n[ \t]*\|', r'」'):
                s = re.search(pat, before)
                if s:
                    stops2.append(s.start())
            pre = before[max(stops2):]
            pre_ms = list(re.finditer(r'\[\[(sk-\d{4})\]\]', pre))
            cid = None
            d_post = post_m.start() if post_m else 10 ** 6
            d_pre = (len(pre) - pre_ms[-1].end()) if pre_ms else 10 ** 6
            if d_pre <= d_post and pre_ms:
                cid = pre_ms[-1].group(1)
            elif post_m:
                cid = post_m.group(1)
            if not cid:
                continue                     # 前后都没标卡号的引文（如引用书名）不核
            STATS['quotes'] += 1
            sec_hits = [k for k in SEC_LABEL if k in tail[:60]]
            ocr_declared = 'OCR' in tail
            if cid not in files:
                PROBLEMS.append(f'{rel}: 引文指向不存在的卡 {cid}')
                continue
            secs = card_sections(files[cid].read_text(encoding='utf-8'))
            # 引文可能用 `……` 拼接了不相邻的片段 → 逐段核
            frags = [f for f in re.split(r'……|\.\.\.', quote) if norm(f)]
            missing: list[str] = []
            found_in: set[str] = set()
            for frag in frags:
                nf = norm(frag)
                hit = [name for name, body in secs.items() if nf in norm(body)]
                if hit:
                    found_in.update(hit)
                else:
                    missing.append(frag[:24])
            if missing and ocr_declared:
                STATS['ocr'] += 1
                continue                     # 已申报的 OCR 录正：放行（不计入 ok）
            if missing:
                PROBLEMS.append(
                    f'{rel}: 引文「{missing[0]}…」在 {cid} 里找不到'
                    f'（声称出处 {sec_hits or "未标注"}；该卡可用小节 {sorted(secs)}）')
                continue
            # 出处节是否对得上
            if sec_hits:
                want = set()
                for k in sec_hits:
                    want.update(SEC_LABEL[k])
                if not (found_in & want):
                    PROBLEMS.append(
                        f'{rel}: {cid} 的引文声称在「{"/".join(sec_hits)}」，'
                        f'实际只在 {sorted(found_in)} —— 出处标错了')
                    continue
            else:
                STATS['nosection'] += 1
            STATS['ok'] += 1

    if PROBLEMS:
        print(f'引文核对：**{len(PROBLEMS)} 处问题**')
        for x in PROBLEMS[:20]:
            print('  ✗ ' + x)
        if len(PROBLEMS) > 20:
            print(f'  … 另有 {len(PROBLEMS) - 20} 处')
        return 1
    print(f'引文核对：全部通过（{len(pages)} 个分析页 · 核对 `「」` 引文 {STATS["quotes"]} 条 · '
          f'逐字命中 {STATS["ok"]} · 已申报的 OCR 录正 {STATS["ocr"]} · '
          f'未标出处节 {STATS["nosection"]}）')
    print('  覆盖边界：只核 `「」` 引文（约定：`"…"` 用于强调/假设，不算引文）；'
          '没标 `[[sk-XXXX]]` 的引文不核。')
    return 0


if __name__ == '__main__':
    sys.exit(main())
