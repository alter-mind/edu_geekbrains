import random

# создадим случайный список
list_1 = [random.randrange(100) for i in range(random.randrange(15, 25))]
print(list_1)

# в задании неточность, а делаю в последние минуты. Я так понял, что сравнивать между
# собой нужно элементы исходного списка.
list_2 = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1[i - 1]]
print(list_2)
