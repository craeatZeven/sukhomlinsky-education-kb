# -*- coding: utf-8 -*-
"""临时辅助脚本：按锚句切片并测量字数 / 逐字核验（不写卡片）。

用法：python scripts/_tmp_measure.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OCR = ROOT / 'local_working_copy' / 'ocr' / 'mineru-range' / 'merged'

V5 = '苏霍姆林斯基选集（五卷本）第5卷.txt'
V4 = '苏霍姆林斯基选集(五卷本)第4卷.txt'
V3 = '苏霍姆林斯基选集（五卷本）第3卷.txt'

norm = lambda s: re.sub(r'\s+', '', s)  # noqa: E731

NOISE = re.compile(
    r'(姆林斯基|姆林斯所基|姆林斯甚|姆林所基|當姆林|苏當姆林|洗集|近集|迭集|选隼|选棐|选集王卷本|全集)'
)

_CACHE = {}


def load(fname):
    if fname not in _CACHE:
        raw = (OCR / fname).read_text(encoding='utf-8')
        out, idx = [], []
        for i, ch in enumerate(raw):
            if not ch.isspace():
                out.append(ch)
                idx.append(i)
        _CACHE[fname] = (raw, ''.join(out), idx)
    return _CACHE[fname]


def is_noise(line: str) -> bool:
    nl = norm(line)
    if not nl:
        return True
    if len(nl) <= 24 and NOISE.search(nl):
        return True
    # 竖排书眉：字被空格拆开、无标点
    if len(nl) <= 24 and line.count(' ') >= 3 and not re.search(r'[。，、？！：；""''—…]', nl):
        return True
    if nl.isdigit():
        return True
    return False


def slice_between(fname, a, b):
    raw, flat, idx = load(fname)
    na, nb = norm(a), norm(b)
    i = flat.find(na)
    if i < 0:
        raise SystemExit(f'  ✗ 找不到起始锚句: {a}')
    j = flat.find(nb, i)
    if j < 0:
        raise SystemExit(f'  ✗ 找不到结束锚句: {b}')
    j += len(nb)
    return raw[idx[i]:idx[j - 1] + 1]


def build(fname, pieces):
    paras = []
    dropped = []
    for a, b in pieces:
        seg = slice_between(fname, a, b)
        for p in re.split(r'\n\s*\n', seg):
            if not p.strip():
                continue
            paras.append(re.sub(r'\s*\n\s*', '', p))
    return paras, dropped


def verify(fname, text):
    raw, flat, idx = load(fname)
    n = norm(text)
    grams = [n[i:i + 8] for i in range(0, max(1, len(n) - 8) + 1, 8)]
    miss = [g for g in grams if g not in flat]
    return len(n), len(grams), miss


def report(tag, fname, pieces, evidence=None):
    paras, dropped = build(fname, pieces)
    text = ''.join(paras)
    n, ng, miss = verify(fname, text)
    print(f'--- {tag} [{fname}] 段数={len(paras)} 字数={n} 窗口={ng} 未命中={len(miss)}')
    for p in paras:
        print(f'    > {p[:100]}{"..." if len(p) > 100 else ""}')
    if dropped:
        print(f'    (丢弃噪声行 {len(dropped)}): ' + ' | '.join(x.strip()[:30] for x in dropped))
    if miss:
        print(f'    ✗ 对不上: {miss[:6]}')
    if evidence is not None:
        ok = norm(evidence) in norm(text)
        print(f'    原文依据 {"✓在摘录内" if ok else "✗不在摘录内"}: {evidence}')
    return n, miss


JOBS = [
    ('sk-0074', V5, [('问题在于，在某些学校，有这么一种不良习气渗进了学生集体的精神生活',
                      '甚至还登了照片。')]),
    ('sk-0075', V5, [('如果本应带给儿童生活和求知快乐的学习成了他们的心病',
                      '两分对学生来说就是鞭了和棍棒。')]),
    ('sk-0076', V5, [('我校接收的107名智力很落后的学生', '在这107人中有13人后来接受了高等教育。')]),
    ('sk-0078', V5, [('比方说，教室里飞进一只不知何名的鸟儿', '而问题则是可激起学生求解愿望的动因。')]),
    ('sk-0079', V5, [('操纵最复杂的机器的能力与手工性劳动的技巧有着直接的依赖关系',
                      '避免断裂或过早地损坏零件。')]),
    ('sk-0081a', V5, [('大概在我7岁时，父亲就让我栽过3棵葡萄树苗', '骗得了别人，而骗不了自已……’”')]),
    ('sk-0081b', V5, [('到了晚上父亲问我，须根蘸过腐殖土浆吗？', '骗得了别人，而骗不了自已……’”')]),
    ('sk-0083a', V5, [('许多教师认为，这主要应归咎于教学大纲和教科书不完善',
                       '但又分别要求不同的智力活动。'),
                      ('死记硬背那些本应去理解的材料', '也被遗忘了。')]),
    ('sk-0083b', V5, [('许多教师认为，这主要应归咎于教学大纲和教科书不完善',
                       '但又分别要求不同的智力活动。')]),
    ('sk-0125a', V5, [('他离开班级两个星期，却并无痛悔之感', '这是我们教育上的重大失误。')]),
    ('sk-0125b', V5, [('我们回顾了教务委员会那次讨论格里戈里停学问题的情形',
                       '这种联系便表现在集体舆论中。')]),
    ('sk-0126', V5, [('在白我教育中，身体锻炼占有非常重要的地位',
                      '这是自我教育和自律特别重要的一个方面。')]),
    ('sk-0128', V5, [('同时，恕我直言：在某些家庭里，孩子的愿望成了认识和理解世界的惟一动力',
                      '像吸血虫似地吮吸父母的鲜血和劳动。')]),
    ('sk-0129', V5, [('多年的经验使我确信，下面这条十分重要的教育规律是正确的',
                      '成了他们童年欢乐的源泉。')]),
    ('sk-0185', V4, [('最后医生得出结论，认为这是因长时间坐在室内而引起的新陈代谢失调',
                      '而原先大家都断定柯利亚是会留级的。')]),
    ('sk-0187a', V3, [('旺盛的新陈代谢需要正确安排饮食',
                       '这对所有男孩与女孩来说都已经习以为常了。')]),
    ('sk-0187b', V3, [('旺盛的新陈代谢需要正确安排饮食',
                       '他从睡梦中醒来时头脑情况如何以及机体对一天的劳动的情绪如何有关。')]),
]


def main():
    only = sys.argv[1:] or None
    for tag, fname, pieces in JOBS:
        if only and tag not in only:
            continue
        try:
            report(tag, fname, pieces)
        except SystemExit as e:
            print(f'--- {tag} {e}')
        print()


if __name__ == '__main__':
    main()
