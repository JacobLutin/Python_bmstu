from tkinter import *

window = Tk()
window.title('Button Example')

btn_end = Button(window, text = 'выход', command=exit)

def tog():
    if window.cget('bg') == 'green':
        window.configure(bg = 'yellow')
    elif window.cget('bg') == 'yellow':
        window.configure(bg = 'blue')
    elif window.cget('bg') == 'blue':
        window.configure(bg = 'red')
    else:
        window.configure(bg = 'green')

btn_tog = Button(window, text = 'нажать', command=tog)

btn_end.pack(padx = 150, pady = 20)
btn_tog.pack(padx = 150, pady = 20, side=RIGHT)

window.mainloop
