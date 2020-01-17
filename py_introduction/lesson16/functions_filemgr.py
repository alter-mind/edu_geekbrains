import os
import shutil
import datetime


# Создание файла
def create_file(name, text=None):
    with open(name, 'w', encoding='utf-8') as file:
        if text:
            file.write(text)


# Создание папки
def create_folder(name):
    try:
        os.mkdir(name)
    except FileExistsError:
        print('Данный каталог уже существует')


# Получение списка файлов и папок
def get_list(folders_only=False):
    result = os.listdir()
    if folders_only:
        result = [f for f in result if os.path.isdir(f)]
    print(result)


# Удаление файла или папки
def delete_file(name):
    if os.path.isdir(name):
        os.rmdir(name)
    else:
        os.remove(name)


# Копирование файла или папки
def copy_file(name, new_name):
    if os.path.isdir(name):
        try:
            shutil.copytree(name, new_name)
        except FileExistsError:
            print('Данный каталог уже существует')
    else:
        shutil.copy(name, new_name)


# Сохранение информации о раболе в log.txt
def save_info(message):
    current_datetime = datetime.datetime.now()
    result = f'{current_datetime} - {message}'
    with open('log.txt', 'a', encoding='utf-8') as file:
        file.write(result + '\n')


# Функция для отображения текущего пути
def info_string(current_path):
    return current_path + ' :> '


# Вывод справки на экран
def ask_for_help():
    answer = input('Показать справку по работе с программой? [y/n]: ')
    if answer in ['y', 'Y', '1', 'д', 'Да', 'да', 'ДА', 'yes', 'Yes', 'Yes']:
        with open('help.txt', 'r', encoding='utf-8') as file:
            for line in file:
                print(line.rstrip())
