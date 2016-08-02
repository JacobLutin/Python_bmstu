import numpy as np
#создание массивов

#одномерный массив

a = np.array((2, -3, 1, 9))
print(type(a))
print(a)
print(a.shape)
print(a.dtype, '\n')

b = np.array([-7, 7, 8, 4], dtype = float)
print(b)
print(b.shape)
print(b.dtype, '\n')

print('input array')
c = np.array(list(map(float, input().split())))
print(c, '\n\n\n')

# Двумерный массив
a = np.array([[1, 2, 3], [9, 8, 7]], 'int64')
print(type(a))
print(a)
print(a.shape)
print(a.dtype, '\n\n')

# Создание матрицы из списка и обратная операция
lst = [[4, 5, 6], [7, 8, 9]]

