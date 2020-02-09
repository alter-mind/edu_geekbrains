def get_valid(message):
    try:
        return float(input(message))
    except (TypeError, ValueError):
        print('Нужно вводить числа')
        return get_valid(message)


class Road:

    def __init__(self):
        self.__length = get_valid('Введите длину дороги в метрах: ')
        self.__width = get_valid('Введите ширину дороги в метрах: ')
        self.__mass = 25
        self.__depth = 1

    def calc(self):
        return self.__length * self.__width * self.__mass * self.__depth


def do():
    road = Road()
    print(road.calc())


if __name__ == '__main__':
    do()
