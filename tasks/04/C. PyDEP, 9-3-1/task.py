#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import os
import urllib3


if __name__ == '__main__':
    api_key = os.getenv('API_KEY', '')
    if not api_key:
        raise ValueError("Illegal API key")

    http = urllib3.PoolManager()

    # Запросить информацию о наборе.
    r = http.request(
        'GET',
        f'https://apidata.mos.ru/v1/datasets/3288?api_key={api_key}'
    )
    info = json.loads(r.data.decode('utf8'))

    # Загрузить записи набора.
    url_lst = [
        "https://apidata.mos.ru/v1/datasets/3288/rows?",
        f"api_key={api_key}&",
        f"$top={info['ItemsCount']}",
    ]
    r = http.request('GET', ''.join(url_lst))

    rows = json.loads(r.data.decode('utf8'))

    count = 0
    for row in rows:
        cells = row.get('Cells')
        if cells:
            duration = cells.get('DurationOfLighting')
            if duration:
                parts = list(map(int, duration.split(':', maxsplit=1)))
                hours = parts[0] + parts[1] / 60
                if hours >= 12:
                    count += 1

    print(count)
