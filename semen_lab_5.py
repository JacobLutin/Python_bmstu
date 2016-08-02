from math import *
N0, St, N1  = map(float,input('Через пробел введите начальное \
значение, шаг и конечное значение параметра A : ').split())

Num_Of_Points = trunc((abs((N1 - N0) /St)+1 )) # Вычисляем кол-во точек
Y1 = [' ']* Num_Of_Points
Y2 = [' ']* Num_Of_Points
X = [' '] * Num_Of_Points
Curr = N0

print()
print('{:^12}'.format('X'),'{:^12}'.format('Y1'),'{:^12}'.format('Y2'),sep='|')
print('-' * 39)
for i in range(Num_Of_Points):
    Y1[i] = sin(Curr)
    #Y1[i] = cos(Curr)
    #Y1[i] = 1/Curr
    #Y1[i] = Curr
    #Y1[i] = 5
    Y2[i] = pow(Curr,2) + 4*sin(Curr)
    X[i] = Curr
    print('{:^12}|{:^12}|{:^12}|'.format('{:5.3f}'.format(X[i]),
                                         '{:6.3f}'.format(Y1[i]),
                                         '{:6.3f}'.format(Y2[i])))
    print('-' * 39)
    Curr += St
print()
    
FMax = max(Y1)
FMin = min(Y1)

# Zero_Point - позиция оси OX на графике
if FMin != FMax:
    k = (0 - FMin) / (FMax - FMin)
    Zero_Point = round(66 * k)
else:
    Zero_Point = 33
    
# Axis_Flag - определяет требуется ли ось OX на графике
if (FMax != FMin and (FMax < 0 or FMin >0)):
    Axis_Flag = False
else:
    Axis_Flag = True
    
for i in range(Num_Of_Points):
    # Pos - позиция точки на графике, если график параллелен оси OX,
    # то выбирается середина между осью OX и границей графика
    if FMin != FMax:
        k = (Y1[i] - FMin) / (FMax - FMin)
        Pos = round(66 * k)
    else:
        if FMax < 0:
            Pos = 16
        elif FMax == 0:
            Pos = 33
        else:
            Pos = 50
        
    if not Axis_Flag :
        print('X = ', '{:^7}'.format( '{:3.3f}'.format(X[i])),
              ' '*Pos, '*', ' '*(66-Pos), sep='')
        continue
    
    if Pos < Zero_Point:
        print('X = ', '{:^7}'.format( '{:3.3f}'.format(X[i])),
              ' '*Pos, '*', ' '*(Zero_Point-1-Pos), '|',
              ' '*(66-Zero_Point), sep='')
    elif Pos == Zero_Point:
        print('X = ', '{:^7}'.format( '{:3.3f}'.format(X[i])),
              ' '*Zero_Point, '*', ' '*(66-Zero_Point), sep='')
    elif Pos > Zero_Point:
        print('X = ', '{:^7}'.format( '{:3.3f}'.format(X[i])),
              ' '*Zero_Point, '|', ' '*(Pos-Zero_Point-1), '*',
              ' '*(66-Pos), sep='')
# Вывод направления оси OX(если требуется)
if Axis_Flag:
    print(' '*(Zero_Point+11),'|\n',
          ' '*(Zero_Point+11), 'V\n',
          ' '*(Zero_Point+11), 'X', sep='')
