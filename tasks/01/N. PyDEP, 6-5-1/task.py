#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path
from typing import List

import openpyxl


def mean(values: List[int]) -> float:
    return sum(values) / len(values)


def median(values: List[int]) -> float:
    values = sorted(values)
    if len(values) & 1:
        return float(values[len(values) >> 1])
    else:
        return (values[len(values) >> 1 - 1] +
                values[len(values) >> 1]) / 2


if __name__ == '__main__':
    path = Path(__file__).absolute().parent / 'salaries.xlsx'
    wb = openpyxl.load_workbook(path)

    sheet = wb.active

    professions = {}
    regions = {}
    for row in sheet.rows:
        region = None

        for cell in row:
            if cell.row == 1:
                if cell.column != 1:
                    professions[cell.column] = (cell.value, [])
            else:
                if cell.column == 1:
                    region = cell.value
                    regions[region] = []
                else:
                    regions[region].append(cell.value)

                    profession, salaries = professions[cell.column]
                    salaries.append(cell.value)
                    professions[cell.column] = (profession, salaries)

    # Поиск региона с максимальной медианной зарплатой.
    salary_by_regions = [
        (region, median(salaries)) for region, salaries in regions.items()
    ]
    region_with_max_median_salary, _ = max(
        salary_by_regions,
        key=lambda item: item[1]
    )

    # Поиск профессии с максимальной средней зарплатой.
    salary_by_professions = [
        (profession, mean(salaries))
        for profession, salaries in professions.values()
    ]
    profession_with_max_mean_salary, _ = max(
        salary_by_professions,
        key=lambda item: item[1]
    )

    print(
        "{} {}".format(
            region_with_max_median_salary,
            profession_with_max_mean_salary
        )
    )
