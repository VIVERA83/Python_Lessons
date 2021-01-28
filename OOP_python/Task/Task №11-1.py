# Создайте функтор для определения порядка сортировки списка p, состоящий из объектов класса Person
# То есть, вызывая функтор (пусть он называется SortKey) с названием поля SortKey("surname"), сортировка выполнялась
# бы по этому свойству. Если указать сразу два значения: SortKey("surname", "forename"), то сортировка делалась бы по
# фамилии, но при их равенстве – по имени.
# (Подсказка: используйте метод sort списка p и его именованный параметр key).

from random import randint


class Test1:
    def __init__(self):
        self.r = randint(0, 50)
        self.b = randint(0, 50)
        self.k = randint(0, 50)


class Person:
    def __init__(self, surname, forename, old):
        self.surname = surname
        self.forename = forename
        self.old = old


class SortKey:
    """Класс функтор который по заданным ключам производит сортировку переданного списка экземпляров классов,
    переданный список должен состоять из однотипных элементов. не допускается списки типа [class Person, class Date],
    так же не поддерживаются стандартные типы данных пример [{1:1}, {2:3}]
    В качестве ключей сортировки используется имена атрибутов класса """

    def __init__(self, *args):
        self.__sortKey = args  # ключевые поля по которым будет проводится сортировка

    def __call__(self, lst:list):
        # Если в параметрах передается пустой список то мы возвращаем пустой список
        if not lst:
            return lst
        # Если хоть один переданный ключ не соответствует атрибутам элементов списка инициализируем исключение и
        # сообщаем об ошибке и возможных атрибутах, в test скидываются ошибочные ключи
        test = [key for key in self.__sortKey if key not in lst[0].__dict__.keys()]
        if test:
            raise KeyError(f"ОШИБКА {tuple(test)} таких ключей нет, в данном списке "
                           f"имеются следующие ключи {tuple(lst[0].__dict__.keys())}")
        return sorted(lst, key=lambda item: [item.__dict__[key] for key in self.__sortKey])


    def __call1__(self, lst):
        """ Вариант где распаковывается список сортируется и потом создаются новый список с новыми классами"""
        # Если в параметрах передается пустой список то мы возвращаем пустой список
        if not lst:
            return lst
        # Если хоть один переданный ключ не соответствует атрибутам элементов списка инициализируем исключение и
        # сообщаем об ошибке и возможных атрибутах, в test скидываются ошибочные ключи
        test = [key for key in self.__sortKey if key not in lst[0].__dict__.keys()]
        if test:
            raise KeyError(f"ОШИБКА {tuple(test)} таких ключей нет, в данном списке "
                           f"имеются следующие ключи {tuple(lst[0].__dict__.keys())}")
        # создаем список в который распаковываем атрибуты (Persons)
        temp = [item.__dict__ for item in lst]
        # сортируем в соответствии с переданными ключами (полями)
        temp = sorted(temp, key=lambda element: [element[key] for key in self.__sortKey if key in element.keys()])
        # Возвращаем отсортированный список, предварительно обратно упаковываем в тод же класс
        # 1 параметр Имя будущего класса
        # 2 Классы от которых новый клас наследуется пример: tuple(Persons, Test1)
        # 3 Список аргументов (Dict)
        return [type(lst[index].__class__.__name__, (lst[index].__class__.__bases__), lst[index].__dict__) for
                index, item in enumerate(temp)]




# Проверка

persons_list = [Person("Иванов", "Иван", 20),
                Person("Петров", "Степан", 21),
                Person("Сидоров", "Альберт", 25),
                Person("Кувыкин", "Иван", 21),
                Person("Абдуллин", "Иван", 28)]

mySort = SortKey("old","forename")

print("Выводим persons_list ДО сортировки")
[print(index, tuple(item.__dict__.values())) for index, item in enumerate(persons_list, 1)]
persons_list = mySort(persons_list)
print("Выводим persons_list ПОСЛЕ сортировки")
[print(index, tuple(item.__dict__.values())) for index, item in enumerate(persons_list, 1)]

test = [Test1() for i in range(4)]
b = SortKey('b', 'k')
a = b(test)

for item in a:
    for key in ['r', 'b', 'k']:
        print(item.__dict__[key], end=' ')
    print()
