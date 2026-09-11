# -*- coding: utf-8 -*-
"""给 4 张薄摘录卡找承载主张的原文段落。

这 4 张卡的 `## 原文/Excerpt` 太短或只有叙述，主张只存在于「中文转述」里——
按元规则编辑转述不能充当主张，所以要回原文补摘。
本脚本**只做定位与候选输出**，不写卡片；摘录由人确认后再写。
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OCR = ROOT / 'local_working_copy' / 'ocr' / 'mineru-range' / 'merged'

# 卡片 id → (OCR 文件, 定位用锚句)
TARGETS = {
    'sk-0368': ('苏霍姆林斯基选集(五卷本)第4卷.txt', '下面我想就听课和分析课的问题'),
    'sk-0348': ('苏霍姆林斯基选集(五卷本)第3卷.txt', '你从父母的巢中飞走了'),
    'sk-1035': ('苏霍姆林斯基选集(五卷本)第2卷.txt', '怎样使学生注意力集中'),
    'sk-0031': ('苏霍姆林斯基-给教师的建议.txt', None),
}


def norm(s: str) -> str:
    return re.sub(r'\s+', '', s)


def find_windows(text: str, anchor: str, before: int, after: int, k: int = 3):
    """按锚句在原文里找，返回若干候选窗口（含前后文，按原文顺序）。"""
    hits = [m.start() for m in re.finditer(re.escape(anchor), text)]
    out = []
    for h in hits[:k]:
        out.append((h, text[max(0, h - before):h + after]))
    return out


def main() -> None:
    for cid, (fname, anchor) in TARGETS.items():
        print('=' * 70)
        print(f'{cid}　OCR 文件：{fname}　锚句：{anchor}')
        if anchor is None:
            print('  （没有锚句——这张卡的 source 是《把心献给孩子》，不在卷本 OCR 里，'
                  '需要另找正文，见报告）')
            continue
        p = OCR / fname
        if not p.exists():
            print(f'  ⚠ 文件不存在：{p}')
            continue
        text = p.read_text(encoding='utf-8')
        flat = norm(text)
        n_anchor = norm(anchor)
        if n_anchor not in flat:
            print(f'  ⚠ 锚句在原文里找不到（可能 OCR 讹字），试试缩短锚句')
            continue
        # 在归一化文本里定位，再映射回原文（简单办法：整段切分后找段）
        paras = [x for x in re.split(r'\n\s*\n', text) if norm(x)]
        idx = [i for i, x in enumerate(paras) if n_anchor in norm(x)]
        print(f'  命中段号：{idx}')
        for i in idx[:2]:
            lo, hi = max(0, i - 1), min(len(paras), i + 3)
            for j in range(lo, hi):
                seg = paras[j].strip().replace('\n', '')
                mark = '→' if j == i else ' '
                print(f'  {mark}[段{j}] {seg[:520]}')
            print('  ' + '-' * 60)


if __name__ == '__main__':
    main()
