def do():
    common_list = []
    name_list = []
    price_list = []
    amount_list = []
    unit_list = []
    numbers = int(input('Введите количество товаров: '))
    for i in range(1,numbers + 1):
        name = input(f'Введите наименование {i} товара: ')
        price = float(input(f'Введите цену {i} товара: '))
        amount = int(input(f'Введите количество {i} товара: '))
        unit = input(f'Введите единицы измерения {i} товара: ')
        common_list.append((1, {'название': name, 'цена': price, 'колличество': amount, 'ед': unit}))
        name_list.append(name)
        price_list.append(price)
        amount_list.append(amount)
        if unit not in unit_list:
            unit_list.append(unit)
    print('Структура "товары":', common_list)
    print('названия:', name_list)
    print('цены:', price_list)
    print('колличество:', amount_list)
    print('ед:', unit_list)


if __name__ == '__main__':
    do()