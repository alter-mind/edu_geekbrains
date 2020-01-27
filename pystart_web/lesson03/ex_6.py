def int_func(user_str):
    return user_str[:1].upper() + user_str[1:]


def int_func_str(user_str):
    return ' '.join([int_func(line) for line in user_str.split()])


def do():
    print(int_func_str(input('Введите строку из нескольких слов, чтобы протестировать: ')))


if __name__ == '__main__':
    do()