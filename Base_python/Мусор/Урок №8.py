
"""Задание №4"""
string = 'abrakadabra'*20
i = string.count('ra')
x = 0
for i in range(i):
    x = string.find('ra', x)
    print(x)
    x += 1

'''______________________'''

string = 'abrakadabra'*10

st = 'ab'
index = 0
while string.find(st, index) >= 0:
    index = string.find(st, index) + 1
    print(index-1)




print("""Чужой код""")
a = 'abrakadabra'
print(a.index('br'),a.index('br',a.index('br') + 1))


number = input('Введите номер телефона согласно шаблону x(xxx)xxxxxxx , x- цифрa от 0..9:')

if len(number)==13 and number[1] == '(' and number[5] == ')' and number[0].isdigit() and number[2:5].isdigit() and number[6:]:
    print('номер введен корректно')
else:
    print('номер введен не правильно')