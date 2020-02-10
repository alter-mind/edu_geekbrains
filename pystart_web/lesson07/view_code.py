def view_code(filename):
    try:
        if input('показать исходный код задачи? [y/n]') == 'y':
            with open(filename, 'r', encoding='utf-8') as file:
                for line in file:
                    print(line.rstrip())
    except:
        print(f'файл {filename} не существует или что-то сломалось')
