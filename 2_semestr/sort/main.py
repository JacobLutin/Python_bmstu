import numpy as np
import time

def quickSort(A, left, right):

    i, j = left, right
    c = left + (right+left) // 2
    while i < j:
        while A[i] 



def test():

    arr = np.random.randint(100, size=100)

    if not np.array_equal(np.sort(arr), shellSort(arr)):
        print("error")
        print(arr)

n = 100

# for i in range(n):
#     test()

def deltaTime():

    arr = np.random.randint(100, size=10000)

    start = time.time()
    shellSort(arr)
    dt = time.time() - start

    return dt

dt = deltaTime()
print("{:.6f}".format(dt))


