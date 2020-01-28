# создадим случайный список
list_1 = [random.randrange(5) for i in range(random.randrange(10, 11))]
print(list_1)

# создаем пустой словарь для работы в генераторе
# словарь выбран из-за удобного метода setdefault, который позволяет добавлять
# элемент и возвращае его в одном действии.
temp = {}
list_2 = [temp.setdefault(x, x) for x in list_1 if x not in temp]
print(list_2)
