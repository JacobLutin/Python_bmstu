import pygame
from math import *

def vector(x, y, r, theta=0):
    
    theta = radians(theta)
    
    x = x + cos(theta) * r
    y = y - sin(theta) * r
    
    return (int(x), int(y))

class Hexagon:

    color = (0,0,0)

    def calc_points(self):

        for theta in range(30, 390, 60):
            self.points.append(vector(self.x, self.y, self.r, theta))

        self.points.append(self.points[0])

    def __init__(self, screen, x, y, r, x_pos, y_pos):

        self.screen = screen
        self.x = x
        self.y = y
        self.r = r
        self.x_pos = x_pos
        self.y_pos = y_pos
        #self.inner_r = sqrt(3)*r/2
        self.points = []
        self.selected = False

        self.calc_points()
        print(self.points)


    def draw(self):

        points = self.points

        if self.selected:
            pygame.draw.polygon(self.screen, (255, 0, 255), points)

        for i in range(len(points)-1):
            pygame.draw.line(self.screen, self.color, points[i], points[i+1], 2)
            

    def check_mouse(self):

        mouse_x, mouse_y = pygame.mouse.get_pos()
        if (mouse_x-self.x)**2 + (mouse_y-self.y)**2 < self.r**2:
            print(self.x_pos, self.y_pos)
            self.selected = not self.selected
            
            

        

        
        
