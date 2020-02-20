class ZerDivErr(Exception):
    def __init__(self, text):
        self.txt = text


def do():
    try:
        print('Частное: ', float(input('Введте делимое: ')) / float(input('Введите делитель: ')))
    except ZeroDivisionError:
        try:
            raise ZerDivErr('Ошибка: деление на 0')
        except ZerDivErr as e:
            print(e)


if __name__ == '__main__':
    do()
