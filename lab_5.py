from math import *
"""
print("Введите следующие значения функции")
g1 = float(input("Начальное значение: "))
n = float(input("Шаг вычисления значений: "))
gn = float(input("Конечное значение: "))
print()
"""

g1 = float(-20)
gn = float(20)
n = 2

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
        if tan(3*g) != 0:
            a1.append(sin(7*g)/tan(3*g))
        else:
            a1.append(0)
        a2.append(g * g - cos(g*pi))
        a3.append(sqrt(a1[i]**2 + a2[i]**2))

        point_f = '| {:^15.6}'

         #Построение таблицы значений
        """
        print(point_f.format(a1[i]),
              point_f.format(a2[i]),
              point_f.format(a3[i]),
              '| {:^12.2f}'.format(g), " |", sep="")
        print(line)
        """
        g += n

    print("\nВведите через пробел номера графиков,", end="")
    print(" которые будет напечатаны: ")

    #Выбор графика для печати
    graph = map(int, input().split())
    for gr in graph:
        if gr == 1:
            a = a1
            print(' ' * 30, "График функции a1")
        elif gr == 2:
            a = a2
            print(' ' * 30, "График функции a2")
        elif gr == 3:
            a = a3
            print(' ' * 30, "График функции a3")
        else:
            print("Такого графика не существует")
            break


        #Нахождение максимального и минимального значений
        fMin = min(a)
        fMax = max(a)

        _indent = 60
        print(' ' * (_indent+6), 'g', sep='')

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
                """
                if pos == 0 and a[i] > 0:
                    pos += 1
                elif a[i] > 0:
                    pos += 1
                """
                #print(pos)

            else:
                if fMax < 0:
                    pos = 16
                elif fMax == 0:
                    pos = 33
                else:
                    pos = 50


            _format = ' {:^10.2f} '

            print(' ', end='')

            if not axis:
                print(' ' * pos, '*', sep='', end='')
                print(' ' * (_indent-pos), _format.format(g), sep='')
                k += 1
            else:

                if pos < zero_point:
                    indent = zero_point-pos-1
                    print(' ' * pos, '*',
                          ' '* (indent), '|', sep='', end='')
                    print(' ' * (_indent-zero_point), _format.format(g), sep='')


                if pos == zero_point:
                    indent = zero_point
                    print(' ' * indent, '*'
                          , sep = '', end='')
                    print(' ' * (_indent-zero_point), _format.format(g), sep='')

                if pos > zero_point:
                    k += 1
                    indent = pos-zero_point-1
                    print(' ' * zero_point, '|',
                          ' ' * indent, '*', sep='', end='')
                    print(' ' * (_indent-pos), _format.format(g), sep='')
            g += n

        if axis:
            indent = zero_point
            print(" " * (indent), "|")
            print(" " * (indent), "V")
            print(" " * (indent), "g")

        print("\nКоличество значений функции a", gr,
          ", которые больше нуля: ", k, sep="")

        print()
