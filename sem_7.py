"""

На плоскости заданы точки (N точек) найти максимально удаленную
от начала координат точку и минимально отдаленную точку из верхней полуплоскости
Далее найти расстояние между двумя найденными точками
Начальное значение числами не задавать

"""

from math import sqrt

points = []

while True:
    array = input().split()
    if array != []:
        array = [int(x) for x in array]
        points.append(array)
    else:
        break

def point_length(point):
    return(sqrt(point[0]**2 + point[1]**2))

def two_points_length(point1, point2):
    return(sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2))

def min_max(points):
    i = -1
    max_point_length = point_length(points[0])
    max_point = 0
    min_point_length = point_length(points[0])
    min_point = 0
    for point in points:
        i += 1
        length = point_length(point)
        if length > max_point_length:
            max_point = i
            max_point_length = length
        if length < min_point_length:
            min_point = i
            min_point_length = length

    return(min_point, max_point)

lengths = []

for point in points:
    lengths.append(point_length(point))
    
print(lengths)

min_point, max_point = min_max(points)

lenght_between_points = two_points_length(points[min_point], points[max_point])

print("Расстояние до наименее удаленной точки: ", points[min_point])
print("Расстояние до наиболее удаленной точки[max_point)

print(lenght_between_points)
