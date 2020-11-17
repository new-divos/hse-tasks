#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from pathlib import Path


if __name__ == '__main__':
    orgs = {}

    path = Path(__file__).absolute().parent / 'input.csv'
    with open(path, 'r', encoding='utf8') as fin:
        reader = csv.reader(fin, delimiter=';')

        for row in reader:
            count, total = orgs.get(row[0], (0, 0))

            count += 1
            total += int(row[1])

            orgs[row[0]] = (count, total)

    salaries = [(total / count, name)
                for name, (count, total) in orgs.items()]
    salaries.sort()

    print('\n'.join(name for _, name in salaries))
