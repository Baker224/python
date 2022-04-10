import os
import yaml

with open("config.yaml") as file_yaml:
    data_file = yaml.safe_load(file_yaml)


def create_data(data):
    for folder, folder_downs in data.items():
        if not os.path.exists(folder):
            os.mkdir(folder)
        os.chdir(folder)
        for folder_down in folder_downs:
            if isinstance(folder_down, dict):
                create_data(folder_down)
            else:
                if not os.path.exists(folder_down):
                    if '.' in folder_down:
                        with open(folder_down, 'w') as f:
                            f.write('')
    else:
        os.chdir('../')


create_data(data_file)
