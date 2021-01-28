# 1. Напишите класс Point3D для хранения координат в трехмерном пространстве (x, y, z). Реализуйте перегрузку
# операторов сложения, вычитания, умножения и деления для этого класса. Также сделайте возможность сравнения координат
# между собой и запись/считывание значений через ключи: “x”, “y”, “z”.

# 2. Напишите класс Matrix для работы с матрицами. Реализуйте перегрузку операторов сложения и вычитания для матриц
# равных размеров. Перегрузите оператор умножения для матриц, которые могут быть перемножены. Также сделайте
# возможность сравнения матриц между собой (на равенство и неравенство).
def matrix_addition(a, b):
    n = len(a)
    return [[a[i][j] + b[i][j] for j in range(n)] for i in range(n)]

# 3. Напишите класс Complex для работы с комплексными числами. Реализуйте операторы сложения, вычитания и умножения.
# Также сделайте возможность присвоения действительных и мнимых значений через ключи «rel» и «img» и через
# свойства rel, img, реализованных с помощью дескрипторов.

# Task_1
from math import sqrt


class Point3D:
    def __init__(self, x, y, z):
        if not all([isinstance(item, (int, float)) for item in (x, y, z)]):
            raise ValueError("Координаты должны быть типа Int или Float")
        self.__x = x
        self.__y = y
        self.__z = z

    def check(self):
        def wrapper(*args, **kwargs):
            if not isinstance(args[1], Point3D):
                raise ArithmeticError("Оба операнда должны быть типа Point3D")
            return self(*args, **kwargs)

        return wrapper

    @property
    def getPoint(self):
        return tuple(self.__dict__[key] for key in self.__dict__.keys())

    @check
    def __add__(self, other):
        return Point3D(*[self.__dict__[key] + value for key, value in other.__dict__.items()])

    @check
    def __iadd__(self, other):
        for key, value in other.__dict__.items():
            self.__dict__[key] += value
        return self

    @check
    def __sub__(self, other):
        return Point3D(*[self.__dict__[key] - value for key, value in other.__dict__.items()])

    @check
    def __isub__(self, other):
        for key, value in other.__dict__.items():
            self.__dict__[key] -= value
        return self

    @check
    def __mul__(self, other):
        return Point3D(*[self.__dict__[key] * value for key, value in other.__dict__.items()])

    @check
    def __imul__(self, other):
        for key, value in other.__dict__.items():
            self.__dict__[key] *= value
        return self

    @check
    def __truediv__(self, other):
        if not all([value for value in other.__dict__.values()]):
            raise ZeroDivisionError(f"Деления на 0 {other.__dict__.values()}")
        return Point3D(*[self.__dict__[key] / value for key, value in other.__dict__.items()])

    def __itruediv__(self, other):
        return self.__truediv__(other)

    @check
    def __eq__(self, other):
        return all([self.__dict__[key] == value for key, value in other.__dict__.items()])

    def __ne__(self, other):
        return not self.__eq__(other)

    @check
    def __gt__(self, other):
        return sqrt(sum([pow(value, 2) for value in self.__dict__.values()])) > \
               sqrt(sum([pow(value, 2) for value in other.__dict__.values()]))

    @check
    def __le__(self, other):
        return sqrt(sum([pow(value, 2) for value in self.__dict__.values()])) >= \
               sqrt(sum([pow(value, 2) for value in other.__dict__.values()]))

    def __getitem__(self, item):
        if not isinstance(item, str):
            raise ValueError("Ключ должен пыть типа str")
        if self.__dict__.get(f"_{self.__class__.__name__}__{item}"):
            return self.__dict__.get(f"_{self.__class__.__name__}__{item}")
        raise KeyError("Доступные ключи: x, y, z")

    def __setitem__(self, key, value):
        if not all([isinstance(key, str), isinstance(value, (int, float))]):
            raise ValueError("Ключ (__key)  должен пыть типа str, __value =должен пыть типа int или float")
        if self.__dict__.get(f"_{self.__class__.__name__}__{key}"):
            self.__dict__[f"_{self.__class__.__name__}__{key}"] = value
        else:
            raise KeyError("Доступные ключи: x, y, z")

#test
point1 = Point3D(1, 2, 1)
point2 = Point3D(1, 2, 2)
print(point1.getPoint)
print(point1.getPoint)
print(point2.getPoint)
point1 *= point2
print('*', point1.getPoint)

point1 /=  point2
point1['x'] = 10
print(point1['x'])
