import sys

edit_index, new_val = sys.argv[1:]
file = open('bakery.csv', 'r+')
tmp_file = open('bakery.tmp', 'w+')
change = False
for i, line in enumerate(file, 1):
    if i == int(edit_index):
        tmp_file.write(f'{new_val}\n')
        change = True
    else:
        tmp_file.write(line)
if not change:
    exit('error')

tmp_file.seek(0)

file.truncate(0)
for line in tmp_file:
    file.write(line)
tmp_file.close()
