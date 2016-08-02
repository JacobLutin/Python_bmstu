from tkinter import *

import tkinter.messagebox as box

window = Tk()
window.title('Вывод сообщений')

def dialog():

    variant = box.askyesno('Блок сообщения', 'Продолжать')

    if variant:
        box.showinfo('Блок Да', 'Продолжение...')
    else:
        box.showwarning('Блок Нет', 'Выход')

btn = Button(window, text='Нажать', command=dialog)

btn.pack(padx=150, pady=50)
window.mainloop()
