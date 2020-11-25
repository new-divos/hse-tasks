#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3

from bs4 import BeautifulSoup


if __name__ == '__main__':
    http = urllib3.PoolManager()

    r = http.request(
        'GET',
        'https://stepik.org/media/attachments/lesson/258944/New-York.html'
    )
    soup = BeautifulSoup(r.data.decode('utf8'), 'html.parser')

    for count, table in enumerate(
        soup.find_all(
            'table',
            attrs={'class': 'wikitable collapsible collapsed'}
        ),
        1
    ):
        if count == 2:
            print(table)
