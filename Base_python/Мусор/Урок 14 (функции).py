# getAreaPerimeteTriangle
import random


def inputEnteringDigits(msg='Введите число:'):
    """функция производит проверку правельности ввода любого числа, в том числе и вещественного, Пока не введена цифровые днанные функция будет просить ввести число"""
    flag = True
    while flag:
        long = input(msg)
        if long.isdigit():
            return float(long)
        elif long.count('.') == 1:
            point = long.find('.')
            long = long.replace('.', '')
            if long.isdigit():
                long = long[0:point] + '.' + long[point:]
                flag = False
            else:
                print('Ошибка ввода, введенные данные не являются числовыми, повторите ввод')
    return float(long)


fun = inputEnteringDigits

# 1
print("""Задайте и вызовите функцию, которая вычисляет площадь  триугольника по формуле S=1/2*a*b
""")


def getAreaTriangle(long, width):
    return long * width * 0.5


print('Площадь треугольника: ',
      getAreaTriangle(fun('Введите Длинну треугольника: '), fun('Введите ширину треугольника: ')))

# 2
print("""Необходимо создать функцию, которая в зависимости от значения формального параметра type
         будет вычислять площадь или периметр прямоугольника
""")


def getAreaOrPerimeterRectangle(long, widht, t=0):
    return long * widht if t == 0 else (long + widht) * 2


long = fun('Длинна прямоуголдьника: ')
widht = fun('Ширина прямоугольнитка: ')
t = input('Для подсчета площади введите любой символ, для вычисления периметра введите 0: ')
if t == 0:
    print(getAreaOrPerimeterRectangle(long, widht))
else:
    print(getAreaOrPerimeterRectangle(long, widht, t))

# 3
print("""Написать функцию поиска максимального значения из переданного ей списка значений
""")

rlist = list(range(0, 10, 3))
print(rlist)


def searchMax(rlist):
    return max(rlist)


print('Максимальное значение', searchMax(rlist))

# 4
print("""Написать функцию вычисления произведения значений элементов переданного ей списка
""")


def getProductList(rlist):
    s = 1
    for i in rlist:
        s *= i
    return s


rlist = [random.randrange(1, 10) for i in range(10)]  # создаем список из 100 элементов с случайным значением
print(rlist)
print('Произведение: ', getProductList(rlist))
