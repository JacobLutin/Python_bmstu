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

a = [8, 6, 7, 4, 3, 5, 6, 9, 10]

print(bogosort(a))
