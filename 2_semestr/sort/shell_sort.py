import numpy as np
import time

def shell_sort(A):

    n = len(A)
    h = n // 2
    while h > 0:
        for i in range(n-h):
            j = i
            while j >= 0 and A[j] > A[j+h]:
                A[j], A[j+h] = A[j+h], A[j]
                print(A)
                j -= h
        print(h)
        h = h // 2

    return A

def test():
    arr = np.random.randint(-100, 100, size=100)

    start = time.time()
    shell_sort(arr)
    dtime = time.time() - start

    print(dtime)

    if not np.array_equal(shell_sort(arr), np.sort(arr)):
        print('error')
        print(shell_sort(arr))


#for i in range(100):
#    test()

arr = np.random.randint(10, size=10)
arr = np.array([9, 8, 7, 6, 5, 4, 3, 2, 1])
print(arr)
shell_sort(arr)





