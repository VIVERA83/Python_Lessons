

from random import randint

N = 3  # ширина поля
X = 'X'  # символ которым отображается Х
O = 'O'  # символ которым отображается Y
Pusto = 1  # символ которым отображается не занятая ячейка
Pole = [i+1 for i in range(9)]
PolePC = [randint(1, 2)-1 for i in range(9)] # [Pusto] * N * N
player = ('Игрок X ', 'Игрок O ')



#def drawingField(Pole, pm=2 ):
#    """Отрисовка игрового поля"""
#    for i in range(3):
#        if pm // N == i:
#            print(f'\033[33m', *Pole[i * N:pm], end='')
#            print(f'\033[31m', str(*Pole[pm:pm + 1]), end='')
#            print(f'\033[33m', *Pole[pm + 1:N * i + N])
#        else:
#            print(f'\033[33m', *Pole[i * N:i * N + N])

def drawingField(Pole, pm=6 ):
    for i in range(N):
        for j in range(N):
            if i*N+j == pm:
                st = '\033[31m'
            elif PolePC[i*N+j] == 1:
                st ='\033[30m'
            else:
                st ='\033[33m'
            s = f' {st}{Pole[i*N+j]}'
            print(s, end='')
        print(end='\n')

print(PolePC)
print(Pole)
drawingField(Pole)

