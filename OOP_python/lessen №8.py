"""Множественное наследование"""


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


class Styles:
    def __init__(self, ):
        print("Конструктор Styles")
        super().__init__()


class Pos:
    def __init__(self, *args):
        print("Конструктор Pos")
        super().__init__()


class Line(Pos, Styles):
    def __init__(self, sp: Point, ep: Point, color="red", width=1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self._width = width

    def draw(self):
        print(f"Рисование линии: {self._sp}, {self._ep}, {self._color}, {self._width}")


# l = Line(Point(11, 10), Point(252, 300), "green", 5)
# l.draw()
# print(Line.mro())


#

