#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

from bs4 import BeautifulSoup
import lxml  # noqa


if __name__ == '__main__':
    path = Path(__file__).parent.parent.parent.parent \
        / 'data' / 'maps' / 'map2.osm'

    with open(path, 'r', encoding='utf8') as fin:
        xml = fin.read()
    soup = BeautifulSoup(xml, 'lxml')

    without_tag_cnt, with_tag_cnt = 0, 0
    for node in soup.find_all('node'):
        if len(tuple(node('tag'))):
            with_tag_cnt += 1
        else:
            without_tag_cnt += 1

    print(without_tag_cnt, with_tag_cnt)
