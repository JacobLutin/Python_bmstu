from pygame import *


MOVE_SPEED = 10
JUMP_FORCE = 30
WIDTH = 32
HEIGHT = 40
COLOR = "#888888"

GRAVITY = 1.5

class Player(sprite.Sprite):

    def __init__(self, x, y):

        sprite.Sprite.__init__(self)

        self.start_position = (x, y)

        self.x_velocity = 0
        self.y_velocity = 0

        self.image = Surface((WIDTH, HEIGHT))
        self.image.fill(Color(COLOR))

        self.rect = Rect(x, y, WIDTH, HEIGHT)

        self.on_ground = False


    def update(self, left, right, up, platforms):

        if self.on_ground:
            self.y_velocity = 0
        else:
            self.y_velocity += GRAVITY

        if up and self.on_ground:
            self.y_velocity = -JUMP_FORCE

        self.on_ground = False


        if left:
            self.x_velocity = -MOVE_SPEED

        if right:
            self.x_velocity = MOVE_SPEED

        if not(left or right):
            self.x_velocity = 0

        self.rect.x += self.x_velocity
        self.collide(self.x_velocity, 0, platforms)

        self.rect.y += self.y_velocity
        self.collide(0, self.y_velocity, platforms)


    def collide(self, x_velocity, y_velocity, platforms):

        for platform in platforms:
            if sprite.collide_rect(self, platform):

                if x_velocity > 0:
                    self.rect.right = platform.rect.left

                if x_velocity < 0:
                    self.rect.left = platform.rect.right

                if y_velocity > 0:
                    self.rect.bottom = platform.rect.top
                    self.y_velocity = 0
                    self.on_ground = True

                if y_velocity < 0:
                    self.rect.top = platform.rect.bottom
                    self.y_velocity = 0


    # def draw(self, screen):
    #
    #     screen.blit(self.image, (self.rect.x, self.rect.y))




