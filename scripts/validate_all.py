# -*- coding: utf-8 -*-
"""Run the full local validation chain.

Usage:
    python scripts/validate_all.py

Runs check_kb.py, audit_cards.py, coverage_report.py and build_site.py in
order. Exits non-zero on the first failure.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SCRIPTS = [
    'check_kb.py',
    'audit_cards.py',
    'coverage_report.py',
    'coverage_volumes.py',
    'build_site.py',
]


def main() -> int:
    for name in SCRIPTS:
        path = ROOT / 'scripts' / name
        print(f'\n=== {name} ===')
        result = subprocess.run([sys.executable, str(path)], cwd=str(ROOT))
        if result.returncode != 0:
            print(f'FAILED: {name}')
            return result.returncode
    print('\nALL OK')
    return 0


if __name__ == '__main__':
    sys.exit(main())
