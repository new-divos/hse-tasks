#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from pathlib import Path


if __name__ == '__main__':
    salaries = []

    path = Path(__file__).absolute().parent / 'input.csv'
    with open(path, 'r', encoding='utf8') as fin:
        reader = csv.reader(fin, delimiter=';')

        for row in reader:
            salaries.append(tuple(reversed(row)))

    out_path = Path.home() / 'output.csv'
    with open(out_path, 'w', encoding='utf8', newline='') as fout:
        writer = csv.writer(fout, delimiter=';')
        writer.writerows(salaries)
