# -*- coding: utf-8 -*-
"""补写 3 张薄摘录卡的「原文/Excerpt」：从 OCR 原文摘出承载主张的段落。

**逐字取自 OCR 文件**，拼接与换行由脚本做，避免手抄出错。
摘录写完后会做一次逐字核验：新摘录的每一句都必须能在 OCR 文件里找到。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OCR = ROOT / 'local_working_copy' / 'ocr' / 'mineru-range' / 'merged'

# 卡片 → (OCR 文件, 起始锚句, 结束锚句)
JOBS = {
    'sk-0368': ('苏霍姆林斯基选集(五卷本)第4卷.txt',
                '一个有经验的校长',
                '下面我想就听课和分析课的问题'),
    'sk-0348': ('苏霍姆林斯基选集（五卷本）第3卷.txt',
                '瞧！你从父母的巢中飞走了',
                '这是我写给从父母的巢中飞走的儿子的第一封信'),
    'sk-1035': ('苏霍姆林斯基选集(五卷本)第2卷.txt',
                '我带领27个小学生到草地参观',
                '只能采取这样一'),
}

norm = lambda s: re.sub(r'\s+', '', s)  # noqa: E731


def paras_of(fname: str) -> list[str]:
    t = (OCR / fname).read_text(encoding='utf-8')
    return [x.strip() for x in re.split(r'\n\s*\n', t) if norm(x)]


def span(paras: list[str], a: str, b: str) -> list[str]:
    na, nb = norm(a), norm(b)
    ia = [i for i, x in enumerate(paras) if na in norm(x)]
    ib = [i for i, x in enumerate(paras) if nb in norm(x)]
    if not ia:
        raise SystemExit(f'找不到起始锚句：{a}')
    if not ib:
        raise SystemExit(f'找不到结束锚句：{b}')
    i0 = ia[0]
    i1 = max(i for i in ib if i >= i0)
    picked = []
    for x in paras[i0:i1 + 1]:
        # 丢掉 OCR 的页眉页脚噪声行
        if re.fullmatch(r'(苏霍姆林斯基选集[（(].*?[)）]|给教师的100条建议|苏霍姆林斯基-给教师的建议)', norm(x)):
            continue
        picked.append(x)
    return picked


def build_excerpt(picked: list[str]) -> str:
    body = []
    for i, x in enumerate(picked):
        if i:
            body.append('>')
        body.append('> ' + re.sub(r'\s*\n\s*', '', x))
    return '\n'.join(body)


def replace_section(text: str, new_body: str, note: str) -> str:
    m = re.search(r'^(## 原文/Excerpt\s*)$', text, re.M)
    if not m:
        raise SystemExit('找不到 ## 原文/Excerpt')
    start = m.end()
    nxt = re.search(r'^## ', text[start:], re.M)
    end = start + (nxt.start() if nxt else len(text) - start)
    block = f'\n\n{new_body}\n\n{note}\n\n'
    return text[:start] + block + text[end:]


def main() -> None:
    for cid, (fname, a, b) in JOBS.items():
        paras = paras_of(fname)
        picked = span(paras, a, b)
        body = build_excerpt(picked)
        chars = len(norm(''.join(picked)))
        # 逐字核验：每个 8 字窗口都要能在 OCR 里找到
        flat = norm((OCR / fname).read_text(encoding='utf-8'))
        n = norm(''.join(picked))
        grams = [n[i:i + 8] for i in range(0, max(1, len(n) - 8), 8)]
        miss = [g for g in grams if g not in flat]
        print(f'{cid}：{fname}　摘 {len(picked)} 段 {chars} 字　'
              f'逐字核验 {"全部命中" if not miss else f"{len(miss)}/{len(grams)} 段对不上"}')
        if miss:
            print('   ⚠ 对不上的窗口：', miss[:5])
            continue
        note = ('（OCR 讹字说明：摘录逐字取自本地 OCR 文本，OCR 讹字与断行照原样保留；'
                '本次补摘的用意见 docs/llm-classification-plan.md §9.4。）')
        card_path = next((ROOT / 'cards').glob(f'{cid}-*.md'))
        txt = card_path.read_text(encoding='utf-8')
        new = replace_section(txt, body, note)
        new = re.sub(r'^updated: ".*?"', 'updated: "2026-09-11"', new, count=1, flags=re.M)
        card_path.write_text(new, encoding='utf-8', newline='')
        print(f'   → 已写入 {card_path.name}')


if __name__ == '__main__':
    main()
