class Complex:
    def __init__(self, real=0, im=0):
        self.real = real
        self.im = im

    def __add__(self, other):
        return Complex(self.real + other.real, self.im + other.im)

    def __mul__(self, other):
        return Complex(self.real * other.real - self.im * other.im, self.real * other.im + self.im * other.real)

    def __str__(self):
        return f'{self.real} + {self.im}i'


def do():
    c = Complex(2, 3)
    c1 = Complex(-1, 1)
    print(c1 * c)
    print(c1 + c)


if __name__ == '__main__':
    do()