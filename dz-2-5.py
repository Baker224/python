my_price = [57.8, 46.1, 97, 55.01, 104.04, 39.44, 49.56, 108, 106.91, 10.08]
print('ID =', id(my_price))
price_string = ''
for price in my_price:
    price_string += ', '
    price_string += str(int(price))
    price_string += ' руб '
    if (int(price * 100 % 100)) < 10:
        price_string += '0' + str(int(price * 100 % 100))
    else:
        price_string += str(int(price * 100 % 100))
    price_string += ' коп'
print(price_string[2:])
my_price.sort()
print('ID =', id(my_price))
price_string = ''
for price in my_price:
    price_string += ', '
    price_string += str(int(price))
    price_string += ' руб '
    if (int(price * 100 % 100)) < 10:
        price_string += '0' + str(int(price * 100 % 100))
    else:
        price_string += str(int(price * 100 % 100))
    price_string += ' коп'
print(price_string[2:])
my_price_reverse = my_price.copy()
my_price_reverse.sort(reverse=True)
print(my_price_reverse)
for i in my_price_reverse[5:]:
    my_price_reverse.remove(i)
my_price_reverse.sort()
price_string_rev = ''
for price_rev in my_price_reverse:
    price_string_rev += ', '
    price_string_rev += str(int(price_rev))
    price_string_rev += ' руб '
    if (int(price_rev * 100 % 100)) < 10:
        price_string_rev += '0' + str(int(price_rev * 100 % 100))
    else:
        price_string_rev += str(int(price_rev * 100 % 100))
    price_string_rev += ' коп'
print(price_string_rev[2:])
