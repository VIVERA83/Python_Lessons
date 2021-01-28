# 1. Создайте базовый класс «Стол» и дочерние: «Прямоугольные столы» и «Круглые столы». Через конструктор базового
# класса передавайте размер поверхности стола: для прямоугольного – ширина и длина, для круглого – радиус.
# В дочерних классах реализуйте метод вычисления площади поверхности стола.
# 2. Создайте класс Animal (животное) и разные производные от него подклассы: Fox, Bird, Cat, Dog и т.п.
# Реализуйте у них общий метод say(), который бы возвращал звук, издаваемый этим животным. Создайте кортеж из
# нескольких этих экземпляров классов, переберите их в цикле и выведите в консоль их звуки (вызовите метод say()).

class Table:
    def __init__(self, width_or_radius: (int, float), length: (int, float) = None):
        if Table.__check_input(width_or_radius, length):
            if width_or_radius and length:
                self.width = width_or_radius
                self.length = length
            else:
                self.radius = width_or_radius

    @staticmethod
    def __check_input(width_or_radius: (int, float), length: (int, float)) -> (bool, ValueError):
        if isinstance(width_or_radius, (int, float)):
            if isinstance(length, (int, float)) or not length:
                return True

        raise ValueError(f'Неверный тип данных, принимается только Int и Float')


class Rectangular_Table(Table):
    def __init__(self, width: (int, float), length: (int, float)):
        super().__init__(width, length)

    def square(self) -> (int, float):
        return self.width * self.length


class Circle_Table(Table):
    def __init__(self, radius: (int, float)):
        super().__init__(radius)

    def square(self) -> (int, float):
        return self.radius ** 2 * 3.14



from random import choice, randint


class Animal:
    def __init__(self):
        self.nickname = randint(0, 10)

    def Say(self):
        raise NotImplementedError("Метод должен быть переопределен в дочернем классе")

class Fox(Animal):
    __voice = 'Я хитрая лисичка'

    def Say(self):
        print(Fox.__voice)

class Bird(Animal):
    __voice = 'Я птичка невеличка'

    def Say(self):
        print(Bird.__voice)

class Cat(Animal):
    __voice = 'Я котик, мяу '

    def Say(self):
        print(Cat.__voice)

class Dog(Animal):
    __voice = 'Я собачка, верный друг'

    def Say(self):
        print(Dog.__voice)

animals = [choice([Fox(), Bird(), Cat(), Dog()]) for _ in range(10)]

for i in animals:
    print(i.__class__.__name__)
    i.Say()
