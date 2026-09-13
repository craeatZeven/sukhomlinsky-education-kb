# -*- coding: utf-8 -*-
"""临时辅助脚本：跨卷按锚句定位候选段落（只打印，不写卡片）。

用法：
    python scripts/_tmp_find_anchors.py "锚句1" "锚句2" ...
可选：--vol=vol5 限定卷。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OCR = ROOT / 'local_working_copy' / 'ocr' / 'mineru-range' / 'merged'

VOLS = [
    '苏霍姆林斯基选集（五卷本）第1卷.txt',
    '苏霍姆林斯基选集(五卷本)第2卷.txt',
    '苏霍姆林斯基选集（五卷本）第3卷.txt',
    '苏霍姆林斯基选集(五卷本)第4卷.txt',
    '苏霍姆林斯基选集（五卷本）第5卷.txt',
    '苏霍姆林斯基-给教师的建议.txt',
]

_CACHE = {}


def norm(s: str) -> str:
    return re.sub(r'\s+', '', s)


def paras_of(fname: str):
    if fname not in _CACHE:
        lines = (OCR / fname).read_text(encoding='utf-8').split('\n')
        out = []
        buf, start = [], None
        for i, ln in enumerate(lines, 1):
            if ln.strip() == '':
                if buf:
                    out.append((start, i - 1, '\n'.join(buf)))
                    buf, start = [], None
            else:
                if start is None:
                    start = i
                buf.append(ln)
        if buf:
            out.append((start, len(lines), '\n'.join(buf)))
        _CACHE[fname] = out
    return _CACHE[fname]


def main() -> None:
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    vol_filter = None
    for a in sys.argv[1:]:
        if a.startswith('--vol='):
            vol_filter = a.split('=', 1)[1]
    files = [f for f in VOLS if not vol_filter or vol_filter in f]
    for anchor in args:
        na = norm(anchor)
        print('#' * 90)
        print(f'# 锚句：{anchor}')
        for fname in files:
            paras = paras_of(fname)
            hits = [(ln0, ln1, x) for ln0, ln1, x in paras if na in norm(x)]
            if not hits:
                continue
            print(f'  [{fname}]  {len(hits)} 处')
            for ln0, ln1, x in hits[:6]:
                print(f'    · 行{ln0}-{ln1} ({len(norm(x))}字): {norm(x)[:260]}')


if __name__ == '__main__':
    main()
