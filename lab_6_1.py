"""
Лабораторная работа № 6.1

Задана матрица Q(12, 10). Вычеркнуть строку содержащую минимальный элемент.
В преобразованной матрице подсчитать в каждом столбце количество элементов,
превышающих значения произведения элементов соотвествующих столбцов матрицы.
Нового массива для хранения матрицы, не вводиить. Напечатать матрицу Q в виде
матрицы и количество элементов.

Лютин Я.С., Группа ИУ7-11
"""
Q = [[-1, 2, 3, 5],
     [4, 0],
     [7, -8, 9, 1],
     [11, 12, -3, 5],
     [9, 0, 1, 0, 9, 10]]

Q = []

i = 0
if not Q:
    print("Задайте матрицу, по несколько элементов в строке: ")
    print("(после окончания ввода, оставьте следующую строку пустой)\n")

    while True:
        s = input()
        if not s:
            break
        Q.append([int(x) for x in s.split()])

        if i == 0:
            minE = Q[0][0]
            minS = 0
        
        for x in Q[i]:
            if x < minE:
                minE = x
                minS = i
        i += 1
else:
    minE = Q[0][0]
    minS = 0
    for i in range(len(Q)):
        for j in range(len(Q[i])):
            
            if Q[i][j] < minE:
                minE = Q[i][j]
                minS = i
                print()

max_col = 0
for i in Q:
    col = len(i)
    if col > max_col:
        max_col = col

col = max_col

f = '{:^6}'
indent = " " * 20
line = "-" * 7 * col

print("Исходная матрица: ")
for i in Q:
    k = 0
    print(indent, end="  |")
    for j in i:
        print(f.format(j), end="|", sep = "")
        k += 1
    line = "-" * 7 * k
    print("\n", indent, line)

Q=Q[:minS]+Q[minS+1:len(Q)]

max_col = 0
for i in Q:
    col = len(i)
    if col > max_col:
        max_col = col

col = max_col

f = '{:^6}'
indent = " " * 20
line = "-" * 7 * col



print("Измененная матрица: ")

for i in Q:
    k = 0
    print(indent, end="  |")
    for j in i:
        print(f.format(j), end="|", sep = "")
        k += 1
    line = "-" * 7 * k
    print("\n", indent, line)

print("Количество элементов:  ", end="")
i = 0
j = 0
while j < max_col:
    col_sum = 0
    p = 1
    for i in range(len(Q)):
        if len(Q[i]) > j:
            p *= Q[i][j]
    for i in range(len(Q)):
        if len(Q[i]) > j:
            if Q[i][j] > p:
                col_sum += 1
    print(f.format(col_sum), end = " ")
    j += 1



