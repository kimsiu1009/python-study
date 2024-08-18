import pygame

pygame.init()

screen = pygame.display.set_mode((400, 400))

pygame.display.set_caption("창 크기 조절")
icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()