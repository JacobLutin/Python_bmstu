from math import pi

"""
eps = float(input("Введите эпсилон(точность) последовательности: "))
x = float(input("Введите начальное значение первого члена последовательности (х): "))
m = int(input("Введите количество элементов: "))
n = int(input("Введите шаг печати членов последовательности: "))
"""
eps = 0.00005
x = 1
m = 100
n = 1

a = x
y = pi/2 - a

print("|{:^4}".format(1.0), '| {:^11}'.format('{:.3}'.format(a)), '| {:^10}'.format('{:.6}'.format(y)), " |", sep="")

for i in range(m+1):
    a = float(pow(n, -1) * (pow(x, 2 * n - 1) / (2 * n - 1)))

    y += a
    
    print("|{:^4}".format(i), '| {:^11}'.format('{:.3}'.format(a)), '| {:^10}'.format('{:.6}'.format(y)), " |", sep="")

print("Конечная сумма ряда равна ", '{:.6}'.format(y))
