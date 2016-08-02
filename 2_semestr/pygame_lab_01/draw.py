import builtins
import pygame
from math import *

screen = builtins.screen
screen_width = builtins.screen_width
screen_height = builtins.screen_height

background_color = builtins.background_color
sky_color = builtins.sky_color
white_color = builtins.white_color
mountain_color = builtins.mountain_color
ship_color = builtins.ship_color
red_color = builtins.red_color

sky_height = 400


def draw_sky(sky_color):

    pygame.draw.rect(screen, sky_color, (0, 0, screen_width, sky_height))


sun_radius = 60
sun_width = 10
sun_len = 100
sun_len1 = 70

def draw_sun(x, y):
    x = int(x)
    y = int(y)

    pos = (x, y)
    pygame.draw.circle(screen, sun_color, pos, sun_radius)
    
    pygame.draw.line(screen, sun_color, pos, (x, y-sun_len), sun_width)
    pygame.draw.line(screen, sun_color, pos, (x, y+sun_len), sun_width)
    pygame.draw.line(screen, sun_color, pos, (x-sun_len, y), sun_width)
    pygame.draw.line(screen, sun_color, pos, (x+sun_len, y), sun_width)

    pygame.draw.line(screen, sun_color, pos, (x-sun_len1, y-sun_len1), sun_width)
    pygame.draw.line(screen, sun_color, pos, (x+sun_len1, y-sun_len1), sun_width)
    pygame.draw.line(screen, sun_color, pos, (x+sun_len1, y+sun_len1), sun_width)
    pygame.draw.line(screen, sun_color, pos, (x-sun_len1, y+sun_len1), sun_width)


def draw_wave(x, y, l):
    h = 0.5
    i = 0
    while i < l:
        x += h
        y += cos(i/2)
        pos = (int(x), int(y))
        pygame.draw.circle(screen, white_color, pos, 1)
        i += h

def draw_mountain_1(x, y):
    points = [(x, y), (x+100, y-200), (x+200, y)]
    pygame.draw.lines(screen, [0, 0, 0], True, points, 5)
    pygame.draw.polygon(screen, mountain_color, points)

    points = [(x+70, y-140), (x+100, y-200), (x+130, y-140)]
    pygame.draw.polygon(screen, white_color, points)
    draw_wave(x+72, y-141, 56)

def draw_mountain_2(x, y):
    points = [(x, y), (x+150, y-300), (x+300, y)]
    pygame.draw.lines(screen, [0, 0, 0], True, points, 5)
    pygame.draw.polygon(screen, mountain_color, points)

    points = [(x+100, y-200), (x+150, y-300), (x+200, y-200)]
    pygame.draw.polygon(screen, white_color, points)
    draw_wave(x+102, y-200, 95)

def draw_ship(x, y):

    points = [(x, y), (x-30, y-30), (x+150, y-30), (x+120,y)]
    pygame.draw.polygon(screen, ship_color, points)
    pygame.draw.lines(screen, [0, 0, 0], True, points, 5)

    points = [(x+60,y-30), (x+60,y-100)]
    pygame.draw.lines(screen, [0,0,0], True, points, 5)

    points = [(x+60,y-100), (x+90, y-80), (x+60,y-60)]
    pygame.draw.lines(screen, [0,0,0], True, points, 10)
    pygame.draw.polygon(screen, red_color, points)
