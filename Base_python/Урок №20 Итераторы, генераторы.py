a = (x * (True if x > 3 else False) for x in range(6))  # создали генератор
b = (x * (2 if x > 'f' else 4) for x in 'asdfghjkl')
c = (x * (True if x > 3 else False) for x in range(6))  # создали генератор

lst = list(b)
st = ' '.join(map(str, a))

print(lst)
print(st)

it = iter(lst)
print(f'сумма: {sum(c)}')
print(next(it).__sizeof__())

print('Можно генерировать итератор из Списка и строки', next(iter(st)))
for i in range(6):  # обход генератора
    print(f'Проходи по эелементно элемент {i}: {next(it)}')


def myfun(n):
    return list(range(n))


def mygen(n):
    for i in range(n):
        yield i


print(myfun(9))
s = mygen(12)
print(next(s))
print(next(s))

"""Пусть дан текст:
 t = Генератор - это итератор ,элементы которого перебирать (итерировать) можно только один раз.
 Итератор - это объект , который подерживает функцию next() для перехода к следующему элементу коллекции.
 
 Написать функцию генератор для выделения слов из этого текста (слова разделяются пробелом либо переносом строки  '\\n')
 Список всех слов не создавать"""

t = """Генератор - это итератор, элементы которого перебирать (итерировать) можно только один раз. 
Итератор - это объект, который подерживает функцию next() для перехода к следующему элементу коллекции."""


def getWordString():
    for i in input(
            f'На этом месте должна быть вот такая строка:{t}, \033[35m но ты можешь написать свою:\033[30m').split():  # st.split():
        yield i


sum_len_str = 0
for i in getWordString():
    sum_len_str += len(i)
    if sum_len_str >= 30:
        print('')
        sum_len_str = 0
    if len(i) > 8:
        print(f'\033[31m{i}\033[30m', end=' ')
    else:
        print(i, end=' ')

st = [y for x in range(30) for y in range(x) if x % 2 == 0]
print(st)

# чужой код не работает
# [y for x in range(5) for y in range(x) if x % 2 == 0] надо разобраться
# def gen_st(st): [yield x for x in st]
# list_st = input('Введите строку: ').split(' ' or '\n')  ХОРОШАЯ ИДЕЯ ПО ПОВОДУ or
# iter_st = gen_st(list_st)
# [print(x) for x in iter_st]