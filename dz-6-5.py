import sys
from itertools import zip_longest
users, hobby, out = sys.argv[1:]
with open(out, 'w', encoding='utf-8') as f:
    file_users = open(users, encoding='utf-8')
    file_hobby = open(hobby, encoding='utf-8')
    num_lines_users = sum(1 for line in file_users)
    num_lines_hobby = sum(1 for line in file_hobby)
    if num_lines_users < num_lines_hobby:
        exit(1)
    file_users.seek(0)
    file_hobby.seek(0)
    for line_user, line_user_hobby in zip_longest(file_users, file_hobby):
        f.write(f'{line_user.strip()}: '
            f'{line_user_hobby.strip() if line_user_hobby is not None else line_user_hobby}\n')