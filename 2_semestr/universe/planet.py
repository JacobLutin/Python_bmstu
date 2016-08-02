import builtins
import pygame
import random
from math import *

screen = builtins.screen

white_color = [255, 255, 255]

class Planet:    

    def __init__(self, name, a, b, x0, y0, theta, size, color=False, velocity=False, path_velocity=False, path=False):
        self.name = name
        self.x = 0
        self.y = 0
        self.x0 = x0
        self.y0 = y0
        self.a = a
        self.b = b
        self.size = size
        if color:
            self.color = color
        else:
            self.color = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)]
        if theta:
            self.theta = radians(theta)
        else:
            self.theta = radians(random.randint(0, 360))
        if velocity:
            self.velocity = velocity
        else:
            self.velocity = random.random()
        if path_velocity:
            self.path_velocity = random.randint(1, 2) / random.randint(100, 200)
        else:
            self.path_velocity = path_velocity
        if path:
            self.path = path
        else:
            self.path = 0.1
        self.path_x = []
        self.path_y = []

    def calc_path(self):
        self.path_x = []
        self.path_y = []
        t = 0
        while t < 2 * pi:
            normal_x = self.a * cos(t)
            normal_y = self.b * sin(t)

            x = normal_x * cos(self.theta) - normal_y * sin(self.theta)
            y = normal_x * sin(self.theta) + normal_y * cos(self.theta)

            
            self.path_x.append(self.x0 + x)
            self.path_y.append(self.y0 + y)

            t += self.path

    def draw(self, dt):
        theta = self.theta 
        normal_x = self.a * cos(dt*self.velocity)
        normal_y = self.b * sin(dt*self.velocity)

        self.x = self.x0 + normal_x * cos(theta) - normal_y * sin(theta)
        self.y = self.y0 + normal_x * sin(theta) + normal_y * cos(theta)
        
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.size)

    def draw_path(self):
        self.theta += self.path_velocity
        self.calc_path()
        path_x = self.path_x
        path_y = self.path_y
        for i in range(len(path_x)):
            pygame.draw.circle(screen, white_color, (int(path_x[i]), int(path_y[i])), 2)
        
