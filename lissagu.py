import pygame
from math import *

pygame.init()
size = (600,600)
screen = pygame.display.set_mode(size)

def rotate(x0, y0, theta, x_center, y_center):

    theta = radians(theta)
    x = x0*cos(theta) - y0*sin(theta) + x_center
    y = x0*sin(theta) + y0*cos(theta) + y_center

    return x, y

def lissagu_figure(A, alpha, beta, delta, x0, y0, dt):

    theta = dt * 1000
    t = 0
    points = []

    while t < 2*pi:
        t += 0.001

        x = A * sin(alpha*t + radians(delta))
        y = A * cos(beta*t)
        x, y = rotate(x, y, theta, x0, y0)        
    
        pygame.draw.circle(screen, (0,0,0), (int(x), int(y)), 5)
        points.append((int(x), int(y)))

    x = A * sin(alpha*dt + radians(delta)) + x0
    y = A * cos(beta*dt) + y0

    pygame.draw.polygon(screen, (0,0,255), points)

    pygame.draw.circle(screen, (255,0,0), (int(x), int(y)), 10)


dt = 0
A = 200

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    dt += 0.001
    
    #alpha =  5 + dt*10
    #beta =   7 + dt*7.5
    #delta = 50 + dt*100

    

    alpha = 1
    beta = 3
    delta = dt*100
    
    #delta = dt*1000
    
    lissagu_figure(A, alpha, beta, delta, 300, 300, 0)
    #print(delta)
    #print(alpha, beta, delta)

    
    

    pygame.display.flip()

pygame.quit()
