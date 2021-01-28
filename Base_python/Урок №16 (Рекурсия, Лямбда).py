print("""
Задание №3 Написать функцию вычисления факториала числа N с помощью рекрсии
""")


def factorial1(n):
    return n * factorial1(n - 1) if n > 1 else (n if n == 1 else 0)  # молодец научился


# сначало понятно потом оптимизируешь

# print('факториал = ', factorial1(int(input('Введите число для вычисления факториала: '))))

print("""
Задание №2 Написать функцию для вычисления среднего арифмитического переданных ей значений в виде аргументов:
arg1,arg2,....,argN
""")


def arithmeticMean(*args):
    return sum(args) / len(args) if len(args) else 0  # переделал после codewars
    # items = summa = 0
    # for i in args:
    #     summa += i
    #     items += 1
    # return summa / items  # if args != 0
    # return  enumerate (args)


def listNumbers():
    print('Введите число, для завершения ввода ввидите любой символ: ')
    s = '0'
    spisok = []
    while s.isdigit():
        spisok.append(int(s))
        s = input()
    spisok.pop(0)
    return spisok


# print('средняя арифмитическая: ', arithmeticMean(*listNumbers()))

print("""
Задание №3 Реализовать функцию сортировки выбранных элементов по возрастанию: элементы передаются функции в виде списка 
и выбираются они с помощью функции селектора, указанной в качестве второго параметра. Привести примеры вызова функции 
сортировки с разными видами селекторов. Селекторы реализовать в виде лямда функции 
""")

data = ['2313,', -1, '23123123,', 0, -5, 5, 7, 23, 6, 3, 8, 2, -555, 445, 45]


def sortf(func, args):
    i = 0
    while i != len(args):
        if func(args[i]):
            args.pop(i)
            i -= 1
        i += 1

    i = 0
    k = 1
    count = 0
    while i < len(args) - k:
        for j in range(i + 1, len(args) - k):
            if args[i] > args[j]:
                args[i], args[j] = args[j], args[i]
            if args[j] > args[len(args) - k]:
                args[len(args) - k], args[j] = args[j], args[len(args) - k]
                if args[i] > args[j]:
                    args[i], args[j] = args[j], args[i]
            count += 1
        i = k
        k += 1
    return args


print(data)
print(sortf(lambda x: True if type(x) == str else False, data))
print('пример 2')

print(sortf(lambda x: x * 2, data))

# наконец то понял как пользоваться лямбдой....


# занес в комент после того что решил выполнить задание по новому....
"""
from random import randint, randrange


def __error(x, typ):
    return True if type(x) == typ else False


def __vibor(func, args1, tp):
    args = []
    args2 = []
    if tp != 'int':
        tp = str
    else:
        tp = int
    for i in args1:
        print(type(i))
        if func(i, list) or func(i, tuple):
            for j in i:
                print('fff', type(j))
                if func(j, tp):
                    args.append(j)
                else:
                    args2.append(j)
        elif func(i, tp):
            args.append(i)
        else:
            args2.append(i)

    return args, args2


def sortfun(typ='int', *args):
    Функция принимает произвольные данные, выделяет из них целочисленные данные поизводит сортировку по
    возрастанию и возращает их оддельном списке, остальные данные возращает в отдельном списке
   

    i = 0
    k = 1
    args, args2 = __vibor(__error, args, typ)
    while len(args) - k >= i:
        for j in range(i + 1, len(args) - k):
            if args[i] > args[j]:
                args[i], args[j] = args[j], args[i]
            if args[j] > args[len(args) - k]:
                args[j], args[len(args) - k] = args[len(args) - k], args[j]
                if args[i] > args[j]:
                    args[i], args[j] = args[j], args[i]
        i = k
        k += 1

    return args, args2


lst = [3, 6, 'a', 2, 1, 5, 'b', 7, -8, 'c']
spisok = [lst[randint(0, 9)] for i in range(10)]

print(*sortfun('int', spisok))"""
