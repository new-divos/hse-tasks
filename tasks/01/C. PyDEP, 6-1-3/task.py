#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path


if __name__ == '__main__':
    path = Path(__file__).absolute().parent / 'input.txt'
    with open(path, 'r', encoding='utf8') as fin:
        sums = []

        for line in fin:
            line = line.strip()
            if line:
                sums.append(sum(int(item) for item in line.split()))

    print(' '.join(str(value) for value in sums))
