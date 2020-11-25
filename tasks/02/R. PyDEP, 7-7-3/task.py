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
        if count > 3:
            break

        data_table = []
        for row in table.findChildren('tr'):
            data_row = []
            for cell in row.findChildren(['th', 'td']):
                data_row.append(cell.text.strip())
            data_table.append(data_row)
        data.append(data_table)

    result = []
    for data_table in data:
        with io.StringIO() as stream:
            writer = csv.writer(stream, delimiter=',')
            writer.writerows(data_table)

            result.append(stream.getvalue().replace('"', ''))

    print('\n'.join(result))
