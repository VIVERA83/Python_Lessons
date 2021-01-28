"""переопределение и перегрузка методов, абстрактные методы"""


class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f"({self.__x}, {self.__y})"

    def isDigit(self):
        if (isinstance(self.__x, int) or isinstance(self.__x, float)) and \
                (isinstance(self.__y, int) or isinstance(self.__y, float)):
            return True
        return False

    def isInt(self):
        if isinstance(self.__x, int) and isinstance(self.__y, int):
            return True
        return False


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = "red", width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def setCoords(self, sp: Point, ep: Point):
        if sp.isDigit() and ep.isDigit():
            self._sp = sp
            self._ep = ep
        else:
            print("Координаты должны быть числами")

    def draw(self):
        raise NotImplementedError("Метод должен быть создан в дочернем классе")


class Line(Prop):
    def drawLine(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")

    def setCoords(self, sp: Point, ep: Point = None):
        if not ep:
            if sp.isInt():
                self._sp = sp
            else:
                print("Координата должна быть целочисленной")
        else:
            if sp.isInt() and ep.isInt():
                Prop.setCoords(self, sp, ep)
            else:
                print("Координаты должны быть целочисленными")


l = Line(Point(11, 2), Point(10, 20))
# l.drawLine()
l.setCoords(Point(111, 11))
l.drawLine()
l.draw()





# Задание по декораторам
# Не работает с вещественными числами, из за того что функция checkInput точку и запятую востпренимает как строку,
# если поменять то все будет огонек
from math import sqrt


def getStekSqrt(fun):
    stek = {}

    def wrapper(n):
        if not stek.get(n):
            stek.setdefault(n, fun(n))
        return stek.get(n)

    return wrapper


mysqrt = getStekSqrt(sqrt)
checkInput = lambda x: int(x) if x.isdigit() else 0
while True:
    n = checkInput(input('Введите число, для подсчета квадратного корня, для выхода введите чушь '))
    if not n: break
    print(f'Квадратный корень из {n} = {mysqrt(n)}')

print('Список подсчитанных корней:')
for key, value in mysqrt.__closure__[1].cell_contents.items():
    print(f'Корень из {key} = {str(value)[0:5]}')
