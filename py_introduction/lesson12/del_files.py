def delete_files():
    import os
    if input('Удалить все сгенерированные файлы? [1 - да, всё остальное - нет]: ') == '1':
        os.remove('group.pickle')
        os.remove('group.json')