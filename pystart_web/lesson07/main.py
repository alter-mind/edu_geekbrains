import ex_1, ex_2, ex_3
from view_code import view_code


def print_menu():
    print('Выберите задачу:')
    for i in range(1, 4):
        print(f'{i}\tзадача')
    print('0\tвыход')


def get_menu_item():
    print_menu()
    try:
        item = int(input('Ваш выбор: '))
        if 0 <= item <= 3:
            return item
        else:
            print('Выберите корректный номер задачи')
            return get_menu_item()
    except (TypeError, ValueError):
        print('Нужно выбрать номер задачи от 1 до 5')
        return get_menu_item()


def main():
    while True:
        select = get_menu_item()
        if select == 0:
            break
        elif select == 1:
            ex_1.do()
            view_code('ex_1.py')
        elif select == 2:
            ex_2.do()
            view_code('ex_2.py')
        else:
            ex_3.do()
            view_code('ex_6.py')


main()
