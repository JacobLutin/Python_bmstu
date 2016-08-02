import numpy as np
import time

def quickSort(mass,left,right):
    i,j = left,right
    centr = left+(right-left)//2
    while i < j:
        while mass[i] < mass[centr]:
            i += 1
        while mass[j] > mass[centr]:
            j -= 1
        if i <= j:
            mass[i],mass[j] = mass[j],mass[i]
            i += 1
            j -= 1
    if left < j:
        quickSort(mass,left,j)
    if right > i:
        quickSort(mass,i,right)
    return(mass)

 #print(quicksort(mass,0,len(mass)-1))

"""
def quickSort(A, left, right):
    i, j = left, right
    c = left+(right-left)//2
    while i < j:
        while A[i] < A[c]:
            i += 1
        while A[j] > A[c]:
            j -= 1
        if i <= j:
            A[i], A[j] = A[j], A[i]
            i += 1
            j -= 1
    if left < j:
        quickSort(A, left, j)
    if right > i:
        quickSort(A, i, right)
    return A
"""

def test():

    arr = np.random.randint(10, size=10)

    if not np.array_equal(np.sort(arr), quickSort(arr, 0, len(arr)-1)):
        print('error')
        print(arr)

def deltaTime():
    arr = np.random.randint(10, size=30)

    start = time.time()
    print(quickSort(arr, 0, len(arr)-1))
    dt = time.time() - start

    return dt

dt = deltaTime()
print('{:.6f}'.format(dt))
