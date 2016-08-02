import sys
import builtins
import pygame
import random

pygame.init()
width = 600; height = 600
builtins.width = width
builtins.height = height
size = (width, height)
builtins.screen = pygame.display.set_mode(size)

from object import *

background_color = (255, 255, 255)
screen.fill(background_color)

number_of_objects = 20
objects = []

colors = [(255,0,0), (255,255,0), (0,255,0), (0,255,255), (0,0,255), (255, 0, 255)]

for i in range(number_of_objects):


    size = random.randint(10, 40)
    x = random.randint(size, width-size)
    y = random.randint(size, height-size)

    object = Object(x, y, size)
    object.color = random.choice(colors)
    object.speed = random.uniform(1, 2)
    object.angle = random.uniform(0, 2*math.pi)

    objects.append(object)


running = True


while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.fill(background_color)

    for object in objects:

        object.display()
        object.move()
        object.bounce()
        for other_object in objects:
            if object != other_object:
                if object.collide(other_object):
                    objects.pop(objects.index(other_object))

    pygame.display.update()

pygame.quit()
