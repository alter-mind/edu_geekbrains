def file_to_list(filename='ex_7.text'):
    list_file = []
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            list_file.append(line.rstrip().split())
    profit = {el[0]: int(el[2]) - int(el[3]) for el in list_file}
    mean = lambda lst: sum(lst) / len(lst)
    average = {'avg_prof': mean([val for val in profit.values() if val > 0])}
    return [profit, average]


def list_to_json(lst, filename='ex_7.text'):
    import json
    new_name = filename.split('.')
    new_name[1] = 'json'
    new_filename = '.'.join(new_name)
    with open(new_filename, 'w', encoding='utf-8') as file:
        json.dump(lst, file)


def do():
    try:
        list_to_json(file_to_list())
    except FileNotFoundError:
        print('Файл не найден')
    except (TypeError, ValueError, IndexError):
        print('Файл содержит некорректные данные')
    except:
        print('Сломалось что-то невообразимое')


if __name__ == '__main__':
    list_to_json(file_to_list())
