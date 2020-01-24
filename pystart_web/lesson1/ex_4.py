def do():
    number = int(input('Введите целое положительное число для поиска наибольшей цифры: '))
    div = 10
    max_num = number % 10
    while div <= number:
        number = number // 10
        if max_num < number % 10:
            max_num = number % 10
    print(f'Самая большая цифра: {max_num}')


if __name__ == '__main__':
    do()
