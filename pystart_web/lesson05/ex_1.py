def create_file(filename):
    with open(filename, 'w', encoding='utf-8') as file:
        while True:
            usr_str = input(f'Введите строку для записи в файл {filename}, пустая строка - для завершения: ')
            if usr_str.upper() != '':
                file.write(usr_str + '\n')
            else:
                break


def do():
    create_file(input('Введите имя файла: '))


if __name__ == '__main__':
    do()