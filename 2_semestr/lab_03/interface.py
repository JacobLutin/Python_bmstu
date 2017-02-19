from methods import *
from draw import *

def getParams():

    print("Введите следующие значения")

    print()

    a = float(input("Введите значение a: "))
    b = float(input("Введите значение b: "))
    h = float(input("Введите шаг h: "))
    eps = float(input("Введите точность (эпсилон): "))
    n = int(input("Введите максимальное кол-во итераций: "))

    params = [a, b, h, eps, n]

    return params

def menu(functions, test=False):

    points = []
    
    if not test:
        #x, a, b, h, eps, n = test()
    
        print("1) Показать на графике корни")
        print("2) Показать на графике экстремумы")
        print("3) Показать на графике точки перегиба")
        print("4) Показать на графике несколько точек")
        print("5) Вычислить площадь пересечения двух функций")
        print()

        choice = int(input('   -----> '))
        print()

        #if choice in [1, 2, 3]:
            #a, b, h, eps, n = getParams()
            #x, a, b, h, eps, n = test()
        if choice == 4:
            s = "Введите одну или несколько цифр через пробел, для вывода точек на графике:"
            print(s)
            print("1) Корни")
            print("2) Экстремумы")
            print("3) Точки перегиба")
            points = input('   -----> ').split()
            points = [ int(x) for x in points]

        a, b, h, eps, n = getParams()
    else:
        choice, a, b, h, eps, n = test()
        if choice == 4:
            print("ok")
            points = [1, 2, 3]

    f = functions[0]
    g = functions[1]
    d = functions[2]

    def fp(x):
        dx = 0.000001
        return (f(x + dx) - f(x)) / dx

    def fpp(x):
        dx = 0.000001
        return (fp(x + dx) - fp(x)) / dx

    pointsNames = []

    if choice in [1, 2, 3]:

        points = [choice]

    if choice == 5:

        roots = iteration(d, a, b, h, eps, n)[0]

        s = 0

        for i in range(len(roots)-1):
            s1 = weddleMethod(f, roots[i], roots[i+1])
            s2 = weddleMethod(g, roots[i], roots[i+1])

            if s2 * s1 > 0:
                if abs(s1) > abs(s2):
                    s += abs(s1) - abs(s2)
                else:
                    s += abs(s2) - abs(s1)
            elif s1 * s2 < 0:
                s += abs(s1) + abs(s2)

        if abs(s) < 0.0001:
            s = 0
            print()
            print("Площадь пересечения графиков функций: 0")
        else:
            print()
            print("Площадь пересечения графиков функций:", '{:.5f}'.format(s))

        drawPlot(a, b, functions, roots, [], [], points=['area'])

        return True

    roots = []
    exes = []
    infp = []

    if 1 in points:
        pointsNames.append('roots')
        roots, iter, x, errors = iteration(f, a, b, h, eps, n)
        CreateTable(roots, iter, x, errors, f, 'Корни')

    if 2 in points:
        pointsNames.append('exes')
        exes, iter, x, errors = iteration(fp, a, b, h, eps, n)
        CreateTable(exes, iter, x, errors, f, 'Экстремумы')

    if 3 in points:
        pointsNames.append('infp')
        infp, iter, x, errors = iteration(fpp, a, b, h, eps, n)
        CreateTable(infp, iter, x, errors, f, 'Точки перегиба')

    print("Типы ошибок:")
    print('0) - ошибки нет')
    print('1) -  превышено число итераций')

    drawPlot(a, b, functions, roots, exes, infp, points=pointsNames)

    return True


def CreateTable(roots, iter, x, errors, f,  name=""):

    width = 15

    line = '-' * width * 8

    print(name)
    print()
    text = ['№', 'x1', 'x2', 'x', 'f(x)', 'Итерации', 'Номер ошибки']
    print(textInRow(text, width))
    print(line)
    for i in range(len(roots)):

        values = [i+1, x[i][0], x[i][1], roots[i], f(roots[i]), iter[i], errors[i]]

        print(valuesInRow(values, width ))

    print()

def textInRow(words, width):

    s = '|'

    # s = '{:^' + str(width) + 'f}'
    for word in words:
        s += word.center(width) + '|'

    return s

def valuesInRow(values, width):

    f = '{:^' + str(width) + 'f}'
    s = '|'

    if abs(values[4]) < 0.0001:
        values[4] = 0

    for value in values:
        if int(value) == value:
            s += ('{:^' + str(width) + '}').format(value) + '|'
        elif abs(value) < 0.00001:
            s +=  ('{:^' + str(width) + 'g}').format(value) + '|'
        else:
            s += str(f.format(value)) + '|'

    return s
