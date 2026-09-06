# -*- coding: utf-8 -*-
"""Report OCR progress for scanned Chinese Sukhomlinsky books.

Scans local_working_copy/ocr/ (EasyOCR + MinerU outputs). This script is
intentionally repo-committed so anyone can run it locally; local_working_copy/
itself is gitignored.
"""
from __future__ import annotations

import os
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OCR = ROOT / 'local_working_copy' / 'ocr'
MINERU = OCR / 'mineru'

BOOKS = [
    ('教育箴言', 'jiao-yu-zhen-yan-zh.txt', '苏霍姆林斯基教育箴言.pdf'),
    ('给教师的建议', 'gei-jiao-shi-de-jian-yi-zh.txt', '苏霍姆林斯基-给教师的建议.pdf'),
    ('五卷本第1卷', 'xuan-ji-zh-vol1.txt', '苏霍姆林斯基选集（五卷本）第1卷.pdf'),
    ('五卷本第2卷', 'xuan-ji-zh-vol2.txt', '苏霍姆林斯基选集(五卷本)第2卷.pdf'),
    ('五卷本第3卷', 'xuan-ji-zh-vol3.txt', '苏霍姆林斯基选集（五卷本）第3卷.pdf'),
    ('五卷本第4卷', 'xuan-ji-zh-vol4.txt', '苏霍姆林斯基选集(五卷本)第4卷.pdf'),
    ('五卷本第5卷', 'xuan-ji-zh-vol5.txt', '苏霍姆林斯基选集（五卷本）第5卷.pdf'),
]


def easyocr_progress(name: str) -> str:
    p = OCR / name
    if not p.exists():
        return 'not started'
    prog = Path(str(p) + '.progress')
    if prog.exists():
        n = len([line for line in prog.read_text(encoding='utf-8').splitlines() if line.strip()])
        return f'{n} pages done'
    return f'exists size={p.stat().st_size}'


def mineru_status(pdf_name: str) -> str:
    stem = pdf_name[:-4]
    md = MINERU / stem / 'ocr' / (stem + '.md')
    if md.exists() and md.stat().st_size > 0:
        return f'done ({md.stat().st_size} bytes)'
    log = MINERU / (stem + '.log')
    if log.exists():
        lines = log.read_text(encoding='utf-8', errors='ignore').splitlines()
        progress_lines = [ln for ln in lines if re.search(r'(Predict|it/s|DONE|Completed batch)', ln)]
        return progress_lines[-1].strip()[-160:] if progress_lines else 'running/starting'
    return 'queued/not started'


def main() -> None:
    print('EasyOCR/plain-text outputs:')
    for label, txt, _ in BOOKS:
        print(f'  {label}: {easyocr_progress(txt)}')
    print('MinerU outputs:')
    for label, _, pdf in BOOKS:
        print(f'  {label}: {mineru_status(pdf)}')


if __name__ == '__main__':
    main()
