import json
from itertools import zip_longest

dict_user_hobby = {}
file_users = open('users.csv', encoding='utf-8')
file_hobby = open('hobby.csv', encoding='utf-8')
num_lines_users = sum(1 for line_user in file_users)
num_lines_hobby = sum(1 for line_hobby in file_hobby)
if num_lines_users < num_lines_hobby:
    exit(1)
file_users.seek(0)
file_hobby.seek(0)
for line_user, line_user_hobby in zip_longest(file_users, file_hobby):
    dict_user_hobby[line_user.strip()] = line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby
with open('homework6-3.json', 'w', encoding='utf-8') as f:
    json.dump(dict_user_hobby, f, ensure_ascii=False)
print(dict_user_hobby)
