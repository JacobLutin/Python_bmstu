from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('listbox test')

frame = Frame(window)

listbox = Listbox(frame)
listbox.insert(1, 'Test 1')
listbox.insert(2, 'Test 2')
listbox.insert(3, 'test 3')

def dialog():
    box.showinfo('your choice ', listbox.get(listbox.curselection()))

btn = Button(frame, text='button', command=dialog)

listbox.pack(side=LEFT)
btn.pack(side=RIGHT)
frame.pack(padx=10,pady=10)
window.mainloop()
