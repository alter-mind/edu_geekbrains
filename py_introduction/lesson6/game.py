import player

def main(): 
    menu_selector()

# функция вывода меню на экран
def print_menu():
    print('-----Игра в угадайку------')
    print('1\t Отгадывать')
    print('2\t Загадывать')
    print('0\t Выход')

# функция получения пунка меню
def get_menu_item():
    try:
        print_menu()
        while True:
            answer = int(input('Ваш выбор: '))
            if answer in range(1,4):
                return answer
            else:
                print('Некорректный выбор')
    except (TypeError, ValueError):
        return get_menu_item()

# функция реализующия выбор пользователя и запускающая нужный модуль
def menu_selector():
    menu = get_menu_item()
    if menu == 1:
        player.play_ask()
    elif menu == 2:
        player.play_answer()
    else:
        print('Вы выбрали выход')

# запуск главной функции
main()