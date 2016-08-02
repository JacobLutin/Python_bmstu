import builtins
import pygame
from math import *
from colors import *


pygame.init()

#background_color = builtins.background_color

builtins.screen_width = 1000
builtins.screen_height = 600

screen_width = builtins.screen_width
screen_height = builtins.screen_height

size = [screen_width, screen_height]
builtins.screen = pygame.display.set_mode(size)
screen = builtins.screen
    
print(builtins.screen)
from draw import *

running = True

sun_x = -30
sun_y = 250

ship_x = 100
ship_y = 500

dt = 0

sky_color = builtins.sky_color

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(background_color)

    dt += 0.03

    

    draw_sky(sky_color)
    
    sun_x += 10
    
    if sun_x < screen_width/2:
        #sun_y -= 2
        sky_color[1] = sky_color[1] + 4
        sky_color[2] = sky_color[2] + 4
    else:
        #sun_y += 2
        if sky_color[2] >= 4:
            sky_color[1] = sky_color[1] - 4
            sky_color[2] = sky_color[2] - 4

    if sun_x > screen_width+30:
        dt = 0
        sun_x = -30
        sky_color = builtins.sky_color

    sun_y = 300 - 200*sin(dt)
    #print(dt)
    #print(-20*sin(dt))
    
    draw_sun(sun_x, sun_y)  

    draw_wave(500, 500, 100)
    draw_wave(300, 550, 100)
    draw_wave(850, 500, 100)
    draw_wave(700, 520, 100)
    draw_wave(200, 450, 100)
    draw_wave(50, 530, 100)

    draw_mountain_1(300, 397)
    draw_mountain_2(400, 397)
    
    ship_x += 5
    ship_y += cos(dt)*2
    draw_ship(ship_x, ship_y)

    if ship_x > screen_width+20:
        ship_x = -120

    pygame.display.flip()
    
pygame.quit()
