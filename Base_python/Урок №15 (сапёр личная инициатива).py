import random

rnf = random.randint

N = 6  # ширина поля
M = '*'
Mine =[]# [*{rnf(0,35) for x in range(10)}] # Мины
Pole = [0]*N*N  # игровое поле закрытое от игрока (служебное)
PolePlayer = ['_']*N*N  # Поле видимое игроку

R = 3  # Радиус движения по клеткам (нужно когда будем генирироваь служебное поле)

def creatingField(Pole,Mine):
   # while len(Mine)<10:
    #    x = rnf(0,36)
     #   if x not in Mine:
     #       Mine.append(x)
   # else:
   Mine =[1, 7, 8, 18, 20, 25, 26, 27, 29, 30]
   for val in Mine:
       Pole[val] = M

   Nindeks=0
   for indeks in range(N*N):
        if Pole[indeks] != M:
            counter = 0
            for y in range(-1,2):
                for x in range(-1,2):
                    Nindeks = indeks + N * y + x
                    if -1 < Nindeks < N * N :
                        if Pole[Nindeks] == M:
                            counter += 1
            Pole[indeks] = counter
   return Pole

def drawingField(Pole,pm=-1):
    """Отрисовка игрового поля"""
    for i in range(N):
        if pm//N == i:
            print('\033[33m', *Pole[i*N:pm], end='')
            print('\033[31m', str(*Pole[pm:pm+1]), end='')
            print('\033[33m', *Pole[pm+1:N*i+N])
        else:
            print('\033[33m', *Pole[i*N:i*N+N])

def movePlayer(controlpole):  # Готово
    """Проверка правельности ввода координат поля игроком, c проверкой на занятость
       функция возращает индекс списка в который нужно ставить Х или O"""

    flag=True
    while flag:
        xy = input('Введите координаты хода, "x" и "y" от 1 до 6:')
        if (len(xy) == 3) and xy[0] in '123456' and xy[2] in '123456':
            pm=(int(xy[2])-1)*N+int(xy[0])-1  # соотносим координаты с адресом ячейки (y-1)*N+x-1
            if controlpole[pm] == '_':
                return pm
            else:
                print('Поле занято, введите другие координаты')
        else:
            print('Вы ввели не правельные координаты, повторите ввод')


def controlGame(pm):
    return True if Pole[pm] == M else False

def runGame():
    creatingField(Pole,Mine)
    step = 0
    pm = -1

    while N*N != step + 10:
        drawingField(PolePlayer)
        step += 1
        pm = movePlayer(PolePlayer)
        PolePlayer[pm] = Pole[pm]
        if controlGame(pm):
            print('Вы подорвались')
            break
pass




runGame()