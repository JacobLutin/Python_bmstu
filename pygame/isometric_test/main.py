import pygame
from pygame import *

WIN_WIDTH = 800
WIN_HEIGHT = 600
DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

BG_COLOR = "#567888"

TILE_WIDTH = 32
TILE_HEIGHT = 16

def main():

    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)

    running = True

    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(Color(BG_COLOR))

        pygame.display.update()


    pygame.quit()

if __name__ == "__main__":
    main()