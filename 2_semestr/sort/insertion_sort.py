import numpy as np
import time

def insertion_sort(A):

    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

    return A


def test():
    arr = np.random.randint(-100, 100, size=100)

    start = time.time()
    insertion_sort(arr)
    dtime = time.time() - start

    print('{:.5f}'.format(dtime))


    if not np.array_equal(insertion_sort(arr), np.sort(arr)):
        print('error')
        print(insertion_sort(arr))


for i in range(100):
    test()




