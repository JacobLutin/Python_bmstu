from tkinter import *
import tkinter.messagebox as box

window = Tk()
window.title('radios')

frame = Frame(window)

book = StringVar()

radio_1 = Radiobutton(frame, text='radio_1', variable=book, value='test1')
radio_2 = Radiobutton(frame, text='radio_2', variable=book, value='test2')
radio_3 = Radiobutton(frame, text='radio_3', variable=book, value='test3')
radio_4 = Radiobutton(frame, text='radio_4', variable=book, value='test4')

frame_1 = Frame(window)


var_1 = IntVar()
var_2 = IntVar()


r1 = Checkbutton(frame_1, text='r1', variable=var_1, onvalue=1, offvalue=0)
r2 = Checkbutton(frame_1, text='r2', variable=var_2, onvalue=1, offvalue=0)
r1.select()

radio_1.select()

def dialog():

    box.showinfo('Answer', 0)


radios = [radio_1, radio_2, radio_3, radio_4]

for radio in radios:
    radio.pack(padx=10, side=LEFT)



btn = Button(frame, text='button', command=dialog)

btn.pack(padx=10,pady=10)

frame.pack(padx=10,pady=10)

r1.pack()
r2.pack()

frame_1.pack()

window.mainloop()
