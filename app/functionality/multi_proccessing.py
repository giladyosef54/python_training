from os import listdir
from os.path import join


def get_file_sum(filepath):
    with open(filepath) as file:
        file_sum = 0
        for line in file.readlines():
            file_sum += int(line)
    return file_sum


def format_result(filename, file_sum):
    return {'file name': filename, 'sum': file_sum}


def iterate_files_of_dir(dirpath):
    result = []
    for filename in listdir(dirpath):
        filepath = join(dirpath, filename)
        file_sum = get_file_sum(filepath)
        file_result = format_result(filename, file_sum)
        result.append(file_result)
    return result
