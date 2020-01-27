def get_sum(message, sum_=0):
    num_list = input(message).split()
    flag = True
    try:
        for number in num_list:
            if number.upper() == 'Q':
                flag = False
                print('*', flag)
                break
            sum_ += float(number)
        return sum_, flag
    except (TypeError, ValueError):
        print('В строке присутствует недопустымый символ, вычисления приостановлены.'
              'Ряд просуммирован до недопустимого символа')
        return sum_, flag


def do():
    print('Введите ряд чисел для суммирования через пробел. Для выхода последним символом используйте "Q"')
    counter = 1
    sum_, proceed = get_sum(f'Последовательность {counter}: ')
    print(proceed)
    while proceed:
        counter += 1
        sum_, proceed = get_sum(f'Последовательность {counter}: ', sum_)
        print(proceed)
        print(f'За {counter} итераций сумма составила: {sum_}')


if __name__ == '__main__':
    do()
