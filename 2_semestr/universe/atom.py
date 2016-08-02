import builtins
import pygame
import random
from math import *



pygame.init()
size = [600, 600]
screen = pygame.display.set_mode(size)
builtins.screen = screen

from planet import *

pygame.display.set_caption('Atom')

background_color = [0,0,0]

dt = 0

x0 = 300
y0 = 300

#theta = pi/4

velocity = 0.5

particle_1 = Planet('particle', 200, 75, x0, y0, 30, 10, color=[252, 64, 52], velocity=velocity, path_velocity=0)
particle_2 = Planet('particle', 200, 75, x0, y0, 90, 10, color=[252, 64, 52], velocity=velocity, path_velocity=0)
particle_3 = Planet('particle', 200, 75, x0, y0, 150, 10, color=[252, 64, 52], velocity=velocity, path_velocity=0)

particle_11 = Planet('particle', 200, 75, x0, y0, 210,  10, color=[252, 64, 52], velocity=velocity, path_velocity=0)
particle_22 = Planet('particle', 200, 75, x0, y0, 270,  10, color=[252, 64, 52], velocity=velocity, path_velocity=0)
particle_33 = Planet('particle', 200, 75, x0, y0, 330,  10, color=[252, 64, 52], velocity=velocity, path_velocity=0)

particle_4 = Planet('particle', 20, 10, x0, y0, 60,  10, color=[252, 64, 52], velocity=velocity, path_velocity=0)
particle_5 = Planet('particle', 10, 20, x0, y0, 120,  10, color=[0, 0, 255], velocity=velocity, path_velocity=0)
particle_6 = Planet('particle', 20, 10, x0, y0, 180,  10, color=[252, 64, 52], velocity=velocity, path_velocity=0)
particle_7 = Planet('particle', 10, 20, x0, y0, 240,  10, color=[0, 0, 255], velocity=velocity, path_velocity=0)

dt = 1

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

    

    screen.fill(background_color)

    
    particle_1.draw_path()
    particle_2.draw_path()
    particle_3.draw_path()

    particle_1.draw(dt)
    particle_2.draw(dt)
    particle_3.draw(dt)

    particle_11.draw(dt)
    particle_22.draw(dt)
    particle_33.draw(dt)
    

    particle_4.draw(dt)
    #particle_4.draw_path()

    particle_5.draw(dt)
    #particle_5.draw_path()

    particle_6.draw(dt)
    #particle_6.draw_path()

    particle_7.draw(dt)
    #particle_7.draw_path()
    

    #theta += 0.1    

    pygame.display.flip()
    #clock.tick(0)


pygame.quit()
        
