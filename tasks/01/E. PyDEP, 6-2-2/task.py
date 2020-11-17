#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import re


if __name__ == '__main__':
    path = Path(__file__).absolute().parent / 'input.txt'
    with open(path, 'r', encoding='utf8') as fin:
        lines = fin.readlines()

    total_lines = len(lines)
    total_words = total_letters = 0

    for line in lines:
        words = re.findall(r'\w+', line)
        total_words += len(words)

        for word in words:
            total_letters += len(word)

    print(
        "Input file contains: {} letters {} words {} lines".format(
            total_letters,
            total_words,
            total_lines
        )
    )
