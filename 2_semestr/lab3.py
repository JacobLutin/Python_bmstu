
def inputMatrix(l):

    m = []
    
    for i in range(l):
        arr = input().split(' ')
        m.append(arr)

    return m

def matrixLoop(m):

    l = len(m)

    prmax = 0
    prx = 0
    pry = 0
    
    for i in range(l):
        for j in range(l):
            
            if m[i][j] == 't':
                
                y = i
                x = j
                
                while (x < l-1) and (m[i][x+1] == 't'):
                    x += 1

                while (y < l-1) and (m[y+1][j] == 't'):
                    y += 1

                x += 1
                y += 1
                
                pr = (x - j) * (y - i)
                
                if pr > prmax:
                    
                    prmax = pr

                    prx = j+1
                    pry = i+1

    return pry, prx
                    
"""
L = 5

m = [['t', 'f', 'f', 'f', 'f'],
     ['f', 'f', 'f', 'f', 't'],
     ['f', 't', 't', 'f', 't'],
     ['f', 't', 't', 'f', 'f'],
     ['f', 't', 't', 'f', 'f']]
"""

L = int(input('Введите размер квадратной матрицы Z: '))
print()
print('Задайте матрицу построчно: ')
print()


m = inputMatrix(L)

x, y = matrixLoop(m)

print()

if x == 0 and y == 0:
    print('В данной матрице не существует ни одного значения true')
else:
    print('Ответ:', x, y)
