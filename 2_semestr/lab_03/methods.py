import numpy as np

def goldenSection(f, x1, x2, eps, maxiter, iter=0):


    def fp(x):
        dx = 0.000001
        return (f(x + dx) - f(x)) / dx
    
    if f(x1) == 0:
        return x1, iter
    if f(x2) == 0:
        return x2, iter

    #const = (1 + np.sqrt(5)) / 2

    #x3 = x2 - (x2 - x1) / const
    #x4 = x1 + (x2 - x1) / const

    if fp(x2) != 0:
        x3 = x2 - f(x2)/fp(x2)
    else:
        x3 = x2 - f(x2)/0.00001

    if fp(x1) != 0:
        x4 = x1 + f(x1)/fp(x1)
    else:
        x4 = x1 + f(x1)/0.00001

    if f(x1) * f(x2) < 0:
        if iter < maxiter:
            if abs(x1 - x2) > eps:
                if abs(f(x3)) > abs(f(x4)):
                    if f(x3) * f(x2) > 0:
                        return x3, iter
                    return goldenSection(f, x3, x2, eps, maxiter, iter+1)
                else:
                    if f(x1) * f(x4) > 0:
                        return x3, iter
                    return goldenSection(f, x1, x4, eps, maxiter, iter+1)
            else:
                return x3, iter
        else:
            return x3, iter

    return None

def iteration(f, a, b, h, eps, maxiter):

    roots = []

    x1 = a
    x2 = a + h


    x = []
    iter = []
    errors = []

    while (x2 < b) or (x1 > b):

        if x2 > b:
            h = b - x1
            x2 = x1+h

        root = False

        if goldenSection(f, x1, x2, eps, maxiter) != None:
            root, k = goldenSection(f, x1, x2, eps, maxiter)

            if k == maxiter:
                errors.append(1)
            else:
                errors.append(0)

            roots.append(root)
            iter.append(k)
            x.append([x1, x2])

        x1 = x2
        x2 += h
        
    return roots, iter, x, errors

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

"""


def goldenSectionExtremums(f, a, b, eps, roots):

    const = (np.sqrt(5) + 1) / 2

    extremums = []

    if a not in roots:
        roots.insert(0, a)
    if b not in roots:
        roots.append(b)

    for i in range(len(roots)-1):

        k = 0

        ax = roots[i]
        bx = roots[i+1]

        x1 = bx - ((bx - ax)/const)
        x2 = ax + ((bx - ax)/const)

        while abs(x1 - x2) > eps:

            if f((ax+bx) / 2) < 0:
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

            k += 1

        c = (ax + bx) / 2


        if c != roots[i] and c != roots[i+1]:
            extremums.append(c)

    return extremums

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
"""
