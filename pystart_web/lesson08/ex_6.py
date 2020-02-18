from ex_4 import *


def get_valid(message):
    try:
        return int(input(message))
    except:
        print('Неверный ввод')
        return get_valid(message)


def create_in(storage):
    print('Выберите тип объекта, который вы хотите создать:')
    choise = get_valid(' 1 - принтер, 2 - сканер, 3 - ксерокс: ')
    if choise == 1:
        p = Printer(input('Введите имя принтер: '))
        storage.update(el=[p, get_valid('Введите количество: ')])
    elif choise == 2:
        s = Scanner(input('Введите имя сканера: '))
        storage.update(el=[s, get_valid('Введите количество: ')])
    elif choise == 3:
        x = Xerox(input('Введите имя ксерокса: '))
        storage.update(el=[x, get_valid('Введите количество: ')])
    else:
        print('Неверный выбор, ничего создано не будет')
    return storage


def do():
    storage = Storage()
    storage = create_in(storage)
    storage.prnt()


if __name__ == '__main__':
    do()
