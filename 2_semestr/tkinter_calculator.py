from tkinter import *
import tkinter.messagebox as box


window = Tk()
window.title('Calculator')

def add_sum():
    sum = 0

sum = 0
book = StringVar()
btn_num_1 = Button(window, text='1', variable=book, value=1, command=add_sum)
btn_num_2 = Button(window, text='2', variable=book, value=2, command=add_sum)
btn_num_3 = Button(window, text='3', variable=book, value=3, command=add_sum)
