from tkinter import *
import tkinter.messagebox as box

window = Tk()
#window.co

def dialog():

    answer = box.askyesno('Test', 'ARe you sure')

    if answer:
        box.showinfo('Hello', entry.get())
    else:
        box.showwarning('Error', 'sorry')


entry = Entry(window, text='Enter name')
btn = Button(window, text='test', command=dialog)


entry.pack(padx=10, pady=10)
btn.pack(padx=10,pady=10)

window.mainloop()
