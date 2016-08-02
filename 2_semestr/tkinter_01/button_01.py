from tkinter import *

n = 0

def button_clicked():
    #global n
    n += 1
    bg = '#010101'
    button['bg'] = bg
    button['text'] = 'Button was clicked'
    print('Button is clicked', n, 'times!')


root = Tk()
button = Button(root, height=50, width=100, bg="black", fg='red', text='Click_me!', command=button_clicked)
button.pack()
root.mainloop()
