def about_user(name, surname, birth_date, city, phone_number, e_mail):
    print(
        f'Имя:{name}, фамилия: {surname}, дата рождения: {birth_date}, город: {city}, номер телефона: {phone_number}, e-mail: {e_mail}')


def do():
    name = input('Введите имя пользователя: ')
    surname = input('Введите фамилию пользователя: ')
    birth_date = input('Введите день рождения пользователя: ')
    city = input('Введите город пользователя: ')
    phone_number = input('Введите номер телефона пользователя: ')
    e_mail = input('Введите e-mail пользователя: ')
    about_user(name=name, city=city, surname=surname, birth_date=birth_date, e_mail=e_mail, phone_number=phone_number)


if __name__ == '__main__':
    do()
