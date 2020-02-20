class Data:
    @classmethod
    def det_int(cls, string):
        return int(''.join(string.split('-')))

    @staticmethod
    def valid(number):
        s_num = str(number)
        day = int(s_num[:2])
        month = int(s_num[2:4])
        year = int(s_num[4:])
        if 1 <= month <= 12:
            if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
                return True if day <= 31 else False
            elif month == 2:
                if year % 4 == 0:
                    return True if day <= 29 else False
                else:
                    return True if day <= 28 else False
            else:
                return True if day <= 30 else False
        else:
            return False


def do():
    print(Data.det_int('12-13-14'))
    print(Data.valid(131415))


if __name__ == '__main__':
    do()
