# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке,
# из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os

def create_dir(dirname):
    try:
        os.mkdir(dirname)
    except FileExistsError:
        print(dirname + ' - каталог существует')


def rm_dir(dirname):
    try:
        os.rmdir(dirname)
    except FileNotFoundError:
        print(dirname + ' - каталога не существует')

# create_dir('dir_1')
# create_dir('dir_9')

# rm_dir('dir_1')
# rm_dir('dir_9')

# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

def print_dir(dirname):
    dirname = os.path.join(os.path.curdir, dirname)

    try:
        for name in os.listdir(dirname):
            if os.path.isdir(name):
                print(name)
    except FileNotFoundError:
        print(dirname + ' - каталога не существует')

# Задача-3:
# Напишите скрипт, создающий копию файла, из которого запущен данный скрипт.

def copy_file():

    from shutil import copyfile

    file_name = os.path.basename(__file__)
    copyfile(file_name, file_name + '.copy')
    print(os.path.basename(__file__))


def chdir(dirname):
    try:
        os.chdir(dirname)
    except FileNotFoundError:
        print(dirname + ' - каталога не существует')

