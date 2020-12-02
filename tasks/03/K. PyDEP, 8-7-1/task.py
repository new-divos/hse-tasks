#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

from bs4 import BeautifulSoup
import lxml  # noqa


if __name__ == '__main__':
    path = Path(__file__).parent.parent.parent.parent \
        / 'data' / 'maps' / 'mapcity.osm'

    with open(path, 'r', encoding='utf8') as fin:
        xml = fin.read()
    soup = BeautifulSoup(xml, 'lxml')

    for idx, node in enumerate(soup.find_all('node')):
        if idx >= 100:
            break

        print(f"{node['id']} {node['lat']} {node['lon']}")
