"""Простейший модуль ревлизующий словарь с с ледующими действиями с словарем: Добавление, Удаление, Перевод"""

chekRusWord = lambda st: all([True if ord(char) in range(1072, 1104) else False for char in st])
chekEngWord = lambda st: all([True if ord(char) in range(97, 123) else False for char in st])
chekWords = lambda st: any([chekEngWord(st), chekRusWord(st)])


engrusdict = {}  # словарь

ERROR = 'Необходимо ввести слово на английском языке и его перевод на русском языке, всего 2 слова, либо нажмите Enter для выхода'


def inputСontrol(message, func):
    """Функция отвечает за коректный ввод """
    while True:
        word = input(message).lower() # строка
        # проверка на корректный ввод, строка разбивается на список строк, далее каждый элемент списка проходит через фильтр
        # и возращается новая строка, если она не равно длине оригинала значит введены некорректные данные.
        if len(' '.join(filter(func, word.split()))) == len(word):
            return word
        print('\033[031mНекорректный ввод.\033[038m Повторите:')


def findWord(word):
    """функция ицет слово в словаре по ключу - если оно набрано на латинице, и по значению если набрано кириллицей"""
    if chekEngWord(word) and engrusdict.get(word):
        return True, word  # слово на английском языке
    if chekRusWord(word):
        for key, item in engrusdict.items():
            if word == item:
                return True, key  # слово на русском
    return (False, '') if word == '' else (False, f'Слово {word} не найдено')  # если пустая строка, для выхода


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
            print(f'Запись: {word[1]} : {engrusdict[word[1]]} , успешно удалена')
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

