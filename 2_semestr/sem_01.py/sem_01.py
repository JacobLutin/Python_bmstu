import numpy as np
from math import *

def vector(array):

    print('print')


def revert(matrix):

    n = len(matrix[0])

    for i in range(0, n//2):
        for j in range(i, n-i-1):
            x = matrix[i][j]
            # print(matrix[n-(j+1)][j])
            matrix[i][j] = matrix[n-(j+1)][j]
            matrix[n-(j+1)][j] = matrix[n-(i+1)][n-(j+1)]
            matrix[n-(j+1)][n-(j+1)] = matrix[i][n-(i+1)]
            matrix[i][n-(i+1)] = x

    return matrix





n = 9
a = np.arange(n)
a1 = np.copy(a)
a2 = np.reshape(a1, (sqrt(n), sqrt(n)))
print(a2)

print(revert(a2))