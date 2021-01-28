"""Задание №1"""


# Создайте модуль с двумя функциями, которые бы вычисляли периметр и площадь прямоугольника. Подключите этот модуль к
# основной программе и вызовите эти функции с аргументами, введенные с клавиатуры.
# import mylib26

def inputcontrol(msg='Введите 2 числa, через пробел: ', func=lambda *args: all(True if i > 0 else False for i in args)):
    while True:
        try:
            answer = list(map(int, input(msg).split(' ')))
            if func(*answer):
                return answer
        except:
            print('\033[031mНекорректный ввод.\033[038m Повторите ввод')


# print(mylib26.getAreaRectangle(*inputcontrol('Введите Ширину и длинну Прямоугольника для подсчета площади прямоугольника')))
# print(mylib26.getPerimeterRectangle(*inputcontrol('Введите Ширину и длинну Прямоугольника для подсчета периметра ')))

"""Задание №2"""


# Задайте в модуле словарь, в котором ключами являются английские слова, а значениями соответствующие русские (переводы).
# Также добавьте необходимые функции для добавления и удаления новых слов в этом словаре. Импортируйте этот модуль в основную
# программу и реализуйте мини-словарь со следующим меню (функционалом):
## 1. Перевести слово
# 2. Добавить слово
# 3. Удалить слово
# 4. Завершить работу
# Попробуйте развить идею словаря и добавьте возможность автоматического сохранения и считывания данных из файла (в файле сохраняется словарь целиком).



print(inputcontrol())
