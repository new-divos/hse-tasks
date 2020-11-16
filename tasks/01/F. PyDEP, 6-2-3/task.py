#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
from pathlib import Path


if __name__ == '__main__':
    path = Path(__file__).absolute().parent / 'input.txt'
    with open(path, 'r', encoding='utf8') as fin:
        lines = fin.readlines()

    d = OrderedDict((line, len(line)) for line in lines)
    max_len = max(d.values())

    for line, current_len in d.items():
        if current_len == max_len:
            print(line)
