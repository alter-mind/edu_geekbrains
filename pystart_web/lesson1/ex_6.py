def do():
    first = float(input('Введите расстояние за первый день: '))
    target = float(input('Введите цель: '))
    days = 1
    current = first
    while current < target:
        days += 1
        current *= 1.1
    print(f'На {days}-й день спортсмен достиг результата не менее {target} км. ({current})')


if __name__ == '__main__':
    do()