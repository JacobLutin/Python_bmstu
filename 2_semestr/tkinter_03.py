from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('Widget Entry')

frame = Frame(window)

entry = Entry(window)

def dialog():
    box.showinfo('Test dialog', 'Hello! ' + entry.get())

btn = Button(, text='Enter text', command=dialog)

btn.pack(side=RIGHT, padx=20)
entry.pack(side=LEFT)


frame.pack(padx=30, pady=30)
