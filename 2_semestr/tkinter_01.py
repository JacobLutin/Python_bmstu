from tkinter import *

window = Tk()
window.title('button test')

btn_end = Button(window, text='exit button', command=exit)
label = Label(text='test')

def toggle():
    if window.cget('bg') == 'green':
        window.configure(bg = 'blue')
    else:
        window.configure(bg = 'green')

btn_toggle = Button(window, text='toggle button', command=toggle)

btn_toggle.pack(padx=100, pady=10)
btn_end.pack(padx=100, pady=10)
label.pack(padx=50, pady=10)

window.mainloop
