def createMatrix(n):

    m = [[0 for x in range(n)] for x in range(n)]

    k = 2

    for i in range(1, n):
        for j in range(0, i):
            m[i][j] = k
            k += 1
            

    for i in range(n):
        m[i][i] = 0

    for i in range(n):
        for j in range(i+1, n):
            m[i][j] = 1

    return m


def writeMatrix(m):

    for arr in m:
        for x in arr:
            print('{:^5}'.format(x), end=' ')
        print()

def writeArray(arr):

    for x in arr:
        print('{:.2f}'.format(x), end=' ')

    print()

def calcAverage(arr):

    s = 0

    for i in arr:
        s += i

    return s / len(arr)

def matrixLoop(m):

    average = []

    for i in range(len(m)):
        column = []
        for j in range(len(m[i])):
            column.append(m[j][i])
            
        x = calcAverage(column)
        average.append(x)

    return average

def findMax(arr):

    max = arr[0]
    
    for x in arr:
        if x > max:
            max = x

    return max

            
        
        
    

n = int(input('Введите размер матрицы D: '))
print()

print('Сформированная матрица D:')
print()

D = createMatrix(n)

writeMatrix(D)

x = matrixLoop(D)
print()
print('Средние арифметические значения столбцов матрицы D:')
writeArray(x)
print()
print('Максимальное средние значение матрицы D =', '{:.2f}'.format(findMax(x)))


