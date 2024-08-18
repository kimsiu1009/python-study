import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self, size, pos):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill('gray')
        self.rect = self.image.get_rect(topleft = pos)

    def update(self, world_shift):
        # update for camera
        # move the entire map by the variable, world_shift
        self.rect.x += world_shift