#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import Counter
import urllib3

from bs4 import BeautifulSoup


if __name__ == '__main__':
    http = urllib3.PoolManager()

    r = http.request(
        'GET',
        'https://stepik.org/media/attachments/lesson/209719/2.html'
    )
    soup = BeautifulSoup(r.data.decode('utf8'), 'html.parser')

    counter = Counter()
    for code in soup.find_all('code'):
        text = code.get_text().strip()
        if text:
            counter.update((text,))

    values = [(-count, key) for key, count in counter.items()]
    values.sort()

    min_negative_count = values[0][0]
    result = [values[0][1]]
    for item in values[1:]:
        if item[0] == min_negative_count:
            result.append(item[1])
        else:
            break

    print(' '.join(result))
