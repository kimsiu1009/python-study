# pygame의 window 크기를 가져오기

import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
x, y = screen.get_size()

pygame.display.quit()

print(x, y)