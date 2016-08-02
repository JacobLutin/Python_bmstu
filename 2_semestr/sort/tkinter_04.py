from tkinter import *
import tkinter.messagebox as box
import time 
import numpy as np

window = Tk()


entry = Entry(window)

def get_array():
    
    st = entry.get()

    if st != ' ' or st != '':
        arr = st.split()
        arr = [int(i) for i in arr]
        return arr
    else:
        return False
def shaker_sort(A):

    left = 0
    right = len(A) - 1

    while left <= right:

        for i in range(left, right, +1):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]

        right -= 1

        for i in range(right, left, -1):
            if A[i] < A[i-1]:
                A[i], A[i-1] = A[i-1], A[i]

        left += 1

    return A

def deltatime(arr):

    start = time.time()
    shaker_sort(arr)
    dt = time.time() - start

    return dt

def sort_arr():

    if get_array():
        arr = get_array()
        sorted_arr = shaker_sort(arr)
        box.showinfo('Результат', arr)
        box.showinfo('Время работы', "{:5f}".format(deltatime(arr)) + ' милисекунд')
    else:
        box.showinfo('Ошибка', 'Массив не был введен')




btn = Button(window, text='sort', command=sort_arr)


entry.pack(padx=10, pady=10, side=LEFT)
btn.pack(padx=10, pady=10, side=LEFT)
