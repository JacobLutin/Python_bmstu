"""

Уточнение корней методом золотого сечения

"""

from math import *
import numpy as np
import matplotlib as plt
from draw import *
from tests import *
from methods import *
from interface import *

def main(test=False):
    
    def f(x):
        return x**2 - 4

    def g(x):
        return cos(x)

    def d(x):
        return f(x) - g(x)

    functions = [f, g, d]

    menu(functions, test)


main()

