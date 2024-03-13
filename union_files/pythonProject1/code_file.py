from pprint import pprint


count_files = 3
file_name_1 = '1.txt'
file_name_2 = '2.txt'
file_name_3 = '3.txt'
union_file = 'union_file.txt'


def sort_files_by_lines(*files):
    files_with_lines = [(file, sum(1 for line in open(file, encoding='utf-8'))) for file in files]
    sorted_files = sorted(files_with_lines, key=lambda x: x[1])
    return [file[0] for file in sorted_files]


def write_sorted_files(sorted_files):
    with open(union_file, 'w', encoding='utf-8') as f:
        for i, file_name in enumerate(sorted_files, start=1):
            f.write(f"{file_name}\n{i}\n")
            with open(file_name, 'r', encoding='utf-8') as file:
                for j, line in enumerate(file, start=1):
                    if line.strip():
                        f.write(f"{line}")
            f.write('\n')

def rewrite_union_file(union_file):#ф-кция удаления пустых строк, 2.txt при перезаписи имеет 2ую пустую строку
    with open(union_file, 'r+', encoding='utf-8') as f:
        lines = f.readlines()
        f.seek(0)
        f.truncate()
        for line in lines:
            if line.strip():
                f.write(line)


# Пример использования функции
union_file = 'union_file.txt'
rewrite_union_file(union_file)
