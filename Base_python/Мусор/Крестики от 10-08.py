

N = 3  # ширина поля
X = 'X'  # символ которым отображается Х
O = 'O'  # символ которым отображается Y
Pusto = 1  # символ которым отображается не занятая ячейка
Pole = [Pusto] * N * N
PolePC = [Pusto] * N * N
player = ('Игрок X ', 'Игрок O ')


# pm -  player move  координаты хода игрока интерпретированные в индекс списка

def drawingField(pm=-1):
    """Отрисовка игрового поля"""
    for i in range(3):
        if pm // N == i:
            print('\033[33m', *Pole[i * N:pm], end='')
            print('\033[31m', str(*Pole[pm:pm + 1]), end='')
            print('\033[33m', *Pole[pm + 1:N * i + N])
        else:
            print('\033[33m', *Pole[i * N:i * N + N])


def runComputer(pm, movepc):
    xy = functXY(pm)
    # x-

    if PolePC[funct(0, xy[1])] or PolePC[funct(1, xy[1])] or PolePC[funct(2, xy[1])] == Pusto:
        sum3 = PolePC[funct(0, xy[1])] * PolePC[funct(1, xy[1])] * PolePC[funct(2, xy[1])]
        for i in range(N): # N - это 3 ширина поля
            if PolePC[funct(i, xy[1])] == Pusto:
                if movepc[0][1] < sum3:
                    movepc[0][0] = funct(i, xy[1])
                    movepc[0][1] = sum3

    # y|
    if (PolePC[funct(xy[0], 0)] == Pusto) or (PolePC[funct(xy[0], 1)] == Pusto) or (PolePC[funct(xy[0], 2)] == Pusto):
        sum3 = PolePC[funct(xy[0], 0)] * PolePC[funct(xy[0], 1)] * PolePC[funct(xy[0], 2)]
        for i in range(3):
            if PolePC[funct(xy[0], i)] == Pusto:
                if movepc[0][1] < sum3:
                    movepc[0][0] = funct(xy[0], i)
                    movepc[0][1] = sum3

    # xy\

    if (xy[0] == xy[1] == 0) or (xy[0] == xy[1] == 1) or (xy[0] == xy[1] == 2):
        sum3 = PolePC[0] * PolePC[4] * PolePC[8]
        for i in range(3):
            if PolePC[i * 4] == Pusto:
                if movepc[0][1] <= sum3:
                    movepc[0][0] = i * 4
                    movepc[0][1] = sum3
                    break
    # xy/ и центр
    if (xy[0] == xy[1] == 1) or (xy[0] == 2 and xy[1] == 0) or (xy[0] == 0 and xy[1] == 2):
        sum3 = PolePC[2] * PolePC[4] * PolePC[6]
        for i in range(1, 4):
            if PolePC[i * 2] == Pusto:
                if movepc[0][1] <= sum3:
                    movepc[0][0] = i * 2
                    movepc[0][1] = sum3
                    break

    if PolePC[movepc[0][0]] == Pusto:
        movepc[0][1] = 1
    else:
        movepc[0][1] = movepc[0][1]*-3
    return movepc


def funct(x, y):
    z = y * N + x
    return z


def functXY(plm):
    XY = []
    XY.append(plm % N)
    XY.append(plm // N)
    return XY


def controlGame(pm, win=0):
    xy = functXY(pm)
    if Pole[funct(0, xy[1])] == Pole[funct(1, xy[1])] == Pole[funct(2, xy[1])]:
        win = 1
    if Pole[funct(xy[0], 0)] == Pole[funct(xy[0], 1)] == Pole[funct(xy[0], 2)]:
        win = 1
    if (xy[0] == xy[1] == 1) or (xy[0] == xy[1] == 0) or (xy[0] == xy[1] == 2):
        if Pole[0] == Pole[4] == Pole[8]:
            win = 1
    if (xy[0] == xy[1] == 1) or (xy[0] == 2 and xy[1] == 0) or (xy[0] == 0 and xy[1] == 2):
        if Pole[2] == Pole[4] == Pole[6]:
            win = 1
    return win


def movePlayer(controlpole, playmsg):  # Готово
    """Проверка правельности ввода координат поля игроком, c проверкой на занятость
       функция возращает индекс списка в который нужно ставить Х или O"""
    playmsg = playmsg + 'Введите координаты хода, "x" и "y" от 1 до 3:'
    flag = True
    while flag:
        xy = input(playmsg)
        if len(xy) == 1 and xy in '123456789':
            xy = (int(xy) - 1)# * N + int(xy[0]) - 1  # соотносим координаты с адресом ячейки (y-1)*N+x-1
            if controlpole[xy] == Pusto:
                return xy
            else:
                print('Поле занято, введите другие координаты')
        else:
            print('Вы ввели не правельные координаты, повторите ввод')

def runGame():

    drawingField()  #
    i = 0
    win = 0
    moveC = [[8,1]]
    movePClast=[[0,0]]
    while (i < 9) and (win == 0):  # Певый ходит 0
        i += 1
        print('Ход =', i)
        if i % 2:
            pm1 = movePlayer(Pole, player[i % 2])
            Pole[pm1] = O  # внесли в поле для отрисовки
            PolePC[pm1] = 2  # внесли в поле для общета хода компьютера
        else:
            movePClast[0][0], movePClast[0][1] = moveC[0][0], moveC[0][1]
            moveC = runComputer(pm1, moveC)                          # ход компьютера от Игрока
            movePClast = runComputer(movePClast[0][0], movePClast)  # ход компьютера от прошлого хода
            if moveC[0][1] <= movePClast[0][1]:
                moveC[0][0] = movePClast[0][0]
            Pole[moveC[0][0]] = X
            PolePC[moveC[0][0]] = -3
            pm1 = moveC[0][0]
        drawingField(pm1)
        win = controlGame(pm1)
    if win:
        print('Победил: ', player[i % 2])
    else:
        print('Ничья')


runGame()

