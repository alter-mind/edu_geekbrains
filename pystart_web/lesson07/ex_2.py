from abc import ABC, abstractmethod


class Dress(ABC):
    @abstractmethod
    def rate(self):
        pass

    def __add__(self, other):
        return self.rate() + other.rate()

    def __radd__(self, other):
        try:
            return self.rate() + other.rate()
        except:
            return self.rate() + other

    def __iadd__(self, other):
        try:
            return self.rate() + other.rate()
        except:
            return self.rate() + other

    def __str__(self):
        return f'{self.name} {self.rate()}'


class Coat(Dress):
    def __init__(self, v, name='Coat'):
        self.name = name
        self.v = v

    def rate(self):
        return self.v / 6.5 + 0.5


class Suit(Dress):
    def __init__(self, h, name='Suit'):
        self.name = name
        self.h = h

    def rate(self):
        return 2 * self.h + 0.3


class DressPack(ABC):
    def __init__(self, *args):
        self.lst = list(args)

    @property
    def total_rate(self):
        return sum(self.lst)


def do():
    c1 = Coat(48)
    c2 = Coat(60)
    s1 = Suit(1.70)
    s2 = Suit(1.80)
    print(c1, c2, c1 + c2)
    print(s1, s2, s1 + s2)
    print(DressPack(c1, c2, s1, s2).total_rate)


if __name__ == '__main__':
    do()
