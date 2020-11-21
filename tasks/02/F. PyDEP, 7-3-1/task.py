#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
import urllib3

from bs4 import BeautifulSoup


if __name__ == '__main__':
    http = urllib3.PoolManager()

    r = http.request(
        'GET',
        'https://stepik.org/media/attachments/lesson/258939/webpage.html'
    )
    soup = BeautifulSoup(r.data.decode('utf8'), 'html.parser')

    with open(Path.home() / 'output.txt', 'w', encoding='utf8') as fout:
        for tag in soup.find_all('a'):
            if tag.has_attr('href'):
                print(tag['href'], file=fout)
