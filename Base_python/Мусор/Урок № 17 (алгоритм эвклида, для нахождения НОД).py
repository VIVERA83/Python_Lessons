
def inputValidation(message = 'Введите число: '):
    msg = ['q']
    while not msg[len(msg)-1].isdigit():
        msg.append(input(message))
    msg.pop(0)
    if len(msg) ==11:
        msg.pop(len(msg)-1)
    return msg


print(""" Задание №1:
Реализовать алгоритм Эвклида НОД (наибольший)с помощью рекурсии""")
def recurs_NOD(a, b): # чужой код
    if a % b == 0:
        return b
    return recurs_NOD(b, a % b)

def getNod(a, b):
    print(a,b)
    if b > a:
        a, b = b, a
    if b > 0:
        a, b = b, a % b
        a = getNod(a, b)
    return a

def newGetNod(a, b):   # моя функция после прохождения codewars
         return b if a % b == 0 else newGetNod(b, a % b)

#print(newGetNod(int(input('Введите первое число: ')), int(input('Введите второе число: '))))
print(getNod(int(input('Введите первое число: ')), int(input('Введите второе число: '))))


print(""" Задание № 2:
Написать функцию нахождения максимального значения среди переданных аргументов
        arg, arg1, ..., argN """)

def newMaximum(*args, ):
    return max(*args)


data = [2313,7,-1,231, 2,31, 23,5, 0, -5, 5, 7, 23, 6, 3, 8, 2,-555, 445, 45]

#print(newMaximum(data))

print(""" Задание № 3:
Написать функцию нахождения максимального или минимального значения среди переданных аргументов
        arg, arg1, ..., argN 
С помощью  функции селектора, увзвнной  в виде лямда функции как один из параметров функции поиска""")

def MaxМim(funct,*args):
    return max(*args) if funct() else min(*args)

print(MaxМim(lambda x=int(input('Введите число, если лно больше 0 будет выведено максимальное число из списка: ')): True if x>0 else False , data))


