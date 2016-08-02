from math import sqrt, cos, trunc, pi

#g1 = input(float(x))
#gn = input(float(x))
#n = input(float(x))

g1 = float(-10)
gn = 2
n = 0.5

frange = trunc((gn - g1) / n + 1)

g = g1

a1 = []
a2 = []
a3 = []

for i in range(frange):
    #a1.append(g**3 + 6.1 * g * g - 35.4 * g - 25.7)
    a1.append(g**3)
    a2.append(g * g - cos(g*pi))
    #a3.append(sqrt(a1*a1 + a2*a2))
    """
    print('| {:^11}'.format('{:.2f}'.format(g)),
          '| {:^10}'.format('{:.5f}'.format(a1[i])),
          '| {:^10}'.format('{:.5f}'.format(a2[i])),
          '| {:^10}'.format('{:.5f}'.format(a2[i])), " |", sep="")
    print("---------------------------------------------------")
    """
    g += n

a = a1
g = g1
mina = 0

k = 0

for i in range(frange):
    if (a[i] < 0 and a[i] < mina):
        mina = a[i]
    if a[i] > 0:
        k += 1
        



mina = trunc(abs(mina) / 3) + 10

for i in range(frange):
    print("X = ", "{:^5}".format("{:.2f}".format(g)), end = "")
    if a[i] < 0:
        indent = mina + trunc(a[i]/3)
        _indent = abs(trunc(a[i]/3))
        print(" " * indent, "*", " " * _indent, "|", sep="")
    else:
        indent = trunc(a[i]/3)
        if indent < 2:
            indent = 0
        else:
            indent -= 1
        print(" " * (mina+1), "|"," " * (indent), "*", sep="")
    g += n

print(" " * (mina + 10), "|")
print(" " * (mina + 10), "V")
print(" " * (mina + 10), "X")

print("Количество значений функции а, которые больше нуля:", k)
