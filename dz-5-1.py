def odd_nums(max_value):
    for numb in range(1, max_value + 1, 2):
        yield numb


value_max = 15
odd_to_15 = odd_nums(value_max)
i = 1
while i < value_max:
    print(next(odd_to_15))
