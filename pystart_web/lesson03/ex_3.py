def my_func(a, b, c):
    return a + b + c - min(a, b, c)


def get_valid(message):
    try:
        return float(input(message))
    except (ValueError, TypeError):
        return get_valid(message)


def do():
    print(my_func(a=get_valid('Введите a: '), b=get_valid('Введите b: '), c=get_valid('Введите c: ')))


if __name__ == '__main__':
    do()
