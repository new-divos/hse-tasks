#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3

from bs4 import BeautifulSoup


if __name__ == '__main__':
    http = urllib3.PoolManager()

    r = http.request(
        'GET',
        'https://stepik.org/media/attachments/lesson/209723/3.html'
    )
    soup = BeautifulSoup(r.data.decode('utf8'), 'html.parser')

    result = 0
    for table in soup.find_all('table'):
        for row in table.findChildren('tr', recursive=False):
            for cell in row.findChildren('td', recursive=False):
                result += int(cell.get_text())

    print(result)
