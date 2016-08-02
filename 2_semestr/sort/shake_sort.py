import numpy as np
import time

def shaker_sort(A):

    left = 0
    right = len(A) - 1

    while left <= right:

        for i in range(left, right):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

        right -= 1

        for i in range(right, left, -1):
            if A[i-1] > A[i]:
                A[i-1], A[i] = A[i], A[i-1]

        left += 1

    return A

n = 100

for i in range(n):
    arr = np.random.randint(100, size=100)
    if not np.array_equal(np.sort(arr), shaker_sort(arr)):
        "error"

def deltatime(A):
    start = time.time()
    shaker_sort(A)
    dt = time.time() - start

    return dt

arr = np.random.randint(100, size=1000)

print(deltatime(arr))













































