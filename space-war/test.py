import pygame
import random

pygame.init()
background = pygame.display.set_mode((480, 360))
pygame.display.set_caption("Rocket game")

image_pico = pygame.image.load("space-war/images/pico-1.png")
image_Rocket = pygame.image.load("space-war/images/Rocket-1.png")

rect_pico = image_pico.get_rect()
rect_Rocket = image_Rocket.get_rect()

x_pos_pico = 100
y_pos_pico = 100

x_pos_Rocket = 150
y_pos_Rocket = 150

rect_pico.topleft = (x_pos_pico, y_pos_pico)
rect_Rocket.topleft = (x_pos_Rocket, y_pos_Rocket)

play = True
while play:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False

    if rect_Rocket.colliderect(rect_pico):
        print("충돌") 

    background.blit(image_pico, (x_pos_pico, y_pos_pico))
    background.blit(image_Rocket, (x_pos_Rocket, y_pos_Rocket))
    pygame.display.update()
    print("그린다")

pygame.quit()