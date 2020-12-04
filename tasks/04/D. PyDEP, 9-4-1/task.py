#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
import json
from pathlib import Path
import warnings

import openpyxl


if __name__ == '__main__':
    path = Path.cwd().parent.parent.parent \
        / 'data' / 'datasets' / 'data-25290-2019-09-30.xlsx'

    warnings.simplefilter("ignore")
    wb = openpyxl.load_workbook(path)
    warnings.simplefilter("default")

    sheet = wb["Sheet0"]

    areas = OrderedDict()
    columns = {}
    for row in sheet:
        info = {}
        for cell in row:
            if cell.row == 1:
                columns[cell.column] = cell.value
            else:
                info[columns[cell.column]] = cell.value

        if not info:
            continue

        adm_area = info.get('AdmArea')
        if adm_area:
            districts = areas.get(adm_area, OrderedDict())

            district = info.get('District')
            if district:
                addresses = districts.get(district, [])

                address = info.get('Address')
                if address:
                    addresses.append(address)

                    districts[district] = addresses
                    areas[adm_area] = districts

    with open(Path.home() / 'output.json', 'w', encoding='utf8') as fout:
        json.dump(areas, fout, ensure_ascii=False)
