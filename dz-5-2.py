max_value = 15
odd_to_15 = (n for n in range(1, max_value + 1, 2))
i = 1
while i < max_value:
    print(next(odd_to_15))
