import sys
import os
from functions_filemgr import *

if len(sys.argv) > 1:  # Обработка запуска с аргументом
    command = sys.argv[1:]
    cmd = True
    save_info('Запуск с аргументом')
else:  # Обработка запуска без аргумента
    command = [None]
    cmd = False
    save_info('Запуск без аргумента')

current_path = os.getcwd()  # Получение текущего пути для отображения
while command[0] != 'exit':  # Программа работает пока не получит комманду на завершение

    if command[0] == 'crf':  # Создание файла
        if len(command) >= 3:
            create_file(command[1], ' '.join(command[2:]))
        elif len(command) == 2:
            create_file(command[1])
        else:
            print('Аргументы не заданы')
            ask_for_help()
        save_info('Выполнена комманда {}'.format(str(command)))
    elif command[0] == 'del':  # Удаление
        if len(command) > 1:
            for arg in command[1:]:  # Если указано несколько файлов или папок - удалить все
                delete_file(arg)
        else:
            print('Файлы для удаления не заданы')
            ask_for_help()
        save_info('Выполнена комманда {}'.format(str(command)))
    elif command[0] == 'crd':  # Создание папки
        if len(command) > 1:
            create_folder(command[1])
        else:
            print('Имя папки не задано')
            ask_for_help()
        save_info('Выполнена комманда {}'.format(str(command)))
    elif command[0] == 'cp':  # Копирование
        if len(command) == 3:
            copy_file(command[1], command[2])
        else:
            print('Аргументы отсутствуют или заданы не верно')
            ask_for_help()
        save_info('Выполнена комманда {}'.format(str(command)))
    elif command[0] == 'ls':
        get_list()
    elif command[0] == 'ch':  # изменение рабочего каталога
        if len(command) == 2 and not cmd:
            try:
                os.chdir(command[1])
                current_path = command[1]
            except FileNotFoundError:
                print('Данный путь или каталог не существует')
        else:
            print('Аргументы отсутствуют или заданы не верно')
            ask_for_help()
        save_info('Выполнена комманда {}'.format(str(command)))
    else:
        if cmd:
            print('Нет такой команды')
            ask_for_help()
        else:
            print('Консольный файловый менеджер. Для справки введите "help"')

    if cmd:  # Завершение цикла, если программа была вызвана с аргументами
        break

    command = input(info_string(current_path)).split(' ')
save_info('Завершение работы с программой')
