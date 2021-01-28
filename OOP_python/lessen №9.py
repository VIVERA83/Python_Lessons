# перегрузка операторов: __add__, __iadd__, __getitem__, __setitem__и другие

class Clock:
    __DAY = 86400

    def __init__(self, secs: int):
        if not isinstance(secs, int):
            raise ValueError("Секунды должны быть целым числом")

        self.__secs = secs % self.__DAY


    @staticmethod
    def __getForm(x):
        return str(x) if x > 9 else "0"+str(x)

    def getFormatTime(self):
        s = self.__secs % 60  # секунды
        m = (self.__secs // 60) % 60  # минуты
        h = (self.__secs // 3600) % 24  # часы
        return f"{self.__getForm(h)}:{self.__getForm(m)}:{self.__getForm(s)}"

    def getSeconds(self):
        return self.__secs

    def __add__(self, other):
        if not isinstance(other, Clock):    
            raise ArithmeticError("Правый операнд должен быть типа Clock")
        print("складываем ", self.__secs + other.getSeconds())
        return Clock(self.__secs + other.getSeconds())

    def __iadd__(self, other):
        if not isinstance(other, Clock):
            raise ArithmeticError("Правый операнд должен быть типа Clock")
        self.__secs += other.getSeconds()
        return self

    def __eq__(self, other):
        if not isinstance(other, Clock):
            raise SyntaxError("Правый операнд должен быть типа Clock")
        return self.__secs == other.getSeconds()

    def __nq__(self, other):
        return not self.__eq__(other)

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен быть строкой")

        if item == "hour":
            return (self.__secs // 3600) % 24
        if item == "min":
            return (self.__secs // 60) % 60
        if item == "sec":
            return self.__secs

        return "Неверный ключ"

    def __setitem__(self, key, value):
        if not any([isinstance(key, str), isinstance(value,int)]):
            raise ValueError("ключ должен быть строкой, значение целым числом")

        s = self.__secs % 60  # секунды
        m = (self.__secs // 60) % 60  # минуты
        h = (self.__secs // 3600) % 24  # часы

        if key == "hour":
            self.__secs = s + 60 * m + value * 3600
        if key == "min":
            self.__secs = s + 60 * value + h * 3600
        if key == "sec":
            self.__secs = value + 60 * m + h * 3600



c1 = Clock(10000)
c2 = Clock(10)
print(c1 == c2)
print(c2.getSeconds())
print(c2.getFormatTime())
c2 += c1 +c2
# print(c1.getFormatTime())
print(c2.getFormatTime(), c1.getFormatTime())
if c1 == c2:
    print('получилось')
c2["sec"] = 60
print(c2["min"])
print(c2.getFormatTime())