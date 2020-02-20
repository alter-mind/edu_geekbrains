import time


class TrafficLigth:
    color = None

    def __init__(self):
        self.color = 'red'
        self.__color_switch = ['Red', 'Yellow', 'Green']
        self.__color_times = [7, 2, 10]
        self.__start_time = time.time()

    def switch(self):
        print(self.__time_passed())
        summ = sum(self.__color_times)
        mark = TrafficLigth.__time_passed(self) % summ
        if mark in range(self.__color_times[0]):
            self.color = self.__color_switch[0]
        elif mark in range(self.__color_times[0], sum(self.__color_times[:2])):
            self.color = self.__color_switch[1]
        else:
            self.color = self.__color_switch[2]

    def __time_passed(self):
        return int(time.time() - self.__start_time)


def do():
    traffic_1 = TrafficLigth()
    print('Чтобы преключать светофор нажимайте Enter. Для выхода введите любой символ')
    while True:
        if input() == '':
            traffic_1.switch()
            print(traffic_1.color)
        else:
            break


if __name__ == '__main__':
    do()