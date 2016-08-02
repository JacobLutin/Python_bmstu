from tkinter import *

import tkinter.messagebox as box

window = Tk()
window.title("Title")

frame = Frame(window)
entry = Entry(frame)


def showDialog():
    box.showinfo("Тест", entry.get())

btn = Button(frame, text="Введите число", command=showDialog)

btn.pack(side=RIGHT, padx=10)
entry.pack(side=LEFT)
frame.pack(padx=30, pady=30)

window.mainloop()



# window = Tk()
# window.title('Виджет Entry')
#
# frame = Frame(window)
# entry = Entry(frame)
#
# def dialog():
#     box.showinfo('Приглашение', 'Сдавать экзамен в сентябре ' + entry.get())
#
#
# btn = Button(frame, text='Введите фамилию', command=dialog)
#
# btn.pack(side=RIGHT, padx=10)
# entry.pack(side=LEFT)
# frame.pack(padx=30, pady=30)
#
# window.mainloop()
