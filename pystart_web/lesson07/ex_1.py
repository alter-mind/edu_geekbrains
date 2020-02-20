class Matrix:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        return '\n'.join(map(str, ['\t'.join(map(str, el)) for el in self.lst]))

    def __getitem__(self, item):
        return self.lst[item]

    def get_dimension(self):
        return len(self.lst), len(self.lst[0])

    def __add__(self, other):
        if self.get_dimension() == other.get_dimension():
            return Matrix(
                [[self.lst[i][j] + other[i][j] for j in range(len(self.lst[i]))] for i in range(len(self.lst))])
        else:
            return None


def do():
    m1 = Matrix([[1 for i in range(5)] for x in range(5)])
    m2 = Matrix([[(i+1) ** x for i in range(5)] for x in range(5)])
    print('m1')
    print(m1)
    print('m2')
    print(m2)
    print('m1 + m2')
    print(m1 + m2)


if __name__ == '__main__':
    do()