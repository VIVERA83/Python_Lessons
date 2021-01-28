st = 'Привет 10 Парни 20 сейчас 30 циферки свалят 23'

b = filter(lambda x: True if x.isalpha() else False ,st.split())
# print(st)
print(' '.join(list(b)))
#
# урок 12
# lst = [int(i) if not int(i) % 2 else 0 for i in input('Введите числа через пробел:').split()]/
lst_dict = {key: key**2 for key in [int(i) for i in input('Введите числа через пробел:').split() if not int(i) % 2]}
# del lst_dict[0]
print(lst_dict)


# чужой код
print(dict([[i, int(i)**2] for i in input('Введи числа через пробел: ').split() if int(i) % 2 == 0]))
# Задание 1.
d = {}
for n in input("Введите числa через запятую: ").replace(",", " ").split():
    n = int(n)
    if n % 2 == 0:
        d.setdefault(n, n ** 2)

print(d)