# 3. Создайте класс Persons для хранения списка уникальных посетителей клуба.
# Сделайте возможность перебора гостей итератором(ми) следующим образом:

# с выводом только их имени;
# с выводом только их возраста;
# с выводом только их фамилии.


class Persons:

    def __check_value(self):
        """Функция которая проверяет корректность переданных данных, перед тем как добавить нового гостя"""

        def wrapper(*args):
            first_name = args[1]
            last_name = args[2]
            age = args[3]
            try:
                if not all([ord(char) in range(1040, 1104) for char in first_name + last_name]):
                    raise ValueError("В написании фамилии и имени допускается использование только русского алфавита")
            except TypeError:
                raise TypeError("Неверный тип данных, должно быть: str")
            try:
                if age <= 0:
                    raise ValueError("Возраст не может быть вещественным числом, отрицательным и равен 0 либо строкой")
            except TypeError:
                TypeError("Неверный тип данных, должно быть: int")
            return self(*args)

        return wrapper

    def __check_key(self):
        def wrapper(*args):
            """Функция проверяет ключ по которому производится вывод данных args[0] =  self, args[1] = key"""
            key = args[1]
            print(key)
            try:
                if key not in args[0].__key.keys():
                    raise KeyError(f"Неверный ключ, доступны значения : {args[0].__key.keys()}")
            except TypeError:
                raise TypeError(f"Неверный тип данных для ключа, доступны значения : {self.__key.keys()}")
            return self(*args)

        return wrapper

    @__check_value
    def __init__(self, first_name: str, last_name: str, age: int):
        self.__persons = set()  # здесь храним уникальный список гостей
        self.__persons.add((first_name, last_name, age))
        self.__num_count = 1  # Кол- во записей(гостей в списке)
        self.__count = -1  # нидекс используется в итераторе
        self.__key = {"first name": 0,
                      "last name": 1,
                      "age": 2,
                      "all": None}
        self.current_key = self.__key["all"]

    @__check_value
    def add(self, first_name: str, last_name: str, age: int):
        self.__persons.add((first_name, last_name, age))
        if self.__num_count == len(self.__persons):
            print(f"Внимание данный гость уже есть в списке {first_name, last_name, age}")
        else:
            self.__num_count += 1

    @__check_key
    def __getitem__(self, key: str):
        self.current_key = key
        return self.__iter__()

    def __iter__(self):
        return self

    def __next__(self):
        self.__count += 1
        try:
            return list(self.__persons)[self.__count] if self.current_key is None else \
            list(self.__persons)[self.__count][
                self.__key[self.current_key]]
        except:
            self.__count = -1
            raise StopIteration


pers = Persons("Смирнов", "Михаил", 30)
pers.add("Алексей", "Федоров", 22)
pers.add("Алексей", "Михайлов", 26)
pers.add("Алексей", "Федоров", 22)  # повтор
pers.add("Александр", "Миронов", 23)
a = pers["age"]  # 26
print(f'a = {a}')

print("Вывод полной информации через метод __iter__")
for values in pers:
    print(values)
print("Вывод по Фамилии через метод __getitem__")
for values in enumerate(pers["last name"], 1):
    print(values)
print("Вывод по Имени через метод __getitem__")
for values in enumerate(pers["first name"], 1):
    print(values)
print("Вывод по возрасту через метод __getitem__")
for values in enumerate(pers["age"], 1):
    print(values)
print("Вывод информации по ключу через метод __iter__")

for index, value in enumerate(pers, 1):
    print(index, value)
