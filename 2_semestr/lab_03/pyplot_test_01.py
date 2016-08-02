import matplotlib.pyplot as plt
import numpy as np
from math import *

a = 0
b = 100

x = np.arange(a, b, 0.01)

def f(x):
    return sqrt(x)

fx = [f(i) for i in x]

plt.plot(x, fx, 'k', label='F(x)')

legend = plt.legend(loc='upper center')

plt.subplot().spines['bottom'].set_position('zero')

plt.grid(True)
plt.show()
