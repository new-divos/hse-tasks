#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path


if __name__ == '__main__':
    path = Path(__file__).absolute().parent.parent.parent.parent \
           / 'data' / 'input611.txt'
    with open(path, 'r', encoding='utf8') as fin:
        text = fin.read()

    words = set(text.split())
    print(len(words))
