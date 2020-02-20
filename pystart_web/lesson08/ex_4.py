from datetime import datetime
from abc import ABC, abstractmethod


class Storage:
    # Данные организованы следующим образом: ключ большого словаря - тип объекта, а значение - словарь с объектами
    # Словарь с объектами устроен следующим образом: ключ - имя конкретного объекта, а значение - список, где нулевой
    # элемент содержит экземпляр объекта, а первый элемент - количество таких объектов.
    # Есть __log, который содержит список строк. Каждая строка - операция на складе.
    def __init__(self):
        self.__log = []
        self.__log.append(f'{datetime.now()} \t ** \t create')
        self.__items = {}

    def update(self, **kwargs):
        for key in kwargs:
            if kwargs[key][0].type() in self.__items:
                self.__items[kwargs[key][0].type()] = self.__dict_mod(self.__items[kwargs[key][0].type()], kwargs[key])
            else:
                self.__items[kwargs[key][0].type()] = self.__dict_mod({}, kwargs[key])
        self.__log.append(f'{datetime.now()} \t + \t {kwargs}')

    @staticmethod
    def __dict_mod(dct, lst):
        if lst[0].name in dct:
            dct[lst[0].name] += lst[1]
        else:
            dct[lst[0].name] = lst
        return dct

    @staticmethod
    def __extract(dct, lst):
        if lst[0].name in dct:
            if dct[lst[0].name][1] > lst[1]:
                dct[lst[0].name][1] -= lst[1]
                return dct, lst
            elif dct[lst[0].name][1] == lst[1]:
                del dct[lst[0].name]
                return dct, lst
            else:
                print(f'Запрошенного количества ({lst[1]}) нет на складе')
                lst[1] = dct[lst[0].name][1]
                del dct[lst[0].name]
                print(f'Выдано сколько было ({lst[1]}):')
                return dct, lst
        else:
            print(f'объекта {lst[0].type} c именем {lst[0].name} нет на складе')
            return None

    # позволяет посмотреть колличество элементов по ключу
    def __getitem__(self, index):
        self.__log.append(f'{datetime.now()} \t ask \t {index}')
        return self.__items[index]

    def deliver(self, **kwargs):
        dct_return = {}
        for key in kwargs:
            if kwargs[key][0].type() in self.__items:
                self.__items[kwargs[key][0].type()], dct_return[kwargs[key][0].name] = self.__extract(
                    self.__items[kwargs[key][0].type()], kwargs[key])
            else:
                print(f'Объекта {kwargs[key][0].type()} нет на складе')
        self.__log.append(f'{datetime.now()} \t - \t {dct_return}')
        return dct_return

    def prnt(self):
        print(self.__items)

    def show_log(self):
        return '\n'.join(self.__log)


class Equipment:
    def __init__(self):
        self.__new = True
        self.__run = False

    def __str__(self):
        return self.name

    def use(self):
        self.__new = False

    def switch_on(self):
        self.__run = True
        self.__new = False

    def switch_off(self):
        self.__run = False

    def info(self):
        return f'Статус устройства {self.name}: \n запущено: {self.__run} \n новое {self.__new}'

    def about(self):
        return f'Устройство класса: {type(self)} с названием {self.name}'

    @abstractmethod
    def type(self):
        pass


class Printer(Equipment):
    def __init__(self, name):
        self.name = name
        Equipment.__init__(self)

    def do(self):
        self.__new = False
        print(f'Принтер {self.name} печатает')

    def type(self):
        return 'printer'


class Scanner(Equipment):
    def __init__(self, name):
        self.name = name
        Equipment.__init__(self)

    def do(self):
        self.__new = False
        print(f'Сканер {self.name} сканирует')

    def type(self):
        return 'scanner'


class Xerox(Equipment):
    def __init__(self, name):
        self.name = name
        Equipment.__init__(self)

    def do(self):
        self.__new = False
        print(f'Ксерокс {self.name} копирует')

    def type(self):
        return 'xerox'


def do():
    printer = Printer('Принтер1')
    print(printer.type())
    storage = Storage()
    storage.update(el=[printer, 5])
    printer1 = Printer('nameP')
    storage.update(el=[printer1, 2])
    scan = Scanner('Сканер')
    xerox = Xerox('Ксерокс')
    storage.update(el1=[xerox, 21], el2=[scan, 12])
    storage.prnt()
    print(storage.deliver(el=[xerox, 10]))
    storage.prnt()
    print(storage.show_log())


if __name__ == '__main__':
    do()