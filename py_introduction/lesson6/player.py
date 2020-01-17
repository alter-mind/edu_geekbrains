import random

# получение случайного числа в заданном диапазоне
def gen_number(mini, maxi):
    return random.randrange(mini, maxi + 1)

# получение ответа пользователя
def get_answer():
    try:
        answer = int(input('Введите ответ: '))
        while answer < 0:
            print('Нужно ввести целое положительное число в заданном диапазоне')
            answer = int(input('Введите ответ: '))
        return answer
    except (TypeError, ValueError):              # если получено не число обругать пользователя и спросить заново
        print('Нужно вводить ЦЕЛЫЕ, ПОЛОЖИТЕЛЬНЫЕ числа')
        return get_answer()

# выбор уровня сложности
def get_difficalty_level():
    try:
        print('Выберите уровень сложности (0 - 3)')
        while True:
            answer = int(input('Ваш выбор: '))
            if answer in range(4):
                return answer
            else:
                print('Сделайте корректый выбор')
    except (TypeError, ValueError):
        print('Нужно вводить целые положительные числа')
        return get_difficalty_level()

# игра, где пользователь угадывает числа
def play_ask():
    level = get_difficalty_level()
    maxi =10 * 10 ** level                 # расчёт уровня сложности
    mini = 1
    print('Вам нужно будет угадать целое число от 1 до', maxi)
    answer = None
    number = gen_number(mini, maxi)
    steps_counter = 0                       # счётчик попыток
    print('Число загадано, всё готово. Приготовьтесь отвечать, если захотите сдаться введите ноль')
    while True:                            # цикл обрабатывающий ответы пользователя и выводящий подсказки
        steps_counter += 1
        answer = get_answer()
        if answer == number:
            print('Вы угадали')
            print('Сделано попыток:', steps_counter)
            print('Уровень сложности:', level)
            break
        elif answer == 0:
            print('Вы сдались')
            print('Сделано попыток:', steps_counter)
            print('Уровень сложности:', level)
            break
        elif answer > number:
            print('Не угадали, нужно меньше')
            print('Сделано попыток:', steps_counter)
            print('Уровень сложности:', level)
        else:
            print('Не угадали, нужно больше')
            print('Сделано попыток:', steps_counter)
            print('Уровень сложности:', level)

# меню для игры, где компьютер угадывает числа
def answer_menu():
    try:
        print('Угадал?')
        print('1\tДа')
        print('2\tНет, загаданное число больше')
        print('3\tНет, загаданное число меньше')
        print('0\tНе важно. Хочу выйти')
        answer = int(input('Ваш ответ: '))
        if answer not  in range(4):
            answer = answer_menu()
        return answer
    except (TypeError,ValueError):
        print('Нужно вводить целые числа от 0 до 3')
        return answer_menu()

# игра, где компьтер угадывает числа
def play_answer():
    level = get_difficalty_level()
    mini = 1
    maxi = 10 * 10 ** level                # вычисление уровня сложности
    steps_counter = 0                      # счётчик попыток
    print('Загадайте число в диапазоне от {} до {}'.format(mini,maxi))
    print('Всё готово. Дайте подумать')
    while True:
        steps_counter += 1
        number = gen_number(mini,maxi)    # угадывание числа
        print('Предполагаю, что это число', number)
        answer = answer_menu()
        if answer == 1:
            print('Ура!')
            print('Всего попыток:',steps_counter)
            print('Уровень сложности:', level)
            break
        elif answer == 2:
            print('Очень жаль, сейчас ещё подумаю')
            print('Всего попыток:',steps_counter)
            print('Уровень сложности:',level)
            mini = number + 1            # определение новых границ с учётом подсказки
        elif answer == 3:
            print('Очень жаль, сейчас ещё подумаю')
            print('Всего попыток:',steps_counter)
            print('Уровень сложности',level)
            maxi = number - 1            # определение новых границ с учётом подсказки
        else:
            print('Очень жаль, что вам надоела игра.')
            print('Я бы обязательно угадал со следующей попытки')
            breakpoint()
        if (maxi - mini) < 1:           # если с учётом подсказок в диапазон не умещаются цифры - пользователь мухлюет
            print('Мне кажется вы обманываете, такого не может быть')
            print('Я за честную игру')
            break

