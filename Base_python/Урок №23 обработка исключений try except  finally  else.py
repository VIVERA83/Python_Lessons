# # x = input('x: ')
# # y = input('y: ')
#
# try:
#     x = int(x)
#     y = int(y)
#     res = y/x
#
# except (ValueError,ZeroDivisionError) as z:
#     res = z #'вы ввели строковые данные'
#
# except ZeroDivisionError as z:
#     res = z
# print('ответ: ',res)

""" Задание №1"""

# Напишите программу ввода натуральных чисел через запятую и преобразования этой строки в список целых чисел.
# (Используйте здесь функцию map для преобразования элементов последовательности строк в последовательность чисел).
# Реализовать обработку возможных исключений при таком преобразовании.

ERROR_list = []

def input_list():
    try:
        lst = list(map(int, input('Введите натуральные числа через запятую: ').split(',')))
    except ValueError as error:
        ERROR_list.append(('Ошибка в функции \033[31m input_list\033[38m:', error))
        return
    return lst


""" Задание №2 """


# Написать функцию вычисления среднего арифметического элементов переданного ей списка. Реализовать обработку возможных
# исключений при ее работе.

def getArithmeticmean(lst):
    try:
        n = sum(lst) / len(lst)
    except TypeError as error:
        ERROR_list.append(('Ошибка в функции \033[31m getArithmeticmean\033[38m:', error))
        return
    return n


lst = input_list()  # из предыдущего задания
print(lst)
print(getArithmeticmean(lst))

""" Задание №3 """


# Написать функцию-генератор (с использованием оператора yield) для удаления произвольного элемента из множества
# (с помощью метода pop()). Функция должна возвращать значение удаленного элемента. Реализовать обработку возможных
# исключений при ее работе.

def getGenirator():
    try:
        n = int(input('Введите число для создания множества: '))
    except ValueError as error:
        ERROR_list.append(('Ошибка в функции \033[31m getGenirator: \033[38m', error))
        print(' Вы ввели ахинею, поэтому число будет 5')
        n = 5
    for i in range(n):
        yield i+1


def delItem(s):
    try:
        n = int(input('Введите количество удаляемых элементов: '))
    except ValueError as error:
        ERROR_list.append(('Ошибка в функции \033[31m delItem: \033[38m', error))
        print('Ошибка ввода, предположим Вы ввели 5')
        n = 5
    try:
        for i in range(n):
            print(s.pop())
    except KeyError as error:
        ERROR_list.append(('Ошибка в функции \033[31m delItem: \033[38m', error))
        print('Множество закончилось до окончания цикла')
    return s
s = set(getGenirator())

# print(s)
d = delItem(s)
print('не удаленные элементы множества:',d)

if ERROR_list:
    print('Ошибки выявленные при работе программы: ')
    for i in ERROR_list:
        print(*i)
        # ValueError
