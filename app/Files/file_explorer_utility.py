from os import listdir
from os.path import isfile, basename, join


def directory_listing(dirpath, indent = '', full_path = True):
    indent += '\t'
    content = dirpath*full_path + basename(dirpath)*(not full_path) + ':\n'

    for name in listdir(dirpath):
        if isfile(join(dirpath,name)):
            content += indent + 'file - ' + name + '\n'
        else:
            content += indent + 'dir - ' + directory_listing(join(dirpath,name), indent, False)
    return content


def read_file_by_generator(filepath):
    with open(filepath) as file:
        file_generator = (line for line in file.readlines())
        for line in file_generator:
            print(line, end='')


def search_function(pattern, dirpath):
    if pattern in basename(dirpath): yield basename(dirpath)
    for name in listdir(dirpath):
        if isfile(join(dirpath,name)):
            if pattern in basename(dirpath): yield basename(dirpath)
        else:
            search_function(join(dirpath,name))

