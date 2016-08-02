def integralPP(a,b,n,f):
    l = abs(b-a)/n
    xn = a+l
    xk = b
    s = 0
    while xn <= xk:
        s += f(xn)
        xn += l
    return s*l
def integralB(a,b,n,f):
    prov = n % 4
    if prov != 0:
        return 0
    else:
        p = n//4
        x = []
        s = 0
        l = abs(b-a)/(4*p)
        xn = a
        for i in range(p):
            x = []
            for i in range(5):
                x.append(f(xn))
                xn += l
            xn -= l
            s += 2/45*l*(7*x[0]+32*x[1]+12*x[2]+32*x[3]+7*x[4])
            
        return s
def integralEPS(a,b,eps):
    t = 1
    flag = 1
    while flag:
        l = abs(b-a)/t
        xn = a+l
        xk = b
        s = 0
        while xn < xk+l:
            s += round(F(xn),6)
            xn += round(l,6)
        if l<eps:
            flag = 0
        else:
            t*=2
    return t,round(s*l,6)
    
def main():
    print("Подсчет интегралов функции y = x**2 на отрезке [а,b]")
    a = float(input("Введите а: "))
    b = float(input("Введите b: "))
    print("Введите кол-во разбиений n1,n2 ")
    n1 = int(input("Введите n1: "))
    n2 = int(input("Введите n2: "))
    print()
    SB1 = integralB(a,b,n1)
    SB2 = integralB(a,b,n2)
    SP1 = integralPP(a,b,n1)
    SP2 = integralPP(a,b,n2)
    print("Метод      |     n1 =",n1,"   |     n2 =",n2,"  |")
    print("Метод ПП   |{:13.5f}".format(SP1)," |{:13.5f}".format(SP2),"|")
    if SB1 == 0 and SB2 != 0:
        print("Метод Буля |    Ошибка!    |{:13.5f}".format(SB2),"|")
    elif SB1 != 0 and SB2 == 0:
        print("Метод Буля |{:13.5f}".format(SB1)," |     Ошибка!  |")
    elif SB1 == 0 and SB2 == 0:
        print("Метод Буля |    Ошибка!    |    Ошибка!   |")
    else:
        print("Метод Буля |{:13.5f}".format(SB1),"|{:13.5f}".format(SB2)," |")
        
    print()
    eps = float(input("Введите eps: "))
    k,s = integralEPS(a,b,eps)
    print("Количество разбиений:",k)
    print("Интеграл = ",round(s,6))
main()
#print(integralEPS(0,3,0.1))
