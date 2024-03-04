from os import listdir
from os.path import isfile, basename, join, isdir


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
    if pattern in basename(dirpath):
        yield dirpath

    for child_name in listdir(dirpath):
        child_path = join(dirpath, child_name)
        if isdir(child_path):
            yield from search_function(pattern, child_path)
        elif pattern in child_name:
            yield child_path

