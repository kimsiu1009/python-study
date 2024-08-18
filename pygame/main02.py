# pygame의 window 크기를 가져오기

import pygame

pygame.init()

screen = pygame.display.set_mode()
x, y = screen.get_size()

pygame.display.quit()
print(x, y)