from math import sqrt

def inp():

    points = []

    n = int(input("Введите количество точек A: "))
    print("Введите координаты точек x и у построчно")
    for i in range(n):
        x, y = input().split()
        points.append([int(x), int(y)])

    circles = []

    n = int(input("Введите количество окружностей B:"))
    print("Введите координаты окружностей x и у, а также ее радиус построчно")
    for i in range(n):
        x, y, r = input().split()
        r = int(r)
        while r <= 0:
            print("Введите коректное значение радиуса окружности")
            x, y, r = input().split()
            r = int(r)

        circles.append([int(x), int(y), r])

    return points, circles

def vector(A, B):

    ax, ay = A
    bx, by = B

    return bx - ax, by - by

def lineFunc(p1, p2, x):

    x1, y1 = p1
    x2, y2 = p2

    if x1 == x2:

    
    y = (x1*y2 - x2*y1 + x*(y1-y2))/(x1-x2)

    #print(y)

    return y

def circleFunc(x, ox, oy, r):

    plusY = oy + sqrt(r**2 - (x-ox)**2)
    minusY = oy - sqrt(r**2 - (x-ox)**2)

    #print(plusY, minusY)

    return plusY, minusY

def isIntersect(points, circle):

    ox, oy, r = circle

    for x in range(ox-r, ox+r+1):
        #print(x)
        Y = lineFunc(points[0], points[1], x)
        upY, downY = circleFunc(x, ox, oy, r)

        if upY >= Y >= downY:
            return True

    return False

def test1():

    points = [[1, 2], [4, 4], [7, 6], [-1, 10], [16, 5]]
    circles = [[4, 1, 3], [2, 5, 3], [15, 6, 4]]

    return points, circles

    
def main(test=False):
    
    if not test:
        points, circles = inp()
    else:
        points, circles = test()

    maxPoints = 'Не существует ни одной прямой'
    maxk = 0

    for point1 in points:
        for point2 in points:
            if point1 != point2:
                
                twoPoints = [point1, point2]

                k = 0
                
                for circle in circles:

                    if isIntersect(twoPoints, circle):
                        k += 1
                        #print(True)

                if k > maxk:

                    maxk = k

                    maxPoints = twoPoints

    

    print(maxPoints)
    print('Количество вхождений:', maxk)

main()
        
            
            
        
