import numpy as np
# Массивы специального вида, можно задавать тип элементов

# Пустая матрица
a = np.empty((3, 2))
print(a, '\n')

# Единичная матрица
b = np.identity(4)
print(b, '\n')

# Нулевая матрица
c = np.zeros((4, 5), int)
print(c, '\n')
