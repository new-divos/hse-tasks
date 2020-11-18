#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from pathlib import Path

import openpyxl


if __name__ == '__main__':
    path = Path(__file__).absolute().parent / 'trekking1.xlsx'
    wb = openpyxl.load_workbook(path)

    sheet = wb["Справочник"]

    meals = {}
    metrics = {}
    for row in sheet.rows:
        meal = None

        for cell in row:
            if cell.row == 1:
                if cell.column != 1:
                    metrics[cell.column] = cell.value
            else:
                if cell.column == 1:
                    meal = cell.value
                    meals[meal] = {
                        metric: 0.0 for metric in metrics.values()
                    }
                elif cell.value:
                    value = float(str(cell.value).replace(',', '.'))
                    meals[meal][metrics[cell.column]] = value

    # Получить метрику Ккал на 100.
    metric = metrics[2]

    # Выделить значения данной метрики.
    meals_with_metric = [
        (-metrics[metric], meal) for meal, metrics in meals.items()
    ]
    meals_with_metric.sort()

    for _, meal in meals_with_metric:
        print(meal)
