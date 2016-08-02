import numpy
import time


def shake_sort(A):
    left = 0
    right = len(A) - 1

    while left <= right:

        for i in range(left, right, +1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

        right -= 1

        for i in range(right, left, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]

        left += 1

    return A


def deltatime(arr):
    start = time.time()
    shake_sort(arr)
    dt = time.time() - start

    return dt
