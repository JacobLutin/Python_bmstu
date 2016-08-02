def f(x):
    return x * x

def methodParabol(f, a, b, n):

    h = (b - a) / (n * 2)

    x = a

    sum = f(x)

    x += h

    for i in range(0, n//2):
        sum += 4 * f(x)
        x += h
        sum += 2 * f(x)
        x += h

    sum += f(x)

    return h/3 * sum

a = 0
b = 3
n = 2

print(methodParabol(f, a, b, n))
    
