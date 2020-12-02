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

    ways = []
    for way in soup.find_all('way'):
        ways.append(
            (
                way['id'],
                len(tuple(way('nd'))),
            )
        )

    max_id, _ = max(ways, key=lambda item: item[1])
    print(max_id)
