# simple class inheritance

# class Point:
#     def __init__(s, x=0, y=0):
#         s.__x = x
#         s.__y = y
#
#     def __str__(s):
#         return f'{s.__x, s.__y}'
#
#
# class Line:
#     def __init__(s, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         s._sp = sp
#         s._ep = ep
#         s._color = color
#         s._width = width
#
#     def drawLine(s):
#         print(f'Рисование линии: {s._sp}, {s._ep}, {s._color}, {s._width}')
#
#
# class Rect:
#     def __init__(s, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         s._sp = sp
#         s._ep = ep
#         s._color = color
#         s._width = width
#
#     def drawLine(s):
#         print(f'Рисование прямоугольника: {s._sp}, {s._ep}, {s._color}, {s._width}')

# модификация
#
# class Point:
#     def __init__(s, x=0, y=0):
#         s.__x = x
#         s.__y = y
#
#     def __str__(s):
#         return f'{s.__x, s.__y}'
#
# class Prop:
#     def __init__(s, sp: Point, ep: Point, color: str = 'red', width: int = 1):
#         s._sp = sp
#         s._ep = ep
#         s._color = color
#         s._width = width
#
# class Line:
#     def __init__(s, *args):
#         print(f'Переопределение конструктора Line')
#         Prop.__init__(s, *args) # не лучший вариант, опасчен при множественном наследовании
#
#
#
#     def drawLine(s):
#         print(f'Рисование линии: {s._sp}, {s._ep}, {s._color}, {s._width}')
#
#
# class Rect(Prop):
#     def drawLine(s):
#         print(f'Рисование прямоугольника: {s._sp}, {s._ep}, {s._color}, {s._width}')

# МОДИФИКАЦИЯ 2
class Point:
    def __init__(self, x=0, y=0):
        self.__x = x
        self.__y = y

    def __str__(self):
        return f'({self.__x}, {self.__y})'


class Prop:
    def __init__(self, sp: Point, ep: Point, color: str = 'red', width: int = 1):
        self._sp = sp
        self._ep = ep
        self._color = color
        self.__width = width

    def getWidth(self):
        return self.__width


class Line(Prop):
    def __init__(self, *args):
        print(f'Переопределение конструктора Line')
        super().__init__(*args)
        self.__width = 5

    def drawLine(self):
        print(f'Рисование линии: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}')


class Rect(Prop):
    def drawLine(self):
        print(f'Рисование прямоугольника: {self._sp}, {self._ep}, {self._color}, {self.getWidth()}')

# l = Line( Point(11, 22), Point(22,33))
# l.drawLine()
# r = Rect(Point(10, 20), Point(30, 80))
# r.drawLine()
#
# print(type(l.drawLine()))
#
# Задачки
# 1. Создайте суперкласс «Персональные компьютеры» и на его основе подклассы: «Настольные ПК» и «Ноутбуки».
# В базовом классе определите общие свойства: размер памяти, диска, модель, CPU. А в производных классах уникальные
# свойства:
#
# для настольных: монитор, клавиатура, мышь, их габариты; и метод для вывода этой информации в консоль;
# для ноутбуков: габариты, диагональ экрана; и метод для вывода этой информации в консоль.
# 2. Повторите это задания для суперкласса «Человек» и подклассов «Мужчина» и «Женщина». Подумайте, какие общие
# характеристики можно выделить в суперкласс и какие частные свойства указать в подклассах.

class Base_configuration:
    def __init__(self,memory: int = 16, disk: int = 500, model: str = 'Home computer' , CPU: str = 'Intel'   ):
        self.memory_size = memory
        self.disk_size = disk
        self.model = model
        self.cpu = CPU

class Notebook(Base_configuration):
    def __init__(self, display, type_matrix,*args):
        self.display = display
        self.type_matrix = type_matrix
        super().__init__(*args)



class Desktop_computer(Base_configuration):
    def __init__(self, case_type, power_unit, *args):
        self.case_type = case_type
        self.power_unit = power_unit
        super().__init__(*args)

    def printSpecification(self):
        print(self.__dict__)
        for key, items in self.__dict__.items():
            key = key[key.find('__')+1:].replace('_', ' ').ljust(12)
            print(key,items)


pc =Desktop_computer('ATX',600)
laptop = Notebook(17,'IPX')

pc.printSpecification()
