import pickle
import json
from del_files import delete_files

my_favorite_group_from_picle = {}
my_favorite_group_from_json = {}

with open('group.pickle','rb') as file:
    my_favorite_group_from_picle = pickle.load(file)
    print('from pickle\n',my_favorite_group_from_picle)

with open('group.json','r',encoding='utf-8') as file:
    my_favorite_group_from_json = json.load(file)
    print('from json\n',my_favorite_group_from_json)

# удаление созданных файлов, чтобы они не попали в git
delete_files()