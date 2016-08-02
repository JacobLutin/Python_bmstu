array = [9, 12, 4, 6, 5, 1]
#array = [5, 4, 3, 2, 1]

def insertionSort1(A):
    counter = 0
    for i in range(1, len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
            counter += 1
        A[j+1] = key
    return A, counter

def insertionSort2(A):
    counter = 0
    for i in range(1, len(A)):
        j = i
        while j > 0 and A[j-1] > A[j]:
            A[j-1], A[j] = A[j], A[j-1]
            j -= 1
            counter += 1
    return A, counter

res = insertionSort1(array)
print(res)
array = [9, 12, 4, 6, 5, 1]
res = insertionSort1(array)
print(res)
#print(x)
