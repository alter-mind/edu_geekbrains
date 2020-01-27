import ex_1, ex_2, ex_3, ex_4, ex_5, ex_6
from view_code import view_code


def print_menu():
    print('Выберите задачу:')
    for i in range(1, 7):
        print(f'{i}\tзадача')
    print('0\tвыход')


def get_menu_item():
    print_menu()
    try:
        item = int(input('Ваш выбор: '))
        if 0 <= item <= 6:
            return item
        else:
            print('Выберите корректный номер задачи')
            return get_menu_item()
    except (TypeError, ValueError):
        print('Нужно выбрать номер задачи от 1 до 6')
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
        elif select == 3:
            ex_3.do()
            view_code('ex_3.py')
        elif select == 4:
            ex_4.do()
            view_code('ex_4.py')
        elif select == 5:
            ex_5.do()
            view_code('ex_5.py')
        else:
            ex_6.do()
            view_code('ex_6.py')


main()
