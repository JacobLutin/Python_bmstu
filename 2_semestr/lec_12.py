from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title('Radio Button пример')

frame = Frame(window)
book = StringVar()
radio_1 = Radiobutton(frame, text='Mark 1', variable=book, value='1952')
radio_2 = Radiobutton(frame, text='Ada', variable=book, value='1970')
radio_3 = Radiobutton(frame, text='Pascal', variable=book, value='1972')
radio_4 = Radiobutton(frame, text='C', variable=book, value='1953')
radio_5 = Radiobutton(frame, text='C++', variable=book, value='1983')
radio_6 = Radiobutton(frame, text='Java', variable=book, value='1995')

radio_1.select()

def dialog():
    box.showinfo('Selection', 'Выбор языка: \n' + book.get())

btn = Button(frame, text='Выбор', command=dialog)

btn.pack(side=RIGHT, padx=5)


radios = [radio_1, radio_2, radio_3, radio_4, radio_5, radio_6]

for radio in radios:
    radio.pack(side=LEFT)

frame.pack(pady=30, padx=30)
window.mainloop()
