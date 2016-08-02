from tkinter import *
import tkinter.messagebox as box


window = Tk()

numbers = []
s = 0

def add_sum(n):
    s += n
    st = 'Sum = ' + sum
    box.showinfo(st, 'Continue')
    

for i in range(10):
    num_btn = Button(window, text=i, command=add_sum)
    num_btn.pack(padx=20, pady=20)

#label = Label(



        
