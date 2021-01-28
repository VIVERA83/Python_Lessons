"""#
# filename = 'input.txt'
# file = open(filename, encoding='utf-8')
#
# entirefile = file.readlines()
#
# file.seek(0)
# for index, line in enumerate(file,1):
#     print(index, line[:-1])
#
# print('А что мы видем дальше')
#
# print(entirefile)
#
# file.close()"""

"""Задание №1"""


# Пользователь через пробел вводит ФИО. На основе этой информации требуется создать строку с сообщением:
# Ваши персональные данные:
# Фамилия: введенная фамилия
# Имя: введенное имя
# Отчество: введенное отчество

def dataentry():
    lst = input('Введите Фамилию, Имя, Отчество через пробел: ').title().split()
    textcolor = ['\033[36m', '\033[31m', '\033[38m']
    for i in range(len(lst), 3):
        lst.append('Незаполненное поле')
    chek = lambda index: True if lst[index] != 'Незаполненное поле' else False
    s = f"Ваши персональные данные: \n" \
        f"Фамилия:  {textcolor[0] if chek(0) else textcolor[1]} {lst[0]} {textcolor[2]}\n" \
        f"Имя:      {textcolor[0] if chek(1) else textcolor[1]} {lst[1]} {textcolor[2]}\n" \
        f"Отчество: {textcolor[0] if chek(2) else textcolor[1]} {lst[2]} {textcolor[2]}"
    return s


# print(dataentry())


"""Задание №2"""


#
# 2. Имеется текстовый файл с содержимым:
#
# Иван, ivan@gm.com, 18
# Татьяна, tat@gm.com, 22
# Сергей, srg@ml.ru, 33
# Федор, fr@ml.ru, 41
# Елена, el@gm.com, 27
#
# Необходимо построчно считывать информацию и для каждой строки для лиц не старше 30 лет сформировать сообщение:
#
# Уважаемый(ая) <имя>! Приглашаем Вас принять участие в курсах по изучению Python. Подробную информацию мы выслали на email: <email>.

def createfile_1(filename='lesson25.txt'):
    st = 'Иван, ivan @ gm.com, 18, Татьяна, tat@gm.com, 22, Сергей, srg@ml.ru, 33,' \
         ' Федор, fr@ml.ru, 41, Елена, el@gm.com, 27'.replace(' ', '')

    lst = st.split(',')
    file = open(filename, 'w', encoding='utf-8')
    a = len(lst)
    for i in range(0, len(lst), 3):
        print(i, lst[i:i + 3])
        file.write(f'{" ".join(lst[i:i + 3])}\n')
    file.close()
    print(a, lst)


def createfile_2(filename='lesson25.txt'):
    file = open(filename, 'w', encoding='utf-8')

    st = 'Иван, ivan @ gm.com, 18, Татьяна, tat@gm.com, 22, Сергей, srg@ml.ru, 33,' \
         ' Федор, fr@ml.ru, 41, Елена, el@gm.com, 27'.replace(' ', '')
    lst = st.split(',')
    i = 0
    while True:
        if lst[i:i + 3] == []:
            break
        file.write(f'{" ".join(lst[i:i + 3])}\n')
        i += 3
    file.close()


def createmessage(filename='lesson25.txt'):
    file = open(filename, encoding='utf-8')
    while True:
        s = file.readline()[:-1].split()
        if s == []:
            break
        if int(s[2]) < 30:
            yield f'Уважаемый(ая) {s[0]}! Приглашаем Вас принять участие в курсах по изучению Python. Подробную информацию мы выслали на email: {s[1]}'
    file.close()


# createfile_1()
for i in createmessage():
    print(i)
