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

        total_letters += sum(len(word) for word in words)

    print("Input file contains:")
    print(f"{total_letters} letters")
    print(f"{total_words} words")
    print(f"{total_lines} lines")
