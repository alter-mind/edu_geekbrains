def get_number():
    try:
        number = float(input('Введите число в диапазоне от 1 до 100: '))
        return number if 1 <= number <= 100 else get_number() # если число не в диапазоне спрашиваем ещё раз
    except ValueError: #если пользователь ввёл не число обработать исключение и получить число.
        print('Нужно вводить числа')
        return get_number()

def some_f(number):
    print(number)
    if number == 13: # вызвать исключение если число 13
        raise ValueError
    else:
        return number**2

print(some_f(get_number()))