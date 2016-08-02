import pygame
from pygame import *

from Player import *
from Platform import *



WIN_HEIGHT = 600
WIN_WIDTH = 800


DISPLAY = (WIN_WIDTH, WIN_HEIGHT)

BG_COLOR = "#004400"



def main():



    pygame.init()
    screen = pygame.display.set_mode(DISPLAY)
    pygame.display.set_caption('Super Mario')

    timer = pygame.time.Clock()

    objects = pygame.sprite.Group()

    levels = ["-------------------------",
              "-                       -",
              "-                       -",
              "-                       -",
              "---                  ----",
              "-                       -",
              "-                       -",
              "-     ----              -",
              "-                       -",
              "-              -----    -",
              "-    ----               -",
              "-                       -",
              "-                       -",
              "----                -----",
              "-                       -",
              "-                       -",
              "-    ----      ---      -",
              "-                       -",
              "-------------------------"]

    player = Player(40, 40)
    left = right = up = False

    objects.add(player)

    platforms = []

    x = 0
    y = 0

    for row in levels:
            for col in row:
                if col == "-":
                    platform = Platform(x, y)
                    platforms.append(platform)
                    objects.add(platform)

                x += PLATFORM_WIDTH

            y += PLATFORM_HEIGHT
            x = 0

    running = True

    while running:

        timer.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == KEYDOWN:
                if event.key == K_a:
                    left = True

                if event.key == K_d:
                    right = True

                if event.key == K_w:
                    up = True

            if event.type == KEYUP:
                if event.key == K_a:
                    left = False

                if event.key == K_d:
                    right = False

                if event.key == K_w:
                    up = False

        screen.fill(Color(BG_COLOR))

        player.update(left, right, up, platforms)

        objects.draw(screen)

        pygame.display.update()

        print(objects)

    pygame.quit()



if __name__ == "__main__":
    main()


