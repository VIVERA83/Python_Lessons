import pickle
from os import path

checkMenu = lambda x: True if len(x) == 1 and '0' < x < '5' else False

chekRusWord = lambda st: all([True if ord(char) in range(1072, 1104) else False for char in st])
chekEngWord = lambda st: all([True if ord(char) in range(97, 123) else False for char in st])
chekWords = lambda st: any([chekEngWord(st), chekRusWord(st)])

filename = 'dictionary.txt'
engrusdict = {}  # словарь

ERROR = 'Необходимо ввести слово на английском языке и его перевод на русском языке, всего 2 слова, либо нажмите Enter для выхода'


def inputСontrol(message, func):
    """Функция отвечает за коректный ввод """
    while True:
        word = input(message).lower()  # строка
        # проверка на корректный ввод, строка разбивается на список строк, далее каждый элемент списка проходит через фильтр
        # и возращается новая строка, если она не равно длинне оригинала значет введены некорректные данные.
        if len(' '.join(filter(func, word.split()))) == len(word):
            return word
        print('\033[031mНекорректный ввод.\033[038m Повторите:')


def findWord(word):
    """функция ицет слово в словаре по ключу - если оно набрано латинице, и по значению если набрано кирилицей"""
    if chekEngWord(word) and engrusdict.get(word):
        return True, word  # слово на английском языке
    if chekRusWord(word):
        for key, item in engrusdict.items():
            if word == item:
                return True, key  # слово на русском
    return (False, '') if word == '' else (
    False, f'\033[031mСлово {word} не найдено\033[038m')  # если пустая строка, для выхода


def menu(menu):
    """Основное меню программы, выводит на экран меню"""
    for i in enumerate(menu, 1):
        print(*i)


def addWord():
    """функция добавления новой записи в словарь (hi = Привет)"""
    while True:
        word = sorted(
            inputСontrol('Введите слово и перевод через пробел, для выхода нажмите Enter:', chekWords).split())
        if word == []:
            break
        if len(word) == 2 and all([chekRusWord(word[1]), chekEngWord(word[0])]):
            if engrusdict.get(word[0]) == None:
                engrusdict.setdefault(*word)
                print('Слово успешно добавлено')
            else:
                print(f'Слово  {word[0], word[1]}  уже есть в словаре')
        else:
            print(ERROR)


def delWord():  # готово
    """функция удаления записи из словаря"""
    while True:
        word = findWord(
            inputСontrol('Введите слово которое необходимо удалить, либо  нажмите Enter для выхода: ', chekWords))
        if word[1] == '':
            break
        if word[0]:
            print(f'\033[36mЗапись: {word[1]} : {engrusdict[word[1]]} , успешно удалена\033[38m')
            del engrusdict[word[1]]
        else:
            print(word[1])


def getTranslate():
    """функция перевода слова с английского на русский и наоборот"""
    while True:
        word = findWord(
            inputСontrol('Введит слово для перевода, либо  нажмите Enter для возврата в основное меню :', chekWords))
        if word[1] == '':
            break
        if word[0]:
            print(f'\033[034m{word[1]} = {engrusdict[word[1]]}\033[38m')
        else:
            print(word[1])


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
    """функция закисывает словарь в файил, выполняется перед выходом из программы"""
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
            getTranslate()
        if answer == '2':
            addWord()
        if answer == '3':
            delWord()


initProgram(filename, engrusdict)
runProgram()
exitProgram(filename, engrusdict)

print()
for i, items in enumerate(engrusdict.items(), 1):
    if i % 2:
        print(i, *items)
    else:
        print(f'\033[036m{i} {items[0]} {items[1]}\033[038m')
