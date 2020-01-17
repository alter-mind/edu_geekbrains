import random

# создание списка случайной длинны (от 10 до 20) со случайными числами в диапазоне от -99 до 99
number_list = [random.randrange(-99,100) for number in range(random.randrange(10,21))]
print(number_list)

result = [number for number in number_list if number % 3 == 0 and number > 0 and number % 4 != 0]
print(result)