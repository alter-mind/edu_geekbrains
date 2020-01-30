def file_to_dict(filename='ex_6.text'):
    list_file = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            list_file.append(line.rstrip().split(':'))
    # работает вот как: в самом внутреннем генераторе из строки list_file[i][1] генерируется список, в котором не цифры
    # заменяются на пробелы. Далее это дело мы при помощи сплит режем, получаем список чисел, но в строковом формате
    # второй генератор делает список уже с числами, и от этого списка берем сумму.
    # Сумма - значение ключа в генераторе словаря
    return {el[0]: sum([int(num) for num in ''.join([ch if '0' <= ch <= '9' else ' ' for ch in el[1]]).split()]) for el
            in list_file}


def do():
    try:
        print(file_to_dict())
    except FileNotFoundError:
        print('Файл не найден')
    except (IndexError, ValueError, TypeError):
        print('Файл содержит некорректные данные')
    except:
        print('Сломалось что-то неожидаемое')


if __name__ == '__main__':
    do()
