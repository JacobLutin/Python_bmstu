import pygame
from hexagon import *

pygame.init()
size = (1000, 600)
screen = pygame.display.set_mode(size)
screen_width = size[0]
screen_height = size[1]

running = True



points = []

hexagons = []

#hexagon = Hexagon(screen, 200, 300, 50)

R = 100
r = int(sqrt(3)*R/2)

row = True
xk = 0
yk = 0

for y in range(R, screen_height, int(1.5*R)):
    for x in range(r, screen_width, 2*r):

        if row:
            hexagons.append(Hexagon(screen, x, y, R, xk, yk))
        else:
            hexagons.append(Hexagon(screen, x+r, y, R, xk, yk))

        xk += 1
    yk += 1


    row = not row

x, y = pygame.mouse.get_pos()

while running:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION:
            x, y = pygame.mouse.get_pos()
            #print(pygame.mouse.get_rel())
        if event.type == pygame.MOUSEBUTTONDOWN:
            #print(points)
            points.append(pygame.mouse.get_pos())
            for hexagon in hexagons:                
                hexagon.check_mouse()
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    for point in points:
        pygame.draw.circle(screen, (0, 255, 0), point, 10)

    #x += dx
    #y += dy

    pos = (x, y)

    pygame.draw.circle(screen, (255,0,0), pos, 10)

    for hexagon in hexagons:
        hexagon.draw()
                        
    pygame.display.flip()


pygame.quit()
