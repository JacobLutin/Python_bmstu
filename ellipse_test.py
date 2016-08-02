import pygame
from math import *

pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)


def ellipse(x0, y0, w, t, d):

    x = x0*cos(w*t)
    y = y0*cos(w*t+d)

    return (250 + int(x), 250 + int(y))

running = True
a = 100
b = 200
dt = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    pos = ellipse(a, b, 1, dt, pi)
    print(pos)

    pygame.draw.circle(screen, (0,255,0), pos, 10)

    dt += 0.1

    pygame.display.flip()
    


pygame.quit()
