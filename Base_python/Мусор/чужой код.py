# Задание 3.
"""Так как"переданный список" может включать разные типы данный, и передаваться разными способами, я делала эксперимент
с поиском максимального ЧИСЛА простого списка(или кортежа), переданного любым способом и включающего ошибочные(нечисловые)
данные:"""


# Задаем внутреннюю функцию (работает только с элементами одного типа данных):
def getMxm(a):
    return max(a)


# Основная функция:

# inp = input("""Если хотите внести свой список через ввод нажмите *,
# По умолчанию программа рассчитывает программный список: \n""")

#
# def getAnyMaxNum(a, inp):
#     if inp == "*":
#         n = []
#         while True:
#             number = input(
#                 'введи число для добавления в список, по окончанию ввода введите пустую строку или нажмите ЕNТЕР: ')
#             if number == '':
#                 break
#             if not number.isalpha() and (number.isdigit()):
#                 n.append(int(number))
#         print(getMxm(b))
#     else:
#         a = [el for el in a if type(el) == int]
#         print(getMxm(a))
#
#
# # для примеров:
# var = 757
# # a = [-4,-42, 0, var,"uih", 35, False] # список с переменной var
# a = (-4, -92, 0, var, "uih", 56, False)  # кортеж с переменной var
#
#
# # Вызываем:
# # getAnyMaxNum(a, inp)
#
# def mltp(n):
#     S = n[0]
#     for el in range(len(n) - 1):
#         S *= n[el + 1]
#         el += 1
#     print(S)

# Влад2.0
# 2 недели назад
# # 3 задача
#
# import pickle
#
# d = {"house": "дом", "car": "машина",
#      "tree": "дерево", "road": "дорога",
#      "river": "река"}
#
# with open('out.bin', 'wb') as fd:
#      pickle.dump(d, fd)
#
# with open('out.bin', 'rb') as fl:
#      bs = pickle.load(fl)
# print(bs)
#
# n = [9, 8, 7, 6, 5, 4, 3, 2, 1]
# # mltp(n)
#
# s = 1
# for i in n:
#     s *= i
#
# n = []
# while True:
#     number = input('введи число для добавления в список, по окончанию ввода введите пустую строку или нажмите ЕNТЕР: ')
#     if number =='':
#         break
#     if number.isdigit() or number[0]=='-' and number[1:].isdigit():
#         n.append(int(number))
# print(n)
#
# dictonary ={'apple': 'яблоко',
#             'lemon': 'лимон',
#             'orange': 'апельсин'}
#
# def translate_word():
#     k = input('Введи английское слово: ')
#     if k in dictonary.keys():
#         print(dictonary[k])
#     else:
#         print('Нет такого слова')
#
# def add_word():
#     k = input('Введи английское слово: ')
#     v = input('Введи перевод: ')
#     dictonary[k] = v
#     print('Добавлено')
#
# def delete_word():
#     k = input('Введи английское слово: ')
#     if k in dictonary.keys():
#         del dictonary[k]
#         print('Удалено')
#     else:
#         print('Нет такого слова')
#
# # main
# # from modul import *
#
# while True:
#     print('************************')
#     print('* 1: Перевести слово   *')
#     print('* 2: Добавить слово    *')
#     print('* 3: Удалить слово     *')
#     print('* 4: Завершить работу  *')
#     print('************************')
#
#     x = int(input('Выбери пункт меню: '))
#     if x == 1:
#         translate_word()
#     elif x == 2:
#         add_word()
#     elif x == 3:
#         delete_word()
#     elif x == 4:
#         print('Конец программы..')
#         break

import random


def create_mtrx(line, colmn, symb):
    """ Создание двумерного массива (поля),
    заполненного указанными символами
    """
    mtrx = []
    for i in range(line):
        internal = []
        for j in range(colmn):
            internal.append(symb)
        mtrx.append(internal)
    return mtrx


F = create_mtrx(3, 3, "_")  # Игровое поле глобальная переменная


def nice_print(lst):
    """(Вывод двумерного массива в виде матрицы),
    Функция отображения текущего состояния поля.
    """
    for el in lst:
        print(*el)


def goPlayer(symb):
    gou = ""
    while gou != "go":

        (in_line, in_column) = input("введите строку (1-3), столбик(1-3): ").replace(",", " ").split()
        x, y = int(in_line) - 1, int(in_column) - 1

        if x not in range(0, 3) or y not in range(0, 3):
            print("\nНеверные координаты\n")
        else:
            if F[x][y] == "_":
                F[x][y] = symb

                gou = "go"
                nice_print(F)
                print()
                return x, y

            else:
                print("\nЭта клетка занята!\n")


def goComp(symb):
    rng = random.Random()
    gou = ""

    while gou != "go":
        x = rng.randrange(len(F))
        y = rng.randrange(len(F[0]))

        if F[x][y] != "_":
            continue
        else:
            F[x][y] = symb
            gou = "go"
            nice_print(F)
            print()
    return x, y


def ifFinish(x, y, symb):
    if (F[x][0] == F[x][1] == F[x][2] == symb) or (F[0][y] == F[1][y] == F[2][y] == symb) or (
            F[0][0] == F[1][1] == F[2][2] == symb) or (F[0][-1] == F[1][-2] == F[2][0] == symb):
        return 1
    else:
        return 0


def createGame():
    """Создание игрового поля, распределение
    фишек - игрок выбирает крестик или нолик,
    первый ход, если компьютеру достался крестик
    """
    symb = input("Выберите свой символ + или 0 (ноль): ")
    comp = "+" if symb == "0" else "0"

    win = False
    count = len(F) * len(F[0])

    while win == False and count > 0:
        if symb == "+":
            count -= 1
            x, y = goPlayer(symb)
            win += ifFinish(x, y, symb)

            if win == False and count > 0:
                count -= 1
                x, y = goComp(comp)
                win += ifFinish(x, y, comp)

        if symb == "0":
            count -= 1
            x, y = goComp(comp)
            win += ifFinish(x, y, symb=comp)

            if win == False and count > 0:
                count -= 1
                x, y = goPlayer(symb)
                win += ifFinish(x, y, symb)

    print("Игра окончена, выиграл %s" % F[x][y]) if win != False else print("Боевая ничья")


# createGame()
def getWordString():
    for i in input(
            f'На этом месте должна быть вот такая строка:{t}, \033[35m но ты можешь написать свою:\033[30m').split():  # st.split():
        yield i

t= "Рассматривается способ перебора элементов коллекций с помощью итераторов. Формирование значений через выражения-генераторы и функции-генераторы"
sum_len_str = 0
for i in getWordString():
    sum_len_str += len(i)
    if sum_len_str >= 30:
        print('')
        sum_len_str = 0
    if len(i) > 8:
        print(f'\033[31m{i}\033[30m', end=' ')
    else:
        print(i, end=' ')