def main():
    player = init_entity('Введите данные игрока')
    enemy = init_entity('Введите данные врага')
    atack(player,enemy)
    print(enemy)


def init_entity(note):
    print(note)
    entity = {'name':None,'health':None, 'damage':None}
    try:
        entity['name'] = input('Введите имя: ')
        entity['health'] = int(input('Введите величину здоровья (целое, положительное): '))
        entity['damage'] = int(input('Введите величину урона (целое, положительное: '))
        return entity
    except (TypeError, ValueError):
        print('Величины должны быть целыми положительными числами. Попробуйте ещё раз')
        return init_entity(note)

def atack(player,enemy):
    enemy['health'] -= player['damage']

main()