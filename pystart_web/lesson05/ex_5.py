import random


def create_file(filename='ex_5.text'):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(' '.join([str(random.randrange(10)) for i in range(random.randrange(10, 100))]))


def sum_file(filename='ex_5.text'):
    with open(filename) as file:
        r_num = file.read().split()
    return sum([float(r_num[i]) for i in range(len(r_num))])


def do():
    try:
        create_file()
        print(sum_file())
    except:
        print('Внезапно что-то пошло не так')
