#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
import io
import urllib3

from bs4 import BeautifulSoup


if __name__ == '__main__':
    http = urllib3.PoolManager()

    r = http.request(
        'GET',
        'https://stepik.org/media/attachments/lesson/258944/New-York.html'
    )
    soup = BeautifulSoup(r.data.decode('utf8'), 'html.parser')

    data = []
    for count, table in enumerate(
        soup.find_all(
            'table',
            attrs={'class': 'wikitable collapsible collapsed'}
        ),
        1
    ):
        if count == 2:
            for row in table.findChildren('tr'):
                data_row = []
                for cell in row.findChildren(['th', 'td']):
                    data_row.append(cell.text.strip())
                data.append(data_row)

            break

    with io.StringIO() as stream:
        writer = csv.writer(stream, delimiter=',')
        writer.writerows(data)

        result = stream.getvalue().replace('"', '')

    print(result)
