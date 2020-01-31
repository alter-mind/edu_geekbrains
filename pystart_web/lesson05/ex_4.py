def file_to_list(filename='ex_4.text'):
    list_file = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            list_file.append(line.rstrip().split())
    return list_file, filename


# вот с этой функцией косяк. Если передавать напрямую возвращаемый первой функцией кортеж
# то она принимает его первым параметром и ищет второй. Как сделать иначе не придумал, поэтому сделал костыль
def create_mod_file(args):
    # Костыль
    list_file = args[0]
    filename = args[1]
    # добавление '_new' перед именем файла для записи
    new_name = filename.split('.')
    new_name[0] += '_new'
    new_filename = '.'.join(new_name)
    # обработкаданных и запись нового файла
    things_to_change = ['первый', 'второй', 'третий', 'четвертый']
    with open(new_filename, 'w', encoding='utf-8') as new_file:
        for i in range(4):
            list_file[i][0] = things_to_change[i]
            new_file.write(' '.join(list_file[i]) + '\n')


def do():
    try:
        create_mod_file(file_to_list())
    except FileNotFoundError:
        print('Запрашиваемый файл не найден')
    except FileExistsError:
        print('Не удалось записать модифицированый файл на диск')
    except (ValueError, TypeError, IndexError):
        print('Исходный файл содержит некорректные данные')
    except:
        print('Сломалось что-то ещё или недостаточно прав для работы в каталоге')


if __name__ == '__main__':
    do()
