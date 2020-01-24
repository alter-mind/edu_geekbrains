def do():
    gain = float(input('Введите значение прибыли: '))
    costs = float(input('Введите значение издержек: '))
    profit = gain - costs
    if profit > 0:
        print(f'Чистая прибыль: {profit}')
        staff = int(input('Введите количество сотрудников: '))
        print(f'Прибыль в пересчёте на сотруднка {profit / staff}')
    else:
        print(f'Фирма понесла убытки: {profit}')


if __name__ == '__main__':
    do()
