class Stationery:
    def __init__(self, title='Stationery'):
        self.title = title

    def draw(self):
        print('Запуск отрисовки')


class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки объекта {self.title} типа {type(self)}')


class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки объекта {self.title} типа {type(self)}')


class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки объекта {self.title} типа {type(self)}')


def do():
    pen = Pen('pen')
    pen.draw()
    pencil = Pencil('pencil')
    pencil.draw()
    handle = Handle('handle')
    handle.draw()


if __name__ == '__main__':
    do()
