def my_func(x, y, simple=True):
    if simple:
        return x ** y
    elif y == 0:
        return 1
    else:
        res = 1
        for i in range(abs(y)):
            res *= x
        return res if y > 0 else 1 / res


def get_valid(message):
    try:
        return float(input(message))
    except (ValueError, TypeError):
        return get_valid(message)


def do():   
    x = get_valid('Введите x: ')
    y = int(get_valid('Введите y: '))
    print(f'Вычисление простым способом: {my_func(x, y)}, сложным способом: {my_func(x, y, simple=False)}')


if __name__ == '__main__':
    do()
