import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        self.image = pygame.Surface((32, 64))
        self.image.fill('lightgreen')
        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0, 0)      # a 2-dimensional vector
        self.player_speed = 8
        self.gravity = 1.4
        self.jump_speed = -16

    def get_input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]: self.direction.x = 1
        elif keys[pygame.K_LEFT]: self.direction.x = -1
        else: self.direction.x = 0

        if keys[pygame.K_SPACE]: self.jump()

    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        self.direction.y = self.jump_speed

    def update(self):
        self.get_input()