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

    nodes = {}
    for node in soup.find_all('node'):
        nodes[int(node['id'])] = (
            float(node['lat']),
            float(node['lon']),
        )

    buildings = []
    for way in soup.find_all('way'):

        refs = []
        for nd in way('nd'):
            refs.append(int(nd['ref']))

        if len(nodes) > 1 and refs[0] == refs[-1]:
            for tag in way('tag'):
                if tag['k'] == 'building' and tag['v']:
                    coords = []
                    for ref in refs:
                        coords.append("({}, {})".format(*nodes[ref]))

                    buildings.append(f"{way['id']}\n[{', '.join(coords)}]")

    with open(Path.home() / 'output.txt', 'w', encoding='utf8') as fout:
        fout.write('\n'.join(buildings))
