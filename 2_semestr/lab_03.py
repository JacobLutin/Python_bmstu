

from math import *
import numpy as np
import matplotlib.pyplot as plt


def main(test=False):
    

    if test:
        a, b, h, eps, n = test()
    else:
        a, b, h, eps, n = input()

    def f(x):
        return np.sin(x)

    def g(x):
        return np.cos(x)/x

    def d(x):
        return f(x) - g(x)

    roots = []
    extremums = []

    roots.append(root1(f, a, b, eps, h))
    extremums.append(goldenSectionExtremums(f, a, b, eps, roots[0]))

    roots.append(root1(g, a, b, eps, h))

    extremums.append(goldenSectionExtremums(g, a, b, eps, roots[1]))

    #printArray(roots)
    #printArray(extremums)

    x = np.arange(a, b, 0.1)

    inters = root1(d, a, b, eps, h)

    print(inters)

    print(f(inters))
    print(g(inters))

    drawPlot(x, [f, g, d], roots, extremums, inters)



def input():

    print("Введите следующие значения")

    print()

    a = input("Введите значение a:")
    b = input("Введите значение b:")
    eps = input("Введите точность (эпсилон):")
    n = input("Введите максимальное кол-во итераций:")

    params = [a, b, eps, n]

    return params


def test1():

    a = -10
    b = 10
    h = 1
    eps = 0.00005
    n = 100

    return a, b, h, eps, n


def form(x):
    return '{:.2f}'.format(x)

def printArray(arr):
    
    for i in arr:
        print(form(i))
        
def drawPlot(x, functions, roots, extremums, inters):

    #print(inters)

    f = functions[0]
    g = functions[1]
    d = functions[2]

    #plt.fill_between(x, f(x), g(x))
    plt.plot(x, f(x), 'k',
             x, g(x), 'r',
             inters, f(inters), 'ro',
             extremums[0], f(extremums[0]), 'go',
             roots[0], f(roots[0]), 'bo',
             extremums[1], g(extremums[1]), 'go',
             roots[1], g(roots[1]), 'bo')
             #x[inters], f(x)[inters], 'ro')
    #plt.subplot().spines['left'].set_position('center')
    plt.subplot().spines['bottom'].set_position('zero')
    plt.ylim(-2,2)
    plt.axis([-10, 10, -2, 2])
    plt.grid(True)
    plt.show()

    return True

def goldenSectionRoots():
    print('test');

def goldenSectionExtremums(f, a, b, eps, roots):

    const = (np.sqrt(5) + 1)/2

    extremums = []

    if a not in roots:
        roots.insert(0, a)
    if b not in roots:
        roots.append(b)
    
    for i in range(len(roots)-1):

        ax = roots[i]
        bx = roots[i+1]

        x1 = bx - ((bx - ax)/const)
        x2 = ax + ((bx - ax)/const)

        while abs(x1 - x2) > eps:

            if f((ax+bx)/2) < 0:
                if f(x1) >= f(x2):

                    ax = x1
                    x1 = x2
                    x2 = ax + ((bx - ax)/const)

                else:

                    bx = x2
                    x2 = x1
                    x1 = bx - ((bx - ax)/const)

            else:
                if f(x1) <= f(x2):

                    ax = x1
                    x1 = x2
                    x2 = ax + ((bx - ax)/const)

                else:

                    bx = x2
                    x2 = x1
                    x1 = bx - ((bx - ax)/const)

        c = (ax + bx) / 2


        if c != roots[i] and c != roots[i+1]:
            extremums.append(c)

    return extremums

def root1(f, a, b, eps, h):

    roots = []

    for x in range(a, b):

        x1 = x
        x2 = x+h

        if f(x1) * f(x2) <= 0:

            while abs(x2 - x1) > eps:

                c = (x1 + x2) / 2

                if f(x1) * f(c) <= 0:
                    x2 = c
                else:
                    x1 = c
            
            #if not np.isclose([c], [a], atol=10)[0]
            #and not np.isclose([c], [b], atol=10)[0]:

            roots.append(c)
    
    return roots

def intersection(x, f, g):

    f = f(x)
    g = g(x)
    
    inters = np.argwhere(np.isclose(f, g, atol=10)).reshape(-1)

    return inters


def areaCalc(f, g, inters):

    area = 0
    i = 0

    while i < len(inters):

        a = inters[i]
        b = inters[i+1]

        weddleMethod(f, a, b)

        i += 2

    return


def weddleMethod(f, a, b):

    n = 4

    h = (b - a) / n

    sum = 0
    x = a

    while x < b - h:
        sum += 7 * f(x)
        x += h
        sum += 32 * f(x)
        x += h
        sum += 12 * f(x)
        x += h
        sum += 32 * f(x)
        x += h
        sum += 7 * f(x)

    return 2/45 * h * sum

main(test1)           
