from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('test')

def dialog1():
    box.showinfo('answer', var1.get()+var2.get()+var3.get())

def dialog2():
    box.showinfo('answer2', book.get())

frame = Frame(window)

var1 = IntVar()
var2 = IntVar()
var3 = IntVar()

check1 = Checkbutton(frame, text='check1', variable=var1, onvalue=1, offvalue=0)
check2 = Checkbutton(frame, text='check2', variable=var2, onvalue=1, offvalue=0)
check3 = Checkbutton(frame, text='check3', variable=var3, onvalue=1, offvalue=0)

btn1 = Button(frame, text='button1', command=dialog1)

check1.pack(padx=10, side=LEFT)
check2.pack(padx=10, side=LEFT)
check3.pack(padx=10, side=LEFT)
btn1.pack()

book = StringVar()

radio1 = Radiobutton(frame, text='radio1', variable=book, value='answer1')
radio2 = Radiobutton(frame, text='radio2', variable=book, value='answer2')
radio3 = Radiobutton(frame, text='radio2', variable=book, value='answer3')
radio1.select()

btn2 = Button(frame, text='button2', command=dialog2)

radio1.pack(side=LEFT)
radio2.pack(side=LEFT)
radio3.pack(side=LEFT)

btn2.pack()

frame.pack(padx=10,pady=10)
