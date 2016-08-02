import numpy as np

a = np.arange(12)
a1 = np.copy(a)
print("Исходная матрицы")
a2 = np.reshape(a1, (3, 4))
print(a2, '\n')

a2 = a2.T
print("Транспонированная матрица")
print(a2, '\n')


#min, max, sum, сортировка

b = np.array([[2, 8, 0], [6, 1, 3], [4, 7, 5]])
print("Новая исходная матрица\n", b, '\n')

dsum = b.sum()
dmin = b.min()
dmax = b.max()
print('Некоторые значения для всей матрицы')
print('sum=', dsum, ' min=', dmin, ' max=', dmax, '\n')

mincol = b.min(axis=0)
maxrow = b.max(axis=1)
print('Значения min и max для столбцов и строк')
print('min в столбцах = ', mincol, ' max в строках = ', maxrow, '\n')




# Функция sort описание
# sort(axis=-1, kind='quicksort', order=None)
# axis - ось, по которой идет сортировка. 
# kind - тпи сортировки. Возможные значения 'quicksort', 'mergesort', 'heapsort'

c = b.copy()
c.sort(axis=0, kind='mergesort')
print('Сортировка столбцов\n', c)
print()

c = b.copy()
c.sort(axis=1, kind='mergesort')
print('Сортировка строк\n', c)
print()
