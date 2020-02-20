from abc import abstractmethod


class Cell:
    def __init__(self, cells):
        self.cells = cells

    def __add__(self, other):
        return Cell(self.cells + other.cells)

    def __str__(self):
        return f'Объект класса "Cell" содержит {self.cells} ячеек'

    def __sub__(self, other):
        result = self.cells - other.cells
        if result > 0:
            return Cell(result)
        else:
            print('Так делать нельзя')

    def __mul__(self, other):
        return Cell(self.cells * other.cells)

    def __truediv__(self, other):
        return Cell(round(self.cells / other.cells))

    @abstractmethod
    def make_order(cell, row):
        # В задании не понял, что именно нужно сделать
        # Понял так: метод, принадлежащий классу принимет экземпляр этого класса и колличество ячеек в ряду (каком?)
        # Если предположить, что формируется что-то типа матрицы и в последнюю строку записывается остаток, а нам
        # нужно строкой описать полченную матрицу, то выйдет нечно такое:
        rows = cell.cells // row
        rest = cell.cells - row * rows
        return f'{"".join("*" for i in range(rest))}\n\n{"".join("*" for i in range(rows))}'


def do():
    c1 = Cell(20)
    print(c1)
    c2 = Cell(8)
    print(c2)
    print('c1 + c2')
    print(c1 + c2)
    print('c1 - c2')
    print(c1 - c2)
    print('c2 + c1')
    print(c2 - c1)
    print('c1 * c2')
    print(c1 * c2)
    print('c1 / c2')
    print(c1 / c2)
    print('make_order demo')
    print(Cell.make_order(c1, 8))


if __name__ == '__main__':
    do()
