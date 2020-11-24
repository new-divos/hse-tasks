#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from typing import List
import urllib3

from bs4 import BeautifulSoup


def get_inner_links(
        http: urllib3.PoolManager,
        url: str
) -> List[str]:
    r = http.request('GET', url)
    soup = BeautifulSoup(r.data.decode('utf8'), 'html.parser')

    result = []
    for link in soup.find_all('a'):
        if link.has_attr('href'):
            href = link['href']

            if (href.startswith('/wiki/') or href.startswith('/w/')) and \
                    ':' not in href and \
                    not href.startswith('#') and \
                    '.org' not in href:
                result.append(href)

    return result


if __name__ == '__main__':
    http = urllib3.PoolManager()

    moscow_links = get_inner_links(
        http,
        'https://stepik.org/media/attachments/lesson/258943/Moscow.html'
    )
    new_york_links = get_inner_links(
        http,
        'https://stepik.org/media/attachments/lesson/258944/New-York.html'
    )

    print(len(moscow_links), len(new_york_links))
