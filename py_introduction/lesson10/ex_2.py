import random

# создание тестового списка случайной длинны со случайными величинами
def create_list():
    result_list = []
    for i in range(random.randrange(0,10)):
        result_list.append(random.randrange(0,10))
    return result_list

# функция получения случайного значения из списка
def choise_list(some_list):
    if some_list == []: # поверка списка на пустоту
        return None
    else:
        return random.choice(some_list)
