from proc1 import *
from proc2 import *
from mGraph import *

def fpp(x):
    """Вторая производная."""
    dX = 0.001
    pr = (fp(x+dX)-fp(x))/dX
    return pr


def zoloto_per(x1 = 0, x2 = 0, eps = 0,interMax = 0):
    """Возвращает корень и кол-во итераций."""
    #Проверяет являются ли границы отрезков корнями
    if fpp(x1) == 0 or fpp(x2) == 0:
        if fpp(x1) == 0:
            return x1,0
        if fpp(x2) == 0:
            return x2,0
    else:
        t = (sqrt(5) - 1) / 2
        t = round(t,6)
        x3 = x1 + (1 - t) * (x2 - x1)
        x4 = x1 + t * (x2 - x1)
        inter = 0
        #Проверяет есть ли в производной функции корни
        if not((fpp(x1) > 0) and (fpp(x2) > 0) or (fpp(x1) < 0) and (fpp(x2) < 0)):
            while abs(x1-x2) > eps:
                if inter < interMax:
                    if abs(fpp(x3)) > abs(fpp(x4)):
                        x1 = x3
                    else:
                        x2 = x4
                else:
                    break
                x3 = x1 + (1 - t) * (x2 - x1)
                x4 = x1 + t * (x2 - x1)
                inter += 1
            return x3,inter
        else:
            return None,None

        
def main3_peregib():
    """Главная процедура программы."""
    print('Метод золотого сечения.')
    print('Нахождение точек перегиба.')
    #xMas,fMas - хранят список экстремумов координатно
    xMas = []
    fMas = []
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    h = float(input('Введите шаг h: '))
    minter = int(input('Введите максимальное кол-во итераций: '))
    eps = float(input('Введите точность eps: '))
    print()
    print('|  №  |    x1    |    x2    |    x     |    f(x)  |  Итерации   \
|  Номер ошибки  |')                            
    x1 = a
    x2 = a+h
    k = 1
    kor = 0
    zero = 0
    #Цикл разбиения отрезка по h
    while x1 < b:
        if x2 > b:
            x2 = b
        if fpp(x2) == 0:
            zero = 1
        xk,inter = zoloto_per(x1,x2,eps,minter)
        err = 0
        #print(x1,x2,xk,f(xk),inter)
        #if f(xk) > 0 + 2*eps or f(xk) < -2*eps:
            #err = -1
        if fpp(x1) == 0 and zero == 1:
            xk = None
        #Проверка на ошибку по максимальному кол-ву интераций
        if inter != None:
            if inter > minter:
                err = 1
        #Проверка на наличие корня
        if xk != None:
            kor += 1
            table(k,x1,x2,xk,inter,err,eps)
        if xk != None:
            #Запись координаты корня для отображения в графике
            xMas.append(xk)
            fMas.append(f(xk))
        x1 , x2 = x2 , x2 + h
        if xk != None: 
            k += 1
    #Условие проверки на наличие корней
    if kor == 0:
        print('                Точек перегиба нет.')
    else:
        print('Типы ошибок: ')
        print('0 - все отлично.')
        print('1 - превышено кол-во итераций.')
    makeGraph(a,b,xMas,fMas,f)


#main3_peregib()
