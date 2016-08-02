def InsertionSort(arr):

    for i in range(1, len(arr)):

        key = arr[i]

        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1

        arr[j+1] = key

    return arr[j+1]


def BubbleSort(arr):

    for i in range(len(arr)-1):

        for j in range(len(arr)-i-1):

            if arr[j] > arr[j+1]:
                c = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = c

    return arr

