from math import *

print("Введите следующие значения функции")
x1 = float(input("Начальное значение функции: "))
xn = float(input("Конечное значение функции: "))
n = float(input("Шаг вычисления значений: "))
print()


if xn <= x1 or n <= 0:
    print("Введены некоректные значения")
else:

    frange = trunc((xn - x1) / n + 1)

    x = x1

    y = []

    print("y                      x")

    for i in range(frange):
        y.append(x*x)

        line = "{:15.5g}".format(y[i])
        line += "   " + '{:^12.2f}'.format(x)
        print(line)

        x += n

    fMin = min(y)
    fMax = max(y)

    _indent = 66

    if fMin != fMax:
        k = (0 - fMin)/(fMax - fMin)
        zeroPoint = round(_indent * k)
    else:
        zero_point = _indent // 2

    if (fMax != fMin) and (fMin >= 0):
        axis = False
    else:
        axis = True

    x = x1

    for i in range(len(y)):

        if fMin != fMax:
            k = (y[i] - fMin)/(fMax - fMin)
            pos = round(_indent * k)
            """
            if pos == 0 and y[i] > 0:
                pos += 1
            elif y[i] > 0:
                pos += 1
            """
        else:
            if fmax < 0:
                pos = 16
            if fmax == 0:
                pos = _indent // 2
            if fmax > 0:
                pos = 50

        _format = '{:6.2f} '

        if not axis:
            line = 'x = ' + _format.format(x) + (' ' * pos) + '*'
            print(line)
        else:
            line = 'x = ' + _format.format(x)
            
            if pos < zeroPoint:
                indent = zeroPoint-pos-1
                line += ' ' * pos + '*' + ' ' * indent + '|'
                print(line)
            if pos == zeroPoint:
                indent = zeroPoint
                line += ' ' * indent + '*'
                print(line)
            if pos > zeroPoint:
                indent = pos-zeroPoint-1
                line += ' ' * zeroPoint + '|' + ' ' * indent + '*'
                print(line)

        x += n

        
    
        
