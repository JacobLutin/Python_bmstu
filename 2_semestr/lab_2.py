from math import acos, sqrt, degrees

#Проверка на колинеарность двух векторов
def isColinear(v1, v2):

    if cross(v1, v2) == 0:
        return True

    return False

#Проверка пересечения двух векторов
def isIntersect(A, B, C, D):

    ax1, ay1 = A
    ax2, ay2 = B
    bx1, by1 = C
    bx2, by2 = D
    
    v1 = (bx2 - bx1)*(ay1 - by1) - (by2 - by1)*(ax1 - bx1)
    v2 = (bx2 - bx1)*(ay2 - by1) - (by2 - by1)*(ax2 - bx1)
    v3 = (ax2 - ax1)*(by1 - ay1) - (ay2 - ay1)*(bx1 - ax1)
    v4 = (ax2 - ax1)*(by2 - ay1) - (ay2 - ay1)*(bx2 - ax1)
    
    return (v1*v2 < 0) and (v3*v4 < 0)

#Функция проверяющая, можно ли составить
#из четыре точек выпуклый четырехугольник 
def isQuadr(A, B, C, D):

    if isColinear(vector(A, B), vector(B, C)):
        return False

    if isColinear(vector(B, C), vector(C, D)):
        return False

    if isColinear(vector(C, D), vector(D, A)):
        return False

    if isIntersect(A, B, C, D) or isIntersect(B, C, A, D):
        return False

    if not isIntersect(A, C, B, D):
        return False

    return True
    
    
#Подсчет угла между двумя векторами
def calcAngle(v1, v2):
    
    ax, ay = v1
    bx, by = v2

    #print(v1, v2)
    
    angle = abs(ax * bx + ay * by) / (sqrt(ax**2 + ay**2) * sqrt(bx**2 + by**2))
    return degrees(acos(angle))

#Нахождение разницы углов
def deltaAngle(deg):
    deg2 = 180 - deg

    return(abs(deg-deg2))

#Преобразование двух точек в вектор
def vector(a, b):
    
    ax, ay = a
    bx, by = b
    
    ab = [bx - ax, by - ay]

    return ab

#Векторное произведение векторов
def cross(a, b):

    ax, ay = a
    bx, by = b

    return ax * by - ay * bx

#Вывод ответа
def output(maxAngle, quadr, maxAngle1, maxAngle2):
    print()
    if quadr:
        print("Четырехугольник построен на точках: ", quadr[0], quadr[1], quadr[2], quadr[3])
        print("Углы пересчения диагоналей четырехугольника составляют", end=' ')
        print("{:.2f}".format(maxAngle1), "и", "{:.2f}".format(maxAngle2), 'градусов')
        print("Разница этих углов составляет", "{:.2f}".format(maxAngle))
    else:
        print("На заданных точках четырехугольник построить невозможно")

def inp():

    n = int(input("Введите количество точек для построения четырехугольника: "))

    if n < 4:
        print("Недостаточно точек для построения четырехугольника")
        return False

    print("Введите координаты x и у каждой точки, построчно")

    points = []

    for i in range(n):
        p = input().split()
        p = [int(x) for x in p]
        points.append(p)
        
    return points


def main(test=0):

    maxAngle = -1

    if test != 0:
        points = test()
    else:
        points = inp()

    if not points:
        return 0

    quadrs = []
    quadr = []

    for p1 in points:
        for p2 in points:
            if p1 != p2:
                for p3 in points:
                    if p3 != p1 and p3 != p2:
                        for p4 in points:
                            if p4 != p3 and p4 != p2 and p4 != p1:
                                if isQuadr(p1, p2, p3, p4):
                                    arr = [p1, p2, p3, p4]
                                    quadrs.append(arr)
    newquadrs = []

    for i in quadrs:
        if i not in newquadrs:
            newquadrs.append(i)

    maxAngle1 = 0
    maxAngle2 = 0

    for point in newquadrs:
        A = point[0]; B = point[1]; C = point[2]; D = point[3];
        x = calcAngle(vector(A, C), vector(B, D))
        if deltaAngle(x) > maxAngle:
            maxAngle1 = x
            maxAngle2 = 180 - x
            maxAngle = deltaAngle(x)
            quadr = [A, B, C, D]
            #print(quadr)
            #print(x)
            

    output(maxAngle, quadr, maxAngle1, maxAngle2)

def test1():
    return [[1, 4], [4, 6], [8, 6], [4, 1], [7, 8], [1, 3]]

def test2():
    return  [[0, 0], [1, 1]]


main()
