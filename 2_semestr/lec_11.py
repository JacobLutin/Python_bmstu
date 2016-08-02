from tkinter import *
import tkinter.messagebox as box


window = Tk()
window.title('Пример на список')

frame = Frame(window)
listbox = Listbox(frame)
listbox.insert(1, 'Python')
listbox.insert(2, 'Java')
listbox.insert(3, 'YashaPidor')
listbox.insert(4, 'Delphi')
listbox.insert(5, 'C')


def dialog():
    box.showinfo('Список для выбора', 'Ваш выбор: ' + \
                 listbox.get(listbox.curselection())) # get(3)


btn = Button(frame, text='Выбор', command=dialog)

btn.pack(side=RIGHT, padx=5)
listbox.pack(side=LEFT)
frame.pack(padx=30, pady=30)
window.mainloop()
