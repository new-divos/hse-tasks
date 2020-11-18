#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from collections import OrderedDict
import math
from pathlib import Path
from typing import Dict, Tuple

import openpyxl


def calculate(
        meals: Dict[str, Dict[str, float]],
        metrics: Dict[int, str],
        menu: Dict[str, int]
) -> Tuple[int, ...]:
    calculation = []
    for meal, weight in menu.items():
        meal_metrics = meals[meal]

        meal_calculation = []
        for metric in metrics.values():
            meal_calculation.append(
                weight * meal_metrics[metric] / 100
            )

        calculation.append(tuple(meal_calculation))

    calculation = list(zip(*calculation))
    return tuple(
        int(math.floor(sum(item))) for item in calculation
    )


if __name__ == '__main__':
    path = Path(__file__).absolute().parent / 'trekking3.xlsx'
    wb = openpyxl.load_workbook(path)

    sheet = wb["Справочник"]

    meals = {}
    metrics = OrderedDict()
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

    sheet = wb["Раскладка"]

    day_menu = OrderedDict()
    for row in sheet.rows:
        day = 0
        meal = None

        for cell in row:
            if cell.row != 1:
                if cell.column == 1:
                    day = cell.value
                elif cell.column == 2:
                    meal = cell.value
                elif cell.column == 3:
                    menu = day_menu.get(day, {})
                    weight = menu.get(meal, 0)
                    weight += cell.value
                    menu[meal] = weight
                    day_menu[day] = menu

    for menu in day_menu.values():
        calories, proteins, fats, carbohydrates = calculate(
            meals,
            metrics,
            menu
        )

        print(
            "{} {} {} {}".format(
                calories,
                proteins,
                fats,
                carbohydrates,
            )
        )
