from tkinter import *

window = Tk()

frame = Frame(window, padx=200, height=400)



numButtons = []

for i in range(1, 10):
    numButton = Button(frame, width=20, pady=20, text=i)
    numButton.pack()
    numButtons.append(numButton)

frame.pack()


window.mainloop()
