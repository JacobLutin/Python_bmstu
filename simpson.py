from math import *

def f(x):
    return sin(x)

def threeEight(f, a, b, n):

    h = (b - a) / n

    x = a

    sum = 0

    while x < b - h:
        sum += f(x)
        x += h
        sum += 3 * f(x)
        x += h
        sum += 3 * f(x)
        x += h
        sum += f(x)

    return 3/8 * h * sum

def simpson(f, a, b, n):

    sum = (b-a)/6 * (f(a) + 4 * f((a + b)/2) + f(b))

    return sum

def boole(f, a, b, n):

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

a = 0
b = 3
n = 3

print(threeEight(f, a, b, n))
print(simpson(f, a, b, n))

a = 0
b = 3
n = 4

print(boole(f, a, b, n))

