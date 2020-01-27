import random


def do():
    my_list = [random.randrange(1, 10) for i in range(random.randrange(2, 5))]
    my_list.sort(reverse=True)
    print('Исходный набор чисел:', my_list)
    numbers = int(input('Введите колличество натуральных чисел для добавления в список: '))
    for i in range(numbers):
        number = int(input(f'Введите {i}-е число для добаления в список. Если недоело - введите 0: '))
        if number == 0:
            break
        elif number > 0:
            meet = True
            for j in range(len(my_list)):
                if number > my_list[j]:
                    my_list.insert(j, number)
                    meet = False
                    break
            if meet:
                my_list.append(number)
        else:
            print('Отрицательные числа не являются натуральными')
        print(my_list)


if __name__ == '__main__':
    do()
