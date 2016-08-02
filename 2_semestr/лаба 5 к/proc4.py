from proc1 import *
from proc2 import *
from proc3 import *
from mGraph import *

def main4_all_proc(kor = 1 , ex = 1 , per = 1):
    """Главная процедура программы."""
    print('Метод золотого сечения.')
    print('Нахождение корней.')
    #xMas,fMas - хранят список корней координатно
    xMas = []
    fMas = []
    a = float(input('Введите а: '))
    b = float(input('Введите b: '))
    h = float(input('Введите шаг h: '))
    minter = int(input('Введите максимальное кол-во итераций: '))
    eps = float(input('Введите точность eps: '))
    print()                          
    x1 = a
    x2 = a+h
    if kor:
        print('Таблица корней:')
        print('|  №  |    x1    |    x2    |    x     |    f(x)  |  Итерации   \
|  Номер ошибки  |')  
        xMass,fMass,kor = func(x1,x2,h,eps,b,zoloto,minter,f)
        xMas.append(xMass)
        fMas.append(fMass)
        if kor == 0:
            print('                                                      Корней нет.')
    print()
    if ex:
        print('Таблица экстремумов:')
        print('|  №  |    x1    |    x2    |    x     |    f(x)  |  Итерации   \
|  Номер ошибки  |')  
        xMass,fMass,kor = func(x1,x2,h,eps,b,zoloto_ex,minter,fp)
        xMas.append(xMass)
        fMas.append(fMass)
        if kor == 0:
            print('                                                     Точек экстремума нет.')
    print()
    if per:
        print('Таблица перегибов:')
        print('|  №  |    x1    |    x2    |    x     |    f(x)  |  Итерации   \
|  Номер ошибки  |')  
        xMass,fMass,kor = func(x1,x2,h,eps,b,zoloto_per,minter,fpp)
        xMas.append(xMass)
        fMas.append(fMass)
        if kor == 0:
            print('                                                     Точек перегибов нет.')
    print('Номера ошибок:')
    print('0 - ошибок нет.')
    print('1 - превышено число итераций.')
    makeGraph_all(a,b,xMas,fMas,f)
def func(x1,x2,h,eps,b,zoloto,minter,funcc):
    xMas = []
    fMas = []
    k = 1
    kor = 0
    zero = 0
    while x1 < b:
        if x2 > b:
            x2 = b
        if funcc(x2) < eps and funcc(x2) > -1*eps:
            zero = 1     
        xk,inter = zoloto(x1,x2,eps,minter)
        err = 0
        #print(x1,x2,xk,f(xk),inter)
        #if f(xk) > 0 + 2*eps or f(xk) < -2*eps:
            #err = -1
        if funcc(x1) < eps and funcc(x1) > -1*eps and zero == 1:
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
    return xMas,fMas,kor


#main4_all_proc(1,1,1)
