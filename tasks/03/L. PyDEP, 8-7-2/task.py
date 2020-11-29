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

    buildings = []
    for way in soup.find_all('way'):

        nodes = []
        for nd in way('nd'):
            nodes.append(int(nd['ref']))

        if len(nodes) > 1 and nodes[0] == nodes[-1]:
            for tag in way('tag'):
                if tag['k'] == 'building' and tag['v']:
                    buildings.append(way['id'])
                    break

    print('\n'.join(buildings))
