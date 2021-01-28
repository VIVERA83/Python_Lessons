"""Задание №1"""
# Напишите две функции создания списка из четных чисел от 0 до N (N – аргумент функции):
# [0, 2, 4, …, N]
# с помощью метода append и с помощью инструмента list comprehensions (генератор списков). Через декоратор определите
# время работы этих функций.

from time import time


def getRunTime(fun):
    def wrapper(*args):
        start = time()
        res = fun(*args)
        print('Время работы функуии:', time() - start)
        return res

    return wrapper


@getRunTime
def getEvenNumbers_one(n):
    listnum = []
    for i in range(n + 1):
        if not i % 2:
            listnum.append(i)
    return listnum


@getRunTime
def getEvenNumbers_two(n):
    return [i for i in range(n + 1) if not i % 2]


N = 100000
getEvenNumbers_one(N)
getEvenNumbers_two(N)

"""Задание № 2"""
# Напишите декоратор для кэширования результатов работы функции вычисления квадратного корня положительного
# целочисленного значения x. То есть, при повторном вызове функции (через декоратор) с одним и тем же аргументом,
# результат должен браться из кэша, а не вычисляться заново.
# (Подсказка: здесь следует использовать замыкание для хранения кэша).

from math import sqrt

def getStekSqrt(fun):
    stek = {}
    def wrapper(n):
        if not stek.get(n):
            res = fun(n)
            stek.setdefault(n, res)
        return stek.get(n)
    return wrapper

mysqrt = getStekSqrt(sqrt)

checkIinput = lambda x: int(x) if x.isdigit() else 0
while True:
    n = checkIinput(input('Введите число, для подсчета квадратного корня, для выхода введите введите чушь '))
    if not n: break
    print(f'Квадратный корень из {n} = {mysqrt(n)}')

lst = dict(mysqrt.__closure__[1].cell_contents)  # запомни может пригодиться
print('Список подсчитанных корней:')
for i, y in lst.items():
    print(f'Корень из {i} = {y}')

# print(dir(getStekSqrt.__closure__))

# from math import sqrt
#
# def getСache(a):
#     x = [sqrt(i) for i in range(a+1)]
#     def wrapper(b):
#         print('a=',a)
#         print('b=',b)
#         if b in range(a) :
#             print('Значение а есть кэше', x[b])
#         else:
#             print('a != b', sqrt(b))
#         return 'что ни будь понял'
#     return wrapper
#
# q=getСache(16)
# print(q(9))
#
# """счетчик вызова"""
# def counter():
#     count = 0
#     def add ():
#         nonlocal count
#         count+=1
#         return count
#     return add
#
# index = counter()
# for i in range(100):
#     index()
# print(index())
# index=counter()
# print(index())
#
# """ замыкание обращение к переменным замкнутым в функции замыкания из глобольной зоны"""
#
# def names(name=[]):
#     def kto(newName):
#         midlename= ' Олегович'
#         nonlocal name
#         name.append(newName+midlename)
#         return name
#     return kto
#
# lst = names()
# while True:
#     i=lst(input('Введите имя, для выхода нажмите Enter :'))
#     if i[len(i)-1]==' Олегович':
#         del i[len(i)-1]
#         break
# print(i)

"""лекция"""
# from time import time
# def getNod(a, b):
#     print(a,b)
#     if b > a:
#         a, b = b, a
#     if b > 0:
#         a, b = b, a % b
#         a = getNod(a, b)
#     return a
#
#
# def newGetNod(a, b):   # моя функция после прохождения codewars
#          return b if a % b == 0 else newGetNod(b, a % b)
#
# def testTime(fn):
#     def wrapper(*args):
#         st = time()
#         a=fn(*args)
#         dt =time()-st
#         print('Время выполнения функции', dt,' секунд')
#         return a ,10
#     return wrapper
#
# test1 =testTime(newGetNod)
#
# print(test1(285,20))
