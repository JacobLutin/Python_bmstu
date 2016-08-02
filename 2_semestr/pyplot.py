import matplotlib.pyplot as plt
import numpy as np


a = 0
b = 10

x = np.arange(a, b, 1)

def f(x):
    return x*x

fx = [f(i) for i in x]

plt.plot(x, fx, 'ro', label='F(x)')

plt.legend(loc='upper center')

plt.subplot().spines['bottom'].set_position('zero')

plt.grid(True)
plt.show()
