def do():
    month = int(input('Введите номер месяца: '))

    print('Решение через списки')
    winter = [1, 2, 12]
    spring = [3, 4, 5]
    summer = [6, 7, 8]
    autumn = [9, 10, 11]
    if month in winter:
        print('Зима')
    elif month in spring:
        print('Весна')
    elif month in summer:
        print('Лето')
    elif month in autumn:
        print('Осень')
    else:
        print('Похоже, что это не месяц')

    print('Решение через словарь')
    seasons = {'Зима': [1, 2, 12], 'Весна': [3, 4, 5], 'Лето': [6, 7, 8], 'Осень': [9, 10, 11]}
    for key in seasons:
        if month in seasons[key]:
            print(key)
if __name__ == '__main__':
    do()