import builtins
import pygame
import random
from math import *



pygame.init()
size = [1200, 800]
screen = pygame.display.set_mode(size)
builtins.screen = screen

from planet import *

pygame.display.set_caption('Universe')

background_color = [0,0,0]

dt = 0

x0 = 600
y0 = 400

theta = 0

sun = Planet('Sun', 1, 1, x0, y0, 0, 50, color=0, velocity=0, path_velocity=1)
mars = Planet('Mars', 150, 200, x0, y0-40, 0, 20, path_velocity=1)
earth = Planet('Earth', 100, 120, x0, y0-20, 0, 10, path_velocity=1)
venus = Planet('Earth', 200, 260, x0-50, y0, 0, 25, path_velocity=1)
plooto = Planet('Plooto', 280, 300, x0, y0+35, 0, 35, path_velocity=1)
saturn = Planet('Saturn', 450, 300, x0, y0+50, 0, 50, path_velocity=1)

saturn_sputnik = Planet('Sputnik', 100, 100, x0, y0, 0, 15, path_velocity=1)
saturn_sputnik.velocity = 2
dt = 1

def random_theta():
    return random.randint(1, 2) / random.randint(100, 200)
    
x_coordinates = [random.randint(0,1200) for i in range(1200)]
y_coordinates = [random.randint(0,1000) for i in range(1000)]

saturn_sputnik.path = 0.2

def calc_path(a, b):
    path_x = []
    path_y = []
    t = 0
    while t < 2 * pi:
        normal_x = self.a * cos(t)
        normal_y = self.b * sin(t)

        x = normal_x * cos(theta) - normal_y * sin(theta)
        y = normal_x * sin(theta) + normal_y * cos(theta)

        
        path_x.append(x0 + x)
        path_y.append(y0 + y)

        t += path

def draw(x, y, dt):
    theta = theta 
    normal_x = a * cos(dt*self.velocity)
    normal_y = b * sin(dt*self.velocity)

    x = x0 + normal_x * cos(theta) - normal_y * sin(theta)
    y = y0 + normal_x * sin(theta) + normal_y * cos(theta)
    
    pygame.draw.circle(screen, self.color, (int(x), int(y)), size)

def draw_path(path_velocity):
    theta += path_velocity
    calc_path()
    path_x = path_x
    path_y = path_y
    for i in range(len(path_x)):
        pygame.draw.circle(screen, white_color, (int(path_x[i]), int(path_y[i])), 2)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    dt += 0.05
    dtheta = 0.01

    

    screen.fill(background_color)

    for i in range(1000):
        pygame.draw.circle(screen, [255,255,255],(x_coordinates[i], y_coordinates[i]),1,1)
    for i in range(1200):
        k = random.randint(0,999)
        pygame.draw.circle(screen, [40,40,40],(x_coordinates[k], y_coordinates[k]),1,1)

    x_coordinate = random.randint(800,1600);
    y_coordinate = random.randint(600,1200);
    
    sun.draw_path()
    #sun.theta += random_theta()
    mars.draw_path()
    #mars.theta += random_theta()
    earth.draw_path()
    #earth.theta += random_theta()
    venus.draw_path()
    #venus.theta += random_theta()
    plooto.draw_path()
    #plooto.theta += random_theta()
    saturn.draw_path()
    #saturn.theta += random_theta()

    sun.draw(dt)
    mars.draw(dt)
    #mars.x0 += 1
    #mars.y0 += 1
    earth.draw(dt)
    venus.draw(dt)
    plooto.draw(dt)
    saturn.draw(dt)

    saturn_sputnik.x0 = saturn.x
    saturn_sputnik.y0 = saturn.y
    saturn_sputnik.draw_path()
    saturn_sputnik.draw(dt)

    pygame.display.flip()


pygame.quit()

        
