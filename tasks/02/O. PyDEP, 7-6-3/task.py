#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3

from bs4 import BeautifulSoup
import html5lib  # noqa


if __name__ == '__main__':
    http = urllib3.PoolManager()

    r = http.request(
        'GET',
        'https://stepik.org/media/attachments/lesson/209723/5.html'
    )
    soup = BeautifulSoup(r.data.decode('utf8'), 'html5lib')

    result = 0
    for table in soup.find_all('table'):
        for row in table.findChildren('tr'):
            for cell in row.findChildren('td'):
                result += int(cell.get_text())

    print(result)
