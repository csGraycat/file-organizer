#  sort the files in a directory by extension

import os
# Get the list of all files and directories
path = input("Insert path to the folder: ")
dir_list = os.listdir(path)

for filename in dir_list:
    if os.path.isfile(path + '/' + filename):
        last_dot = filename[::-1].index('.')
        extension = filename[-last_dot:-1] + filename[-1]
        dir_name = extension.upper()
        if dir_name not in dir_list:
            os.mkdir(path + '//' + dir_name)
            dir_list.append(dir_name)
        try:
            os.rename(path + '//' + filename, path + '//' + dir_name + '//' + filename)
        except FileExistsError as e:
            print(e)