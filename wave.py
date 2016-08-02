import matplotlib.pyplot as plt
import numpy as np
from math import *


a = 0
b = 2


T = np.arange(a, b, 0.00001)

A = -0.011
beta = 2
omega = 20
omega0 = 20
phi = 25


def x(t):
    #print(cos(radians(omega*t+phi)))
    return (A*exp(-beta*t))*cos((omega*t+radians(phi)))

def set_Xt():
    Xt = []
    for t in T:
        Xt.append(x(t))

    return Xt
    

#Xt = set_Xt()

#plt.plot(T, Xt, 'k')


#omega = 30
#omega = 1
#beta = 1
#A = 4
#phi = 20

Xt1 = set_Xt()
plt.plot(T, Xt1, 'r')

phi = 60
beta = 0.2

#Xt2 = set_Xt()
#plt.plot(T, Xt2, 'y')

#plt.fill_between(T, Xt1, Xt2)




plt.grid(True)
inp = 'true'
plt.show()
    
    
