from tkinter import *
import tkinter.messagebox as box
window = Tk()
window.title('Виджет Checkbutton: ')


frame = Frame(window)
var_1 = IntVar()
var_2 = IntVar()
var_3 = IntVar()
var_4 = IntVar()
#var_5 = IntVar()

langs = [['Fortran', var_1, '1954'],
         ['Basic', var_2, '1964'],
         ['Ada', var_3, '1488'],
         ['Python', var_4, '1234']]

books = []

for lang in langs:
    book = Checkbutton(frame, text=lang[0], variable=lang[1], onvalue=1, offvalue=0)
    books.append(book)


def dialog():
    str = 'Выбор языка: '
    for lang in langs:
        if lang[1].get == 1: str += '/' + lang[2]
