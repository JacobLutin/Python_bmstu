
n = 10
frange = n*10

def f(x):
    return (5 * x + 1)/(7 - 9 * x)

for x in range(frange):
    if x % n == 0:
        result = f(x)
        print(result)
