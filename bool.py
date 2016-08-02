from math import *

def f(x):
    return x * x

def methodBoole(f, a, b, n):
    
    h = (b - a) / n
    sum = 7 * (f(a) + f(b))
    sum1 = 0; sum2 = 0; sum3 = 0

    for i in range(1, n):
        if i % 2 == 1:
            sum1 += f(a+h*i)
        else:
            if i % 4 == 0:
                sum3 += f(a+h*i)
            else:
                sum2 += f(a+h*i)

    sum = sum + 32*sum1 + 12*sum2 + 7*2*sum3

    return sum * h * 2 / 45

def methodBooleNew(f, a, b, n):

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
b = 6
n = 4

print(methodBoole(f, a, b, n))
print(methodBooleNew(f, a, b, n))
