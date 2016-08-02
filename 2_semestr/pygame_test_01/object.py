import builtins
import math
import pygame

screen = builtins.screen
width = builtins.width
height = builtins.height

class Position:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __call__(self):
        return (int(self.x), int(self.y))

class Object:
    def __init__(self, x, y, size):
        self.position = Position(x, y)
        self.size = size
        self.color = (0, 0, 255)
        self.thickness = 1
        self.speed = 2
        self.angle = math.pi

    def display(self):
        pygame.draw.circle(screen, self.color, self.position(), self.size, self.thickness)

    def move(self):
        self.position.x += math.sin(self.angle) * self.speed
        self.position.y -= math.cos(self.angle) * self.speed

    def bounce(self):
        angle = self.angle
        if self.position.x - self.size < 0:
            self.angle = -self.angle

        if self.position.x + self.size > width:
            self.angle = -self.angle

        if self.position.y - self.size < 0:
            self.angle = math.pi/2 + self.angle

        if self.position.y + self.size > height:
            self.angle = math.pi/2 + self.angle

    def collide(self, other_object):
        pos1 = self.position
        pos2 = other_object.position
        if (pos2.x - other_object.size < pos1.x < pos2.x + other_object.size):
            if (pos2.y - other_object.size < pos1.y < pos2.y + other_object.size):
                print('Collide', pos1())
                object = Object(pos1.x, pos1.y, 5)
                object.color = (0, 0, 0)
                object.thickness = 0
                object.display()
                if self.size > other_object.size:
                    self.size += other_object.size
                    return True
                # elif:
                #     self.size < other_object.size:
                #     other.object.sz

        return False




    #def collide(self, other_object):
        #if other_object.x + other_object.size/2 < self.x#

#class Boundary:
#   def init(self, x, y):
