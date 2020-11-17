#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import csv
from pathlib import Path


if __name__ == '__main__':
    shops = {}

    path = Path(__file__).absolute().parent / 'input.csv'
    with open(path, 'r', encoding='utf8') as fin:
        reader = csv.reader(fin, delimiter=';')

        meals = None
        for row in reader:
            if meals is None:
                meals = row
            else:
                prices = {}
                for i, price in enumerate(row[1:], 1):
                    prices[meals[i]] = float(price)

                shops[row[0]] = prices

    ordered = []
    for shop, meals in shops.items():
        for meal, price in meals.items():
            ordered.append((price, meal, shop))

    ordered.sort()
    print(f"{ordered[0][1]}\n{ordered[0][2]}")
