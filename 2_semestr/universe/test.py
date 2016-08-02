import builtins
import pygame
import random
from math import *

pygame.init()
size = [600, 600]
screen = pygame.display.set_mode(size)

pygame.display.set_caption('test')

background_color = [0,0,0]

running = True

wheel_x = 300
wheel_y = 300

x = wheel_x + 100
y = wheel_y + 100

dt = 0

a = 100

center_x = 300
center_y = 300

x1 = 200
y1 = 200

def revert(x, y, dt):
    
    x = x * cos(dt) - y * sin(dt)
    y = x * sin(dt) + y * cos(dt)

    return x, y

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    dt += 0.1

    x1 = 50 + a*cos(dt)
    y1 = 50 + a*sin(dt)

    x1, y1 = revert(x1, y1, dt)

    start_pos = (100, 100)
    end_pos = (int(x1), int(y1))

    pygame.draw.circle(screen, [100,100,100], end_pos, 100)
    print(x1, y1)

    x, y = revert(x, y, dt)

    start_pos = (int(wheel_x), int(wheel_y))
    end_pos = (int(x), int(y))

    #pygame.draw.line(screen, [255,255,255], start_pos, end_pos, 5)  

    pygame.display.flip()


pygame.quit()
