from math import sqrt, cos, trunc, pi
print("Введите следующие значения функции")
g1 = float(input("Начальное значение: "))
n = float(input("Шаг вычисления значений: "))
gn = float(input("Конечное значение: "))
print()
#g1 = float(-12)
#gn = float(4)
#n = 1
if gn <= g1 or n <= 0:
    print("Введеные значения некорректны")
else:
    

    frange = trunc((gn - g1) / n + 1)

    g = g1

    a1 = []
    a2 = []
    a3 = []

    print("|      a1        |       a2       |        a3      |      g      |")
    print("------------------------------------------------------------------")

    t = 0;

    #Вычисление значений трех функций
    for i in range(frange):
        a1.append(g**3 + 6.1 * g * g - 35.4 * g - 25.7)
        a2.append(g * g - cos(g*pi))
        #a3.append(g**2 - g - 1)
        a3.append(sqrt(a1[i]**2 + a2[i]**2))

        #center_f = '| {:^15}'
        center_f = '{}'
        point_f = '| {:^15.6}'
        
        #Построение таблицы значений
        print(center_f.format(point_f.format(a1[i])),
              center_f.format(point_f.format(a2[i])),
              center_f.format(point_f.format(a3[i])), 
              center_f.format('| {:^11.2f}'.format(g)), " |", sep="")
        print("------------------------------------------------------------------")
        
        g += n


    graph = input("Введите номер графика, который будет напечатан: ").split()
    graph = [int(x) for x in graph]
    

    if graph == 1:
        a = a1
    elif graph == 2:
        a = a2
    elif graph == 3:
        a = a3
    else:
        a = a3
        print("Такого графика не существует")

    
    g = g1
    maxa = 0
    
    """

    #Поиск максимального элемента функции
    for i in range(frange):
        if abs(a[i]) > maxa:
            maxa = abs(a[i])

    koef = 1

    #Нахождение отступа
    if maxa > 30:
        while maxa > 30:
            maxa = maxa / 1.2
            koef *= 1.2
            
    t = 0

    #Проверка, нужна ли нулевая ось Х(абсцисса)
    for i in range(frange):
        if a[i] < 0:
            t = 1
            break

    if t:
        _indent = 30
    else:
        _indent = 0

    k = 0

    print()
    
    #Построение графика
    for i in range(frange):
        if a[i] > 0:
            k += 1
        #if x < 0:
        print("X = ", "{:10.2f}".format(g), end = "", sep="")
        g += n
        indent = trunc(a[i]/koef)
        if a[i] > 0:
            print(" " * _indent, "|" * t, " " * indent, "*", sep="")
        elif a[i] < 0 and not trunc(a[i]/koef):
            indent += _indent
            print(" " * (indent-1), "*", " " * (abs(int(a[i]/koef))-1), "|" * t, sep="")
        elif a[i] < 0:
            indent += _indent
            print(" " * indent, "*", " " * (abs(int(a[i]/koef))-1), "|" * t, sep="")
    if t:
        _indent += 13
        print(" " * (_indent), "|")
        print(" " * (_indent), "V")
        print(" " * (_indent), "g")
    print("\nКоличество значений функции a", graph,
          " ,которые больше нуля: ", k, sep="")
    """
    #Построение графика 2
    T = []
    for i in range(frange-1):
        T.append(abs(a[i]-a[i+1]))
        print(abs(a[i]+a[i+1]))
    minT = 1000000000000
    for i in T:
        if i < minT:
            minT = i
    koef = 1
    print(T)
    
    while minT > 10:
        minT /= 10
        koef *= 10

    

    for i in T:
        print(trunc(i/koef))
    
    
#volkovdaniil9777@gmail.com
