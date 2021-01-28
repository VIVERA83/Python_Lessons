# 1. Создайте модуль с двумя функциями, которые бы вычисляли периметр и площадь прямоугольника. Подключите этот модуль
# к основной программе и вызовите эти функции с аргументами, введенные с клавиатуры.
#
# 2. Задайте в модуле словарь, в котором ключами являются английские слова, а значениями соответствующие русские
# (переводы). Также добавьте необходимые функции для добавления и удаления новых слов в этом словаре. Импортируйте этот
# модуль в основную программу и реализуйте мини-словарь со следующим меню (функционалом):
#
# 1. Перевести слово
# 2. Добавить слово
# 3. Удалить слово
# 4. Завершить работу
#
# Попробуйте развить идею словаря и добавьте возможность автоматического сохранения и считывания данных из файла
# (в файле сохраняется словарь целиком).

import pickle
from os import path
import translator as ts

checkMenu = lambda x: True if len(x) == 1 and '0' < x < '5' else False

filename = 'dictionar.txt'

def inputСontrol(message, func):
    """Функция отвечает за коректный ввод """
    while True:
        word = input(message).lower() # строка
        # проверка на корректный ввод, строка разбивается на список строк, далее каждый элемент списка проходит через фильтр
        # и возращается новая строка, если она не равно длине оригинала значит введены некорректные данные.
        if len(' '.join(filter(func, word.split()))) == len(word):
            return word
        print('\033[031mНекорректный ввод.\033[038m Повторите:')

def menu(menu):
    """Основное меню программы, выводит на экран меню"""
    for i in enumerate(menu, 1):
        print(*i)


def initProgram(filename, dictionary):
    """функция подгружает словарь из файла, если его находит"""
    try:
        file = open(filename, 'br')
    except:
        print(f'Файл словаря {filename} не найден, будет создан новый.')
    else:
        size = path.getsize(filename)
        while file.tell() != size:
            dictionary.update(pickle.load(file))
        file.close()


def exitProgram(filename, dictionary):
    """функция записывает словарь в файил, выполняется перед выходом из программы"""
    file = open(filename, 'wb')
    pickle.dump(dictionary, file)
    file.close()


def runProgram():
    """основная функция"""
    mainmenu = ['Перевести слово',  # 1
                'Добавить слово',  # 2
                'Удалить слово',  # 3
                'Завершить работу']  # 4
    answer = 0
    while answer != '4':
        menu(mainmenu)
        answer = inputСontrol('Выберите пункт меню: ', checkMenu)
        if answer == '1':
            ts.getTranslate()
        if answer == '2':
            ts.addWord()
        if answer == '3':
            ts.delWord()


initProgram(filename, ts.engrusdict)
runProgram()
exitProgram(filename, ts.engrusdict)
print(ts.engrusdict)