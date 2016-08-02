from tkinter import *
from math import *

root = Tk()

canvas = Canvas(root, width=600, height=600)
canvas.pack()


width = 2
bear_color = "sienna4"

def create_claw(x, y):
    points=[x+430, y+335, x+430, y+310, x+440, y+330]
    canvas.create_polygon(points, fill="white")
    canvas.create_line(points, width=width)

def create_body():
    points = [340, 620, 337, 594, 339, 537, 348, 468, 345, 416, 345, 396, 293, 389, 285, 374, 369, 333, 261, 296]
    points += [220, 230, 289, 228, 309, 191, 361, 182, 423, 180, 423, 162, 443, 142, 495, 154, 467, 198, 515, 223]
    points += [580, 289, 600, 600]

    canvas.create_polygon(points, fill=bear_color, smooth=True)

    points.pop(); points.pop();
    canvas.create_line(points, width=width, smooth=True)
    canvas.create_line(435, 163, 479, 154, 466, 185, width=width, smooth=True)

    canvas.create_rectangle(600, 600, 550, 500, fill='red')
    
    canvas.create_line(475, 471, 428, 328, 476, 306, 531, 407, smooth=True, width=width)
    create_claw(10, 0)
    create_claw(20, -10)
    create_claw(33, -7)

def create_hand(x, y):
    points = [x+475, y+471, x+428, y+328, x+476, y+306, x+531, y+407]
    create_claw(x+10, y+0)
    create_claw(x+20, y-10)
    create_claw(x+33, y-7)
    canvas.create_polygon(points, fill=bear_color, smooth=True)
    #canvas.create_line(points, smooth=True, width=width)
    
def create_ear():
    points = [324, 192, 305, 162, 329, 148, 358, 152, 361, 182, 348, 200]
    canvas.create_oval
    canvas.create_polygon(points, fill=bear_color, smooth=True)
    canvas.create_line(points, smooth=True, width=width)
    canvas.create_line(327, 162, 340, 157, 349, 162, 350, 175, width=width, smooth=True)

def create_eyes():
    canvas.create_oval(312, 212, 325, 225, fill="white", width=width)
    canvas.create_oval(317, 218, 318, 219, fill="black", width=width)

    canvas.create_oval(369, 221, 385, 235, fill="white", width=width)
    canvas.create_oval(375, 228, 377, 230, fill="black", width=width)

def create_mouth():
    points = [261, 296, 268, 278, 309, 292, 341, 302, 351, 296, 374, 298, 392, 295, 295, 378, 285, 366]
    canvas.create_polygon(points, fill="red", smooth=True)
    canvas.create_polygon(261, 296, 305, 340, 285, 366, 329, 350, 289, 302, fill="red")
    canvas.create_line(points, smooth=True, width=width)
    points = [261, 296, 305, 341, 281, 372]
    canvas.create_polygon(points, fill="medium sea green")

def create_nose():
    points = [235, 254, 232, 244, 232, 240, 232, 237, 234, 235, 246, 230, 270, 225, 270, 245]
    canvas.create_polygon(points, fill="black", smooth=True)

def create_bush():
    canvas.create_rectangle(0, 0, 600, 600, fill="sea green")
    points =[600, 600, 600, 96, 198, 39, 107, 210, 117, 356, 88, 600]
    canvas.create_polygon(points, fill="medium sea green", smooth=True)

    points=[600, 600, 600, 96, 400, 96, 38, 600]
    canvas.create_polygon(points, fill="medium sea green")

def create_teeth(x, y):
    points = [x+308, y+360, x+307, y+340, x+319, y+356]
    canvas.create_polygon(points, fill="white")
    canvas.create_line(points, width=width)

def create_teeth_top(x, y):
    points = [x+282, y+282, x+287, y+302, x+301, y+288]
    canvas.create_polygon(points, fill="white")
    canvas.create_line(points, width=width)

def create_leaves_1():
    points = [497, 600, 421, 557, 469, 551]
    points += [441, 494, 525, 465, 527, 430, 571, 428, 530, 360]
    points += [565, 355, 535, 325, 560, 289, 520, 258, 600, 240, 600, 600]
    canvas.create_polygon(points, fill="dark green")
    canvas.create_line(points, width=width)

def create_tree():
    points=[0, 0, 0, 600, 60, 600, 60, 270, 120, 270, 120, 250, 60, 250, 60, 0, 0, 0]
    canvas.create_polygon(points, fill="saddle brown")
    canvas.create_line(points, width=width)

def create_honey():
    points = [120, 190, 210, 330]
    canvas.create_oval(points, fill="gold")
    canvas.create_line(120, 260, 165, 280, 210, 260, width=width, smooth=True)
    canvas.create_line(125, 230, 165, 250, 205, 230, width=width, smooth=True)
    canvas.create_line(130, 214, 165, 230, 200, 214, width=width, smooth=True)
    canvas.create_line(125, 290, 165, 310, 205, 290, width=width, smooth=True)
    canvas.create_line(130, 306, 165, 330, 200, 306, width=width, smooth=True)
    canvas.create_oval(155, 260, 175, 280, fill="black")

def create_vetka():
    canvas.create_line(60, 50, 160, 60, width=width)
    
    canvas.create_line(160, 60, 220, 80, width=width)
    canvas.create_line(160, 60, 200, 45, width=width)

    #canvas.create_oval(points, fill="black")
    
    # canvas.create_oval([312, 212, 325, 225], points, fill="white", width=width)


create_bush()
create_ear()
create_hand(-140, 100)
create_body()
create_leaves_1()
create_mouth()
create_teeth(0, 0)
create_teeth(23, -13)
create_teeth(45, -35)
create_teeth_top(0, 0)
create_teeth_top(30, 10)
create_eyes()
create_nose()
create_tree()
create_vetka()
create_honey()


mainloop()
