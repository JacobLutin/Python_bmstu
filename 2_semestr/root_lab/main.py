from math import *

from draw import *
from methods import *
from interface import *
from methods import *
from tests import *

'''
Лабораторная работа по уточнению корней методом секущих
'''

def f(x):
	#return x**3 - 18*x - 83
	return sin(x) + cos(x) * x
        #return sin(x) + cos(2*x)

def fp(x):
	dx = 1e-5
	return (f(x + dx) - f(x)) / dx

def fpp(x):
	dx = 1e-5
	return (fp(x + dx) - fp(x)) / dx

test = False

points = []

print('Лабораторная работа по уточнению корней методом секущих')
print()
    
if not test:
    #x, a, b, h, eps, n = test()

    print("1) Показать на графике корни")
    print("2) Показать на графике экстремумы")
    print("3) Показать на графике точки перегиба")
    print("4) Показать на графике несколько точек")
    print("5) Показать на графике все точки")
    print()

    choice = int(input('   -----> '))
    print()

    if choice == 4:
        s = "Введите одну или несколько цифр через пробел, для вывода точек на графике:"
        print(s)
        print("1) Корни")
        print("2) Экстремумы")
        print("3) Точки перегиба")
        points = input('   -----> ').split()
        points = [ int(x) for x in points]
    elif choice == 5:
    	points = [1, 2, 3]

    a, b, h, eps, n = getParams()
    print()
else:
    choice, a, b, h, eps, n = test()
    if choice == 4:
        points = [1, 2, 3]

pointsNames = []

if choice in [1, 2, 3]:

    points = [choice]

roots = []
exes = []
infp = []

if 1 in points:
    pointsNames.append('roots')
    roots, x, iter, errors = iteration(f, a, b, h, eps, n)
    if f(b) == 0:
        roots.append(b)
        x.append([b, b])
        iter.append(0)
        errors.append(0)
    drawTable(roots, iter, x, errors, f, 'Корни')

if 2 in points:
    pointsNames.append('exes')
    exes, x, iter, errors = iteration(fp, a, b, h, eps, n)
    drawTable(exes, iter, x, errors, f, 'Экстремумы')

if 3 in points:
    pointsNames.append('infp')
    infp, x, iter, errors = iteration(fpp, a, b, h, eps, n)
    drawTable(infp, iter, x, errors, f, 'Точки перегиба')

print("Типы ошибок:")
print('0) - ошибки нет')
print('1) -  превышено число итераций')
print('2) -  нулевая разность f(x0) и f(x1) в формуле уточнения корня')

drawPlot(a, b, f, roots, exes, infp, points=pointsNames)

# a = -10
# b = 10
# h = 1
# eps = 1e-50
# maxiter = 10000

# roots, segments, iterations, errors = iteration(fp, a, b, h, eps, maxiter)

# draw_table(f, roots, segments, iterations, errors)


# x = np.arange(a, b, 0.1)
# y = [f(t) for t in x]

# plt.plot(x, y)
# plt.plot(roots, [f(t) for t in roots], 'ro')

# plt.subplot().spines['bottom'].set_position('zero')
# plt.subplot().spines['left'].set_position('zero')
# plt.grid(True)

# plt.show()
