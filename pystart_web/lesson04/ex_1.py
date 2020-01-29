from sys import argv


def print_note():
    print('Неверно заданы аргументы. Запустите с aргументом "help" для справки')


if len(argv) == 4:
    try:
        print(f'Заработная плата составит: {float(argv[1]) * float(argv[2]) + float(argv[3])}')
    except:
        print_note()
elif len(argv) == 2:
    if argv[1] == 'help':
        print('Скрипт для рассчёта заработной платы')
        print('Аргументы (числа): ')
        print('1\tвыработка в часах')
        print('2\tставка')
        print('3\tпремия')
    else:
        print_note()
else:
    print_note()
