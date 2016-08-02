from math import *
import numpy as np
import matplotlib as plt


def f(x):
    return x

def fp(x):
    dx = 0.00000001
    return (f(x+dx)-f(x))/ dx

x = 0

while x < 10:
    if x == -y:
        print(x, -x)
    x += 0.01
