"""

Заданы координаты вершины треугольника. Найти высоту,
проведенную из наибольшего угла треугольника. Переполнения не будет.

Лютин Я. С. ИУ7-11

"""

from math import sqrt

print(30 % 17 + 1)

print("Введите координаты трех точек треугольника через пробел")

x1, y1 = map(int, input("Первая точка: ").split())
x2, y2 = map(int, input("Вторая точка: ").split())
x3, y3 = map(int, input("Третья точка: ").split())

a = sqrt((x1 - x2)**2 + (y1 - y2)**2)
b = sqrt((x2 - x3)**2 + (y2 - y3)**2)
c = sqrt((x1 - x3)**2 + (y1 - y3)**2)

if a + b <= c or a + c <= b or b + c <= a:
    print("Такого треугольника не существует")
else:
    
    p = (a + b + c) / 2

    s = sqrt(p * (p - a) * (p - b) * (p - c))

    if a >= b >= c or a >= c >= b:
        h = s * 2 / a
    elif b >= a >= c or b >= c >=a:
        h = s * 2 / b
    elif c >= a >= b or c >= b >= a:
        h = s * 2 / c

    print("Длина высоты равна ", "{:.2f}".format(h))

             
             
