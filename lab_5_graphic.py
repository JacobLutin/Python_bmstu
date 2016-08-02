from math import sqrt, cos, trunc, pi, sin

print("Введите следующие значения функции")
g1 = float(input("Начальное значение: "))
n = float(input("Шаг вычисления значений: "))
gn = float(input("Конечное значение: "))
print()

"""
g1 = float(-12)
gn = float(6)
n = 1
"""

if gn <= g1 or n <= 0:
    print("Введеные значения некорректны")
else:
    

    frange = trunc((gn - g1) / n + 1)

    g = g1

    a1 = []
    a2 = []
    a3 = []
    a4 = []

    line = "-------------------------------------------------------------------"
    
    print("|      a1        |       a2       |        a3      |       g      |")
    print(line)

    t = 0;

    #Вычисление значений трех функций
    for i in range(frange):
        a1.append(g**3 + 6.1 * g * g - 35.4 * g - 25.7)
        a2.append(g * g - cos(g*pi))
        #a3.append(sqrt(a1[i]**2 + a2[i]**2))
        a3.append(g*20)
        a4.append(20 * sin(g) - 80)
        a = []
                  
        point_f = '| {:^15.6}'
        point_f *= 3

         #Построение таблицы значений

        ln = point_f.format(a1[i], a2[i], a3[i]) + '| {:^12.2f}'.format(g) + " |"
        print(ln)
        
        print(line)
        
        g += n

    a.append(a1)
    a.append(a2)
    a.append(a3)
    a.append(a4)
    
    print("\nВведите через пробел номера графиков,", end="")
    print(" которые будет напечатаны: ")

    #Выбор графика для печатиx
        
    fxn = 0

    fMin = min(a[0])
    fMax = max(a[0])
    
    for fx in a:
        if min(fx) < fMin:
            fMin = min(fx)
        if max(fx) > fMax:
            fMax = max(fx)

    _indent = 66

    if fMin != fMax:
            koef = (0 - fMin)/(fMax-fMin)
            zero_point = round(_indent * koef)
    else:
        zero_point = _indent // 2

    if (fMax != fMin) and (fMin > 0):
        axis = False
    else:
        axis = True

    
    g = g1

    _format = ' {:^6.2f} '

    k = 0

    print("Обозначения:\n* - a1\n@ - a2\no - a3\n+ - a4\n")
    print(' ' * (zero_point-10), "График трех функций:")
    print(' ' * (_indent+8), 'g')
        
    for i in range(frange):
    
        #Нахождение максимального и минимального значений

        arr_pos = [0] * (_indent + 2)

        if axis:
            arr_pos[zero_point] = -1

        fxn += 1
        #print(fx)

        fxn = 0

        for j in range(len(a)):

            fxn += 1
            
            if fMin != fMax:
                koef = (a[j][i] - fMin)/(fMax - fMin)
                pos = round(_indent * koef)
                if pos == 0 and a[j][i] > 0:
                    pos += 1
                elif a[j][i] > 0:
                    #pos += 1
                    k += 1
            
            else:
                if fMax < 0:
                    pos = 16
                elif fMax == 0:
                    pos = 33
                else:
                    pos = 50

            arr_pos[pos] = fxn
            
        line = ' '
        for j in range(_indent+1):
            if arr_pos[j] == 0:
                line += ' '
            elif arr_pos[j] == -1:
                line += '|'
            elif arr_pos[j] == 1:
                line += '*'
            elif arr_pos[j] == 2:
                line += '@'
            elif arr_pos[j] == 3:
                line += 'o'
            elif arr_pos[j] == 4:
                line += '+'
        print(line, ' ', _format.format(g), sep='')
        g += n
    
                
    if axis:
        indent = zero_point
        print(" " * (indent), "|")
        print(" " * (indent), "V")
        print(" " * (indent), "g")

    

    
    print("\nКоличество значений функции a",
      ", которые больше нуля: ", k, sep="")

    print()
