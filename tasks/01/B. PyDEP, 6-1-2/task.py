#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
from pathlib import Path


if __name__ == '__main__':
    path = Path(__file__).absolute().parent / 'input.txt'
    with open(path, 'r', encoding='utf8') as fin:
        text = fin.read()

    counter = Counter(text.split())
    words = [(-count, word) for word, count in counter.items()]
    words.sort()

    print(' '.join(word for _, word in words))
