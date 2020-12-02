#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

import json


if __name__ == '__main__':
    path = Path.cwd().parent.parent.parent \
        / 'data' / 'datasets' / 'input.json'
    with open(path, 'r', encoding='utf8') as fin:
        dct = json.loads(fin.read())

    popup = dct['menu']['popup']
    menuitem = popup['menuitem']

    for now in menuitem:
        for key in sorted(now):
            print(key, now[key])
