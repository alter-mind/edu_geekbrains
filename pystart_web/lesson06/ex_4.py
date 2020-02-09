class Car:
    def __init__(self, speed, color, name, is_police=False):
        self.speed = float(speed)
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self, speed):
        self.speed = speed
        print(f'Автомобиль {self.name} поехал со скоростью {self.speed}')

    def stop(self):
        self.speed = 0
        print(f'Автомобиль {self.name} остановился')

    def turn(self, direction):
        print(f'Автомобиль {self.name} поворачивает {direction}')


class TownCar(Car):
    def go(self, speed):
        self.speed = speed
        print(f'Автомобиль {self.name} поехал со скоростью {self.speed}')
        if speed > 60 and not self.is_police:
            print(f'Автомобиль {self.name} превышает скорость')


class WorkCar(Car):
    def go(self, speed):
        self.speed = speed
        print(f'Автомобиль {self.name} поехал со скоростью {self.speed}')
        if speed > 40 and not self.is_police:
            print(f'Автомобиль {self.name} превышает скорость')


def do():
    car = Car(70, 'blue', 'car')
    police = WorkCar(0, 'police', 'police', is_police=True)
    taxi = TownCar(0, 'yellow', 'taxi')
    car.go(90)
    car.turn('Направо')
    print(f'Автомобиль {car.name} едет со скоростью {car.speed}')
    police.go(120)
    police.stop()
    taxi.go(60)


if __name__ == '__main__':
    do()
