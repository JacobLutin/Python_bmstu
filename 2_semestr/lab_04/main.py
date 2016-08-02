import numpy as np
from methods import *
from tests import *
from table import *

import time
import random

def DeltaTime(function, array=None):

    start = time.time()
    function(array)
    dtime = time.time() - start

    return dtime

def getArray(size):
    arr = []
    for i in range(size):
        arr.append(random.randint(-100, 100))

    return arr


def getAdditionalArray(size):

    arr = []
    for i in range(size):
        arr.append([random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100), random.randint(-100, 100)])

    return arr


def PrintArray(array):

    for x in array:
        print('{:.7f}'.format(x))


def Main():

    lengths = [512, 1024, 2048]
    iterations = 3
    results = []

    for i in range(iterations):

        result = []

        for l in lengths:

            arr = getArray(l)

            arr.sort()
            dt = DeltaTime(BubbleSort, arr) * 1000
            result.append(dt)

        for l in lengths:

            arr = getArray(l)

            dt = DeltaTime(BubbleSort, arr) * 1000
            result.append(dt)


        for l in lengths:

            arr = getArray(l)

            arr.sort()
            arr.reverse()
            dt = DeltaTime(BubbleSort, arr) * 1000
            result.append(dt)

        results.append(result)

    print("         Сортировка одномерного массива пузырьком")

    CreateTable(results, iterations)

    results = []

    for i in range(iterations):

        result = []

        for l in lengths:

            arr = getAdditionalArray(l)

            arr.sort()
            dt = DeltaTime(BubbleSort, arr) * 1000
            result.append(dt)

        for l in lengths:

            arr = getAdditionalArray(l)

            dt = DeltaTime(BubbleSort, arr) * 1000
            result.append(dt)


        for l in lengths:

            arr = getAdditionalArray(l)

            arr.sort()
            arr.reverse()
            dt = DeltaTime(BubbleSort, arr) * 1000
            result.append(dt)

        results.append(result)

    print("         Сортировка массива с дополнительной информацией")

    CreateTable(results, iterations)

    print("Размеры массивов: ", lengths[0], lengths[1], lengths[2])
    print("Единица измерения времени - миллисекунды")

Main()
