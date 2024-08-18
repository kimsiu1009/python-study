# images 사용하기

import pygame

pygame.init()
screen = pygame.display.set_mode((500, 500))
images1 = pygame.image.load("images/img0.gif")
images2 = pygame.image.load("images/img0.gif")
screen.blit(images1, (0, 0))
screen.blit(images1, (300, 300))

pygame.display.flip()
running = True
color = "red"
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()