import os
import shutil

dir_result = 'find_folder'
if not os.path.exists(dir_result):
    os.mkdir(dir_result)

folder_search = r'my_project'
files = []


for r, d, f in os.walk(folder_search):
    for file in f:
        if '.html' in file:
            files.append(os.path.join(r, file))
for path in files:
    folder_new = os.path.join(dir_result, os.path.basename(os.path.dirname(path)))
    if not os.path.exists(folder_new):
        os.mkdir(folder_new)
    save_path = os.path.join(folder_new, os.path.basename(path))
    shutil.copy(path, save_path)
