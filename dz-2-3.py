my_list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']

list_index = 0
while list_index < len(my_list):
    if my_list[list_index].isdigit():
        my_list.insert(list_index + 1, '"')
        my_list[list_index] = str(f'{int(my_list[list_index]):02}')
        my_list.insert(list_index, '"')
        list_index += 2
    elif (my_list[list_index].startswith('+') or my_list[list_index].startswith('-')) and my_list[list_index][1:].isdigit():
        my_list.insert(list_index + 1, '"')
        my_list[list_index] = str(f'{my_list[list_index][0]}{int(my_list[list_index][1:]):02}')
        my_list.insert(list_index, '"')
        list_index += 2
    else:
        list_index += 1
output_list = ' '.join(my_list)

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

