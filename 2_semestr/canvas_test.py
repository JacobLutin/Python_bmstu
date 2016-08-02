from tkinter import *

window = Tk()
window.title('canvas')

canvas = Canvas(window, height=500, width=500, bg='blue')

canvas.create_line(0, 0, 200, 200, 300, 200, fill='white', width=5)

canvas.pack()
window.mainloop()
