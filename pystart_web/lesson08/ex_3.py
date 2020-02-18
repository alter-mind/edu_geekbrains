class MyException(Exception):
    def __init__(self, text):
        self.txt = text


def ListNum(lst):
    new_lst = []
    for el in lst:
        try:
            new_lst.append(float(el))
        except ValueError:
            try:
                raise MyException(f'Элемент: "{el}" не является числом и не был добавлен в список')
            except MyException as e:
                print(e)
    return new_lst


def do():
    user_lst = []
    print('Вводите поочередно элементы списка. Для выхода введите "Q"')
    while True:
        el = input('Введите ещё элемент: ')
        if el.upper() == 'Q':
            break
        else:
            user_lst.append(el)
    print(ListNum(user_lst))


if __name__ == '__main__':
    do()
