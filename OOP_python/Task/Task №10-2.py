# Реализуйте класс ListInt для хранения списка целых чисел и сделайте его итерируемым так, чтобы значения возвращались
# с конца в начало.

def check_value(fun):
    """Проверка на то что переданные данные имеют тип Int"""

    def wrapper(*args):
        if isinstance(args[1], int):
            return fun(*args)
        else:
            raise TypeError("Неверный тип данных, поддерживается только int")

    return wrapper


class Node:
    """Тип данных который имеет три параметра, _data = непосредственно данные, _next = ссылка на следующий элемент,
    _prev =  ссылка на предыдущий элемент"""

    @check_value
    def __init__(self, value: int):
        self._data = value
        self._next = None  # связь с следующим
        self._prev = None  # связь с предыдущим


class ListInt:
    """ Класс который условно описывает работу списка"""

    def __init__(self, value: int):
        self.__root = Node(value)  # начальная точка списка
        self.__end = self.__root  # последний элемент списка
        self.__current_item = self.__root  # текущий элемент списка (нужен для __next__)
        self.__flag = True  # нужен для вывода первого элемента в списке (нужен для __next__)

    def add(self, value: int):
        """Функция добавления нового элемента в список"""
        self.__end._next = Node(value)  # добавляем в конец новый элемент
        self.__end._next._prev = self.__end  # добавляем в новый элемент ссылку на предыдущий (родителя)
        self.__end = self.__end._next  # устанавливаем указатель последнего элемента в конец
        self.__current_item = self.__end  # устанавливаем указатель последнего элемента в конец (для __next__)

    def __iter__(self):
        return self

    def __next__(self):
        if self.__current_item._prev:
            self.__current_item = self.__current_item._prev
            return self.__current_item._next._data
        if self.__flag:
            self.__flag = False
            return self.__current_item._data
        self.__flag = True
        self.__current_item = self.__end
        raise StopIteration

    def __str__(self):
        return f"{self.__class__.__name__}: {[value for value in self.__iter__()]}"


test = ListInt(1)
test.add(2)
test.add(3)
print(test)
print('________________')
test.add(4)
print(test)
print('________________')
for i in test:
    print(i)
for i in test:
    print(i)
