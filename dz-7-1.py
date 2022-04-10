import os

pattern = {'my_project': ['settings', 'mainapp', 'adminapp', 'authapp']}
for root, folders in pattern.items():
    if os.path.exists(root):
        print(root, 'папка существует')
        for folder in folders:
            current_dir = os.path.join(root, folder)
            try:
                os.makedirs(current_dir)
                print(root, '/', folder, 'папка создана')
            except FileExistsError:
                print(root, '/', folder, 'папка существует')
    else:
        print(root, 'папка создана')
        for folder in folders:
            cur_dir = os.path.join(root, folder)
            os.makedirs(current_dir)
            print(root, '/', folder, 'папка создана')
