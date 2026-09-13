# -*- coding: utf-8 -*-
"""临时辅助脚本：为 13 张「转述概括冒充原文」的卡片在 OCR 里定位候选段落。

只做定位与打印，不写任何卡片。用法：
    python scripts/_tmp_locate_paraphrase.py <卡片id> <锚句1> [锚句2 ...]
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OCR = ROOT / 'local_working_copy' / 'ocr' / 'mineru-range' / 'merged'

VOL = {
    'vol1': '苏霍姆林斯基选集（五卷本）第1卷.txt',
    'vol2': '苏霍姆林斯基选集(五卷本)第2卷.txt',
    'vol3': '苏霍姆林斯基选集（五卷本）第3卷.txt',
    'vol4': '苏霍姆林斯基选集(五卷本)第4卷.txt',
    'vol5': '苏霍姆林斯基选集（五卷本）第5卷.txt',
    'jys': '苏霍姆林斯基-给教师的建议.txt',
}


def norm(s: str) -> str:
    return re.sub(r'\s+', '', s)


def paras_with_lines(fname: str):
    """返回 [(起始行号, 段落文本)]，按空行切分。"""
    p = OCR / fname
    lines = p.read_text(encoding='utf-8').split('\n')
    out = []
    buf, start = [], None
    for i, ln in enumerate(lines, 1):
        if ln.strip() == '':
            if buf:
                out.append((start, '\n'.join(buf)))
                buf, start = [], None
        else:
            if start is None:
                start = i
            buf.append(ln)
    if buf:
        out.append((start, '\n'.join(buf)))
    return out


def main() -> None:
    vol = sys.argv[1]
    anchors = sys.argv[2:]
    fname = VOL[vol]
    paras = paras_with_lines(fname)
    for a in anchors:
        na = norm(a)
        print('=' * 90)
        print(f'锚句：{a}')
        hits = [(ln, x) for ln, x in paras if na in norm(x)]
        if not hits:
            print('  ✗ 未命中')
            continue
        for ln, x in hits:
            print(f'  ✓ 行 {ln}: {x[:400]}')
    # 同时打印每个锚句前后各 2 段的上下文（用第一个命中）
    print('=' * 90)
    for a in anchors:
        na = norm(a)
        idx = [i for i, (ln, x) in enumerate(paras) if na in norm(x)]
        for i0 in idx[:2]:
            print(f'--- {a} @ 段{i0} ---')
            for j in range(max(0, i0 - 2), min(len(paras), i0 + 4)):
                ln, x = paras[j]
                mark = '→' if j == i0 else ' '
                print(f'  {mark}[行{ln}] {norm(x)[:400]}')


if __name__ == '__main__':
    main()
