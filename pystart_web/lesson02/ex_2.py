def do():
    new_list = []
    numbers = int(input('Введите количество элементов списка: '))
    for i in range(numbers):
        new_list.append(input(f'Введите {i} элемент списка: '))
    print(new_list)
    print('А теперь обмен')
    for i in range(1, len(new_list), 2):
        new_list.insert(i - 1, new_list.pop(i))
    print(new_list)


if __name__ == '__main__':
    do()
