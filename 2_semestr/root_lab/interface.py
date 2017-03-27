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
    
def drawTable(roots, iter, x, errors, f,  name=""):

    width = 15

    line = '-' * (width * 8 - 6)

    print(name)
    print()
    text = ['№', 'x1', 'x2', 'x', 'f(x)', 'Итерации', 'Номер ошибки']
    print(textInRow(text, width))
    print(line)
    for i in range(len(roots)):

        values = [i, x[i][0], x[i][1], roots[i], f(roots[i]), iter[i], errors[i]]

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

    # if abs(values[4]) < 0.0001:
    #     values[4] = 0
    i = 0
    for value in values:
        if (i == 1 or i == 2) and abs(value) < 0.00001:
            value = 0
        if i == 4:
            s +=  ('{:^' + str(width) + 'e}').format(value) + '|'
        elif int(value) == value:
            s += ('{:^' + str(width) + '}').format(value) + '|'
        elif abs(value) < 0.00001:
            s +=  ('{:^' + str(width) + 'g}').format(value) + '|'
        else:
            s += str(f.format(value)) + '|'
        i += 1

    return s
