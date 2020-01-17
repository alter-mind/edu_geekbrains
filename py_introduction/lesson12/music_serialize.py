import pickle
import json
from del_files import delete_files

my_favorite_group = {'name':'Г.М.О',
                     'tracks':['Последний месяц осени','Шапито'],
                     'Albums':[{'name':'Делать панк-рок','year':2016},
                               {'name':'Шапито', 'year':2014}]}

with open('group.pickle','wb') as file:
    pickle.dump(my_favorite_group,file)

with open('group.json','w', encoding='utf-8') as file:
    json.dump(my_favorite_group, file)

# функция удаления сгенерированных файлов, чтобы они не попали в git
delete_files()
