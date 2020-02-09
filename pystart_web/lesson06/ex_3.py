class Worker(object):
    """Базовый класс"""

    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {'wage': income[0], 'bonus': income[1]}


class Position(Worker):
    def get_full_name(self):
        return ' '.join([self.name, self.surname])

    def get_total_income(self):
        return sum(self._Worker__income.values())


def do():
    pos = Position('John', 'Smith', 'Killer', [100000, 10000])
    print(f'Рабочий {pos.get_full_name()} '
          f'работает на должности {pos.position} '
          f'и получает суммарно {pos.get_total_income()}')


if __name__ == '__main__':
    do()
