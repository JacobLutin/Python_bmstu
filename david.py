import pygame
import numpy as np
from math import *


pygame.init()
size = (800, 500)
screen = pygame.display.set_mode(size)

def vector(x, y, r, theta):
    theta = radians(theta)
    
    x = x + cos(theta) * r
    y = y - sin(theta) * r
    
    return (int(x), int(y))


def draw_cube(x, y, theta):

    start = (int(x), int(y))

    points = []

    for i in range(0, 360, 90):

        end = vector(x, y, r, i+theta)

        points.append(end)

    pygame.draw.polygon(screen, (0, 255, 255), (points[0], start, points[1]))
    pygame.draw.polygon(screen, (255, 0, 255), (points[1], start, points[2]))
    pygame.draw.polygon(screen, (255, 0, 0), (points[2], start, points[3]))
    pygame.draw.polygon(screen, (255, 255, 0), (points[3], start, points[0]))

    """
    pygame.draw.line(screen, (0,0,0), points[0], points[1], width)
    pygame.draw.line(screen, (0,0,0), points[1], points[2], width)
    pygame.draw.line(screen, (0,0,0), points[2], points[3], width)
    pygame.draw.line(screen, (0,0,0), points[3], points[0], width)
    """


def draw_sin():

    x = 0

    while x <= size[0]:
        y = 100 * sin(x/20) + height
        pygame.draw.circle(screen, (0,0,0), (int(x), int(y)), 1)

        x += 0.1
        


#R = 100

R = float(input("Введите длину ребра куба: "))
r = R*sqrt(2)
width = 3

height = size[1]/2
x = 50
theta = 0

running = True

speed = 5

while running:
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    draw_sin()

    x += speed
    
    if x >= 800 or x <= 0:
        speed *= -1
        
    theta += 1
    
    y = 100 * sin(x/20) + height

    draw_cube(x, y, theta)

    pygame.display.flip()

pygame.quit()
