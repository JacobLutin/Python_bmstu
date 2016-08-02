import pygame

pygame.init()

size = (600, 600)
screen = pygame.display.set_mode(size)



running = True

class Player:

    velocity = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, (0,0,0), (self.x, self.y), 10)

class Breek:

    width = 100
    height = 30

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.alive = True

    def draw(self):
        rect = (self.x, self.y, self.width, self.height)
        pygame.draw.rect(screen, (0, 255, 0), rect)

class Ball

    radius = 30
    self.velocity = 1

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def draw(self):
        pygame.draw.circle(screen, (0, 0, 255), self.radius)



#def draw_field(x, 

player = Player(300, 300)
breek = Breek(100, 100)

while running:

    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                player.x -= player.velocity
            if event.key == pygame.K_d:
                player.x += player.velocity

    screen.fill((255,255,255))
        

    player.draw()

    playe

    breek.draw()

    
    pygame.display.flip()

pygame.quit()
