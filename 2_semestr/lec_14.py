from tkinter import *
root = Tk()

canv = Canvas(root, width=500, height=500, bg='lightblue', cursor='pencil')

canv.create_line(200, 50, 300, 50, width=3, fill='blue')
canv.create_line(0, 0, 100, 100, width=2, arrow=LAST)

x = 75
y = 110

canv.create_rectangle(x, y, x+80, y+50, fill='white', outline='blue')
canv.create_polygon([250, 100],[200, 150],[300, 150], fill='yellow')


canv.create_polygon([250, 100], [200, 150], [300, 150], fill='yellow')
canv.create_polygon([300, 80], [400, 80], [450, 75], [450, 200],
                    [300, 180], [330, 160],outline="white",smooth=1)

            
canv.pack()
