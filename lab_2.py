from math import acos, sqrt, degrees


def isColinear(v1, v2):

    if cross(v1, v2) == 0:
        return True

    return False




def isQuadr(A, B, C, D):

    if isColinear(vector(A, B), vector(B, C)):
        return False

    if isColinear(vector(B, C), vector(C, D)):
        return False

    if isColinear(vector(C, D), vector(D, A)):
        return False

    return True
    
    

def calcAngle(v1, v2):
    
    ax, ay = v1
    bx, by = v2

    print(v1, v2)
    
    angle = acos(abs(ax * bx + ay * by) / (sqrt(ax**2 + ay**2) + sqrt(bx**2 + by**2)))

    return degrees(angle)


def vector(a, b):
    
    ax, ay = a
    bx, by = b
    
    ab = [bx - ax, by - ay]

    return ab

def cross(a, b):

    ax, ay = a
    bx, by = b

    return ax * by - ay * bx

A = [2.5, 5]
B = [4, 1]
C = [1, 1]
D = [1, 3.5]

#A = [1, 1]
#B = [1, 3]
#C = [1, 6]
#D = [5, 1]

points = [[2.5, 5], [4, 1], [1, 1], [1, 3.5], [4, 3.5]]
points = [[0, 0], [0, 0], [0, 1], [1, 1]]

for p1 in points:
    for p2 in points:
        if p1 != p2:
            for p3 in points:
                if p3 != p1 and p3 != p2:
                    for p4 in points:
                        if p4 != p3 and p4 != p2 and p4 != p1:
                            print(isQuadr(p1, p2, p3, p4))
