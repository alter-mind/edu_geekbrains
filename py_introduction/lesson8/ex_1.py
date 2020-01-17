def about(name, age, city):
    return '{}, {} год(а), проживает в городе {}'.format(name,age,city)
name = input('Введите имя: ')
age = input('Введите возраст: ')
city = input('Введите город: ')
print(about(name,age,city))