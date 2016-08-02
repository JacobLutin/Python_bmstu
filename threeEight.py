def f(x):
    return x * x

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

a = 0
b = 3
n = 6

print(threeEight(f, a, b, n))
