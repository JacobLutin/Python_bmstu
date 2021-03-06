"""
Лабораторная работа № 6.2

Задана целочисленная квадратная матриц D(k, k), k <= 8. Повернуть ее на 180
градусов по часовой стрелке. Напечатать исходную матрицу, а также
сформированную. Дополнительных массивов не использовать

Лютин Я.С., Группа ИУ7-11
"""

print("Задайте матрицу, по несколько элементов в строке: ")
print("(после окончания ввода, оставьте следующую строку пустой)\n")


D = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9],
     [11, 12, 3]]

D = []

if not D:
    while True:
        s = input()
        if not s:
            break
        D.append([int(x) for x in s.split()])


print("Исходная матрица: ")
for row in D:
    for x in row:
        print(x, end = " ")
    print()

print("\nМатрица, перевернутая на 180 градусов:")
for i in range(len(D)-1, -1, -1):
    for j in range(len(D[i])-1, -1, -1):
        print(D[i][j], end=" ",)
    print()
