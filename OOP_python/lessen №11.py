# Что такое функторы и как они реализуются. Метод __call__. Создание собственных менеджеров контекста.
# Методы __enter__ и __exit__. Ключевое слово with.

class Counter:
    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        self.__counter += 1
        print(self.__counter)
        return self.__counter


class StripChars:
    def __init__(self, char):
        self.__char = char

    def __call__(self, *args: str, **kwargs):
        if not isinstance(args[0], str):
            raise ValueError("Аргумент должен быть строкой")
        return args[0].strip(self.__char)


def StripChars_def(char):
    def StringStrip(string):
        if not isinstance(string, str):
            raise ValueError("Аргумент должен быть строкой")
        return string.strip(char)

    return StringStrip


s1 = StripChars_def("?:!. ;")
print(s1("Hello World! ?"))

# Менеджир контекста __enter__() и  __exit__()

filename = "lessen_11.txt"
try:
    with open(filename) as fp:
        for string in fp:
            print(string)
except:
    print(f"Файл {filename} не  найден, будет создан новый")
    fp = open(filename, "w")
    fp.close()


class DefenderVector:
    def __init__(self, v: list):
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:] # делаем копию а не ссылку
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(exc_type, exc_val, exc_tb)
        if exc_type is None:
            self.__v[:] = self.__temp
        # return True



v1 = [1,2,3]
v2 = [1,2,3]
# Так как в __exit__ стоит True, исключение не передается, и мы по хорошому не знаем об ошибке, поэтому лучше что бы
# __exit__ возвращал информацию об ошибке, для ее быстрой локализации
# with DefenderVector(v1) as dv:
#     for i in range(len(dv)):
#         dv[i] += v2[i]

# правельней вот так
try:
    with DefenderVector(v1) as dv:
        for i in range(len(dv)):
            dv[i] += v2[i]
except Exception as e:
    print(e) # list index out of range
print(v1)
