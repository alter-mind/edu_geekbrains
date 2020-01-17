my_list_1 = [2,2,5,12,8,2,12]
# создание словаря с колючами из списка
my_dict_1 = dict.fromkeys(set(my_list_1),0)
# подсчёт количества повторов каждого значения в списке с занесением резельтата в значение словаря
for number in my_list_1:
    my_dict_1[number] += 1
# финальный список создаём из ключей значение которых равны 1
final_list = []
for number in my_dict_1.keys():
    if my_dict_1[number] == 1:
        final_list.append(number)
print(final_list)