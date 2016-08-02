from random import shuffle

def issorted(array):
    return not any(
        array[i] > array[i+1]
        for i in xrange(len(array)-1)
    )

def bogosort(array):
    while not issorted(array):
        shuffle(array)

    return array

A = [9, 8, 10, 7, 11, 5, 15, 4, 16]

B = bogosort(A)

print(B)
