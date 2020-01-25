def do():
    some_string = input('введите строку из нескольких слов: ')
    str_list = some_string.split()
    for word in str_list:
        print(word[:10])


if __name__ == '__main__':
    do()
