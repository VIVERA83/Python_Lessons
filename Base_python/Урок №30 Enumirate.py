# Путь кодера
# Подвиг 1. Имеется упорядоченный список:
# A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# Перебрать все элементы этого списка с помощью функций enumerate и элементы, стоящие на главной диагонали (имеющие равные индексы), превратить в нули.
# Подвиг 2. Написать свою функцию enumerate, которая бы для словарей возвращала кортеж из трех значений:
# (индекс, ключ, значение)
# Для остальных коллекций работала бы без изменений.
# Подвиг 3. Написать свою функцию enumerate, которая бы позволяла одним циклом for перебирать двумерные (вложенные) упорядоченные списки (как в подвиге 1) и возвращала кортеж из трех значений:
# (строка, столбец, значение)

"""Задание №1"""
print("""
Подвиг 1. Имеется упорядоченный список: A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
         Перебрать все элементы этого списка с помощью функций enumerate и элементы, стоящие на главной диагонали (имеющие равные индексы), превратить в нули.
         """)  # 1.5.9
A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def getPrimer(lst: list):
    # for i, item in enumerate(lst):
    #     for index, value in enumerate(item):
    #         if index == i:
    #             lst[i][index] = 0
    return [0 if index == i else value for i, item in enumerate(lst) for index, value in
            enumerate(item)]  # одномерный список


print(getPrimer(A))

"""Задание №2"""
print("""
Подвиг 2. Написать свою функцию enumerate, которая бы для словарей возвращала кортеж из трех значений:
         (индекс, ключ, значение)
         """)

test_dict = {'a': ord('a'),
             'b': ord('b'),
             'c': ord('c')}

dict_enum = lambda d: tuple((index, *(key, value)) for index, (key, value) in enumerate(d.items()))
print(dict_enum(test_dict))

print("""
Подвиг 3. Написать свою функцию enumerate, которая бы позволяла одним циклом for перебирать двумерные (вложенные) упорядоченные списки (как в подвиге 1) и возвращала кортеж из трех значений:
          (строка, столбец, значение)
""")

for index,value in enumerate(A,1):
    for v in enumerate(value,1):
        print(index,*v, value)