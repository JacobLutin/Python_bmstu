def insertion_sort_1(A):

    for i in range(len(A)):

        x = A[i]
        pos = 0

        for j in range(i):
            if x <= A[j]:
                pos = j
                break

        for j in range(i, pos, -1):
            A[j] = A[j-1]

        A[pos] = x

    return A

def insertion_sort_2(A):

    print(A)

    for i in range(1, len(A)):

        x = A[i]

        j = i - 1

        while A[j] > x and j >= 0:
            A[j+1] = A[j]
            j -= 1
            

        A[j+1] = x

        print(A)

    return A


arr = [4, -1, 3, 2, 1]

arr = insertion_sort_2(arr)

#print(arr)
            
