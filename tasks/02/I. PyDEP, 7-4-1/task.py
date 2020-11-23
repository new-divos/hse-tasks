#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3

from bs4 import BeautifulSoup


if __name__ == '__main__':
    http = urllib3.PoolManager()

    r = http.request(
        'GET',
        'https://stepik.org/media/attachments/lesson/258943/Moscow.html'
    )
    soup = BeautifulSoup(r.data.decode('utf8'), 'html.parser')

    links = set()
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            href = link['href']

            if (href.startswith('/wiki/') or href.startswith('/w/')) and \
                    ':' not in href and \
                    not href.startswith('#') and \
                    '.org' not in href:
                links.add(href)

    print(len(links))
