n =
frange = n * 10

def f(x):
    return (2**x + 3**x)/(2**x - 3**x)

for x in range(1, frange):
    if x % n == 0:
        result = f(x)
        print(result)
