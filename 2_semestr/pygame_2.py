import pygame
import sys

_GRAVITY = 9.8

pygame.init()
size = (500, 500)
screen = pygame.display.set_mode(size)

running = True

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class GameObject:

    def __init__(self, x, y):
        self.position = Position(x, y)

    def move(self)

    


box = GameObject(1, 2)
def drawCircle(pos):
    red = (0,255,0)
    #pos = (100, 100)
    radius = 50
    pygame.draw.circle(screen, red, pos, radius)

def drawHouse(x, y, width, height, screen, color):
    points = [(x,y- ((2/3.0) * height)), (x,y), (x+width,y), (x+width,y-(2/3.0) * height), 
        (x,y- ((2/3.0) * height)), (x + width/2.0,y-height), (x+width,y-(2/3.0)*height)]
    lineThickness = 2
    pygame.draw.lines(screen, color, False, points, lineThickness)

def drawBox(x, y):
    width = 50
    height = 100
    points = (x, y, width, height)
    color = (244,164,96)
    thickness = 1
    pygame.draw.rect(screen, color, points, 0)

while running:

    red = (255,0,0)

    drawCircle((100, 100))
    drawBox(200, 100)
    
    
    event = pygame.event.wait ()
    if event.type == pygame.QUIT:
        running = False  # Be IDLE friendly

    pygame.display.update()


pygame.quit ()

