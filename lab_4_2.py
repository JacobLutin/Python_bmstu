"""
Лабораторная работа 4.2

Вычислить по формуле и напечатать массив А(13)

a(i) = { sqrt(b(i)), если b(i) <= 7.8 | sqrt4(b), если b(i) > 7.8 }

где b(i) - элемент массива B(13). Если в массиве B окажется хотя бы один
отрицательный элемент, то прекратить вычисления и выдать соответсвующий текст"

Лютин Я. С. Группа ИУ7-11

"""

from math import sqrt

B = input("Введите не более тринадцати чисел через пробел: ").split()

B = [float(x) for x in B]

A = []

boolean = True

for b in B:
    if b < 0:
        boolean = False
        break
    elif b <= 7.8:
        A.append(sqrt(b))
    else:
        A.append(sqrt(sqrt(b)))

if boolean:
    print("Получившийся массив: ", end="")
    A = [print("{:.4f},".format(x), end=" ") for x in A]
else:
    print("Массив содержит отрицательный элемент")


        
