import csv
from pathlib import Path
import sys


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

    min_price = sys.float_info.max
    target_shop = target_meal = None

    for shop, meals in shops.items():
        for meal, price in meals.items():
            if min_price > price:
                min_price = price
                target_shop = shop
                target_meal = meal

    print(f"{target_shop}, {target_meal}, {min_price}")
