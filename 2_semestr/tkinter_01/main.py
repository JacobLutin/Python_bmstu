from tkinter import *

n = 0

def button_clicked():
    global n
    n += 1
    print('Button is clicked', n, 'times!')


root = Tk()
button1 = Button(root, bg='red', text='Click_me!', command=button_clicked)
button1.pack()
root.mainloop()
