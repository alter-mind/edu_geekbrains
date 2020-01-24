def do():
    time = int(input('Введите время в секундах: '))
    print(f' часов:{time // 3600 :02d} минут:{time % 3600 // 60 :02d} секунд:{time % 60 :02d}')


if __name__ == '__main__':
    do()
