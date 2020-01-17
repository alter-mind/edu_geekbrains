age = int(input(('Введите ваш возраст: ')))
weight = float(input(('Введите ваш вес: ')))
if age < 30 and weight in range(50,121):
    print('Вы в хорошем состоянии')
elif age in range(30,41) and not(weight in range(50,121)):
    print('Вам следует заняться собой')
elif age > 40 and not(weight in range(50,121)):
    print('Вам требуется врачебный осмотр')
else:
    print('Для вас не нашлось подходящего диагноза, вы можете придумать его самостоятельно')