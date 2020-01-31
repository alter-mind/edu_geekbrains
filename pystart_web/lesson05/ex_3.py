def get_file_date(filename='ex_3.text'):
    list_file = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            list_file.append(line.rstrip().split())
    return list_file


def do():
    try:
        list_file = get_file_date()
        total_pay = 0
        for i in range(len(list_file)):
            total_pay += float(list_file[i][1])
        if float(list_file[i][1]) < 20000:
            print(f'Зарплата сотрудника по фамилии {list_file[i][0]} меньше 20000')
        print(f'Средняя зарплата сотрудников составляет {total_pay / len(list_file)}')
    except FileNotFoundError:
        print('Указанный файл не найден')
    except (TypeError, ValueError, IndexError):
        print('Указанный файл найден, но содержит некорректные данные')


if __name__ == '__main__':
    do()
