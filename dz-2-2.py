my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
my_list_new = []

for value in my_list:
    if value.isdigit():
        my_list_new.append('"')
        my_list_new.append(str(f'{int(value):02}'))
        my_list_new.append('"')
    elif (value.startswith('+') or value.startswith('-')) and value[1:].isdigit():
        my_list_new.append('"')
        my_list_new.extend([str(f'{value[0]}{int(value[1:]):02}')])
        my_list_new.append('"')
    else:
        my_list_new.append(value)
output_list = ' '.join(my_list_new)

space_index = []
for space, letter in enumerate(output_list):
    if letter == '"':
        space_index.append(space)
for space in range(len(space_index)):
    if space % 2 == 0:
        space_index[space] = space_index[space] + 1
    else:
        space_index[space] = space_index[space] - 1
for del_space in reversed(space_index):
    output_list = output_list[:del_space] + output_list[del_space + 1:]
print(output_list)