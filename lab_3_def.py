"""

Защита лабораторной работы №3

Лютин Я.С. группа ИУ7-11

"""

eps = float(input("Введите эпсилон(точность) последовательности: "))
x = float(input("Введите начальное значение первого члена последовательности (х): "))
#m = int(input("Введите максимальное значение прохождений последовательностью цикла: "))
#n = float(input("Введите шаг печати членов последовательности: "))

a = x
y = x

k = 1
i = 1

print("|{:^4}".format(k), '| {:^11}'.format('{:.3}'.format(a)), '| {:^10}'.format('{:.3}'.format(y)), " |", sep="")

#for i in range(3, m+1, 2):
while (abs(a) >= abs(eps)):
    i += 2
    k += 1

    a *= (x * x)/(i * (i - 1))
    a *= -1

    y += a

    print("|{:^4}".format(k), '| {:^11}'.format('{:.3}'.format(a)), '| {:^10}'.format('{:.6}'.format(y)), " |", sep="")

print("Конечная сумма ряда равна ", '{:.6}'.format(y))
    