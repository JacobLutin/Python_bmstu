from math import sqrt, cos, trunc, pi, sin

print("Введите следующие значения функции")
g1 = float(input("Начальное значение: "))
n = float(input("Шаг вычисления значений: "))
gn = float(input("Конечное значение: "))
print()

"""
g1 = float(-10000000)
gn = float(10000100)
n = 1000000
"""
if gn <= g1 or n <= 0:
    print("Введеные значения некорректны")
else:
    

    frange = trunc((gn - g1) / n + 1)

    g = g1

    a1 = []
    a2 = []
    a3 = []

    line = "-------------------------------------------------------------------"
    
    print("|      a1        |       a2       |        a3      |       g      |")
    print(line)

    t = 0;

    #Вычисление значений трех функций
    for i in range(frange):
        #a1.append(g**3 + 6.1 * g * g - 35.4 * g - 25.7)
        a1.append(sin(g))
        a2.append(g * g - cos(g*pi))
        a3.append(sqrt(a1[i]**2 + a2[i]**2))
                  
        point_f = '| {:^15.6}'

         #Построение таблицы значений
        
        print(point_f.format(a1[i]),
              point_f.format(a2[i]),
              point_f.format(a3[i]), 
              '| {:^12.2f}'.format(g), " |", sep="")
        print(line)
        
        g += n
    
    print("\nВведите через пробела номера графиков,", end="")
    print("которые будет напечатаны: ")

    graph = map(int, input().split())
    for gr in graph:
        if gr == 1:
            a = a1
            print(' ' * 30, "График функции a1\n")
        elif gr == 2:
            a = a2
            print(' ' * 30, "График функции a2\n")
        elif gr == 3:
            a = a3
            print(' ' * 30, "График функции a3\n")
        else:
            print("Такого графика не существует")
            break
        

        fMin = min(a)
        fMax = max(a)

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

        k = 0

        for i in range(len(a)):
            
            if fMin != fMax:
                koef = (a[i] - fMin)/(fMax - fMin)
                pos = round(_indent * koef)
                if pos == 0 and a[i] > 0:
                    pos += 1
                elif a[i] > 0:
                    pos += 1
                #print(pos)
            
            else:
                if fMax < 0:
                    pos = 16
                elif fMax == 0:
                    pos = 33
                else:
                    pos = 50
            

            _format = '{:6.2f} '
            
            if not axis:
                print('g = ', _format.format(g), ' ' * pos, '*', sep='')
                k += 1
            else:

                if pos < zero_point:
                    indent = zero_point-pos-1
                    print('g = ', _format.format(g), ' ' * pos, '*',
                          ' '* indent, '|', sep='')
                    
                if pos == zero_point:
                    indent = zero_point
                    print('g = ', _format.format(g), ' ' * indent, '*'
                          , sep = '')
                    
                if pos > zero_point:
                    k += 1
                    indent = pos-zero_point-1
                    print('g = ', _format.format(g), ' ' * zero_point, '|',
                          ' ' * indent, '*', sep='')
            g += n
            
        if axis:
            indent = zero_point + 14
            print(" " * (indent), "|")
            print(" " * (indent), "V")
            print(" " * (indent), "g")

        print("\nКоличество значений функции a", gr,
          ", которые больше нуля: ", k, sep="")

        print()
