#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path


if __name__ == '__main__':
    path = Path(__file__).absolute().parent / 'input.txt'
    with open(path, 'r', encoding='utf8') as fin:
        lines = fin.readlines()

    reversed_lines = list(
        reversed(
            [line.rstrip()[::-1] for line in lines]
        )
    )
    reversed_lines.append('')

    print('\n'.join(reversed_lines))
