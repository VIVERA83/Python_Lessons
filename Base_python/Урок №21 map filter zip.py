# # map(функция, итератор )
from time import time

#
# lst = [['Москва', 'Санкт-Петербург'],
#        ['Пушкин', 'Колпино'],
#        ['Выборг', 'Сестрорецк']]
# lst1 = ['Москва', 'Санкт-Петербург',
#         'Пушкин', 'Колпино',
#         'Выборг', 'Сестрорецк']
#
# st = map(len, lst1)
#
# print(list(st))
#
#
# def primer(st):
#     return ''.join(set(st)), st
#
#
# st = map(primer, lst1)
# print(list(st))
#
#
# def primer2(st):
#     return {f'что ты такое написал? = {st}': len(st)}
#
#
# # print(list(map(primer2,input().split())))
# # str.
#
#
# # filter(функция, итератор)
# st = 'Привет Парни чейчас нас останется меньше'
# st = 'Hi Guys there are fewer of us left now'
#
# b = filter(lambda x: True if ord(x) > 80 else False, st)
# print(st)
# print(''.join(list(b)))

# Задание!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""" 1. Поставте в соответствии следующим образом английским символам русские буквы:
      h=х e=е l=л o=о w = в r=р d= д 
     и преобразуйте строку : hello world! в руские символы
"""


def getTranscriptions(st):
    dict_Rus_eng = {'h': 'х', 'e': 'е',
                    'l': 'л', 'o': 'о',
                    'w': 'в', 'r': 'р',
                    'd': 'д'
                    }
    # set(st) & set(dict_Rus_eng)  - возрвщает новое множество в котором есть элементы из обоих множеств, то есть будем работать только по тем буквам которые есть в словаре
    for i in set(st) & set(dict_Rus_eng):  # проходим по общим элементам словаря(ключи) и строки
        st = st.replace(i, dict_Rus_eng.get(i))  # подставляем в строку значение ключей словаря
    return st


# Чужой код
dic = {'h': 'х', 'e': 'е', 'l': 'л', 'o': 'о', 'w': 'в', 'r': 'р', 'd': 'д'}


def tr(x):
    t = ''
    for i in x:
        t += dic.get(i, i)
    return t

##########################
st = 'hello ,wowa world!'
print('Привет',getTranscriptions(st))

""" 2. Дан текст:
t='''Куда ты скачешь гордый конь,
И где опустишь ты копыта?
О мощьный властилин судьбы!
Не так ли ты над самой бездной,
На высоте, уздой железной
Россию поднял на дыбы?
'''
    Необходимо выделить каждое второе слово из этого стихотворяния и представить результат в виде упорядоченного списка.
    (Подумайте как реализовать алгоритм с наименьшими затратами по памяти). 
"""


def sortPoem(st):
    poem_lst = [st.split()[i] for i in range(len(st.split())) if i % 2]  # Вариант 1 Медленный
    return sorted(poem_lst), poem_lst.__sizeof__()  #


def sortPoem1(st):  # Вариант 2
    it = (value for index, value in enumerate(st.split()) if index % 2)  # Создаем из строки итератор

    # poem_lst = list(it)
    # flag = False # признак четности если True значет четное
    # for i in it:
    #     if flag:
    #         poem_lst.append(i)
    #     flag = not flag
    return it.__sizeof__(), sorted(it)  # ,poem_lst.__sizeof__()


t = '''Куда ты скачешь гордый конь,
И где опустишь ты копыта?
О мощьный властилин судьбы!
Не так ли ты над самой бездной,
На высоте, уздой железной
Россию поднял на дыбы?
'''
print(sortPoem1(t), sep='\\n')
print(sortPoem(t))

""" 3. Реализовать Алгоритм для нахождения все делителей натурального числа N. Число N вводится с клавиатуры
Для начала можно реализовать простым перебором для всех И возжможных чисел (делителей). Затем подумать как можно 
оптимизировать по скорости этот алгорим
"""


def get_all_div_number(n):  # Вариант 1
    div_num = [1]
    for i in range(2, n):
        if not n % i:
            div_num.append(i)
    div_num.append(n)
    return div_num, len(div_num)  # , div_num.__sizeof__()


def get_all_div_number1(n):  # Вариант 2 Самый коротки и медленный
    return [i for i in range(1, n + 1) if not n % i]  # , [i for i in range(1, n+1) if not n % i].__sizeof__()


def get_all_div_number3(n):  # Вариант 3
    """Функция выдает все делители числа в виде отсортированнаго списка """
    num_comp_list = {}  # Состав числа(множетели числа): ключ - это делитель, а значение cтепень делителя
    div_num = 2  # Временная переменная, используется при разборе числа на состав

    # шаг 1 находим состав числа
    count = 0  # счетчик степени
    while n >= div_num:  # выполняем пока число меньше делителя
        if n % div_num:  # Есличисло делетися с остатком
            div_num += 1  # Увеличиваем делитель
            count = 0  # степь приравниваем 0
        else:
            count += 1
            n //= div_num  # изначальное число делим нацело
            num_comp_list[div_num] = count

    # шаг 2  извлекаем из словаря список
    lst = []
    for key in num_comp_list:
        lst.append([key ** x for x in range(num_comp_list[key] + 1)])

    # Находим все делители числа
    for i in range(1, len(lst)):  # перемножаем
        temp_list = []
        for item in lst[0]:
            temp_list.extend(list(map(lambda y, x=item: y * x, lst[i])))
        lst[0].extend(temp_list)

    # шаг 4 готовим данные к выводу,
    lst = list(set(lst[0]))  # удаляем повторяющиеся элементы
    return sorted(lst)


def check_input():
    """Функция контарлирует корректность ввода числовых данных"""
    n = ''
    while not n.isdigit():
        n = input('Введти число: ')
    return int(n)


n = 40322591

# a = time()
# print(list((bin(n)[2:])), len(list((bin(n)[2:]))))
# print(list((bin(n)[2:])[::-1]))
#
# print(get_all_div_number(n))
# print(f'Прошло времяни функция 1: {time() - a}')

# a = time.time()
# print(get_all_div_number1(n))
# print(f'Прошло времяни первая функция 2: {time.time() - a}')

a = time()
print(get_all_div_number3(n))
print(f'Прошло времяни первая функция 3: {time() - a}')

#  чцжой код
# Прмеры длугих уроков очень медленно решение
# number = 40321
# divider = 1
# result = []
# a = time()
# while divider < number ** 2:
# 	if number % divider == 0:
# 		result.append(divider)
# 	divider += 1
# print(f'Прошло времяни чужого кода: {time() - a}')
# print(result)

def get_all_div_number(N):
    i = 2
    res = {1, N} # само число и 1 всегда являются делителями
    while i * i <= N: # Идем только до корня числа. Если число 88,
        # то на возможный делитель число 8 проверяем (8*8=64),
        # а число 9 =нет (9*9=91). Но найдя меньший делитель числа,
        # например 4 для 88, сразу добавляем два делителя 4 и 88//4=22
        if N % i == 0:
            res.update([i, N // i])
        i += 1
    return sorted(list(res))

a = time()
print(get_all_div_number(n))
print(f'Прошло времяни функция 1: {time() - a}')