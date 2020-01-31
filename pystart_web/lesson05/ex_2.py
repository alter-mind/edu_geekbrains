def file_to_list(filename='ex_2.text'):
    list_file = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            list_file.append(line.rstrip().split())
    return list_file


def do():
    try:
        list_file = file_to_list()
        if len(list_file) != 0:
            print(f'Строк в файле: {len(list_file)}')
            for i in range(len(list_file)):
                print(f'Количество слов в {i+1}-й строке: {len(list_file[i])}')
        else:
            print('Пустой файл')
    except (FileExistsError, FileNotFoundError):
        print('Нет такого файла')


if __name__ == '__main__':
    do()
