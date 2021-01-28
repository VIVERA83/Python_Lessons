# error_list = []
#
# try:
#     file_name_st = 'Привет.txt'
#     file = open(file_name_st, encoding='utf-8')
# except FileNotFoundError as error:
#     error_list.append((f'Ошибка при открытие файла \033[31m{file_name_st}\033[38m :', error))
#     print(f'Фаил с именем \033[31m{file_name_st}\033[38m отствует в данном каталоге, создать?')
#     answer = ''
#     while answer not in ('да', 'нет'):
#         answer = input('Да/Нет?').lower()
#         if answer == 'да':
#             file = open(file_name_st, 'w')
#
# else:
#     print('\033[035m открытие файла прошло нормально\033[038m')
# try:
#     n = int(input('Сколько символов прочесть из файла%? :'))
# except ValueError as error:
#     error_list.append((f' Ошибка Некоректно были введены кол-во прочитаемых символов из файла : ',error))
#     n = 10
#     print(f'Будут использоваться данные по умолчанию: {n}')
# else:
#     print(file.read(n))
# answer = ''
# while answer !='выход':
#     answer = input('Введите сколько еще прочетать из файла, либо: "начало","строка","весь" для выхода наберите "выход": ').lower()
#     if answer.isdigit():
#         print(f'\033[34m{file.read(int(answer))}\033[38m')
#     if answer == 'начало':
#         file.seek(0)
#     if answer=="строка":
#         print(file.readline(), end='')
#     if answer=='весь':
#         file.seek(0)
#         for i in file:
#             print(i, end='')
#
#     temp = file.tell()
#     st=file.readline()
#     if st=='':
#         file.seek(0)
#         print('Вернулись в начало файла')
#     else:
#         file.seek(temp)
# print(f'Позиция при выходе: {file.tell()}')
# file.close()
# if error_list:
#     print(f'\033[32mОбработанные ошибки\033[38m')
#     for i in error_list:
#         print(*i)

""" Задание №1"""


# Выполните считывание данных из текстового файла через символ и записи прочитанных данных в другой текстовый файл.
# Прочитывайте так не более 100 символов.

def readfile(filename='input.txt', nfile='output.txt'):
    try:
        newfile = open(nfile)
    except:
        newfile = open(nfile, 'w')
        answer = 'да'
    else:
        answer = ''
        while answer.lower() not in ['да', 'нет']:
            answer = input(f'\033[32mВнимание данный фаил: {nfile} уже существуе перезаписать? да/нет: \033[38m')

    if answer == 'да':
        newfile = open(nfile, 'w')
        with open(filename, encoding='utf-8') as file:
            for i in range(200):
                s = file.read(1)
                if s == '':
                    print('Из файла прочитано менее 100 символов:')
                    break
                if not i % 2:
                    newfile.write(s)
        newfile.close()
    else:
        print('выход из программы')


# readfile()
# В лесу родилась ёлочка, в лесу она росла

""" Задание №2"""


# Пользователь вводит предложение с клавиатуры. Разбейте это предложение по словам (считать, что слова разделены
# пробелом) и сохраните их в столбец в файл.

def writeinfile(filename='Твой стишок.txt'):
    st = input(f'Напиши стишок дружок, а я его сохраню в файлик {filename}: ').split()
    with open(filename, 'w') as file:
        for i in st:
            file.writelines([i, '\n'])  # ИЛИ ТАК .write(i + '\n')  # print(i)


# writeinfile()

""" Задание №3"""
# 3. Пусть имеется словарь:
# d = {"house": "дом", "car": "машина",
#      "tree": "дерево", "road": "дорога",
#      "river": "река"}
# Необходимо каждый элемент этого словаря сохранить в бинарном файле как объект.
# Затем, прочитать этот файл и вывести считанные объекты в консоль.

from pickle import dump, load
from os import path


def binfile(savedict, filename='output.bin'):
    with open(filename, 'wb') as file:
        for i in savedict.items():
            dump(i, file)

    with open(filename, 'br') as file:
        a = path.getsize(filename)
        while file.tell() != a:
            print(k, load(file))
    return 'END'


d = {"house": "дом", "car": "машина",
     "tree": "дерево", "road": "дорога",
     "river": "река"}


# print(binfile(d))

def readfile(filename='input.txt', nfile='output.txt'):
    try:
        newfile = open(nfile)
    except:
        newfile = open(nfile, 'w')
        answer = 'да'
    else:
        answer = ''
        while answer.lower() not in ['да', 'нет']:
            answer = input(f'\033[32mВнимание данный фаил: {nfile} уже существуе перезаписать? да/нет: \033[38m')

    if answer == 'да':
        newfile = open(nfile, 'w')
        with open(filename) as file:
            for i in range(100):
                s = file.read(1)
                if s == '\n':
                    s = file.read(1)
                file.seek(file.tell() + 1)
                newfile.write(s)
                if s == '':
                    print('Из файла прочитано менее 100 символов, файл закончился:')
                    break
        newfile.close()
    else:
        print('выход из программы')


readfile()
