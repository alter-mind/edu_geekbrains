import random
import math

#создание списка для задачи с помощью генератора
numbers_list = [random.randrange(-9,10) for i in range(random.randrange(10,21))]
print(numbers_list)

def get_sqare_list(input_list):
    return [math.sqrt(number) if number >= 0 else number for number in input_list]

print(get_sqare_list(numbers_list))