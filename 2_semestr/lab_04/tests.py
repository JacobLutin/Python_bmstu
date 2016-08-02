import random as r

def RandomArray(n, a, b):

    array = []

    for i in range(n):
        array.append(r.randint(a, b))

    return array

def Test1():

    iterations = 50

    a = 0
    b = 100

    nMin = 256
    nMax = 1024

    arrayMin = RandomArray(nMin, a, b)
    arrayMax = RandomArray(nMax, a, b)

    return iterations, arrayMin, arrayMax

