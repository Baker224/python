import sys

price_add = sys.argv[1]

file = open('bakery.csv', 'a', encoding='utf-8')
file.write(price_add + '\n')
