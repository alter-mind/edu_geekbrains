def main():
    player = init_entity('Введите данные игрока')
    enemy = init_entity('Введите данные врага')
    atack(player,enemy, lambda damage: damage // enemy['armour'])
    print(enemy)


def init_entity(note):
    print(note)
    entity = {'name':None,'health':None, 'damage':None, 'armour':None}
    try:
        entity['name'] = input('Введите имя: ')
        entity['health'] = int(input('Введите величину здоровья (целое, положительное): '))
        entity['damage'] = int(input('Введите величину урона (целое, положительное: '))
        entity['armour'] = float(input('Введите величину брони (вещественное число, больше 1): '))
        return entity
    except (TypeError, ValueError):
        print('Величины должны быть целыми положительными числами. Попробуйте ещё раз')
        return init_entity(note)

def atack(player,enemy,function):
    enemy['health'] -= function(player['damage'])

main()