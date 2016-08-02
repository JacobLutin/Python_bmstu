import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt


def fLinespace(ln,func):
    """Создает массив y для построения графика."""
    mas = []
    for i in ln:
        mas.append(func(i))
    return mas

    
def makeGraph(a,b,xMas,fMas,func):
    """Строит график."""
    #Строит список иксов на интервале [a,b]
    ls = np.linspace(a,b,num = round(b - a) * 100)
    #Строит график f(x)
    plt.plot(ls,fLinespace(ls,func),xMas,fMas,'ro')
    plt.grid(True)
    plt.show()

    
def makeGraph_all(a,b,xMas,fMas,func):
    colors = ['red','green','blue']
    ls = np.linspace(a,b,num = round(b - a) * 100)
    plt.plot(ls,fLinespace(ls,func))
    for i in range(len(xMas)):
        plt.plot(xMas[i],fMas[i],'ro',color = colors[i])
    plt.grid(True)
    plt.show()


def fLinespacee(ln,func):
    """Создает массив y для построения графика."""
    mas = []
    for i in ln:
        mas.append(func(i))
    return np.array(mas)


def makeGraph_sqr(a,b,xMas,fMas,func1,func2):
    ls = np.arange(a,b,round(b - a) / 1000)
    x = ls
    x1 = xMas[0]
    x2 = xMas[len(xMas)-1]
    flag1 = 1
    flag2 = 1
    i = 0
    while i < len(x):
        flag3 = 1
        if x[i] >= x1 and flag1 == 1:
            x = x[i:]
            flag1 = 0
            i = -1
            flag3 = 2
        if x[i] >= x2 and flag2 == 1 and flag3 != 2:
            print(i)
            x = x[:i]
            flag2 = 0
        i += 1
##    print(ls)
##    print(x)
    plt.plot(ls,fLinespace(ls,func1))
    plt.plot(ls,fLinespace(ls,func2))
    plt.plot(xMas,fMas,'ro',color = 'red')
    y1 = fLinespacee(x,func1)
    y2 = fLinespacee(x,func2)
    plt.plot(x, y1, x, y2, color='black')
    plt.fill_between(x, y1, y2, where=y2 >= y1, facecolor='green', interpolate=True)
    plt.fill_between(x, y1, y2, where=y2 <= y1, facecolor='red', interpolate=True)
    plt.grid(True)
    plt.show()
    
