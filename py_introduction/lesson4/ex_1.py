my_list_1 = [2,5,8,12,12,4]
my_list_2 = [2,7,12,3]
final_list = []
for number in my_list_1:
    if number not in my_list_2:
        final_list.append(number)
print(final_list)