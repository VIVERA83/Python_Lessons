a = [2, 3, 4, 6, 2, 7, 5]
a = sorted(a, key=lambda x: x % 2)
print(a)  #

a = [2, 3, 4, 6, 2, 7, 5]
a = sorted(a, key=lambda x: x + 100 if x % 2 else x)
print(a)

""" Задание №1"""


# Используя сортировку, найдити первые три наименьшие значения в списке:
# a =[1, 2,-5,0,5,10]
# сам список должен остаться неизмененным

def top_3_min_list(lst):
    top = sorted(lst)[:3]
    return top


a = [1, 2, -5, 0, 5, 10]
print(top_3_min_list(a))
# для сайта
print(sorted(a)[:3])

""" Задание №2"""
# Отсортируйте список:
# digs = (-10,0,7,-2,3,6,-8)
# так что бы сначало шли отрицательные цифры, а затем положительные

# digs = (-10, 0, 7, -2, 3, 6, -8)
digs = (-10, 0, 7, -2, 3, 6, -8, -1)
print('Задача №2: ',sorted(digs))

""" Задание №3"""
# Пусть имеется словарь:
# {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}
# Необходимо вывести телефонные номера по убыванию чисел, указанных в ключах, то есть, в порядке:
# +4, +5, +7, +12

a = {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}
lst = list(zip(a.keys(), a.values()))  #
lst = sorted(lst, key=lambda x: int(x[0][1:]))
lst = ','.join([i[0] + str(i[1]) for i in lst])

print('Задача №3',lst)
def sortPhoneCode(code_dict):
    code_dict = sorted(code_dict.items(), key=lambda x: int(x[0][1:]))

    return ','.join([i[0] + str(i[1]) for i in code_dict])

print(sortPhoneCode(a))



def sortPhoneCode(code_dict):
    code_dict = sorted(code_dict.items(), key=lambda x: int(x[0][1:]))
    print(code_dict)
    return ','.join([i[0] + str(i[1]) for i in code_dict])




a = {'+7': 2345678901, '+4': 3456789012, '+5': 5678901234, '+12': 78901234}
b = ','.join([i[0] + str(i[1]) for i in sorted(a.items(), key=lambda x: int(x[0][1:]))])

print(sortPhoneCode(a))
print('b=',b)

print('    эываваsdasd asdasdasdasdasdasd')
# чужой код  заинтересовала eval()
"""di = {'+7': 2345678901,
      '+4': 3456789012,
      '+5': 5678901234,
      '+12': 78901234
      }

di_m = sorted(di.keys(), key=eval)
print(di_m)"""


digs = (-10, 0, 7, -2, 3, 6, -8, -1)
 # Добавила в коллекцию -1.
print(sorted(digs, key=lambda x: x >= -1))   # Ваш код даст ошибку [-10, -2, -8, 0, 7, 3, 6, -1]
print(sorted(digs, key=lambda x: x >= 0))   #  [-10, -2, -8, -1, 0, 7, 3, 6]
# Но в задаче не указано, что в том же порядке, значит можно просто
print(sorted(digs))  # [-10, -8, -2, -1, 0, 3, 6, 7]