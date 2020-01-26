def my_func(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print('Делитель не может равняться нулю')


def get_valid(message):
    try:
        return float(input(message))
    except (ValueError, TypeError):
        return get_valid(message)


def do():
    print(f"Ответ: {my_func(get_valid('Введите делимое: '), get_valid('Введите делитель:'))}")


if __name__ == '__main__':
    do()