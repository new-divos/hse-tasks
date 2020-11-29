#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math
from pathlib import Path
from typing import List, Tuple

from bs4 import BeautifulSoup
import lxml  # noqa


def get_area(coord_lst: List[Tuple[float, float]]) -> float:
    base_lat = coord_lst[0][0]
    base_lon = coord_lst[0][1]

    degree_len = 111300

    new_coord = []
    for now in coord_lst:
        new_coord.append(
            (
                (now[0] - base_lat) * degree_len,
                (now[1] - base_lon) * degree_len * math.sin(base_lat)
            )
        )

    sqr = 0.0
    for i in range(len(new_coord) - 1):
        sqr += new_coord[i][0] * new_coord[i + 1][1] \
               - new_coord[i + 1][0] * new_coord[i][1]

    sqr += new_coord[-1][0] * new_coord[0][1] \
           - new_coord[0][0] * new_coord[-1][1]

    return math.fabs(sqr)


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
                        coords.append(nodes[ref])

                    buildings.append(
                        (
                            int(way['id']),
                            coords,
                        )
                    )

    areas = [
        (building_id, get_area(building_coords))
        for building_id, building_coords in buildings
    ]

    building_id, _ = max(areas, key=lambda item: item[1])
    print(building_id)
