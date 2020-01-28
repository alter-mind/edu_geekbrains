from itertools import count, cycle


# a) бесконечный итератор, генерирующий целые числа начиная с number
def some_iter(number):
    yield cycle(number)


# b) бесконечный итератор, повторяющий элементы объекта some_list, поддерживающего итерации
def anoter_iter(some_list):
    for el in cycle(some_list):
        yield el
