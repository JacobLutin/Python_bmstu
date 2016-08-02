import pygame

pygame.init()

size = (500, 500)

screen = pygame.display.set_mode(size)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((252, 56, 75))

    pygame.draw.line(screen, (0, 0, 0), (0, 0), (200, 100), 10)
    pygame.draw.rect(screen, (65, 64, 24), (100, 100, 100, 100), 10)
    
    pygame.display.flip()

pygame.quit()
