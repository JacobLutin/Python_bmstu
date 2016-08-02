

def insertion_sort(A):

    for i in range(len(A)):
        key = A[i]
        j = i - 1
        while j >= 0 and A[j] > key:
            A[j+1] = A[j]
            j -= 1
        A[j+1] = key

    return A

arr = [9,8,6,4,1]
print(insertion_sort(arr))
