N = 3  # ширина поля
X ='X' # символ которым отображается Х
O ='O' # символ которым отображается Y
Pusto = '0' # символ которым отображается не занятая ячейка
Pole =[Pusto]*N*N


# pm -  player move  координаты хода игрока интерпретированные в индекс списка

def drawingField(pm=-1):
    """Отрисовка игрового поля"""
    for i in range(3):
        if pm//N == i:
            print('\033[33m', *Pole[i*N:pm], end='')
            print('\033[31m', str(*Pole[pm:pm+1]), end='')
            print('\033[33m', *Pole[pm+1:N*i+N])
        else:
            print('\033[33m', *Pole[i*N:i*N+N])


def controlGame(pm):
    for y in range(-1,2):
        for x in range(-1,2):
            if (pm//N+x in range(N)) and (pm%N+y in range(N)):
                newpm=(pm//N+y)*N+pm%N+x # строим  новую точку для обхода ( по формуле (y-1)*N+x-1 где pm%N- старый Y )
                print('Все хорошо:',newpm, ' x: ',pm%N+x, ' y: ', pm//N+y, 'точка -----:',(pm//N+y*(0))*N+pm%N+x*(-1) )
                if (Pole[newpm] == Pole[pm]) and (newpm!=pm):
                     if -1*(pm // N + x in range(N)) and -1*(pm % N + y in range(N)):
                            newpm1=(pm//N+y*(-1))*N+pm%N+x*(-1)
                            print( 'Точка 3 на проверку: ',newpm1)

            else:
                print('Все плохо')
    pass


def movePlayer(controlpole):  # Готово
    """Проверка правельности ввода координат поля игроком, c проверкой на занятость
       функция возращает индекс списка в который нужно ставить Х или O"""

    flag=True
    while flag:
        xy = input('Введите координаты хода, "x" и "y" от 1 до 3:')
        if (len(xy) == 3) and xy[0] in '123' and xy[2] in '123':
            pm=(int(xy[2])-1)*N+int(xy[0])-1  # соотносим координаты с адресом ячейки (y-1)*N+x-1
            if controlpole[pm] == Pusto:
                return pm
            else:
                print('Поле занято, введите другие координаты')
        else:
            print('Вы ввели не правельные координаты, повторите ввод')

def runGame():
    drawingField()
    for i in range(3):
        pm = movePlayer(Pole)
        Pole[pm] = X
        drawingField(pm)
        controlGame(pm)

runGame()

