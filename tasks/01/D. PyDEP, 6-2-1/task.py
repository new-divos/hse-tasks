#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path


if __name__ == '__main__':
    path = Path(__file__).absolute().parent / 'input.txt'
    with open(path, 'r', encoding='utf8') as fin:
        lines = fin.readlines()

    reversed_lines = list(reversed(lines))
    reversed_lines.append('\n')

    print(''.join(reversed_lines))
