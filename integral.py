"""
Численное вычисление интеграла методами Трапеций и Уэддля
"""

from math import *

def f(x):
    #return sqrt(x)
    return x+1

def trapezeMethod(a, b, n):
    
    i = 0

    h = (b - a) / n

    for x in range(1, n):
        i += f(a + h * x)

    i = h * ((f(a) + f(b))/2 + i)

    return i

x = trapezeMethod(0, 5, 100)
print(x)
"""
def weddleMethod(a, b, n):
    
    
    h = (b - a) / n # шаг
    
    i = 0 #текущее значение интеграла
    x = a
    
    k = [1, 5, 1, 6, 1, 5, 1]

    n += n // 6
    
    for j in range(n):
        
        i += k[j % 7] * f(x)
        if j % 7 < 6:
            x += h

        
        f(x)dx = 3h/10*[f(x) + 5f(x) + f(x) + 6f(x) + f(x) + 5f(x) + f(x)]

        i += f(x)
        x += h
        i += 5 * f(x)
        x += h
        i += f(x)
        x += h
        i += 6 * f(x)
        x += h
        i += f(x)
        x += h
        i += 5 *f(x)
        x += h
        i += f(x)
        
        
    return i * h * 3/10;
    
    
    def calculation(x):
        calcSum = 0

        for i in range(7):
            calcSum += k[i] * f(a + x*step - (6-i)*(step/6))

        return calcSum

    for x in range(1, n-1):
        integral += calculation(x)

    integral = integral * step/6
    
    return integral

    
    
    k = [41, 216, 27, 272, 27, 216]
    
    step = (b - a) / n

    x = a
    
    integral = 0
    
    for j in range(n):
        
        for i in range(7):
            print(integral)
            integral += k[i % 6] * f(x)
            x += step / 6
        
    x -= step / 6

        
    integral = step * integral / 840
    
    return integral
    

def SimpsonMethod(a, b, n):

    h = (b - a) / (2 * n)
    
    i = 0
    
    x = a + h

    while x < b:
        i += 2 * f(x)
        x += h
        i += 3 * f(x)
        x += h

    i = (3*h)/ 8 * (i + f(a) + f(b));

    return i
    
def printTable():
    

    a = 1
    b = 3
    n1 = 100
    n2 = 600000

    inp = "Введите начальное и конечное значения функции: "
    a, b = map(int, input(inp).split())
    inp = "Введите первое и второе количества шагов (кратные 6): "
    n1, n2 = map(int, input(inp).split())
    
    if n1 < 6 or n1 % 6 != 0 or n2 < 6 or n2 % 6 != 0:
        print("Некорректно введнное количество шагов (не кратное 6)")
        return
    
    print('Введите эпсилон(точность) для определения количества')
    eps = input('шагов вычисления интеграла методом Трапеций: ')
    print()

    lnIndent = '-' * 70
    f = '{:^20} | '

    pn1 = "при n = " + str(n1)
    pn2 = "при n = " + str(n2)

    print("|", "Метод".center(20, " "), "|",  pn1.center(20, " "), "|", pn2.center(20, " "), "|")
    def printMethod(name, integral1, integral2):

        
        name = '{:^20} | '.format(name)
        if integral1 != 0 or trunc(integral2) != integral2:
            integral1 = f.format("{:.7e}".format(integral1))
        else:
            integral1 = f.format("{:.7}".format(integral1))
        if integral2 != 0 or trunc(integral2) != integral2:
            integral2 = f.format("{:.7e}".format(integral2))
        else:
            integral2 = f.format("{:.7}".format(integral2))
        line = "| " + name + integral1 + integral2

        print(line)
        print(lnIndent)

    print(lnIndent)

    integral1 = trapezeMethod(a, b, n1)
    integral2 = trapezeMethod(a, b, n2)
    

    printMethod("Метод трапеций", integral1, integral2)

    integral1 = weddleMethod(a, b, n1)
    integral2 = weddleMethod(a, b, n2)

    printMethod("Метод Уэддля", integral1, integral2)
    
    eps = float(eps)

    stepNum = 1

    while (abs(trapezeMethod(a, b, stepNum*2) - trapezeMethod(a, b, stepNum)) > eps):
        stepNum *= 2
    
    print('\nДля вычисления интеграла методом трапеций с точностью до', sep='');
    print(eps,' потребовалось ', stepNum,' шагов.', sep='')
    print()
    print("Результат:", "{:.7g}".format(trapezeMethod(a, b, stepNum)))

printTable()
"""
    
