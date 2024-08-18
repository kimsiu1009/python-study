import pygame
from sys import exit
from settings import *
from level import Level

pygame.init()

screen = pygame.display.set_mode((1200, 700))
clock = pygame.time.Clock()

level = Level(level_map, screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.fill('black')
    level.run()

    pygame.display.update()
    clock.tick(60)