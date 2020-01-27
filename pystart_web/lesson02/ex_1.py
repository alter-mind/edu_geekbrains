def do():
    new_list = []
    new_list.append('строка')
    new_list.append(2134)
    new_list.append(('кортеж', 'строк'))
    for i in range(len(new_list)):
        print(f'{i} элемент списка содержит: {new_list[i]}. Данные относятся к типу {type(new_list[i])}')


if __name__ == '__main__':
    do()
