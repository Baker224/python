cube_list = []
i = 0
for i in range(1, 1000, 2):
    i = i ** 3
    cube_list.append(i)
print(cube_list)
sum_cube = 0
for number_part in cube_list:
    number = number_part
    sum_part = 0
    while number_part != 0:
        sum_part = sum_part + (number_part % 10)
        number_part = number_part // 10
    if sum_part % 7 == 0:
        sum_cube = sum_cube + number
print('Сумма чисел из списка делящихся нацело на 7 = ', sum_cube)

sum_cube = 0
for number_part in cube_list:
    number_part = number_part + 17
    number = number_part
    sum_part = 0
    while number_part != 0:
        sum_part = sum_part + (number_part % 10)
        number_part = number_part // 10
    if sum_part % 7 == 0:
        sum_cube = sum_cube + number
print('Сумма чисел из списка+17 делящихся нацело на 7 = ', sum_cube)