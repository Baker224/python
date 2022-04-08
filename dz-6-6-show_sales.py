import sys

nums = sys.argv[1:]
file = open('bakery.csv', encoding='utf-8')
if len(nums) > 1:
    start_index = int(nums[0])
    end_index = int(nums[1])
elif len(nums) == 0:
    start_index = 0
    end_index = sum(1 for line in file)
    file.seek(0)
else:
    start_index = int(nums[0])
    end_index = sum(1 for line in file)
    file.seek(0)
for index, line in enumerate(file):
    if start_index <= index + 1 <= end_index:
        print(line.strip())
