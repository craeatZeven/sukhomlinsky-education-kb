# -*- coding: utf-8 -*-
"""内容契约的**离线**检查：不需要浏览器，直接读产物对账。

为什么要有这个文件：加固过的浏览器验证脚本（`tools/web-audit/verify-hardened.mjs`）
覆盖了渲染层，但它需要 Chrome 与静态服务，进不了 `validate_all.py`。
于是把**纯数据层**的那几条契约检查抽出来放在这里，接进校验链——
这样每次 `validate_all.py` 都会替我们盯住它们，而不是靠我记得去跑浏览器。

每一条都对应一次真实踩过的坑，注释里写明出处。
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / 'scripts'))

PROBLEMS: list[str] = []


def fail(msg: str) -> None:
    PROBLEMS.append(msg)


def main() -> int:
    cards = json.loads((ROOT / 'web/data.json').read_text(encoding='utf-8'))['cards']
    cls = json.loads((ROOT / 'classification.json').read_text(encoding='utf-8'))

    # ① 原文摘录槽位里不许出现「转述 / 非直引 / 编者概括 / 概述」这类自述。
    #    坑：有 20 张卡把**编者概括**写在 `## 原文/Excerpt` 里，页面以引文样式呈现、
    #    读者会当成原话；分类依据又引用这段概括，于是概括在展示/分类/核验三处循环。
    #    见 docs/codex-final-opinion.md A1 与 docs/review-disposition.md §九。
    BAD = re.compile(r'转述|非直引|非原文|编者概括|概述')
    off = [c['id'] for c in cards
           for ex in (c.get('excerpts') or []) if BAD.search(ex[:60])]
    if off:
        fail(f'{len(off)} 张卡的原文摘录槽位里写着「转述/非直引」：{off[:8]}')

    # ② 没有逐字原文的卡必须**显式**标注，不许静默为空。
    #    判据从"摘录不为空"改成"要么有原文、要么 excerpt_status=paraphrase + 编者概括"，
    #    因为原来的字面要求正是逼人把概括塞进引文槽位的诱因（taxonomy.md §五 门槛⑥）。
    silent, marked = [], []
    for c in cards:
        has_orig = bool([x for x in (c.get('excerpts') or []) if re.sub(r'\s', '', x)])
        if c.get('excerpt_status') == 'paraphrase':
            marked.append(c['id'])
            if not re.sub(r'\s', '', c.get('editor_summary') or ''):
                fail(f'{c["id"]} 标了 paraphrase 但没有编者概括（等于空卡）')
        elif not has_orig:
            silent.append(c['id'])
    if silent:
        fail(f'{len(silent)} 张卡既无原文又无显式标注（静默空缺）：{silent[:8]}')

    # ③ 入门卡的三个角色必须齐全且互不重复。
    #    坑：原来按"摘录最短"挑，A11 挑出三张全是 quote/principle，
    #    "短不等于有代表性"——见 docs/codex-rereview-opinion.md §B「四个重点问题」1。
    entry_dir = ROOT / 'web/data/entry'
    n_start = 0
    two_card = []
    for p in sorted(entry_dir.glob('*.json')):
        d = json.loads(p.read_text(encoding='utf-8'))
        if d.get('tag'):
            continue
        st = d.get('start') or []
        roles = [x.get('role') for x in st]
        if not st:
            fail(f'条目 {d["code"]} 没有入门卡（start 为空）')
            continue
        n_start += 1
        if len(set(x['id'] for x in st)) != len(st):
            fail(f'条目 {d["code"]} 的入门卡有重复：{[x["id"] for x in st]}')
        for want in ('为什么', '怎么做'):
            if want not in roles:
                fail(f'条目 {d["code"]} 的入门卡缺角色「{want}」（现有 {roles}）')
        # 「一个教学案例」只在**该条目确实有案例**时要求。
        # 实测 A1 / A20 没有任何挂靠案例，那就只能两张——
        # 硬凑一张会把不相干的案例说成"这一条的例证"，比少一张更糟。
        # 这里记下来供人看，不算失败。
        if d.get('cases'):
            if '一个教学案例' not in roles:
                fail(f'条目 {d["code"]} 有 {len(d["cases"])} 条案例，'
                     f'入门卡却没给「一个教学案例」（现有 {roles}）')
        elif '一个教学案例' in roles:
            fail(f'条目 {d["code"]} 没有案例，入门卡却标了「一个教学案例」')
        else:
            two_card.append(d['code'])

    # ④ 相关案例的张数必须与 classification.json 现算一致——
    #    **不从分片反推**。坑：分片与上游同时丢数据时，两边一致也说明不了问题
    #    （docs/codex-rereview-opinion.md §A「PASS 判据的问题」）。
    n_case = 0
    for p in sorted(entry_dir.glob('*.json')):
        d = json.loads(p.read_text(encoding='utf-8'))
        code = d['code']
        want = sum(1 for r in cls.values()
                   if r.get('type') == 'case' and code in (r.get('case_entries') or []))
        got = len(d.get('cases') or [])
        if got != want:
            fail(f'条目 {code} 的相关案例数 {got} ≠ classification.json 现算 {want}')
        n_case += want

    # ⑤ 分类记录里标了 evidence_unverified 的卡，必须在数据层也标着 paraphrase。
    #    否则会出现"分类说依据不可核验、卡片却显示有原文"的矛盾。
    #
    #    **这条只查一个方向**（unverified ⇒ paraphrase），反过来不成立，是故意的：
    #    `evidence_unverified` 是论述卡的属性——判读管线拿 `evidence` 字段去模糊匹配
    #    卡片正文，匹配不上才标。而 673 张故事卡（type=case）**没有** `evidence` 字段，
    #    没东西可核，自然不标。实测：paraphrase 11 张、evidence_unverified 9 张，
    #    差的 2 张正是 story 卡 sk-0111 / sk-0185（`local_working_copy/diag_paraphrase_vs_unverified.py`
    #    可复算）。所以要求两者数量相等会误报。
    for cid, rec in cls.items():
        if rec.get('evidence_unverified'):
            c = next((x for x in cards if x['id'] == cid), None)
            if c is None:
                fail(f'{cid} 在分类里标了 evidence_unverified，数据层却没有这张卡')
            elif c.get('excerpt_status') != 'paraphrase':
                fail(f'{cid} 分类标 evidence_unverified，但卡片 excerpt_status='
                     f'{c.get("excerpt_status")}（应当一致）')

    if PROBLEMS:
        print(f'内容契约：**{len(PROBLEMS)} 处不一致**')
        for p in PROBLEMS[:20]:
            print('  ✗ ' + p)
        if len(PROBLEMS) > 20:
            print(f'  … 另有 {len(PROBLEMS) - 20} 处')
        return 1
    print(f'内容契约：全部一致'
          f'（{len(cards)} 张卡 · 原文待补 {len(marked)} 张 · '
          f'{n_start} 个条目有入门卡 · 案例挂靠 {n_case} 处）')
    if two_card:
        print(f'  注：{len(two_card)} 个条目本身没有挂靠案例，入门卡只有两张'
              f'（{two_card}）——不硬凑，如实如此')
    return 0


if __name__ == '__main__':
    sys.exit(main())
