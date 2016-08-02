
n = 500
frange = n * 10

def f(x):
    return ((x + 1)**2)/(2 * x**3)

for x in range(1, frange):
    if x % n == 0:
        result = f(x)
        print(result)
