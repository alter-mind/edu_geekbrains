from itertools import count


# немного не понял задание. Описано про факториал, а в примере вызова
# судя по имени речь идёт о числах фибоначчи. Пусть будет факториал
def fact_gen():
    ans = 1
    for i in count(1):
        if i > 15:
            break
        ans *= i
        yield ans


print([x for x in fact_gen()])
