#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import urllib3


if __name__ == '__main__':
    http = urllib3.PoolManager()

    r = http.request(
        'GET',
        'https://stepik.org/media/attachments/lesson/209717/1.html'
    )
    text = r.data.decode('utf8')

    python_count = text.count('Python')
    cpp_count = text.count('C++')

    print('Python' if python_count >= cpp_count else 'C++')
